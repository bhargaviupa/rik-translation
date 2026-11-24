# The status report of a second pass — one format for every volume

Proposed Nov 24 2026 from the Vol 5 report (`STATUS_REPORT.md`, branch `hopeful-mayer-wuypje`) and the Vol 6 record. **The report is made by `tools/rv/sp_report.py N`; nobody types it.** It reads four machine files in `volN/review/second_pass/` and writes `volN/review/second_pass/STATUS_REPORT.md`. After every batch the dispatcher runs one command:

```
python3 tools/rv/sp_report.py N --add-batch FIRST LAST --tokens 272k --commit abc1234 [--edits-ok N --edits-failed N] [--note "…"]
```
(rows, applied and questions of the batch are **counted** from `findings.tsv` for those pages; the commit is the commit of the batch's work, put in the next commit if it is not known yet; `--pages LO-HI` on any run gives "x of y pages".)

## The files (same names and columns in every volume)
| File | Columns | Written by |
|---|---|---|
| `findings.tsv` | page, kind (a code of `docs/ERROR_KINDS.md`), reader (R1\|R3\|R6), place, as_found, proposed, basis, decision (applied\|question), log | the batch reader, append only |
| `questions.tsv` | page, place, as_found, question, why_not_settled | the batch reader, one row per `question` finding |
| `batches.tsv` | batch, first, last, rows, applied, edits_ok, edits_failed, questions, tokens, commit, date, note | `sp_report.py --add-batch` |
| `open.tsv` | kind (page-absent\|boundary-shifted\|marker\|block-not-read\|tool\|findings-row-stale\|other), pages, text | the dispatcher: things the editor must know that are not findings |
| `edits/eA-B.tsv` + `.result.tsv` | page, target (en\|kn), old, new, kind, basis; result: status | the reader; `tools/rv/sp_apply.py` |

## The report (always these seven parts, in this order)
1. **State** — stage; pages read "x of y" with the list of batches; findings (applied / questions); edits ok / failed; reader tokens and tokens per page; last commit.
2. **Batches** — one row each: batch, pages, findings, applied, edits ok / failed, questions, tokens, commit, note (the note is one line: what was unusual).
3. **Findings by kind** — kind, applied, questions, total; then the count by reader.
4. **Open items (not findings)** — absent pages, shifted page boundaries, wrong page markers, blocks the pass does not read, tool problems, stale rows. Each with its pages.
5. **Questions for the editor** — the count and the kinds; the rows are in `questions.tsv`.
6. **Files** — where everything is, including `repair_log.md` and `data/source_fixes.tsv`.
7. **Next** — what is done next.

## What changes for Vol 5 (differences found on Nov 24 2026)
- **Batch size:** Vol 5 uses 15 pages, Vol 6 30. The report does not care; the batch row says which pages.
- **Commit and tokens:** Vol 5's columns say "see git log" and "see notification". Use the real short hash and the agent's token count (k).
- **Failures:** Vol 5's "not applied" is one column mixed with questions. Use `edits_ok / edits_failed` (edits that could not be placed) and `questions` (decision `question`) as separate columns.
- **Findings columns:** in Vol 5 the `kind` and `reader` columns are mixed in places (`kind` = R1, `reader` = S2, `place` with `L6534:` line numbers of the English file). Use kind = the code (S1, S14, H29 …) and reader = R1|R3|R6; put a line number into `place` only after the words.
- **One batch file per batch** (`batch_185-199.tsv`) in Vol 5: use the single `findings.tsv` (append) and keep the per-batch edit files under `edits/`.
- **Apply tool:** Vol 5 has `tools/rv/second_pass_apply.py`; Vol 6 uses `tools/rv/sp_apply.py` (exact-once edits on `### Page N`, handles a page with two headings; it cannot place text in an English file organised by Ṛk, which is Vol 5's case). Two tools for one job should become one: the Vol 5 session decides which stays.
- **Pages without text:** in Vol 5 two pages (232–233) were found absent after a reader had assumed the text was in the neighbour page. Put every such page in `open.tsv` at S0 and say in the batch note when a reader could not read a page.
- The S0 sieve is `sieve.md` in both volumes, as now.

`python3 tools/rv/sp_report.py N` also rebuilds the report from the files alone at any time (no `--add-batch`), so a session can start by running it and reading part 1.
