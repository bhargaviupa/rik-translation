# Prompt for the Vol 1 re-check session (paste into a new Claude Code session on this repo)

You run a **re-check of Volume 1** of the Rigveda translation (repo `bhargaviupa/rik-translation`) against a new source: the user's machine-read text of the Kannada edition (html/markdown files the user uploads). Vol 1 was translated long ago from page scans; its Kannada text and its English were read from the scans by a model, so both carry reading errors, some marked `[?]` and some not. The job has three parts: (A) make a Kannada file from the supplied text, (B) settle the `[?]` places with it, (C) find reading errors that carry no mark. **Agent method**: you are the dispatcher; the page-by-page reading is done by fresh Sonnet agents, one batch at a time. No Batch API, no API key.

Read first: `CLAUDE.md`, `vol1/STATUS.md`, `vol1/vol1_qmarks_log.md` (how `[?]` places were settled before), `docs/LESSONS.md`.

## What is there now (checked Nov 11 2026)
- English: `vol1/Rigveda_Samhita_Vol1_English_Translation.md` (16,115 lines, 105 `[?]`) and `vol1/Rigveda_Samhita_Vol1_Gaps_English_Translation.md` (printed pp. 95–167, 191–205, 261–283, 288–295; 5,524 lines, 14 `[?]`). Page headings have the form `### Page 176` / `### Page vi`, not `### Printed p. N`.
- Kannada read from the scans: `vol1/kannada/Rigveda_Samhita_Vol1_Kannada_Text.md` and `…_Kannada_Review.md` (208 `[?]` together).
- Vol 1 is a legacy volume: no `volcfg.json`, no windows; `tools/rv/batch.py` does not run on it. It keeps the old conventions (`[?]`, bracketed remarks). **Do not convert it to the `**NOTE**` convention** and do not change its layout: the user has not asked for that.
- The files are closed except for agreed passes. This is an agreed pass: every change to them is a repair, logged line by line in `vol1/review/repair_log.md` (page, old → new, why).

## Rules for this job
1. **How a place is decided** (user, Nov 11 2026: most `[?]` are references and numbers, and those should simply be corrected):
   - **Numbers and references** (verse numbers, page numbers, book.chapter.verse, counts, dates): the supplied text is taken. Digits are what a machine reads best and what the scan reading got wrong most. Correct the place and remove the `[?]`. Exception: the supplied number is impossible where it stands (a verse number out of sequence, a reference to a chapter that the same page counts differently, a digit lost at a cut line end): then keep `[?]` and list it.
   - **Text** (Sanskrit quotations, names, Kannada words): where the two readings differ, decide from the context — the Kannada sentence, the Sanskrit grammar and metre of the quotation, the gloss that follows it, the English printed in the edition — and correct. The supplied text has its own errors (Vols 12–18: cut line ends, wrong conjuncts), so it is not taken blindly; but a reading that the context supports is put in without a mark.
   - Only where the context does not decide between the two does `[?]` stay (or get added). Never settle a letter or a number from memory or from another edition.
2. The translator never types Devanagari or IAST: a corrected Sanskrit reading is taken from the supplied text by script (`tools/rv/convert.py`, `publish/tools/translit/`), as in the other volumes.
3. A change of reading that changes the meaning also changes the English sentence that depends on it; say so in the log.
4. No per-volume tools: what you write for this job goes into `tools/rv/` and takes the volume as an argument, because Vol 2 will need the same pass.
5. Git: work on the branch this session was given; commit and push after every batch; never force-push; no pull request and no merge into `main` unless the user asks. One writer at a time on the Vol 1 files.
6. Honest reports: counts only from finished commands; say what was compared and what was not.

## Part A: the Kannada file from the supplied text
1. Ask the user to upload the files; put them in `vol1/html/`, merge them losslessly with `tools/rv/merge_md.py` as Vols 17–18 did (see `vol17/STATUS.md`, "Source and inputs"), commit.
2. Run `python3 tools/rv/html_pages.py` on the merged file: report the page range, **the missing page numbers**, and where the roman-numbered front matter ends. Vol 1 is mostly prose chapters (preface, introduction, Sāyaṇa's Bhāṣya-bhūmikā) with only Maṇḍala 1 Sūktas 1–2 at the end, so the Ṛk-structure pass of `html_to_kn.py` applies to the last part only; extend the shared scripts where the prose pages need it rather than working around them.
3. Write `vol1/kannada/Rigveda_Samhita_Vol1_Kannada_Text_html.md` (page marks `<!-- printed N -->`, the text cleaned as `html_to_kn.py` does). The old scan-read Kannada file stays untouched beside it.
4. Tell the user what Part A showed before going on: pages covered, pages missing, how the page numbers of the supplied text map to the `### Page N` headings of the English.

## Part B and C: the comparison, by script first
Write `tools/rv/recheck.py VOL` (shared). Per printed page it aligns the old scan-read Kannada with the new Kannada (rapidfuzz, as `check_inline.py` does) and writes `vol1/review/recheck/pNNNN.md` with:
- every `[?]` of that page in the English and in the old Kannada, each with the corresponding words of the supplied text;
- every place where the two Kannada readings differ in a Sanskrit quotation, a proper name, a numeral or a reference (book.chapter.verse), ignoring spacing, punctuation and line breaks;
- the numerals and references of the English page against those of the supplied text;
- pages present in one source and not in the other.
It also writes a summary table (page, number of `[?]`, number of differences). Show the user the summary before any agent is started: it tells how large the job is.

## The agent loop
- **Pilot first: 20 printed pages** from the middle of the volume, one Sonnet agent. Report to the user: places looked at, `[?]` settled, `[?]` kept, unmarked errors found and corrected, tokens used; show five of the corrections with old and new reading. Go on only after the user has seen it.
- Then batches of about 30 printed pages, one fresh Sonnet agent per batch, one batch at a time. Each agent gets: the page list, the `recheck/pNNNN.md` files, the three texts for those pages, the rules above. It decides each listed place by rule 1 (numbers and references from the supplied text; text by context; undecided only as the last resort), edits the English file and writes its log lines; it does not read pages for which the script lists nothing.
- After each batch the dispatcher runs the script checks (no new Kannada script in the English, `[?]` count went down or stayed, every edit has a log line, three-layer Sanskrit intact), appends the agent's token count to `vol1/parts/batch_costs.md`, commits and pushes, and updates `vol1/STATUS.md`.
- Settled `[?]` places also go into `vol1/vol1_qmarks_log.md` in its existing form.

## Stop and tell the user when
- the supplied text does not cover a page range of the English, or its page numbers cannot be mapped;
- a batch finds more than about one unmarked error per page (then the method or the batch size needs a decision);
- a correction would change a heading, a verse number or the structure of the file;
- the usage limit is near: commit and push first; the next session resumes with this prompt and `vol1/STATUS.md`.

## At the end
`vol1/STATUS.md`: pages compared, `[?]` before and after, unmarked errors corrected, places left undecided (with the list file), cost. Add the lessons to `docs/LESSONS.md`. The docx/PDF of Vol 1 are **not** rebuilt in this job: ask the user.
