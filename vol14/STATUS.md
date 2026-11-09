# Vol 14 — status

*Moved out of the general CLAUDE.md on Nov 8 2026. Update this file (not CLAUDE.md) whenever the state of this volume changes.*

## Scope
Maṇḍala 1 from Sūkta 185 to Maṇḍala 2 Sūkta 23 (Second Aṣṭaka, Adhyāyas 5–6), printed pp. 1–954.

## Source and inputs
Printed pp. 1–766: scans (9 parts, 979 PDF pp., ~660 ppi — **removed from the working tree Nov 7 2026**). Printed pp. 767–954 (Maṇḍala 2 Sūktas 15–23): the user's machine-read text `vol14/html/rig_14_2.html` (+ `vol14/html/figures/`, 21 embedded pictures kept). Offset: printed = PDF − 18 to PDF 222, − 19 from PDF 224, − 20 from PDF 336 (PDF 223 and 335 are duplicates).

## Outputs
`vol14/Rigveda_Samhita_Vol14_English_Translation.md` (moved from the repository root on Nov 9 2026) and `vol14/Rigveda_Samhita_Vol14_Kannada_Text.md`.

## How it was made
pp. 1–766 scan-based (Sonnet/Opus translators, numerals from user files `vol14/numerals/`, `vol14/vol14_runbook.md`); pp. 767–954 with the Vol 15 pipeline on branch `claude/vol14-html`; verse blocks later corrected from the embedded pictures.

## Status
Fully translated (Nov 5 2026). `vol14/vol14_state.md` is **out of date** (still says 'in progress, p. 371').

## Open items
Sūkta 18 Ṛk 4 Saṃhitā was missing in the supplied text (now read from the embedded picture; `vol14/review/todo_missing.md`); `[?]` and accent differences in `vol14/review/doubts.tsv`, `accent_report.tsv`; accents for the Maṇḍala 1 part still to run; printed p. 288 needs a re-scan (right edge cut off); Kannada text covers only the html part.

## Publication (print PDF)
Not built yet. Use `publish/volbook.py` after normalising the file format (see `docs/REPO_REVIEW.md`).

## Pointers
`vol14/README.md`, `vol14/vol14_runbook.md`, `vol14/parts/session_state.md`.
