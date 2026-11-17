# Vol 2 — status

*Moved out of the general CLAUDE.md on Nov 8 2026. Update this file (not CLAUDE.md) whenever the state of this volume changes.*

## Scope
Maṇḍala 1 Sūktas 3–19 (First Adhyāya of the First Aṣṭaka).

## Source and inputs
Old single-file scan (printed = PDF − 15); better scans in `vol2/scans/` have their own page maps (see `vol2/vol2_runbook.md`).

## Outputs
`vol2/Rigveda_Samhita_Vol2_English_Translation.md` (+ docx/pdf).

## How it was made
Scan-based legacy workflow. A numeral/`[?]`/accent pass was agreed (user, Oct 27 2026; `vol2/vol2_runbook.md`, review files in `vol2/review/`).

## Status
Translated. The file is closed except for that agreed pass.

**Nov 17 2026: opened for the clean-up pass agreed with the user** (remove our remarks, verify accents; no re-translation). Prompt: `vol2/CLEANUP_PROMPT.md`; proposal: `vol2/review/cleanup_proposal.md` (Step A1 done, waiting for the user's yes); every change goes to `vol2/review/repair_log.md`.

## Open items
Old mid-file progress notes and a stray Cyrillic string in the file; varga numerals unreconciled with colophons; expert review wanted; `[?]` (see Vol 1).

## Publication (print PDF)
Built with `publish/build_vol2.py` + `vol2_clean.py`; `publish/out/vol2_full.pdf` (and `.html`).

## Pointers
`vol2/README.md`, `vol2/vol2_runbook.md`, `docs/HISTORY.md`.
