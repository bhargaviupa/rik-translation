#!/usr/bin/env python3
"""Replace the labelled glosses of quoted passages by the marker **GLOSS** (user, Nov 17 2026: the glosses of quoted Ṛks are to come from our own
edition, requirement B3.5; until then a marker stands).

  python3 tools/rv/gloss_marker.py VOL [VOL …]            # report only
  python3 tools/rv/gloss_marker.py VOL [VOL …] --write    # change the English file; every removed gloss goes to volN/review/glosses_removed.tsv
  python3 tools/rv/gloss_marker.py --list FILE.tsv [--write]   # glosses found by a reader (vol, line, exact text): replaced only when found once in the line

Only glosses that are labelled as ours AND stand in one of the exact forms below are replaced, whole (label, quotation marks and gloss); nothing
else on the line is touched.  A labelled gloss in any other form is left as it is and listed in volN/review/glosses_left.tsv for a reading.
Glosses that carry no label (woven into the prose) cannot be found by script.
Forms:  line    `> Gloss: "…"` / `*Gloss, mine and tentative:* "…"` alone on its line
        paren   `(Gloss, mine and tentative: "…"; "…".)` / `("…": mine and tentative.)` / `("…" — mine and tentative.)`
        tail    `… — mine and tentative: "…".` at the end of a line
        after   `"…" (mine and tentative)` / `"…" (mine, tentative)`
Added Nov 18 2026 (the forms left in Vols 3–8), tried after the ones above:
        parenx  `(Gloss[es][,] mine and tentative[, for the first | (for both)]: "…"; "…".)`, also `My glosses, **mine and tentative**: 1. "…"; 2. "…"`,
                `Translation[ of the ṛk][,] mine and tentative: "…"`, `My gloss, tentative: "…"`, glosses in '…'; the whole parenthesis when it holds nothing else
        inline  the same label and quotation(s) anywhere in a line (after a dash, inside a longer remark): only label and quotation(s) are replaced
        aftercap `"…" (Mine, tentative.)`
Never replaced: `**Translation** (mine, tentative): …` (our translation of the bhāṣya's introduction, not a gloss of a quotation), `Sense, mine and
tentative: …` and `Gist (mine)` (renderings of the bhāṣya), and a label that is not followed at once by a quotation."""
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
    ('aftercap', re.compile(QS + r'\s*\*?\(\s*Mine(?: and|,) tentative\.?\s*\)\*?'), '**GLOSS**'),
]
Q1 = r"'(?:[^'\n\u0900-\u097F*]|\*(?!\*)|'(?=\w))+?[^\s'*]'(?![\w'])"
QX = r'(?:' + QS + r'|' + Q1 + r')'
NUM = r'(?:\(?\d+\)?\.|\d+[.\-]\d+[.\-]\d+)'
GAP = r'(?:\s*\[\?\]|\s+for the \w+)?'          # a doubt mark or "for the first" between two glosses of one list goes with them
QLX = r'(?:' + NUM + r'\s*)?' + QX + r'(?:(?:' + GAP + r'\s*[;,]\s*(?:and\s+)?(?:' + NUM + r'\s*)?|\.?\s+' + NUM + r'\s*|\s*—\s*)' + QX + r')*(?:\s+for the (?:second|third|last)(?=\.))?'
LABX = (r'(?:(?:(?:[Mm]y )?(?:[Gg]loss(?:es)?|[Tt]ranslation|sense)(?: of the (?:[ṛṚ]k|Sanskrit|quotation)| on these \w+ citations)?,?\s+)?\*{0,2}(?<!Sense, )[Mm]ine(?: and|,) tentative\*{0,2}'
        r'|[Mm]y gloss(?:es)?, tentative)')
