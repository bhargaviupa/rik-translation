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
Translated. **May be edited only for numeral corrections.**

## Open items
Numerals of Sūktas 98–112 only partly re-read (~280 flagged pages remain); 14 first-person phrases for `voice.EXACT`.

## Publication (print PDF)
Built with `build_vol45.py 8 full`; `publish/out/vol8_full.pdf`.

## Pointers
`vol8/numerals/`, `publish/tools/numeral_pass/METHOD.md`.

- **Nov 18 2026, glosses (T12):** 71 more labelled glosses replaced by the marker `**GLOSS**` (214 markers in the volume now; removed text in `review/glosses_removed.tsv`, 22 labelled lines left in `review/glosses_left.tsv`); see `review/repair_log.md`. Unlabelled glosses not yet looked for. No final copy while a marker remains (D9).
