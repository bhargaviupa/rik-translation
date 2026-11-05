# Tooling review across volumes, and a proposed standard for Vol 15 onwards (Nov 5 2026)

Read-only survey of every `vol*/tools/`, `publish/` and `publish/tools/` script. Nothing was changed.

## 1. What exists

| Where | Files | Lines | What it is |
|---|---|---|---|
| vol1/tools | 28 | 812 | numeral/`[?]` pass on the better scan: viewing, crops, review page, edits |
| vol2/tools | 27 | 771 | the same toolkit, copied |
| vol3/tools | 50 | 1,320 | same again plus many one-off `zl_*`, `zf_*`, `apply_w3`-type scripts |
| vol4/tools | 67 | 1,459 | same plus one-offs (largest) |
| vol5/tools, vol6/tools | 36, 27 | 1,085, 750 | newer layout: `cfg.py`, `view.py`, `doubt*.py`, review-page builders |
| vol10/tools, vol12/tools, vol13/tools | 13, 7, 14 | 568, 176, 308 | `cfg.py`, `page.py`/`view.py`, `numsheets.py`, `append_en.py`, `doubt.py`, review HTML |
| **vol14/tools** | 12 | 623 | **most complete**: `page.py`, `api_batch.py`, `numerals_for.py`, `numeral_checks.py`, `labels.py`, `accents.py`, `append_en.py`, `doubt.py` |
| publish/ | 13 + tools | ~1,800 | build scripts (docx/PDF/HTML), cleaners, `voice.py`, `review_all.py` |
| publish/tools | accents, english_ocr, numeral_pass, pageprep, ref_check (17), translit, verify11 | ~2,500 | shared: `add_iast.py`, `accent_volume.py`, `crop_pages.py`, `english_block.py`, numeral-file alignment (`ref_check/`) |

## 2. Findings

1. **Copies, not a library.** 12 scripts are byte-identical in Vols 1–4 (`zoom`, `zc`, `view`, `crop`, `ruler`, `montage`, `lines`, `pagework`, `latin_filter`, `samcrop`, `acc`, `accent`); 4 more in Vols 2–4; `numsheets.py` identical in Vols 10/12/13. A fix in one place never reaches the others.
2. **Every volume re-invents `cfg.py`** (scan parts, global-PDF to printed-page map, duplicate/missing pages, EN path). The page maps with their special cases live in code (Vol 14: offsets 18/19/20/…, duplicate PDFs 223, 335, 447, 559). That is where errors come from.
3. **Two eras.** Vols 1–6 tools exist for correcting an existing translation (numerals, `[?]`, review pages). Vols 10–14 tools exist for producing one. Vols 1–6 scripts are not needed for a new volume.
4. **Vol 14 is the working model.** Measured from `vol14/parts/api_costs.jsonl`: 92 API batches, 276 pages, $32.81 = **$0.119 per page** (Sonnet, ~5,900 output tokens and ~38 s per page; ≈ $115 for a 960-page volume). Its pipeline: scan strips → numeral-file rows → API call → `add_iast.py` → `labels.normalise` → accents → `append_en.py` → doubts log → commit. In Vol 14 so far: 1,103 `[?]` in the file; 563 API doubt lines.
5. **Weak spots in Vol 14's design that Vol 15 should fix:** hard-coded Vol 14 paths inside the scripts (page map, prompt files, branch guard); the scripted steps are only reachable through `api_batch.py`, so a Claude Code translator has to run them one by one; no Kannada output though Vol 11 onwards should have a Kannada file; Pada is not accented.
6. **Hygiene.** Compiled `.pyc` files are tracked (`vol14/tools/__pycache__`), which caused a merge conflict today. Several `publish/work/*_clean.md` are rebuilt outputs. Docs still mention old root paths.
7. **Shared pieces already good:** `publish/tools/translit/add_iast.py`, `publish/tools/accents/accent_volume.py` (new), `publish/tools/pageprep/crop_pages.py`, `publish/tools/ref_check/` (numeral file alignment), `vol14/tools/page.py` (strips at max dpi without viewer shrinking).

## 3. Proposed standard for Vol 15 onwards (user decision, Nov 5 2026: **Vol 15 onwards is done in Claude Code sessions, not through the Mac API**)

The API batch runner (`vol14/tools/api_batch.py`) stays what it is for Vol 14 only. Vol 15+ follows the Claude Code routine of Vols 10-14: a dispatcher session hands each 3-page batch to a fresh translator agent that can zoom. What changes is that everything around the agent becomes shared, scripted and checked.

**One shared toolkit, one config file per volume.**

