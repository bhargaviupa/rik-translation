# Vol 12 — status

*Update this file (not CLAUDE.md) whenever the state of this volume changes. Template: `docs/STATUS_TEMPLATE.md`.*

## Scope
Maṇḍala 1, Third Adhyāya of the Second Aṣṭaka: Sūktas 158–165 (Sūkta 158 begins on printed p. 2; the closing colophon of the third adhyāya is on p. 727). Printed pp. 2–727 are in the supplied text (684 text pages; the other 42 numbers are pages that print no number and merge into the page before). **The series had a gap here until Nov 10 2026: Vols 11 and 13 existed, Vol 12 did not.**

## Source and inputs
The user's machine-read markdown, two files merged losslessly (`tools/rv/merge_md.py`) into `vol12/html/rig_12.md` (printed pp. 2–727; part 1 = pp. 2–334, part 2 = pp. 335–727; the converter's `Pages: N/N` footer lines were removed). Its 36 embedded pictures (verse blocks the machine reader could not read, 24 + 12) were extracted to `vol12/html/figures/` (`fig1_lineNNNNN.jpg`, `fig2_…`; page index `figures/INDEX.tsv`, 33 pages) and are marked in the text as `[figure: vol12/html/figures/…jpg]`. **Not in the supplied text: printed p. 1 (title page).** No scan, no numeral file (the old `vol12/scans/Rig_Vol12.pdf` was purged from git on Nov 8 2026). Config: `vol12/volcfg.json` (`source` = `vol12/html/rig_12.md@2-727`, window 3, branch `claude/vol12-html`). The accent reference is `refs/mandala/rv_mandala1.html`.
**Legacy files in this folder are obsolete** (old scan workflow, nothing translated): `START_PROMPT.md`, `CONTINUE_PROMPT.md`, `vol12_runbook.md`, `vol12_state.md`, `tools/`. Do not follow them.

## Outputs
`vol12/Rigveda_Samhita_Vol12_English_Translation.md` and `vol12/Rigveda_Samhita_Vol12_Kannada_Text.md` (empty, progress note "Done through printed p. 1"). Review files in `vol12/review/`, window costs in `vol12/parts/batch_costs.md`.

## How it was made
Set up Nov 10 2026 (merge, pictures, config; `batch.py prep 12` tested). Translation: Vol 15 pipeline (`tools/rv/RUNBOOK.md`); dispatcher prompt `vol12/CONTINUE_PROMPT_HTML.md`.

## Status
In progress. **Done through printed p. 315** on branch `claude/affectionate-faraday-2iv8y4` (which contains `claude/vol12-html` through p. 196 plus the pipeline changes of Nov 10 2026: see `CLAUDE.md`, `tools/rv/RUNBOOK.md`, `docs/LESSONS.md` 31–36). Windows pp. 197–199, 200–203 and 204–210 were made with the new flow (`TASK.md` → `en.md` → `batch.py done`); `window` is now 6 pages. Next: `python3 tools/rv/batch.py next 12` (starts at p. 316; batches of three 6-page windows per fresh Sonnet agent, see `parts/batch_costs.md`). `batch.py audit 12` passes; 0 `[?]`. Real token counts are in `parts/batch_costs.md` from p. 197 on.
**Continue on this branch (or merge it into `claude/vol12-html` first); do not resume the old branch at p. 197, the two would diverge.**

## Open items
1. Dispatcher session: translate pp. 197–727 (~165 more windows). Pending repairs and decisions are in `review/repair_log.md` (w0002 invented "Sense" paragraph; w0093 letter change; w0113 avagraha from picture marks). Reference abbreviations to confirm with the user: ಕೃ. ಸಂ., ಖ. ಸಂ., ಜ. ಸಂ., ಭಾ. ಉ., ಕರ., ಬೃ. ವೇ./ಪೇ., ಛಾ. ಉ., ಇ. ಬ್ರ. (see `review/page_flags.md`). The accent_report.tsv is rewritten per window; regenerate with the accent pass at the end. Recurring hand-fixes still manual: garbled Saṃhitā/Pada/bhāṣya/Pratipadārtha/Bhāvārtha labels, Pratipadārtha inside the bhāṣya block, hyphen joins, merged page heads. 2. User: printed p. 1 (title page) if wanted; settle `[?]` readings. 3. After the volume: CLAUDE.md §11 checklist.
