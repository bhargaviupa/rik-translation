"""`rv import N`: lay a volume's existing English file into the units (docs/DESIGN.md §7).

The English file is cut at its own headings; each piece goes to the unit of the same sūkta, Ṛk and part.  Text is taken over as it stands.
Sanskrit blocks of the English file are NOT taken over (the printer makes them from the source); they are only compared with the source.
`**NOTE**` marks leave the text: the unit keeps a place-holder and the question from review/notes.tsv."""
import re, os, csv, collections
from .common import *

HEAD = [('संहितापाठः', 'samhita'), ('पदपाठः', 'pada'), ('सायणभाष्यम्', 'bhashya'), ('Gist of the bh', 'summary'), ('Pratipad', 'pratipada'), ('Bhāvārtha', 'bhavartha'),
        ('English translation', 'english'), ('Printed English', 'english'), ('Special Topics', 'vishesha'), ('Viśeṣa', 'vishesha'), ('Grammar', 'grammar'), ('Vyākaraṇa', 'grammar')]
NOTE = '⟨NOTE⟩'

def parse_en(vol):
    """-> ordered list of pieces {m, s, rk, kind, en: [items]}; item = ['text', line] | ['block', [Devanagari lines]] | ['label', name]."""
    L = open(vol_paths(vol)['en'], encoding='utf8').read().split('\n'); pieces = []; cur = None; m = s = rk = None; last = {}; st = collections.Counter()
    def start(kind):
        nonlocal cur
        cur = dict(kind=kind, m=m, s=s, rk=rk, en=[]); pieces.append(cur)
        if rk: last[(m, s, rk)] = kind
        return cur
    def ensure():
        if cur is None: start('preface' if s is None else ('intro' if rk is None else last.get((m, s, rk), 'loose')))
        return cur
    def kind_of(text):
        for k, v in HEAD:
            if k in text: return v
    inblock = None; nn = [0]; loose_notes = []
    def piece_of(kind):                                                       # the piece of this Ṛk and kind (made if it is not there yet)
        nonlocal cur
        prev = next((p for p in reversed(pieces) if (p['m'], p['s'], p['rk'], p['kind']) == (m, s, rk, kind)), None) if rk else None
        if prev is not None: cur = prev
        else: start(kind)
        return cur
    def number(mm):
        nn[0] += 1; return f'⟨NOTE:{nn[0]}⟩'
    for i, l in enumerate(L):
        t = l.strip()
        if '**NOTE**' in l:
            if l.startswith('> ') or re.match(r'#', t): k0 = nn[0]; l = re.sub(r'\s*\*\*NOTE\*\*', lambda mm: (number(mm), '')[1], l); loose_notes.append((i, list(range(k0 + 1, nn[0] + 1)))); t = l.strip()
            else: l = re.sub(r'\*\*NOTE\*\*', number, l); t = l.strip()
        if i < 3 and l.startswith('# '): continue
        if t == '---' or t.startswith('**Progress note:**'): continue
        if l.startswith('> '):
            body = l[2:].rstrip()
            if body.startswith('*') and body.rstrip().endswith('*') and not DEVA.search(body): st['transliteration lines left behind (made again at print time)'] += 1; continue
            u = ensure()
            if u['kind'] == 'summary' and inblock is None: u = piece_of('bhashya')    # the bhāṣya goes on after a page break, with no label of its own
            if inblock is None: inblock = ['block', []]; u['en'].append(inblock); st['Sanskrit blocks in the English file'] += 1
            if loose_notes and loose_notes[-1][0] == i: u.setdefault('loose', []).extend(loose_notes[-1][1])
            inblock[1].append(body.rstrip()); continue
        if not t: continue                                                      # a blank line does not end a block: its transliteration follows after one
        inblock = None
        if re.match(r'### Printed p\. ', t): st['page headings (not taken over: pages come from the Kannada side)'] += 1; continue
        if t == '## Preface (Pīṭhike)': m = s = rk = None; start('preface'); continue
        mm = re.match(r'## Maṇḍala (\d+)\s*$', t)
        if mm: m = int(mm.group(1)); continue
        mm = re.match(r'## Sūkta (\d+) \(Maṇḍala (\d+)\)', t)
        if mm: s, m, rk = int(mm.group(1)), int(mm.group(2)), None; start('intro'); continue
        mm = re.match(r'#### Ṛk (\d+)(.*)$', t)
        if mm:
            rk = int(mm.group(1)); cur = None
            if 'contin' in mm.group(2): st['"(continued)" headings dropped'] += 1
            continue
        mm = re.match(r'#{5,6} (.*)$', t) or re.fullmatch(r'\*\*(Bhāvārtha|Special Topics|Pratipad[aā]rtha|Grammar)\*\*(\s*\*\(contin[^)]*\)\*)?', t)
        if mm:
            kind = kind_of(mm.group(1))
            if rk is None and s is not None:                                    # inside a sūkta's introduction: Sāyaṇa's block, Anuvāda, Particulars
                ensure()['en'].append(['label', mm.group(1).strip()]); continue
            if kind is None: ensure()['en'].append(['text', '**' + mm.group(1).strip() + '**']); st['other sub-headings kept as text'] += 1; continue
            prev = next((p for p in reversed(pieces) if (p['m'], p['s'], p['rk'], p['kind']) == (m, s, rk, kind)), None) if rk else None
            if prev is not None: cur = prev; last[(m, s, rk)] = kind
            else: start(kind)
            continue
        u = ensure()
        if u['kind'] == 'bhashya' and rk: u = piece_of('summary')                # English under the bhāṣya is its summary
        u['en'].append(['text', l.rstrip()])
    st['NOTE marks numbered in file order'] = nn[0]
    return pieces, st

