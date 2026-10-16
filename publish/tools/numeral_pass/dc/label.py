#!/usr/bin/env python3
"""Weak labels: align segmented glyph groups (extract.py output) with the reader's Google-Docs OCR
reference numbers per page, by hyphen-part lengths. usage: label.py GLYPHS.npz OCR_PAGES.json OFFSET OUT.npz
OCR_PAGES.json maps printed page -> OCR text; pdf page = printed + OFFSET."""
import sys, re, json, difflib, numpy as np
K = dict(zip('೦೧೨೩೪೫೬೭೮೯', '0123456789'))
pat = re.compile(r'[೦-೯]+(?:\s*[-–]\s*[೦-೯]+)+')
def refs(t):
    out = []
    for m in pat.finditer(t):
        s = ''.join(K.get(c, c) for c in m.group(0))
        out.append(re.sub(r'\s+', '', s).replace('–', '-').split('-'))
    return out
d = np.load(sys.argv[1]); X, M = d['X'], d['M']
pages = json.load(open(sys.argv[2])); off = int(sys.argv[3])
y = -np.ones(len(X), int)      # digit label or -1
conf = np.zeros(len(X), int)   # 1 = in an aligned, shape-equal group
by = {}
for i, m in enumerate(M):
    by.setdefault((m[0], m[1]), []).append(i)   # (pdfpage, group) -> glyph indices
ng = 0; nm = 0
for pdfp in sorted(set(M[:, 0])):
    pr = str(pdfp - off)
    if pr not in pages: continue
    gl = sorted([g for (p, g) in by if p == pdfp])
    gshape = []
    for g in gl:
        idx = by[(pdfp, g)]; nparts = M[idx[0]][8] + 1
        cnt = [0] * nparts
        for i in idx: cnt[M[i][2]] += 1
        gshape.append(tuple(cnt))
    rl = refs(pages[pr]); rshape = [tuple(len(x) for x in r) for r in rl]
    sm = difflib.SequenceMatcher(None, gshape, rshape, autojunk=False)
    for a, b, n in sm.get_matching_blocks():
        for k in range(n):
            g = gl[a + k]; r = rl[b + k]; ng += 1
            idx = by[(pdfp, g)]
            # order glyphs by part then idx
            idx = sorted(idx, key=lambda i: (M[i][2], M[i][3]))
            digs = ''.join(r)
            if len(digs) != len(idx): continue
            for i, c in zip(idx, digs): y[i] = int(c); conf[i] = 1
            nm += 1
print('groups aligned', nm, 'glyphs labelled', (y >= 0).sum())
np.savez_compressed(sys.argv[4], X=X, M=M, y=y)
