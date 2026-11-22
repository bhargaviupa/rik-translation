#!/usr/bin/env python3
"""Index the Wikisource Ṛgveda pages (refs/wikisource/raw/, from ws_pull.py) into one searchable SQLite file.

    python3 tools/rv/ws_index.py build            # raw wikitext → refs/wikisource/index/ws.sqlite (+ checks.tsv)
    python3 tools/rv/ws_index.py get M.S[.R[.P]]  # print one record as JSON (a sūkta, a Ṛk, or one bhāṣya paragraph)
    python3 tools/rv/ws_index.py search TEXT [--layer L] [--limit N]   # TEXT in Devanagari or IAST; accents and spacing ignored
    python3 tools/rv/ws_index.py stats

REFERENCE POINTS (one scheme for all volumes; M = maṇḍala, S = sūkta, R = Ṛk, P = paragraph of Sāyaṇa's text):
  M.S          the sūkta: header (ṛṣi, devatā/chandas note, previous/next), Sāyaṇa's introduction, extras
  M.S.R        the Ṛk: layers samhita (plain), samhita_acc (accented), pada_acc, pada, bhashya (all paragraphs of
               its section), each with an IAST twin (iast_*); English is added later as layer `english`
  M.S.R.P      one paragraph of Sāyaṇa's bhāṣya, as the page has it (R = 0: the introduction before Ṛk 1)
A volume can pick any layers per Ṛk: `get 1.137.2` returns them all, the caller chooses.

TABLES  sukta · rik · para · extra · meta. Every Devanagari column has a `*_s` twin with accents, quotation marks,
danda, digits and spacing removed (used by `search`). Nothing is corrected; markup of the wiki ([[links]], '''bold''',
HTML tags) is removed and nothing else is changed. What is not understood is kept in `extra` or listed in `checks.tsv`.
`para.prelude` = 1 where the paragraph is not the first of its Ṛk and states a ritual use (सूत्रितं, इत्येषा …): Sāyaṇa
puts that before the NEXT Ṛk, which the page prints at the end of the previous one. It is a hint, not a decision.
"""
import json, pathlib, re, sqlite3, sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
RAW = ROOT / 'refs' / 'wikisource' / 'raw'
OUT = ROOT / 'refs' / 'wikisource' / 'index'
DB = OUT / 'ws.sqlite'
sys.path.insert(0, str(ROOT / 'publish' / 'tools' / 'translit'))
DEV = str.maketrans('०१२३४५६७८९', '0123456789')
ACC = re.compile('[॒॑॓॔᳐-᳿]')
MARK = re.compile(r'[॥।]+\s*([०-९0-9]+)\s*[॥।]*\s*$')
USE = re.compile('सूत्रितं|इत्येषा|इत्यृच|सवने|शस्त्रे|याज्या|पशौ|प्रस्थित|षष्ठेऽहनि|सोमातिरेके')


def iast(s):
    from add_iast import deva_to_iast
    return deva_to_iast(s)


def squash(s):
    """Devanagari (or IAST) reduced for searching: no accents, quotes, danda, digits, spaces, avagraha; nasals unified."""
    s = ACC.sub('', s).replace('ॐ', '')
    s = re.sub('[ङञणनम]्(?=[क-ह])', 'ं', s)
    return re.sub(r'[\s।॥ऽ\-\'"“”‘’()\[\]०-९0-9.,;:|‖*]', '', s)


LAT = re.compile('[^a-zāīūṛṝḷḹṅñṭḍṇśṣṃḥ]')


def isq(s):
    """IAST of Devanagari text reduced to its letters, for searching."""
    return LAT.sub('', iast(s).lower().replace('ṁ', 'ṃ')) if s else ''


def unwiki(t):
    t = re.sub(r'\[https?://\S+\s+([^\]]*)\]', r'\1', t)          # external link: keep its text (reference numbers are linked)
    t = re.sub(r'\[\[(?:[^\]|]*\|)?([^\]]*)\]\]', r'\1', t)
    t = re.sub(r"'''?", '', t)
    t = re.sub(r'<br\s*/?>', '\n', t)
    t = re.sub(r'</?(?:span|poem|big|small|b|i|div|center|nowiki)[^>]*>', '', t)
    return t


def template_spans(t):
    """[(start, end)] of top-level {{ … }} templates."""
    spans, depth, st = [], 0, 0
    i = 0
    while i < len(t) - 1:
        two = t[i:i + 2]
        if two == '{{':
            if depth == 0: st = i
            depth += 1; i += 2
        elif two == '}}' and depth:
            depth -= 1; i += 2
            if depth == 0: spans.append((st, i))
        else:
            i += 1
    return spans


