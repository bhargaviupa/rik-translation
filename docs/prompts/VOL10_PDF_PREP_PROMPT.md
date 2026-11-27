# Prompt: prepare the review PDF of Volume 10 (paste into a new Claude Code session on this repo)

You prepare the **English review PDF of Volume 10** of the Rigveda translation (repo `bhargaviupa/rik-translation`; Maṇḍala 1 Sūktas 122–136, printed pp. 2–707; `vol10/Rigveda_Samhita_Vol10_English_Translation.md`, about 17,100 lines). The work is the same that was done on Volume 1 on Nov 25–27 2026: generic remarks out of the text, then one build with the shared print rules, then a check, then the user's review. **Nothing is translated again and no Sanskrit is corrected.**

## Read first (in this order, and only these)
1. `CLAUDE.md` (short rules).
2. `docs/REQUIREMENTS.md`, section **A4 "Print rules"** (rules 1–17 and the paragraph "How a comment of the user on a PDF is handled") and **B4.6**, **B2.6–B2.7**, **D22**.
3. `docs/HANDBOOK.md` §8 (the paragraph "Rules of every PDF build").
4. `docs/LESSONS.md`, the section "PDF builds of all volumes" (Nov 25–26 2026) and the entries of Nov 26 2026 after it.
5. `vol10/STATUS.md`, and `vol1/review/repair_log.md` from the entry of 2026-11-25 on (what was done on Vol 1 and what went wrong).

## What Volume 10 is (checked Nov 27 2026; confirm with your own counts)
- Made from page scans. **There is no supplied machine-read text and no Kannada file**, so: no Kannada book, no second pass, no mending of sentences against the Kannada, no title levels from the original.
- Layout: `### Printed p. N` (723), `## Sūkta N — …` (15), `#### Ṛk N` (137), bold labels.
- In the text now: `[?]` on 958 lines, `[sic]` on 30, 2 `**GLOSS**` markers, **674 lines with Kannada script**, 1,961 bold runs, 68 lines ending in dots.
- Builder: `cd publish && python3 build_vol45.py 10 full` (cleaner `publish/vol67_clean.py`, function `clean9(10, 122)`) → `vol10/review/vol10_full.pdf`. The one command that builds, checks and records: `python3 publish/build_all.py 10`.
- Dry run of the clean-up on Nov 27 2026: session 1, paren 363, ownnote 43, twin 0, leaders 0 lines.

## Set-up
`git fetch origin main && git merge origin/main` on the branch this session was given. `pip install weasyprint pypandoc indic-transliteration rapidfuzz openpyxl lxml` and `apt-get install -y fonts-lohit-deva fonts-noto-core fonts-lohit-knda` (they install in a cloud session; a build takes 1–2 minutes). Never force-push; no pull request; **push to `main` only when the user says so.**

## Steps, in this order

**Step 1. Build once before touching anything.** `python3 publish/build_all.py 10`. Keep: the page count, the line `[printfix] …`, the result of the check, and the list of `<h1>`/`<h2>` headings of `publish/out/vol10_full.html` (copy the file aside). This is the state to compare against.

**Step 2. Clean-up of the text, dry run first.** `python3 tools/rv/cleanup_remarks.py 10 all` prints the counts. The patterns were fitted on Volume 1, so before writing:
- print every remark that would be kept **in part** (the script shortens a parenthesis and keeps the rest) and read them all, old against new; Vol 1 had 104 such places and two patterns had to be tightened first;
- read 30 of the whole-line removals of each kind;
- if a kind removes content (a reference, a figure, a reading of the print, a sentence of the translation), fix the pattern in the shared tool `tools/rv/cleanup_remarks.py`, never by a Vol 10 exception.
Then `python3 tools/rv/cleanup_remarks.py 10 all --write`. Every removal is a row of `vol10/review/removed_remarks.tsv`; `[?]` and `[sic]` are **not** removed, they are listed in `vol10/review/open_readings.tsv`.

**Step 3. Build again and compare with Step 1.** The `<h1>`/`<h2>` headings must be the same as before, apart from headings that came from removed notes. In Volume 1 a removed note was the marker the cleaner used to insert whole chapters, and five chapters vanished. Read `publish/vol67_clean.py` for strings it searches in the text (`startswith(`, `in first`, `re.match`) and make sure none of them was removed; if one was, restore that line and exempt it in the tool, as was done for "Note on a deliberate skip".

