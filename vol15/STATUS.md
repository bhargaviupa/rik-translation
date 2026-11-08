# Vol 15 — status

*Moved out of the general CLAUDE.md on Nov 8 2026. Update this file (not CLAUDE.md) whenever the state of this volume changes.*

## Scope
Maṇḍala 2 Sūktas 24–43 and Maṇḍala 3 Sūktas 1–6 (Second Aṣṭaka, Adhyāyas 7–8), printed pp. 1–800. First volume made entirely from the supplied machine-read text (no scans).

## Source and inputs
`vol15/html/rig_15_1.md` (front matter lines 1–445, then printed pp. 1–435) and `rig_15_2.md` (pp. 436–800); `vol15/volcfg.json` `source`. Front-matter scan PDF supplied by the user (Nov 8 2026, 15 pages) → `publish/assets/vol15/fm_NN.jpg`. No page scans in the repo.

## Outputs
`vol15/Rigveda_Samhita_Vol15_English_Translation.md` and `…_Kannada_Text.md` (merged to `main`); `publish/out/vol15_full_Eng.pdf` / `vol15_full_Kan.pdf`.

## How it was made
Standing single Sonnet agent, one 3-page window per batch (≈ 257 windows, p. 1–800); dispatcher verified every commit (`git log`, one progress note, no `XXX`). Cost log `vol15/parts/batch_costs.md` (tokens mostly 'n/a'). Details of the method: `CLAUDE.md` (pipeline).

## Status
Translated through printed p. 800 (final; colophon on p. 800). Front matter is **not translated by the user's decision**; the Kannada PDF carries the original scans.

## Open items
- 118 `[?]` in `review/doubts.tsv`; 39 inline Sanskrit segments of early windows differ from kn.md (`review/inline_mismatch.tsv`, need the scan).
- Accent mismatches/non-matches are mostly not logged in `review/accent_report.tsv` (agents reported them in chat only).
- `review/page_flags.md`: merged page heads, missing real p. 235, truncated lines pp. 495–496, p. 527 reference.
- Sūkta 39/40 have no `##` heading in the English file (volbook supplies them in memory).
- ~500 multi-line Sanskrit quotations are raw Kannada script in the English .md (volbook converts them for the PDF; the .md is unchanged).
- Printed contents: all 159 numbers match the scan; '443' (Jātavedas) is as printed (`review/contents_check.md`).
- Kannada text has no Sūkta/Ṛk headings.

## Publication (print PDF)
`python3 publish/volbook.py 15 [eng|kan]` (config `vol15/pubcfg.json`); outputs in `publish/out/`; front matter = the user's scan pages; Guruji and 'present day' pages kept (user decision).

## Pointers
`vol15/README.md`, `vol15/volcfg.json`, `vol15/pubcfg.json`, `vol15/review/`, `vol15/parts/`.
