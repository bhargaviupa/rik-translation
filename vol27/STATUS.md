# Vol 27 — status

*Update at the end of every working session. Rules: `CLAUDE.md`. Route: Batch API (as Vols 23 and 30).*

## Scope
Ṛgveda-saṃhitā Part 27: Aṣṭaka 7, adhyāyas 5–8 = Maṇḍala 9 Sūktas 101–114 and Maṇḍala 10 Sūktas 1–40 (`"mandalas": [9, 10]`). Printed pp. 1–992 (editor's preface dated 7-5-1954 and contents before p. 1). Editor-translator H. P. Venkata Rao. Branch `claude/zen-euler-5ntywc`.

## Source and inputs
Supplied by the user (Nov 25 2026) as three machine-read files, `rig_27_1.md` (pp. 1–385), `rig_27_2.md` (386–785), `rig_27_3.md` (786–992); concatenated into `vol27/html/rig_27.md` (inputs not kept; the user has them). Changes to the supplied text, and nothing else: (1) converter footers `Pages: N/N` removed; (2) the leading `Markdown source` line of parts 2 and 3 removed; (3) 79 embedded pictures moved to `vol27/html/figures/` by `tools/rv/extract_figures.py`; (4) `<!-- page 1 -->` inserted before the body title page (line 354); (5) 60 Pratipadārtha words corrected from the Wikisource Pada (`data/source_fixes.tsv`). The seams carry running heads (pp. 385/386, 785/786).
`html_pages.py` (with the head-variant fixes of Nov 25 2026, including a structural head pattern): 975 pages for printed 1–992; 17 printed numbers without a page of their own: 137, 148, 177, 241, 242, 281, 312, 349, 518, 549, 624, 625, 639, 773, 835, 843, 903 (not checked one by one).

## Word-meaning check (REQUIREMENTS C4/D18)
Before: 96 `fix-certain` rows; 60 applied (one letter, not an ending/voicing/visarga/initial vowel); after: 3,676 Pratipadārtha words ok (+60), 36 `fix-certain` left for the editor. Ṛks not matched to the reference: 930 Pada words (17%), 162 Pratipadārtha words.

## Preface
Translated by `api_front.py 27 2 72 preface` ($0.035, checks PASS, 0 NOTE), installed Nov 25 2026.

## Plan and batch
Full plan: 163 windows, 991 pages, 3,698,515 input tokens (estimate $3.70 + output $9.25–22.19). The user has about $8 of API budget (Nov 25 2026), so the batch is cut to the FIRST 120 windows (pp. 1–about 732, 2,739,105 input tokens; expected real cost $6.7–7.1 from Vols 23 and 30: $2.4–2.6 per million input tokens). The remaining 43 windows (about pp. 733–992, about $2.4) wait for more budget: `api_batch.py plan 27 --windows 60` continues after the last committed page.

## Status
**Done through printed p. 992: the whole volume** (colophon and benediction on p. 992). Batch API: 130 windows, pp. 1–794 (two batches, Nov 25 2026, $6.95 + $0.58); agents: the last 33 windows, pp. 795–992 (11 batches of three windows by Sonnet agents, Nov 25–26 2026, 14–23 tool uses and 157k–192k tokens each, see `parts/batch_costs.md`), after the API budget was spent. `batch.py audit 27` passes; `next 27`: "no further window"; `check_labels.py 27`: 1947 English blocks, 1947 Kannada, 0 not matched; `rkheads 27 --dry-run`: nothing to change; sūkta sequence checked by script: Maṇḍala 9 Sūktas 101–114 and Maṇḍala 10 Sūktas 1–40, all present in order; `kn_headings.py 27 --write` run (54 sūktas, 578 Ṛk headings). Ṛk counts agree with the Wikisource reference in every sūkta except Maṇḍala 10 Sūkta 10 (13 headings for 14 Ṛks: Ṛk 4 has no Saṃhitā/Pada in the supplied text, NOTE and `notes.tsv` row). 481 `**NOTE**` marks = 481 rows in `review/notes.tsv`; 9 `**GLOSS**` marks. Preface translated and installed.

## Repairs (in `review/repair_log.md`)
Batch API part: 14 windows stopped or failed after commit (list in the log). Agent part: garbled Pada label of p. 853 restored in both files; 'Viśpalā' → 'Viśvalā'; a doubled phrase on p. 989 and a cut Pratipadārtha entry on pp. 983/984 joined.

## Open items
1. (user) 481 `**NOTE**` questions in `review/notes.tsv`; 36 `fix-certain` word-meaning rows left and the `near`/`absent` rows (`review/pratipada_check_source.tsv`).
2. (user) the Saṃhitā and Pada of 10.10.4 missing in the supplied text.
3. 17 printed numbers without a page of their own (see above).
4. The finishing checklist (HANDBOOK §11: accent report, QA samples, review lists, front matter and PDFs, metrics, lessons) is not run yet.
5. Merge to `main` when the user says so.