def parse_sukta(m, s, wt):
    chk, extras = [], []
    spans = template_spans(wt)
    hdr, bh, body_parts, last = {}, None, [], 0
    for a, b in spans:
        tpl = wt[a:b]
        nm = re.match(r'\{\{+\s*([^|\n}]+)', tpl)
        name = nm.group(1).strip() if nm else '(unnamed)'
        if name == 'header':
            for k, v in re.findall(r'^\s*\|\s*(\w+)\s*=(.*)$', tpl, flags=re.M): hdr[k] = unwiki(v).strip()
        elif name == 'सायणभाष्यम्':
            bh = tpl[tpl.index('|') + 1:-2]
        elif re.fullmatch(r'ऋग्वेदः मण्डल [०-९]+', name):
            pass
        else:
            extras.append((name, unwiki(tpl)))
        body_parts.append(wt[last:a]); last = b
    body_parts.append(wt[last:])
    rest = ''.join(body_parts)
    cats = re.findall(r'\[\[(?:Category|वर्गः|श्रेणी):[^\]]*\]\]', rest)
    for c in cats: extras.append(('category', c))
    # plain Saṃhitā: lines of the poem block, grouped at ॥N॥
    pm = re.search(r'<poem[^>]*>(.*?)</poem>', rest, flags=re.S)
    plain, buf = [], []
    for line in unwiki(pm.group(1) if pm else '').split('\n'):
        line = line.strip()
        if not line: continue
        buf.append(line)
        if re.search(r'[॥।]+\s*[०-९0-9]+\s*[॥।]+\s*$', line):
            plain.append('\n'.join(buf)); buf = []
    if buf: chk.append(f'plain Saṃhitā: {len(buf)} lines after the last Ṛk end')
    if not pm: chk.append('no <poem> block')
    paras = []
    if bh is not None:
        for line in unwiki(bh).split('\n'):
            if line.strip(): paras.append(line.strip())
    else:
        chk.append('no सायणभाष्यम् template')
    def mk(i):
        mm = MARK.search(paras[i]); return int(mm.group(1).translate(DEV)) if mm else None
    riks, i = [], 0
    while i < len(paras):
        l = paras[i]
        if mk(i) is not None and ACC.search(l) and ' । ' not in l and len(l) < 300:
            n, a = mk(i), i
            b = next((j for j in range(a + 1, min(a + 6, len(paras))) if mk(j) == n and ACC.search(paras[j])), None)
            c = next((j for j in range(b + 1, min(b + 6, len(paras))) if mk(j) == n and not ACC.search(paras[j])), None) if b else None
            if b is None or c is None:
                chk.append(f'Ṛk {n}: Pada lines not found after paragraph {a}'); i += 1; continue
            st = a
            while st - 1 >= 0 and ACC.search(paras[st - 1]) and ' । ' not in paras[st - 1] and len(paras[st - 1]) < 200 \
                    and mk(st - 1) is None and (not riks or st - 1 > riks[-1]['c']):
                st -= 1
            riks.append({'n': n, 'a0': st, 'a': a, 'b': b, 'c': c}); i = c + 1
        else:
            i += 1
    out = []
    first = riks[0]['a0'] if riks else len(paras)
    intro = paras[:first]
    for j, r in enumerate(riks):
        nxt = riks[j + 1]['a0'] if j + 1 < len(riks) else len(paras)
        out.append({'n': r['n'], 'samhita_acc': '\n'.join(paras[r['a0']:r['a'] + 1]), 'pada_acc': '\n'.join(paras[r['a'] + 1:r['b'] + 1]),
                    'pada': '\n'.join(paras[r['b'] + 1:r['c'] + 1]), 'paras': paras[r['c'] + 1:nxt]})
    # checks
    if [r['n'] for r in out] != list(range(1, len(out) + 1)): chk.append(f'Ṛk numbers {[r["n"] for r in out]}')
    if plain and len(plain) != len(out): chk.append(f'{len(plain)} plain Ṛks, {len(out)} Ṛks with Pada and bhāṣya')
    for r, pl in zip(out, plain):
        if squash(pl) != squash(r['samhita_acc']):
            chk.append(f'Ṛk {r["n"]}: accented Saṃhitā differs from the plain Saṃhitā of the page (spelling of nasals/sandhi)')
    for r in out:
        if not r['paras']: chk.append(f'Ṛk {r["n"]}: no bhāṣya paragraph')
    return hdr, plain, intro, out, extras, chk


