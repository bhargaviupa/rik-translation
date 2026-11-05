# Vol 9 numeral files (user, Nov 5 2026)
`Rigveda_Clean_Numerals_9_1_100.xlsx` (PDF 2–100, 422 rows) + `Rigveda_Clean_Numerals_9_101_623.xlsx` (2,330 rows) merged into `Rigveda_Numerals_Lines_9_2_623.xlsx`. **File page = PDF page** (1,212 exact overlaps at offset 0; ≤ 74 elsewhere). Page headings in the md read `### Printed p. N (PDF M)` (script updated). Method: `publish/tools/ref_check/NUMERAL_FILE_LESSONS.md`.
First alignment (`Vol9_file_vs_md.xlsx`): SAME 1,449, SAME-but-md-has-[?] 8, DIFFERENT 616, NOT FOUND 723.
Applied: `[?]` dropped on rows equal to the file (`numeral_drop_q_same.applied.tsv`). DIFFERENT rows not applied yet (waiting for the user).

## DIFFERENT rows applied (user, Nov 5 2026: "all are correct in my file")
Incomplete md tokens (`4-?`, `3-?? as read [?]`) are now read and replaced by the file's full value (170); multi-reference lines (e.g. file p. 177 line 21: Ni. 3-7 and 4-2) apply both values in order. `numeral_apply_different.py … --parts-ok` on `Vol9_file_vs_md_inc.xlsx`: **647 tokens changed**, log `numeral_apply_different.applied.tsv`; 34 rows skipped (30 edit distance ≥ 4, 4 incomplete tokens whose prefix differs). Re-run after the edit: `Vol9_file_vs_md_after.xlsx` — SAME 1,897, DIFFERENT 274, NOT FOUND 625.
