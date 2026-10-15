# Start prompt for a new Vol 9 session (paste as the first message)

Continue the Rigveda Kannada→English translation, Volume 9 (`Rig_Vol9.pdf`, Maṇḍala 1 Sūktas 113–130), on branch `claude/modest-ptolemy-9efv8s`. First `git pull`, and `git lfs pull` if the PDF is a 133-byte pointer.

Before anything else read, in this order: `CLAUDE.md` (all of it), `publish/tools/numeral_pass/METHOD.md` (digit key only), and the last ~40 lines of `Rigveda_Samhita_Vol9_English_Translation.md` (the progress note holds the position). Read `docs/HISTORY.md` only if something is unclear.

This session: translate ONE unit — if the progress note says Pīṭhike is next, do the Kannada Pīṭhike (PDF 8–20); otherwise do the next Sūkta (Sūkta 113 starts on printed p. 2 = PDF 22; printed = PDF − 20; re-check the offset against the page header first). Follow CLAUDE.md exactly:
- Crop pages with `publish/tools/pageprep/crop_pages.py` (150 dpi), view each page image once, write immediately, never re-view a written page. No OCR for words; read the images.
- Read numerals correctly the first time using the digit key; zoom only doubtful digits; mark `[?]` where unsure; record what is printed.
- Write Devanagari + English only, then run `publish/tools/translit/add_iast.py` for the IAST layer and review its `--check` output. Every Sanskrit citation ends with three layers.
- Printed English of each Ṛk: start from `publish/tools/english_ocr/english_block.py`, compare with the page, keep misprints as [sic].
- Per-Ṛk structure as in CLAUDE.md; grammar pages get a 2–4 line note. Batch writes (a whole Ṛk or 4–6 pages per call).
- Append-only with the safe append helper: exactly one "**Progress note:**" at the end, replaced each batch. Never restore the file with git checkout.
- Commit and push each batch to `claude/modest-ptolemy-9efv8s`. No PR, no docx/PDF mid-stream. Keep replies short.
- Check the printed page number of every page against what you just wrote; note gaps.

At the end of the unit report: pages done, approximate tokens per page, any tool that failed or helped, and open `[?]` flags — in five lines or fewer.
