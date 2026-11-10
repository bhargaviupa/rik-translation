# Handbook — Rigveda Saṃhitā translation (Kannada → English): the full rules (was CLAUDE.md until Nov 10 2026; `CLAUDE.md` is now the short version every session and agent loads)

This file is the **general** instruction file. It says how every volume from **Vol 15 onwards** is created (inputs, tools, translation loop, outputs, publication, git). It contains **no volume-specific status**: each volume keeps its own `volN/STATUS.md` (position, open items, publication state). Rules for the older, scan-based Volumes 1–14 are in `docs/LEGACY_SCAN_WORKFLOW.md`. A frank review of what should still change in the repository is in `docs/REPO_REVIEW.md`. **Read `docs/LESSONS.md` before starting a volume and extend it afterwards: every volume must leave the tools and rules better than it found them (§15).**

## 1. What we make

The source is the 1949–1952 Kannada edition of the Ṛgveda-saṃhitā with Sāyaṇa's Sanskrit bhāṣya and the Kannada commentary of Asthāna Mahāvidvān H. P. Venkata Rao (Śrī Jayacāmarājendra Vedaratna-mālā, ~35 volumes; each volume = one or two adhyāyas). For every volume we produce:

| Deliverable | File | Notes |
|---|---|---|
| English translation (working text) | `volN/Rigveda_Samhita_VolN_English_Translation.md` | append-only, one trailing progress note; Sanskrit in three layers |
| Kannada text | `volN/Rigveda_Samhita_VolN_Kannada_Text.md` | made by script from the supplied text, appended together with the English file; basis for later Telugu/Hindi work |
| Print PDF, English | `publish/out/volN_full_Eng.pdf` | front matter from the volume's own scans; Vol 1 pattern |
| Print PDF, Kannada | `publish/out/volN_full_Kan.pdf` | same front matter + the original Kannada pages' text |
| Status | `volN/STATUS.md` | the only place for volume-specific state |

