#!/usr/bin/env python3
"""Turn the Sanskrit blocks of a machine-read volume file into `[[block: samhita|pada|bhashya]]` markers, so that tools/rv/ws_fill.py can fill them from the
Wikisource index (shared tool; Vol 26 first). Dry run by default.

  python3 tools/rv/blocks_to_markers.py VOL FIRST LAST [--src FILE] [--out FILE] [--write]

For the printed pages FIRST..LAST of volN/html/rig_N.md (or --src) it asks the pipeline's own structure reader (tools/rv/html_to_kn.py: the same pass that makes kn.md)
which lines are the Saṃhitā, Pada and Sāyaṇa-bhāṣya blocks and which line is the label before each, and replaces
  [label line] + block lines   by   a standard label line (`## ॥ ಸಂಹಿತಾಪಾಠಃ ॥`, `## ॥ ಪದಪಾಠಃ ॥`, `## ॥ ಸಾಯಣಭಾಷ್ಯಂ ॥`) + one marker line;
a block that continues from the previous page (no label on this page) gets a bare marker (ws_fill treats it as the continuation). Nothing else is changed: the prose,
the running heads, the sūkta boxes and the pages outside FIRST..LAST stay as they are. --write writes --out (default volN/html/rig_N.markers.md) and a report
volN/review/blocks_to_markers.tsv (page, kind, source lines replaced, first words)."""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import html_pages, html_to_kn as K
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
vol, first, last = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]); a = sys.argv[4:]
src = a[a.index('--src') + 1] if '--src' in a else os.path.join(ROOT, f'vol{vol}', 'html', f'rig_{vol}.md')
out = a[a.index('--out') + 1] if '--out' in a else os.path.join(ROOT, f'vol{vol}', 'html', f'rig_{vol}.markers.md')
LAB = {'samhita': '## ॥ ಸಂಹಿತಾಪಾಠಃ ॥', 'pada': '## ॥ ಪದಪಾಠಃ ॥', 'bhashya': '## ॥ ಸಾಯಣಭಾಷ್ಯಂ ॥'}
lines = open(src, encoding='utf8').read().split('\n'); heads = {}
P = html_pages.pages_md(src, heads); LP = list(html_pages.LINE_PAGE)
assert len(LP) == len(lines), (len(LP), len(lines))
page_lines = {}
for ln, p in enumerate(LP):
    if p is not None: page_lines.setdefault(p, []).append(ln)
mand = [int(x) for x in re.findall(r'\d+', os.environ.get('MANDALAS', '9'))]
st = {'ref': K.ref_index(mand), 'known': set(P)}; section = None
# warm up: the section at the start of the range is found by running the pass over the 12 pages before (as kn_pages does)
allp = sorted(P); before = [p for p in allp if p < first][-12:]
plan = []; report = []
for p in before + [q for q in allp if first <= q <= last]:
    idxs = page_lines.get(p, [])
    if not idxs: continue
    body = idxs[1:] if len(idxs) > 1 else []            # the first line of a page is its running head
    kept = []; text = []
    for ln in body:
        raw = re.sub(r'^#+\s*', '', lines[ln])
        if raw.strip() == '' : continue
        text.append(raw)
    txt = '\n'.join(text); txt = re.sub(r'\n\s*\n+', '\n', txt).strip()
    # the same line list as kn_page builds: clean_line of every non-empty line, empty results dropped
    cl = [(ln, K.clean_line(re.sub(r'^#+\s*', '', lines[ln]))) for ln in body if re.sub(r'^#+\s*', '', lines[ln]).strip()]
    cl = [(ln, c) for ln, c in cl if c]
    st['trace'] = []
    _, section = K.kn_page(p, heads.get(p, ''), txt, section, st)
    if p < first: continue
    tr = {i: (kind, sec) for i, kind, sec in st['trace']}
    # runs of block lines
    run = None; skipping = False
    def close():
        global run
        if run: plan.append(run); run = None
    for i, (ln, c) in enumerate(cl):
        kind, sec = tr.get(i, (None, None))
        if kind == 'lab' and sec in LAB and re.search(r'ಸಾಯಣ\s*ಭಾ[ಷಷ]್ಯ\s*ಸಂ?ಹಿತಾ', c):      # the title line "ಸಾಯಣಭಾಷ್ಯ ಸಂಹಿತಾ" is not the label of the bhāṣya: the title lines after it stay as text
            close(); skipping = True; continue
        if skipping and kind == 'blk': continue
        if kind != 'blk': skipping = False
        if kind == 'lab' and sec in LAB:
            close(); run = dict(page=p, kind=sec, start=ln, label=True, end=ln, first=''); continue
        if kind == 'blk':
            if run and run['kind'] == sec and (run['end'] is not None): run['end'] = ln; run['first'] = run['first'] or c[:30]
            else:
                close(); run = dict(page=p, kind=sec, start=ln, label=False, end=ln, first=c[:30])
            if run['label'] and not run['first']: run['first'] = c[:30]
        else:
            if run and run['label'] and not run['first']: run = None      # a label with no block after it: leave as it is
            else: close()
    close()
