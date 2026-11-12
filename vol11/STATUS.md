# Vol 11 — status

*Moved out of the general CLAUDE.md on Nov 8 2026. Update this file (not CLAUDE.md) whenever the state of this volume changes.*

## Scope
Maṇḍala 1 Sūktas 137–157 (Second Adhyāya of the Second Aṣṭaka).

## Source and inputs
Scan in `vol11/scans/`.

## Re-translation from the supplied text (started Nov 12 2026)
`vol11/html/rig_11.md` = the user's `rig_11_1.md` (350 source pages, printed pp. 2–332) + `rig_11_2.md` (364 source pages, pp. 333–696), merged losslessly except for the converter's two `Pages: N/N` footer lines (removed); the originals are in the commit before the merge. The splitter finds 658 pages, printed 2–696, 37 numbers without a head of their own (6, 24, 42, 66, 78, 100, 104, 129, 137, 140, 144, 149, 160, 176, 180, 210, 211, 226, 250, 262, 266, 278, 314, 334, 350, 382, 416, 457, 458, 482, 496, 510, 514, 532, 590, 651, 668: pages that print no running head, merged into the page before). Head numbers repaired by the splitter's neighbour rule: 93→92, 153→155, 263→268, 533→535, 638→658, 693→695; **p. 211/212 is ambiguous** (head reads 211, rule gives 212, pages 210 and 211 have no head). 16 + 17 embedded pictures not yet extracted. The scan-based files above are still under the standard names (to be renamed `…_scan_…` before the new run).

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
