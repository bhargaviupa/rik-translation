# Vol 23 — status

*Update at the end of every working session. Rules: `CLAUDE.md`. Route: Batch API (`docs/prompts/VOL23_API_PROMPT.md`).*

## Scope
Ṛgveda-saṃhitā Part 23 (Jayachamarajendra Vedaratnamala no. 23): Aṣṭaka 5 adhyāyas 6–8 and Aṣṭaka 6 adhyāya 1 = Maṇḍala 7 Sūktas 81–104 and Maṇḍala 8 Sūktas 1–20 (`"mandalas": [7, 8]`; from the supplied contents page and the running heads). Printed pp. 1–856 (preface and contents before p. 1). Editor-translator H. P. Venkata Rao; preface dated 21-8-1953. Branch `claude/zen-euler-5ntywc`.

## Source and inputs
Supplied by the user (Nov 24 2026) as two machine-read markdown files, `rig_23_1.md` (pp. to 388) and `rig_23_2.md` (from 389); concatenated into `vol23/html/rig_23.md` (the inputs are not kept; the user has them). Changes to the supplied text, and nothing else: (1) the converter footer lines `Pages: 395/395` and `Pages: 468/468` removed; (2) the leading `Markdown source` line of part 2 removed; (3) 72 embedded pictures moved to `vol23/html/figures/` by `tools/rv/extract_figures.py` (line replaced by `[figure: …]`); (4) `<!-- page 1 -->` inserted before the body title page (line 305). `merge_md.py` refused its automatic check (4 pages at the seam and the end are numbered differently when a file is split alone: the OCR heads of printed pp. 386–388 are misread, `೫೮೬`, `ಮುಗ್ರೇದಸಂಹಿತಾ . 387`); the merge itself is a plain concatenation.

`html_pages.py`: 770 pages, printed 1–856. 86 printed numbers have no page of their own in the text (the list is the second line of `python3 tools/rv/html_pages.py vol23/html/rig_23.md`): mostly pages without a running head (first pages of a sūkta or section, lesson 67); NOT yet checked one by one whether any page is really missing. Front matter lines 1–~304 (title pages, dedication, preface, contents). The text ends with `॥ ಮಂಗಳಂ ॥` (line 36949).

## Word-meaning check (Nov 24 2026; REQUIREMENTS C4/D18)
`pratipada_check.py 23 --source`: Pratipadārtha words ok 3,624; `fix-certain` 101 (66 pass the apply filters, 28 are not one letter / change an ending, 7 not found once); Ṛks not matched to the reference ('noref'): 253 of the Pratipadārtha words, 624 of the Pada words (< a third: layout fine). **Not applied yet**: waiting for the user's yes (`python3 tools/rv/pratipada_apply.py 23`, then `--write`).

## Preface
Translated by `api_front.py 23 2 94 preface` (one request, $0.040, checks PASS, 0 NOTE) and installed Nov 24 2026 (logged in `review/repair_log.md`). Word-meaning corrections: 66 applied Nov 24 (user's yes), check re-run: 3,690 ok (+66), no new mismatch.

## Plan (free)
`api_batch.py plan 23 --windows 150`: 129 windows, about 849 pages, 2,774,590 input tokens, estimate **$9.7–19.4** (input $2.77 + output $6.94–16.65). Not submitted.

## Status
Done through printed p. 856 (the whole volume; one API batch of 129 windows submitted Nov 24 2026, collected the same day; `batch.py audit 23` passes; `rkheads 23 --dry-run`: nothing to change; `kn_headings.py 23 --write` run: 44 sūktas, 699 Ṛk headings). Sūktas present in order: Maṇḍala 7 Sūktas 81–104, Maṇḍala 8 Sūktas 1–20. Preface translated and installed. Cost: batch $7.17 (real usage) + preface $0.04 + three direct requests ($0.092 + $0.024 + earlier none) = about $7.33 of the $25. 173 `**NOTE**` marks in the English text (175 rows in `review/notes.tsv`), 0 `**GLOSS**`.

## What was repaired by hand or by script (all in `review/repair_log.md`)
Printed pp. 372–373 (Maṇḍala 8 Sūkta 2, Ṛks 36–38) had running heads misread as 572/573 in the supplied text: corrected in `html/rig_23.md` (`data/source_fixes.tsv`), translated by one direct request (`tools/rv/api_window.py`) and INSERTED before p. 374 (a logged exception to append-only); w0569 re-translated the same way. 66 Pratipadārtha words corrected from the Pada reference (`data/source_fixes.tsv`; `tools/rv/pratipada_check.py`/`pratipada_apply.py`). Windows stopped by gates and were repaired: w0008, w0016, w0045, w0067, w0140, w0206, w0264, w0337, w0389, w0396, w0524, w0588, w0631, w0740, w0802, w0835, w0841 (kinds: Sanskrit typed in Latin letters inside quotes, translator remarks about window breaks, a second Saṃhitā heading for the second line of a verse, blocks counted one off because of a stray label or a Kannada line set as a block, a page without a running head). The first two kinds are now settled by script in `tools/rv/api_batch.py` (lessons for `docs/LESSONS.md`).

## Open items
1. (user) 173 `**NOTE**` questions in `review/notes.tsv`.
2. (dispatcher) 84 printed page numbers have no running head in the supplied text (`html_pages.py` "missing numbers"); the text of such a page stands inside the preceding page, so the Kannada and English files carry no page mark for them (p. 843 was added by hand). Page 372/373 were the only ones found to be misread heads; the others look like genuine missing heads (the preceding page is unusually long).
3. (user) `kn_headings.py` warning: Kannada line 29716 reads Sūkta 18 (as supplied) where the English order has Sūkta 17 (Maṇḍala 8): the heading follows the English order; check the supplied sūkta number.
4. (user) the accent report has NOMATCH lines (`--api` with `RIK_API_KEY`).
5. (user) word-meaning rows not applied (35 `fix-certain` that failed the one-letter filter, `fix`, `near`, `absent`): `review/pratipada_check_source.tsv`.
6. Finishing checklist (accent report, QA, PDFs, front matter jsons) not done.

## Metrics
