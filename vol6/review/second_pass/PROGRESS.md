# Vol 6 second pass — progress record (for the editor to review)

Kept by the dispatcher after every batch. Findings: `findings.tsv`; questions for you: `questions.tsv`; every English repair: `../repair_log.md` (heading "second pass"); Kannada source edits: `../../data/source_fixes.tsv`; edit files and their results: `edits/`.
Method: one fresh Sonnet reader per batch of about 30 printed pages (brief `tools/rv/SECOND_PASS_BRIEF.md`), repairs applied by `tools/rv/sp_apply.py` (exact-once, logged); numbers and references from the supplied Kannada text (your decision of Nov 24); text places only where the Kannada decides, else a question. Before the batches: 28 anchored number corrections and the reference names by the one list (commit 849b2fe).

| Batch | Pages | Rows | Applied (edits ok / failed) | Questions | Reader tokens | Commit | Note |
|---|---|---|---|---|---|---|---|
| pilot | 300–309 | 24 | 15 rows → 17 edits ok / 0 | 9 | 139k + 109k (apply) | b7ae9b6 | |
| 2-31 | 2-31 | 86 | 35 rows → 43 edits ok / 0 not applied | 51 | 304k | 2a611eb | mostly H29 questions: misprints in the Kannada that the English had silently corrected; pp. 7–8 are one English section (edits for p. 7 filed under page 6) |
| 32-61 | 32-61 | 44 | 37 rows → 37 edits ok / 0 not applied | 7 | 208k | fed3619 | 24 S2: sūtra numbers the English had and the Kannada does not print were removed (no number where the print has none); 7 H29 questions |
| 62-91 | 62-91 | 76 | 55 rows → 55 edits ok / 0 not applied | 21 | 311k | 96960c4 | 30 S2 (numbers not in the print removed); p. 66 text is inside the p. 65 block in the Kannada book (marker fix open); English p. 72/73 boundary shifted by about a paragraph |
| 92-121 | 92-121 | 50 | 35 rows → 34 edits ok / 1 not applied | 15 | 204k | 26ecee4 | 22 S2 (numbers not in the print removed). One edit (p. 95, Ā. 7-7→7-3) failed because the English has two '### Page 95' headings: sp_apply.py now searches every section of a page; the edit was applied afterwards (35 of 35 ok); the findings row of p. 95 still says question |