Not translated (user decision, Nov 7 2026): the Kannada front matter (title page, imprint, dedication, board, translator's note/preface, contents, abbreviations). It is carried as scanned pages in the PDFs.

## 2. Non-negotiable rules

1. **Sanskrit always in three layers**: Devanagari + IAST (italic, by script) + English, on every citation. The Saṃhitā block also carries Vedic accents (by script). Never two layers, never IAST alone, never silently drop a citation.
2. **The supplied text is the base. Never "correct" a letter or number from memory** or from outside sources. A place that cannot be settled becomes `[?]` in both files and goes to `volN/review/doubts.tsv` for the user. Where the print gives no number, write none. Printed oddities (misspellings, wrong numbers, misprints in the printed English → `[sic]`) are **kept as printed and noted** in a bracketed italic note, never fixed.
3. **No hand-typed Devanagari or IAST by the translator.** Sanskrit blocks are placed with `[[bN]]`, inline Sanskrit is copied from `kn.md` inside `⟦ ⟧`; scripts convert (`kannada_to_deva`, `add_iast.py`, `accent_volume.py`).
4. **Output files are append-only**, each with exactly one trailing `**Progress note:** Done through printed p. N …` (replaced by script at each commit). Never edit, `git checkout`, or restore an output file by hand mid-run; never rewrite earlier sections. Repairs of earlier text are separate, logged edits.
5. **Honesty in reports**: say what was verified and how (git log, tail of the file, grep results); never report a commit that you have not seen in `git log`; if a gate fails say so with the output.
6. **Git**: work on branch `claude/volN`; commit and push every window; never force-push; no pull requests unless asked; merge into `main` only when the user says so (the user has recently asked for direct work on `main` for publication changes — follow the current instruction, and say so in the commit). If a push is rejected because `main` moved, `git fetch` and `git rebase origin/main`, never force. Commit messages end with the attribution lines given by the session.
7. **Privacy/licence**: `refs/mandala/*.html` (accented reference text) is for personal study; keep the repo private (see `refs/mandala/README.md`). Portraits, covers and the 1952 text are reproduced for a working edition; publisher/ISBN/permissions are placeholders until the user decides.

## 3. Repository map

```
CLAUDE.md                 this file (general instructions only)
docs/                     LEGACY_SCAN_WORKFLOW.md, REPO_REVIEW.md, STATUS_TEMPLATE.md, HISTORY.md (old CLAUDE.md copy), old reports
tools/rv/                 THE pipeline for Vol 15+ (batch.py, rvlib.py, html_pages.py, html_to_kn.py, convert.py, labels.py, numerals.py, check_inline.py, …)
                          RUNBOOK.md (dispatcher), TRANSLATOR_RULES.md (agent)
publish/volbook.py        THE print builder (Eng + Kan PDFs) driven by volN/pubcfg.json
publish/tools/frontmatter/  fm_extract.py (front-matter scan PDF → page images), contents_parse.py (printed contents → blocks), README.md
publish/tools/translit/   kannada_to_deva.py, add_iast.py, deva_to_kannada.py (shared by all volumes)
publish/tools/accents/    accent_volume.py (accent marks from refs/mandala)
publish/assets/           covers/portraits of old volumes; assets/volN/fm_NN.jpg + frontmatter.json (new volumes); guruji.jpg, maharaja.jpg
publish/style*.css        style.css, style_vol1.css (old), style_volbook.css, style_volbook_kan.css
publish/out/              built PDFs/HTML (see REPO_REVIEW: these should not live in git)
publish/build*.py, vol*_clean.py, voice.py   FROZEN: builders/cleaners of Vols 1–13 (old md formats); do not extend
refs/mandala/             rv_mandala1..10.html: accented Ṛgveda text (all ten Maṇḍalas)
vol1 … volN/              one folder per volume (layout below)
```

**Layout of a new volume `volN/`** (created by `batch.py new`, then `pubcfg.json` and `STATUS.md` by hand from the templates):

```
STATUS.md                 position, open items, publication state — update at the end of every working session
volcfg.json               pipeline config: vol, mandala, branch, source (file@FIRST-LAST printed pages), window, output paths
pubcfg.json               print config for publish/volbook.py (copy vol15/pubcfg.json)
html/                     the user's machine-read text files (base64 images stripped); unchanged after supply
contents_fixes.json       (only if needed) restores page numbers lost in the machine-read contents; each fix justified in review/contents_check.md
Rigveda_Samhita_VolN_English_Translation.md / …_Kannada_Text.md
review/                   doubts.tsv, accent_report.tsv, inline_mismatch.tsv, page_flags.md, contents_check.md (all human-readable, tab/markdown)
parts/                    batch_costs.md (one line per window)
numerals/                 optional numeral files (cross-check only)
scans/                    optional, empty by default; spot checks only; never committed in bulk
work/                     one dir per window (git-ignored): kn.md, en.md, en_final.md, kn_final.md, pages.json, PROMPT.txt, numerals.txt
```
**Do not create `volN/tools/`, per-volume prompts or per-volume copies of tools.** If a tool is wrong, fix the shared one in `tools/rv/` or `publish/`; every volume then benefits. (Vols 10–14 each grew their own tools and prompt files; that is exactly what we stop doing.)

## 4. Inputs the user supplies (Vol 15 onwards — no page scans)

1. **Machine-read text** of the volume (HTML or markdown) in one or more files → `volN/html/`. If the user gives several markdown files, merge them into ONE file with `python3 tools/rv/merge_md.py volN/html/rig_N.md IN1.md IN2.md … --write` (lossless; it refuses unless the page split is identical), point `volcfg.json` `source` and `pubcfg.json` `supplied_md` at it and `git rm` the inputs. Strip embedded base64 images from markdown before committing. Page images are **not** read. The text matched an independent reading of the scan on 98.85 % of characters (Vol 5 tests), and the user found its numerals correct. Known weak points: `||` and the avagraha are lost (repaired by script); single-letter OCR slips; garbled running heads; stray "This image contains no text…" description lines (kept as italic notes); a few Latin/Telugu/Devanagari letters inside Kannada.
2. **Front-matter scan PDF** (cover, title page, portrait, permission page, board of scholars, preface, contents pages, abbreviations): used only as page images for the PDFs and to verify the printed contents.
3. **Optional** numeral file (xlsx) → `volN/numerals/` (cross-check only; see `docs/LEGACY_SCAN_WORKFLOW.md` for the old method).
4. The accented reference `refs/mandala/rv_mandalaM.html` for the volume's Maṇḍala(s) already exists for all ten.

Check the text once before starting: `python3 tools/rv/html_pages.py FILE` (is each printed page recognised? the splitter needs a running head with the page number; a misspelled head merges two pages — see §6 hand-fixes).

## 5. Set-up of a new volume (once)

1. `git switch -c claude/volN origin/main`.
2. `python3 tools/rv/batch.py new N --mandala M --start-page 1 --source "volN/html/FILE1@1-100" --source "volN/html/FILE2@101-200"` → `volcfg.json`, folders, empty English/Kannada files with the progress note "Done through printed p. START-1". Edit `volcfg.json` `source` ranges to the real printed pages of each file (front-matter lines belong to no window).
3. Create `volN/STATUS.md` from `docs/STATUS_TEMPLATE.md`; create `volN/pubcfg.json` from `vol15/pubcfg.json` (title lines, adhyāya line, imprint, front-matter roles, `missing_headings`).
4. `python3 tools/rv/batch.py prep N` → first window (`work/wPPPP/`, named by its first printed page).

## 6. The translation loop (Vol 15: ≈ 257 windows of 3–4 printed pages)

**Roles.** The *dispatcher* is the main session: it prepares windows, sends them, verifies, logs, pushes. The *translator* is a Sonnet agent: it checks `kn.md`, writes `en.md`, runs the gates and commits. The agent never types Sanskrit.

**Standing agent (Vol 15 decision, much cheaper):** one translator agent is kept for the whole volume and receives one window per `SendMessage` (≈11–27k tokens per batch vs ≈100k for a fresh agent per window). Its context can only be emptied by the harness compacting it or by starting a fresh agent; when its counter drops, resend a one-paragraph rules recap with the next batch. Never run two agents on one volume.

**Dispatcher cycle per window**
1. `python3 tools/rv/batch.py prep N` → new `work/wPPPP/`.
2. Send the agent: window path, printed pages, where the previous window ended (exact last sentence), the standing gates (below), "report in ≤ 15 lines and quote `git log -1`, `git status -sb`, tail of the English file".
3. **Verify yourself** (do not trust the report): `git log -1 --oneline`; `git status -sb` (pushed); exactly one `**Progress note**` and "Done through printed p. N" equals the window end; no `XXX`; no empty `⟦ (*⟦*)⟧`. Append a line to `volN/parts/batch_costs.md`; commit and push the log; `prep` the next window.
3a. **Gates are enforced by you, not trusted**: a report that says 'committed' is checked against `git log`; a window whose `commit` output you did not see is treated as not committed (batch 121 of Vol 15 was reported done and was not). Never run two long jobs on the repo at once.
4. Every ~10 windows give the user a 5-line status (page reached, windows done, `[?]` count, accent-report count). Stop when the usage limit nears; the next session resumes from the progress note.

**Agent steps per window** (full rules: `tools/rv/TRANSLATOR_RULES.md`)
1. Read `kn.md` (and `numerals.txt`); fix `kn.md` with `batch.py fix N WIN kn "OLD" "NEW"`.
2. Write `en.md`: headings `### Printed p. N`, `## Sūkta N (Maṇḍala M)`, `#### Ṛk N`, labels, English prose, `[[bN]]` for every Sanskrit block, `⟦…⟧` for inline Sanskrit copied from `kn.md` (use start/end text markers and a script, never retype).
3. `batch.py build N WIN`, `batch.py check N WIN`, then **`python3 tools/rv/check_inline.py volN/work/WIN`** and only `&&` after it: `… && python3 tools/rv/batch.py commit N WIN --note "…"` (the note must not start with "Done through printed p."; `--max-doubts K` when `[?]` marks exist). **`commit` does not run `check_inline`** — two bad commits happened when it was chained with `;`. After every edit of `en.md`, confirm the edit applied (a silent failed edit once duplicated text). Read the commit output (`git: pushed`).
4. `git log -1`, `git status -sb`, `tail` of the English file, grep `XXX` and `⟦ (*⟦*)⟧`; report.

**Hand-fixes of `kn.md` that recur (all noted in `en.md`; never delete a line)**
- prose Sanskrit (Special Topics quotations) stays prose in `kn.md` and is quoted in full in `en.md` via `⟦ ⟧`; a long Nirukta/Brāhmaṇa quotation must be quoted in full, not summarised;
- Saṃhitā / Pada / bhāṣya merged into one `>` block → split into separate blocks; Pratipadārtha/Bhāvārtha inside the bhāṣya block → move out and un-quote; Anuvāda and particulars lines inside the introduction block → move out;
- garbled labels (`॥ ಜದಕಾರ ॥`, `ಭವಾರ್ಥ`, `ಪದಹಾರ`, …) → keep the garbled line as an italic note, insert the standard label; missing labels → insert;
- stray lines ("48", "- 6523 -", Tamil numerals, "This image contains…", `Pages: 365/365`) → keep as italic notes;
- hyphenated line breaks inside blocks → join (a break across a page boundary inside a word is kept and noted); a colon between two references → semicolon in `kn.md` so the reference check reads them separately;
- **misspelled/missing running head → the splitter merges two pages**: insert `<!-- printed N -->` + the head line in `kn.md`, add `### Printed p. N` in `en.md`, append the page to `pages.json`; the next `prep` then starts after the true last page (≈40 pages of Vol 15 needed this);
- **Reference abbreviations are read as the user reads the print** (user, Nov 9 2026): ಸಿ. = ನಿ. (Nirukta, write `Ni.`), ಮಿ. ಸಂ. / ಮ. ಸಂ. / ಪು. ಸಂ. = ಋ. ಸಂ. (Ṛgveda-saṃhitā, write `Ṛ. Saṃ.`), ಇ. ಬ್ರಾ. = ಐ. ಬ್ರಾ. (`Ai. Brā.`). `html_to_kn.py` corrects them in `kn.md` before the translator sees it (`refs_fix.py`); in `en.md` always write the corrected Latin form (`Ni. 10-14`, `Ṛ. Saṃ. 2-24-4`), no "printed ಸಿ." remark. Other abbreviations that look misread: ask the user (list them in `review/page_flags.md`).
- Om sign `ॐ` and any Devanagari/Telugu letters inside the Kannada file → rewrite letter for letter as Kannada (the check rejects Devanagari in the Kannada file) and say so;
- `check` requires the same number of `[?]` in both files and an English twin for every reference: references are written as in `kn.md` in Latin digits; where the twin check cannot accept the printed form (e.g. a stray "ಗ." inside a reference) write it as supplied and add "as supplied".

**Page-split caveats**: a window may run one page past its end when a head was merged; the position is always "Done through printed p. N" from the progress note, and the next window starts at N+1.

## 7. Format of the outputs

English file: `### Printed p. N` (one per page), `## Sūkta N (Maṇḍala M)` per sūkta (a new Maṇḍala gets `## Maṇḍala M`), Sāyaṇa's introduction (Sanskrit block, English Anuvāda, particulars), then per Ṛk `#### Ṛk N` with: Saṃhitā-pāṭha (accented), Pada-pāṭha, Sāyaṇa-bhāṣya (Sanskrit block + ≤ 25-word gist, grammatical tail transcribed but not explained), Pratipadārtha, Bhāvārtha, **Printed English translation** (reproduced as printed, `[sic]`), Special Topics (Viśeṣaviṣayagaḷu; all Sanskrit quotations in three layers with their printed references), grammar pages as a 2–4 line note. The last sūkta of an adhyāya ends with the Sanskrit colophon + the Kannada closing line (three layers) and the volume's closing formulas, nothing added. Bracketed italic notes record anything odd about the supplied text.
Kannada file: `<!-- printed N -->` markers, the running head as an italic line, standard section labels, Sanskrit as `>` blocks; no Devanagari; `## Maṇḍala M`, `## ಸೂಕ್ತ N (ಮಂಡಲ M)` and `#### ಋಕ್ N` headings are added from the English structure by `python3 tools/rv/kn_headings.py N --write` after the volume is finished (the windows themselves do not write them).
Review files: `doubts.tsv` (every `[?]` with the exact words), `accent_report.tsv` (Saṃhitā lines the reference text did not match; agents must log them, not only mention them in chat), `inline_mismatch.tsv` (inline Sanskrit not found in `kn.md`: needs the scan), `page_flags.md` (merged pages, missing pages, truncated lines), `contents_check.md`.

## 8. Publication (print PDFs)

One generic builder for all new volumes: **`python3 publish/volbook.py N [eng|kan]`** → `publish/out/volN_full_Eng.pdf`, `volN_full_Kan.pdf` (+ `.html`); reads `volN/pubcfg.json`; never changes the `.md` files. Needs `pip install weasyprint` and `apt-get install fonts-lohit-deva fonts-noto-core fonts-lohit-knda` (fonts are not preinstalled in cloud sessions). Lohit Devanagari is used because it draws the svarita as a vertical stroke; check no dotted circles (◌) in `pdftotext`.

Steps for a volume: (1) user's front-matter scan PDF → `python3 publish/tools/frontmatter/fm_extract.py UPLOAD.pdf --vol N --roles cover,title,portrait,permission,board,preface1,preface2,contents1,…,abbreviations` → `publish/assets/volN/`; (2) `python3 publish/tools/frontmatter/contents_parse.py volN/html/FILE.md --check` and **compare every contents number with the scan pages** (Vol 15: 159/159 equal after restoring one lost number; a number that is wrong *in the print* stays as printed and is recorded in `review/contents_check.md`); (3) fill `pubcfg.json` roles; (4) build; (5) open the first ~20 pages of both PDFs as images (cover, title page on ONE page, portrait, permission, board, contents, index), check page counts and fonts.
Front-matter order: cover scan | title page (English typeset / Kannada scan) | credits | Maharaja portrait scan | permission page | board of scholars | preface scans (Kannada PDF) | Guruji portrait | "The Present Day" placeholders (kept by user decision) | printed contents typeset like the original with links to the "p. N" marks | abbreviations scan | English PDF also an index of sūktas | body.
**English PDF specifics (Vol 15 review, Nov 9 2026 — user decisions):** the front matter is **translated** (typeset from `volN/frontmatter_en.json`: board of scholars, preface — the volume's own Pīṭhike printed before the contents, which the machine-read text mislabels "ಜೀರಿಕೆ" —, list of abbreviations with the printed form, the form used here and the work); the printed contents are translated into English (`volN/contents_en.json`, one entry per `contents_parse` block, Sanskrit words copied inside `⟦ ⟧` and converted to IAST by script) and every entry shows the page **of this book** (`leader` + `target-counter` to the `#pN` mark of its printed page; `pubcfg.contents_target_overrides` {md line: printed page} where the print's own number is wrong, with a footnote); there is no separate sūkta index. The translator's remarks (italic bracketed paragraphs: running heads, stray lines, doubtful readings, and inline parentheses/brackets that say 'as supplied', 'supplied text', 'as printed', 'Doubt:') are **footnotes** at the foot of the page, numbered from 1 in each front-matter section, at the first body page and at every sūkta; `[?]` and `[sic]` stay in the text. The opening chapter of the body is headed **Introduction** (never "Pīṭhike"; the volume's own front Pīṭhike is the **Preface**) and starts on a new page; printed p. 1 carries a large ॐ at the top. All of this happens in memory in `publish/volbook.py`; the `.md` files are not changed by the build.
In memory only (the `.md` is not changed): missing `## Sūkta` headings are supplied (`pubcfg.missing_headings`), leftover multi-line `⟦Kannada Sanskrit⟧` quotations are converted to Devanagari + (IAST). The cover must be the real cover scan; a reconstructed cover (Vol 13 artwork re-lettered) was only a stop-gap.
**Translating front matter for a new volume**: read the user's front-matter scan pages (`publish/assets/volN/fm_NN.jpg`), take the Kannada from the supplied md for comparison (OCR errors: check against the image), write `volN/frontmatter_en.json` (same schema as `vol15/frontmatter_en.json`; `{{fn: …}}` = footnote) and translate the contents with an agent from `contents_parse` blocks (`volN/review/contents_kn_blocks.json` → `volN/contents_en.json`), then review them yourself.

