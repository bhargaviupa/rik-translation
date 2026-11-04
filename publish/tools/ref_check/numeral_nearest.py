#!/usr/bin/env python3
"""Replace every doubtful numeral ([?]) by the nearest UNUSED entry of the user's numeral file on the same PDF page
(user decision Nov 4 2026: the file is always correct). File page = PDF page.
  python3 numeral_nearest.py --md MD --num XLSX --log TSV [--apply]
Pool per page = file entries on that page minus those exactly equal to a non-doubtful md numeral.
Doubtful numerals are counted on Devanagari-bearing non-italic lines; pairing is greedy by edit distance
(same part count preferred: +3 penalty otherwise; incomplete tokens like 4-1-? compare their known prefix).
The new value is then written wherever the same old token+[?] occurs on that page (IAST twins, English notes)
when the page maps it to one new value only."""
import argparse, re, collections
import openpyxl
D2A = str.maketrans("०१२३४५६७८९", "0123456789"); A2D = str.maketrans("0123456789", "०१२३४५६७८९")
DEV = re.compile(r"[ऀ-ॿ]")
REF = re.compile(r"(\[?[०-९0-9]+\]?(?:[ ]?[-–.,][ ]?\[?[०-९0-9]+\]?)+)(\s*\[\?\])?")
INC = re.compile(r"((?:[०-९0-9]+\s*-\s*)+)\[\?\]|\[([०-९0-9]+(?:\s*-\s*[०-९0-9]+)*\s*-\s*)\?\]\s*\[\?\]")
parts = lambda s: re.findall(r"\d+", s.translate(D2A))
def lev(x, y):
    d = list(range(len(y) + 1))
    for i, c in enumerate(x, 1):
        p, d[0] = d[0], i
        for j, e in enumerate(y, 1): p, d[j] = d[j], min(d[j] + 1, d[j - 1] + 1, p + (c != e))
    return d[-1]
def cost(known, nk, v):
    """known: list of digit strings (nk = complete? False means last part missing)"""
    vp = v.split("-")
    if any(int(x) == 0 for x in vp): return 99   # the file misreads digits as 0 (README); never applied
    if nk and len(vp) != len(known): return 99
    if nk:  # complete token
        return lev("-".join(known), v) + (0 if len(vp) == len(known) else 3)
    if len(vp) <= len(known): return 99
    return lev("-".join(known), "-".join(vp[:len(known)])) + 1
ap = argparse.ArgumentParser(); ap.add_argument("--md", required=True); ap.add_argument("--num", required=True); ap.add_argument("--log", required=True); ap.add_argument("--apply", action="store_true"); a = ap.parse_args()
fp = collections.defaultdict(list)
for r in list(openpyxl.load_workbook(a.num, read_only=True).active.iter_rows(values_only=True))[1:]:
    if isinstance(r[0], int):
        v = "-".join(parts(str(r[3])))
        if len(v.split("-")) >= 2: fp[r[0]].append(v)
L = open(a.md, encoding="utf8").read().split("\n")
pg = {}; cur = None
for n, l in enumerate(L):
    m = re.match(r"#+\s*Page\s+\d+\s*\(PDF\s*(\d+)", l)
    if m: cur = int(m.group(1))
    pg[n] = cur
items = collections.defaultdict(lambda: {"ex": [], "q": []})   # page -> ...
for n, l in enumerate(L):
    P = pg[n]
    if P is None or l.lstrip().startswith("*") or not DEV.search(l): continue
    taken = []
    for m in INC.finditer(l):
        kn = parts(m.group(0)); items[P]["q"].append((n, m.start(), m.end(), kn, False, m.group(0))); taken.append((m.start(), m.end()))
    for m in REF.finditer(l):
        if any(s <= m.start() < e for s, e in taken): continue
        ps = parts(m.group(1))
        if len(ps) < 2: continue
        if m.group(2): items[P]["q"].append((n, m.start(), m.end(), ps, True, m.group(0)))
        else: items[P]["ex"].append("-".join(ps))
assign = {}   # (n,start) -> new value ; and per page old-token map
log = []; unres = []
for P, it in sorted(items.items()):
    pool = list(fp.get(P, []))
    for v in it["ex"]:
        if v in pool: pool.remove(v)
    q = it["q"]
    # exact first
    rest = []
    for t in q:
        n, s, e, kn, comp, tok = t; v = "-".join(kn)
        if comp and v in pool: pool.remove(v); assign[(n, s)] = (v, t, 0, P)
        else: rest.append(t)
    cand = sorted((cost(t[3], t[4], v), i, j) for i, t in enumerate(rest) for j, v in enumerate(pool))
    ui, uj = set(), set()
    for c, i, j in cand:
        if c >= 99 or i in ui or j in uj: continue
        ui.add(i); uj.add(j); assign[(rest[i][0], rest[i][1])] = (pool[j], rest[i], c, P)
    for i, t in enumerate(rest):
        if i not in ui: unres.append((t[0] + 1, P, t[5], "no unused entry left" if not pool else "no compatible entry"))
# page-level map for twin/English lines
pmap = collections.defaultdict(lambda: collections.defaultdict(set))
for (n, s), (nv, t, c, P) in assign.items(): pmap[P]["-".join(t[3]) + ("" if t[4] else "?")].add(nv)
def fmt(nv, tok):
    out = nv.replace("-", "-")
    return out.translate(A2D) if DEV.search(re.sub(r"[^०-९]", "", tok) or "") else out
with open(a.log, "w", encoding="utf8") as f:
    f.write("md_line\tPDF\told_token\tnew_value\tedit_cost\n")
    for (n, s), (nv, t, c, P) in sorted(assign.items()): f.write(f"{n+1}\t{P}\t{t[5].strip()}\t{nv}\t{c}\n")
    for u in unres: f.write(f"{u[0]}\t{u[1]}\t{u[2]}\tUNRESOLVED ({u[3]})\t\n")
cd = collections.Counter(c for (_, _, c, _) in assign.values())
print(f"{len(assign)} assigned (cost distribution {dict(sorted(cd.items()))}); {len(unres)} unresolved")
if a.apply:
    nd = nt = 0
    for n, l in enumerate(L):
        P = pg[n]
        if P is None: continue
        sp = [(s, e, nv, t) for (nn, s), (nv, t, c, PP) in assign.items() if nn == n for e in [t[2]]]
        if sp:
            for s, e, nv, t in sorted(sp, reverse=True): l = l[:s] + fmt(nv, t[5]) + l[e:]; nd += 1
            L[n] = l; continue
        if "[?]" not in l: continue
        def rep(m):
            global nt
            if not m.group(2): return m.group(0)
            ps = parts(m.group(1)); v = "-".join(ps); nv = pmap.get(P, {}).get(v)
            if nv and len(nv) == 1: nt += 1; return fmt(next(iter(nv)), m.group(1))
            return m.group(0)
        L[n] = REF.sub(rep, l)
    open(a.md, "w", encoding="utf8").write("\n".join(L))
    print("applied: Devanagari-line tokens", nd, "; twin/English occurrences", nt)
