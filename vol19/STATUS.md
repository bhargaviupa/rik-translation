# Vol 19 — status

## Scope
Ṛgveda-saṃhitā Maṇḍala 5, Sūktas 9–62 (from the title page and contents of the supplied text); Aṣṭaka 4, Adhyāyas 1–3; printed pp. 1–852. Expected from Vol 18's end (Sūkta 9); the Sūkta heading sequence is checked at the stage checks.

## Source and inputs
`vol19/html/rig_19.md`: the user's two files (`rig_19_1.md`, `rig_19_2.md`; supplied Nov 17 2026) merged losslessly with `tools/rv/merge_md.py` (809 page splits identical before and after). Changes made, all mechanical: 80 embedded pictures extracted to `vol19/html/figures/` and replaced by `[figure: …]` lines; the two converter footer lines `Pages: N/N` removed; **one line `<!-- page 1 -->` inserted before the opening "ॐ" of the body** (line 486; printed p. 1 prints no running head).
The page splitter finds 810 of the 852 printed pages. **Printed page numbers with no running head (42, the translator marks them):** 4, 10, 35, 48, 90, 92, 97, 134, 162, 176, 194, 213, 236, 245, 258, 262, 278, 308, 349, 366, 390, 404, 411, 413, 417, 436, 456, 477, 512, 516, 525, 528, 542, 564, 568, 594, 600, 722, 764, 782, 791, 808.
Front matter (lines 1–485, no window covers it): title pages and board of scholars; **preface (ಪೀಠಿಕೆ) lines 119–176, signed 18-5-1953**; contents from line 181 (partly tables); list of abbreviations. `vol19/html/_layout.json` records these (end lines approximate). Page-head anomalies (misread numbers, e.g. p. 407 read as 107) are listed by `html_pages.py`; the splitter's used numbers follow the sequence. `volcfg.json`: `source` = `rig_19.md@1-852`, window 6, `mandalas` [5], conventions of Vol 18, `printed_english_label` "English translation". No scans.

## Status
Done through printed p. 0 (prepared; no window translated).

## Open items
1. Preface translation (one agent, into `vol19/work/preface/en.md`): after the first batch, with the user's yes.
