#!/usr/bin/env python3
"""Apply the user's file value to every md numeral marked DIFFERENT in Vol7_file_vs_md.xlsx (user, Nov 4 2026: all DIFFERENT rows had
the correct value in his file). Same old value within +-8 lines (IAST twin, English renderings) gets the new value; [?] and 'as read'
brackets removed; md separators and digit script kept when the part count agrees. Skipped (listed in the log): rows whose part count differs (the file loses separators: 7-4-79 -> 7-479, 6-4-24 -> 6-4-24-4); md tokens that are plain
comma lists ('119, 124, 125'), edit distance >= 4."""
import re, sys, openpyxl
D2A = str.maketrans("०१२३४५६७८९", "0123456789"); A2D = str.maketrans("0123456789", "०१२३४५६७८९")
REF = re.compile(r"(\[?[०-९0-9]+\]?(?:[ ]?[-–.,][ ]?\[?[०-९0-9]+\]?)+)(\s*\[\?\])?")
md, xl, log = sys.argv[1:4]   # optional 4th arg --parts-ok: also apply rows whose part count differs (user confirmed Nov 4)
L = open(md, encoding="utf8").read().split("\n")
MINC = next((float(a.split("=")[1]) for a in sys.argv if a.startswith("--min-ctx=")), 0.0)   # only rows whose context score >= this
rows = [x for x in list(openpyxl.load_workbook(xl, read_only=True).active.iter_rows(values_only=True))[1:] if x[7] == "DIFFERENT" and (x[9] or 0) >= MINC]
def lev(a, b):
    p = list(range(len(b) + 1))
    for i, c in enumerate(a, 1):
        q = [i]
        for j, e in enumerate(b, 1): q.append(min(q[-1] + 1, p[j] + 1, p[j - 1] + (c != e)))
        p = q
    return p[-1]
f = open(log, "w", encoding="utf8"); f.write("md_line\tPDF\told\tnew\tnote\n"); done = set(); n_tok = n_skip = 0
for x in rows:
    P, ln, new, old = x[0], x[4], x[2], x[5]
    if re.search(r"\d\s*,\s*\d", x[6] or "") and "-" not in (x[6] or ""): f.write(f"{ln}\t{P}\t{x[6]}\t{new}\tSKIPPED plain list\n"); n_skip += 1; continue
    if "--parts-ok" not in sys.argv and len(old.split("-")) != len(new.split("-")): f.write(f"{ln}\t{P}\t{x[6]}\t{new}\tSKIPPED part count differs (file likely lost/moved a separator)\n"); n_skip += 1; continue
    if lev(old, new) >= 4: f.write(f"{ln}\t{P}\t{x[6]}\t{new}\tSKIPPED distance>=4\n"); n_skip += 1; continue
    for i in range(max(0, ln - 9), min(len(L), ln + 8)):
        if i in done: continue
        def rep(m):
            global n_tok
            if "-".join(re.findall(r"\d+", m.group(1).translate(D2A))) != old: return m.group(0)
            tok = m.group(1).replace("[", "").replace("]", ""); seps = re.findall(r"[ ]?[-–.,][ ]?", tok); np_ = new.split("-")
            out = "".join(p + (seps[k] if len(seps) == len(np_) - 1 else "-") if k < len(np_) - 1 else p for k, p in enumerate(np_))
            if re.search("[०-९]", tok): out = out.translate(A2D)
            n_tok += 1; f.write(f"{i+1}\t{P}\t{m.group(0)}\t{out}\t\n"); return out
        nl = REF.sub(rep, L[i])
        if nl != L[i]: L[i] = nl; done.add(i)
open(md, "w", encoding="utf8").write("\n".join(L)); print(len(rows), "DIFFERENT rows;", n_tok, "tokens changed;", n_skip, "rows skipped")
