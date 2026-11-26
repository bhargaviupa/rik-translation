# Vol 22 — status

*Update this file at the end of every working session.*

## Scope
Maṇḍala 7 (expected: from Sūkta 20; the running heads read `ಮಂ. ೭ … ಸೂ. ೨೦…`), Aṣṭaka 5, Adhyāyas 2–4(5), printed pp. 1–600 (PDF pp. 27–626). The Kannada preface (ಪೀಠಿಕೆ) stands before p. 1. The exact sūkta range is to be confirmed from the text.

## Source and inputs
The supplied text is the user's machine reading of the book, **re-transcribed page by page from the scan PDF `Rig_Vol22.pdf`** (626 pages; PDF page = printed page + 26) by Claude agents reading high-resolution strips of each page (Nov 25–26 2026), because the Gemini OCR of the user's files had too many errors. `vol22/html/rig_22.md`: `<!-- page P -->` before every printed page 1–600 (`html_pages.py`: 600 pages, no gaps, no anomalies), the 21 front-matter pages (PDF 6–26) still the Gemini OCR, `<!-- body -->` between. Which directory each page comes from: `vol22/html/pages_map.tsv` (`retranscribed/` 473 pages, `transcribed/` 127 pages; built by `tools/rv/assemble_pages.py`).
- **Numbers** are settled by rules, not marked: printed page = PDF − 26; verse numbers from the Wikisource Ṛk (`tools/rv/ref_verify.py`) and in sequence; head numbers by sequence and the image (`tools/rv/numbers_check.py` is clean on all 600 pages). No `[?]` stands on a number.
- **Pada words** were settled from Wikisource by the user's decision (Nov 25: "use Wikisource", `tools/rv/ref_settle.py`); the Saṃhitā blocks were not (spelling conventions of the print, REQUIREMENTS B5.5). All corrections are rows of `vol22/data/source_fixes.tsv`; raw tool logs: `vol22/data/retranscription_*.tsv`.
- **No Vedic accent marks** in the transcription (the pipeline strips them anyway). `[?]` marks on words: few; many Sāyaṇa and Kannada-commentary words are best readings (no reference text for them), and citation numbers (Āśvalāyana, Nirukta, Bṛhaddevatā …) are unverified; see the agents' notes in the commit messages of `vol22/html/retranscribed/`.
- The page tool honours explicit `<!-- page N -->` markers (≥ 50); the Kannada-script accent signs are removed by `html_to_kn.py` (lessons of Nov 25).
- **`[?]` marks:** the marked master is `vol22/html/rig_22_marked.md` (166 marks, 93 pages; list with scan strips `vol22/review/qmarks/qmarks_to_verify.md`; corrections of those words are made there, then `python3 tools/rv/assemble_pages.py vol22/html/rig_22.md --no-marks --front vol22/html/rig_22_marked.md vol22/html/retranscribed vol22/html/transcribed`). The pipeline reads `rig_22.md` = the same text without the `[?]` marks, because the gate wants equal `[?]` counts in the English and Kannada files and the BRIEF forbids `[?]` in the English (Nov 26 2026: a first batch stopped on 3 `[?]` in Kannada prose). Windows translated before the marks are checked rest on the best readings.
- Older files: `vol22/html/rig_22_merged.md`, `rig_22_ordered.md` (Gemini versions, kept for history).

## Outputs
`vol22/Rigveda_Samhita_Vol22_English_Translation.md`, `…_Kannada_Text.md` (empty so far), `vol22/work/`.

## How it was made
Agent route as Vols 19–21 (one Sonnet agent per batch of three windows; no API). Prepared Nov 25 2026 on branch `claude/hopeful-fermi-kypcts`.

## Status
Window w0001 (printed pp. 1–6) was translated from the OLD (Gemini) text and must be redone on the new text; nothing else translated. Source quality check by the user pending (Nov 26 2026).

## Open items
1. User: the 127 transcribed pages need a proofread against the scan (accents, uncertain words).
2. Dispatcher: confirm sūkta range and the preface from the text before/while translating.
