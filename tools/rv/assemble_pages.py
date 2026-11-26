#!/usr/bin/env python3
"""Assemble a volume's supplied-text file from per-page transcription files.

  python3 tools/rv/assemble_pages.py OUT.md --offset 26 --first 1 --last 600 --front OLD.md DIR1 [DIR2 ...]

Printed page P is taken from the first directory that has pdf{P+offset}.md (the order of the directories is the priority). The front matter
(everything before '<!-- body -->' of OLD.md) is copied unchanged. Output: front matter, '<!-- body -->', then for each page '<!-- page P -->' and its text
(tools/rv/html_pages.py honours these markers when there are at least 50). Pages without a file are listed (and written as an empty page).
Also writes OUT.pages.tsv: printed page, PDF page, source directory, characters."""
import sys, os, re
args = sys.argv[1:]
def opt(n, d=None):
    if n in args:
        i = args.index(n); v = args[i+1]; del args[i:i+2]; return v
    return d
off = int(opt('--offset', 26)); first = int(opt('--first', 1)); last = int(opt('--last', 600)); front = opt('--front')
out, dirs = args[0], args[1:]
fm = ''
if front:
    t = open(front, encoding='utf8').read()
    fm = t.split('<!-- body -->')[0].rstrip() + '\n\n'
body = []; tsv = ['printed\tpdf\tsource\tchars']; miss = []
for P in range(first, last + 1):
    n = P + off; src = None
    for d in dirs:
        f = os.path.join(d, f'pdf{n}.md')
        if os.path.exists(f): src = (d, open(f, encoding='utf8').read().strip('\n')); break
    if not src: miss.append(P); body.append(f'<!-- page {P} -->\n'); tsv.append(f'{P}\t{n}\t-\t0'); continue
    body.append(f'<!-- page {P} -->\n{src[1]}\n'); tsv.append(f'{P}\t{n}\t{os.path.basename(src[0].rstrip("/"))}\t{len(src[1])}')
open(out, 'w', encoding='utf8').write(fm + '<!-- body -->\n\n' + '\n'.join(body))
open(out.rsplit('.', 1)[0] + '.pages.tsv', 'w', encoding='utf8').write('\n'.join(tsv) + '\n')
print(f'{last-first+1-len(miss)} pages written, missing: {miss}')