## 9. Tool index (one set for all volumes)

| Tool | Purpose |
|---|---|
| `tools/rv/batch.py` | `new`, `prep`, `build`, `check`, `zoomlist`, `fix`, `commit` — the window workflow |
| `tools/rv/html_pages.py`, `html_to_kn.py`, `merge_md.py` | split the supplied text into printed pages; make the Kannada text by script; merge several supplied md files into one (checked) |
| `tools/rv/convert.py`, `labels.py`, `numerals.py`, `rvlib.py` | Kannada→Devanagari expansion of `[[bN]]` and `⟦⟧`; label normalisation; numeral-file cross-check; config |
| `tools/rv/check_inline.py` | every inline `⟦⟧` segment of `en.md` occurs in `kn.md` (run before every commit) |
| `tools/rv/refs_fix.py` | the user's corrections of misread reference abbreviations (ಸಿ.→ನಿ. = Ni., ಮಿ./ಮ./ಪು. ಸಂ.→ಋ. ಸಂ. = Ṛ. Saṃ., ಇ. ಬ್ರಾ.→ಐ. ಬ್ರಾ. = Ai. Brā.); applied automatically by `html_to_kn.py` to every new window and by `refs_fix.py N --write` to a finished volume |
| `tools/rv/kn_headings.py`, `repair_inline.py`, `annotate_report.py` | after a volume: headings for the Kannada file; convert leftover multi-line `⟦⟧` quotations (older files; `convert.py` now joins such lines); add printed pages to a review TSV |
| `publish/tools/translit/*` | Kannada↔Devanagari, IAST |
| `publish/tools/accents/accent_volume.py` | Vedic accents from `refs/mandala` (`--write`; unmatched lines → `accent_report.tsv`) |
| `publish/tools/frontmatter/*`, `publish/volbook.py` | front matter, contents, print PDFs |
| `tools/rv/compare_html_scan.py`, `repair_worksheet.py`, `publish/tools/ref_check/`, `numeral_pass/` | repair/verification passes on older volumes |

