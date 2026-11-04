#!/usr/bin/env python3
"""Align the md's numerals (in reading order, per page) with the numeral file's rows (in line order) by dynamic
programming; exact matches act as anchors, and doubtful md numerals ([?]) take the file row they align to.
  python3 numeral_align.py --md MD --num XLSX [--test] [--out TSV]
--test: hold out every exactly-matched numeral, predict it from the alignment, report accuracy."""
import argparse, re, collections, random
import openpyxl
D2A = str.maketrans("०१२३४५६७८९", "0123456789"); DEV = re.compile(r"[ऀ-ॿ]")
REF = re.compile(r"(\[?\d+\]?(?:\s*[-–.,]\s*\[?\d+\]?)+)(\s*\[\?\])?")
def parts(s): return re.findall(r"\d+", s.translate(D2A))
def lev(x, y):
    d = list(range(len(y) + 1))
    for i, c in enumerate(x, 1):
        p, d[0] = d[0], i
        for j, e in enumerate(y, 1): p, d[j] = d[j], min(d[j] + 1, d[j - 1] + 1, p + (c != e))
    return d[-1]
def score(m, f):
    if m is None: return 0 if f else -1
    if m == f: return 4
    if len(m.split("-")) != len(f.split("-")): return -3
    return 1 if lev(m, f) <= 1 else (0 if lev(m, f) <= 2 else -2)
def align(M, F, gap=-1):
    n, k = len(M), len(F); S = [[0] * (k + 1) for _ in range(n + 1)]; B = [[None] * (k + 1) for _ in range(n + 1)]
    for i in range(1, n + 1): S[i][0] = i * gap; B[i][0] = "u"
    for j in range(1, k + 1): S[0][j] = j * gap; B[0][j] = "l"
    for i in range(1, n + 1):
        for j in range(1, k + 1):
            c = [(S[i-1][j-1] + score(M[i-1], F[j-1]), "d"), (S[i-1][j] + gap, "u"), (S[i][j-1] + gap, "l")]
            S[i][j], B[i][j] = max(c)
    i, j, pairs = n, k, {}
    while i > 0 or j > 0:
        b = B[i][j]
        if b == "d": pairs[i-1] = j-1; i -= 1; j -= 1
        elif b == "u": i -= 1
        else: j -= 1
    return pairs
def load(md, num):
    fp = collections.defaultdict(list)
    for r in list(openpyxl.load_workbook(num, read_only=True).active.iter_rows(values_only=True))[1:]:
        if isinstance(r[0], int):
            v = "-".join(parts(str(r[3])))
            if len(v.split("-")) >= 2 and (not fp[r[0]] or fp[r[0]][-1][1] != v): fp[r[0]].append((r[1], v))
    mp = collections.defaultdict(list); page = None
    for n, l in enumerate(open(md, encoding="utf8").read().split("\n"), 1):
        m = re.match(r"#+\s*Page\s+\d+\s*\(PDF\s*(\d+)", l)
        if m: page = int(m.group(1))
        if page is None or l.lstrip().startswith("*") or not DEV.search(l): continue      # skip IAST twins
        for m in REF.finditer(l.translate(D2A) if False else l):
            ps = parts(m.group(1))
            if len(ps) >= 2: mp[page].append(dict(line=n, val="-".join(ps), q=bool(m.group(2)), tok=m.group(0)))
    return fp, mp
def run(md, num, test=False, out=None):
    fp, mp = load(md, num); res = []; hits = tot = 0; random.seed(1)
    for P, M in sorted(mp.items()):
        best = max((-1, 0, -2, 1), key=lambda k: sum(1 for x in M if x["val"] in {v for _, v in fp.get(P + k, [])}))
        F = [v for _, v in fp.get(P + best, [])]
        if not F: continue
        vals = [x["val"] for x in M]
        if test:
            idx = [i for i, x in enumerate(M) if x["val"] in F and not x["q"]]
            hold = set(random.sample(idx, max(1, len(idx) // 3))) if idx else set()
            Mt = [None if i in hold else v for i, v in enumerate(vals)]
            pr = align(Mt, F)
            for i in hold:
                tot += 1; hits += (i in pr and F[pr[i]] == vals[i])
            continue
        pr = align(vals, F)
        for i, x in enumerate(M):
            if x["q"]:
                f = F[pr[i]] if i in pr else None
                res.append((x["line"], P, x["tok"].strip(), x["val"], f, score(x["val"], f) if f else None, best))
    if test: print(f"held-out numerals: {tot}; predicted correctly: {hits} ({100*hits/max(tot,1):.0f}%)"); return
    if out:
        with open(out, "w", encoding="utf8") as f:
            f.write("md_line\tPDF\tmd_token\tmd_digits\talign_file_value\tscore\toffset\n")
            for r in res: f.write("\t".join("" if x is None else str(x) for x in r) + "\n")
    c = collections.Counter("agree" if r[4] == r[3] else "differ" if r[4] else "none" for r in res)
    print(len(res), "[?] numerals;", dict(c))
if __name__ == "__main__":
    ap = argparse.ArgumentParser(); ap.add_argument("--md", required=True); ap.add_argument("--num", required=True)
    ap.add_argument("--test", action="store_true"); ap.add_argument("--out"); a = ap.parse_args(); run(a.md, a.num, a.test, a.out)