def letters(lines): return canon(' '.join(lines))

def run(vol):
    P = vol_paths(vol); units = load_units(vol); pieces, st = parse_en(vol)
    by = {}
    for u in units: by.setdefault((u['m'], u['s'], u['rk'], u['kind']), u); u['en'] = []; u['notes'] = []
    orphans = []; made = 0; nolabel = []
    for p in pieces:
        key = (p['m'], p['s'], p['rk'], p['kind']); u = by.get(key)
        if u is None and p['kind'] == 'summary':                               # the summary of the bhāṣya has no Kannada of its own: a unit beside the bhāṣya unit
            b = by.get((p['m'], p['s'], p['rk'], 'bhashya'))
            u = dict(kind='summary', m=p['m'], s=p['s'], rk=p['rk'], kn=[], en=[], notes=[]); u['id'] = unit_id(vol, u); by[key] = u; made += 1
            units.insert(units.index(b) + 1 if b is not None else len(units), u)
        if u is None and p['rk'] and any(it[0] == 'text' for it in p['en']):       # the English has a part whose label the Kannada file lacks: a unit without Kannada, listed
            after = [x for x in units if (x['m'], x['s'], x['rk']) == (p['m'], p['s'], p['rk'])]
            u = dict(kind=p['kind'], m=p['m'], s=p['s'], rk=p['rk'], kn=[], en=[], notes=[], no_kn_label=True); u['id'] = unit_id(vol, u); by[key] = u; nolabel.append(u['id'])
            units.insert(units.index(after[-1]) + 1 if after else len(units), u)
        if u is None: orphans.append(p); continue
        u['en'] += p['en']
        if p.get('loose'): u.setdefault('loose', []).extend(p['loose'])
    # repairs kept as data (data/import_fixes.json): applied at every run
    import json
    fp = os.path.join(P['data'], 'import_fixes.json'); fx = json.load(open(fp, encoding='utf8')) if os.path.exists(fp) else {}; fixed = []
    byid = {u['id']: u for u in units}
    for mv in fx.get('move', []):
        a, b = byid.get(mv['from']), byid.get(mv['to'])
        if a is None or b is None: fixed.append(f"NOT APPLIED move {mv['from']} -> {mv['to']} (unit not found)"); continue
        b['en'] = (a['en'] + b['en']) if mv.get('where') == 'prepend' else (b['en'] + a['en']); b.setdefault('loose', []).extend(a.pop('loose', []))
        units.remove(a); by.pop((a['m'], a['s'], a['rk'], a['kind']), None)
        if a['id'] in nolabel: nolabel.remove(a['id'])
        fixed.append(f"moved {mv['from']} -> {mv['to']} ({mv.get('where')}): {mv['why']}")
    for sa in fx.get('set_aside', []):
        u = byid.get(sa['id'])
        if u is None: fixed.append(f"NOT APPLIED set aside {sa['id']}"); continue
        u['set_aside'] = sa['why']; fixed.append(f"set aside (kept in the data, not printed) {sa['id']}: {sa['why']}")
        if u['id'] in nolabel: nolabel.remove(u['id'])
    for ad in fx.get('add_en', []):
        u = byid.get(ad['id'])
        if u is None or any(it[0] == 'text' for it in u.get('en', [])): fixed.append(f"NOT APPLIED add {ad['id']} (unit missing or already has English)"); continue
        u['en'] = [['text', f"- {kn2deva(k)} (*{deva_to_iast(kn2deva(k)).strip()}*)—{g}"] for k, g in ad['lines']]; u['supplied'] = ad['why']
        fixed.append(f"English supplied for {ad['id']} ({len(ad['lines'])} entries): {ad['why']}")
    # the Sanskrit blocks of the English file against the source (they are not taken over; this is the proof that the source has the same)
    cmp_ = collections.Counter(); bad = []
    for u in units:
        if u['kind'] not in ('samhita', 'pada', 'bhashya'): continue
        kb = [letters([kn2deva(x) for x in it[1]]) for it in u['kn'] if it[0] == 'block']; eb = [letters(it[1]) for it in u.get('en', []) if it[0] == 'block']
        a, b = ''.join(kb), ''.join(eb)
        if not eb: cmp_['no block in the English file'] += 1
        elif a == b: cmp_['equal to the source, letter for letter'] += 1
        else: cmp_['different from the source'] += 1; bad.append(u['id'])
        u['en'] = [it for it in u.get('en', []) if it[0] != 'block']             # verse, Pada and bhāṣya are printed from the source
    # NOTE marks -> questions (the i-th mark of the file is the i-th row of review/notes.tsv)
    rows = list(csv.reader(open(P['notes'], encoding='utf8'), delimiter='\t'))[1:] if os.path.exists(P['notes']) else []; marks = 0
    q = lambda k: (rows[k - 1][2] if 0 < k <= len(rows) else '')
    for u in units:
        for it in u.get('en', []):
            if it[0] != 'text': continue
            for k in re.findall(r'⟨NOTE:(\d+)⟩', it[1]): u['notes'].append([int(k), q(int(k))]); marks += 1
        for k in u.pop('loose', []): u['notes'].append([k, q(k)]); marks += 1
    for u in units: u['state'] = 'set aside' if u.get('set_aside') else 'supplied' if u.get('supplied') else 'imported' if u.get('en') else ('source only' if u['kind'] in ('samhita', 'pada', 'bhashya', 'english') else 'to do')
    got = collections.Counter(it[1] for u in units if not u.get('supplied') for it in u.get('en', []) if it[0] == 'text')      # counted before the editor's decisions change any text
    # the editor's decisions (data/decisions.tsv): the text changes they require (data/import_fixes.json, replace_en), then the decided marks leave the text
    dp = os.path.join(P['data'], 'decisions.tsv'); dec = {}
    if os.path.exists(dp):
        for r in list(csv.reader(open(dp, encoding='utf8'), delimiter='\t'))[1:]:
            if len(r) >= 4 and r[3].strip() and (len(r) < 6 or r[5].strip() == 'decided'): dec[int(r[0])] = r[3].strip()      # only what was carried out counts as decided
    nrep = 0; miss = []
    for rp in fx.get('replace_en', []):
        u = byid.get(rp['unit']); hit = [it for it in (u or {}).get('en', []) if it[0] == 'text' and it[1] == rp['old']]
        if len(hit) == 1: hit[0][1] = rp['new']; nrep += 1
        else: miss.append(rp['unit'])
    # abbreviations: the forms the one list (rv/references.tsv) marks as decided mistakes are replaced by the form to use; numbers are not touched
    amap = {}
    for r in csv.DictReader(open(os.path.join(ROOT, 'rv', 'references.tsv'), encoding='utf8'), delimiter='\t'):
        if r['status'] == 'mistake' and r['work'].startswith('→ ') and '?' not in r['work']: amap[r['english']] = r['work'][2:].strip()
    nabbr = collections.Counter()
    if amap:
        arx = re.compile(r'(?<![A-Za-zāīūṛṃḥṇṭḍśṣñĀĪŪṚŚṢ.] )(?<![A-Za-zāīūṛṃḥṇṭḍśṣñĀĪŪṚŚṢ])(' + '|'.join(re.escape(k).replace(r'\ ', r'\s?') for k in sorted(amap, key=len, reverse=True)) + r')(?=\s?\d)')
        def ab(mm):
            k = re.sub(r'\s+', ' ', mm.group(1)); k = k if k in amap else re.sub(r'\.(?=\S)', '. ', k)
            if k not in amap: return mm.group(0)
            nabbr[k] += 1; return amap[k]
        for u in units:
            for it in u.get('en', []):
                if it[0] == 'text': it[1] = arx.sub(ab, it[1])
    ndec = 0
    for u in units:
        for n_ in u.get('notes', []):
            if n_[0] in dec and len(n_) == 2: n_.append(dec[n_[0]]); ndec += 1
        ks = {n_[0] for n_ in u.get('notes', []) if len(n_) > 2}
        if ks:
            for it in u.get('en', []):
                if it[0] == 'text': it[1] = re.sub(r'\s*⟨NOTE:(\d+)⟩', lambda mm: '' if int(mm.group(1)) in ks else mm.group(0), it[1])
    save_units(vol, units)
    # proof 1: every English paragraph of the file is in exactly one unit
    src = collections.Counter(it[1] for p in pieces for it in p['en'] if it[0] == 'text')
    lost = sum((src - got).values()); twice = sum((got - src).values())
    ntext = sum(src.values()); need = [u for u in units if not u.get('set_aside') and u['kind'] in ('pratipada', 'bhavartha', 'vishesha', 'grammar', 'intro', 'preface', 'summary')]
    empty = [u['id'] for u in need if not any(it[0] == 'text' for it in u.get('en', []))]
    kinds = collections.Counter(u['kind'] for u in units)
    rep = [f'# Vol {vol}: import report (rv import)', '', f'English file cut into {len(pieces)} pieces; units now {len(units)} ({made} summary units added beside their bhāṣya).', '',
           '## Proof 1: every English paragraph placed once', f'- paragraphs of English text in the file: {ntext}', f'- placed in a unit: {ntext - lost}', f'- not placed (their piece has no unit): {lost}' + (f' in {len(orphans)} pieces: ' + ', '.join(sorted({str((p["m"], p["s"], p["rk"], p["kind"])) for p in orphans})[:12]) if orphans else ''),
           f'- placed more than once: {twice}', f'- parts that the English has and the Kannada file has no label for (units without Kannada; a fault of the supplied text or of its labels): {len(nolabel)}' + (': ' + ', '.join(nolabel) if nolabel else ''), f'- units that should have English and have none: {len(empty)}' + (': ' + ', '.join(empty[:15]) if empty else ''), '',
           '## Proof 2: the Sanskrit of the English file equals the source (verse, Pada, bhāṣya)'] + [f'- {k}: {v}' for k, v in sorted(cmp_.items())] + ([f'- units that differ: ' + ', '.join(bad[:20])] if bad else []) + ['',
           '## Repairs applied from data/import_fixes.json'] + ([f'- {x}' for x in fixed] or ['- none']) + ['',
           '## Questions for the editor', f'- NOTE marks in the English file: {st["NOTE marks numbered in file order"]}; rows in review/notes.tsv: {len(rows)}; attached to units: {marks}', f'- decided (data/decisions.tsv): {ndec}; still open: {marks - ndec}', f'- abbreviations replaced by the form of the one list: {sum(nabbr.values())} (' + ', '.join(f'{k} {v}' for k, v in nabbr.most_common()) + ')', f'- paragraphs changed to carry out a decision (data/import_fixes.json, replace_en): {nrep}' + (f'; NOT APPLIED (paragraph not found): {len(miss)}: ' + ', '.join(miss[:8]) if miss else ''), '',
           '## Left behind on purpose'] + [f'- {k}: {v}' for k, v in sorted(st.items())]
    open(os.path.join(P['review'], 'import_report.md'), 'w', encoding='utf8').write('\n'.join(rep) + '\n'); print('\n'.join(rep))
