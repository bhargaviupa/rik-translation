#!/usr/bin/env python3
"""Move the pictures embedded in a supplied markdown file out of it (they make the file 10x bigger and the translator cannot use them inline).

  python3 tools/rv/extract_figures.py VOL FILE.md [--write]

Every line `![...](data:image/TYPE;base64,...)` becomes the line `[figure: volN/html/figures/figNLINE.ext]` (LINE = its line number in FILE, 5 digits; the line count
does not change, so the page splitter sees the same pages) and the picture is written to volN/html/figures/. Without --write only counts are printed. The window prep
shows the pictures to the translator (BRIEF.md: 'read the picture, write the block into kn.md, remove the line'). Used for Vol 11 (Nov 12 2026); Vol 17 did it by hand."""
import re, sys, os, base64
vol, path = sys.argv[1], sys.argv[2]; write = '--write' in sys.argv
root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')); out = os.path.join(root, f'vol{vol}', 'html', 'figures')
L = open(path, encoding='utf8').read().split('\n'); n = 0; size = 0
for i, l in enumerate(L):
    m = re.match(r'!\[[^\]]*\]\(data:image/(\w+);base64,([A-Za-z0-9+/=\s]+)\)\s*$', l)
    if not m: continue
    ext = {'jpeg': 'jpg'}.get(m.group(1), m.group(1)); name = f'fig_line{i + 1:05d}.{ext}'; data = base64.b64decode(m.group(2)); size += len(data); n += 1
    if write:
        os.makedirs(out, exist_ok=True); open(os.path.join(out, name), 'wb').write(data)
        L[i] = f'[figure: vol{vol}/html/figures/{name}]'
print(f'{n} pictures ({size // 1024} KB){" extracted" if write else " found (dry run)"}; images left in the file: {sum(1 for l in L if l.startswith("![") or "base64," in l)}')
if write: open(path, 'w', encoding='utf8').write('\n'.join(L))
