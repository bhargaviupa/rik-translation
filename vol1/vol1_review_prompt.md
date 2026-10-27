# Prompt: numeral review of Volume 1 with one-go HTML review pages

Paste everything below the line into a new Claude Code session on `bhargaviupa/rik-translation`.

---

You are continuing a project in the repo `bhargaviupa/rik-translation`: English translations (and for later volumes Kannada transcriptions) of a 1949 Kannada commentary on the Ṛgveda. In Volume 11 we found a reliable way to correct the small Kannada reference numerals (Pāṇini, Uṇādi, Nirukta, Ṛg, Brāhmaṇa references, page-header numerals): **I review every numeral of a volume myself on a few HTML pages (crop of the printed numeral + an editable box), and you place my readings in the files.** Now do this for **Volume 1**, for the entire volume.

**Authorisation.** `CLAUDE.md` says the Vol 1–7 files are closed. I am opening Volume 1 for **numeral corrections only** (and for a word that is plainly misread next to a numeral you fix; list each such word fix for me). Do not change anything else in Vol 1. Do not touch other volumes.

**Branch.** Work on a new branch `claude/numerals-vol1-<yourtag>` made from `main`. Commit and push small batches to that branch. Do not push to `main` and do not open a pull request unless I say so. Before any merge into `main`, fetch `main` and check whether it has new commits on the same files.

## Read first, in this order
1. `CLAUDE.md` (project rules; the build section is current).
2. `docs/NUMERAL_METHODS_REPORT.md` (why the HTML method: the earlier strip reading was 63% right on a scored test).
3. `docs/PASS_LOG_numerals.md` (what was done for Vol 11, including mistakes to avoid).
4. The tools in `publish/tools/numeral_pass/`: `locate.py`, `review_html.py`, `align_edits.py`, `glyphs.py`, `batches/apply_*.py`, `docx_csfont.py`. They were written for Vol 11 (two files, headings `### Printed p. N (PDF M)` and `<!-- PDF M · printed N -->`) and need adapting for Vol 1.
5. `docs/HISTORY.md`, the Volume 1 parts only.

## Volume 1 facts (check them; do not trust blindly)
- Files: `Rigveda_Samhita_Vol1_English_Translation.md` (page sections `### Page N`, printed page numbers, roman for the preface; no PDF numbers), and `Rigveda_Samhita_Vol1_Gaps_English_Translation.md` (portions printed pp. 95–167, 191–205, 261–283, 288–295, translated later). A numeral may live in either file; both must be covered. Vol 1 has **no Kannada file**; do not create one in this task.
- Scans in the repo (Git LFS; run `git lfs pull` if a file is a small pointer): `Rig_Vol1(1).pdf` (599 pages) and `Rig_Vol1(2).pdf` (346 pages), 300 dpi black-and-white. `docs/HISTORY.md` calls them "extra Volume 1 scans … not in use", so **first establish which printed pages each PDF covers** (read the page-number header on a sample of pages; expect duplicated and missing pages) and build a table `PDF file, PDF page → printed page`. If the two PDFs do not cover the whole volume, stop and ask me.
- **Ask me before starting whether I have a better scan of Volume 1** (600 dpi, like the Vol 11 one). A better scan makes the crops much clearer. If I give one, store it on a separate branch `scans-vol1` as ordinary git files (LFS uploads are blocked from cloud sessions), never merged, like `scans-vol11`.
- The Vol 1 file has relatively few `[?]` (about 140), so many wrong numerals are **unflagged**. Treat every numeral as needing my review, not only the `[?]` ones.

## Method

**1. Locate every numeral group on every page (no tokens).** Use Tesseract `kan` only to find *where* numerals are (word boxes), never as a reader: that is my decision for this project. `apt-get install tesseract-ocr tesseract-ocr-kan` (ask me first; about 50 MB). Run each page with a time limit (`timeout 60`, `OMP_THREAD_LIMIT=1`): on a 300 dpi page Tesseract once hung for over 11 minutes. Keep only groups that are mostly digits or have a hyphen between digits (Tesseract reads many words as digits because ೦ looks like the anusvāra ಂ). Ask me before any run longer than about 20 minutes.

**2. Pre-fill a reading for each crop.** Use the file's own reading where one can be matched (page-order alignment like `align_edits.py`), otherwise leave the box empty or use the shape classifier (`glyphs.py`, trained on glyphs whose file reading is confident). Show the file's reading next to the box.

**3. Build the HTML review pages** with `review_html.py` adapted to Vol 1: for each numeral, a black-and-white crop (cut at the scan's resolution, with a little context left and right), an editable box with the pre-fill, and "file: …" beside it; a heading per page (`PDF file/page · printed p. N`); ids `PDFPAGE_INDEX`, plus the file name if both PDFs are used. Split the volume into pages of about 100–150 PDF pages each (about 500 KB each). Send them to me in the chat with `SendUserFile` (display "render") and keep a copy in `vol1/review/`. Tell me plainly:
- Each box: correct it if it does not match the image; **empty a box if the crop is not a reference numeral**; `?` for a digit I cannot decide.
- My edits are saved only in my browser. The "Copy my edits" button does not work in Safari inside the viewer: I should click in the text box at the bottom, press Cmd+A, Cmd+C, and paste into the chat. Uploading the HTML file back does **not** carry my edits.
- **Do not send me a new copy of a page I am working on**: my saved edits may not appear in the new copy.

**4. Apply my edits.** For each pasted list:
- First save it raw in `vol1/review/edits_<range>.txt` and commit it.
- Place each edit by aligning the page's crops (print order) with the numeral groups of that page section in the file. Edits that do not align, and any where the file number and my reading look like different references: render the printed line (as `/tmp/.../lines.py` did for Vol 11: the whole line with the crop boxed) and look at it before placing. Unedited rows are **not** confirmations; ignore them.
- My reading wins over the file. Record numerals **as printed**; if one differs from the usual number, add ` [as printed]` after it. Never supply or "correct" a number from memory. A number the print has and the file lacks is added; tell me each one.
- Apply all edits of a page **from the end of the page backwards**, with each anchor computed from the untouched page text. (In Vol 11 two edits close together corrupted seven spots when applied forwards.)
- Before committing, run a word-level diff of the batch against the last commit and read it; every change must be a numeral swap or a deliberate addition. Check the file did not shrink unexpectedly and still ends with exactly one `**Progress note:**`.
- Log each batch with `PASS_LOG_FILE=vol1/vol1_pass_log.md python3 publish/tools/pass_log.py …` (adapt it to Vol 1's headings), naming numbers kept as printed, numbers added, and readings you could not place.
- Commit and push after each batch.

**5. At the end**, on my request only: rebuild the Vol 1 outputs (`python3 publish/build_vol1.py full` for the designed PDF; DOCX/PDF per the build section of `CLAUDE.md`, with `docx_csfont.py` and Lohit Devanagari), check the Devanagari count and that there are no dotted circles, and give me the files.

## Rules that matter most
- Never complete a numeral or a word from memory; never use an outside concordance unless I agree.
- Keep `[?]` where neither my reading nor the print settles a digit.
- Ask me before any large install, long job, or anything shared outside the repo.
- Report briefly after each step: pages done, numerals located, edits applied, numbers added, numbers kept as printed, readings not placed, `[?]` count before/after, tokens per page.
