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

HOW THE PAGES ARE READ. Ṛks are found from the page's own plain Saṃhitā (the <poem> blocks): Ṛk n has k lines there, and
the template holds its accented Saṃhitā, accented Pada and plain Pada, k lines each (some pages give the Saṃhitā of several
Ṛks first, then Pada pairs; some lack the accented Pada). When that fails a second reader goes by the shape of the lines.
`rik.bh_at` = the Ṛk whose section holds Sāyaṇa's text for this Ṛk (Sāyaṇa often comments on two or three Ṛks together; the
text stands after the last of them). Footnotes (<ref>) become a marker [१] in the paragraph and a row in `extra`. A second
template name, भाष्यम्, holds Sāyaṇa for the Vālakhilya sūktas (8.49–8.59) and some extra blocks. `sukta.layout` = per-rik
or partial (some Ṛk could not be placed: 10.27 Ṛk 1, whose first accented Pada line is missing on the page).

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
    hdr, bh, bh_alt, body_parts, last = {}, None, None, [], 0
    for a, b in spans:
        tpl = wt[a:b]
        nm = re.match(r'\{\{+\s*([^|\n}]+)', tpl)
        name = nm.group(1).strip() if nm else '(unnamed)'
        if name == 'header':
            for k, v in re.findall(r'^\s*\|\s*(\w+)\s*=(.*)$', tpl, flags=re.M): hdr[k] = unwiki(v).strip()
        elif name == 'सायणभाष्यम्':
            bh = tpl[tpl.index('|') + 1:-2]
        elif name == 'भाष्यम्':
            bh_alt = tpl[tpl.index('|') + 1:-2]                 # Sāyaṇa under another template name (the Vālakhilya sūktas)
            extras.append((name, unwiki(tpl)))
        elif re.fullmatch(r'ऋग्वेदः मण्डल [०-९]+', name):
            pass
        else:
            extras.append((name, unwiki(tpl)))
        body_parts.append(wt[last:a]); last = b
    body_parts.append(wt[last:])
    if bh is None and bh_alt is not None:
        bh = bh_alt; extras[:] = [x for x in extras if x[0] != 'भाष्यम्']; chk.append('info: Sāyaṇa is under the template भाष्यम् (running text)')
    rest = ''.join(body_parts)
    cats = re.findall(r'\[\[(?:Category|वर्गः|श्रेणी):[^\]]*\]\]', rest)
    for c in cats: extras.append(('category', c))
    # plain Saṃhitā: every <poem> block of the page, lines grouped at ॥N॥ (the last group may lack its mark)
    pms = re.findall(r'<poem[^>]*>(.*?)</poem>', rest, flags=re.S)
    plain, buf = [], []
    for line in unwiki('\n'.join(pms)).split('\n'):
        line = line.strip()
        if not line: continue
        buf.append(line)
        mm = list(re.finditer(r'[॥।]+\s*[०-९0-9]+\s*[॥।]+', line))
        if mm and len(line) - mm[-1].end() <= 45:                 # closing ॥N॥, possibly followed by a mark like * or a short note
            plain.append('\n'.join(buf)); buf = []
    if buf and re.search('[॥।]', ' '.join(buf)):
        plain.append('\n'.join(buf)); chk.append(f'plain Saṃhitā: the last Ṛk ({len(plain)}) has no closing number; taken as a Ṛk')
    elif buf:
        chk.append(f'info: text after the last Ṛk of the plain Saṃhitā ignored: {" ".join(buf)[:40]!r}')
    if not pms: chk.append('no <poem> block')
    paras = []
    if bh is not None:
        fn = []
        def _fn(mm):
            fn.append(unwiki(mm.group(1)).strip())
            return '[' + str(len(fn)).translate(str.maketrans('0123456789', '०१२३४५६७८९')) + ']'
        bh = re.sub(r'<ref>(.*?)</ref>', _fn, bh, flags=re.S)          # footnotes: a marker [१] in the text, the note in `extra`
        for k_, f_ in enumerate(fn, 1): extras.append((f'footnote {k_}', f_))
        for line in unwiki(bh).split('\n'):
            if re.fullmatch(r'[A-Za-z ]+', line.strip() or '-'):
                chk.append(f'info: editor label {line.strip()!r} dropped (the raw text keeps it)'); continue
            if len(line.strip()) <= 3 and not re.search('[॥।]|[०-९0-9]', line):
                if line.strip(): chk.append(f'info: stray fragment line {line.strip()!r} dropped (the raw text keeps it)')
                continue
            if line.strip(): paras.append(line.strip())
    else:
        chk.append('no सायणभाष्यम् template')
    def mk(i):
        mm = MARK.search(paras[i]); return int(mm.group(1).translate(DEV)) if mm else None
    def kind(i):
        l = paras[i]
        if ACC.search(l) and len(l) < 500:
            return 'PA' if re.search(r'।\s+[^\s॥।]', l) else 'S'      # a danda between words: a Pada line
        return 'O'
    def dcount(l): return l.replace('।।', '॥').count('।')
    def like_pada(x, y):
        """paragraph x (no accents) is the plain twin of the accented Pada line y: same words, about as long, same danda count"""
        a, b = paras[x], paras[y]
        return (kind(x) == 'O' and 0.45 * len(b) <= len(a) <= 1.1 * len(b)
                and dcount(a) >= max(1, 0.6 * dcount(b)) and dcount(a) <= 1.5 * dcount(b) + 1)
    def find_old():
        """Ṛks found by the shape of the lines: accented Saṃhitā run, accented Pada run, plain Pada lines."""
        riks, i, last_n = [], 0, 0
        notes = []
        while i < len(paras):
            if kind(i) == 'S' and (i == 0 or kind(i - 1) != 'S'):
                j = i
                while j < len(paras) and kind(j) == 'S': j += 1
                k = j
                while k < len(paras) and kind(k) == 'PA' and k - j < j - i: k += 1       # as many Pada lines as Saṃhitā lines
                while k < len(paras) and kind(k) == 'PA' and len(ACC.findall(paras[k])) >= 0.05 * len(paras[k]):   # more only if clearly accented
                    k += 1
                pa = list(range(j, k))
                ok, plain_ix = False, []
                if pa:
                    tot_len = sum(len(paras[y]) for y in pa); tot_d = sum(dcount(paras[y]) for y in pa)
                    x, acc_d, acc_len = k, 0, 0
                    while x < len(paras) and acc_d < 0.85 * tot_d and len(paras[x]) < 500 and '।' in paras[x]:
                        plain_ix.append(x); acc_d += dcount(paras[x]); acc_len += len(paras[x]); x += 1
                    ok = bool(plain_ix) and 0.4 * tot_len <= acc_len <= 1.15 * tot_len and acc_d <= 1.3 * tot_d + 1
                if not ok:
                    notes.append(f'Ṛk after Ṛk {last_n}: Saṃhitā at paragraph {i}, its Pada lines not recognised'); i = j; continue
                n = next((mk(x) for x in (j - 1, k - 1, plain_ix[-1]) if mk(x) is not None), None)
                if n is None: n = last_n + 1
                if n != last_n + 1: notes.append(f'Ṛk number {n} follows {last_n}')
                riks.append({'n': n, 'a0': i, 'a': j - 1, 'b': k - 1, 'c': plain_ix[-1]}); last_n = n; i = plain_ix[-1] + 1
            else:
                i += 1
        return riks, notes

    def find_anchored():
        """Ṛks found by the plain Saṃhitā of the page. Ṛk n has k lines there; on the page come its accented Saṃhitā,
        accented Pada and plain Pada, k lines each. Some pages put the Saṃhitā of several Ṛks first and then
        (accented Pada, plain Pada) for each of them, or give no accented Pada; both are tried."""
        import difflib
        riks, pos, notes, n0 = [], 0, [], 1
        dups = set()
        L = [len(pl.split('\n')) for pl in plain]
        acc = lambda x: bool(ACC.search(paras[x]))
        light = lambda x: len(ACC.findall(paras[x])) <= 3 or len(ACC.findall(paras[x])) < 0.08 * len(paras[x])
        def attempt(q, m):
            ks = L[n0 - 1:n0 - 1 + m]
            K = sum(ks)
            if len(ks) < m or q + K > len(paras) or not all(acc(x) for x in range(q, q + K)): return None
            items, p2, s_off = [], q + K, q
            for idx, k in enumerate(ks):
                sl = '\n'.join(paras[s_off:s_off + k])
                if difflib.SequenceMatcher(None, squash(sl), squash(plain[n0 - 1 + idx]), autojunk=False).ratio() < 0.8: return None
                s = (s_off, s_off + k); s_off += k
                if p2 + 2 * k <= len(paras) and all(acc(x) for x in range(p2, p2 + k)) and all(light(x) for x in range(p2 + k, p2 + 2 * k)):
                    pa, pl = (p2, p2 + k), (p2 + k, p2 + 2 * k); p2 += 2 * k
                elif p2 + k <= len(paras) and all(not acc(x) for x in range(p2, p2 + k)) and idx == 0 and m == 1:
                    pa, pl = (p2, p2), (p2, p2 + k); p2 += k
                else:
                    return None
                items.append({'n': n0 + idx, 's': s, 'pa': pa, 'pl': pl})
            return items, p2
        while n0 <= len(plain):
            hit = None
            for q in range(pos, len(paras)):
                if not acc(q): continue
                if (q + 1 < len(paras) and acc(q + 1) and len(paras[q]) > 20 and
                        difflib.SequenceMatcher(None, squash(paras[q]), squash(paras[q + 1]), autojunk=False).ratio() >= 0.9):
                    dups.add(q); continue                    # a line printed twice: the first copy is set aside
                for m in range(1, 7):
                    r = attempt(q, m)
                    if r: hit = r; break
                if hit: break
            if not hit:
                notes.append(f'Ṛk {n0}: not found by its plain Saṃhitā'); n0 += 1; continue
            items, pos = hit
            riks += items; n0 += len(items)
        for q in sorted(dups):
            if q < pos: notes.append(f'info: a line of the accented Saṃhitā is printed twice on the page (paragraph {q}); the first copy is set aside')
        return riks, notes, dups

    def as_slices(old):
        return [{'n': r['n'], 's': (r['a0'], r['a'] + 1), 'pa': (r['a'] + 1, r['b'] + 1), 'pl': (r['b'] + 1, r['c'] + 1)} for r in old]

    riks, notes_a, dups = find_anchored() if plain else ([], [], set())
    if len(riks) < len(plain) or not plain:
        riks_o, notes_o = find_old()
        if len(riks_o) > len(riks): riks, notes_a, dups = as_slices(riks_o), notes_o, set()
    for x in notes_a: chk.append(x)
    out = []
    first = min((r['s'][0] for r in riks), default=len(paras))
    intro = [x for k, x in enumerate(paras[:first]) if k not in dups]
    starts = sorted({x for r in riks for x in (r['s'][0], r['pa'][0], r['pl'][0])})
    for r in riks:
        st = r['pl'][1]
        nxt = min((x for x in starts if x >= st), default=len(paras))
        out.append({'n': r['n'], 'samhita_acc': '\n'.join(paras[r['s'][0]:r['s'][1]]), 'pada_acc': '\n'.join(paras[r['pa'][0]:r['pa'][1]]),
                    'pada': '\n'.join(paras[r['pl'][0]:r['pl'][1]]), 'paras': paras[st:nxt]})
    if [r['n'] for r in out] != list(range(1, len(out) + 1)): chk.append(f'Ṛk numbers {[r["n"] for r in out]}')
    if plain and len(plain) != len(out): chk.append(f'{len(plain)} plain Ṛks, {len(out)} Ṛks with Pada and bhāṣya')
    for r in out:
        if 0 < r['n'] <= len(plain) and squash(plain[r['n'] - 1]) != squash(r['samhita_acc']):
            chk.append(f'info: Ṛk {r["n"]}: accented Saṃhitā spells nasals/sandhi otherwise than the plain Saṃhitā of the page')
    return hdr, plain, intro, out, extras, chk


SCHEMA = '''
CREATE TABLE meta(k TEXT PRIMARY KEY, v TEXT);
CREATE TABLE sukta(ref TEXT PRIMARY KEY, m INT, s INT, title TEXT, revid INT, timestamp TEXT, fetched TEXT,
  rishi TEXT, note TEXT, prev TEXT, next TEXT, n_rik INT, n_plain INT, layout TEXT, has_bhashya INT, intro TEXT, intro_i TEXT);
CREATE TABLE rik(ref TEXT PRIMARY KEY, m INT, s INT, r INT, samhita TEXT, samhita_acc TEXT, pada_acc TEXT, pada TEXT,
  samhita_i TEXT, pada_i TEXT, n_para INT, has_sayana INT, bh_at INT);
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
                bh_at = n if paras_n else next((x['n'] for x in riks if x['n'] > n and x['paras']), None)    # Sāyaṇa on several Ṛks together stands with the last
                con.execute('INSERT INTO rik VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)',
                            (f'{m}.{s}.{n}', m, s, n, pl, sa, pa, pd, isq(sa or pl), isq(pd), len(paras_n), int(rk is not None), bh_at))
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
