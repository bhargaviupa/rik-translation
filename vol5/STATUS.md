# Vol 5 — status

*Moved out of the general CLAUDE.md on Nov 8 2026. Update this file (not CLAUDE.md) whenever the state of this volume changes.*

## Scope
Maṇḍala 1 Sūktas 47–61 (Fourth Adhyāya) and the Kannada Pariśiṣṭa on the deities and persons of the Ṛgveda (printed pp. 531–708, translated at the user's request).

## Source and inputs
Scan `vol5/scans/Rig_Vol5.pdf` (724 pp.; printed = PDF − 16). Machine-read text in `vol5/html/` (user, Nov 17 2026; replaces the two files of the repair pilot, `rig_5_1.html` and the old `rig_5_2.md`, which read the same pages: median likeness of the Kannada letters per page 99.45 %): `rig_5_1.md` (front matter and printed pp. 2–83), `rig_5_2.md` (pp. 85–184; no head for 131, 154, 180), `rig_5_3.md` (pp. 185–286; no head for 193, 232, 233, 260), `rig_5_6.md` (pp. 486–584; no head for 506, 514, 518, 530, 542, 559, 566, 578). `rig_5_45.md` (pp. 273–468, supplied later the same day; **pp. 273–286 stand in both file 3 and this file**: which copy is used is decided when the volume is prepared). `rig_5_7.md` (pp. 584–708, the end of the volume with the printer's line; supplied Nov 19 2026; p. 584 stands in both file 6 and this file). **Not yet supplied: pp. 468–485** (file 45 ends at p. 467, file 6 begins at p. 486). Page numbers without a running head are first pages of a sūkta or section (lesson 67) and are not listed for this file. The 32 embedded pictures were moved to `vol5/html/figures/` by `tools/rv/extract_figures.py` (which now also reads pandoc's `<img src="data:…">` form); nothing else was changed. Page 84 has no head of its own (the last head of file 1 reads 84 and is taken as 83 by the splitter: to be looked at).

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
