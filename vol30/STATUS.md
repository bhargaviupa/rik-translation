# Vol 30 — status

*Update at the end of every working session. Rules: `CLAUDE.md`. Route: Batch API (as Vol 23; `docs/prompts/VOL23_API_PROMPT.md`).*

## Scope
Ṛgveda-saṃhitā Part 30 (Jayachamarajendra Vedaratnamala no. 30), the LAST part of the edition: Aṣṭaka 8, adhyāyas 5–8 = Maṇḍala 10 Sūktas 95–191 (`"mandalas": [10]`); ends with the colophon "ಋಗ್ವೇದಸಂಹಿತೆಯು ಸಮಾಪ್ತವು" and the benediction. Printed pp. 1–1288 (preface roman i–vii and contents viii–xii before p. 1). Editor-translator H. P. Venkata Rao; preface dated 30-9-1955. Branch `claude/zen-euler-5ntywc`.

## Source and inputs
Supplied by the user (Nov 25 2026) as three machine-read markdown files, `rig_30_1.md` (pp. 1–475), `rig_30_2.md` (476–975), `rig_30_3.md` (976–1288); concatenated into `vol30/html/rig_30.md` (the inputs are not kept; the user has them). Changes to the supplied text, and nothing else: (1) the converter footer lines `Pages: N/N` removed from each part; (2) the leading `Markdown source` line of parts 2 and 3 removed; (3) 132 embedded pictures moved to `vol30/html/figures/` by `tools/rv/extract_figures.py` (line replaced by `[figure: …]`); (4) `<!-- page 1 -->` inserted before the body title page (line 667); (5) 83 Pratipadārtha words corrected from the Wikisource Pada (`data/source_fixes.tsv`, see below). The seams (pp. 475/476 and 975/976) carry running heads, nothing lost.

`html_pages.py` (with the head-variant fix of Nov 25 2026, `ಸಾಯಣಭಾವ್ಯ/ಭಾಷ್ಪ/ಭಾಜ್ಯಸಹಿತಾ`, `ಋಗ್ವೇದಸಹಿತಾ`): 1271 pages for printed 1–1288; 17 printed numbers have no page of their own: 27, 148, 207, 237, 242, 243, 344, 598, 599, 941, 1059, 1081, 1129, 1130, 1207, 1241, 1271 (their text stands inside the page before; not checked one by one whether a head is misread).

## Word-meaning check (REQUIREMENTS C4/D18), Nov 25 2026
`pratipada_check.py 30 --source`: before: 143 `fix-certain`; 83 applied by `pratipada_apply.py` (one letter, not a case ending, voicing swap, visarga or an initial vowel added/dropped); after: 5,239 Pratipadārtha words ok (+83), 60 `fix-certain` left for the editor. Ṛks not matched to the reference: 161 Pratipadārtha words, 455 Pada words (small share).

## Preface
Translated by `api_front.py 30 3 253 preface` (one request, $0.119, checks PASS, 0 NOTE) and installed Nov 25 2026.

## Plan (free)
`api_batch.py plan 30 --windows 260`: 212 windows, about 1285 pages, 4,855,941 input tokens, estimate input $4.86 + output $12.14–29.14. Vol 23's real cost was about 74% of the low end of its estimate, so about $12–13 is expected. Not submitted: waiting for the user's yes (ceiling $20, user, Nov 25).

## Status
Done through printed p. 1288 (the whole volume and the last of the edition; one API batch of 212 windows submitted and collected Nov 25 2026; `batch.py audit 30` passes; `check_labels.py 30`: 2358 English blocks, 2361 Kannada, 0 not matched, 0 under another section's label; `rkheads 30 --dry-run`: nothing to change; `kn_headings.py 30 --write` run: 97 sūktas (Maṇḍala 10, Sūktas 95–191, all in order), 680 Ṛk headings). Preface (roman pp. i–vii) translated and installed. Real cost: batch $11.81 + preface $0.12 + w0712 direct $0.10 = about $12.03 of the $20 ceiling (the estimate's low end was $17.0). 305 `**NOTE**` marks in the English text, 320 rows in `review/notes.tsv`.

