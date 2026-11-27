# Vol 10 — status

*Moved out of the general CLAUDE.md on Nov 8 2026. Update this file (not CLAUDE.md) whenever the state of this volume changes.*

## Scope
Maṇḍala 1 Sūktas 122–136 (First Adhyāya of the Second Aṣṭaka), printed pp. 2–707.

## Source and inputs
`vol10/scans/Rig_Vol10.pdf` (728 PDF pp.) — **scan PDFs removed from the working tree on Nov 7 2026** (user); restore with `git checkout <commit> -- <path>` (see `vol10/scans/README.md`). Printed = PDF − 21 (header 'Maṃ. 1 A. 18 Sū. N').

## Outputs
`vol10/Rigveda_Samhita_Vol10_English_Translation.md` (+ docx/pdf).

## How it was made
Scan-based legacy workflow. Numeral aids were dropped (they did not help); a separate numeral pass is to follow.

## Status
Fully translated.

## Open items
The user's numeral files (`vol10/numerals/*.xlsx`, see its README) are available for the numeral pass (`publish/tools/numeral_pass/METHOD.md`). Open flags are in the progress note at the end of the English file.

## Publication (print PDF)
Built (`build_vol45.py 10 full`); `vol10/review/vol10_full.pdf`.

## Pointers
`vol10/README.md`, `vol10/PHASE2_WORKER.md`.

- **Nov 18 2026, glosses (T12):** 2 more labelled glosses replaced by the marker `**GLOSS**` (2 markers in the volume now; removed text in `review/glosses_removed.tsv`, 5 labelled lines left in `review/glosses_left.tsv`); see `review/repair_log.md`. Unlabelled glosses not yet looked for. No final copy while a marker remains (D9).

- **Nov 27 2026 (user): Vol 10 is to be converted to `**NOTE**` style** (`notes.tsv`, no `[?]`/`[sic]`) — not kept in the legacy `[?]` form of Vols 2–6. Order: (1) second pass on the supplied text (rig_10 files settle numerals and doubtful words; part 1 = pp. 2–379 supplied, Kannada Text made; part 2 pp. ~380–707 not yet supplied), (2) `[?]` that the supplied text does not settle, and `[sic]`, converted by the shared tool (`tools/rv/to_note_style.py`), (3) `notes_resolve.py` by the default rule. Nothing converted yet.

- **Nov 27 2026 (user), superseding the entry above: the NOTE conversion is skipped.** Vol 10 stays in the legacy `[?]`/`[sic]` form (as Vols 2–6); the second pass removes a `[?]` only where the supplied text (rig_10 files) settles it. Saṃhitā, Pada and bhāṣya come from the Wikisource reference and are not touched. To-do list: `vol10/TODO.md`. Supplied text and Kannada Text file for pp. 2–707 exist.

- **Nov 27 2026, `[?]` marks: 1,852 → 35** (counted by Python over the English file). Stages: `qmark_strip.py 10 --write` (753: Sanskrit blocks 597, as-read references settled from the Kannada page 141, boilerplate remarks 15), then five mark-only reader batches (`tools/rv/QMARK_READER_BRIEF.md`; marks of pp. 2–368, 350–499, 500–579, 580–619, 620–659, 660–707: 810 removed, 33 kept) after the first page-by-page batches (pp. 300–309, 2–211: 58 removed). The 35 left: kept on Kannada non-words or an undecidable different reading (rows in `review/second_pass/kn_misprints.tsv`, `decided_by_default.tsv`), front-matter pages the supplied text does not carry, and 2 inside the closing progress note. Pages 212–299 and 310–349 had only the mark-only treatment, not the full page-by-page reading (wrong numbers/names without a mark are not looked for there; `open.tsv` lists unmarked numbers that disagree with the Kannada). `[sic]` 38 and `**GLOSS**` 2 unchanged. Kannada Text file and supplied text: pp. 2–707. Report: `review/second_pass/STATUS_REPORT.md`. Not done: remark clean-up (`cleanup_remarks.py 10 all`), PDF, NOTE conversion (skipped by the user).
