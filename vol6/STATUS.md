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
Built with `build_vol45.py 6 full`; `publish/out/vol6_full.pdf`.

## Pointers
`vol6/README.md`.

- **Nov 18 2026, glosses (T12):** 67 more labelled glosses replaced by the marker `**GLOSS**` (115 markers in the volume now; removed text in `review/glosses_removed.tsv`, 17 labelled lines left in `review/glosses_left.tsv`); see `review/repair_log.md`. Unlabelled glosses not yet looked for. No final copy while a marker remains (D9).

## Second pass (Nov 24 2026) — state
Report: `review/second_pass/STATUS_REPORT.md` (made by `tools/rv/sp_report.py 6`; format `docs/SECOND_PASS_REPORT.md`). S0 sieve: `review/second_pass/sieve.md` (with the S3 before/after table). S1: `Rigveda_Samhita_Vol6_Kannada_Text.md` made from the supplied text (618 page marks, pp. 2–619). S2: **all 618 printed pages read** in 22 batches by Sonnet readers (pilot pp. 300–309, then batches of about 30 pages); 1,188 findings, 871 applied (878 edits, none failed, each a line of `review/repair_log.md`), 317 questions (314 rows in `review/second_pass/questions.tsv`; most are Kannada misprints the English had silently corrected: the English is right, the Kannada text has the non-word; to be classified in bulk, not asked one by one). Kannada source edits: 1 (`data/source_fixes.tsv`, p. 300). Numbers and references were taken from the supplied Kannada (user, Nov 24); about 300 sūtra numbers that the English had and the print has not were removed; numbers that are impossible as printed (p. 370 `18-18-8`, p. 451 Pā. 9-2-2, p. 507) were applied as printed and listed in `review/second_pass/open.tsv` (open items: page boundaries shifted at pp. 72/73, 141/142, 232–235, 256/257, 315/316, 324/325, 471/472, 480/481, 570/571; the Kannada p. 66 marker; blocks not read: bhāṣya blocks with `[?]` numerals on pp. 268, 280, 284, 293).
S4: `review/second_pass/ws_coverage.tsv` — Maṇḍala 1 Sūktas 62–80, 185 Ṛks, each with Saṃhitā, Pada and bhāṣya in the Wikisource index, none missing, none twice; sūkta counts equal the index's `n_rik` (bhāṣya not translated: needs the user's decision, K4.3/F49). S5: `review/Vol6_pictures.pdf` (60 pictures: 56 verse/quotation pictures, 4 others). Picture 1 = the printed title page (Ṛgveda-saṃhitā, Bhāga 5, Sūktas 62–80); picture 2 = a portrait of a person in royal dress with a sword, picture 3 a seated person with white beard, picture 60 (p. 619) the goddess Durgā: the ornate cover of DESIGN 14.1 is not among pictures 1–2 of this file. Not part of this pass: the bhāṣya, `[?]`→NOTE, the scan check R7, PDFs.
