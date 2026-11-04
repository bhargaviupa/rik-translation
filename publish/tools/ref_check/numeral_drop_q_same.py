#!/usr/bin/env python3
"""Drop '[?]' (and 'as read' brackets) on md numerals whose digits equal the aligned row of the user's file
(status 'SAME but md has [?]' in Vol7_file_vs_md.xlsx). Applies to the same value within +-8 lines (IAST twin, English renderings)."""
import re, sys, openpyxl
D2A = str.maketrans("०१२३४५६७८९", "0123456789")
REF = re.compile(r"(\[?[०-९0-9]+\]?(?:[ ]?[-–.,][ ]?\[?[०-९0-9]+\]?)+)(\s*\[\?\])")
md, xl, log = sys.argv[1:4]
L = open(md, encoding="utf8").read().split("\n")
rows = [x for x in list(openpyxl.load_workbook(xl, read_only=True).active.iter_rows(values_only=True))[1:] if x[7] == "SAME but md has [?]"]
n_tok = 0; f = open(log, "w", encoding="utf8"); f.write("md_line\tvalue\told\tnew\n")
for x in rows:
    ln, val = x[4], x[2]
    for i in range(max(0, ln - 9), min(len(L), ln + 8)):
        def rep(m):
            global n_tok
            if "-".join(re.findall(r"\d+", m.group(1).translate(D2A))) != val: return m.group(0)
            new = m.group(1).replace("[", "").replace("]", ""); n_tok += 1; f.write(f"{i+1}\t{val}\t{m.group(0)}\t{new}\n"); return new
        L[i] = REF.sub(rep, L[i])
open(md, "w", encoding="utf8").write("\n".join(L)); print(len(rows), "file rows;", n_tok, "tokens cleaned")