# the same label repeated at the top of the next page with nothing but the running head between: the block continues (kn_page treats it so); the second run loses its label
heads_ln = {idxs[0] for idxs in page_lines.values() if idxs}
plan.sort(key=lambda r: r['start']); merged = 0
# two runs of one kind with only blank lines between them are one block
i_ = 0
while i_ + 1 < len(plan):
    r1, r2 = plan[i_], plan[i_ + 1]
    if r1['kind'] == r2['kind'] and not any(lines[x].strip() for x in range(r1['end'] + 1, r2['start'])) and not r2['label']:
        r1['end'] = r2['end']; del plan[i_ + 1]; merged += 1
    else: i_ += 1
print(f'adjacent runs of one kind merged: {merged}'); merged = 0
for r1, r2 in zip(plan, plan[1:]):
    if r1['kind'] == r2['kind'] and r2['label'] and r2['start'] > r1['end']:
        between = [x for x in range(r1['end'] + 1, r2['start']) if lines[x].strip() and lines[x].strip() != '---' and not lines[x].startswith('<!--') and x not in heads_ln]
        if not between: r2['label'] = False; merged += 1
print(f'repeated labels over a page break turned into continuations: {merged}')
# sūktas that the Wikisource fill cannot take (the supplied text lacks or reorders a Ṛk there) keep their machine-read blocks: --skip-lines 27137-27800,...
if '--skip-lines' in a:
    for rng in a[a.index('--skip-lines') + 1].split(','):
        lo, hi = map(int, rng.split('-')); n0_ = len(plan)
        plan[:] = [r for r in plan if not (lo - 1 <= r['start'] <= hi - 1)]; print(f'lines {lo}-{hi}: {n0_ - len(plan)} blocks left as they are')
# apply from the end so that line numbers stay valid
res = list(lines); rep = []
for r in sorted(plan, key=lambda r: -r['start']):
    if r['label'] and not r['first']: continue
    new = ([LAB[r['kind']]] if r['label'] else []) + [f"[[block: {r['kind']}]]"]
    res[r['start']:r['end'] + 1] = new; rep.append((r['page'], r['kind'], r['start'] + 1, r['end'] + 1, r['label'], r['first']))
# --- a block that continues over a page break is read by the structure reader as the next section when its first line ends with a verse number: a bare marker (no label
# before it) whose kind differs from the marker before it, followed by a labelled marker of its own kind, is the continuation of the block before it.
mk = [i for i, l in enumerate(res) if re.fullmatch(r'\[\[block: (samhita|pada|bhashya)\]\]', l.strip())]
fixed = 0
for n_, i in enumerate(mk[:-1]):
    if n_ == 0: continue
    kind = re.search(r'block: (\w+)', res[i]).group(1); prevk = re.search(r'block: (\w+)', res[mk[n_ - 1]]).group(1); nextk = re.search(r'block: (\w+)', res[mk[n_ + 1]]).group(1)
    lab_before = any(res[j].lstrip('# ').startswith('॥') for j in range(max(0, i - 3), i) if res[j].strip())
    lab_next = any(res[j].lstrip('# ').startswith('॥') for j in range(max(0, mk[n_ + 1] - 3), mk[n_ + 1]) if res[j].strip())
    if not lab_before and kind != prevk and kind == nextk and lab_next:
        res[i] = f'[[block: {prevk}]]'; fixed += 1
