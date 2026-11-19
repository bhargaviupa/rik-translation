#!/usr/bin/env python3
"""Replace the labelled glosses of quoted passages by the marker **GLOSS** (user, Nov 17 2026: the glosses of quoted Ṛks are to come from our own
edition, requirement B3.5; until then a marker stands).

  python3 tools/rv/gloss_marker.py VOL [VOL …]            # report only
  python3 tools/rv/gloss_marker.py VOL [VOL …] --write    # change the English file; every removed gloss goes to volN/review/glosses_removed.tsv

Only glosses that are labelled as ours AND stand in one of the exact forms below are replaced, whole (label, quotation marks and gloss); nothing
else on the line is touched.  A labelled gloss in any other form is left as it is and listed in volN/review/glosses_left.tsv for a reading.
Glosses that carry no label (woven into the prose) cannot be found by script.
Forms:  line    `> Gloss: "…"` / `*Gloss, mine and tentative:* "…"` alone on its line
        paren   `(Gloss, mine and tentative: "…"; "…".)` / `("…": mine and tentative.)` / `("…" — mine and tentative.)`
        tail    `… — mine and tentative: "…".` at the end of a line
        after   `"…" (mine and tentative)` / `"…" (mine, tentative)`"""
import re, sys, os
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
QS = r'[“"][^“”"\n]{4,}[”"]'
QL = QS + r'(?:\s*[;,]\s*(?:and\s+)?' + QS + r')*'
MT = r'mine(?: and|,) tentative|mine'
LAB = r'(?:Gloss(?:es)?(?:\s*\((?:' + MT + r')\)|,\s*(?:' + MT + r'))?|[Mm]ine(?: and|,) tentative|Translation,\s*mine and tentative)'
FORMS = [
    ('line', re.compile(r'^(\s*(?:>\s*)?)\*?' + LAB + r'\s*:?\*?\s*:?\s*' + QL + r'\.?\s*(?:\[tentative\])?\s*$'), r'\1**GLOSS**'),
    ('paren', re.compile(r'\*?\(\s*\*?' + LAB + r'\s*:\*?\s*' + QL + r'\.?\s*\)\*?'), '**GLOSS**'),
    ('paren', re.compile(r'\*?\(\s*' + QL + r'\s*(?::|—|–|-)\s*(?:' + MT + r')\.?\s*\)\*?'), '**GLOSS**'),
    ('tail', re.compile(r'\s*(?:—|–)\s*\*?' + LAB + r'\s*:\*?\s*' + QL + r'\.?\s*$'), ' — **GLOSS**'),
    ('after', re.compile(QS + r'\s*\*?\(\s*(?:' + MT + r')\.?\s*\)\*?'), '**GLOSS**'),
]
MARK = re.compile(r'mine and tentative|\bmine, tentative|\(mine\)|— mine\b|\bGloss(?:es)?\b[^.\n]{0,40}:|\[tentative\]|my gloss|tentative gloss', re.I)
def run(vol, write):
    p = os.path.join(ROOT, f'vol{vol}', f'Rigveda_Samhita_Vol{vol}_English_Translation.md')
    if not os.path.exists(p): return
    L = open(p, encoding='utf8').read().split('\n'); removed = []; left = []; n = {}
    for i, l in enumerate(L):
        new = l
        for name, rx, sub in FORMS:
            def f(m, name=name):
                removed.append((i + 1, name, m.group(0).strip())); n[name] = n.get(name, 0) + 1
                return m.expand(sub)
            new = rx.sub(f, new)
        if MARK.search(new) and not re.search(r'^\*?Sense \(mine\)', new.strip()): left.append((i + 1, new.strip()[:300]))
        L[i] = new
    print(f'Vol {vol}: glosses replaced by the marker: {sum(n.values())} {n}; labelled lines left for a reading: {len(left)}' + ('' if write else '  (report only)'))
    if not write: return
    d = os.path.join(ROOT, f'vol{vol}', 'review'); os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, 'glosses_removed.tsv'), 'a', encoding='utf8') as f:
        if f.tell() == 0: f.write('line\tform\tremoved text\n')
        for r in removed: f.write('\t'.join(map(str, r)).replace('\n', ' ') + '\n')
    with open(os.path.join(d, 'glosses_left.tsv'), 'w', encoding='utf8') as f:
        f.write('line\ttext (a gloss or remark labelled as ours, in a form the script does not replace)\n')
        for r in left: f.write(f'{r[0]}\t{r[1]}\n')
    open(p, 'w', encoding='utf8').write('\n'.join(L))
if __name__ == '__main__':
    a = sys.argv[1:]; w = '--write' in a
    for v in [x for x in a if x.isdigit()]: run(int(v), w)
