#!/usr/bin/env python3
"""Per-page SET comparison (no row mapping). For each md PDF page: file numerals on pages P-2..P form a pool;
md numerals that match a pool value exactly use it up; the doubtful md numerals ([?]) left over are paired with the
remaining pool values by closest digits (same number of parts), best pairs first.
  --test : hold out 1/3 of the exactly matched numerals as if doubtful and report how often the pairing recovers them.
  --out TSV : candidates for the real [?] numerals."""
import argparse, re, collections, random
import openpyxl
D2A = str.maketrans("०१२३४५६७८९", "0123456789"); DEV = re.compile(r"[ऀ-ॿ]")
REF = re.compile(r"(\[?\d+\]?(?:\s*[-–.,]\s*\[?\d+\]?)+)(\s*\[\?\])?")
parts = lambda s: re.findall(r"\d+", s.translate(D2A))
def lev(x, y):
    d = list(range(len(y) + 1))
    for i, c in enumerate(x, 1):
        p, d[0] = d[0], i
        for j, e in enumerate(y, 1): p, d[j] = d[j], min(d[j] + 1, d[j - 1] + 1, p + (c != e))
    return d[-1]
def load(md, num):
    fp = collections.defaultdict(list)
    for r in list(openpyxl.load_workbook(num, read_only=True).active.iter_rows(values_only=True))[1:]:
        if isinstance(r[0], int):
            v = "-".join(parts(str(r[3])))
            if len(v.split("-")) >= 2: fp[r[0]].append(v)
    mp = collections.defaultdict(list); page = None
    for n, l in enumerate(open(md, encoding="utf8").read().split("\n"), 1):
        m = re.match(r"#+\s*Page\s+\d+\s*\(PDF\s*(\d+)", l)
        if m: page = int(m.group(1))
        if page is None or l.lstrip().startswith("*") or not DEV.search(l): continue
        for m in REF.finditer(l):
            ps = parts(m.group(1))
            if len(ps) >= 2: mp[page].append(dict(line=n, val="-".join(ps), q=bool(m.group(2)), tok=m.group(0).strip()))
    return fp, mp
def pair(pool, doubt, maxlev):
    """greedy closest pairs; returns {index_in_doubt: pool_value}"""
    cand = sorted((lev(d, v), i, j) for i, d in enumerate(doubt) for j, v in enumerate(pool) if len(d.split("-")) == len(v.split("-")) and lev(d, v) <= maxlev)
    ui, uj, out = set(), set(), {}
    for l, i, j in cand:
        if i in ui or j in uj: continue
        ui.add(i); uj.add(j); out[i] = (pool[j], l)
    return out
def run(md, num, test, out, maxlev):
    fp, mp = load(md, num); random.seed(2); tot = ok = wrong = 0; res = []
    for P, M in sorted(mp.items()):
        pool = [v for p in range(P - 2, P + 2) for v in fp.get(p, [])]
        if not pool: continue
        # exact matches consume pool values
        left = list(pool); doubt = []
        hold = set()
        if test:
            ex = [i for i, x in enumerate(M) if x["val"] in pool and not x["q"]]
            hold = set(random.sample(ex, max(1, len(ex) // 3))) if ex else set()
        for i, x in enumerate(M):
            if (x["q"] or i in hold) :
                doubt.append(i); continue
            if x["val"] in left: left.remove(x["val"])
        # the doubtful ones: first remove exact matches among them (non-test) then pair the rest
        dv = [M[i]["val"] for i in doubt]
        if not test:
            keep = []
            for i in doubt:
                v = M[i]["val"]
                if v in left: left.remove(v)
                else: keep.append(i)
            doubt = keep; dv = [M[i]["val"] for i in doubt]
        else:
            # held-out ones must not see their own value as exact: pair against left + their own consumed values
            for i in hold:
                pass
            left2 = list(left)
            for i in hold:
                if M[i]["val"] in pool: left2.append(M[i]["val"])
            left = left2
        pr = pair(left, dv, maxlev)
        for k, (cand, l) in pr.items():
            i = doubt[k]
            if test:
                if i in hold: tot += 1; ok += (cand == M[i]["val"]); wrong += (cand != M[i]["val"])
            else:
                res.append((M[i]["line"], P, M[i]["tok"], M[i]["val"], cand, l))
        if test: tot += sum(1 for i in hold if i not in [doubt[k] for k in pr])
    if test: print(f"maxlev {maxlev}: held-out {tot}; recovered correctly {ok} ({100*ok/max(tot,1):.0f}%); paired wrongly {wrong}; not paired {tot-ok-wrong}"); return
    if out:
        with open(out, "w", encoding="utf8") as f:
            f.write("md_line\tPDF\tmd_token\tmd_digits\tpool_value\tlev\n")
            for r in res: f.write("\t".join(map(str, r)) + "\n")
    print(len(res), "pairings; lev distribution:", dict(collections.Counter(r[5] for r in res)))
    return res
if __name__ == "__main__":
    ap = argparse.ArgumentParser(); ap.add_argument("--md", required=True); ap.add_argument("--num", required=True)
    ap.add_argument("--test", action="store_true"); ap.add_argument("--out"); ap.add_argument("--maxlev", type=int, default=2)
    a = ap.parse_args(); run(a.md, a.num, a.test, a.out, a.maxlev)
