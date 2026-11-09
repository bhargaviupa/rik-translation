# Vol 14 — state

Status: **in progress.** Translated through **printed p. 371 (PDF 391)** of ~961 printed pages (scan: 9 parts, 979 PDF pages, ~660 ppi, in `scans/`). Maṇḍala 1, Aṣṭaka 2, Adhyāya 5 (Anuvāka 24); Sūktas 185–190 complete; **Sūkta 191 begun** (half-title, Pīṭhike, Anuvāda cut off mid-sentence on p. 332).

## Facts
- Page offset: printed = PDF − 18 up to PDF 222; **PDF 223 is a pixel-identical duplicate of PDF 222 (skipped); printed = PDF − 19 for PDF 224–334; PDF 335 duplicates 334 (skipped, at the part 3/4 boundary); printed = PDF − 20 from PDF 336.** Numeral-file page = printed + 18 always (`tools/numerals_for.py` does the mapping). `doubt.py` applies this.
- Output: `vol14/Rigveda_Samhita_Vol14_English_Translation.md` (append-only; one trailing progress note holds the open position and the recent flags; older flags are archived in `review/flags_archive_*.md`).
- Position and per-batch log: `parts/session_state.md` (last entry = where to resume). Resume by pasting `CONTINUE_PROMPT.md` into a new session (translators = Opus, 6 pages per batch).
- Review logs: `review/doubts_v14.json` (every zoomed/undecided place, ~1,300 entries); flag archives in `review/`.

## Open items
- **Re-scan wanted for printed p. 288 (PDF 307):** right edge cut off (Sūkta numeral in header and 1–3 characters at line ends lost; marked […] in the text).
- `tools/page.py --strip K --box` zoom misaims (a line or more high/low). Work-around: locate lines from the strip's ink profile, use tall generous boxes or crop the strip locally.
- `add_iast.py` gaps: skips a bhāṣya block directly followed by a `**Pratipadārtha.**` line or a `*Gist:*` line; duplicates lines inside blockquotes (write quoted English as plain paragraphs). Other bhāṣya blocks earlier in Vol 14 may lack IAST: check before the DOCX build.
- `append_en.py` refuses if the file shrinks by > 2,000 characters (archive flags in the same append as new text).
- Undecided `[?]` places and readings kept "as printed" are listed in the progress note and `review/`; several sūtra/Nirukta numbers differ from the standard numbering (printed as is).

## Direction change (Oct 31 2026)
Translators now Sonnet; numerals from user-supplied files in `numerals/` (see `numerals/README.md`, `vol14_runbook.md` last section). Do not resume translating until numeral files for the next pages are present.

## Sonnet pilot (user, Oct 31 2026)
Pilot: Sonnet translators + supplied numeral files for the **next 100 pages** (printed pp. 314–413 = PDF 333–432). After that, review quality (IAST completeness, repeated text, reading accuracy against the Opus-era pages, numeral-file fit) and decide whether to continue. Start only when the numeral files for these pages are in `numerals/`.

## API mode (user decision, Nov 3 2026)
User has ~$100 of Anthropic API credit and wants the translation run through the API instead of chat sessions. Plan (not built yet): one Python runner `vol14/tools/api_batch.py` that, per 3-page batch, (1) renders strips with `page.py`, (2) reads the numeral rows from `numerals_for.py`, (3) calls the Messages API with the strip images + `TRANSLATOR_PROMPT.md`-style instructions + the last ~60 lines of the output + the progress note, with prompt caching on the fixed instructions, (4) writes the returned chunk, runs `add_iast.py`, calls `append_en.py`, commits. Needs: `ANTHROPIC_API_KEY` in the environment where it runs (not in the repo), a model choice (Sonnet-class for cost; Opus only for spot-checks), a per-batch cost log and a hard budget cap. No tool use loop: crops/zooms would need a second call, so doubtful places stay `[?]` for a later pass. First step next session: build the runner and test it on one batch (printed pp. 372–374), measure cost per page, then extrapolate (~590 pages remain).
