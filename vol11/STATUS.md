# Vol 11 — status

*Moved out of the general CLAUDE.md on Nov 8 2026. Update this file (not CLAUDE.md) whenever the state of this volume changes.*

## Scope
Maṇḍala 1 Sūktas 137–157 (Second Adhyāya of the Second Aṣṭaka).

## Source and inputs
Scan in `vol11/scans/`.

## Re-translation from the supplied text (started Nov 12 2026)
`vol11/html/rig_11.md` = the user's `rig_11_1.md` (350 source pages, printed pp. 2–332) + `rig_11_2.md` (364 source pages, pp. 333–696), merged losslessly except for the converter's two `Pages: N/N` footer lines (removed); the originals are in the commit before the merge. The splitter finds 658 pages, printed 2–696, 37 numbers without a head of their own (6, 24, 42, 66, 78, 100, 104, 129, 137, 140, 144, 149, 160, 176, 180, 210, 211, 226, 250, 262, 266, 278, 314, 334, 350, 382, 416, 457, 458, 482, 496, 510, 514, 532, 590, 651, 668: pages that print no running head, merged into the page before). Head numbers repaired by the splitter's neighbour rule: 93→92, 153→155, 263→268, 533→535, 638→658, 693→695; **p. 211/212 is ambiguous** (head reads 211, rule gives 212, pages 210 and 211 have no head). Decisions of the user (Nov 12 2026): all pages exist even where the number is not printed (the translator marks them); **printed p. 1 prints no number: `<!-- page 1 -->` inserted before the opening "ॐ" (line 591)**; **p. 212 is not decided: the mark `**NOTE**{printed page number 212? …}` goes on that page** (`page_notes` in `volcfg.json`, shown in the window's TASK.md); route = Batch API (`tools/rv/api_batch.py`); conventions of Vols 17–18 (`note_style` NOTE, bhāṣya block Devanagari only, grammar in Sanskrit, layout subheads). The 33 embedded pictures were extracted by `tools/rv/extract_figures.py` to `vol11/html/figures/` (`fig_lineNNNNN.ext`, N = line in `rig_11.md`) and replaced by `[figure: …]` lines. The scan-based files were renamed `Rigveda_Samhita_Vol11_scan_English_Translation.*` / `…_scan_Kannada_Text.*` (md, docx, pdf; kept for comparison); the standard names now belong to the new run (`volcfg.json`, window 6). Scripts of the old build (`publish/`, `publish/tools/verify11/`) still point to the old names: update them when the new Vol 11 is built.

