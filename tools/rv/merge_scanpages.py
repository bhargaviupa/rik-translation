#!/usr/bin/env python3
"""Merge several OCR files that use '## Page N' labels (scan-page index) into ONE file, sorted by label.

  python3 tools/rv/merge_scanpages.py OUT.md IN1.md IN2.md ... [--drop LO-HI ...]

Empty pages are ignored; a page present in several files keeps its longest non-empty version (differences are listed in the header).
--drop LO-HI: labels to ignore in the FOLLOWING sense: any file's labels LO..HI that carry a lone printed number far from label-21/22
(e.g. a run restarting at 10 whose printed page is 488) are mislabelled; they are dropped only when you name them. Nothing else is edited.
The header lists the labels present and the MISSING ones (gaps are never filled or guessed)."""
import re, sys
args = sys.argv[1:]; drop = set()
while '--drop' in args:
    i = args.index('--drop'); a, b = args[i+1].split('-'); drop |= set(range(int(a), int(b)+1)); del args[i:i+2]
out, ins = args[0], args[1:]
def pages(f):
    p = re.split(r'^## Page (\d+)\s*$', open(f, encoding='utf8').read(), flags=re.M)
    return [(int(p[i]), p[i+1].strip().removesuffix('---').strip()) for i in range(1, len(p), 2)]
best = {}; conf = []
for f in ins:
    seen_high = False
    for n, b in pages(f):
        if n > 100: seen_high = True
        if n in drop and seen_high: continue          # a label that restarted low after high ones = mislabelled
        if not b: continue
        if n in best:
            if best[n] != b: conf.append(n)
            if len(b) <= len(best[n]): continue
        best[n] = b
nums = sorted(best); miss = [i for i in range(1, max(nums)+1) if i not in best]
def rg(l):
    r = []; s = p = None
    for x in l:
        if s is None: s = p = x
        elif x == p+1: p = x
        else: r.append((s, p)); s = p = x
    if s is not None: r.append((s, p))
    return ', '.join(str(a) if a == b else f'{a}-{b}' for a, b in r)
hdr = (f"# vol (Kannada Transcription) — merged by merge_scanpages.py\n<!-- Labels present: {len(nums)} (1-{max(nums)}). MISSING ({len(miss)}): {rg(miss)} -->\n"
       f"<!-- Labels dropped as mislabelled (named by --drop): {rg(sorted(drop))}. Pages that differ between files (longest kept): {rg(sorted(set(conf)))} -->\n\n")
open(out, 'w', encoding='utf8').write(hdr + '\n'.join(f'## Page {n}\n\n{best[n]}\n' for n in nums))
print(len(nums), 'pages;', len(miss), 'missing:', rg(miss)); print('differing:', rg(sorted(set(conf))))
