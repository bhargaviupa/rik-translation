# Vol 14 — state

Status: **in progress.** Translated through **printed p. 313 (PDF 332)** of ~961 printed pages (scan: 9 parts, 979 PDF pages, ~660 ppi, in `scans/`). Maṇḍala 1, Aṣṭaka 2, Adhyāya 5 (Anuvāka 24); Sūktas 185–190 so far (185–189 complete; **190 open at Ṛk 3**, bhāṣya cut off at "tasya mahattvamāha | arakṣasaḥ").

## Facts
- Page offset: printed = PDF − 18 up to PDF 222; **PDF 223 is a pixel-identical duplicate of PDF 222 (skipped); from PDF 224 on printed = PDF − 19.** `doubt.py` applies this.
- Output: `Rigveda_Samhita_Vol14_English_Translation.md` (append-only; one trailing progress note holds the open position and the recent flags; older flags are archived in `review/flags_archive_*.md`).
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
