# Vol 5 second pass — running status report
(updated after every batch; the plan is `batches.tsv`; rows of findings: `findings.tsv`; repairs: `../repair_log.md`)

Batches are of **15 printed pages** (not 30): a Kannada page is ~3 500 characters and the pilot (10 pages) cost 140k tokens, so 30 pages would not fit one agent's context. One fresh Sonnet agent per batch, one at a time; after each batch: findings appended, `second_pass_apply.py 5` applied, commit, push.

| Batch | Pages | Rows | Applied | Not applied / questions | Commit |
|---|---|---|---|---|---|
| pilot | 350–359 | 21 | 18 | 1 not applied (p. 354, whole Pratipadārtha omitted: needs a hand insertion) + 2 questions | see git log |
| 1 | 185–199 | 20 | 16 | 4 questions (one set from applied by me: L3657 'your sacrifices', a misprinted Kannada word); agent tokens 197k | see git log |
| 2 | 200–214 | 16 | 15 | 1 question (p. 206 stopāsakānām); agent tokens: see notification | see git log |