## 10. Cost and speed (measured on Vol 15)

Fresh agent per window ≈ 90–110k agent tokens; standing agent ≈ 11–27k per batch (cumulative counter resets when the harness compacts the agent). Once the loop ran, one window took ≈ 1–3 minutes of agent time. Vol 15 (800 printed pages) needed ≈ 257 windows (`parts/batch_costs.md` has one line per window); plan on ~270 windows for an 800-page volume. Record real tokens in `parts/batch_costs.md` (the harness reports them per agent; Vol 15's early lines say "n/a", which loses the data).

## 11. Finishing a volume — checklist (do all, in this order, then update `volN/STATUS.md`)

1. Last window committed; progress note "Done through printed p. LAST (final)"; colophon and closing lines in three layers, nothing added.
2. **Repair/consistency tools on the finished files**: `python3 tools/rv/refs_fix.py N` (report; the pipeline already applies it, so 0 changes expected), `python3 tools/rv/repair_inline.py N` (must report 0 leftover `⟦` quotations; windows built with the current `convert.py` should have none), missing `## Sūkta` headings in the English file (compare the count with the contents), `python3 tools/rv/check_inline.py` over all windows (log mismatches in `review/inline_mismatch.tsv`).
3. **Accent report**: `python3 publish/tools/accents/accent_volume.py N --html refs/mandala/rv_mandalaM.html [refs/mandala/rv_mandalaM2.html]` (report mode) → `review/accent_report.tsv`; `python3 tools/rv/annotate_report.py N` adds printed pages. Apply with `--write` only when asked; unaccented lines are listed for the user, never accented by hand.
4. **Kannada headings**: `python3 tools/rv/kn_headings.py N --write` (needs equal counts of Sūktas and Ṛks in both files; a printed-number WARN is logged).
5. **QA sample**: ≥ 12 stratified printed pages (+ ≥ 12 Special-Topics pages) checked by a *different* model (Agent tool, `model: opus`, read-only, not told what to expect): numbers/references, names/terms/quotations, negations/attribution, omissions/additions. Write `review/qa_sample.md`; repair findings with logged edits (`review/repair_log.md`); if ERRORs are found, double the sample.
6. **Front matter and PDFs** (§8): front-matter scan PDF from the user → `fm_extract.py` → `contents_parse.py --check` → compare every contents number with the scan → `pubcfg.json` → `volbook.py N`; **look at the first 20 pages and one body page of both PDFs as images**.
7. **Review lists for the user** are complete and human-readable: `doubts.tsv`, `inline_mismatch.tsv`, `page_flags.md`, `accent_report_pages.tsv`, `contents_check.md`, `qa_sample.md`.
8. **Metrics** in `STATUS.md` (windows, pages, hand-fixes by kind, `[?]` count, gate failures, tokens, cost) so the next volume can be compared with this one.
9. **Retrospective**: add lessons to `docs/LESSONS.md`; change tools/rules (§15); update `TRANSLATOR_RULES.md` / `RUNBOOK.md` if agent or dispatcher behaviour changes; update the template `docs/STATUS_TEMPLATE.md` if a new section is needed.
10. Merge only when the user says so; before the session ends, deliver or push anything worth keeping.

## 12. Status files — the contract

Every volume has `volN/STATUS.md` (template: `docs/STATUS_TEMPLATE.md`): scope, source and inputs, outputs, how it was made, status, open items, publication state, pointers. **Update it at the end of every session**; the general rules above never carry a volume's position. Currently present: `vol1/STATUS.md` … `vol15/STATUS.md` (Vol 12 is the missing volume of the series: not started, waiting for the user's text). Older per-volume state files (`vol12_state.md`, `vol13_state.md`, `vol14_state.md`, READMEs) are historical and partly out of date; `STATUS.md` wins.

