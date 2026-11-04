#!/usr/bin/env python3
"""Two sheets. (1) Doubtful numerals, each with ALL numeral-file entries on its page that no md numeral uses (value, file line, Raw Line Context).
(2) Every unused numeral-file entry per page (the ones not matched by any md numeral), so a page can be read top to bottom."""
import argparse, re, collections
import openpyxl
from openpyxl.styles import Font, Alignment, PatternFill
from openpyxl.utils import get_column_letter
ap = argparse.ArgumentParser(); ap.add_argument("--md", required=True); ap.add_argument("--num", required=True); ap.add_argument("--out", required=True); a = ap.parse_args()
D2A = str.maketrans("०१२३४५६७८९", "0123456789"); DEV = re.compile(r"[ऀ-ॿ]")
parts = lambda s: re.findall(r"\d+", s.translate(D2A))
def lev(x, y):
    d = list(range(len(y) + 1))
    for i, c in enumerate(x, 1):
        p, d[0] = d[0], i
        for j, e in enumerate(y, 1): p, d[j] = d[j], min(d[j] + 1, d[j - 1] + 1, p + (c != e))
    return d[-1]
rows = collections.defaultdict(list)
for r in list(openpyxl.load_workbook(a.num, read_only=True).active.iter_rows(values_only=True))[1:]:
    if isinstance(r[0], int):
        v = "-".join(parts(str(r[3])))
        if len(v.split("-")) >= 2: rows[r[0]].append(dict(v=v, line=r[1], ctx=re.sub(r"\s+", " ", str(r[4] or ""))[:110]))
L = open(a.md, encoding="utf8").read().split("\n"); page = None; printed = None
pg = collections.defaultdict(lambda: {"ex": [], "q": []})
for n, l in enumerate(L, 1):
    m = re.match(r"#+\s*Page\s+(\d+)\s*\(PDF\s*(\d+)", l)
    if m: printed, page = int(m.group(1)), int(m.group(2))
    if page is None or l.lstrip().startswith("*") or not DEV.search(l): continue
    lt = l.translate(D2A)
    for m in re.finditer(r"(\[?\d+\]?(?:\s*[-–.,]\s*\[?\d+\]?)+)(\s*\[\?\])?", lt):
        ps = parts(m.group(1))
        if len(ps) >= 2:
            if m.group(2): pg[page]["q"].append((n, printed, "-".join(ps), m.group(0).strip(), re.sub(r"\s+", " ", l[max(0, m.start() - 90): m.end() + 30])))
            else: pg[page]["ex"].append("-".join(ps))
    for m in re.finditer(r"(\d+(?:\s*-\s*\d+)*)\s*-\s*\[\?\]|\[(\d+)\s*-\s*\?\]\s*\[\?\]", lt):
        pg[page]["q"].append((n, printed, "-".join(parts(m.group(0))) + "-?", m.group(0).strip(), re.sub(r"\s+", " ", l[max(0, m.start() - 90): m.end() + 30])))
wb = openpyxl.Workbook(); s1 = wb.active; s1.title = "Doubtful + unused entries"
s1.append(["PDF page", "printed page", "md line", "md reading", "text in our file around it", "unused numeral-file entries on this page (value | file line | file context), closest digits first", "YOUR CORRECT DIGITS (C = our reading is correct)"])
s2 = wb.create_sheet("All unused entries by page"); s2.append(["PDF page", "file line", "value", "file context (column E)"])
nq = nu = 0
for P in sorted(pg):
    cands = list(rows.get(P, []))
    for v in pg[P]["ex"]:
        k = next((i for i, c in enumerate(cands) if c["v"] == v), None)
        if k is not None: cands.pop(k)
    U = []
    for t in pg[P]["q"]:
        n, pr, v, tok, ctx = t; k = next((i for i, c in enumerate(cands) if c["v"] == v and not v.endswith("?")), None)
        if k is not None: cands.pop(k)
        else: U.append(t)
    for n, pr, v, tok, ctx in U:
        base = v.rstrip("?-")
        order = sorted(cands, key=lambda c: lev(base, "-".join(c["v"].split("-")[: len(base.split("-"))])))
        s1.append([P, pr, n, tok, ctx, "\n".join(f'{c["v"]}  |  line {c["line"]}  |  {c["ctx"]}' for c in order) or "(none left on this page)", ""]); nq += 1
    for c in cands: s2.append([P, c["line"], c["v"], c["ctx"]]); nu += 1
for ws, w in ((s1, [8, 8, 8, 22, 70, 110, 24]), (s2, [8, 8, 14, 110])):
    for c in ws[1]: c.font = Font(bold=True, color="FFFFFF"); c.fill = PatternFill("solid", fgColor="305496"); c.alignment = Alignment(wrap_text=True, vertical="top")
    for i, x in enumerate(w, 1): ws.column_dimensions[get_column_letter(i)].width = x
    for row in ws.iter_rows(min_row=2):
        for c in row: c.alignment = Alignment(wrap_text=True, vertical="top")
    ws.freeze_panes = "A2"; ws.auto_filter.ref = ws.dimensions
wb.save(a.out); print(nq, "doubtful numerals;", nu, "unused entries ->", a.out)
