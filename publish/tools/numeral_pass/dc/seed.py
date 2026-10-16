#!/usr/bin/env python3
"""Cut single-digit glyphs (labelled by position) from the reader's Kannada_Numbers_0000_to_9999 sheets.
usage: seed.py DIR_WITH_JPEGS OUT.npz"""
import sys, os, glob, numpy as np, cv2
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
import glyphs
X, Y, bad = [], [], 0
for f in sorted(glob.glob(sys.argv[1] + '/*.jpeg')):
    base = int(os.path.basename(f).split('_')[2]); im = cv2.imread(f, 0)
    b = (im < 140).astype(np.uint8)
    rp = b.sum(1) > 0
    runs = []; s = None
    for i, v in enumerate(rp):
        if v and s is None: s = i
        if not v and s is not None: runs.append((s, i)); s = None
    for ri, (a, z) in enumerate(runs):
        n, lab, st, _ = cv2.connectedComponentsWithStats(b[a:z], 8)
        comps = sorted([tuple(map(int, t)) for t in st[1:] if t[4] > 20], key=lambda t: t[0])
        if len(comps) != 80: bad += 1; continue
        for k, c in enumerate(comps):
            num = base + ri * 20 + k // 4
            d = int(f"{num:04d}"[k % 4])
            x, y, w, h = c[:4]
            X.append(glyphs.norm(im[a:z], (x, y, w, h))); Y.append(d)
print(len(X), 'glyphs;', bad, 'bad rows')
np.savez_compressed(sys.argv[2], X=np.array(X), y=np.array(Y))