SCHEMA = '''
CREATE TABLE meta(k TEXT PRIMARY KEY, v TEXT);
CREATE TABLE sukta(ref TEXT PRIMARY KEY, m INT, s INT, title TEXT, revid INT, timestamp TEXT, fetched TEXT,
  rishi TEXT, note TEXT, prev TEXT, next TEXT, n_rik INT, n_plain INT, layout TEXT, has_bhashya INT, intro TEXT, intro_i TEXT);
CREATE TABLE rik(ref TEXT PRIMARY KEY, m INT, s INT, r INT, samhita TEXT, samhita_acc TEXT, pada_acc TEXT, pada TEXT,
  samhita_i TEXT, pada_i TEXT, n_para INT, has_sayana INT);
CREATE TABLE para(ref TEXT PRIMARY KEY, m INT, s INT, r INT, p INT, deva TEXT, iast_s TEXT, prelude INT);
CREATE TABLE extra(m INT, s INT, kind TEXT, text TEXT);
CREATE INDEX rik_ms ON rik(m, s); CREATE INDEX para_ms ON para(m, s, r);
'''


def build():
    OUT.mkdir(parents=True, exist_ok=True)
    if DB.exists(): DB.unlink()
    con = sqlite3.connect(DB)
    con.executescript(SCHEMA)
    checks, ns = [], 0
    other = {}
    for f in sorted(RAW.glob('*.jsonl')):
        for line in f.read_text(encoding='utf-8').splitlines():
            r = json.loads(line)
            mm = re.fullmatch(r'ऋग्वेदः सूक्तं ([०-९]+)\.([०-९]+)', r['title'])
            if not mm:
                other[r['title']] = r; continue
            m, s = int(mm.group(1).translate(DEV)), int(mm.group(2).translate(DEV))
            hdr, plain, intro, riks, extras, chk = parse_sukta(m, s, r['wikitext'])
            for c in chk: checks.append((f'{m}.{s}', c))
            ns += 1
            if riks:
                intro_list = intro
            else:                                     # no per-Ṛk structure on the page: all of Sāyaṇa's text stays together under Ṛk 0
                intro_list = [x for x in intro]
            intro_t = '\n'.join(intro_list)
            nplain = len(plain)
            layout = ('none' if not intro_list and not riks else 'running' if not riks else
                      'per-rik' if len(riks) == nplain else 'partial')
            con.execute('INSERT INTO sukta VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',
                        (f'{m}.{s}', m, s, r['title'], r['revid'], r['timestamp'], r['fetched'], hdr.get('author', ''), hdr.get('notes', ''),
                         re.sub(r'\s+', ' ', hdr.get('previous', '')), re.sub(r'\s+', ' ', hdr.get('next', '')), len(riks), nplain, layout,
                         int(bool(riks or intro_list)), intro_t, isq(intro_t)))
            byn = {rk['n']: rk for rk in riks}
            for n in sorted(set(byn) | set(range(1, nplain + 1))):
                rk = byn.get(n)
                pl = plain[n - 1] if n - 1 < nplain else ''
                paras_n = rk['paras'] if rk else []
                sa, pa, pd = (rk['samhita_acc'], rk['pada_acc'], rk['pada']) if rk else ('', '', '')
                bh = '\n'.join(paras_n)
                con.execute('INSERT INTO rik VALUES (?,?,?,?,?,?,?,?,?,?,?,?)',
                            (f'{m}.{s}.{n}', m, s, n, pl, sa, pa, pd, isq(sa or pl), isq(pd), len(paras_n), int(rk is not None)))
                for p, tx in enumerate(paras_n, 1):
                    con.execute('INSERT INTO para VALUES (?,?,?,?,?,?,?,?)',
                                (f'{m}.{s}.{n}.{p}', m, s, n, p, tx, isq(tx), int(p > 1 and bool(USE.search(tx)))))
            for p, tx in enumerate(intro_list, 1):
                con.execute('INSERT INTO para VALUES (?,?,?,?,?,?,?,?)', (f'{m}.{s}.0.{p}', m, s, 0, p, tx, isq(tx), 0))
            for kind, t in extras:
                con.execute('INSERT INTO extra VALUES (?,?,?,?)', (m, s, kind, t))
    for t, r in other.items():
        con.execute('INSERT INTO extra VALUES (?,?,?,?)', (0, 0, 'page:' + t, unwiki(r['wikitext'])))
    con.execute('INSERT INTO meta VALUES (?,?)', ('built_from', str(len(list(RAW.glob("*.jsonl")))) + ' raw files'))
    con.commit()
    (OUT / 'checks.tsv').write_text('sūkta\tcheck\n' + ''.join(f'{a}\t{b}\n' for a, b in checks), encoding='utf-8')
    stats(con)
    print(f'{len(checks)} checks open, listed in {OUT.relative_to(ROOT)}/checks.tsv')


