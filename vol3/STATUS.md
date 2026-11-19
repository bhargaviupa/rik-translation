# Vol 3 — status

*Moved out of the general CLAUDE.md on Nov 8 2026. Update this file (not CLAUDE.md) whenever the state of this volume changes.*

## Scope
Maṇḍala 1 Sūktas 20–32 (Second Adhyāya of the First Aṣṭaka; printed pp. 1–647).

## Source and inputs
Old single-file scan (printed = PDF − 15); better scans in `vol3/scans/` (page maps in `vol3/vol3_runbook.md`).

## Supplied machine-read text (user, Nov 18 2026)
`vol3/html/rig_3_1.md` (supplied as HTML under the name `rig_3_1.md`; converted to markdown with `pandoc -f html-auto_identifiers -t markdown --wrap=preserve` at the user's request, Nov 18 2026; front matter and printed pp. 2–285, every page found in both forms) and `vol3/html/rig_3_2.md` (pp. 286–647, every page found; ends with the printer's line). Together the whole volume, pp. 2–647. Changes made: the 37 embedded pictures moved to `vol3/html/figures/` (`tools/rv/extract_figures.py`), the line "HTML source" at the head of file 1 removed; nothing else.

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
