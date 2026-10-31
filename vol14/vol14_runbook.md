# Vol 14 — translation runbook (Oct 31, 2026)

Priority: **correct readings the first time, few tokens.** Only the translation; no audits, tests, calibration passes or whole-volume scans. CLAUDE.md conventions apply (three-layer Sanskrit, per-Ṛk structure, printed English with [sic], progress-note pattern, digit key).

## Scan
`vol14/scans/14 Rigveda Samhitha Volume 14 N.pdf`, 9 parts, 979 PDF pages in part order, ~660 ppi 1-bit. `vol14/tools/cfg.py` maps a global PDF page to part + page (`git lfs pull` if pointers). Ignore `Rig_Vol14(1/2).pdf`.

## Reading a page (tool: `vol14/tools/page.py`)
`python3 vol14/tools/page.py PDFPAGE /tmp/pg` trims the margins, cuts the text block into full-width strips (top to bottom) and renders them at the highest dpi the viewer shows **without shrinking** (it reduces any image over ~2000 px; at ~360 dpi a strip is read at full detail). View every strip, read, write the page. **There is no separate zoom step**: a strip already shows small numerals and accents. If one place is still unclear: `page.py PDFPAGE /tmp/z --zoom Y0 Y1 [X0 X1] --dpi 600` (fractions of the trimmed block), once. Still undecidable → `[?]` and log it: `python3 vol14/tools/doubt.py PDFPAGE y0 y1 x0 x1 "note"` (→ `vol14/review/doubts_v14.json`; fractions of the whole page; one flat review list is built later with `doubts_v14.py`).

## Set-up (once)
1. Page offset by sampling ~6–8 header strips spread over the volume: `python3 vol14/tools/numsheets.py FIRST LAST PREFIX` (contact sheet of header strips). Agreeing offsets = no missing/duplicate pages between; if it changes, bisect. Front matter is roman-numbered. Set OFFSET in `vol14/tools/cfg.py`; note it in `vol14_state.md`.
2. Title page once, for the Sūkta range (confirm doubtful digits from the ordinal word on the title page or the contents). Nothing else before translating.

## Work: ONE translator agent, pages on request
The main session starts **one** translator agent (Agent tool, name it `translator`) and then only dispatches: it sends the translator a page range (3–4 pages at a time), the translator reads each page with `page.py`, writes it and appends it, and replies with one line ("done through printed p. N / Ṛk R; next?"). The main session sends the next range, updates `vol14/parts/session_state.md`, commits and pushes (every sūkta or ~15 pages). The translator keeps context of the style and of the Ṛk it is in; its context is compacted automatically as it fills. If it dies or loses the thread, start a new translator, point it at `session_state.md` and the last ~40 lines of the output file.
- Translator rules: view each page once (all its strips); write immediately; page-anchored (mark each printed page); Devanagari + English written by you; **IAST by script** `python3 publish/tools/translit/add_iast.py FILE.md`; Sāyaṇa-bhāṣya in Sanskrit with a ≤ 25-word gist where needed; grammar pages a 2–4-line note; the source's printed English with [sic]; no OCR for readings; an image view that returns no image → STOP, write nothing for that page.
- Append: `python3 vol14/tools/append_en.py "PROGRESS NOTE" < chunk.md` (one trailing progress note; asserts the file did not shrink).
- Each sūkta opens with a heading block (Sūkta number, Ṛk count, ṛṣi, devatā, chandas): read it when you reach it. No page counting, no lists of start pages.

## Hygiene
One branch (`claude/vol14`); never force-push or reset; merge to main only when the user says; no PRs. Git/LFS: if `git checkout -b … origin/main` fails with "should have been a pointer": `GIT_LFS_SKIP_SMUDGE=1 git -c filter.lfs.clean=cat -c filter.lfs.process= -c filter.lfs.required=false checkout -f -b BRANCH origin/main`, then `git lfs pull`. Kill background jobs by PID, never `pkill -f`; no sleep-polling.
