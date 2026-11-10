# Vol 15+ runbook for the dispatcher (the main Claude Code session)

One window = 3 consecutive PDF pages. The dispatcher only dispatches; a Sonnet translator agent does the reading. **Preferred (Vol 15): one standing agent per volume**, one window per `SendMessage` (≈11–27k tokens per batch vs ≈100k for a fresh agent); resend a short rules recap when its token counter drops (context compaction) and recycle it about every 60 windows. A fresh agent per window remains possible (the output files carry the continuity).

## The loop since Nov 10 2026 (this section replaces "Per window", the message template and the manual verification below)

Measured on Vol 12 pp. 2–196: most of the translator's turns went into hand-fixes of `kn.md` (garbled labels, hyphen joins, merged pages) and into running five separate gate commands; most of the dispatcher's turns went into manual `git log`/`grep` checks and a separate log commit. All of that is script work now.

1. Once: start ONE standing Sonnet agent: "Read tools/rv/BRIEF.md. You will get one window per message."
2. Per window, the dispatcher runs **one command**: `python3 tools/rv/batch.py next N --tokens T --tools K --min M` (T/K/M = what the harness reported for the window just finished; omit on the first call). It audits both volume files and git (one progress note, no XXX, no empty ⟦⟧, equal page marks, equal `[?]`, pushed), appends the cost line (committed with the next window), preps the next window and prints `MESSAGE: …`. Send that message to the agent. If it prints `AUDIT FAIL`, fix that first.
3. The agent: reads `WIN/TASK.md`, writes `WIN/en.md`, runs `python3 tools/rv/batch.py done N WIN --note "…"` until it prints `VERIFIED`, reports in ≤ 4 lines. `done` = build + check (now including inline segments, XXX, empty segments, stray progress note, leftover figure lines, page markers) + commit + push + audit.
4. Every ~10 windows: one status line to the user from the `next` output. Recycle the agent about every 60 windows or when it gets slow; a fresh agent only needs BRIEF.md.
The dispatcher does not re-verify by hand: `next` refuses to prepare a window while the audit fails, so a false "done" cannot go unnoticed.

## Set-up (once per volume)
1. `python3 tools/rv/batch.py new N --mandala M --start-page 1 --source "volN/html/FILE1.html@1-100" --source "volN/html/FILE2.md@101-200"` -> `volN/volcfg.json`, folders, empty `Rigveda_Samhita_VolN_English_Translation.md` and `..._Kannada_Text.md` (progress note: Done through printed p. START-1). Each `--source` is a file of the supplied machine-read text with the printed pages (`@FIRST-LAST`) taken from it; add one per file as the user supplies them. Strip embedded base64 images from a markdown file before committing it.
2. Numeral file: optional (the supplied text's numerals were found correct). If the user supplies one, put it in `volN/numerals/`; it is then used as a cross-check. Set `numerals.file_page` (file page = PDF - delta) and `printed` (printed = PDF - k) in `volcfg.json` only to the extent the numeral file needs PDF numbers (`prep` warns when no rows are found).
3. Accented reference: `refs/mandala/rv_mandalaM.html` must exist for the volume's Maṇḍala (the user adds Maṇḍala 3+).
4. Branch: create `claude/volN` from main; `volcfg.json` "branch" guards commits.
5. Check the supplied text once: `python3 tools/rv/html_pages.py FILE` (page numbers present? a page with no running head merges into the previous one: the splitter needs a running head with the page number on each page; markdown files lacking one need that head restored).

## Per window
1. `python3 tools/rv/batch.py prep N` -> window directory with `kn.md` (script-made from the supplied text), numerals, PROMPT.txt. The next 3 printed pages after the progress note are used; if the supplied text ends, prep stops and asks for the next file.
2. Start a translator agent (`model: sonnet`) with the content of `WIN/PROMPT.txt` and "follow tools/rv/TRANSLATOR_RULES.md; finish with `commit`; never wait for an answer: if blocked, write the reason to WIN/BLOCKED.txt and stop". One window per agent; never two agents writing the same volume files; never switch branches while an agent runs.
3. When the agent returns: confirm `git log -1` shows the window's commit and `tail -3` of the English file shows the new progress note. If BLOCKED.txt exists, handle it and re-run the window.
4. Record the agent's tokens/minutes in `volN/parts/batch_costs.md`.
5. Every ~10 windows: spot-check one window against the scan if the user has supplied it (IAST layer present, one progress note, no repeated text, `[?]` density, numerals vs file).

## Gates (batch.py check; commit refuses to append if any fails)
page markers in both files (`<!-- printed N -->` in kn.md, `### Printed p. N` in en.md); `[?]` within the allowance; numerals vs the user's file (NEAR / missing rows); English references have Kannada twins; no unplaced Sanskrit block; no Devanagari in the Kannada file; Ṛk headings in order; no hand-typed IAST.

## Files
`tools/rv/rvlib.py` (config, page map, source text) · `html_pages.py` (split the supplied text into printed pages) · `html_to_kn.py` (Kannada text by script) · `page.py` (scan strips/zoom, optional) · `numerals.py` · `convert.py` (Kannada -> Devanagari expansion) · `labels.py` · `batch.py` (new, prep, build, check, zoomlist, fix, commit). Shared with older volumes: `publish/tools/translit/add_iast.py`, `kannada_to_deva.py`, `publish/tools/accents/accent_volume.py`.

## Not built yet / to decide
- The `[?]` re-check pass over Vols 1–14's existing files (separate tool).
- Real-scan test of the whole loop with an agent (only the scripts were tested, on a synthetic window).
- The numeral file's new Kannada-numerals column: only header-name matching is implemented; send a sample when ready.

## Per-window message to the standing agent (template)
"Batch K: translate window volN/work/wPPPP (printed pp. A–B) under the standing rules (inline ⟦ ⟧ by script from kn.md with start/end text markers; `check_inline` then `commit` only with `&&`; verify any edit applied; grep `XXX` and empty `⟦ (*⟦*)⟧`; read the commit output; keep stray lines as italic notes; ≤ 15-line report quoting `git log -1`, `git status -sb`, tail of the English file). The previous window ended at: «exact last sentence». Continue seamlessly without removing or repeating earlier text. Then wait."

## Dispatcher verification after every window (do not skip; reports are not evidence)
`git log -1 --oneline` is the window's commit; `git status -sb` has no ahead marker; `grep -c '^\*\*Progress note'` = 1 in both files that have one; the note says the expected page; `grep -c XXX` = 0; no `⟦ (*⟦*)⟧`. Then: cost line in `volN/parts/batch_costs.md` (real tokens), commit + push, `batch.py prep N`, next message. If a check fails, fix it before the next window.

## After the last window
Follow the checklist in CLAUDE.md §11 (repair/consistency tools, accent report, Kannada headings, QA sample by a different model, front matter and PDFs, review lists, metrics, retrospective in `docs/LESSONS.md`).

## Tools added after Vol 15 (all in `tools/rv/`)
`check_inline.py` (inline Sanskrit ⊂ kn.md; required before commit) · `repair_inline.py` (convert leftover multi-line quotations of older files) · `kn_headings.py` (Kannada headings from the English structure) · `annotate_report.py` (printed pages in a review TSV). `convert.py` now joins quotations broken over several lines.
