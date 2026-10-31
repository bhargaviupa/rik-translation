# Vol 14 — translation runbook (Oct 31, 2026)

Priority: **correct readings the first time, few tokens.** Only the translation; no audits, tests, calibration passes or whole-volume scans. CLAUDE.md conventions apply (three-layer Sanskrit, per-Ṛk structure, printed English with [sic], progress-note pattern, digit key).

## Scan
`vol14/scans/14 Rigveda Samhitha Volume 14 N.pdf`, 9 parts, 979 PDF pages in part order, ~660 ppi 1-bit. `vol14/tools/cfg.py` maps a global PDF page to part + page (`git lfs pull` if pointers). Ignore `Rig_Vol14(1/2).pdf`.

## Reading a page (tool: `vol14/tools/page.py`)
`python3 vol14/tools/page.py PDFPAGE /tmp/pg` trims the margins, cuts the text block into full-width strips (top to bottom) and renders them at the highest dpi the viewer shows **without shrinking** (it reduces any image over ~2000 px; at ~360 dpi a strip is read at full detail). View every strip, read, write the page. **There is no separate zoom step**: a strip already shows small numerals and accents. If one place is still unclear: `page.py PDFPAGE /tmp/z --strip K --box X0 Y0 X1 Y1 --dpi 600` (K = strip number; box in the pixel coordinates of that strip image as you saw it, multiplied by the factor the viewer states if it displayed the image smaller), once. It prints the whole-page fractions to give to `doubt.py`. **Every place you zoomed is logged for the user's review, resolved or not**: note starts `ZOOMED, read: <your reading>` (or `UNDECIDED:` with `[?]` kept in the file). Undecidable → `[?]`. Log with: `python3 vol14/tools/doubt.py PDFPAGE y0 y1 x0 x1 "note"` (→ `vol14/review/doubts_v14.json`; fractions of the whole page, as printed by the zoom command; one flat review list is built later with `doubts_v14.py`).

## Set-up (once)
1. Page offset by sampling ~6–8 header strips spread over the volume: `python3 vol14/tools/numsheets.py FIRST LAST PREFIX` (contact sheet of header strips). Agreeing offsets = no missing/duplicate pages between; if it changes, bisect. Front matter is roman-numbered. Set OFFSET in `vol14/tools/cfg.py`; note it in `vol14_state.md`.
2. Title page once, for the Sūkta range (confirm doubtful digits from the ordinal word on the title page or the contents). Nothing else before translating.

## Work: a fresh translator for each batch of 6 pages
An agent cannot drop old images from its own context, and the translation file already holds everything needed to continue. So the main session only dispatches: for each batch of **6 consecutive pages** it starts a new `translator` agent (Agent tool) whose prompt is: the page numbers (PDF and printed), "Translator rules" below, the position from `vol14/parts/session_state.md` (done-through printed page / Ṛk), the last ~40 lines of the output file, and the path of one finished sūkta as a format model. The translator reads each page with `page.py`, writes it, appends it and replies in one line ("done through printed p. N, Ṛk R"); it is then discarded. The main session records that line in `session_state.md`, commits and pushes (every sūkta or ~15 pages), and starts the next translator. A Ṛk that runs over the end of the batch is finished by the translator that reads the page where it ends: the next batch starts on the page after the last one written, and the progress note says which Ṛk is open.
- Translator rules: view each page once (all its strips); write immediately; page-anchored (mark each printed page); Devanagari + English written by you; **IAST by script** `python3 publish/tools/translit/add_iast.py FILE.md`; Sāyaṇa-bhāṣya in Sanskrit with a ≤ 25-word gist where needed; grammar pages a 2–4-line note; the source's printed English with [sic]; no OCR for readings; an image view that returns no image → STOP, write nothing for that page.
- Append: `python3 vol14/tools/append_en.py "PROGRESS NOTE" < chunk.md` (one trailing progress note; asserts the file did not shrink).
- Each sūkta opens with a heading block (Sūkta number, Ṛk count, ṛṣi, devatā, chandas): read it when you reach it. No page counting, no lists of start pages.

## Lessons from the pilot (printed pp. 2–55)
- Opus as translator: ~150k tokens and ~6 min per 6-page batch, ~2–7 distinct `[?]` places per batch. Sonnet (batches 6–8): similar tokens, 5–20 `[?]` places per batch, more mis-aimed zooms: use Opus.
- `pip install indic_transliteration` if `add_iast.py` fails on import. Run `add_iast.py` on your own chunk file only, never on the whole output file. No hand-typed IAST, not even for short inline words (`⟦देवा⟧` markers instead).
- Zoom boxes: coordinates are those of the image **as displayed**; multiply by the viewer's stated factor. Make the box a generous full line. Check the zoom shows the intended word; redo once. Log one `doubt.py` entry per place with the fractions the zoom command prints.
- `[?]` is for places a zoom cannot decide; every zoomed place is logged for the user's review either way.
- Never switch branches or run branch-changing git commands while a translator is writing.

## Hygiene
One branch (`claude/vol14`); never force-push or reset; merge to main only when the user says; no PRs. Git/LFS: if `git checkout -b … origin/main` fails with "should have been a pointer": `GIT_LFS_SKIP_SMUDGE=1 git -c filter.lfs.clean=cat -c filter.lfs.process= -c filter.lfs.required=false checkout -f -b BRANCH origin/main`, then `git lfs pull`. Kill background jobs by PID, never `pkill -f`; no sleep-polling.

## Change of direction (Oct 31 2026, user decision): Sonnet translators + supplied numeral files
- Translators are now **Sonnet** (cost). The dispatcher starts each 6-page batch with `model: sonnet`.
- **Numerals come from files supplied by the user** (one per page or page range, placed in `vol14/numerals/`; format to be recorded in `vol14/numerals/README.md` when the first files arrive). Translators take all reference/sūtra/header/Ṛk/Varga numbers from them, do **no zooming for numerals and no digit analysis**, and do not log numeral zooms in `doubts_v14.json`. A numeral the file marks unreadable → `[?]`. Missing file for a page → STOP and report (never read numerals by eye).
- Zooming remains allowed for doubtful **letters/words** only (use ink-profile line location and tall generous boxes; the zoom tool misaims).
- Pages already translated (through printed p. 313) keep their Opus-era numeral readings; the numeral files can later be used to check/correct them.
- Quality watch: Sonnet drafts need a spot check after the first batches (IAST markers ⟦⟧ used, every Devanagari block has IAST, one progress note, no repeated text).
