#!/usr/bin/env python3
"""Volume-level check: is every block of the English file under the label of ITS section?

  python3 tools/rv/check_labels.py N

Needs the sub-heading layout (`##### ॥ संहितापाठः ॥`, `##### ॥ पदपाठः ॥`, `##### ॥ सायणभाष्यम् ॥`: Vols 17, 18).  Each Devanagari block of the English file is matched
(letters only, accents/punctuation/spaces dropped) with the Kannada blocks near the same position of the Kannada file, converted letter for letter; the
section of the best match (the label line before it in the Kannada file) is compared with the sub-heading above the English block.  Blocks that match
nothing (a bhāṣya cut in the English by the window's page break, a Kannada block with no label) are counted but not reported.
Why: in Vol 18 six windows (162, 223, 316, 371, 445, 729) had every block under the label of another section and no window gate saw it (lesson 61)."""
import re, sys, pathlib, difflib
root = pathlib.Path(__file__).resolve().parents[2]; sys.path.insert(0, str(root / 'publish' / 'tools' / 'translit'))
from kannada_to_deva import kn2deva
vol = int(sys.argv[1])
en = (root / f'vol{vol}' / f'Rigveda_Samhita_Vol{vol}_English_Translation.md').read_text(encoding='utf8').split('\n')
kn = (root / f'vol{vol}' / f'Rigveda_Samhita_Vol{vol}_Kannada_Text.md').read_text(encoding='utf8').split('\n')
SEC = {'ಸಂಹಿತಾಪಾಠಃ': 'samhita', 'ಪದಪಾಠಃ': 'pada', 'ಸಾಯಣಭಾಷ್ಯಂ': 'bhashya'}
ESEC = {'संहितापाठः': 'samhita', 'पदपाठः': 'pada', 'सायणभाष्यम्': 'bhashya'}
KEEP = re.compile('[^ऄ-हा-ौॐ]')       # letters and vowel signs only (no accents, danda, digits, virama kept out too: robust to spelling of conjuncts)
def norm(s): return KEEP.sub('', s)
# Kannada blocks with the section of the label above them
kb = []; sec = None; cur = None; page = None
for l in kn:
    m = re.match(r'<!-- printed (\d+)', l)
    if m: page = int(m.group(1))
    m = re.fullmatch(r'\*([^*\[\]]+)\*', l.strip())
    if m: sec = SEC.get(m.group(1).strip(), sec if m.group(1).strip() not in SEC else None); cur = None; continue
    if l.startswith('> ') and not l.startswith('> *'):
        if cur is None: cur = []; kb.append([sec, page, cur])
        cur.append(kn2deva(l[2:]))
    else: cur = None
for b in kb: b[2] = norm(' '.join(b[2]))
# English blocks with the sub-heading above them
eb = []; lab = None; cur = None; page = None
for l in en:
    m = re.match(r'### Printed p\. (\d+)', l)
    if m: page = int(m.group(1))
    m = re.match(r'##### ॥ (\S+) ॥', l)
    if m: lab = ESEC.get(m.group(1)); cur = None; continue
    if l.startswith('#'): lab = None; cur = None; continue
    if l.startswith('> ') and not l.startswith('> *'):
        if cur is None: cur = []; eb.append([lab, page, cur])
        cur.append(l[2:])
    elif l.strip(): cur = None
for b in eb: b[2] = norm(' '.join(b[2]))
bad = []; unmatched = 0; j0 = 0
for i, (lab, page, t) in enumerate(eb):
    if not lab or len(t) < 20: continue
    cand = []
    for j in range(max(0, j0 - 6), min(len(kb), j0 + 12)):
        k = kb[j]
        if not k[2]: continue
        cand.append((difflib.SequenceMatcher(None, t[:300], k[2][:300], autojunk=False).ratio(), j))
    best = max(cand, default=(0, None))
    same = [c for c in cand if kb[c[1]][0] == lab and c[0] >= best[0] - 0.03]      # Saṃhitā and Pada differ only in sandhi: a tie goes to the block with the right section
    if same and best[1] is not None: best = max(same)
    if best[1] is None or best[0] < 0.6: unmatched += 1; continue
    j0 = best[1] + 1
    ksec = kb[best[1]][0]
    if ksec and ksec != lab and best[0] >= 0.9: bad.append((page, lab, ksec, round(best[0], 2)))
print(f'Vol {vol}: {len(eb)} English blocks, {len(kb)} Kannada blocks, {unmatched} not matched, {len(bad)} under the label of another section')
pages = sorted({b[0] for b in bad})
for b in bad[:60]: print('  p.', b[0], 'under', b[1], 'but the Kannada block is', b[2], '(match', b[3], ')')
if pages: print('pages:', pages)
sys.exit(1 if bad else 0)
