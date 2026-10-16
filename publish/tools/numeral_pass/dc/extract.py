#!/usr/bin/env python3
"""Render PDF pages at 300 dpi (grey) and cut reference-numeral glyph crops with glyphs.py.
usage: extract.py PDF FIRST LAST OUT.npz [--procs N]
Writes X (n,32,32 uint8), M (n,10 ints: pdfpage, group, part, idx, x,y,w,h, nparts_in_group... as glyphs.py) """
import sys, os, subprocess, tempfile, argparse, numpy as np, cv2
from multiprocessing import Pool
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
import glyphs

def work(a):
    pdf, pg = a
    with tempfile.TemporaryDirectory() as d:
        subprocess.run(['pdftoppm', '-r', '300', '-gray', '-f', str(pg), '-l', str(pg), '-png', pdf, d + '/p'], check=True)
        f = [x for x in os.listdir(d) if x.endswith('.png')][0]
        im = cv2.imread(os.path.join(d, f), 0)
    X, M = [], []
    for gi, (c, parts) in enumerate(glyphs.groups(im)):
        for pi, part in enumerate(parts):
            for si, s in enumerate(part):
                X.append(glyphs.norm(im, s))
                M.append((pg, gi, pi, si, s[0], s[1], s[2], s[3], len(c), len(part)))
    return X, M

if __name__ == '__main__':
    ap = argparse.ArgumentParser(); ap.add_argument('pdf'); ap.add_argument('first', type=int); ap.add_argument('last', type=int)
    ap.add_argument('out'); ap.add_argument('--procs', type=int, default=4); a = ap.parse_args()
    with Pool(a.procs) as p:
        res = p.map(work, [(a.pdf, i) for i in range(a.first, a.last + 1)], chunksize=2)
    X = [x for r in res for x in r[0]]; M = [m for r in res for m in r[1]]
    np.savez_compressed(a.out, X=np.array(X), M=np.array(M))
    print(len(X), 'glyphs from', a.last - a.first + 1, 'pages')
