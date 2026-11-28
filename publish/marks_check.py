#!/usr/bin/env python3
"""D23 (REQUIREMENTS): the page marks of a built Kannada book equal the page markers of the volume's Kannada Text file.

  python3 publish/marks_check.py [N …]        (default: every volume that has a Kannada Text file and a built publish/out/volN_full_Kan.html)

Counts `<!-- printed N -->` (numbers and roman) in the md against id="pN" in the built HTML; lists the marks the build lost. Exit 1 if any volume loses a mark.
Why: a mark glued to the line above it was once swallowed by pandoc without any warning (Vol 17: 5 pages)."""
import re, sys, os, pathlib
ROOT = pathlib.Path(__file__).resolve().parent.parent
def main(a):
    vols = [int(x) for x in a if x.isdigit()] or range(1, 31); bad = 0
    for v in vols:
        k = ROOT / f'vol{v}' / f'Rigveda_Samhita_Vol{v}_Kannada_Text.md'; h = ROOT / 'publish' / 'out' / f'vol{v}_full_Kan.html'
        if not k.exists() or k.stat().st_size < 2000: continue
        if not h.exists(): print(f'vol{v}: no built HTML (publish/out/vol{v}_full_Kan.html)'); continue
        md = set(re.findall(r'(?m)^<!-- printed (\d+|[ivxlc]+) -->$', k.read_text(encoding='utf8')))
        ids = set(re.findall(r'id="p(\d+|[ivxlc]+)"', h.read_text(encoding='utf8')))
        miss = sorted(md - ids, key=lambda x: (len(x), x))
        print(f'vol{v}: {len(md)} marks in the md, {len(ids)} in the build; lost: {miss[:8] if miss else "none"}')
        bad += bool(miss)
    return 1 if bad else 0
if __name__ == '__main__': sys.exit(main(sys.argv[1:]))
