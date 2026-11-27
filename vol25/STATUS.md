# Vol 25 — status

*Update this file at the end of every working session (the only place for volume-specific state).*

## Scope
Maṇḍala 8 Sūktas 68–103 and Maṇḍala 9 Sūktas 1–43 (Aṣṭaka 6, Adhyāyas 5–8; printed pp. 1–878; PDF page = printed + 12). Front matter (PDF pp. 1–12: cover, title page, portrait [Vol 1 page used], preface, contents) is in the text before `<!-- page 1 -->`.

## Source and inputs
Made from the page scans (no machine-read text): `vol25/scans/Rig_Vol25.pdf` (+ the one-page tail, printed p. 878). Kannada prose read by agents from the scans; the Saṃhitā, Pada and Sāyaṇa-bhāṣya blocks come from the Wikisource index (`tools/rv/ws_fill.py`). The one file `vol25/html/rig_25.md` (final, filled) is the source of `volcfg.json`. How it was made and repaired (OCR cross-check, enlarged crops read by two readers, votes, the user's readings): `docs/SCAN_PIPELINE.md`, `vol25/review/repair_log.md`, `reread_applied.tsv`, `wordfix_applied.tsv`, `heads_applied.tsv`, `user_decisions_applied.tsv`. **321 `[?]` remain in the text** (218 words, 101 numbers, 2 head digits): list `vol25/review/CHECK_FOR_USER.md`; the translator marks each `[?]` in prose as `**NOTE**{question}`, never settled from memory. Page numbers without a running head: 217, 475, 574, 575, 681 (first pages of a sūkta or section; lesson 67). Real misprints in the print's heads: p. 298 prints 293, p. 338 prints 339 (kept as printed). Head digits of 41 pages disagree with their neighbours (`review/head_anomalies.tsv`; 25 clear ones corrected).

## Outputs
`vol25/Rigveda_Samhita_Vol25_English_Translation.md`, `…_Kannada_Text.md` (written by `batch.py`), `vol25/review/`.

## How it was made
Translation by Sonnet agents, one agent per batch of three windows (`docs/prompts/VOL24_AGENT_PROMPT.md` with 25), not by the API.

## Status
**Translation finished through printed p. 878 (Nov 26 2026)**: 50 batches (one agent per batch of three windows, preface included), about 4.85M agent tokens in all (`parts/batch_costs.md`), about 5.5k–9.5k per printed page; `check_labels` 2,462 English = 2,462 Kannada blocks, 0 wrong; every sūkta (Maṇḍala 8: 68–103, Maṇḍala 9: 1–43) has its heading; 0 `[?]` in the source text. `**NOTE**` rows: `review/notes.tsv` (each one a place where the print is damaged or disagrees with itself); `**GLOSS**` marks where a quotation has no Kannada meaning. Hand repairs (all in `review/repair_log.md`): Maṇḍala digit of Sūktas 71 and 79, sūkta number 74, the `[?]` gate for scan-read volumes (`scan_read` in volcfg), kn2deva ಁ, the user's later readings taken into the English (16 NOTEs resolved, Nov 26). Shared-tool fixes made during the run: `html_to_kn.py` (Anuvāda without a dash or heading word stays plain text; "xxv. NN" signatures are stray lines). The colophon (Sāyaṇa's verse, "समाप्तं च षष्ठाष्टकम्", ॐ तत्सत्, the closing verse, शुभं भूयात्) is in the file as plain `⟦ ⟧` lines.

Not done yet from HANDBOOK §11: steps 2–9 (refs_fix, accent report, `kn_headings.py`, QA sample by a different model, front matter and PDF, review lists, metrics, retrospective).

## Open items
1. User: printed p. 298 is a scan duplicate of p. 293 (the real p. 298 is missing); the NOTE list `review/notes.tsv`; the preface is installed (Nov 27 2026).
2. Dispatcher: the preface (printed before p. 1) is translated by one agent into `vol25/work/preface/en.md`; installing it is a logged repair with the user's yes.
3. Pictures: the cover and title page for the PDF (`vol25/html/figures/fig1_title.png`, `fig2_cover.png`).

## Publication (print PDF)
Not built.
