# Prompt: prepare the review PDFs of one of Volumes 7, 8, 9, 10 (paste into a new Claude Code session on this repo; replace N)

You prepare the **English and Kannada review PDFs of Volume N** (N = 7, 8, 9 or 10: Maṇḍala 1, the Ṛk volumes made from scans and then read a second time) of the Rigveda translation (repo `bhargaviupa/rik-translation`). The work is what was done on Volume 1 on Nov 25–27 2026: generic remarks out of the text, then builds with the shared print rules, then a check, then the user's review. **Nothing is translated again, no Sanskrit is corrected, one volume only.**

## Read first (in this order, and only these)
1. `CLAUDE.md`.
2. `docs/REQUIREMENTS.md`, section **A4 "Print rules"** (rules 1–17 and the paragraph "How a comment of the user on a PDF is handled"), **B4.6**, **B2.6–B2.7**, **D22**.
3. `docs/HANDBOOK.md` §8, the paragraph "Rules of every PDF build".
4. `docs/LESSONS.md`: the section "PDF builds of all volumes" and the entries of Nov 26 2026 after it.
5. `vol1/review/repair_log.md` from the entry of 2026-11-25 on (what was done on Vol 1, what went wrong), and `volN/STATUS.md` (second-pass section).

## State of the volumes (counted Nov 28 2026 on `main` at e4262837; confirm with your own counts after `git merge origin/main`)
| | Vol 7 | Vol 8 | Vol 9 | Vol 10 |
|---|---|---|---|---|
| English file, lines | 16,223 | 22,831 | 14,282 | 17,134 |
| page headings in the English | `### Page N` (old layout) | `### Page N` (old layout) | `### Printed p. N` (617) | `### Printed p. N` (723) |
| `[?]` / `[sic]` lines | 252 / 51 | 336 / 50 | 36 / 25 | 32 / 30 |
| Kannada-script lines in the English | 27 | 34 | 30 | 351 |
| `**GLOSS**` markers | 248 | 210 | 0 | 2 |
| lines ending in dots | 41 | 30 | 291 | 68 |
| clean-up dry run (`cleanup_remarks.py N all`: session / paren / ownnote) | 1 / 76 / 49 | 1 / 122 / 155 | 1 / 116 / 29 | 1 / 358 / 41 |
| Kannada book (second pass), pages marked | 566 | 831 | 602 | 706 |
| existing PDF `volN/review/volN_full.pdf` | old build, before the second pass | same | same | same |

- The **second pass** (other sessions) corrected the text and made a Kannada book `volN/Rigveda_Samhita_VolN_Kannada_Text.md` from the supplied text (`volN/html/`). It has `<!-- printed N -->` marks, running heads (`*[…]*`, about one per page), `[figure]` places, **no** sūkta or Ṛk headings and **no** chapter lines. Page marks are missing for some pages (Vol 8: p. 323 is missing from the scan itself).
- The existing PDFs fail `publish/pdf_check.py` (no footer, "original p. N" in the body). They are not the current text.
- English builder: `cd publish && python3 build_vol45.py N full` (cleaner `publish/vol67_clean.py`; Vols 9 and 10 use `clean9`). The one command that builds, checks and records: `python3 publish/build_all.py N`.
- There is **no `volN/pubcfg.json`**; the Kannada book needs one (Step 4).

## Set-up
`git fetch origin main && git merge origin/main` on the branch this session was given. `pip install weasyprint pypandoc indic-transliteration rapidfuzz openpyxl lxml` and `apt-get install -y fonts-lohit-deva fonts-noto-core fonts-lohit-knda`; a build takes 1–2 minutes. Never force-push; no pull request; **push to `main` only when the user says so.**

## Steps, in this order

**Step 1. Baseline.** `python3 publish/build_all.py N` on the text as it is. Keep the page count, the `[printfix] …` line, the check result, and a copy of `publish/out/volN_full.html`'s `<h1>`/`<h2>` headings.

**Step 2. Clean-up of the English text, dry run first.** `python3 tools/rv/cleanup_remarks.py N all` prints counts per kind. The patterns were fitted on Volume 1: before writing, print every remark that would be kept **in part** and read them all, and read 30 of the whole-line removals of each kind. If a kind removes content (a reference, a figure, a reading of the print, a sentence of the translation), fix the pattern in the shared tool, never by a volume exception. Then `… all --write`. Every removal is a row of `volN/review/removed_remarks.tsv`; `[?]` and `[sic]` are not removed, they are listed in `volN/review/open_readings.tsv`; `**GLOSS**` markers stay.

**Step 3. Build again and compare with Step 1.** The `<h1>`/`<h2>` headings must be the same, apart from headings that came from removed notes. In Vol 1 a removed note was the marker by which the cleaner inserted whole chapters. Read `publish/vol67_clean.py` (and `clean9`) for strings searched in the text (`startswith(`, `in first`, `re.match`, `deliberate skip`) and make sure none was removed; if one was, restore it and exempt it in the tool.

