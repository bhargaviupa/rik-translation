#!/usr/bin/env python3
"""Per-page leftover matching. For each PDF page P: file entries on page P (+ optionally neighbours) that no md numeral
matches exactly are the 'unused entries'; the doubtful md numerals ([?], incl. incomplete ones like '3-2-[?]') on the page
are paired with them by lowest cost (digit distance + shape), best pairs first, one-to-one. Report only; --apply writes.
  python3 numeral_leftover.py --md MD --num XLSX --out TSV [--maxcost 6] [--pad 0]"""
import argparse, re, collections
import openpyxl
D2A = str.maketrans("०१२३४५६७८९", "0123456789"); DEV = re.compile(r"[ऀ-ॿ]")
def lev(x, y):
    d = list(range(len(y) + 1))
    for i, c in enumerate(x, 1):
        p, d[0] = d[0], i
        for j, e in enumerate(y, 1): p, d[j] = d[j], min(d[j] + 1, d[j - 1] + 1, p + (c != e))
    return d[-1]
parts = lambda s: re.findall(r"\d+", s.translate(D2A))
REFQ = re.compile(r"(\[?[०-९0-9]+[\]\?]*(?:\s*[-–.,]\s*\[?[०-९0-9\?]*[\]]*)*)\s*\[\?\]")
def cost(md_parts, complete, v):
    vp = v.split("-")
    if complete:
        c = lev("-".join(md_parts), v) + 3 * abs(len(vp) - len(md_parts))
        return c
    # incomplete: md gives only a prefix; the candidate must start with it
    if len(vp) < len(md_parts): return 99
    d = lev("-".join(md_parts), "-".join(vp[: len(md_parts)]))     # the printed prefix may itself be misread by a digit or two
    return 99 if d > 2 else d + 0.5 * (len(vp) - len(md_parts))
def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--md", required=True); ap.add_argument("--num", required=True)
    ap.add_argument("--out", default="leftover.tsv"); ap.add_argument("--maxcost", type=float, default=6); ap.add_argument("--pad", type=int, default=0)
    a = ap.parse_args()
    fp = collections.defaultdict(list)
    for r in list(openpyxl.load_workbook(a.num, read_only=True).active.iter_rows(values_only=True))[1:]:
        if isinstance(r[0], int):
            v = "-".join(parts(str(r[3])))
            if len(v.split("-")) >= 2: fp[r[0]].append(v)
    pages = collections.defaultdict(lambda: {"all": [], "q": []}); page = None
    for n, l in enumerate(open(a.md, encoding="utf8").read().split("\n"), 1):
        m = re.match(r"#+\s*Page\s+\d+\s*\(PDF\s*(\d+)", l)
        if m: page = int(m.group(1))
        if page is None or l.lstrip().startswith("*") or not DEV.search(l): continue
        for m in re.finditer(r"(\[?\d+\]?(?:\s*[-–.,]\s*\[?\d+\]?)+)(\s*\[\?\])?", l.translate(D2A) if False else l):
            ps = parts(m.group(1))
            if len(ps) >= 2:
                (pages[page]["q"] if m.group(2) else pages[page]["all"]).append((n, ps, True, m.group(0).strip()))
        for m in re.finditer(r"(\d+(?:\s*-\s*\d+)*)\s*-\s*\[\?\]|\[(\d+)\s*-\s*\?\]\s*\[\?\]", l.translate(D2A)):
            ps = [x for x in re.findall(r"\d+", m.group(0))]
            pages[page]["q"].append((n, ps, False, m.group(0).strip()))
    out = []
    for P, d in sorted(pages.items()):
        pool = collections.Counter(v for k in range(-a.pad, a.pad + 1) for v in fp.get(P + k, []))
        for n, ps, comp, tok in d["all"]:
            v = "-".join(ps)
            if pool.get(v, 0) > 0: pool[v] -= 1
        for n, ps, comp, tok in list(d["q"]):                      # exact matches among doubtful ones also use their entry
            v = "-".join(ps)
            if comp and pool.get(v, 0) > 0: pool[v] -= 1; d["q"].remove((n, ps, comp, tok))
        left = [v for v, c in pool.items() for _ in range(c)]
        U = d["q"]
        pairs = sorted((cost(ps, comp, v), i, j) for i, (n, ps, comp, tok) in enumerate(U) for j, v in enumerate(left))
        ui, uj = set(), set()
        for c, i, j in pairs:
            if c > a.maxcost or i in ui or j in uj: continue
            ui.add(i); uj.add(j); n, ps, comp, tok = U[i]
            out.append((n, P, tok, "-".join(ps), left[j], c, len(U), len(left)))
    with open(a.out, "w", encoding="utf8") as f:
        f.write("md_line\tPDF\tmd_token\tmd_digits\tunused_file_entry\tcost\tdoubtful_on_page\tunused_entries_on_page\n")
        for o in out: f.write("\t".join(map(str, o)) + "\n")
    print(len(out), "pairings; cost distribution:", dict(sorted(collections.Counter(int(o[5]) for o in out).items())))
main()
