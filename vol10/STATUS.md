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
Built (`build_vol45.py 10 full`); `publish/out/vol10_full.pdf`.

## Pointers
`vol10/README.md`, `vol10/PHASE2_WORKER.md`.