## Repairs (all in `review/repair_log.md`)
17 windows stopped or failed after the commit (heading missing, blocks counted one off by garbled labels in the supplied text, a Saṃhitā split at a window break, remarks, a cut-off answer (w0712 re-sent), a picture that was an ornament, glued heading, Ṛk headings out of order). New shared tools from this volume: `tools/rv/fix_split_samhita.py`, head-variant recognition in `html_pages.py`, more remark patterns in `api_batch.py`, `--only` and the initial-vowel rule in `pratipada_apply.py`.

## Open items
1. (user) 305 `**NOTE**` questions in `review/notes.tsv`.
2. (user) 60 `fix-certain` Pratipadārtha rows left (`review/pratipada_check_source.tsv`) and the `near`/`absent` rows.
3. (user) Kannada sūkta numbers misprinted as 109, 128, 122 where the order gives 119, 129, 172 (`kn_headings.py` WARN; heading follows the English order).
4. (user) 17 printed numbers without a page of their own (see above): the English and Kannada carry no page mark for them.
5. (user) Findings of the QA samples left for the editor: see the last line of `review/repair_log.md` (Telugu Pada of Ṛk 4 p. 651, Kannada prose in the bhāṣya blocks pp. 173/851/857/859, short-e sign ॆ/è from the Kannada, IAST-only headwords).
6. Front matter and PDFs not done: need the user's front-matter scan PDF; WeasyPrint and fonts are not installed in cloud sessions.

## Finishing checklist (HANDBOOK §11), Nov 25 2026
Done: 1 (last window, p. 1288), 2 (`check_labels`: 0; `repair_inline`: 0 left; `check_inline` over all windows: 0 mismatches; `refs_fix`: 1 English line would change, left to the reference-corrector), 3 (accent report with `--api`, $0.30: 210 unmatched before, 55 accepted; `review/accent_report.tsv`, `accent_report_pages.tsv`, report only), 4 (`kn_headings.py 30 --write`), 5 (QA: two samples of 24 pages by Opus agents, read-only: **10 ERRORs, 42 MINORs**; the clear findings repaired; the second sample was taken at once because the first showed errors), 7 (review lists: `notes.tsv` 321 rows, `inline_mismatch.tsv`, `page_flags.md`, `accent_report_pages.tsv`, `qa_sample.md`, `qa_sample_2.md`; `doubts.tsv` none), 8 (metrics below), 9 (lessons in `docs/LESSONS.md`). Not done: 6 (front matter and PDFs).

## Metrics
| windows | pages | hand-fixes by kind | gate failures | `[?]` | inline mismatches | accent lines unmatched | QA samples (pages, errors, minors) | cost |
|---|---|---|---|---|---|---|---|---|
| 212 batch windows + 1 re-sent (w0712) | 1288 printed (1271 pages in the source, 17 numbers without a head) | 17 stops or failed verifications: missing heading 3, blocks counted one off 4, Saṃhitā split at a window break 2, Ṛk headings/sūkta headings 3, remarks 3, cut-off answer 1, picture ornament 1, Cyrillic letter 1 | 17 | 0 | 0 | 155 (210 − 55 by `--api`) | 48 pages, 10 errors, 42 minors | $11.81 batch + $0.12 preface + $0.10 direct + $0.30 accent API = $12.33; QA agents not counted |

## English review PDF (2026-11-28, branch claude/vol30-pdf)
Built `vol30/review/vol30_full_Eng.pdf` (2147 pages, pdf_check passes; NOTE 311). No contents page (pubcfg `no_index`: waiting for the user to choose none / generated Sūkta table). Volume is final (colophon present).