**Step 4. Check and look.** `python3 publish/pdf_check.py 10` must pass (no ◌, no page heading of the original in the body, footer with page number, "Kannada edition p. N" and the build number on the body pages). Then look at pages **as images** (`pdftoppm`), never at text copied from the PDF, which scrambles Devanagari: the first 20 pages, one page of each kind of content (a sūkta opening, a Ṛk with Saṃhitā/Pada/bhāṣya, word meanings, Special Topics, a grammar section, a table), and 10 pages spread over the volume.

**Step 5. Things specific to this volume that the shared rules will meet for the first time. Look at each and report before changing a rule:**
1. **Bold (rule 10).** The print step sets whole bold sentences and bold words inside a sentence as plain text. In a Ṛk volume some bold may be meant, for example the Sanskrit word before each meaning in the word-to-word section. Count what the step removed (the `[printfix]` line), look at such a page, and if intended bold is lost, show the user two pages and ask; do not decide alone.
2. **Kannada script (rule 13): 674 lines.** The step drops a Kannada word that has its English beside it and transliterates the rest. Sample 30 places in the built HTML and report what kinds there are (printed forms quoted in remarks, headings, whole Kannada lines) and whether the result reads properly.
3. **English inside quotation bars (rule 12).** In this volume the bars also hold the Saṃhitā, Pada and bhāṣya blocks. Check that only the English renderings of quotations disappear and that no part of a Ṛk (the edition's "English translation", the meanings, the Gist) is lost; these stand outside bars and must all be printed.
4. **Page headings.** `### Printed p. N` and forms such as `### Printed p. i  (PDF 7)` must end in the footer only. If `pdf_check` reports one in the body, widen `printfix.page_headings`, not the Vol 10 cleaner.
5. **Headings.** Sūkta and Ṛk headings should print in two lines where they carry a title (rule 1) and without names in Kannada script. Title levels 1–3 (rule 17) are **not** to be invented here: there is no Kannada text to take them from.
6. **Contents page (rule 7).** It is the original's own contents with this book's page numbers. See what the file has of the original's contents and what the builder prints now; report, and propose before building anything new.
7. **Lines ending in dots (68).** Only list them with `python3 tools/rv/join_pages.py prep 10` and report the count by kind. Do not start readers: without a Kannada text they cannot be mended, only listed for the user.
8. **Tables** (rule 14) and **lists that continue over a page turn** (rule 4): find one of each and look at it.

**Step 6. Records.** `vol10/review/repair_log.md` (what was removed by kind, how it was checked, what was restored), `vol10/STATUS.md`, `PUBLICATION_TODO.md` (Vol 10 row, change log, "Last updated"), `publish/BUILD_STATUS.md` is written by `build_all.py`. A new lesson goes into `docs/LESSONS.md`. Commit and push after Step 2, Step 3 and at the end.

**Step 7. Hand over to the user.** Send `vol10/review/vol10_full.pdf` and say in a few lines: build number and page count; counts before and after for `[?]`, `[sic]`, "as printed", session words (from `pdf_check`); what was removed by kind; what you looked at; what is not right yet; the questions of Step 5. Then wait for the user's review.

## How the user's comments are handled (the user's standing instruction)
A comment on a page is almost always meant **for all pages and all volumes**. So: (1) write it as a rule in `docs/REQUIREMENTS.md` A4; (2) build it into the shared step `publish/printfix.py` / `publish/style_footer.css` (or the shared text tool), never into the Vol 10 builder unless the thing exists only in Vol 10; (3) rebuild, run the check, look at the page as an image; (4) answer with the build number. Ask the user to quote "build NN, p. N" (the build number is in the footer); do not guess which copy they are reading. Several comments together are fixed in one rebuild.

## Do not
- Do not build or touch any other volume. The user reviews one volume at a time and stopped an all-volume run on Nov 26 2026.
- Do not start reader agents or the Batch API without showing the user an estimate first; the token budget is tight. Building and checking are scripts and cost nothing.
- Do not correct Sanskrit, numbers or references by hand or from memory; do not type Devanagari or IAST.
- Do not remove `[?]`, `[sic]` or `**GLOSS**`; do not reword the translation; do not hand the user long lists to review.
- Do not write a Vol 10 tool or a Vol 10 stylesheet.
- Do not report a step as done that you did not run, or a commit you have not seen in `git log`.

## Stop and ask when
A removal kind cannot be told from the content by its form; the headings differ after the clean-up and you cannot see why; a shared rule would lose something that looks intended (bold in word meanings, a part of a Ṛk); the check fails for a reason that needs a new rule.
