# Vol 13 — status

*Update this file at the end of every working session. It is the only place for volume-specific state; the general rules live in `CLAUDE.md`.*

## Decision (user, Nov 11 2026)
**Vol 13 is re-translated from the user's machine-read text**, by the Batch API route with the Vol 17 conventions. Reason: the old translation, read from page scans, has 1,482 `[?]` marks on 517 of its 653 pages (about 390 after a number or reference, 425 after Sanskrit, 650 after English words), its Sanskrit was typed from the scans, and there is no Kannada file.

## Scope
Expected from the old edition: Maṇḍala 1 Sūktas 166–183 (Fourth Adhyāya of the Second Aṣṭaka), printed pp. 1–657. To be confirmed from the supplied text.

## Source and inputs
Two machine-read files supplied by the user (Nov 27 2026: `rig_13_1.md`, `rig_13_2.md`), merged losslessly into `vol13/html/rig_13.md` (656 pages in, 656 merged), pictures in `vol13/html/figures/` (20), `<!-- page 1 -->` inserted before the opening ॐ; printed pp. 1–657, no page number missing. Front matter: preface (lines 1–228), contents, abbreviations (`html/_layout.json`). 21 certain Pratipadārtha corrections applied before translation (`data/source_fixes.tsv`).

## Outputs
New, empty: `vol13/Rigveda_Samhita_Vol13_English_Translation.md` and `…_Kannada_Text.md` (progress note "Done through printed p. 0"). `volcfg.json`: window 6, `note_style` NOTE, sub-heading layout, bhāṣya block Devanagari only, grammar in Sanskrit, Wilson label (to confirm), `source` page range to be set from the text.
**Old translation, kept untouched: `vol13/legacy/`** (`Rigveda_Samhita_Vol13_English_Translation_scan.md`, `.docx`, `.pdf`). `vol13/legacy/vol13_full.pdf` and `vol13/legacy/Rigveda_Samhita_Vol13_English_Translation.pdf` (moved from `publish/out/` Nov 25 2026) are builds of the old text. `publish/build_vol45.py 13` no longer finds its input at the old path.

## Status
Done through printed p. 657 (final). Audit PASS; Kannada headings written (18 sūktas, 166–183, and 142 Ṛks; every sūkta's Ṛk count equals the Wikisource index); preface translated and installed; NOTE questions settled by the default rule (`tools/rv/notes_resolve.py`: 222 rows); QA samples 48 pages (8 ERRORs repaired, 20 MINORs, about half repaired; `review/qa_sample.md`, `qa_sample_2.md`); second reading against the old scan translation and the user's 39 readings (`review/legacy_compare.tsv`, `review/user_readings_compare.tsv`, by `tools/rv/legacy_compare.py`: lists only, nothing changed from them). Made by one Batch API batch of 110 windows (`msgbatch_014ChvsHfeU594BUp3WBpzwK`), collected with a dispatcher loop; cost about $8.25 (`parts/batch_costs.md`).

## Open items
1. Not done: front matter (the user's scan PDF), print PDFs.
2. QA findings left (see the end of `review/repair_log.md`): end-of-Ṛk mark after the grammar sections, IAST-only Pratipadārtha headwords, Kannada words in the composed grammar on two pages.
3. The English has one block fewer than the Kannada file (452 against 453, label check passes with none unmatched).
4. `review/legacy_compare.tsv` and `review/user_readings_compare.tsv` are lists for the user; 9 of the user's 39 readings have references not found on that page of the new text.

## Pointers
`vol13/CONTINUE_PROMPT_HTML.md`, `vol17/STATUS.md`, `vol18/STATUS.md`, `tools/rv/api_batch.py`, `docs/LESSONS.md` 41–54. Old workflow: `vol13/vol13_state.md`, `vol13/vol13_runbook.md`.
