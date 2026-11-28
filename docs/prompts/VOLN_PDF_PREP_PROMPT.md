# Prompt: prepare the English review PDF of one of Volumes 7, 8, 9, 10 (paste into a new Claude Code session on this repo; replace N)

You prepare the **English review PDF of Volume N** (N = 7, 8, 9 or 10: Maṇḍala 1, the Ṛk volumes made from scans and then read a second time) of the Rigveda translation (repo `bhargaviupa/rik-translation`). The work is what was done on the English book of Volume 1 on Nov 25–27 2026: generic remarks out of the text, then a build with the shared print rules, then a check, then the user's review. **The Kannada book is not part of this task** (the user will say when). Nothing is translated again, no Sanskrit is corrected, one volume only.

## Out of scope: the front matter (user, Nov 28 2026: "I am finalising the first few pages every volume carries")
The pages before the text, which every volume carries in one uniform form — title page with the volume name, the pictures, credits, copyright page, board of scholars, permission page, thank-you pages, cover and the like (REQUIREMENTS A2) — are being finalised by the user separately. In this task:
- do **not** change them, in any file: not the front-matter code in the builders (`front()` in `publish/volbook.py`, the front-matter part of `publish/build_vol45.py`), not `publish/assets/`, `publish/release.json`, `volN/pubcfg.json`, `volN/frontmatter_en.json`, `docs/REQUIREMENTS.md` A2;
- do **not** judge them, report on them, or ask the user about them; if a check fails only because of a front-matter page, say that in one line and go on;
- look at the book **from its first page of text** (the preface or the first page of the Maṇḍala), not from the cover.
Everything after the front matter is in scope, **including the contents page** (rule 7) unless the user says otherwise.

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
| existing PDF `volN/review/volN_full.pdf` | old build, before the second pass | same | same | same |

- The **second pass** (other sessions) corrected the English text and made a Kannada book `volN/Rigveda_Samhita_VolN_Kannada_Text.md`. **Leave the Kannada files alone.** They have no sūkta, Ṛk or chapter headings, so the title levels of Vol 1 (made from Kannada chapter lines) do not exist here.
- The existing PDFs fail `publish/pdf_check.py` (no footer, "original p. N" in the body). They are not the current text.
- English builder: `cd publish && python3 build_vol45.py N full` (cleaner `publish/vol67_clean.py`; Vols 9 and 10 use `clean9`). The one command that builds, checks and records: `python3 publish/build_all.py N`.

## Set-up
`git fetch origin main && git merge origin/main` on the branch this session was given. `pip install weasyprint pypandoc indic-transliteration rapidfuzz openpyxl lxml` and `apt-get install -y fonts-lohit-deva fonts-noto-core fonts-lohit-knda`; a build takes 1–2 minutes. Never force-push; no pull request; **push to `main` only when the user says so.**

## Steps, in this order

**Step 1. Baseline.** `python3 publish/build_all.py N` on the text as it is. Keep the page count, the `[printfix] …` line, the check result, and a copy of `publish/out/volN_full.html`'s `<h1>`/`<h2>` headings.

**Step 2. Clean-up of the English text, dry run first.** `python3 tools/rv/cleanup_remarks.py N all` prints counts per kind. The patterns were fitted on Volume 1: before writing, print every remark that would be kept **in part** and read them all, and read 30 of the whole-line removals of each kind. If a kind removes content (a reference, a figure, a reading of the print, a sentence of the translation), fix the pattern in the shared tool, never by a volume exception. Then `… all --write`. Every removal is a row of `volN/review/removed_remarks.tsv`; `[?]` and `[sic]` are not removed, they are listed in `volN/review/open_readings.tsv`; `**GLOSS**` markers stay.

