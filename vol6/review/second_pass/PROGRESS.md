# Vol 6 second pass — progress record (for the editor to review)

Kept by the dispatcher after every batch. Findings: `findings.tsv`; questions for you: `questions.tsv`; every English repair: `../repair_log.md` (heading "second pass"); Kannada source edits: `../../data/source_fixes.tsv`; edit files and their results: `edits/`.
Method: one fresh Sonnet reader per batch of about 30 printed pages (brief `tools/rv/SECOND_PASS_BRIEF.md`), repairs applied by `tools/rv/sp_apply.py` (exact-once, logged); numbers and references from the supplied Kannada text (your decision of Nov 24); text places only where the Kannada decides, else a question. Before the batches: 28 anchored number corrections and the reference names by the one list (commit 849b2fe).

| Batch | Pages | Rows | Applied (edits ok / failed) | Questions | Reader tokens | Commit | Note |
|---|---|---|---|---|---|---|---|
| pilot | 300–309 | 24 | 15 rows → 17 edits ok / 0 | 9 | 139k + 109k (apply) | b7ae9b6 | |
| 2-31 | 2-31 | 86 | 35 rows → 43 edits ok / 0 not applied | 51 | 304k | @COMMIT@ | mostly H29 questions: misprints in the Kannada that the English had silently corrected; pp. 7–8 are one English section (edits for p. 7 filed under page 6) |
