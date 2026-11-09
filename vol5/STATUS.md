# Vol 5 — status

*Moved out of the general CLAUDE.md on Nov 8 2026. Update this file (not CLAUDE.md) whenever the state of this volume changes.*

## Scope
Maṇḍala 1 Sūktas 47–61 (Fourth Adhyāya) and the Kannada Pariśiṣṭa on the deities and persons of the Ṛgveda (printed pp. 531–708, translated at the user's request).

## Source and inputs
Scan `vol5/scans/Rig_Vol5.pdf` (724 pp.; printed = PDF − 16). Machine-read text `vol5/html/rig_5_1.html`, `rig_5_2.md` (used for the repair pilot).

## Outputs
`vol5/Rigveda_Samhita_Vol5_English_Translation.md` (+ docx/pdf).

## How it was made
Scan-based legacy workflow.

## Status
Translated and complete including the Pariśiṣṭa (printed pp. 1–529 and 531–708; p. 530 blank).

## Open items
Repair pilot: `[?]` in printed pp. 1–184 repaired against the supplied text (`vol5/review/html_repair_log.tsv`, tools `tools/rv/repair_worksheet.py`, `compare_html_scan.py`); the user judges disagreements. Vol 5 tests (`vol5/review/exp15`, `exp40`) are the basis of the decision to use the supplied text as base from Vol 15 on.

## Publication (print PDF)
Built with `build_vol45.py 5 full`; `publish/out/vol5_full.pdf`.

## Pointers
`vol5/README.md`.
