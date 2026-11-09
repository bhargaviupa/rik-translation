# Vol 15 — status

*Moved out of the general CLAUDE.md on Nov 8 2026. Update this file (not CLAUDE.md) whenever the state of this volume changes.*

## Scope
Maṇḍala 2 Sūktas 24–43 and Maṇḍala 3 Sūktas 1–6 (Second Aṣṭaka, Adhyāyas 7–8), printed pp. 1–800. First volume made entirely from the supplied machine-read text (no scans).

## Source and inputs
`vol15/html/rig_15.md` (the user's two files `rig_15_1.md` + `rig_15_2.md` merged losslessly with `tools/rv/merge_md.py`: front matter lines 1–445, then printed pp. 1–800; the page split is identical to the two originals; `volcfg.json` `source` = `rig_15.md@2-800`). Front-matter scan PDF supplied by the user (Nov 8 2026, 15 pages) → `publish/assets/vol15/fm_NN.jpg`. No page scans in the repo.

## Outputs
`vol15/Rigveda_Samhita_Vol15_English_Translation.md` and `…_Kannada_Text.md` (merged to `main`); `publish/out/vol15_full_Eng.pdf` / `vol15_full_Kan.pdf`.

## How it was made
Standing single Sonnet agent, one 3-page window per batch (≈ 257 windows, p. 1–800); dispatcher verified every commit (`git log`, one progress note, no `XXX`). Cost log `vol15/parts/batch_costs.md` (tokens mostly 'n/a'). Details of the method: `CLAUDE.md` (pipeline).

## Status
Translated through printed p. 800 (final; colophon on p. 800). Front matter is **not translated by the user's decision**; the Kannada PDF carries the original scans.

## Open items
Done on Nov 9 2026 (branch `claude/vol15-fixes`, logged in `review/repair_log.md`): the 500 leftover multi-line `⟦Kannada Sanskrit⟧` quotations of the English file converted to Devanagari + (IAST) (`tools/rv/repair_inline.py`; `tools/rv/convert.py` now joins such lines so future windows are right); the missing `## Sūkta 39` / `## Sūkta 40` headings inserted; Maṇḍala/Sūkta/Ṛk headings added to the Kannada file from the English structure (`tools/rv/kn_headings.py`; 26 sūktas + 276 Ṛks; one printed sūkta line reads "ಸೂಕ್ತ—೫" at Kannada line ~3634 where the sequence says Sūkta 28: kept as supplied, logged as WARN); the accent report regenerated (`review/accent_report.tsv`, 57 Saṃhitā lines the accented reference did not match + 1 partial; with printed pages in `review/accent_report_pages.tsv`).

**User:** (1) the 118 `[?]` in `review/doubts.tsv`; (2) the 39 inline Sanskrit segments in `review/inline_mismatch.tsv` (need the scan); (3) `review/page_flags.md` (missing real p. 235, truncated lines pp. 495–496, p. 527 reference); (4) the 57 unmatched accent lines (`accent_report_pages.tsv`: unaccented Saṃhitā lines; they differ in spelling from the reference text); (5) publisher/ISBN/permissions text and the "present day" portraits; (6) the QA sample (`review/qa_sample.md`).
Printed contents: all 159 numbers match the scan; "443" (Jātavedas) is as printed (`review/contents_check.md`).
Front matter is deliberately not translated.

## Publication (print PDF)
`python3 publish/volbook.py 15 [eng|kan]` (config `vol15/pubcfg.json`); outputs in `publish/out/`; front matter = the user's scan pages; Guruji and 'present day' pages kept (user decision).

## Metrics (Vol 15 = the baseline; later volumes should beat it)
| windows | pages | hand-fixes | gate failures | `[?]` | inline mismatches | accent lines unmatched | QA sample | tokens / cost |
|---|---|---|---|---|---|---|---|---|
| ≈ 257 | 800 | ≈ 40 merged page heads; ≈ 1 garbled label per Ṛk; ≈ 1 stray line per ~3 pages; hyphen joins in most windows (counts not logged: start logging) | 3 known (batch 121 false report; `XXX` placeholder; empty inline segment); 1 silent failed edit | 118 | 39 | 57 | 12 pages: 0 errors, 4 minor (fixed) | standing agent ≈ 11–27k per batch (early lines "n/a") |

## Lessons from this volume
See `docs/LESSONS.md` (items 1–24 come from Vol 15).

## Pointers
`vol15/README.md`, `vol15/volcfg.json`, `vol15/pubcfg.json`, `vol15/review/`, `vol15/parts/`.
