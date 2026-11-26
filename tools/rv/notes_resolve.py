#!/usr/bin/env python3
"""Settle the NOTE questions of a volume by the user's rule (Nov 25 2026: no question lists for the editor).

  python3 tools/rv/notes_resolve.py N [--write]

Every row of volN/review/notes.tsv without a decision is settled by default: the English text is kept as it is, the **NOTE** mark stays in the
text (marks = rows is an audit gate), and the row is copied to
  review/kn_misprints.tsv      the question speaks of a misprint / misreading / garbled or doubtful Kannada word and the English has the sense the Kannada intends;
  review/decided_by_default.tsv  any other doubt;
and the `decision` column of notes.tsv says so. Columns of the two lists: page, place, as_found, question, why_not_settled, decision (docs/SECOND_PASS_REPORT.md).
Nothing in the translation is changed; a repair_log line says what was done. Preview unless --write."""
import datetime, pathlib, re, sys
ROOT = pathlib.Path(__file__).resolve().parents[2]
vol = sys.argv[1]; write = '--write' in sys.argv
d = ROOT / f'vol{vol}' / 'review'
rows = [l.rstrip('\n').split('\t') for l in open(d / 'notes.tsv', encoding='utf8') if l.strip()]      # plain tab split: the file is not quoted, a field may start with a quotation mark
head, body = rows[0], rows[1:]
MIS = re.compile(r'misprint|misread|garbled|printed (?:for|as)|as printed|as supplied|OCR|intended\?|reads |typo|wrong|\bfor\b.*\?|cut|truncated|damaged', re.I)
DEC_M = 'English kept (Kannada misprint or misreading; default rule, user Nov 25 2026)'
DEC_D = 'English kept unchanged (default rule, user Nov 25 2026)'
mis, dflt, n = [], [], 0
for r in body:
    r += [''] * (5 - len(r))
    if r[4].strip(): continue
    is_m = bool(MIS.search(r[2]))
    r[4] = DEC_M if is_m else DEC_D
    (mis if is_m else dflt).append([r[1], r[3].strip()[:80], '', r[2], 'doubt cannot be settled from the supplied text alone', r[4]]); n += 1
print(f'vol{vol}: {len(body)} rows, {n} undecided: {len(mis)} Kannada misprints, {len(dflt)} other doubts')
if not write: print('preview only; --write applies'); sys.exit()
def append(name, rs):
    p = d / name; new = not p.exists()
    with open(p, 'a', encoding='utf8', newline='') as f:
        if new: f.write('page\tplace\tas_found\tquestion\twhy_not_settled\tdecision\n')
        for r in rs: f.write('\t'.join(x.replace('\t', ' ') for x in r) + '\n')
append('kn_misprints.tsv', mis); append('decided_by_default.tsv', dflt)
with open(d / 'notes.tsv', 'w', encoding='utf8', newline='') as f:
    for r in [head] + body: f.write('\t'.join(r) + '\n')
with open(d / 'repair_log.md', 'a', encoding='utf8') as f:
    f.write(f'- {datetime.date.today()}: tools/rv/notes_resolve.py: {n} NOTE rows settled by the default rule (English kept): {len(mis)} to kn_misprints.tsv, {len(dflt)} to decided_by_default.tsv; decision column of notes.tsv filled; NOTE marks and text unchanged.\n')
