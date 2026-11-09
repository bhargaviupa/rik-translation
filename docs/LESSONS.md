# Lessons log — read before starting a volume, extend after every volume

Each entry: **what happened → rule or tool change → status**. Status: DONE (in a tool/gate), RULE (in CLAUDE.md / TRANSLATOR_RULES / RUNBOOK, enforced by people), TODO (listed in `docs/REPO_REVIEW.md`). When you meet a problem twice, it stops being a "hand-fix" and becomes a tool change (see CLAUDE.md §15).

## Process (dispatcher and agents)
1. **A subagent's report is not evidence.** Batch 121 was reported "committed and pushed" while the commit had never happened (a silent failed edit, then `&&` stopped the chain). → The dispatcher verifies every window itself (`git log -1`, `git status -sb`, one progress note, no `XXX`, no empty `⟦ (*⟦*)⟧`) and the agent quotes the actual lines. RULE.
2. **Gates that depend on an agent remembering are not gates.** `commit` did not run `check_inline`; two bad commits followed (empty inline segment, `XXX` placeholder). → `check_inline && commit`, never `;`. TODO: make `commit` run it (REPO_REVIEW A1).
3. **A failed edit must be noticed.** A Python edit of `en.md` failed its assertion; the old text went into the commit. → after every edit confirm "applied"; read the commit output. RULE.
4. **One standing agent is ~5× cheaper than a fresh agent per window** (11–27k vs ~100k tokens) but its context is compacted by the harness at unpredictable moments (the counter drops). → resend a rules recap after a drop; recycle ~every 60 windows; never two agents on one volume. RULE.
5. **Quote Sanskrit in full, never paraphrase it** (a long Nirukta quotation was summarised once; a bhāṣya gloss was paraphrased on p. 138 and only found by the QA sample). → TRANSLATOR_RULES; QA sample checks it. RULE.
6. **Printed oddities are kept and noted, never smoothed**: the QA sample found two silently smoothed misprints (p. 296, p. 577) and a mis-expanded running head ("Aṣṭaka" for ಅ. which is Anuvāka, 8 pages). → note every misprint/odd word "as supplied"; expand abbreviations only with the legend in hand (ಅ. between ಮಂ. and ಸೂ. = Anuvāka). RULE.
7. **Measure after a process has finished.** I reported the local `.git` as 640 MB while `git gc` was still running (true size 1.2 GB, then 680 MB after a proper repack). → quote sizes/counts only from a finished command; say "measuring" otherwise. RULE.
8. **Do not run two long background jobs on one repo** (two `git gc` runs competed). Kill by PID, check `pgrep` first. RULE.
9. **Independent QA catches what gates cannot.** A 12-page sample by a different model (not told what to expect) found 4 minor issues in 1.5 % of pages. → every volume gets a QA sample (CLAUDE.md §11); concentrate on Special Topics pages. RULE; automation TODO.

## Tools and pipeline
10. **Multi-line `⟦…⟧` quotations were never converted** (≈500 raw Kannada-script quotations in the English file). → `convert.py` now joins the lines; `tools/rv/repair_inline.py` repairs older files. DONE.
11. **A misspelled/missing running head merges two printed pages** (~40 pages in Vol 15, fixed by hand each time). → hand-fix procedure in CLAUDE.md §6; TODO: make `html_pages.py` sequence-aware (REPO_REVIEW A3).
12. **Accent misses were reported in chat only** → `accent_volume.py` (report mode) regenerates `review/accent_report.tsv`; `tools/rv/annotate_report.py` adds printed pages. DONE (the report must be regenerated at the end of every volume).
13. **The Kannada file had no headings** → `tools/rv/kn_headings.py N --write` builds them from the English structure (counts must match; a mismatching printed number is a logged WARN, the English order wins; headings need a blank line before them or pandoc ignores them). DONE.
14. **Check inline Sanskrit against `kn.md`** (`tools/rv/check_inline.py`): the first run over Vol 15 found 39 mismatching segments from early windows (`review/inline_mismatch.tsv`). DONE.
15. **Machine-read contents have lost numbers**: `contents_parse.py --check` flags non-monotonic pages and unnumbered items; a fix file `{line: page}` / `{line: {"page":N,"nojoin":true}}` restores them; **a number that is wrong in the print itself ("443" for 543) stays as printed** (the clean scan is the arbiter). DONE.
16. **Characters from other scripts appear inside Kannada** (Devanagari ॐ, Telugu letters, Latin S for avagraha): rewrite letter for letter as Kannada and note it; the Kannada file must stay Devanagari-free. RULE.

## Text and publication
0. **Several supplied md files → one file, losslessly.** The user's two files had to be listed with page ranges and each carried converter lines ('Markdown source', 'Pages: N/N'). → `tools/rv/merge_md.py` merges them and refuses unless the printed-page split of the merged file equals the union of the inputs' splits; the config then names one file. DONE (Vol 15, Nov 9).
17. **Always look at the generated PDF**, not only at counts: the cover caption spilled to its own page, the title page split over two pages, the portrait and its caption landed on different pages, the Kannada index had one entry (headings without a blank line). → check the first ~20 pages and a body page of both PDFs as images after every build (CLAUDE.md §8). RULE.
18. **Front matter comes from the volume's own scans** (cover, title, portrait, permission page, board, preface, contents, abbreviations), not from reconstructions; the user supplies the front-matter PDF; `fm_extract.py` → `publish/volbook.py`. DONE. The Vol 15 stop-gap cover (Vol 13 artwork re-lettered) was replaced by the real scan.
19. **Pandoc**: a heading must start its own block; never put note text in `^[...]`; internal links need ids (`#pN` on every printed-page mark). DONE in volbook.
20. **WeasyPrint is slow** (~1.5 min per volume pair): build `eng` or `kan` alone while iterating.

## Git, size and delivery
21. **Scans and built PDFs do not belong in git.** `.git` reached 3.1 GB (2.5 GB scans). History was purged with `git filter-repo` (backup mirror first; refs/heads force-pushed; `refs/pull/*` cannot be rewritten; every other clone must `fetch` + `reset --hard` + `gc`). → scans are git-ignored (`vol*/scans/*`); TODO: stop committing built PDFs (REPO_REVIEW B). A local clone reaches its true size only after `git reflog expire --expire=now --all && git repack -adf --window=50 --depth=50`. DONE/RULE.
22. **Delivering large files to the user**: `SendUserFile` accepts ≤ 400 MiB per file; split with `split -b 300M -d -a 2`, add `SHA256SUMS.txt` and a README with the `cat` + `git clone bundle` steps. RULE.
23. **If a push is rejected because `main` moved**, `git fetch` + `git rebase origin/main`, never force (except the agreed purge). RULE.
24. **Sessions are ephemeral**: anything worth keeping is committed, pushed or delivered before the session ends; `/tmp` backups die with the session. RULE.

## How to add a lesson
Append to the right section: number, one-sentence incident, the rule/tool change, status. If the lesson changes behaviour, also edit `CLAUDE.md` (general), `tools/rv/TRANSLATOR_RULES.md` (agent) or `tools/rv/RUNBOOK.md` (dispatcher), and the tool itself where possible.
