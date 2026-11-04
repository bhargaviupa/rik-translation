#!/usr/bin/env python3
"""After numeral edits on Devanagari-bearing lines: update the same references on English-only lines of the same page.
  python3 numeral_sweep_english.py --md MD --base-rev GITREV [--apply]   (base = md before the numeral work)"""
import argparse, re, difflib, collections, subprocess
ap = argparse.ArgumentParser(); ap.add_argument("--md", required=True); ap.add_argument("--base-rev", required=True); ap.add_argument("--apply", action="store_true"); a = ap.parse_args()
D2A = str.maketrans("०१२३४५६७८९", "0123456789"); dev = re.compile("[ऀ-ॿ]")
REF = re.compile(r"(\[?\d+\]?(?:\s*[-–.,]\s*\[?\d+\]?)+)(\s*\[\?\])?")
A = subprocess.run(["git", "show", f"{a.base_rev}:{a.md}"], capture_output=True, text=True).stdout.split("\n")
B = open(a.md, encoding="utf8").read().split("\n")
val = lambda m: "-".join(re.findall(r"\d+", m.group(1).translate(D2A)))
chg = []
for tag, i1, i2, j1, j2 in difflib.SequenceMatcher(None, A, B, autojunk=False).get_opcodes():
    if tag != "replace" or i2 - i1 != j2 - j1: continue
    for k in range(i2 - i1):
        ra = [(val(m), bool(m.group(2))) for m in REF.finditer(A[i1 + k])]; rb = [(val(m), bool(m.group(2))) for m in REF.finditer(B[j1 + k])]
        if len(ra) == len(rb):
            for (va, qa), (vb, qb) in zip(ra, rb):
                if qa and (va != vb or not qb): chg.append((j1 + k + 1, va, vb))
cur = None; pg = {}
for n, l in enumerate(B, 1):
    m = re.match(r"#+\s*Page\s+\d+\s*\(PDF\s*(\d+)", l)
    if m: cur = int(m.group(1))
    pg[n] = cur
maps = collections.defaultdict(lambda: collections.defaultdict(set))
for jn, va, vb in chg: maps[pg[jn]][va].add(vb)
n_upd = n_val = 0
for n, l in enumerate(B, 1):
    if dev.search(l) or "[?]" not in l or pg.get(n) is None: continue
    def rep(m):
        global n_upd, n_val
        if not m.group(2): return m.group(0)
        v = val(m); nv = maps.get(pg[n], {}).get(v)
        if not nv or len(nv) > 1: return m.group(0)
        nv = next(iter(nv)); n_upd += 1; n_val += (nv != v); return nv
    new = REF.sub(rep, l)
    if new != l and a.apply: B[n - 1] = new
print(f"English-only occurrences to update: {n_upd} (value changed: {n_val}, only [?] dropped: {n_upd - n_val})")
if a.apply: open(a.md, "w", encoding="utf8").write("\n".join(B))
