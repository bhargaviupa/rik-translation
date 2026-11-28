# Vol 7 — status

*Moved out of the general CLAUDE.md on Nov 8 2026. Update this file (not CLAUDE.md) whenever the state of this volume changes.*

## Scope
Maṇḍala 1 Sūktas 81–94 (Sixth Adhyāya).

## Source and inputs
Scan in `vol7/scans/`; printed = PDF − 15.

## Outputs
`vol7/Rigveda_Samhita_Vol7_English_Translation.md` (+ docx/pdf).

## How it was made
Scan-based legacy workflow, then **reopened** for the reference-text pilot (Müller's edition, `muller-655-900.pdf`, via `publish/tools/ref_check/ref_check.py`) and the user's numeral file (`vol7/numerals/`, see its README; 35 `[?]` numerals dropped where the file agreed, 29 differing values not applied).

## Status
Translated; reopened for the pilots above.

## Open items
Still to check: p. 198 `व्यत्ययेन मध्यमः [?]`. See `docs/LEGACY_SCAN_WORKFLOW.md` (reference-text pilot, numeral files).

## Publication (print PDF)
Built with `build_vol45.py 7 full` (cleaner `vol67_clean.py`); `vol7/review/vol7_full.pdf`.

## Pointers
`vol7/numerals/README.md`.

- **Nov 18 2026, glosses (T12):** 39 more labelled glosses replaced by the marker `**GLOSS**` (248 markers in the volume now; removed text in `review/glosses_removed.tsv`, 2 labelled lines left in `review/glosses_left.tsv`); see `review/repair_log.md`. Unlabelled glosses not yet looked for. No final copy while a marker remains (D9).

- **Nov 27 2026, second pass (`[?]` and Kannada book):** supplied text `vol7/html/rig_7_1.md` and `rig_7_2.md` (pp. 2–567; 27 pictures in `vol7/html/figures/`); Kannada book `Rigveda_Samhita_Vol7_Kannada_Text.md` pp. 2–567 (564 pages made, no page of its own: 361). `[?]` marks 1,939 → 341 (see `review/second_pass/STATUS_REPORT.md`, `TODO.md`); 20 Pratipadārtha words in the Kannada corrected (`data/source_fixes.tsv`). 341 marks left: 51 inside the closing Progress note (never edited by hand), the rest Kannada non-words/misprints (`review/second_pass/kn_misprints.tsv`), unsettled places (`decided_by_default.tsv`) and 40 in our remarks.