## 13. Bringing the older volumes under the same tools

New volumes use the pipeline above. Vols 1–14 keep their legacy workflow (`docs/LEGACY_SCAN_WORKFLOW.md`) for repair passes; their closed `.md` files are not edited except the agreed passes recorded in each `STATUS.md`. To print Vols 4–14 with `volbook.py` we need a small *format adapter* per old format (heading layout `## Sūkta N — "…"`, `### Rik N`, inline notes) — see `docs/REPO_REVIEW.md`; do not fork `volbook.py`.

## 14. Session hygiene (cloud sessions are ephemeral)

- Anything worth keeping is committed **and pushed** (or delivered to the user) before the session ends; `/tmp` and the scratchpad die with it. The stop hook asks for a commit/push when files are uncommitted.
- Run one long job at a time (builds, `git gc`, mirror clones); check `pgrep` first; use `run_in_background` + a monitor for anything over ~2 minutes. Quote sizes and counts only from finished commands.
- After a history rewrite every other clone needs `git fetch --prune`, `git reset --hard origin/main`, `git reflog expire --expire=now --all`, `git repack -adf --window=50 --depth=50` (see `docs/LESSONS.md` 21); the repo is kept small: no scans, no new built artifacts if avoidable.
- Large files to the user: ≤ 400 MiB per file, split with checksums and a README.
- Fonts and WeasyPrint are installed per session (§8). Keep `work/` directories out of git; they hold scratch windows only.

