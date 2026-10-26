# Session report — Vol 11 verification against the better scan

Repo `bhargaviupa/rik-translation`; branch `claude/modest-ptolemy-9efv8s` (also pushed to `main`).
Files: `Rigveda_Samhita_Vol11_English_Translation.md`, `Rigveda_Samhita_Vol11_Kannada_Text.md`; log `docs/PASS_LOG.md`.

## 1. What was done

**Goal.** Check both Vol 11 files page by page against the user's 600-dpi scan (merged `/tmp/nv/new.pdf`, PDF pp. 1–140; printed page = PDF − 18), fix `[?]` marks and unflagged misreadings, commit and push each batch, log each page.

**Coverage.**
- PDF 25–140 were processed (PDF 24 partly; PDF 38–39 had no marks). The latest stretch was PDF 74–140, ending with PDF 135–140 (printed pp. 117–122; Sūkta 140, Ṛks 5–6).
- Every page edit was committed and pushed; the working tree is clean and `main` and the feature branch are at the same commit (235a6e5).

**Method per page.**
1. Render strips at about 260 dpi, view each once.
2. Edit English and Kannada with page-scoped helpers that refuse non-unique matches.
3. Check with `ctx.py`, log with `pass_log.py`, commit, push.

**Typical corrections.**
- Sanskrit bhāṣya, Saṃhitā, Pada and quotation blocks re-transcribed in full from print (Śatapatha, Aitareya, Taittirīya, Bṛhaddevatā and Āśvalāyana quotations were often wrong or incomplete).
- Kannada prose wording; Pratipadārtha glosses; grammar-page paragraphs (the Kannada file now carries the printed paragraphs, not a headword summary); Varga numbers filled from page headers.
- Paragraphs and grammar entries cut at print page breaks: tails moved to the top of the next page, with "(continues …)" markers.
- Quotation references: numbers were read without zoom where legible and logged for later checking.

**Instruction followed.** "Let's not focus on the numerals; correct only other things." Numerals were left as `[?]` and no zoom tiles were made for them.

## 2. Remarks and caveats

- **Numerals.** The remaining `[?]` marks are mostly numerals (Ṛ. Saṃ., Pā. Sū., Ni., Brāhmaṇa references). They are meant for the separate numerals project.
- **Numbers read without zoom.** Examples: Pā. 3-4-6/99, 6-4-81, 6-1-6/189, Ṛ. 1-34-11, Ai. Brā. 4-20, Śa. Brā. 6-2-3-11, 6-2-4-3, Tai. 1-5-1, Ṛ. 6-2-5, Pā. 6-1-71, Muṇḍaka 1-2-4,5, the sūtra numbers on PDF 129 and 133, and Ṛ. 1-58-4 / 1-88-6 (PDF 135). Treat these as provisional.
- **PDF 135.** The Ṛ. Saṃ. reference numbers I tried to fill in did not apply: the edits found no match, and those two lines are still `[?]`. One English phrase edit and one Kannada Special Topics wording edit also did not apply.
- **PDF 140.** One Kannada Bhāvārtha edit found no match; the other Bhāvārtha wording fixes applied.
- **Doubtful readings kept as `[?]`.**
  - PDF 137: the Śatapatha *lokān …-eveyom iti* phrase and *avyetv abhvam*.
  - PDF 138: the garbled opening of the Saṃhitā line *tā inn…eva*.
  - PDF 139: *svam eva*.
  - PDF 140: *sañ-śṛṅgam*.
  - PDF 138–139 grammar entries: *yajoci…* (the *yaṅ-luk* sūtra name), *paunaḥ…*.
- **Kannada file.** The Sanskrit in it is converted by script from the Devanagari; it is not independent transcription.
- **Accents.** Saṃhitā accents were added to Sūkta 139 Ṛks 1–4 and earlier pages only; Sūkta 139 Ṛk 5 onward and Sūkta 140+ are not yet done.
- **Parallel work.** The user runs other projects (OCR dataset, separate verification window, numerals project with Opus/Fable). Avoid overlapping page ranges.
- **Earlier in this project (for context).** Tesseract and Google Docs OCR were judged no better for Kannada. A requirements document for a Kannada-specific OCR and a numerals brief exist in `docs/`.

## 3. To do

1. **PDF 141–714** need further scans from the user; same workflow once available.
2. **Numerals pass** (`publish/tools/numeral_pass/METHOD.md`, `docs/NUMERAL_READING_BRIEF.md`): resolve all numeral `[?]` marks, and spot-check the unzoomed numbers listed in section 2.
3. Retry the unapplied PDF 135 reference numbers and the unapplied wording edits on PDF 135 and 140.
4. Add Saṃhitā accents for Sūkta 139 Ṛk 5 onward and Sūkta 140+.
5. Resolve the doubtful words in section 2 with a higher-zoom look or the user's answer.
6. Optional, only if asked: rebuild progress notes, `.docx` / PDF, and review worklists.
7. Older open items from CLAUDE.md: Vol 8 numeral pass (~280 flagged pages) and 14 first-person phrases for `voice.EXACT`; outside Vedic expert review for Vols 1–2; ~9,000 `[?]` across Vols 1–10; the combined back-fill pass (English `[?]` plus Kannada file) for Vols 1–10 needs the user's answers.
