#!/usr/bin/env python3
"""Decode hyphenated reference numerals from glyph groups. usage: decode.py GLYPHS.npz CLF.pkl OUT.json
Output: {pdfpage: [ {ref:'6-1-171', conf:min-prob, x,y, digits:[[digit,prob,top2]]} ]}"""
import sys, json, pickle, numpy as np, cv2
d = np.load(sys.argv[1]); X, M = d['X'], d['M']; clf = pickle.load(open(sys.argv[2], 'rb'))
F = np.array([cv2.GaussianBlur(x, (3, 3), 0).ravel() / 255. for x in X], dtype=np.float32)
P = clf.predict_proba(F); cls = clf.classes_
g = {}
for i, m in enumerate(M): g.setdefault((int(m[0]), int(m[1])), []).append(i)
out = {}
for (pg, gi), idx in sorted(g.items()):
    idx = sorted(idx, key=lambda i: (M[i][2], M[i][3])); parts = {}; ok = True; mins = 1.0; dets = []
    for i in idx:
        o = np.argsort(-P[i]); top = int(cls[o[0]]); p = float(P[i][o[0]])
        if top == 10: ok = False; break
        mins = min(mins, p); dets.append((top, round(p, 2), int(cls[o[1]]), round(float(P[i][o[1]]), 2)))
        parts.setdefault(int(M[i][2]), []).append(str(top))
    if not ok: continue
    ref = '-'.join(''.join(parts[k]) for k in sorted(parts))
    out.setdefault(pg, []).append(dict(ref=ref, conf=round(mins, 2), x=int(M[idx[0]][4]), y=int(M[idx[0]][5]), d=dets))
json.dump(out, open(sys.argv[3], 'w'), ensure_ascii=False)
print(sum(len(v) for v in out.values()), 'references decoded on', len(out), 'pages')
