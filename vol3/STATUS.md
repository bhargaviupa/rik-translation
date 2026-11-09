# Vol 3 — status

*Moved out of the general CLAUDE.md on Nov 8 2026. Update this file (not CLAUDE.md) whenever the state of this volume changes.*

## Scope
Maṇḍala 1 Sūktas 20–32 (Second Adhyāya of the First Aṣṭaka; printed pp. 1–647).

## Source and inputs
Old single-file scan (printed = PDF − 15); better scans in `vol3/scans/` (page maps in `vol3/vol3_runbook.md`).

## Outputs
`vol3/Rigveda_Samhita_Vol3_English_Translation.md` (+ docx/pdf). The *anāhitāgni* note (Sūkta 31, p. 576) is a separate section at the end of the file.

## How it was made
Scan-based legacy workflow. A numeral + `[?]` + accent pass was set up Oct 27 2026 (branch `claude/numerals-vol3`).

## Status
Translated. **Audit (`vol3/Session_Report_Vol3_Sukta29-32.md`):** Sūkta 29 Ṛks 6–7 and all of Sūkta 30 (pp. 452–517) were first written while page-image views were failing; they were redone from the images and on Oct 27 2026 the redone text replaced the unverified version. **Rule for every volume: if an image view returns no image, STOP and report; never write that page.**

## Open items
Pass in progress or pending per the runbook; see Vol 2 for common open items.

## Publication (print PDF)
Built (799 pp.) with `publish/build.py 3 full`; `publish/out/vol3_full.pdf`.

## Pointers
`vol3/README.md`, `vol3/vol3_runbook.md`, `vol3/Session_Report_Vol3_Sukta29-32.md`.
