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

## Batch
Submitted Nov 24 2026 (user's yes): ONE batch of 129 windows, id in `vol23/work/api_batch.json` (`msgbatch_01AgqnECQJUJP2opjNg62PHJ`), estimate $9.7–19.4, ceiling $25. Next: `api_batch.py status 23` until ended, then `collect 23` (no commits by hand while it runs).

## Open items
1. (user) budget stated Nov 24: API $25 and the agent budget (66%) both expire Nov 25; yes to the body estimate not given yet.
2. (dispatcher) the body in few, large stages.
3. (dispatcher) check the 86 printed numbers without a page of their own.
