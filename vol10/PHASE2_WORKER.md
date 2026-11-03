# Vol 10 Phase 2 — worker instructions (page-reading pass; Sonnet only)

You correct the remaining `[?]` in `Rigveda_Samhita_Vol10_English_Translation.md` for ONE unit (a PDF-page range, see `vol10/parts/units.json`). You work in your own git worktree on your own branch; the coordinator merges. Never touch other units' pages, never reset/force-push, never merge, no PRs, never switch branches. Never wait for an answer; if blocked, write the reason in your state file and stop.

## Rules (CLAUDE.md + Vol 13/14 learnings)
- **Numerals from the user's sheets are final**: every reference number already placed from the numeral sheets is authoritative — never change it from a glyph reading. You may read a number only where the English still has `[?]` for a number the sheets did not settle; then zoom, and keep `[?]` if not unambiguous (450 dpi). Where no number is printed, write "(no reference is printed here)"; never supply one from memory.
- **No OCR for readings. Never complete a word from memory or from the Saṃhitā.** Convert letter by letter from the page image; if a letter stays unclear after a zoom, keep `[?]` on just that syllable/word. An image view that returns no image → STOP, write nothing for that page.
- **Typeface facts (Vol 13 notes)**: plain *ma* and *ya* are drawn with a hook like the sign ು (ಮುನುಷ್ಯಾ = manuṣyā, ಸನೇಮು = sanema, ಧಾಮು = dhāma, ಲಭೇಮುಹಿ = labhemahi): never read that hook as *u* unless the word clearly needs *u*. In Pada lines a small subscript stroke is the compound mark (ऽ). Digits 2 / 3 / 7 look alike (calibrate on the running header).
- **Three layers**: Devanagari + IAST + English on every Sanskrit citation. Edit the Devanagari (and the English) by hand; produce IAST for the changed Devanagari by script (`python3 publish/tools/translit/add_iast.py` on a scratch file of just the changed lines, then copy the IAST line), or, for a short inline correction, change the matching IAST syllable consistently. Keep the italic IAST line equal to the Devanagari.
- Fix the English gloss only where it depends on the corrected reading. Do not rewrite anything else; do not touch the progress note.
- Page-anchored: a page is the block under `### Printed p. N  (PDF g)`. Check that the printed number on the image agrees (note a mismatch in your state file).

## Procedure (follow the turn economy: ≤ ~12 turns per 3 pages)
1. `cd` into your worktree (path in the prompt). `export V10SCANS=/home/user/rik-translation/vol10/scans V10WORK=/tmp/v10w_<unit>/ V10UNIT=<unit>` (cfg.py reads them; doubts go to `vol10/review/doubts_v10_<unit>.json`).
2. List your pages' `[?]` places: `python3 vol10/tools/qlist.py <FROM> <TO>` (prints, per page, each `[?]` with context). View only pages that have `[?]`.
3. Batch of ~3 pages: one Bash call renders all (`for p in A B C; do python3 vol10/tools/page.py $p $V10WORK/p$p; done` → `…_0.png`, `…_1.png`); then ONE message with all Reads of all strips (parallel). Read each doubtful place against the image.
4. Doubtful letters/words that the strip does not settle: ONE parallel turn of zooms: `python3 vol10/tools/page.py PDFPAGE $V10WORK/z1 --strip K --box X0 Y0 X1 Y1 --dpi 450` (box in the pixel coordinates of that strip image **as displayed**, multiplied by the viewer's stated factor; make the box a generous full line or two lines — the zoom tool misaims: check the zoom shows the intended word; redo once). Then one message with all zoom Reads.
5. Write the corrections for the batch as ONE JSON list `[[old,new],…]` (each `old` must occur exactly once in the file; take enough context) and run `python3 vol10/tools/apply.py batch.json` (all-or-nothing). Then fix IAST/English lines consistently (same mechanism). Do not hand-edit the file with ad-hoc rewrites.
6. Log every zoomed place (resolved or not) for the user's review: `python3 vol10/tools/doubt.py PDFPAGE y0 y1 x0 x1 "ZOOMED, read: <reading>"` (or `UNDECIDED: …`), using the whole-page fractions the zoom command prints.
7. After each batch: `git add -A && git commit -m "Vol 10 pass2 <unit>: PDF a-b"`. Append one line to `vol10/parts/state_<unit>.md` (done-through PDF page, `[?]` left in unit, open items).
8. When all pages of the unit are done (or after ~45 image views, or a failure): final commit, then reply with ONE line: `unit <id>: pages a–b, [?] before N after M, branch <name>`.

Goal: resolve as many `[?]` as the page genuinely settles; a `[?]` kept honestly is better than a guess. Expected: about two thirds resolve.