print(f'continuations read as the next section corrected: {fixed}')
# --- sūkta headings: ws_fill finds a sūkta by its box line `ಮಂಡಲ—… ಸೂಕ್ತ—…`; the machine reader dropped some boxes. Where a sūkta has its spoken-number line
# (`ಐವತ್ತನಾಲ್ಕನೆಯ ಸೂಕ್ತವು`) but no box, a box line `ಮಂಡಲ—೯ || ಸೂಕ್ತ—N ||` is inserted before the label of its first Saṃhitā block (a logged edit of the supplied
# text: the number is the position of the sūkta in the sequence, checked against every box that can be read).
if '--first-sukta' in a:
    n0 = int(a[a.index('--first-sukta') + 1]); mandala = int(a[a.index('--mandala') + 1]) if '--mandala' in a else 9
    KDIG = str.maketrans('0123456789', '೦೧೨೩೪೫೬೭೮೯'); KD2 = str.maketrans('೦೧೨೩೪೫೬೭೮೯', '0123456789')
    ORD = re.compile(r'^#*\s*[^\s]{3,40}(\s+[^\s]{2,25})?\s*ಸೂಕ್ತವು\.?\s*$')
    ev = []
    for i, l in enumerate(res):
        if len(l) < 45 and ORD.match(l): ev.append((i, 'ord'))
        elif re.search('ಮಂಡಲ[—–-]', l) and re.search('ಸೂಕ್ತ[—–-]', l): ev.append((i, 'box'))
    clusters = []
    for i, kind in ev:
        if kind == 'ord': clusters.append({'ord': i, 'box': None})
        else:
            if clusters and clusters[-1]['box'] is None and i - clusters[-1]['ord'] < 300: clusters[-1]['box'] = i
            else: clusters.append({'ord': None, 'box': i})
    ins = []; rows = []
    for k, cl in enumerate(clusters):
        N = n0 + k; read = None
        if cl['box'] is not None:
            m = re.search(r'ಸೂಕ್ತ[—–-]\s*([೦-೯0-9]+)', res[cl['box']]); read = int(m.group(1).translate(KD2)) if m else None
        rows.append((N, cl['ord'] + 1 if cl['ord'] is not None else '', cl['box'] + 1 if cl['box'] is not None else '', read))
        if cl['box'] is None:
            j = next(x for x in range(cl['ord'], len(res)) if res[x].strip() == '[[block: samhita]]')
            j -= 1
            while j > 0 and not res[j].lstrip('# ').startswith('॥ ಸಂಹಿತಾ'): j -= 1
            ins.append((j, f'ಮಂಡಲ—{mandala} || ಸೂಕ್ತ—{str(N).translate(KDIG)} ||'.replace(str(mandala), str(mandala).translate(KDIG), 1)))
    for j, line in sorted(ins, reverse=True): res[j:j] = [line, '']
    bad = [r for r in rows if r[3] is not None and r[3] != r[0]]
    print(f'{len(clusters)} sūktas found (expected {len(clusters)} from {n0}); boxes inserted: {len(ins)} ({[r[0] for r in rows if r[2] == ""]}); boxes read differently from the sequence: {[(r[0], r[3]) for r in bad]}')
from collections import Counter
c = Counter(k for _, k, *_ in rep)
print(f'pages {first}-{last}: {len(rep)} blocks replaced by markers {dict(c)}')
if '--write' in a:
    open(out, 'w', encoding='utf8').write('\n'.join(res))
    os.makedirs(os.path.join(ROOT, f'vol{vol}', 'review'), exist_ok=True)
    with open(os.path.join(ROOT, f'vol{vol}', 'review', 'blocks_to_markers.tsv'), 'w', encoding='utf8') as f:
        f.write('page\tkind\tfirst_line\tlast_line\twith_label\tfirst_words\n')
        for r in sorted(rep): f.write('\t'.join(map(str, r)) + '\n')
    print('written', os.path.relpath(out, ROOT))
