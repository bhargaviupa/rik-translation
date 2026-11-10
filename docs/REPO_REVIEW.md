# Frank review of the repository (Nov 8 2026) — what to change, in priority order

Context: 15 of ~35 volumes are translated, Vol 12 is missing, 20 more volumes are coming. The Vol 15 pipeline works and is cheap, but the repository around it grew by accretion. These are the problems I would fix, with the cost of leaving each one.

## A. Fix before the next volume (small, high value)

1. **(Done Nov 10: `check` now includes the inline, XXX, empty-segment and note gates; `batch.py done` runs everything.) Make `commit` run `check_inline` (and an `XXX`/empty-segment guard) itself.** Two bad commits in Vol 15 (empty `⟦ (*⟦*)⟧` line, `XXX` placeholder) happened because `commit` does not run it and an agent chained it with `;`. Gates that depend on an agent remembering are not gates. Also make `commit` refuse a note that starts with "Done through printed p." and refuse when `git status` shows other modified files.
2. **(Done Nov 9: `convert.py` joins multi-line quotations; Vol 15's file repaired with `repair_inline.py`.) Teach the build to convert multi-line `⟦…⟧` quotations.** `convert.py` converts only one-line segments; ~450 multi-line Sanskrit quotations in the Vol 15 English file are raw Kannada script (three-layer rule violated in the `.md`; only the PDF builder repairs them in memory). Fix once in `convert.py` and re-run over Vol 15 (a scripted, logged repair).
3. **(Mostly done Nov 10: `html_to_kn.py` finds missed running heads — 34 of 42 in Vol 12 — and `prep` flags over-long pages.) Make `html_pages.py` robust.** About 40 of 800 pages in Vol 15 had a misspelled/absent running head and merged into the previous page; the agents inserted markers by hand every time. Use the expected page number sequence (next page = last + 1), fuzzy head matching, and report suspicious merges (a page with > 1.6× median length) in `prep`.
4. **Log accent misses in a file.** Agents reported DIFF/NOMATCH lines in chat only; `accent_report.tsv` stayed almost empty. `build` should always write them.
5. **(Done Nov 10: `batch.py next --tokens --tools --min`.) Record real token costs.** `parts/batch_costs.md` has "n/a" for most Vol 15 lines. The harness gives tokens per agent report; the dispatcher must copy them (or `batch.py` should take `--tokens`).
6. **(Done Nov 9 for Vol 15: `kn_headings.py`; still to be called by `commit`/finish step.) Add Sūkta/Ṛk headings to the Kannada file** (the English file already has them) so the Kannada PDF can have a real contents and running heads. Generate them from the English structure at `commit` time.
7. **Delete stray/outdated files**: `Rigveda_Samhita_Vol14_English_Translation.md` at the repository root (4 MB; moved into `vol14/` on Nov 9 2026), empty `kannada/`, `vol14/vol14_state.md` (says "in progress, p. 371"), duplicate prompt files (`CONTINUE_PROMPT*.md`, `START_PROMPT.md`, `API_PROMPT.md`, `TRANSLATOR_PROMPT.md` across vol10–15), `Translation_Conventions_Handoff.*` (superseded; keep the content in `docs/` if still wanted).

## B. Repository size and what lives in git (medium; needs your decision)

- `.git` is **3.1 GB** (pack 2.7 GB); the working tree 580 MB; tracked PDFs 349 MB. Scans (Vols 4–9, 12) and built PDFs/docx/HTML (`publish/out/`, `volN/*.pdf`, `*.docx`) dominate. A clone is slow, sessions that clone fresh pay for it every time, and every new volume adds ~100 MB of output.
- Recommendation: **built artifacts do not belong in git.** Keep only sources (`.md`, config, assets that are inputs). Publish PDFs/docx as GitHub Release assets (or another store) with the commit hash in the name; keep a `publish/out/README` listing the latest. You decided earlier not to rewrite history; that is fine — just **stop adding** artifacts now (`git rm --cached` + `.gitignore` for `publish/out/*.pdf`, `volN/*.pdf`, `*.docx`, `*.html`), and consider a one-time history purge only if clone time becomes a real problem.
- Scans: the removal of Vols 10, 13, 14 scans from the working tree was right; do the same for the others when each volume's passes are finished. `muller-655-900.pdf` (21 MB, root) should move to `refs/` or out.
- `refs/mandala/*.html` (8 MB) is third-party text under a personal-study note: keep the repo private, say so in a top-level `README`, and never publish the repo.

## C. One layout, one toolset (medium)

- Volumes 1–14 have five layouts (`vol1/` with `kannada/`, `vol4–9` flat, `vol10–14` each with its own `tools/`, prompts and state files). Eleven `volN/tools` directories contain near-copies of the same scripts (`page.py`, `doubt.py`, `append_en.py`, `numsheets.py` …). New volumes already use `tools/rv` + `publish/volbook.py`; freeze the rest: add a `LEGACY` notice to each `volN/tools/README` and **do not copy them again**.
- Print builders: `build.py`, `build_vol1.py`, `build_vol2.py`, `build_vol45.py` plus four `*_clean.py` plus `voice.py` handle four old English-file dialects. Do not fork `volbook.py` for them: write a small **format adapter** (old md → the Vol 15 heading layout) so `volbook.py` prints every volume, and then retire the old builders. Until then the old PDFs stay as built.
- Move `tools/rv` and `publish/tools/{translit,accents,frontmatter}` into a single package (`rv/` with `rv/cli.py`) with one `pip install -e .`; today the scripts import each other by `sys.path.insert`, which is fragile.
- Give every volume the same `volN/STATUS.md` (done) and a machine-readable `volN/pubcfg.json` + `volcfg.json`. Add `batch.py new` support to write both and the STATUS skeleton.

## D. Quality and verification (important for a scholarly edition)

- **There is no automated test suite and no CI.** Add (1) a smoke test running a synthetic window through `prep → build → check → commit` in a temp clone; (2) a GitHub Action that, on every push, runs repository invariants over each `volN` English/Kannada pair: exactly one progress note, no `XXX`, no empty `⟦⟧`, no Devanagari in Kannada files, page markers monotonic, `[?]` counts equal in both files, every `Printed p. N` present in both. These checks exist piecemeal in `check`; they should also guard the output files directly, because agents can and did bypass them.
- **Independent verification pass**: the translation is checked only for references/structure; nobody verifies the English against the Kannada. Plan a sampling QA per volume (e.g. 5 % of pages) by a different model, with a diff report of numerals, names, negations and quotations; budget it as a standing step.
- **Source quality**: the supplied text has OCR slips that are never repaired (inline mismatches, `ಕ/ಣ`, Latin letters). A script that compares each Saṃhitā/Pada with the accented reference (`refs/mandala`) already finds many; extend it to the bhāṣya quotations of Ṛks and write the differences to `review/` for the user — it is the cheapest way to find OCR errors in verses.
- Vol 15's `[?]` list is small (118) because agents left odd words as supplied and flagged them in notes; decide whether "as supplied" notes should also be counted/logged so none is lost.

## E. Series-level gaps and decisions

- **Vol 12 does not exist** (only an old low-quality scan). Ask for the machine-read text and run it through the Vol 15 pipeline first; every later volume's numbering depends on it.
- Vols 1–14 still lack a Kannada text file (except 11, 14-part): back-fill from the supplied text where available, as agreed.
- Vol 14 needs a PDF build and a normalised file (its English file sits in the repository root; its last 188 pages came from a different pipeline than the first 766).
- Rights: the PDFs carry "© Bhargavi Upadhya" over the translation and reproduce the original cover, portraits and Kannada pages; ISBN/publisher/permission are placeholders. Decide before anything leaves the private repo.

## F. Process (cost and safety)

- Keep the **standing-agent** model but add a recycling rule (fresh agent every ~60 windows or when the counter drops) and always resend the rules recap. Keep the dispatcher's own verification step; it caught a false "committed" report (batch 121).
- Keep work on `claude/volN` and merge to `main` only on request; publication-only changes may go to `main` when the user says so. Record that in the commit message.
- Nothing prevents two sessions from editing the same volume file. A lock file (`volN/.lock` with branch+session id, checked by `commit`) would be cheap insurance.