**Step 3. Build again and compare with Step 1.** The `<h1>`/`<h2>` headings must be the same, apart from headings that came from removed notes. In Vol 1 a removed note was the marker by which the cleaner inserted whole chapters. Read `publish/vol67_clean.py` (and `clean9`) for strings searched in the text (`startswith(`, `in first`, `re.match`, `deliberate skip`) and make sure none was removed; if one was, restore it and exempt it in the tool.

**Step 4. Check and look.** `python3 publish/pdf_check.py N` must pass. Then look at pages **as images** (`pdftoppm`), never at text copied from a PDF (it scrambles Devanagari): the first 20 pages of text (after the front matter), one page of each kind of content (a sūkta opening, a Ṛk with Saṃhitā/Pada/bhāṣya, word meanings, Special Topics, a grammar section, a table) and 10 pages spread over the volume.

**Step 5. Things that the shared rules meet in these volumes. Look at each, and report before changing a rule:**
1. **Bold (rule 10).** The print step sets whole bold sentences and bold words inside a sentence as plain text. In a Ṛk volume some bold may be meant (for example the Sanskrit word before each meaning). Count what was removed (the `[printfix]` line), look at such a page; if intended bold is lost, show the user two pages and ask.
2. **Kannada script in the English (rule 13).** Sample 30 places in the built HTML: what kinds (printed forms in remarks, headings, whole lines), and does the transliterated result read properly? (Vol 10 has 351 lines.)
3. **English inside quotation bars (rule 12).** Here the bars also hold the Saṃhitā, Pada and bhāṣya blocks. Check that only the English renderings of quotations disappear and that no part of a Ṛk (the edition's "English translation", the meanings, the Gist) is lost.
4. **Page headings** (`### Page N`, `### Printed p. N`, `### Printed p. i  (PDF 7)`) must end in the footer only; if `pdf_check` finds one in the body, widen `printfix.page_headings`, not the cleaner.
5. **Headings.** The rule of two-line headings with the original's name in the footer (rule 1) is carried out by `printfix.headings` for part and chapter headings only (`h1.part`, `h2.chapter`). The old builder prints Sūkta headings as `h2.sukta`, which that step does **not** touch: they keep their present look. Title levels (rule 17) are not applied (no Kannada chapter lines to take them from). If the user wants the Maṇḍala – Sūkta – Ṛk – parts structure restyled, that is a new rule to be written first; ask, do not invent it.
6. **Contents page (rule 7: the original's own contents, with this book's page numbers, no generated list beside it).** What exists: the English files of **Vols 9 and 10** hold the original's contents translated (Vol 9: `## Viṣayānukramaṇike (Table of Contents) — printed pp. vii–?`; Vol 10: `## Table of contents (Viṣayānukramaṇike), printed pp. x–xv`); **Vols 7 and 8 hold none**. The builder `build_vol45.py` still prints its **own generated contents list** of Sūktas and Ṛks (in Vol 1's builder that list was switched off). And `printfix.contents_sections` finds a section only by the words "Table of Contents" with a capital C, so Vol 10's heading is **not found**. To do, for Vols 9 and 10: make that match case-insensitive in the shared step, switch the generated list off in `build_vol45.py` as was done in `build_vol1.py`, rebuild, and check that the contents come out as a table with this book's page numbers (links resolve). For Vols 7 and 8: do not decide; ask the user (no contents in the English; options: none, or made from the original's contents in the Kannada file).
7. **Tables** (rule 14) and **lists over a page turn** (rule 4): find one of each and look.
8. **Lines ending in dots.** `python3 tools/rv/join_pages.py prep N` lists them with the Kannada beside each. Count them by kind and **leave out the ones inside the edition's own printed English** (blocks headed "Embedded English translation, as given in the source"), which the book does not print. Do **not** start reader agents or the Batch API: give the user the number of real places and a token estimate (Vol 1: 269 places cost about 1.2M agent tokens) and wait. A spreadsheet of the places for the user to complete is made only if the user asks for it.

**Step 6. Records.** `volN/review/repair_log.md` (what was removed by kind, how it was checked, what was restored), `volN/STATUS.md`, `PUBLICATION_TODO.md` (row of the volume, change log, "Last updated"); `publish/BUILD_STATUS.md` is written by `build_all.py`. A new lesson goes into `docs/LESSONS.md`. Commit and push to the session's branch after Steps 2, 3 and at the end.

**Step 7. Hand over.** Send the PDF and say in a few lines: build number and page count; counts before and after for `[?]`, `[sic]`, "as printed", session words (from `pdf_check`); what was removed by kind; what you looked at; what is not right yet; the questions of Step 5. Then wait for the user's review.

## What was done on Vol 1 (English), and where it stands in this prompt
"By code" means: the shared print step does it in any build, found by reading the code; **none of Vols 7–10 has been built with the new step yet**, so Step 1 and Step 4 are where it is proved.
| Done on Vol 1 | In this prompt |
|---|---|
| generic remarks, own notes, doubled Devanagari lines, dotted leaders out of the text | Step 2 (script; dry run, read, write) |
| bold only for headings and labels (sentences and single bold words plain) | by code; Step 5.1 (may remove bold that is meant in a Ṛk volume: ask) |
| page headings of the original out of the body, page of the original in the footer, page number, REVIEW COPY, build number | by code; Step 4 (`pdf_check`), Step 5.4 |
| Part and chapter headings in two lines, original's names in the footer | by code, **only for `h1.part`/`h2.chapter`**; Sūkta headings not covered (Step 5.5) |
| contents = the original's own, a table, with this book's page numbers | **not automatic here: Step 5.6 (3 changes needed)** |
| title levels chapter – 1 – 2 – 3 | **not applicable** (no Kannada chapter lines; Step 5.5) |
| sentences cut at a page turn joined into one paragraph; dots removed | joining by code; mending the words at the break only with readers: Step 5.8 (list and wait) |
| numbered lists keep their numbers over a page turn | by code; Step 5.7 |
| Sanskrit smaller, transliteration on its own line | by code; look at it in Step 4 |
| English of quotations not printed inside quotation bars | by code; Step 5.3 |
| no Kannada script in the body | by code; Step 5.2 |
| wide tables fit the page; words broken at line ends | by code; Step 5.7 |
| the edition's own English printed twice (Part II) | Vol 1 only; not applicable |
| list of incomplete sentences for the user | only if the user asks |

## How the user's comments are handled (the user's standing instruction)
A comment on a page is almost always meant **for all pages and all volumes**. So: (1) write it as a rule in `docs/REQUIREMENTS.md` A4; (2) build it into the shared step `publish/printfix.py` / `publish/style_footer.css` (or the shared text tool), never into the volume's builder unless the thing exists only there; (3) rebuild, run the check, look at the page as an image; (4) answer with the build number. Ask the user to quote "build NN, p. N" (the build number is in the footer). Several comments together are fixed in one rebuild.

## Do not
- Do not touch the front matter (see "Out of scope"): title page, pictures, credits, copyright, board, permission page, thank-you pages, cover.
- Do not build or touch any other volume. The user reviews one volume at a time.
- Do not start readers or the Batch API without showing an estimate first; the token budget is tight. Building and checking are scripts and cost nothing.
- Do not correct Sanskrit, numbers or references by hand or from memory; do not type Devanagari or IAST; do not edit the Saṃhitā, Pada or bhāṣya lines (they are derived data).
- Do not remove `[?]`, `[sic]` or `**GLOSS**`; do not reword the translation; do not hand the user long lists to review.
- Do not write a per-volume tool or stylesheet.
- Do not report a step as done that you did not run, or a commit you have not seen in `git log`.

## Stop and ask when
A removal kind cannot be told from content by its form; the headings differ after the clean-up and you cannot see why; a shared rule would lose something that looks intended; the check fails for a reason that needs a new rule; a change to the shared step would alter how another volume prints.
