# Vol 13 — prompt to paste into a NEW, independent session

(Open a fresh Claude Code session on this repo. It is not coordinated by any other session. Paste everything below the line.)

---

You are starting Volume 13 of the Rigveda Samhita translation project (Kannada → English; repo bhargaviupa/rik-translation). Work on a new branch `claude/vol13` from origin/main (git push -u origin claude/vol13; no PRs; merge to main only when I say; never force-push). Read CLAUDE.md first, then vol13/README.md, vol13/vol13_state.md (set-up checklist) and vol13/vol13_runbook.md (draft runbook: the nine principles). For method, look at vol11's files (Rigveda_Samhita_Vol11_English_Translation.md and _Kannada_Text.md) and vol5/vol5_runbook.md (digit key).

SCANS: vol13/scans/ — 6 parts, 677 PDF pages, ~660–720 ppi 1-bit. vol13/tools/cfg.py maps global PDF page → part+page (`part_of`; `git lfs pull` if pointers). The older 300-dpi scan is Rig_Vol13.pdf at the repo root (fallback only).

KNOWN PROBLEM: several scan pages are upside down (180°), e.g. around PDF 6–7 and 10–11 (maybe more). vol13/tools/orient_v13.py (OCR in both orientations; keeps the one with more Kannada letters; writes vol13/review/orient_v13.json) is a locating aid: run it (python3 vol13/tools/orient_v13.py 1 677 4) unless the JSON is already on main, spot-check 6–8 pages visually, and make vol13/tools/view.py auto-rotate pages marked 180 so you never view an upside-down page.

TASKS (set-up checklist; do not start translating until I agree):
1. Page inventory: printed page number + header for every PDF page (even pages 'Maṃ. 1 A. N Sū. N', odd 'Aṣṭaka N, Adhyāya N, Varga N'); write vol13/review/page_map_v13.json; printed = PDF − k (note where k changes); list missing/duplicate/out-of-order pages; set OFFSET in vol13/tools/cfg.py. Numbers only from crops you viewed (OCR may only locate); verify every ~20th page and every offset change.
2. Read the contents table (around PDF 13–18) and Pīṭhike: record the Maṇḍala/Aṣṭaka/Adhyāya/Sūkta range, Ṛk counts, dvaipada sūktas, start page of each sūkta in vol13/vol13_state.md and README.
3. Digit key calibration (~20 headings + ~20 references at 300–450 dpi); record glyph rules in the runbook (2/7, 3/5, 6/7, 8/9).
4. Tools: crop by whole-page fractions; apply with unique-match asserts; lint (impossible references, Ṛk/sūkta numbering gaps, non-monotonic vargas); doubts page builder (vol13/tools/doubts_v13.py); Kannada→Devanagari→IAST by script (publish/tools/translit/). Test on 3 pages.
5. Sample quality test: 5 random pages incl. a dense reference page and a grammar page; report how legible small numerals are.
6. Update vol13/vol13_runbook.md (page-anchored file, Kannada file alongside the English as in Vol 11, per-unit doubts page, lint after each unit, 10% blind re-read audit, units of 15–25 pages, fresh session per unit, Sonnet-vs-Opus test on 5 pages). Then STOP and report: set-up results, scan quality, proposed plan and cost estimate.

HARD RULES: no OCR for readings (words/numbers only from crops you actually viewed); if an image view returns no image STOP and write nothing for that page; never fill from memory; `[?]` where unsure; Sanskrit always three layers (Devanagari + IAST + English); view crops, not whole pages at high dpi; keep replies short; commit and push after each task.
