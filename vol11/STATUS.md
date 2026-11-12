# Vol 11 — status

*Moved out of the general CLAUDE.md on Nov 8 2026. Update this file (not CLAUDE.md) whenever the state of this volume changes.*

## Scope
Maṇḍala 1 Sūktas 137–157 (Second Adhyāya of the Second Aṣṭaka).

## Source and inputs
Scan in `vol11/scans/`.

## Re-translation from the supplied text (started Nov 12 2026)
`vol11/html/rig_11.md` = the user's `rig_11_1.md` (350 source pages, printed pp. 2–332) + `rig_11_2.md` (364 source pages, pp. 333–696), merged losslessly except for the converter's two `Pages: N/N` footer lines (removed); the originals are in the commit before the merge. The splitter finds 658 pages, printed 2–696, 37 numbers without a head of their own (6, 24, 42, 66, 78, 100, 104, 129, 137, 140, 144, 149, 160, 176, 180, 210, 211, 226, 250, 262, 266, 278, 314, 334, 350, 382, 416, 457, 458, 482, 496, 510, 514, 532, 590, 651, 668: pages that print no running head, merged into the page before). Head numbers repaired by the splitter's neighbour rule: 93→92, 153→155, 263→268, 533→535, 638→658, 693→695; **p. 211/212 is ambiguous** (head reads 211, rule gives 212, pages 210 and 211 have no head). Decisions of the user (Nov 12 2026): all pages exist even where the number is not printed (the translator marks them); **printed p. 1 prints no number: `<!-- page 1 -->` inserted before the opening "ॐ" (line 591)**; **p. 212 is not decided: the mark `**NOTE**{printed page number 212? …}` goes on that page** (`page_notes` in `volcfg.json`, shown in the window's TASK.md); route = Batch API (`tools/rv/api_batch.py`); conventions of Vols 17–18 (`note_style` NOTE, bhāṣya block Devanagari only, grammar in Sanskrit, layout subheads). The 33 embedded pictures were extracted by `tools/rv/extract_figures.py` to `vol11/html/figures/` (`fig_lineNNNNN.ext`, N = line in `rig_11.md`) and replaced by `[figure: …]` lines. The scan-based files were renamed `Rigveda_Samhita_Vol11_scan_English_Translation.*` / `…_scan_Kannada_Text.*` (md, docx, pdf; kept for comparison); the standard names now belong to the new run (`volcfg.json`, window 6). Scripts of the old build (`publish/`, `publish/tools/verify11/`) still point to the old names: update them when the new Vol 11 is built.

## Outputs
`vol11/Rigveda_Samhita_Vol11_English_Translation.md` and `…_Kannada_Text.md` (+ docx/pdf each).

## How it was made
Scan-based legacy workflow; accents by `accent_volume.py` (first volume with accents by script); Kannada text built alongside (decision Oct 2026).

## Status
Translated; accented; Kannada text exists.

## Open items
Verification pass: `docs/SESSION_REPORT_Vol11_verification.md`, `docs/VERIFY_PASS_REQUIREMENTS.md`, `publish/tools/verify11/`.

## Publication (print PDF)
Built with `build_vol45.py 11 full` (accent CSS); `publish/out/vol11_full.pdf`.

## Pointers
`docs/SESSION_REPORT_Vol11_verification.md`.