**Step 4. The Kannada book.** Make `volN/pubcfg.json` on the pattern of `vol1/pubcfg.json` (`"kannada_only": true`, `kannada_md`, `english_md`, `out`; `range_line`, `adhyaya_line` from `volN/STATUS.md`; year and press from the colophon of the supplied text, flagged "to be confirmed by the user"; **no** publisher/ISBN/rights, those live only in `publish/release.json`). Build with `python3 publish/volbook.py N kan`. Look at the front matter (raw machine-read text: cover lines garbled), the running heads and `[figure]` places (the build removes them), pages without a mark, words broken at a line end, and the contents (the original's own contents pages become the contents table with this book's page numbers, `volbook.kan_contents`; report what it did).

**Step 5. Check and look.** `python3 publish/pdf_check.py N` must pass for both books. Then look at pages **as images** (`pdftoppm`), never at text copied from a PDF (it scrambles Devanagari): the first 20 pages, one page of each kind of content (a sūkta opening, a Ṛk with Saṃhitā/Pada/bhāṣya, word meanings, Special Topics, a grammar section, a table), 10 pages spread over the volume, and the same for the Kannada book.

**Step 6. Things that the shared rules meet in these volumes. Look at each, and report before changing a rule:**
1. **Bold (rule 10).** The print step sets whole bold sentences and bold words inside a sentence as plain text. In a Ṛk volume some bold may be meant (for example the Sanskrit word before each meaning). Count what was removed (the `[printfix]` line), look at such a page; if intended bold is lost, show the user two pages and ask.
2. **Kannada script in the English (rule 13).** Sample 30 places in the built HTML: what kinds (printed forms in remarks, headings, whole lines), and does the transliterated result read properly? (Vol 10 has 351 lines.)
3. **English inside quotation bars (rule 12).** Here the bars also hold the Saṃhitā, Pada and bhāṣya blocks. Check that only the English renderings of quotations disappear and that no part of a Ṛk (the edition's "English translation", the meanings, the Gist) is lost.
4. **Page headings** (`### Page N`, `### Printed p. N`, `### Printed p. i  (PDF 7)`) must end in the footer only; if `pdf_check` finds one in the body, widen `printfix.page_headings`, not the cleaner.
5. **Headings.** Sūkta and Ṛk headings print in two lines where they carry a title, without Kannada script. **Title levels (rule 17) are not applied here:** they were made from chapter lines of Vol 1's prose part, and these volumes have none. Do not invent levels.
6. **Contents page (rule 7).** What does the English file hold of the original's contents, and what does the book print? Report; propose before building anything new.
7. **Tables** (rule 14) and **lists over a page turn** (rule 4): find one of each and look.
8. **Lines ending in dots.** `python3 tools/rv/join_pages.py prep N` lists them with the Kannada beside each. Count them by kind and **leave out the ones inside the edition's own printed English** (blocks headed "Embedded English translation, as given in the source"), which the book does not print. Do **not** start reader agents or the Batch API: give the user the number of real places and a token estimate (Vol 1: 269 places cost about 1.2M agent tokens) and wait. A spreadsheet of the places for the user to complete is made only if the user asks for it.

**Step 7. Records.** `volN/review/repair_log.md` (what was removed by kind, how it was checked, what was restored), `volN/STATUS.md`, `PUBLICATION_TODO.md` (row of the volume, change log, "Last updated"); `publish/BUILD_STATUS.md` is written by `build_all.py`. A new lesson goes into `docs/LESSONS.md`. Commit and push to the session's branch after Steps 2, 3, 4 and at the end.

**Step 8. Hand over.** Send both PDFs and say in a few lines: build numbers and page counts; counts before and after for `[?]`, `[sic]`, "as printed", session words (from `pdf_check`); what was removed by kind; what you looked at; what is not right yet; the questions of Step 6. Then wait for the user's review.

## How the user's comments are handled (the user's standing instruction)
A comment on a page is almost always meant **for all pages and all volumes**. So: (1) write it as a rule in `docs/REQUIREMENTS.md` A4; (2) build it into the shared step `publish/printfix.py` / `publish/style_footer.css` (or the shared text tool), never into the volume's builder unless the thing exists only there; (3) rebuild, run the check, look at the page as an image; (4) answer with the build number. Ask the user to quote "build NN, p. N" (the build number is in the footer). Several comments together are fixed in one rebuild.

## Do not
- Do not build or touch any other volume. The user reviews one volume at a time.
- Do not start readers or the Batch API without showing an estimate first; the token budget is tight. Building and checking are scripts and cost nothing.
- Do not correct Sanskrit, numbers or references by hand or from memory; do not type Devanagari or IAST; do not edit the Saṃhitā, Pada or bhāṣya lines (they are derived data).
- Do not remove `[?]`, `[sic]` or `**GLOSS**`; do not reword the translation; do not hand the user long lists to review.
- Do not write a per-volume tool or stylesheet.
- Do not report a step as done that you did not run, or a commit you have not seen in `git log`.

## Stop and ask when
A removal kind cannot be told from content by its form; the headings differ after the clean-up and you cannot see why; a shared rule would lose something that looks intended; the check fails for a reason that needs a new rule; the Kannada book's front matter or contents cannot be made readable by the build alone.
