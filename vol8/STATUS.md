# Vol 8 — status

*Moved out of the general CLAUDE.md on Nov 8 2026. Update this file (not CLAUDE.md) whenever the state of this volume changes.*

## Scope
Maṇḍala 1 Sūktas 95–112 (Seventh Adhyāya; Sūkta 112 has 25 Ṛks, ends with the colophon and closing verses).

## Source and inputs
Scan `vol8/scans/Rig_Vol8.pdf` (852 PDF pp.); printed = PDF − 20. Clean 600-ppi alternate scan (branch `alt-scan-vol8`; alt PDF page = printed + 21).

## Outputs
`vol8/Rigveda_Samhita_Vol8_English_Translation.md` (+ docx/pdf).

## How it was made
Scan-based legacy workflow; numeral second pass (Pīṭhike pp. ii–ix and Sūktas 95–97 re-read from the alternate scan).

## Status
Translated. *Nov 27 2026: the old restriction "numeral corrections only" is lifted for the second pass (user, Nov 27 2026: resolve `[?]` from the supplied text, words included).*

## Open items
Numerals of Sūktas 98–112 only partly re-read (~280 flagged pages remain); 14 first-person phrases for `voice.EXACT`.

## Publication (print PDF)
Built with `build_vol45.py 8 full`; `vol8/review/vol8_full.pdf`.

## Pointers
`vol8/numerals/`, `publish/tools/numeral_pass/METHOD.md`.

- **Nov 18 2026, glosses (T12):** 71 more labelled glosses replaced by the marker `**GLOSS**` (214 markers in the volume now; removed text in `review/glosses_removed.tsv`, 22 labelled lines left in `review/glosses_left.tsv`); see `review/repair_log.md`. Unlabelled glosses not yet looked for. No final copy while a marker remains (D9).

- **Nov 27 2026, second pass (`[?]` and Kannada book):** supplied text `vol8/html/rig_8_1.md` (pp. 2–380) and `rig_8_2.md` (pp. 381–832), 56 pictures in `vol8/html/figures/`; Kannada book `Rigveda_Samhita_Vol8_Kannada_Text.md` pp. 2–832 (822 pages made; no page of its own: 161, 335, 361, 415, 416, 435, 507). `[?]` marks 4,616 → 368 (see `review/second_pass/STATUS_REPORT.md`, `TODO.md`); 21 Pratipadārtha words in the Kannada corrected (`data/source_fixes.tsv`). The numeral flags of Sūktas 98–112 above are settled from the supplied text, not from the alternate scan. 368 marks left: Kannada non-words/misprints (`review/second_pass/kn_misprints.tsv`), unsettled places (`decided_by_default.tsv`), and marks in our remarks.
