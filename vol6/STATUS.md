# Vol 6 — status

*Moved out of the general CLAUDE.md on Nov 8 2026. Update this file (not CLAUDE.md) whenever the state of this volume changes.*

## Scope
Maṇḍala 1 Sūktas 62–80 (Fifth Adhyāya).

## Source and inputs
Scan `vol6/scans/Rig_Vol6.pdf` (638 PDF pp.); printed = PDF − 18.

## Supplied machine-read text (user, Nov 19 2026)
`vol6/html/rig_6_1.md` (front matter and printed pp. 2–81, Sūktas 62–63), `rig_6_2.md` (pp. 83–382, to Sūkta 73) and `rig_6_3.md` (pp. 383–619, to the end: it closes with the printer's line). `rig_6_1_0.md` is printed p. 82 alone (supplied separately Nov 19 2026; it joins p. 81 and p. 83 without a gap: the word-meaning list of Sūkta 63 Ṛk 6 ends on p. 81, p. 82 opens with its Bhāvārtha, and its last sentence runs on into p. 83). **The supplied text covers the whole volume, pp. 2–619.** The 60 embedded pictures were moved to `vol6/html/figures/` (`tools/rv/extract_figures.py`); nothing else changed.

## Outputs
`vol6/Rigveda_Samhita_Vol6_English_Translation.md` (+ docx/pdf).

## How it was made
Scan-based legacy workflow.

## Status
Translated; file closed.

## Open items
`[?]` readings only.

## Publication (print PDF)
Built with `build_vol45.py 6 full`; `vol6/review/vol6_full.pdf`.

## Pointers
`vol6/README.md`.

- **Nov 18 2026, glosses (T12):** 67 more labelled glosses replaced by the marker `**GLOSS**` (115 markers in the volume now; removed text in `review/glosses_removed.tsv`, 17 labelled lines left in `review/glosses_left.tsv`); see `review/repair_log.md`. Unlabelled glosses not yet looked for. No final copy while a marker remains (D9).
