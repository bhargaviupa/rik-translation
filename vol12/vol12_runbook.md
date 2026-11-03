# Vol 12 — translation runbook (Nov 2 2026; lean method of Vols 13/14, Sonnet only)

Priority: correct readings, few tokens. **Sonnet only** (dispatcher session and every translator; never Opus). CLAUDE.md conventions apply (three-layer Sanskrit, per-Ṛk structure, printed English with [sic], progress-note pattern, digit key incl. the Oct 31 correction: round = 2, hooked = 3, flat-footed = 7). No OCR for readings; an image view that returns no image → STOP, write nothing for that page. No audits, tests or whole-volume scans.

## Scan and set-up (once)
1. Use the scan named in `vol12_state.md` (better scan in `scans/` if uploaded; else the old `Rig_Vol12.pdf` only with the user's recorded approval — otherwise STOP and ask).
2. Page offset by sampling ~6–8 spans of header strips (`python3 vol12/tools/numsheets.py FIRST LAST PREFIX`); set OFFSET in `tools/cfg.py`; read the title page once for the Sūkta range; record both in `vol12_state.md`. Create the output file with a short header (as in Vol 13/14).

## Reading and writing (the dispatcher starts a fresh translator per 3-page batch)
- **Reading:** `python3 vol12/tools/page.py PDFPAGE /tmp/pg` (trimmed strips; 300 dpi for the old scan, `--dpi 400` for a better one). View all strips of the batch in one message. Zoom only a doubtful **letter/word** (never numerals): `page.py PDFPAGE /tmp/z --strip K --box X0 Y0 X1 Y1 --dpi 450` (box in the coordinates of the image as displayed; it prints the fractions for `doubt.py`).
- **Numerals** come from the user's files in `numerals/` (format described in `numerals/README.md` by the first worker). A numeral the file marks unreadable → `[?]`; no file for the page → STOP (never read numerals by eye).
- **Writing:** Devanagari + English by the translator, **IAST by script** (`publish/tools/translit/add_iast.py` on the chunk; inline `⟦…⟧`); Sāyaṇa-bhāṣya in Devanagari with a ≤ 25-word gist where needed; grammar pages a 2–4-line note; the source's printed English with [sic]. Append with `python3 vol12/tools/append_en.py "PROGRESS NOTE" < chunk.md` (one trailing progress note).
- **Turn economy:** every tool call re-reads the whole context. Per 3-page batch: render all pages in one Bash call; view all strips in one message of parallel Reads; zooms in one message; write each page with one call; log all doubts in one call; target ≤ 12 turns per batch. Log each batch's cost in `parts/batch_costs.md` (pages, model, tool_uses, tokens, minutes).
- Every zoomed place and every `[?]` goes to `review/doubts_v12.json` (`tools/doubt.py`); the user reviews one flat list.

## Hygiene
One branch `claude/vol12`; never force-push or reset; merge to main only when the user says; no PRs; never switch branches while a translator writes in the same folder (use `git worktree` for side work). LFS: if checkout fails with "should have been a pointer": `GIT_LFS_SKIP_SMUDGE=1 git checkout …`, then `git lfs pull -I <file>`.
