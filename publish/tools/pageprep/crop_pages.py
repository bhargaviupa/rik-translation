#!/usr/bin/env python3
"""Render PDF pages, trim to the text box, and optionally split into strips at blank gaps.
Cheaper to look at than whole pages (about a third fewer pixels), and the strips let you view only what a step needs.

Usage:
  python3 crop_pages.py PDF FIRST LAST OUTDIR [--dpi 150] [--strips N] [--gap 18] [--quality 80]
    PDF pages FIRST..LAST (PDF numbering). Writes OUTDIR/p<PDF>.jpg (trimmed page), or with --strips N:
    OUTDIR/p<PDF>_<k>.jpg, cutting the trimmed page into at most N strips at the widest blank gaps (>= --gap px).
    The first strip is usually the running head; the last often the foot.
Needs: pdftoppm (poppler), pillow, numpy.
"""
import subprocess, sys, os, glob, tempfile
import numpy as np
from PIL import Image

def trim(im, pad=12):
    a = np.array(im.convert('L')) < 140
    ys, xs = np.where(a)
    if len(xs) == 0: return im
    x0, x1 = int(np.percentile(xs, 0.1)), int(np.percentile(xs, 99.9))
    y0, y1 = int(np.percentile(ys, 0.1)), int(np.percentile(ys, 99.9))
    return im.crop((max(0, x0 - pad), max(0, y0 - pad), min(im.width, x1 + pad), min(im.height, y1 + pad)))

def split(im, n, gap):
    a = (np.array(im.convert('L')) < 140).sum(axis=1)
    blank = a <= 1
    runs, start = [], None
    for y, b in enumerate(blank):
        if b and start is None: start = y
        if not b and start is not None:
            if y - start >= gap: runs.append((y - start, start, y))
            start = None
    cuts = sorted(sorted(runs, reverse=True)[:max(0, n - 1)], key=lambda r: r[1])
    ys = [0] + [(r[1] + r[2]) // 2 for r in cuts] + [im.height]
    return [im.crop((0, ys[i], im.width, ys[i + 1])) for i in range(len(ys) - 1)]

def main():
    if len(sys.argv) < 5: sys.exit(__doc__)
    pdf, a, b, out = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
    opt = lambda k, d: type(d)(sys.argv[sys.argv.index(k) + 1]) if k in sys.argv else d
    dpi, strips, gap, q = opt('--dpi', 150), opt('--strips', 0), opt('--gap', 18), opt('--quality', 80)
    os.makedirs(out, exist_ok=True)
    with tempfile.TemporaryDirectory() as t:
        subprocess.run(['pdftoppm', '-r', str(dpi), '-gray', '-f', str(a), '-l', str(b), '-png', pdf, t + '/p'], check=True)
        for f in sorted(glob.glob(t + '/p-*.png')):
            n = int(os.path.basename(f)[2:-4])
            im = trim(Image.open(f))
            if strips > 1:
                for k, s in enumerate(split(im, strips, gap)): s.save(f'{out}/p{n}_{k}.jpg', quality=q)
            else:
                im.save(f'{out}/p{n}.jpg', quality=q)
            print('page', n, im.size)

if __name__ == '__main__':
    main()
