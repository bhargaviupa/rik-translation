# Vol 8 — to-do list (Nov 27 2026)

Done: supplied text `html/rig_8_1.md`, `rig_8_2.md` (pp. 2–832, 56 pictures); Kannada book pp. 2–832 (822 pages; gaps 161, 335, 361, 415, 416, 435, 507); `[?]` inventory 4,616 → **368 left** (212 latin, 154 inside our remarks, 2 number).

## A. Set-up — done
1. Supplied files, pictures, Kannada book, sieve (`review/second_pass/sieve*.tsv`), `qmarks.tsv`, `recheck_numbers.py 8` dry run (93 unambiguous reference corrections proposed in `review/recheck/numbers_candidates.tsv`, not applied), `refs_apply.py 8` preview.

## B. `[?]` pass — done
2. Pilot and 8 page batches (pp. 2–241, 550–559, old brief), `qmark_strip.py` (1,409 marks), 17 mark-only batches (pp. 242–549, 560–832). 26 batches, 5.04M tokens (`review/second_pass/batches.tsv`).
3. 21 Pratipadārtha words corrected in the Kannada book (`data/source_fixes.tsv`); 20 more certain candidates were not unique places.
4. Records: `findings.tsv` (3,131 rows), `kn_misprints.tsv`, `decided_by_default.tsv`, `open.tsv` (impossible printed numbers applied as printed), `questions.tsv` empty.

## C. Not done (not part of this pass)
5. The 368 marks left: Kannada misprints (kept English), places the Kannada does not settle, marks in our own remarks (`cleanup_remarks.py 8 all` later).
6. Page-by-page reading of pp. 242–832 against the Kannada for wrong numbers/names that carry no `[?]` (`tools/rv/SECOND_PASS_BRIEF.md`, about 8k tokens per page); `recheck_numbers.py 8 --write` for the 93 unambiguous reference corrections.
7. Sample check of Q2 removals (mark removed because the Kannada agrees): the first 13 mark batches accepted a match on the same page; tightened from batch 14.
8. NOTE conversion — skipped (user); accents; bhāṣya English; remark clean-up; review PDF; scan check; `batch.py audit 8` (no `volcfg.json`).
