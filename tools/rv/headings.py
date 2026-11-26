#!/usr/bin/env python3
"""Title structure of a prose volume from its Kannada text (user, Nov 26 2026: chapters - title level 1 - level 2 - level 3).

  python3 tools/rv/headings.py N          writes volN/data/headings_kn.tsv (nothing else is changed)

How the levels are found, by script only:
  chapter   a line 'ಒಂದನೆಯ ಪ್ರಕರಣ' (N-th chapter); the line after it is the chapter's title
  level 1   a title line of the body that is one of the topics the ORIGINAL lists for that chapter in its own contents pages
            (the contents are read from the front of the same file; a topic and a title line are matched by their letters, >= 80 of 100)
  level 3   a title line that begins with a number ('1.', '೧.', '(1)')
  level 2   every other title line
A title line is: a short line (at most 45 letters) that stands after the end of a sentence or an empty line and before a longer line,
with no daṇḍa and no reference number in it.  The file is a proposal: column 'use' is 'y' for every row; the editor can set 'n' or
change the level, and the print build (publish/volbook.py, Kannada book) makes headings of the rows with 'y'."""
import os, re, sys
from rapidfuzz import fuzz
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
def kn_file(vol):
    for p in (f'vol{vol}/Rigveda_Samhita_Vol{vol}_Kannada_Text.md', f'vol{vol}/kannada/Rigveda_Samhita_Vol{vol}_Kannada_Text.md'):
        if os.path.exists(os.path.join(ROOT, p)): return os.path.join(ROOT, p)
CH = re.compile(r'^([^\s#>*|<\[][^\n]{0,24}ನೆಯ ಪ್ರಕರಣ)(?:ವು)?\s*[.—-]?\s*(.*)$')
def norm(s): return re.sub('[^ಀ-೿]', '', s)
def main():
    vol = int(sys.argv[1]); f = kn_file(vol); L = open(f, encoding='utf8').read().split('\n')
    first = next(i for i, l in enumerate(L) if l.startswith('<!-- printed 2 -->'))
    # the original's contents: chapter -> topics
    topics, cur = {}, None
    for l in L[:first]:
        m = CH.match(l.strip())
        if m and '—' in l or (m and '-' in l): cur = norm(m.group(1)); topics[cur] = []; continue
        if cur: topics[cur] += [t.strip(' .0123456789೦೧೨೩೪೫೬೭೮೯') for t in re.split(r'—|--', l) if len(norm(t)) >= 4]
    rows, page, chap = [], None, None
    for i in range(first, len(L)):
        l = L[i]; t = l.strip()
        m = re.match(r'<!-- printed (\d+) -->', l)
        if m: page = m.group(1); continue
        if not t or t.startswith(('>', '*', '#', '|', '<', '[')): continue
        prev = L[i - 1].strip(); nxt = L[i + 1].strip() if i + 1 < len(L) else ''
        c = CH.match(t)
        if c and len(t) <= 40 and not c.group(2):
            chap = norm(c.group(1)); title = nxt if 0 < len(nxt) <= 60 else ''
            rows.append((i + 1, page, 'chapter', t.rstrip('.'), title, '')); continue
        if rows and rows[-1][0] == i and rows[-1][2] == 'chapter' and rows[-1][4] == t: continue        # the chapter's title line
        if len(t) > 45 or not re.search('[ಀ-೿]', t) or re.search(r'[।॥]|\d-\d|[೦-೯]-[೦-೯]', t) or t.endswith((',', ';', '—', '-')): continue
        if not (not prev or prev.endswith(('.', '?', '।', '॥', ':')) or prev.startswith(('<', '*'))) or len(nxt) <= len(t): continue
        if re.match(r'^[(\[]?[\d೦-೯]{1,2}[.)\]]', t): rows.append((i + 1, page, '3', t, '', '')); continue
        best = max(((fuzz.ratio(norm(t), norm(x)), x) for x in topics.get(chap, [])), default=(0, ''))
        rows.append((i + 1, page, '1' if best[0] >= 80 else '2', t, best[1] if best[0] >= 80 else '', str(round(best[0])) if best[0] >= 80 else ''))
    d = os.path.join(ROOT, f'vol{vol}', 'data'); os.makedirs(d, exist_ok=True); out = os.path.join(d, 'headings_kn.tsv')
    with open(out, 'w', encoding='utf8') as o:
        o.write('line\tprinted page\tlevel\ttitle line\tchapter title / topic of the original contents\tmatch\tuse\n')
        for r in rows: o.write('\t'.join(str(x) for x in r) + '\ty\n')
    import collections
    print(dict(collections.Counter(r[2] for r in rows)), '| chapters with topics in the contents:', len(topics), '| topics:', sum(len(v) for v in topics.values()), '->', os.path.relpath(out, ROOT))
if __name__ == '__main__': main()
