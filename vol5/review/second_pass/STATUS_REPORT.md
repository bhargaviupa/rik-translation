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
| 7 | 275–289 | 15 | 11 | 4 questions (R3) | see git log |
| 8 | 290–304 | 18 | 13 | 6 questions; p. 290 not in the supplied text. Name-spelling rows (Kausya, Varṣagaṇya, Prātarahna) rest on the Kannada spelling alone | see git log |
| 9 | 305–319 | 24 | 19 | 4 questions; p. 318 not in the supplied text | see git log |
| 10 | 320–334 | 16 | 14 | 2 questions; p. 324 not in the supplied text | see git log |
| 11 | 335–349 | 31 | 22 | 8 questions; p. 338 not in the supplied text | see git log |
| 12 | 360–367 | 18 | 11 | 7 questions; p. 366 not in the supplied text | see git log |
| 13 | 368–382 | 32 | 30 | 3 questions; p. 372 not in the supplied text; 3 rows restore misprints of the source's own English (libitations, yoyage, whily) — easy to drop | see git log |
| 14 | 383–397 | 18 | 18 | 0 questions; p. 390 not in the supplied text | see git log |
| 15 | 398–412 | 24 | 19 | 7 questions; p. 408 not in the supplied text | see git log |
| 16 | 413–427 | 14 | 12 | 3 questions; pp. 414, 422 not in the supplied text | see git log |
| 17 | 428–442 | 21 | 18 | 3 questions; pp. 434, 440 not in the supplied text | see git log |
| 18 | 443–457 | 22 | 20 | the agent hit the usage limit before its report: file complete to p. 457 and well-formed, but its list of unchecked pages is lost (pp. 458, 465, 466 are not in the supplied text) | see git log |
| 19 | 458–472 | 13 | 11 | 2 questions; p. 458 not in the supplied text (465–466: text found under neighbouring labels) | see git log |
| 20 | 473–487 | 22 | 15 | 7 questions (L8720 Pā. 6-3-67/62: two supplied places disagree, set to question by me); p. 484 not in the supplied text | see git log |
| 21 | 488–502 | 30 | 28 | 2 questions | see git log |
| 22 | 503–517 | 14 | 8 | 7 questions; pp. 506, 514 not in the supplied text | see git log |
| 23 | 518–532 | 29 | 28 | 1 question; p. 518 not in the supplied text (p. 530 blank) | see git log |
| 24 | 533–542 | 22 | 21 | 1 question (p. 539 non-word) | see git log |
| 25 | 543–553 | 60 | 54 | 6 questions; 14 reference numbers changed to the supplied ones | see git log |
| 26 | 554–564 | 45 | 41 | 4 questions | see git log |
| 27 | 565–575 | 56 | 48 | 8 questions | see git log |
| 28 | 576–586 | 50 | 46 | 4 questions | see git log |
