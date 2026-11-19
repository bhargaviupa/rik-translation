#!/usr/bin/env python3
"""List for the user, nothing applied: from a numeral_align_all.py report, (A) DIFFERENT file rows not applied (with the reason: part count,
distance, context, several file values for one md numeral), (B) md numerals still marked [?] / incomplete with no aligned file row, with the three
closest unmatched file rows, (C) NOT FOUND file rows that carry a Ṛgveda-style reference (>= 3 parts) as a count only.
  python3 numeral_for_user_tsv.py MD REPORT.xlsx APPLIED_LOG_TSV... --out OUT.tsv"""
import sys, re, collections, openpyxl
args = sys.argv[1:]; out = args[args.index("--out") + 1]; args = args[:args.index("--out")]
md, rep, logs = args[0], args[1], args[2:]
L = open(md, encoding="utf8").read().split("\n")
applied = set()
for lg in logs:
    for r in open(lg, encoding="utf8").read().split("\n")[1:]:
        c = r.split("\t")
        if len(c) >= 5 and not c[4].startswith("SKIPPED") and c[0].isdigit(): applied.add(int(c[0]))
def lev(a, b):
    p = list(range(len(b) + 1))
    for i, c in enumerate(a, 1):
        q = [i]
        for j, e in enumerate(b, 1): q.append(min(q[-1] + 1, p[j] + 1, p[j - 1] + (c != e)))
        p = q
    return p[-1]
wb = openpyxl.load_workbook(rep, read_only=True)
fr = list(wb["file rows vs md"].iter_rows(values_only=True))[1:]; mr = list(wb["md numerals vs file"].iter_rows(values_only=True))[1:]
cnt = collections.defaultdict(set)
for x in fr:
    if x[7] == "DIFFERENT": cnt[(x[4], x[5])].add(x[2])
def around(ln, tok):
    t = L[ln - 1]; k = (tok or "").split()[0].strip("[]") if tok else ""; i = max(t.find(k), 0) if k else 0
    return t[max(0, i - 60): i + 40].replace("\t", " ")
o = open(out, "w", encoding="utf8"); o.write("kind\tPDF page\tmd line\ttext value\tfile value\tfile line\tscore\tcontext\treason / closest unmatched file rows\ttext around the numeral\n")
nA = nB = 0
for x in fr:
    if x[7] != "DIFFERENT" or x[4] in applied: continue
    old, new = x[5], x[2]
    if old.endswith("-?"): why = "incomplete token, not applied (context or score below the threshold, or prefix differs)"
    elif len(old.split("-")) != len(new.split("-")): why = "part count differs"
    elif lev(old, new) >= 4: why = "edit distance >= 4"
    elif len(cnt[(x[4], old)]) > 1: why = "same md numeral paired with several file values"
    elif (x[9] or 0) < 0.8: why = "context below 0.8"
    else: why = "score below 0.85 or left alone after reading"
    nA += 1; o.write(f"DIFFERENT\t{x[0]}\t{x[4]}\t{x[6]}\t{new}\t{x[1]}\t{x[8]}\t{x[9]}\t{why}\t{around(x[4], x[6])}\n")
for y in mr:
    if str(y[5]).startswith("NOT IN FILE") and "[?]" in str(y[5]):
        nB += 1; o.write(f"md [?] no file row\t{y[0]}\t{y[2]}\t{y[4]}\t\t\t\t\t{str(y[10] or '').replace(chr(10), ' ; ')}\t{around(y[2], y[4])}\n")
nC = sum(1 for x in fr if x[7] == "NOT FOUND in md")
o.close(); print(f"A DIFFERENT not applied: {nA}; B md [?] without file row: {nB}; C NOT FOUND file rows (not listed, see the report sheet 'file rows vs md'): {nC}")
