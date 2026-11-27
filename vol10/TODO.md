# Vol 10 — to-do list (Nov 27 2026)

Done: supplied text pp. 2–707 in `html/` (2 files); Kannada Text file pp. 2–707 (706 pages, no gaps); `[?]` inventory (`review/second_pass/qmarks.tsv`, 1,852 marks); decision: convert to NOTE style.

## A. Set-up
1. Merge `origin/main`; add Vol 10 to the table of `tools/rv/second_pass_prompt.py`; generate `docs/prompts/second_pass/VOL10.md`.
2. Look at the two head anomalies (pp. 530→580, 609→608), the extra marker at p. 58 and the 20 extracted pictures (`figures_sheet.py 10 --pdf`).
3. S0 sieve with full scope: `second_pass_sieve.py 10`, `qmark_resolve.py 10`, `recheck_numbers.py 10`, `refs_apply.py 10` (preview); letters of other scripts (Kannada p. 7 pages, English 4,753).

## B. Second pass (supplied text settles numerals and doubtful words)
4. Pilot: 10 middle pages, then batches of ~30 pages, one Sonnet reader at a time (`SECOND_PASS_BRIEF.md`); apply with `sp_apply.py`; every edit logged (`repair_log.md`, `data/source_fixes.tsv`); commit + push per batch.
5. Remove `[?]` where the supplied text confirms (numbers: 16 of 28 on pp. 2–379 so far); fix numbers from the Kannada; remove numbers the print lacks.
6. Word meanings: `pratipada_check.py 10 --source`, `pratipada_apply.py 10` (certain one-letter fixes only).
7. Misprints/doubts by rule: `kn_misprints.tsv`, `decided_by_default.tsv`; `questions.tsv` stays empty.
8. Structure checks: sūkta list (122–136) and Ṛk counts against Wikisource index; particulars lines; labels lost at page breaks; Sanskrit in Latin letters; Cyrillic in Latin words; Kannada script inside the English (674 lines).
9. Repairs applied (S3), checks rerun with before/after counts; `sp_report.py 10` → `STATUS_REPORT.md`.

## C. Convert to NOTE style
10. `to_note_style.py 10` trial → read report → `--easy --write`; remaining `[?]`/`[sic]` → `**NOTE**` + `review/notes.tsv`; 2 `**GLOSS**` markers stay (D9 blocks final copy).
11. Test each NOTE's premise against the Kannada, then `notes_resolve.py 10 --write` (default rule).
12. Accents: report only (`accent_volume.py`), no replacing without the user.

## D. Clean-up and PDF
13. `cleanup_remarks.py 10 all` dry run, read kept-in-part places, then `--write` (logged in `removed_remarks.tsv`).
14. Review-PDF steps of the pasted prompt (build before/after, `pdf_check.py 10`, pages as images, bold, Kannada script, quotation bars, page headings, contents page, dotted lines, tables); heading titles from the Kannada now possible.
15. Send `vol10/review/vol10_full.pdf` to the user for review.

## E. Quality and closing
16. Independent QA reader (24 pages, English vs Kannada), second reader if errors; count each kind over the whole volume.
17. `batch.py audit 10`, `check_labels.py`, `check_inline.py`.
18. Records: `vol10/STATUS.md`, `PUBLICATION_TODO.md`, `docs/LESSONS.md`; release gate items (D9, finishing checklist HANDBOOK §11).
19. Not now: bhāṣya English, dictionary, tags, scan check.
