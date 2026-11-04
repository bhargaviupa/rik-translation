#!/usr/bin/env python3
"""Check md numerals WITHOUT [?] against the user's numeral file (file page = PDF page).
Per page: each certain md numeral (Devanagari-bearing non-italic lines) takes an exactly equal file entry (page P-1..P+1) if one exists (CONFIRMED);
otherwise it is listed with the closest file entries on its page (UNCONFIRMED). Report only; the md is not changed."""
import argparse, re, collections
import openpyxl
from openpyxl.styles import Font, Alignment, PatternFill
D2A = str.maketrans("०१२३४५६७८९", "0123456789"); DEV = re.compile(r"[ऀ-ॿ]")
REF = re.compile(r"(\[?[०-९0-9]+\]?(?:[ ]?[-–.,][ ]?\[?[०-९0-9]+\]?)+)(\s*\[\?\])?")
parts = lambda s: re.findall(r"\d+", s.translate(D2A))
def lev(x, y):
    d = list(range(len(y) + 1))
    for i, c in enumerate(x, 1):
        p, d[0] = d[0], i
        for j, e in enumerate(y, 1): p, d[j] = d[j], min(d[j] + 1, d[j - 1] + 1, p + (c != e))
    return d[-1]
ap = argparse.ArgumentParser(); ap.add_argument("--md", required=True); ap.add_argument("--num", required=True); ap.add_argument("--out", required=True); a = ap.parse_args()
fp = collections.defaultdict(list)
for r in list(openpyxl.load_workbook(a.num, read_only=True).active.iter_rows(values_only=True))[1:]:
    if isinstance(r[0], int):
        v = "-".join(parts(str(r[3])))
        if len(v.split("-")) >= 2: fp[r[0]].append((v, r[1]))
cur = None; printed = None; pg = collections.defaultdict(list)
for n, l in enumerate(open(a.md, encoding="utf8").read().split("\n"), 1):
    m = re.match(r"#+\s*Page\s+(\d+)\s*\(PDF\s*(\d+)", l)
    if m: printed, cur = int(m.group(1)), int(m.group(2))
    if cur is None or l.lstrip().startswith("*") or not DEV.search(l): continue
    for m in REF.finditer(l):
        ps = parts(m.group(1))
        if len(ps) >= 2 and not m.group(2) and "?" not in m.group(0):
            pg[cur].append((n, printed, "-".join(ps), re.sub(r"\s+", " ", l[max(0, m.start() - 80): m.end() + 20])))
ok = 0; bad = []
for P, M in sorted(pg.items()):
    pool = [(v, ln, p) for p in (P, P - 1, P + 1) for v, ln in fp.get(p, [])]
    left = list(pool); un = []
    for t in M:
        k = next((i for i, c in enumerate(left) if c[0] == t[2]), None)
        if k is None: k = next((i for i, c in enumerate(pool) if c[0] == t[2]), None); (left.remove(pool[k]) if k is not None and pool[k] in left else None)
        else: left.pop(k)
        if k is None: un.append(t)
        else: ok += 1
    for t in un:
        # closest among entries not exactly used on the page
        near = sorted(((lev(t[2], c[0]) + (0 if len(c[0].split("-")) == len(t[2].split("-")) else 3), c) for c in left))[:4]
        bad.append((P, t, near))
wb = openpyxl.Workbook(); ws = wb.active; ws.title = "Unconfirmed certain numerals"
ws.append(["PDF page", "printed", "md line", "md reading (no ?)", "text in md", "closest unused file entries (value | file line)", "YOUR ANSWER (C = md correct, or digits)"])
for P, t, near in bad:
    ws.append([P, t[1], t[0], t[2], t[3], "\n".join(f"{c[0]}  |  line {c[1]}  (page {c[2]}, dist {d})" for d, c in near) or "(none)", ""])
for c in ws[1]: c.font = Font(bold=True, color="FFFFFF"); c.fill = PatternFill("solid", fgColor="305496"); c.alignment = Alignment(wrap_text=True, vertical="top")
for i, w in enumerate([8, 8, 8, 18, 70, 60, 24]): ws.column_dimensions["ABCDEFG"[i]].width = w
for row in ws.iter_rows(min_row=2):
    for c in row: c.alignment = Alignment(wrap_text=True, vertical="top")
ws.freeze_panes = "A2"; ws.auto_filter.ref = ws.dimensions
wb.save(a.out)
tot = ok + len(bad); print(f"certain numerals: {tot}; confirmed by exact file entry: {ok}; unconfirmed: {len(bad)}")
d = collections.Counter(min((x[0] for x in n), default=99) for _, _, n in bad); print("nearest-entry distance of unconfirmed:", dict(sorted(d.items())))
