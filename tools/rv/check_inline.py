#!/usr/bin/env python3
"""Check that every inline ⟦…⟧ Kannada segment in a window's en.md occurs in that window's kn.md.
Usage: python3 tools/rv/check_inline.py vol15/work/wNNNN [more dirs]   (no args: all window dirs of vol15)
Whitespace, hyphens, ZWJ/ZWNJ and '|' are ignored. Prints mismatches; exit 1 if any."""
import re, sys, os, glob
norm = lambda s: re.sub(r'[\s‌‍\-–|]+', '', s)
dirs = sys.argv[1:] or sorted(glob.glob('vol15/work/w*'))
bad = []
for d in dirs:
    e, k = os.path.join(d, 'en.md'), os.path.join(d, 'kn.md')
    if not (os.path.exists(e) and os.path.exists(k)): continue
    kn = norm(open(k, encoding='utf8').read())
    for s in re.findall(r'⟦([^⟧]+)⟧', open(e, encoding='utf8').read()):
        if norm(s) not in kn: bad.append((os.path.basename(d.rstrip('/')), s))
for d, s in bad: print(f'{d}\t{s}')
print(f'{len(bad)} inline segment(s) not found in kn.md', file=sys.stderr)
sys.exit(1 if bad else 0)
