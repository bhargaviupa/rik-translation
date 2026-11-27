# Vol 10 second pass — status report
*Made by `python3 tools/rv/sp_report.py 10` from `findings.tsv`, `questions.tsv`, `batches.tsv`, `open.tsv`; updated 2026-11-27. Format: `docs/SECOND_PASS_REPORT.md`.*

## 1. State
- **Stage:** S2 reading in page batches
- **Pages read:** 160 (300–309, 2–31, 32–61, 62–91, 92–121, 122–151)
- **Findings:** 304 — applied 253, kept/not applied 51 (English kept: misprints and doubts settled by rule; see part 5); edits ok 272, failed 0
- **Reader tokens (batches so far):** 1317k; per page 8.2k
- **Last commit:** (this commit)

## 2. Batches
| Batch | Pages | Findings | Applied | Edits ok / failed | Kept / not applied | Tokens | Commit | Note |
|---|---|---|---|---|---|---|---|---|
| 1 | 300–309 | 35 | 30 | 38 / 0 | 5 | 180k | e889856a | pilot; 27 [?] seen, 22 resolved from the Kannada, 5 kept (inside our remarks) |
| 2 | 2–31 | 24 | 14 | 17 / 0 | 10 | 157k | 1119c0fb | pp. 2-3 read in full; pp. 4-31 script-assisted (numbers, refs, all 19 [?]) not read as prose: re-read later; 19 [?] seen, 6 removed, 13 kept |
| 3 | 32–61 | 96 | 87 | 87 / 0 | 9 | 251k | c53f4019 | all pages read; 68 of 87 edits add sutra numbers the Kannada prints; 17 [?] seen, 0 removed (Kannada non-words), 17 kept |
| 4 | 62–91 | 77 | 72 | 72 / 0 | 5 | 224k | 9d18ba97 | all pages read; 41 edits add sutra numbers; 8 [?] seen, 5 removed, 3 kept (in remarks) |
| 5 | 92–121 | 43 | 30 | 34 / 0 | 13 | 268k | 3ef7390f | all pages read; 15 [?] seen, 8 removed, 7 kept |
| 6 | 122–151 | 29 | 20 | 24 / 0 | 9 | 237k | (this commit) | all pages read; 15 [?] seen, 8 removed, 7 kept |

## 3. Findings by kind
| Kind | Applied | Kept / not applied | Total |
|---|---|---|---|
| S3 | 116 | 1 | 117 |
| Q2 | 3 | 34 | 37 |
| S1 | 32 | 0 | 32 |
| S13 | 24 | 4 | 28 |
| S2 | 24 | 3 | 27 |
| Q1 | 26 | 0 | 26 |
| S14 | 18 | 2 | 20 |
| H29 | 0 | 5 | 5 |
| S7 | 5 | 0 | 5 |
| S16 | 4 | 0 | 4 |
| S18 | 0 | 2 | 2 |
| S15 | 1 | 0 | 1 |

By reader: R1 283, R3 18, R6 3

## 4. Open items (not findings)
- **other** (pages 307): running head Varga printed ವ. ೧೭ (neighbouring heads ವ. ೧೩); applied as printed (Varga 17)
- **other** (pages 29): Ghoṣā sūktas printed ೨೯-೪೦ ಮತ್ತು ೪೧ನೇ; applied as printed
- **other** (pages 37): grammar sūtra number printed ೨-೪-೨೨೬ (juhotyādibhyaḥ śluḥ; Aṣṭādhyāyī 2-4 has fewer sūtras); applied as printed
- **other** (pages 78): Pā. Sū. printed ೩-೧-೫-೩ (four figures); applied as printed

## 5. Questions for the editor
**0 open questions** in `questions.tsv` (the editor decides only what the rules cannot: nothing else is asked).

Settled by rule, no reading needed: 55 Kannada misprints where the English is kept (`kn_misprints.tsv`); 21 places where the English is kept unchanged and listed for the scholar sample (`decided_by_default.tsv`). Impossible or odd printed numbers applied as printed are in part 4.

## 6. Files
`vol10/review/second_pass/findings.tsv` · `questions.tsv` · `batches.tsv` · `open.tsv` · `edits/` (edit files and results) · `../repair_log.md` (every English repair, heading "second pass") · `../../data/source_fixes.tsv` (edits of the supplied Kannada)

## 7. Next
the next page batch; then S3 totals (re-run the S0 checks), S4 coverage, S5 pictures, S6 records
