# Vol 14 — status

*Moved out of the general CLAUDE.md on Nov 8 2026. Update this file (not CLAUDE.md) whenever the state of this volume changes.*

## Scope
Maṇḍala 1 from Sūkta 185 to Maṇḍala 2 Sūkta 23 (Second Aṣṭaka, Adhyāyas 5–6), printed pp. 1–954.

## Source and inputs
**Key files (html-based, Vol 15 pipeline):** `vol14/Rigveda_Samhita_Vol14_English_Translation.md` and `vol14/Rigveda_Samhita_Vol14_Kannada_Text.md`. Today they hold printed **pp. 501–954** only: pp. 501–766 re-translated from the user's machine-read text (experiment on `claude/vol14-exp`, 89 windows; notes and word-level comparison with the scan-based text in `vol14/review/html501-766/`) joined (Nov 9 2026) to pp. 767–954 (earlier html translation). Source: `vol14/html/rig_14_2.html` (+ `figures/`, pictures read by the agents where the machine reader gave garbage).
**Printed pp. 1–500** (Maṇḍala 1 Sūktas 185–191, Maṇḍala 2 Sūktas 1–5): waiting for the user's machine-read files; to be translated with the standing-agent method and put in front of p. 501.
**Scan-based translation (old, whole volume pp. 1–954):** `vol14/Rigveda_Samhita_Vol14_scan_English_Translation.md` (kept for comparison and as the interim text of pp. 1–500; scans were purged from git on Nov 8 2026; offset printed = PDF − 18 to PDF 222, − 19 from PDF 224, − 20 from PDF 336). Legacy tools in `vol14/tools/` work on this file.

## Outputs
Key files above; scan-based file as named. The Kannada key file has page markers for printed pp. 501–954 (p. 537 is not a separate page in the supplied text).

## How it was made
pp. 501–766: fresh Sonnet agent per 3-page window (~100k tokens each), figures read by the agents, dispatcher notes in `vol14/review/html501-766/dispatcher_notes.md`; pp. 767–954: Vol 15 pipeline; pp. 1–500 (scan-based, old): Sonnet/Opus translators with numeral files `vol14/numerals/`.

## Status
Html-based text: pp. 501–954 done and joined; pp. 1–500 outstanding. Scan-based text: whole volume done (Nov 5 2026).

## Open items
Wait for the html of pp. 1–500; then `batch.py` windows from p. 1 (standing agent). `[?]` and accent differences: `vol14/review/html501-766/doubts.tsv`, `accent_report.tsv` (pp. 501–766), `vol14/review/doubts.tsv`, `accent_report.tsv` (scan-based). Colon-joined references in windows 607, 634, 715 rewritten in words; Ṛk numbers missing from many supplied Saṃhitā lines were not added; ~20 figure-read blocks (see dispatcher notes). Printed p. 288 of the scan needs a re-scan (scan-based text only).

## Publication (print PDF)
Not built yet. Use `publish/volbook.py` after normalising the file format (see `docs/REPO_REVIEW.md`).

## Pointers
`vol14/README.md`, `vol14/vol14_runbook.md`, `vol14/parts/session_state.md`.