## 15. Keep improving — rules for every future session (user request, Nov 9 2026)

Every volume must be cheaper, faster and cleaner than the one before. Concretely:
1. **Read `docs/LESSONS.md` at the start; add to it at the end.** A lesson is: incident → rule or tool change → status (DONE / RULE / TODO).
2. **Twice is a pattern.** A workaround used twice (a hand-fix of `kn.md`, a recurring check, a repeated manual command) becomes a tool change or a gate. Fix the shared tool (`tools/rv/`, `publish/`), never a per-volume copy; add the change to `docs/LESSONS.md`, the tool's docstring and the relevant rules file.
3. **Prefer a gate to a promise.** If a mistake was possible once, make the tool refuse it (e.g. `commit` should run `check_inline`; `html_pages.py` should flag suspiciously long pages). Open items of this kind are listed in `docs/REPO_REVIEW.md`; take at least the top item of its section A at the start of every volume if nobody has.
4. **Measure.** Record per volume: windows, hand-fixes by kind, gate failures, `[?]` count, QA-sample result, tokens/cost. A metric that does not improve is a signal to change something.
5. **Propose, then do.** When you see a better way (a cheaper model split, a smarter check, a clearer file layout), tell the user in two lines with the expected gain; do it when it is small and reversible, ask when it changes outputs, history or rights.
6. **Do not lose what exists.** Improvements must keep old volumes reproducible: tools stay backward compatible, format changes ship with a repair script (like `repair_inline.py`) and a log entry in `volN/review/repair_log.md`.
7. **Say what you did not verify.** Reports separate "verified (how)" from "not checked"; sizes and counts are quoted from finished commands only.

## 16. Where to look

`docs/LESSONS.md` (what went wrong before and what we changed), `docs/REPO_REVIEW.md` (what still to change), `docs/LEGACY_SCAN_WORKFLOW.md`, `docs/HISTORY.md` (old CLAUDE.md copy with per-volume details), `tools/rv/RUNBOOK.md`, `tools/rv/TRANSLATOR_RULES.md`, `publish/tools/frontmatter/README.md`, `volN/STATUS.md`.
