#!/usr/bin/env python3
"""Check that every inline ⟦…⟧ Kannada segment in a window's en.md occurs in that window's kn.md.
Usage: python3 tools/rv/check_inline.py volN/work/wNNNN [more dirs]     (also run by `batch.py commit` / `batch.py done`: it is a gate, not a promise)
Whitespace, hyphens, ZWJ/ZWNJ and '|' are ignored. Prints mismatches; exit 1 if any."""
import re, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import convert
norm = lambda s: re.sub(r'[\s‌‍\-–—|>।]+', '', s)   # '>' = block prefix of kn.md lines (a span over a line break inside a block matches); the single danda is ignored too, so words quoted from a Pada-pāṭha match
def mismatches(d):
    e, k = os.path.join(d, 'en.md'), os.path.join(d, 'kn.md')
    if not (os.path.exists(e) and os.path.exists(k)): return []
    raw = open(k, encoding='utf8').read(); kn = norm(raw) + norm(convert.kn_flat(raw))
    en = convert.resolve_markers(open(e, encoding='utf8').read(), raw)
    return [s for s in re.findall(r'⟦([^⟧]+)⟧', en) if '~~' not in s and norm(s) not in kn]
if __name__ == '__main__':
    if len(sys.argv) < 2: sys.exit(__doc__)
    bad = [(os.path.basename(d.rstrip('/')), s) for d in sys.argv[1:] for s in mismatches(d)]
    for d, s in bad: print(f'{d}\t{s}')
    print(f'{len(bad)} inline segment(s) not found in kn.md', file=sys.stderr)
    sys.exit(1 if bad else 0)
