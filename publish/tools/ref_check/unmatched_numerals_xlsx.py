#!/usr/bin/env python3
"""Spreadsheet of numeral [?] in a volume md that are still unmatched against the user's numeral file."""
import argparse, re, collections
import openpyxl
from openpyxl.styles import Font, Alignment, PatternFill
from openpyxl.utils import get_column_letter
ap = argparse.ArgumentParser(); ap.add_argument("--md", required=True); ap.add_argument("--num", required=True)
ap.add_argument("--out", required=True); ap.add_argument("--printed-offset", type=int, default=15)
a = ap.parse_args()
D2A = str.maketrans("०१२३४५६७८९", "0123456789")
NUMTOK = re.compile(r"([०-९0-9\[\]]+(?:[-–.,][ ]?[०-९0-9\[\]]+)*)\s*\[\?\]"); DEV = re.compile(r"[ऀ-ॿ]")
parts = lambda s: re.findall(r"\d+", s.translate(D2A))
fp = collections.defaultdict(set)
for r in list(openpyxl.load_workbook(a.num, read_only=True).active.iter_rows(values_only=True))[1:]:
    if isinstance(r[0], int): fp[r[0]].add("-".join(parts(str(r[3]))))
def lev(x, y):
    d = list(range(len(y) + 1))
    for i, c in enumerate(x, 1):
        p, d[0] = d[0], i
        for j, e in enumerate(y, 1): p, d[j] = d[j], min(d[j] + 1, d[j - 1] + 1, p + (c != e))
    return d[-1]
lines = open(a.md, encoding="utf8").read().split("\n"); page = None; suk = "81"; rows = []
for n, l in enumerate(lines, 1):
    m = re.match(r"#+\s*Page\s+(\d+)\s*\(PDF\s*(\d+)", l)
    if m: printed, page = int(m.group(1)), int(m.group(2))
    h = re.match(r"##\s+Sūkta\s+(\d+)", l)
    if h: suk = h.group(1)
    if page is None or "[?]" not in l or not DEV.search(l): continue
    for m in NUMTOK.finditer(l):
        ps = parts(m.group(1))
        if not ps: continue
        md = "-".join(ps); win = set().union(*(fp.get(p, set()) for p in range(page - 2, page + 2)))
        near = sorted((lev(md, v), v) for v in win if len(v.split("-")) == len(ps))[:4]
        rows.append([n, printed, page, suk, "bhāṣya / Devanagari block" if l.lstrip().startswith(">") else "English note",
                     md, m.group(1), ", ".join(f"{v}" for d, v in near), re.sub(r"\s+", " ", l[max(0, m.start() - 70): m.end() + 25]), ""])
wb = openpyxl.Workbook(); ws = wb.active; ws.title = "Unmatched numerals"
ws.append(["md line", "printed page", "PDF page", "Sūkta (section)", "Where", "md digits (as read)", "md token (raw)",
           "nearest numeral-file values on page window (same no. of parts)", "text around it", "YOUR CORRECT DIGITS"])
for r in rows: ws.append(r)
for c in ws[1]: c.font = Font(bold=True, color="FFFFFF"); c.fill = PatternFill("solid", fgColor="305496"); c.alignment = Alignment(wrap_text=True, vertical="top")
for i, w in enumerate([8, 9, 8, 10, 22, 16, 16, 30, 90, 22], 1): ws.column_dimensions[get_column_letter(i)].width = w
for row in ws.iter_rows(min_row=2):
    for c in row: c.alignment = Alignment(wrap_text=True, vertical="top")
ws.freeze_panes = "A2"; ws.auto_filter.ref = ws.dimensions
wb.save(a.out); print(len(rows), "rows ->", a.out)
