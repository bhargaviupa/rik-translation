#!/usr/bin/env python3
"""xlsx of OUR file's data only, one row per remaining [?] on Devanagari-bearing lines:
page nr | Kannada extract (our Devanagari reading re-written in Kannada script by script) | our reading | English translation."""
import argparse, re, sys
from pathlib import Path
import openpyxl
from openpyxl.styles import Font, Alignment, PatternFill
from openpyxl.utils import get_column_letter
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "translit"))
from deva_to_kannada import deva2kn
ap = argparse.ArgumentParser(); ap.add_argument("--md", required=True); ap.add_argument("--out", required=True)
ap.add_argument("--printed-offset", type=int, default=15); a = ap.parse_args()
L = open(a.md, encoding="utf8").read().split("\n"); dev = re.compile(r"[ऀ-ॿ]")
D2K = str.maketrans("0123456789", "೦೧೨೩೪೫೬೭೮೯"); D2A = str.maketrans("०१२३४५६७८९", "0123456789")
def kn(s): return deva2kn(s).translate(D2K)
def english_for(i, l):
    if not l.lstrip().startswith(">"): return re.sub(r"\s+", " ", l.strip())[:1200]            # English note line itself
    for j in range(i + 1, min(i + 14, len(L))):
        if L[j].lstrip().startswith("*Translation") or L[j].lstrip().startswith("*Sense"): return re.sub(r"\s+", " ", L[j])[:1200]
        if L[j].lstrip().startswith(">") and j > i + 1: break
    return ""
rows = []; page = None; printed = None
for i, l in enumerate(L):
    m = re.match(r"#+\s*Page\s+(\d+)\s*\(PDF\s*(\d+)", l)
    if m: printed, page = int(m.group(1)), int(m.group(2))
    if page is None or "[?]" not in l or not dev.search(l) or l.lstrip().startswith("*"): continue
    en = english_for(i, l)
    for m in re.finditer(r"\[\?\]", l):
        pre = l[max(0, m.start() - 9): m.start()]
        isnum = bool(re.search(r"[०-९0-9\]]", pre))
        ctx = l[max(0, m.start() - 70): m.end() + 25]
        if isnum:
            t = re.search(r"([०-९0-9\[\]]+(?:\s*[-–.,]\s*[०-९0-9\[\]]+)*)\s*\[\?\]$", l[:m.end()])
            reading = (t.group(1) if t else pre) + "  [?]"
        else:
            w = re.findall(r"[ऀ-ॿ]+", l[max(0, m.start() - 40): m.start()])
            reading = (w[-1] if w else "") + "  [?]"
        rows.append([page, printed, kn(ctx), reading, en, i + 1])
wb = openpyxl.Workbook(); ws = wb.active; ws.title = "Our reading"
ws.append(["page nr (our PDF page)", "printed page (book)", "Kannada extract (our reading in Kannada script; [?] = doubtful)", "our reading (doubtful item)", "English translation (our file)", "md line (to merge back; may be deleted)"])
for r in rows: ws.append(r)
for c in ws[1]: c.font = Font(bold=True, color="FFFFFF"); c.fill = PatternFill("solid", fgColor="305496"); c.alignment = Alignment(wrap_text=True, vertical="top")
for i, w in enumerate([12, 10, 60, 22, 90, 12], 1): ws.column_dimensions[get_column_letter(i)].width = w
for row in ws.iter_rows(min_row=2):
    for c in row: c.alignment = Alignment(wrap_text=True, vertical="top")
ws.freeze_panes = "A2"; ws.auto_filter.ref = ws.dimensions
wb.save(a.out); print(len(rows), "rows ->", a.out)
