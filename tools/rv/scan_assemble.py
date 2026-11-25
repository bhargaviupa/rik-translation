#!/usr/bin/env python3
"""Assemble the transcribed scan pages into one machine-text file in the layout of the supplied files (shared tool; Vol 25 first). No API.

  python3 tools/rv/scan_assemble.py VOL FIRST LAST [--first-printed 1] [--out volN/html/rig_N.md]
      joins volN/work/scan_pages/pNNNN.md for PDF pages FIRST..LAST, one page after another, separated by a line `---` (as in vol21/html/rig_21.md);
      `<!-- page 1 -->` stands before the first body page; the file `volN/html/pages_map.tsv` lists (position, PDF page, first line of the page, number of [?]).
      Nothing is changed in the text: [[block: …]] markers and [?] stay (they are filled / answered by later steps).
"""
import os, re, sys
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
def main():
    a = sys.argv[1:]; out = None; fp = 1
    if '--out' in a: i = a.index('--out'); out = a[i + 1]; del a[i:i + 2]
    if '--first-printed' in a: i = a.index('--first-printed'); fp = int(a[i + 1]); del a[i:i + 2]
    vol, first, last = a[0], int(a[1]), int(a[2])
    d = os.path.join(ROOT, f'vol{vol}', 'work', 'scan_pages'); out = out or os.path.join(ROOT, f'vol{vol}', 'html', f'rig_{vol}.md')
    parts = []; rows = []
    for n, pg in enumerate(range(first, last + 1)):
        f = os.path.join(d, f'p{pg:04d}.md')
        if not os.path.exists(f): sys.exit(f'missing page file {f}')
        t = open(f, encoding='utf8').read().strip('\n')
        parts.append((f'<!-- page {fp} -->\n' if n == 0 else '') + t)
        rows.append((n + 1, pg, t.split('\n')[0][:60], t.count('[?]')))
    os.makedirs(os.path.dirname(out), exist_ok=True)
    open(out, 'w', encoding='utf8').write('\n\n---\n\n'.join(parts) + '\n')
    with open(os.path.join(os.path.dirname(out), 'pages_map.tsv'), 'w', encoding='utf8') as g:
        g.write('position\tpdf_page\tfirst_line\tquestion_marks\n')
        for r in rows: g.write('\t'.join(map(str, r)) + '\n')
    print(f'{len(rows)} pages → {os.path.relpath(out, ROOT)} ({os.path.getsize(out)} bytes), [?] total {sum(r[3] for r in rows)}; map in pages_map.tsv')
main()
