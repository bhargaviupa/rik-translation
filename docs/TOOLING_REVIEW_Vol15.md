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
5. **Weak spots in Vol 14's design that Vol 15 should fix:** hard-coded Vol 14 paths inside `api_batch.py` (`vol14`, page map, prompt files, "BRANCH_FOR_RUNS"); the API mode cannot zoom, so doubts are only logged, not resolved; no Kannada output though Vol 11 onwards should have a Kannada file; Pada is not accented; `api_batch.py` commits with a fixed session URL.
6. **Hygiene.** Compiled `.pyc` files are tracked (`vol14/tools/__pycache__`), which caused a merge conflict today. Several `publish/work/*_clean.md` are rebuilt outputs. Docs still mention old root paths.
7. **Shared pieces already good:** `publish/tools/translit/add_iast.py`, `publish/tools/accents/accent_volume.py` (new), `publish/tools/pageprep/crop_pages.py`, `publish/tools/ref_check/` (numeral file alignment), `vol14/tools/page.py` (strips at max dpi without viewer shrinking).

## 3. Proposed standard for Vol 15 onwards

**One shared toolkit, one config file per volume.**

```
tools/rv/            shared code (no per-volume copies)
  config.py          reads volN/volcfg.json
  page.py            render strips / zoom a box          (from vol14/tools/page.py)
  numerals_for.py    rows of the user's numeral file       (generalised)
  api_batch.py       the batch translator                 (generalised from vol14)
  labels.py, accents.py, checks.py, doubt.py, append_en.py
  build/             docx/PDF (from publish/)
volN/volcfg.json     scan parts, printed = PDF - k with a list of [from_pdf, new_k], duplicate/missing PDFs,
                     output paths, first Mandala/Sukta, numeral file path, model, price, budget, branch
volN/prompt.md       volume-specific notes only (the common rules live in CLAUDE.md + tools/rv/PROMPT.md)
```

**Pipeline per 3-page batch (automatic, `python3 tools/rv/api_batch.py N`):**
1. Check the position from the progress note; skip configured duplicates.
2. Render strips; look up numeral rows (user's file).
3. API call: English + Devanagari (+ Kannada text for the volume's Kannada file); output chunk, note, doubts.
4. Scripted steps in a fixed order: `add_iast` → `labels.normalise` → `accent_volume` → structural checks (Ṛk counts, headings, numeral consistency) → append → doubts → commit.
5. Stop on any failed check; never on its own judgement.

**Second pass for the `[?]` places** (the API cannot zoom): a small job that reads `doubts` entries, renders a 300–450 dpi box for each, asks the model for a reading with the crop, and writes proposals to a review file for the user (nothing applied without the user). This is what the Vol 13 zoom-fix did by hand with Sonnet; it works (94 of 99 resolved).

**Decisions for the user before Vol 15**
1. Is the Mac API batch the main method for Vol 15 onwards (≈ $0.12/page on Sonnet)? Or keep Claude Code sessions for some?
2. Add the Kannada file to the same API call (Vol 11 rule), or keep it as a separate later pass?
3. Which model: Sonnet (cheaper, 5–20 `[?]`/batch in the pilot) or Opus (2–7)?
4. Pada accents: not covered by the Mandala HTML script; leave unaccented?
5. Freeze Vols 1–6 tools (move to `legacy/`) or leave them where they are? They are only needed for the planned back-fill passes.

## 4. Suggested order of work (nothing started)
1. Remove tracked `__pycache__`, add to `.gitignore`.
2. Create `tools/rv/` by generalising Vol 14's `page.py`, `api_batch.py`, `numerals_for.py`, `labels.py`, `accents.py`, `numeral_checks.py`, `doubt.py`, `append_en.py`; keep the Vol 14 scripts working until Vol 14 is done.
3. Write `volcfg.json` for Vol 14 first (proves the format), then Vol 15.
4. Dry-run on 3 pages of an already translated volume (e.g. Vol 13) and compare with the existing text.
5. Only then switch Vol 14's remaining pages over.
