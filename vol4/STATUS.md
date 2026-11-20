# Vol 4 — status

*Moved out of the general CLAUDE.md on Nov 8 2026. Update this file (not CLAUDE.md) whenever the state of this volume changes.*

## Scope
Maṇḍala 1 Sūktas 33–46 (Third Adhyāya of the First Aṣṭaka).

## Source and inputs
Scan `vol4/scans/`; printed page = PDF − 14.

## Supplied machine-read text (user, Nov 19 2026)
`vol4/html/rig_4_1.md` (front matter and printed pp. 2–286; heads read Maṇḍala 1 Sūktas 33–37) and `vol4/html/rig_4_2.md` (pp. 287–608, to Sūkta 46; ends with the closing lines "ಶುಭಂ ಭೂಯಾತ್ / ಮಂಗಳಂ"). Together the whole volume, pp. 2–608; 15 page numbers have no running head of their own (first pages of a sūkta or section, lesson 67). Changes made: the 38 embedded pictures moved to `vol4/html/figures/` (`tools/rv/extract_figures.py`); nothing else.

## Outputs
`vol4/Rigveda_Samhita_Vol4_English_Translation.md` (+ docx/pdf).

## How it was made
Scan-based legacy workflow.

## Status
Translated; file closed.

## Open items
None recorded beyond `[?]` readings.

## Publication (print PDF)
Built with `publish/build_vol45.py 4 full` (cleaner `vol45_clean.py`); `publish/out/vol4_full.pdf`.

## Pointers
`vol4/README.md`, `docs/HISTORY.md`.

- **Nov 18 2026, glosses (T12):** 49 more labelled glosses replaced by the marker `**GLOSS**` (82 markers in the volume now; removed text in `review/glosses_removed.tsv`, 31 labelled lines left in `review/glosses_left.tsv`); see `review/repair_log.md`. Unlabelled glosses not yet looked for. No final copy while a marker remains (D9).
