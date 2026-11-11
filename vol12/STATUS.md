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
**Translated through printed p. 727 (FINAL, Nov 10 2026)**: Sūktas 158–165 complete (Ṛk headings 6, 5, 5, 14, 22, 13, 52, 15, none missing in sequence), page headings for every printed page 2–727, adhyāya colophon and closing lines on p. 727. `python3 tools/rv/batch.py audit 12` passes; 0 `[?]`; no `[figure: …]` line left. Branch `claude/affectionate-faraday-2iv8y4` (contains `claude/vol12-html`); not merged into `main`.
pp. 2–196: old flow (63 windows of 3 pages, standing agent, tokens not recorded). pp. 197–727: new flow (`TASK.md` → `en.md` → `batch.py done`; 6-page windows, three windows per fresh Sonnet agent): 32 agent runs, 5,965,692 tokens (harness count), 579 tool calls, about 193 agent-minutes = about 11,200 tokens per page (`parts/batch_costs.md`).
**Finishing checklist (Nov 10 2026):** done — repair/consistency tools (`repair_inline`: 0 leftover; `refs_fix` report: 7 lines, all inside "as supplied" notes quoting the print, not applied), accent pass with `--write` (70 of 358 Saṃhitā lines still unaccented, listed with pages in `review/accent_report_pages.tsv`), Kannada headings (8 sūktas, 132 Ṛks), QA samples (`review/qa_sample.md`: 72 pages, 18 ERRORs, 81 MINORs, all repaired with logged edits), merged into `main`. **Not done:** print PDFs (the front-matter scan PDF of Vol 12 has not been supplied); a second-reader pass over the 654 pages outside the samples (at the sampled rate, about 150 comparable faults remain); the user's reading of the reference abbreviations and of the guesses marked "as supplied … read here as" (e.g. pp. 285, 702).

## Open items
**From the new-flow windows (pp. 197–727), for the repair pass and the user:**
- `review/repair_log.md`: Sūkta 164 Ṛk 31 and Ṛk 32 Saṃhitā set as blocks (done); closing dandas of quotations restored by script on pp. 197–727; QA repairs; two earlier logged repairs (empty `⟦⟧` line p. 54; "Vol. XXXII" restored on p. 536–540).
- QA sample should look for wording changed to satisfy a gate (one case was found only from an agent's report: the roman numeral above). References the print gives without a hyphen were written as supplied ("6-4 14", "1-162 4", "6-3 84", "6-1970").
- Reference abbreviations kept as supplied, for the user's reading (as in Vol 15): ತ್ರೈ. ಸಂ., ಕೃ. ಸಂ., ಖ. ಸಂ., ಕೈ. ಸಂ., ಭಾ. ಉ. (used for Chāndogya citations), ಕಡ., ಕರ., ಕೇಸ., ಪ. ಬ್ರಾ., ಶ. ಬ್ರಾ. in several spellings, ಶ. ಪ್ರಾ., ಕ. ಪ್ರಾ., ಬೃ. ಪೇ./ದೇ., ಮುಗ್ವಿ., ಇ. ಆ., ವಾ. ಸೂ., ಪು. ಉ., Telugu "సి." for Ni.; printed "10-128-1" for the Nāsadīya verse.
- Accent step: `review/accent_report_cumulative.tsv` (99 DIFF/NOMATCH lines by window) and `review/accent_flags.tsv`; regenerate with the volume-wide accent pass.
- Script weaknesses met (candidates for `html_to_kn.py`): Pratipadārtha/Bhāvārtha swallowed by the bhāṣya block when the label is unreadable ("ಭಾಷಾ", "ಬಸವೇಶ್ವರ"); a Saṃhitā label inserted after a quoted verse; sūkta introductions not blocked; running heads inside long pages (pp. 254, 407, 421–422, 441, 583, 665, 673, 703–704 were marked by hand); `[figure: …]` lines that only repeat a verse (about 15, each looked at and removed).

1. Dispatcher session: translate pp. 197–727 (~165 more windows). Pending repairs and decisions are in `review/repair_log.md` (w0002 invented "Sense" paragraph; w0093 letter change; w0113 avagraha from picture marks). Reference abbreviations to confirm with the user: ಕೃ. ಸಂ., ಖ. ಸಂ., ಜ. ಸಂ., ಭಾ. ಉ., ಕರ., ಬೃ. ವೇ./ಪೇ., ಛಾ. ಉ., ಇ. ಬ್ರ. (see `review/page_flags.md`). The accent_report.tsv is rewritten per window; regenerate with the accent pass at the end. Recurring hand-fixes still manual: garbled Saṃhitā/Pada/bhāṣya/Pratipadārtha/Bhāvārtha labels, Pratipadārtha inside the bhāṣya block, hyphen joins, merged page heads. 2. User: printed p. 1 (title page) if wanted; settle `[?]` readings. 3. After the volume: CLAUDE.md §11 checklist.

## IAST layer
Not stored in the English file (user decision, Nov 11 2026): the print build adds it for Saṃhitā and Pada blocks (`volcfg.json` `"iast_blocks": "build"`); stored runs were removed with `tools/rv/strip_iast.py` and logged in `review/repair_log.md`; bhāṣya blocks never get it.

