# Vol 9 — to-do list (Nov 27 2026)

Done (Nov 27 2026): supplied text pp. 2–603 in `html/` (2 files, 68 pictures in `html/figures/`); Kannada Text file pp. 2–603 (601 pages made, 0 gaps, 1 extra marker p. 361, head anomalies pp. 2, 36, 362, 597); `[?]` marks 1,921 → 40 (BLOCK 765, BARE 2, NUMREAD/NUMOK 599, readers 515); decision: legacy form, no NOTE conversion.

## A. Second pass of the `[?]` marks — finished
Records in `review/second_pass/` (`findings.tsv`, `batches.tsv`, `kn_misprints.tsv`, `decided_by_default.tsv`, `open.tsv`; `questions.tsv` empty; `STATUS_REPORT.md`).

## B. Open
1. 40 `[?]` left (Kannada non-words, front matter/progress note, sūtras the Kannada lacks): see `kn_misprints.tsv`, `decided_by_default.tsv`.
2. `open.tsv`: unmarked places where the English disagrees with the Kannada, and impossible printed numbers applied as printed. Not edited.
3. Done (Nov 27 2026): `pratipada_apply.py` on the Kannada Text file: 56 certain word fixes (`data/source_fixes.tsv`; 28 skipped: not one letter / not found once); `recheck_numbers.py 9 --apply`: 68 reference corrections from the Kannada (`repair_log.md`, tag NUMBER); 3 further proposals and 626 manual cases remain in `review/recheck/numbers_candidates.tsv`.
4. Optional full page-by-page reading (`SECOND_PASS_BRIEF.md`, about 8k tokens per page).

## C. Not now
NOTE conversion, accents, bhāṣya English, remark clean-up (`cleanup_remarks.py 9 all`) and review PDF, scan check.
