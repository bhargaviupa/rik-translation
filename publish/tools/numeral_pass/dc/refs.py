#!/usr/bin/env python3
"""Find and decode hyphenated reference numerals (e.g. 6-1-171) on PDF pages.
usage: refs.py PDF FIRST LAST OUT.json CLF.pkl [--procs N] [--crops DIR]
Per page: list of {ref, conf, x, y, w, h, digits:[(d,p,second,p2)]}; optional crops of each reference."""
import sys, os, json, pickle, tempfile, subprocess, argparse, numpy as np, cv2
from multiprocessing import Pool
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
import glyphs
CLF = None
def init(p):
    global CLF; CLF = pickle.load(open(p, 'rb'))
def feat(A): return np.array([cv2.GaussianBlur(x, (3, 3), 0).ravel() / 255. for x in A], dtype=np.float32)
def page(a):
    pdf, pg, crops = a
    with tempfile.TemporaryDirectory() as d:
        subprocess.run(['pdftoppm', '-r', '300', '-gray', '-f', str(pg), '-l', str(pg), '-png', pdf, d + '/p'], check=True)
        im = cv2.imread(os.path.join(d, [x for x in os.listdir(d) if x.endswith('.png')][0]), 0)
    b = (im < 150).astype(np.uint8)
    n, lab, st0, _ = cv2.connectedComponentsWithStats(b, 8)
    st0 = [tuple(map(int, t[:4])) for t in st0[1:]]
    H, W = im.shape
    dd = [t for t in st0 if t[3] <= 5 and 6 <= t[2] <= 45 and 250 < t[1] < H - 120]      # thin bars = hyphen pieces
    pieces = sorted([t for t in st0 if t[3] > 5 and 250 < t[1] < H - 120 and t[2] < 60], key=lambda t: t[0])
    st = []
    for t in pieces:       # rejoin narrow pieces of one glyph (e.g. the two legs of an arch)
        if st:
            q = st[-1]; gap = t[0] - (q[0] + q[2])
            if q[2] <= 9 and t[2] <= 9 and gap <= 10 and abs(q[1] - t[1]) <= 4 and abs(q[3] - t[3]) <= 4 and 12 <= q[3] <= 40:
                x0 = q[0]; y0 = min(q[1], t[1]); x1 = t[0] + t[2]; y1 = max(q[1] + q[3], t[1] + t[3])
                st[-1] = (x0, y0, x1 - x0, y1 - y0); continue
        st.append(t)
    cand = [s for s in st if 12 <= s[3] <= 40 and 8 <= s[2] <= 40]
    if not cand: return pg, []
    P = CLF.predict_proba(feat([glyphs.norm(im, s) for s in cand])); cls = CLF.classes_
    items = []
    for s, p in zip(cand, P):
        o = np.argsort(-p)
        items.append(dict(s=s, d=int(cls[o[0]]), p=float(p[o[0]]), d2=int(cls[o[1]]), p2=float(p[o[1]])))
    for t in items:   # junk top-1 but a digit a close second: take the digit (the reader's confusions are among digits)
        if t['d'] == 10 and t['d2'] != 10 and t['p2'] > 0.25: t['d'], t['p'] = t['d2'], t['p2']
    dig = [t for t in items if t['d'] != 10 and t['p'] > 0.25]
    dashes = [d for d in dd if 250 < d[1] < H - 120]
    # chain: digits sorted by x on a line; clusters separated by gap<=14 px; clusters joined by a dash
    dig.sort(key=lambda t: (round((t['s'][1] + t['s'][3] / 2) / 30), t['s'][0]))
    lines = {}
    for t in dig:
        yc = t['s'][1] + t['s'][3] / 2
        for k in lines:
            if abs(k - yc) < 14: lines[k].append(t); break
        else: lines[yc] = [t]
    refs = []
    for yc, row in lines.items():
        row.sort(key=lambda t: t['s'][0])
        # clusters
        cl = [[row[0]]]
        for t in row[1:]:
            q = cl[-1][-1]['s']; gap = t['s'][0] - (q[0] + q[2])
            cl[-1].append(t) if gap <= 16 else cl.append([t])
        # dashes on this line
        dl = [d for d in dashes if abs((d[1] + d[3] / 2) - yc) < 18]
        chain = [cl[0]]
        def link(a, b):
            xa = a[-1]['s'][0] + a[-1]['s'][2]; xb = b[0]['s'][0]
            if not (4 <= xb - xa <= 70): return False
            return any(xa - 6 <= d[0] and d[0] + d[2] <= xb + 6 for d in dl)
        groups = []
        cur = [cl[0]]
        for c in cl[1:]:
            if link(cur[-1], c): cur.append(c)
            else:
                groups.append(cur); cur = [c]
        groups.append(cur)
        for g in groups:
            if len(g) < 2: continue
            ds = [t for c in g for t in c]
            x0 = min(t['s'][0] for t in ds); y0 = min(t['s'][1] for t in ds)
            x1 = max(t['s'][0] + t['s'][2] for t in ds); y1 = max(t['s'][1] + t['s'][3] for t in ds)
            refs.append(dict(ref='-'.join(''.join(str(t['d']) for t in c) for c in g),
                             conf=round(min(t['p'] for t in ds), 2), x=int(x0), y=int(y0), w=int(x1 - x0), h=int(y1 - y0),
                             digits=[(t['d'], round(t['p'], 2), t['d2'], round(t['p2'], 2)) for t in ds]))
            if crops:
                cv2.imwrite(f"{crops}/p{pg}_{int(x0)}_{int(y0)}.png", im[max(0, y0 - 8):y1 + 8, max(0, x0 - 8):x1 + 8])
    refs.sort(key=lambda r: (r['y'] // 25, r['x']))
    return pg, refs
if __name__ == '__main__':
    ap = argparse.ArgumentParser(); ap.add_argument('pdf'); ap.add_argument('first', type=int); ap.add_argument('last', type=int)
    ap.add_argument('out'); ap.add_argument('clf'); ap.add_argument('--procs', type=int, default=4); ap.add_argument('--crops')
    a = ap.parse_args()
    if a.crops: os.makedirs(a.crops, exist_ok=True)
    with Pool(a.procs, initializer=init, initargs=(a.clf,)) as p:
        res = p.map(page, [(a.pdf, i, a.crops) for i in range(a.first, a.last + 1)], chunksize=2)
    json.dump({str(pg): r for pg, r in res}, open(a.out, 'w'), ensure_ascii=False)
    print(sum(len(r) for _, r in res), 'references on', len(res), 'pages')
