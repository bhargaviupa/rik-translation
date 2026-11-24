# Vol 5 second pass — running status report
(updated after every batch; the plan is `batches.tsv`; rows of findings: `findings.tsv`; repairs: `../repair_log.md`)

Batches are of **15 printed pages** (not 30): a Kannada page is ~3 500 characters and the pilot (10 pages) cost 140k tokens, so 30 pages would not fit one agent's context. One fresh Sonnet agent per batch, one at a time; after each batch: findings appended, `second_pass_apply.py 5` applied, commit, push.

| Batch | Pages | Rows | Applied | Not applied / questions | Commit |
|---|---|---|---|---|---|
| pilot | 350–359 | 21 | 18 | 1 not applied (p. 354, whole Pratipadārtha omitted: needs a hand insertion) + 2 questions | see git log |
| 1 | 185–199 | 20 | 16 | 4 questions (one set from applied by me: L3657 'your sacrifices', a misprinted Kannada word); agent tokens 197k | see git log |
| 2 | 200–214 | 16 | 15 | 1 question (p. 206 stopāsakānām); agent tokens: see notification | see git log |
| 3 | 215–229 | 29 | 23 | 8 questions (6 R1, 1 R3, 1 R6) | see git log |
| 4 | 230–244 | 16 | 14 | 2 questions. pp. 232–233 are **absent from the supplied text** (the S0 note that such text stands in the neighbour page was wrong for them; batch 4b, a re-read on that assumption, found nothing to read). Their English comes from the older scan, per its own note: **unchecked, needs the user's text or scan** | see git log |
| 4b | 232–233 | 0 | 0 | not readable: no supplied text | see git log |
| 5 | 245–259 | 38 | 25 | questions: 17 (R1 8, R3 4, R6 1 and others); p. 260 not in the supplied text | see git log |
| 6 | 260–274 | 35 | 30 | 5 questions; p. 260 not in the supplied text | see git log |