## Stage 1 of the batch-API run (Nov 12 2026, branch claude/zen-clarke-2ogr57)
Base: the set-up of claude/gallant-dijkstra-e9ze2x merged into this branch (user's choice). Preface (lines 126–368 of `rig_11.md`, 2 hand repairs) installed; **printed pp. 1–267 translated** (41 windows, one batch, no retries). Cost of the 41 windows **$4.31** (estimate $3.7–7.4; `parts/batch_costs.md`); the preface's cost was not logged (tool bug, fixed; Vol 18's preface was $0.224). `audit 11` passes at "done through printed p. 267"; `check_labels.py 11`: 0 under the label of another section; `rkheads --dry-run`: nothing to change. Sūktas 137–141 complete and 142 begun; 227 rows in `review/notes.tsv`. Page 211 has no heading (undecided by the user: the NOTE "printed page number 212?" stands on p. 212).
Windows that stopped `collect` (10 of 41, all repaired by hand, `review/repair_log.md`): w0014 (missing page heading; Arabic letter in "Paruchchhepa"), w0020 / w0052 / w0202 (Pāṇini sūtra numbers changed by the model from memory or guessed, with self-notes), w0033 (two `<en>` blocks in the answer; Pada label garbled in kn.md), w0064 (page heading inside a grammar entry), w0229 (remark "[as printed]"). Shared tools changed: stray-script gate, last `<en>` block, `join_split_entries`, BRIEF line on sūtra numbers, `api_front` makedirs.

## Stage 2 (Nov 12 2026): printed pp. 268–519
40 windows, one batch, no retries; **$3.67** (estimate $0.96 input + $2.41–5.78 output); running total of the 81 windows **$7.98** (`parts/batch_costs.md`). `audit 11` passes at "done through printed p. 519"; `check_labels.py 11`: 0; `rkheads --dry-run`: nothing to change; Sūktas 137–151 complete and 152 begun (every sūkta's Ṛks 1…n); 369 rows in `review/notes.tsv`. Page 211 still the only page without a heading.
Windows that stopped `collect` (7 of 40): w0281, w0356, w0405 (sūtra number whose hyphen the print lost at a space or line break: NOTE; the shared twin check now accepts this form), w0324 (stray `## Special Topics (continued)` heading, removed in the volume file), w0424 (remark "[as printed]"; now stripped by the tool), w0493 (Saṃhitā heading and label repeated for a verse running over a page break), plus the Sūkta 147 stray heading (w0418) found afterwards. Repairs in `review/repair_log.md`. Known, not repaired: the model sometimes leaves a Kannada phrase inside the Sanskrit grammar (e.g. "ರಸರವಾಗಿ ಬರುತ್ತದೆ", p. 156, p. 356) because the print has it so; the QA agents' page-boundary placement of headings (see `review/qa_sample.md`) is unchanged.

## Stage 3 and end of the translation (Nov 12 2026): printed pp. 520–696
29 windows, one batch, no retries; **$2.37** (estimate $0.71 input + $1.77–4.26 output). **Whole volume: preface + 110 windows = $10.36 for windows** (stage 1 $4.31, stage 2 $3.67, stage 3 $2.37; preface not logged; `parts/batch_costs.md`), 696 printed pages (about $0.015 a page). **Translation complete: `audit 11` passes at "done through printed p. 696"** (695 page headings; p. 211 has none, undecided by the user; colophon, "Śrīḥ / Om tat sat", closing verse and "Śubhaṃ bhūyāt / Maṅgalaṃ" at the end, nothing added). 21 sūktas (137–157), 143 Ṛk headings, every sūkta's Ṛks 1…n (counts: 3 4 11 13 13 13 8 7 5 5 5 5 5 3 9 7 4 6 6 5 6); `check_labels.py 11`: 0; `rkheads --dry-run`: nothing to change; 469 rows in `review/notes.tsv`.
Stage 3 stops (5 of 29): w0581 (page heading inside a quotation that crosses a page), w0587 (sūtra number split by a running head: NOTE), w0648 (remark "[sic, as printed]", hand IAST), w0661 (Telugu letter in the supplied printed English; gate now ignores letters that kn.md has), w0692 (answer without `<en>` tags; extractor now accepts it). All in `review/repair_log.md`.
**Free end-of-volume scripts done:** `kn_headings --write` (21 sūktas, 143 Ṛks; the supplied Kannada reads "Sūkta 150" at the place of Sūkta 152: the heading follows the English order); Dravidian vowel signs in Devanagari (ॆ ॊ): 146 lines, almost all single misread letters of the supplied Sanskrit, left as supplied: `review/dravidian_signs.tsv`; doubled daṇḍa: 8 lines, `review/doubled_danda.tsv`; **second reading from the old translation**: `tools/rv/legacy_refs.py` (new shared script) → `review/legacy_compare.tsv` (550 of 696 pages differ in references; 1,024 reference numerals only in the old text, 1,828 only in the new; the old text was read from scans with 5,666 `[?]` marks, so most differences are its misreadings; for the user, nothing was changed from it); the stock page comparison is in `review/legacy_compare_pages.tsv`.
Not done (separate job, with the user): the finishing checklist (HANDBOOK §11: accent report, QA sample of stages 2–3, front matter, PDFs; the old build scripts still use the old file names).

## Finishing job (Nov 12 2026)
Done: `refs_fix` (0 changes), `repair_inline` (22 leftover ⟦ ⟧ wrappers around quoted verses on pp. 299–304 removed, now 0; logged), `check_labels` 0, `check_inline` over all windows 0 mismatches; Kannada headings (21 sūktas, 143 Ṛks); accent report (`review/accent_report.tsv`, `accent_report_pages.tsv`: 119 lines: 88 without a match in the reference, 22 OK_VERSE, 7 DIFF, 2 OK_PART; the other lines were accented window by window; nothing accented by hand, `--write` not run); second QA sample of stages 2–3 (`review/qa_sample.md`, second part: no ERROR beyond 5 remarks, repaired); review PDFs built with `publish/volbook.py 11` from `vol11/pubcfg.json` (new): `publish/out/vol11_full_Eng.pdf` (962 pp.) and `vol11_full_Kan.pdf` (766 pp.), each with `.html`; first pages and a body page of both looked at as images; no dotted circles (◌) in `pdftotext`. Front matter = title page + credits only (as Vol 18).
**Check before anyone relies on the PDFs:** the credits page text is the shared template: it says the cover, portrait and permission page are "reproduced from the scanned front matter" and that board, preface, contents and abbreviations are "translated"; for Vol 11 none of that exists yet (no front-matter scan, no `frontmatter_en.json`, no `contents_en.json`; only the preface is translated, in the body file). The year **1950** in `pubcfg.json` is taken from the preface's date (20-6-1950); the supplied title page shows no year; the imprint "Śrī Vināyak Press, Mysore" is from the supplied title page. Publisher/ISBN/rights remain placeholders (`publish/release.json`).
Not done: front matter proper (needs the user's scan PDF of the front matter, §8 steps 1–3; contents from `html/rig_11.md` lines 373–590, abbreviations; the supplied md has the board and a list of scholars); accents `--write` (only when asked); the old `publish/` Vol 11 scripts still use the old file names.
Metrics: 110 windows (41 + 40 + 29), 696 pages, windows cost $10.36 (preface not logged); 22 windows stopped `collect` once (10 + 7 + 5), no retries; 469 NOTE rows; 0 `[?]`; hand repairs by kind in `review/repair_log.md`.

## Outputs
`vol11/Rigveda_Samhita_Vol11_English_Translation.md` and `…_Kannada_Text.md` (+ docx/pdf each).

## How it was made
Scan-based legacy workflow; accents by `accent_volume.py` (first volume with accents by script); Kannada text built alongside (decision Oct 2026).

## Status
Re-translated from the supplied text by the batch API (Nov 12 2026, pp. 1–696, complete); the scan-based files are `*_scan_*` (kept for comparison).

## Open items
Verification pass: `docs/SESSION_REPORT_Vol11_verification.md`, `docs/VERIFY_PASS_REQUIREMENTS.md`, `publish/tools/verify11/`.

## Publication (print PDF)
Built with `build_vol45.py 11 full` (accent CSS); `publish/out/vol11_full.pdf`.

## Pointers
`docs/SESSION_REPORT_Vol11_verification.md`.