FILL = r'(?:\s*\((?:for )?[^()":\n]{0,60}\)|,\s*[^:;"“()\n]{0,60})?'
CORE = LABX + FILL + r'\s*:\*?\s*' + QLX
FORMS += [
    ('parenx', re.compile(r'\*?\(\s*\*?' + CORE + r'\.?\s*\)\*?'), '**GLOSS**'),
    ('inline', re.compile(r'(?<![*\w,\s])(\s+)' + LABX + FILL + r'\s*:\*\s*' + QLX), r'*\1**GLOSS**'),   # the label closes an italic remark: its closing mark stays
    ('inline', re.compile(r'\*?' + CORE), '**GLOSS**'),
]
SKIP = re.compile(r'^\s*(?:>\s*)?\*\*Translation\*\*')
MARK = re.compile(r'mine and tentative|\bmine, tentative|\(mine\)|— mine\b|\bGloss(?:es)?\b[^.\n]{0,40}:|\[tentative\]|my gloss|tentative gloss', re.I)
def run(vol, write):
    p = os.path.join(ROOT, f'vol{vol}', f'Rigveda_Samhita_Vol{vol}_English_Translation.md')
    if not os.path.exists(p): return
    L = open(p, encoding='utf8').read().split('\n'); removed = []; left = []; n = {}
    for i, l in enumerate(L):
        new = l
        for name, rx, sub in ([] if SKIP.search(l) else FORMS):
            def f(m, name=name):
                removed.append((i + 1, name, m.group(0).strip())); n[name] = n.get(name, 0) + 1
                return m.expand(sub)
            new = rx.sub(f, new)
        if MARK.search(new.replace('**GLOSS**', '')) and not re.search(r'^\*?Sense \(mine\)', new.strip()): left.append((i + 1, new.strip()[:300]))
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
def run_list(path, write):
    """Glosses that carry no label or stand in a single odd form, found by a reader: a TSV `vol <tab> line <tab> exact text`.  The text is replaced
    by the marker only when it stands exactly once in that line; otherwise the row is refused and nothing of it is changed."""
    rows = [r.rstrip('\n').split('\t') for r in open(path, encoding='utf8') if r.strip() and not r.startswith('vol\t')]
    for vol in sorted({int(r[0]) for r in rows}):
        p = os.path.join(ROOT, f'vol{vol}', f'Rigveda_Samhita_Vol{vol}_English_Translation.md')
        L = open(p, encoding='utf8').read().split('\n'); done = []; refused = []
        for r in [r for r in rows if int(r[0]) == vol]:
            ln, text = r[1], r[2]; i = int(ln) - 1
            new = r[3] if len(r) > 3 and r[3].strip() else '**GLOSS**'      # optional 4th column: what stands instead (one marker, e.g. with a bracket the label had opened)
            if not text.strip() or L[i].count(text) != 1 or new.count('**GLOSS**') != 1: refused.append((ln, L[i].count(text) if text.strip() else 0, text[:80])); continue
            L[i] = L[i].replace(text, new); done.append((int(ln), 'listed', text.strip()))
        print(f'Vol {vol}: listed glosses replaced by the marker: {len(done)}; refused: {len(refused)}' + ('' if write else '  (report only)'))
        for r in refused: print(f'   refused line {r[0]} (found {r[1]} times): {r[2]}')
        if not write: continue
        d = os.path.join(ROOT, f'vol{vol}', 'review'); os.makedirs(d, exist_ok=True)
        with open(os.path.join(d, 'glosses_removed.tsv'), 'a', encoding='utf8') as f:
            if f.tell() == 0: f.write('line\tform\tremoved text\n')
            for r in done: f.write('\t'.join(map(str, r)).replace('\n', ' ') + '\n')
        open(p, 'w', encoding='utf8').write('\n'.join(L))
if __name__ == '__main__':
    a = sys.argv[1:]; w = '--write' in a
    if '--list' in a: run_list(a[a.index('--list') + 1], w)
    else:
        for v in [x for x in a if x.isdigit()]: run(int(v), w)