```
tools/rv/            shared code (no per-volume copies)
  config.py          reads volN/volcfg.json
  page.py            render strips / zoom a box, one Bash call per batch   (from vol14/tools/page.py)
  numerals_for.py    rows of the user's numeral file, generalised
  batch.py           ONE command that does the scripted steps for a chunk file: add_iast -> labels -> accents -> checks -> append (+ note) -> doubts -> commit
  labels.py, accents.py (wraps publish/tools/accents/accent_volume.py), checks.py, doubt.py, append_en.py
  build/             docx/PDF (from publish/)
volN/volcfg.json     scan parts, printed = PDF - k with a list of [from_pdf, new_k], duplicate/missing PDFs, output paths,
                     first Mandala/Sukta, numeral file path, branch
volN/runbook.md      volume-specific notes only (the common rules live in CLAUDE.md and tools/rv/TRANSLATOR_RULES.md)
```

**Per 3-page batch (dispatcher + translator agent, as in the Vol 14 runbook "Turn economy"):**
1. Dispatcher: reads position from the progress note, skips configured duplicate pages, starts a fresh translator with the page numbers and the position.
2. Translator: one Bash call renders the batch; one turn views all strips; zooms only doubtful words in one parallel turn; writes one chunk file per page (Devanagari + English, inline Sanskrit as `⟦…⟧`).
3. `python3 tools/rv/batch.py N CHUNK... --note "..."` runs the fixed scripted steps and stops on any failed check (heading order, Rik counts, numeral consistency, no change to existing text, exactly one progress note, accents added). The translator never types IAST or accents.
4. Doubts are logged at the moment of zooming; every zoomed place goes to the user's review.
5. Target <= 12 turns per 3-page batch.

Because the agent can zoom, no separate zoom-fix pass is needed for readings it resolves; the leftover `[?]` places are listed for the user.

**Still to decide (the user answered only the first question)**
1. ~~Mac API for Vol 15+?~~ **No: Claude Code.**
2. ~~Kannada text file~~ **Decided (Nov 5): build it in parallel with the English from Vol 15 onwards**, same single viewing of each page. So far only Vol 1 and Vol 11 have one; Vols 12-14 do not. `batch.py` must therefore take a Kannada chunk next to the English chunk and append both (Sanskrit layers by `publish/tools/translit/deva_to_kannada.py`, Kannada prose transcribed by the translator).
3. Translator model: Opus (2-7 `[?]` places per 6-page batch in the Vol 14 pilot) or Sonnet (5-20, cheaper)?
4. Pada accents: not covered by the Maṇḍala HTML script; leave the Pada unaccented?
5. Move the Vol 1-6 tools to `legacy/`, or leave them where they are? They are only needed for the planned back-fill passes.

## 4. Suggested order of work (nothing started)
1. Remove tracked `__pycache__`, add to `.gitignore`.
2. Create `tools/rv/` by generalising Vol 14's `page.py`, `numerals_for.py`, `labels.py`, `accents.py`, `numeral_checks.py`, `doubt.py`, `append_en.py`, and add `batch.py`; keep the Vol 14 scripts working until Vol 14 is done.
3. Write `volcfg.json` for Vol 14 first (proves the format), then Vol 15.
4. Dry-run `batch.py` on a chunk from an already translated volume and compare with the existing text.
5. Write `tools/rv/TRANSLATOR_RULES.md` from the Vol 14 runbook and API prompt (one version, used by the dispatcher for every batch).

## 5. Open design question: which script is the primary reading? (raised Nov 5 2026, not tested)

**Evidence from Vol 11** (English file vs Kannada file, same single viewing): 701 pages compared; `[?]` counts per page correlate at 0.92; 618 pages have `[?]` in both files, 12 only in the Kannada one, 11 only in the English one. The Kannada file's Sanskrit layers (bhāṣya, Saṃhitā, Pada) were converted by script from the Devanagari, so every misread letter appears in both files. Unique doubts in Vol 11: bhāṣya 1,396 (954 on Devanagari lines), Special Topics 1,930 (mostly numerals), grammar 593 (almost all numerals).

**Vol 11 routine:** page image (Kannada script) -> model reads and converts in its head -> Devanagari -> script -> Kannada file.

**Idea for Vol 15+ (to be tested on a few pages before adoption):** page image -> model transcribes the Sanskrit in **Kannada script** (same script as the page, easier to compare with the image) -> script converts Kannada -> Devanagari and IAST. This removes the model's mental conversion step and makes the Kannada file the primary reading. Needed: a Kannada -> Devanagari converter (the repo has only `publish/tools/translit/deva_to_kannada.py`; `indic_transliteration` can probably do both directions) and a check that it handles this print's conventions (hooked ma/ya, ಜ/ಙ, anusvāra/visarga, the compound mark in Pada lines).

**Test to run first:** take 5 pages of an already translated volume (e.g. Vol 13), have the translator transcribe the bhāṣya in Kannada script, convert by script, and compare with the existing Devanagari. Differences are either converter problems or reading problems; look at each against the page. Only if the converted text is at least as accurate as the current Devanagari, adopt it.

Not done: nothing here has been built or measured beyond the Vol 11 figures above.
