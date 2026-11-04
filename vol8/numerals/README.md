# Vol 8 numeral file (user, Nov 4 2026): `Rigveda_Numerals_Lines_8_6_852.xlsx`
3,683 rows (pages 7–851); **file page = PDF page** (offset 0: 2,149 exact value overlaps vs ≤ 94 at any other offset). Method and rules: `publish/tools/ref_check/NUMERAL_FILE_LESSONS.md`.
First report (`numeral_align_all.py`): SAME 2,097, SAME-but-md-has-[?] 90, DIFFERENT 984, NOT FOUND 512. Spot rows on printed p. ii (file p. 7) match as in Vol 7.
Applied: `[?]` dropped on the 90 numerals equal to the aligned file row (`numeral_drop_q_same.applied.tsv`). DIFFERENT rows NOT applied (Vol 7 lesson: pairings are unreliable; the user marks `Vol8_file_vs_md.xlsx`).

## DIFFERENT rows applied (user, Nov 4 2026: "I checked the different; get the correct value from my file for all")
`numeral_apply_different.py … --parts-ok`: **819 tokens** (Devanagari lines, IAST twins, English renderings within ±8 lines) now carry the file's value; `[?]` removed. Log `numeral_apply_different.applied.tsv`. **64 rows skipped** (63 edit distance ≥ 4, 1 plain list; marked SKIPPED in the log): they pair two different references (e.g. md 9-114-3 vs file 8-25-3 on p. 7). Re-run of the alignment after the edit: `Vol8_file_vs_md_after.xlsx`.

## Second apply (user, Nov 4 2026: "all different are ok" on `Vol8_file_vs_md_after.xlsx`)
236 more tokens changed (log `numeral_apply_different_2.applied.tsv`); 61 rows still skipped (60 edit distance ≥ 4, 1 plain list). Re-run: `Vol8_file_vs_md_after2.xlsx` — SAME 2,993, DIFFERENT 225, NOT FOUND 508 (each round exposes new pairings; the remaining DIFFERENT rows shrink: 986 → 367 → 225).
