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
Prepared Nov 26 2026; done through printed p. 0 (no window translated yet).

## Open items
1. User: the remaining 321 `[?]` (numbers: the user's numeral list; `vol25/review/CHECK_FOR_USER.md`).
2. Dispatcher: the preface (printed before p. 1) is translated by one agent into `vol25/work/preface/en.md`; installing it is a logged repair with the user's yes.
3. Pictures: the cover and title page for the PDF (`vol25/html/figures/fig1_title.png`, `fig2_cover.png`).

## Publication (print PDF)
Not built.