def stats(con=None):
    con = con or sqlite3.connect(DB)
    q = lambda x: con.execute(x).fetchone()[0]
    print(f'{q("select count(*) from sukta")} sūktas, {q("select count(*) from rik")} Ṛks with Sāyaṇa, '
          f'{q("select count(*) from para")} bhāṣya paragraphs, {q("select count(*) from extra")} extras; '
          f'sūktas without bhāṣya: {q("select count(*) from sukta where has_bhashya=0")}')
    print('  layouts:', dict(con.execute('select layout, count(*) from sukta group by layout').fetchall()))
    print(f'  Ṛks (plain Saṃhitā): {q("select count(*) from rik")}; with Pada and Sāyaṇa split by Ṛk: {q("select sum(has_sayana) from rik")}')
    for m, n, k, kk in con.execute('select m, count(*), sum(n_plain), sum(n_rik) from sukta group by m order by m'):
        print(f'  maṇḍala {m}: {n} sūktas, {k} Ṛks, {kk} with Sāyaṇa split by Ṛk')


def get(ref):
    con = sqlite3.connect(DB); con.row_factory = sqlite3.Row
    parts = ref.split('.')
    tab = {2: 'sukta', 3: 'rik', 4: 'para'}.get(len(parts))
    row = con.execute(f'select * from {tab} where ref=?', (ref,)).fetchone() if tab else None
    if not row: sys.exit(f'no record {ref}')
    d = {k: row[k] for k in row.keys() if not (k.endswith('_s') or k.endswith('_i'))}
    for k in ('samhita', 'samhita_acc', 'pada', 'bhashya', 'deva', 'intro'):
        if d.get(k):
            d['iast_' + k] = iast(d[k].replace('ऽ', '-') if k == 'pada' else d[k])
    if tab == 'sukta':
        d['riks'] = [r[0] for r in con.execute('select ref from rik where m=? and s=? order by r', (parts[0], parts[1]))]
        d['extras'] = [dict(x) for x in con.execute('select kind,text from extra where m=? and s=?', (parts[0], parts[1]))]
    if tab == 'rik':
        ps = con.execute('select ref, deva from para where m=? and s=? and r=? order by p', (parts[0], parts[1], parts[2])).fetchall()
        d['paras'] = [x[0] for x in ps]
        d['bhashya'] = '\n'.join(x[1] for x in ps)
        d['iast_bhashya'] = iast(d['bhashya']) if ps else ''
    print(json.dumps(d, ensure_ascii=False, indent=1))


def search(text, layer='bhashya', limit=20):
    """Substring search; accents, spacing and punctuation ignored. Devanagari or IAST (diacritics needed in IAST)."""
    con = sqlite3.connect(DB)
    dev = bool(re.search('[\u0900-\u097F]', text))
    needle = squash(text) if dev else LAT.sub('', text.lower().replace('ṁ', 'ṃ'))
    tab, dc, ic = {'bhashya': ('para', 'deva', 'iast_s'), 'samhita': ('rik', 'samhita', 'samhita_i'),
                   'pada': ('rik', 'pada', 'pada_i'), 'intro': ('sukta', 'intro', 'intro_i')}[layer]
    n = 0
    if dev:
        rows = ((r, d) for r, d in con.execute(f'select ref, {dc} from {tab} order by m, s, ref') if needle in squash(d or ''))
    else:
        rows = con.execute(f'select ref, {dc} from {tab} where instr({ic}, ?) > 0 order by m, s', (needle,))
    for ref, d in rows:
        print(f'{ref}\t{d.strip().replace(chr(10), " ")[:160]}'); n += 1
        if n >= limit: break
    print(f'-- {n} shown (layer {layer}; more with --limit)')


def main(a):
    if not a: sys.exit(__doc__)
    if a[0] == 'build': build()
    elif a[0] == 'stats': stats()
    elif a[0] == 'get' and len(a) > 1: get(a[1])
    elif a[0] == 'search' and len(a) > 1:
        layer = a[a.index('--layer') + 1] if '--layer' in a else 'bhashya'
        lim = int(a[a.index('--limit') + 1]) if '--limit' in a else 20
        search(a[1], layer, lim)
    else: sys.exit(__doc__)


if __name__ == '__main__':
    main(sys.argv[1:])
