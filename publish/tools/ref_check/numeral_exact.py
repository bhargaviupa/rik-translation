#!/usr/bin/env python3
"""Drop [?] on a numeral when its digits EXACTLY equal a row of the user's numeral file on the same page window
(file page in PDF-2..PDF; no Sanskrit-context requirement). Chance-match rate measured at ~0-1%.
  python3 numeral_exact.py --md MD --num XLSX [--apply] [--log LOG.tsv]
Never changes digits: only removes '[?]' (and the 'as read' brackets inside the token) on the Devanagari line, its IAST twin."""
import argparse, re, collections
from pathlib import Path
import openpyxl
D2A = str.maketrans("०१२३४५६७८९", "0123456789")
NUMTOK = re.compile(r"([०-९0-9\[\]]+(?:[-–.,][ ]?[०-९0-9\[\]]+)*)\s*\[\?\]")
DEV = re.compile(r"[ऀ-ॿ]")
def parts(s): return re.findall(r"\d+", s.translate(D2A))
ap = argparse.ArgumentParser(); ap.add_argument("--md", required=True); ap.add_argument("--num", required=True)
ap.add_argument("--apply", action="store_true"); ap.add_argument("--log", default="numeral_exact.log.tsv")
a = ap.parse_args()
fp = collections.defaultdict(set)
for r in list(openpyxl.load_workbook(a.num, read_only=True).active.iter_rows(values_only=True))[1:]:
    if isinstance(r[0], int): fp[r[0]].add("-".join(parts(str(r[3]))))
lines = Path(a.md).read_text(encoding="utf8").split("\n"); page = None; done = []
for n, l in enumerate(lines, 1):
    m = re.match(r"#+\s*Page\s+\d+\s*\(PDF\s*(\d+)", l)
    if m: page = int(m.group(1))
    if page is None or "[?]" not in l or not DEV.search(l): continue
    win = set().union(*(fp.get(p, set()) for p in range(page - 2, page + 2)))
    hits = [(i, mm) for i, mm in enumerate(NUMTOK.finditer(l)) if parts(mm.group(1)) and "-".join(parts(mm.group(1))) in win]
    if not hits: continue
    new = l
    for i, mm in sorted(hits, key=lambda x: -x[1].start()):
        tok = mm.group(1).replace("[", "").replace("]", "")
        new = new[:mm.start()] + tok + new[mm.end():]
        done.append((n, page, mm.group(1), "-".join(parts(mm.group(1)))))
    lines[n - 1] = new
    if l.lstrip().startswith(">"):
        j = n
        while j < len(lines) and lines[j].strip() == "": j += 1
        if j < len(lines) and lines[j].lstrip().startswith(("*", "> *")):
            t = lines[j]
            for i, mm in hits:
                ps = parts(mm.group(1))
                rx = re.compile(r"\[?" + r"[-–.,\s\[\]]*".join(ps) + r"\]?\s*\[\?\]")
                t = rx.sub(lambda x: re.sub(r"\s*\[\?\]$", "", x.group(0)).replace("[", "").replace("]", ""), t, count=1)
            lines[j] = t
print(len(done), "numerals confirmed by exact match on the page window")
if a.apply:
    Path(a.md).write_text("\n".join(lines), encoding="utf8")
    Path(a.log).write_text("\n".join("\t".join(map(str, d)) for d in done), encoding="utf8")
    print("applied; log", a.log)
