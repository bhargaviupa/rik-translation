#!/usr/bin/env python3
"""Cut hyphenated reference numerals (e.g. ೬-೧-೧೭೧) of a page into single-digit glyph crops.

usage: glyphs.py PAGE.png [PAGE.png ...] --out DIR
Each page gives groups; a group is a chain of dashes on one line plus the digit
components sitting left of the first dash, between dashes, and right of the last.
Writes DIR/glyphs.npz (images 32x32, meta) so they can be clustered/labelled.
"""
import sys, re, argparse, numpy as np, cv2


def find_dashes(b):
    """free-standing thin horizontal bars (hyphens), even when their ends touch a digit"""
    op = cv2.morphologyEx(b, cv2.MORPH_OPEN, np.ones((1, 11), np.uint8))
    n, lab, st, _ = cv2.connectedComponentsWithStats(op, 8)
    H, W = b.shape
    out = []
    for x, y, w, h, a in st[1:]:
        if not (10 <= w <= 60 and 1 <= h <= 9 and w > 2.5 * h):
            continue
        xa, xb = x + int(0.2 * w), x + w - int(0.2 * w)
        up = b[max(0, y - 11):max(0, y - 3), xa:xb]
        dn = b[y + h + 3:y + h + 11, xa:xb]
        if up.sum() <= 2 and dn.sum() <= 2:
            out.append((int(x), int(y), int(w), int(h)))
    return out


def comps(im):
    b = (im < 140).astype(np.uint8)
    b2 = b.copy()
    dd = find_dashes(b)
    for x, y, w, h in dd:
        b2[y:y + h + 1, x:x + w] = 0
    n, lab, st, cen = cv2.connectedComponentsWithStats(b2, 8)
    return b2, lab, [tuple(map(int, s)) for s in st[1:]], dd


def groups(im):
    b, lab, st, dd = comps(im)
    H, W = im.shape
    dashes = [d for d in dd if 250 < d[1] < H - 150]
    dashes.sort(key=lambda d: (d[1] // 40, d[0]))
    chains = []
    for d in dashes:
        for c in chains:
            l = c[-1]
            if abs(l[1] - d[1]) <= 6 and 12 <= d[0] - (l[0] + l[2]) <= 90:
                c.append(d); break
        else:
            chains.append([d])
    digs = [s for s in st if 9 <= s[3] <= 60 and 6 <= s[2] <= 60]
    out = []
    for c in chains:
        if len(c) < 1:
            continue
        yc = np.mean([d[1] + d[3] / 2 for d in c])
        x0 = c[0][0] - 100
        x1 = c[-1][0] + c[-1][2] + 150
        row = [s for s in digs if abs((s[1] + s[3] / 2) - yc) <= 14 and x0 <= s[0] and s[0] + s[2] <= x1]
        row.sort()
        # merge stray pieces lying inside another glyph's x-range
        mg = []
        for s in row:
            if mg:
                q = mg[-1]
                ov = min(q[0] + q[2], s[0] + s[2]) - max(q[0], s[0])
                if ov > 0.6 * min(q[2], s[2]) and (s[2] < 0.6 * q[2] or q[2] < 0.6 * s[2]):
                    x0_, y0_ = min(q[0], s[0]), min(q[1], s[1])
                    x1_ = max(q[0] + q[2], s[0] + s[2]); y1_ = max(q[1] + q[3], s[1] + s[3])
                    mg[-1] = (x0_, y0_, x1_ - x0_, y1_ - y0_, 0)
                    continue
            mg.append(s)
        row = mg
        # split merged pairs
        if row:
            mw = np.median([s[2] for s in row]); nr = []
            for s in row:
                if s[2] > 1.45 * mw and s[2] > 30:
                    x, y, w, h = s[:4]
                    cols = b[y:y + h, x:x + w].sum(0).astype(float)
                    lo, hi = int(0.3 * w), int(0.7 * w)
                    k = lo + int(np.argmin(cols[lo:hi]))
                    nr += [(x, y, k, h, 0), (x + k, y, w - k, h, 0)]
                else:
                    nr.append(s)
            row = nr
        # drop parens / long marks: height far from median
        if not row:
            continue
        med = np.median([s[3] for s in row])
        row = [s for s in row if 0.4 * med <= s[3] <= 1.5 * med and s[2] <= 1.6 * med]
        # split row by dash positions into parts
        parts = [[] for _ in range(len(c) + 1)]
        for s in row:
            cx = s[0] + s[2] / 2
            k = sum(1 for d in c if cx > d[0] + d[2] / 2)
            parts[k].append(s)
        # trailing part: keep only contiguous glyphs (gap < 25 px)
        def contig(p, rev=False):
            p = sorted(p)
            if rev:
                p = p[::-1]
            keep = []
            for s in p:
                if keep:
                    prev = keep[-1]
                    gap = (s[0] - (prev[0] + prev[2])) if not rev else (prev[0] - (s[0] + s[2]))
                    if gap > 12:
                        break
                keep.append(s)
            return sorted(keep)
        parts[0] = contig(parts[0], True)
        parts[-1] = contig(parts[-1])
        if all(parts):
            out.append((c, parts))
    return out


def norm(im, s):
    x, y, w, h = s[:4]
    g = 255 - im[y:y + h, x:x + w]
    m = max(w, h)
    sq = np.zeros((m, m), np.uint8)
    sq[(m - h) // 2:(m - h) // 2 + h, (m - w) // 2:(m - w) // 2 + w] = g
    return cv2.resize(sq, (32, 32), interpolation=cv2.INTER_AREA)


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('pages', nargs='+')
    ap.add_argument('--out', required=True)
    a = ap.parse_args()
    X, M = [], []
    for p in a.pages:
        pg = int(re.search(r'(\d+)\.png$', p).group(1))
        im = cv2.imread(p, 0)
        for gi, (c, parts) in enumerate(groups(im)):
            for pi, part in enumerate(parts):
                for si, s in enumerate(part):
                    X.append(norm(im, s))
                    M.append((pg, gi, pi, si, s[0], s[1], s[2], s[3], len(c), len(part)))
    np.savez_compressed(a.out + '/glyphs.npz', X=np.array(X), M=np.array(M))
    print(len(X), 'glyphs', len(set(m[0] for m in M)), 'pages')
