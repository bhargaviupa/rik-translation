# Vol 14 — status

*Moved out of the general CLAUDE.md on Nov 8 2026. Update this file (not CLAUDE.md) whenever the state of this volume changes.*

## Scope
Maṇḍala 1 from Sūkta 185 to Maṇḍala 2 Sūkta 23 (Second Aṣṭaka, Adhyāyas 5–6), printed pp. 1–954.

## Source and inputs
**Key files (html-based, Vol 15 pipeline), complete for the supplied text:** `vol14/Rigveda_Samhita_Vol14_English_Translation.md` and `vol14/Rigveda_Samhita_Vol14_Kannada_Text.md`, printed **pp. 2–954**. Sources: `vol14/html/rig_14_1.md` (pp. 2–498; the user's two md files merged, pictures extracted to `vol14/html/figures_p1/` and marked `[figure: …]`) and `vol14/html/rig_14_2.html` (pp. 501–954, `figures/`). **Not in the supplied text: printed p. 1 (title page) and pp. 499–500** (Sūkta 5 Ṛk 5 Pada, bhāṣya, Pratipadārtha, Bhāvārtha, printed English); a bracketed note marks the gap before p. 501.
**Scan-based translation (old, whole volume pp. 1–954):** `vol14/Rigveda_Samhita_Vol14_scan_English_Translation.md`, kept for comparison (scans purged from git on Nov 8 2026). Legacy tools in `vol14/tools/` work on that file.

## Outputs
Key files above (English with three-layer Sanskrit and accents; Kannada with page markers). The Kannada file has page markers for pp. 2–954 except where the supplied text merges pages. Print PDFs: not built.

## How it was made
pp. 2–498: standing Sonnet agent, one 3-page window at a time (≈ 20–40k tokens per window; log in `vol14/parts/batch_costs_html2-498.md`; dispatcher notes in `vol14/review/html2-498/dispatcher_notes.md`). pp. 501–766: fresh agent per window (experiment, notes in `vol14/review/html501-766/`). pp. 767–954: earlier html pipeline. Pictures of the supplied text were read by the agents; only words that differed from the machine text were corrected, each with an italic note.

## Status
Html-based text complete for pp. 2–954 (Nov 9–10 2026), with the gaps above. Not merged into `main` yet.

## Open items
Obtain pp. 499–500 (and p. 1 if wanted) from the user; run accents/numeral checks; back-fill the unmarked doubts listed in `vol14/review/html2-498/dispatcher_notes.md`; user to settle the `[?]` readings (`vol14/review/html2-498/doubts.tsv`, `html501-766/doubts.tsv`). `[?]` and accent differences: `vol14/review/html501-766/doubts.tsv`, `accent_report.tsv` (pp. 501–766), `vol14/review/doubts.tsv`, `accent_report.tsv` (scan-based). Colon-joined references in windows 607, 634, 715 rewritten in words; Ṛk numbers missing from many supplied Saṃhitā lines were not added; ~20 figure-read blocks (see dispatcher notes). Printed p. 288 of the scan needs a re-scan (scan-based text only).

## IAST layer
Not stored in the English file (user decision, Nov 11 2026): the print build adds it for Saṃhitā and Pada blocks (`volcfg.json` `"iast_blocks": "build"`); stored runs were removed with `tools/rv/strip_iast.py` and logged in `review/repair_log.md`; bhāṣya blocks never get it.

## Publication (print PDF)
Not built yet. Use `publish/volbook.py` after normalising the file format (see `docs/REPO_REVIEW.md`).

## Pointers
`vol14/README.md`, `vol14/vol14_runbook.md`, `vol14/parts/session_state.md`.
