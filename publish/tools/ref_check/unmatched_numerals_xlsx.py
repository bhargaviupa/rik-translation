#!/usr/bin/env python3
"""Spreadsheet of numeral [?] in a volume md that are still unmatched against the user's numeral file.
For each, the file rows on the page's LOCAL page (offset from exact matches) that are not already used by an exact
match are listed (closest digits first) with their Raw Line Context (file column E) for a context check."""
import argparse, re, collections, sys
from pathlib import Path
import openpyxl
from openpyxl.styles import Font, Alignment, PatternFill
from openpyxl.utils import get_column_letter
sys.path.insert(0, str(Path(__file__).resolve().parent))
import numeral_pageset as ps
ap = argparse.ArgumentParser(); ap.add_argument("--md", required=True); ap.add_argument("--num", required=True)
ap.add_argument("--out", required=True); ap.add_argument("--ncand", type=int, default=3)
a = ap.parse_args()
D2A = str.maketrans("०१२३४५६७८९", "0123456789")
NUMTOK = re.compile(r"([०-९0-9\[\]]+(?:[-–.,][ ]?[०-९0-9\[\]]+)*)\s*\[\?\]"); DEV = re.compile(r"[ऀ-ॿ]")
parts = lambda s: re.findall(r"\d+", s.translate(D2A))
rows_by_page = collections.defaultdict(list)
for r in list(openpyxl.load_workbook(a.num, read_only=True).active.iter_rows(values_only=True))[1:]:
    if isinstance(r[0], int):
        rows_by_page[r[0]].append(dict(page=r[0], line=r[1], val="-".join(parts(str(r[3]))), ctx=re.sub(r"\s+", " ", str(r[4] or ""))[:110]))
fp, mp = ps.load(a.md, a.num); OFF = ps.local_offsets(fp, mp)
lines = open(a.md, encoding="utf8").read().split("\n"); page = None; suk = "81"; out = []
# which md numerals on each page are exact matches (to consume pool values)
used = collections.defaultdict(collections.Counter)
for P, M in mp.items():
    pool = collections.Counter(v for k in OFF.get(P, [0]) for v in fp.get(P + k, []))
    for x in M:
        if not x["q"] and pool.get(x["val"], 0) > 0: pool[x["val"]] -= 1; used[P][x["val"]] += 1
for n, l in enumerate(lines, 1):
    m = re.match(r"#+\s*Page\s+(\d+)\s*\(PDF\s*(\d+)", l)
    if m: printed, page = int(m.group(1)), int(m.group(2))
    h = re.match(r"##\s+Sūkta\s+(\d+)", l)
    if h: suk = h.group(1)
    if page is None or "[?]" not in l or not DEV.search(l): continue
    for m in NUMTOK.finditer(l):
        pp = parts(m.group(1))
        if not pp: continue
        md = "-".join(pp)
        ks = OFF.get(page, [0, -1, 1])
        cand = []
        cnt = collections.Counter(used[page])
        for k in ks:
            for r in rows_by_page.get(page + k, []):
                if cnt.get(r["val"], 0) > 0: cnt[r["val"]] -= 1; continue          # used by an exact match
                if len(r["val"].split("-")) != len(pp): continue
                cand.append((ps.lev(md, r["val"]), r))
        cand.sort(key=lambda x: x[0])
        row = [n, printed, page, suk, "bhāṣya / Devanagari block" if l.lstrip().startswith(">") else "English note", md, m.group(1)]
        for d, r in cand[: a.ncand]: row += [r["val"], f"file p.{r['page']} line {r['line']} (Δ{d}): {r['ctx']}"]
        row += [""] * (2 * a.ncand - 2 * min(a.ncand, len(cand)))
        row += [re.sub(r"\s+", " ", l[max(0, m.start() - 70): m.end() + 25]), ""]
        out.append(row)
wb = openpyxl.Workbook(); ws = wb.active; ws.title = "Unmatched numerals"
hdr = ["md line (line no. in the .md file, NOT the book)", "printed page (book)", "our PDF page", "Sūkta (section)", "Where", "md digits (as read)", "md token (raw)"]
for i in range(1, a.ncand + 1): hdr += [f"numeral-file value {i}", f"numeral-file value {i}: file page / file line no. (Δ digits) + Raw Line Context (col E)"]
hdr += ["text around it in the md", "YOUR CORRECT DIGITS"]
ws.append(hdr)
for r in out: ws.append(r)
for c in ws[1]: c.font = Font(bold=True, color="FFFFFF"); c.fill = PatternFill("solid", fgColor="305496"); c.alignment = Alignment(wrap_text=True, vertical="top")
widths = [8, 9, 8, 10, 22, 14, 14] + [12, 48] * a.ncand + [70, 22]
for i, w in enumerate(widths, 1): ws.column_dimensions[get_column_letter(i)].width = w
for row in ws.iter_rows(min_row=2):
    for c in row: c.alignment = Alignment(wrap_text=True, vertical="top")
ws.freeze_panes = "A2"; ws.auto_filter.ref = ws.dimensions
wb.save(a.out); print(len(out), "rows ->", a.out)
