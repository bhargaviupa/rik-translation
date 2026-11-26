# Vol 26 — status

*Update this file at the end of every working session. It is the only place for volume-specific state; the general rules live in `CLAUDE.md`.*

## Scope
Ṛgveda-saṃhitā Part 26: Aṣṭaka 7 adhyāyas 1–4 = Maṇḍala 9, Sūktas 44–100 (`"mandalas": [9]`), preceded by the introduction to the maṇḍala (ಮಂಡಲದ ಪೀಠಿಕೆ, on Soma; printed pp. 1–98). Read from the supplied text: first sūkta announcement "ನಲವತ್ತನಾಲ್ಕನೆಯ ಸೂಕ್ತವು" (file line 4753), last sūkta head line `ಸೂಕ್ತ—೯೮`, the text ends with Ṛk 9 of 9.100, the colophon of the fourth adhyāya and "ಶುಭಂ ಭೂಯಾತ್" on p. 894. Printed pp. 1–894. Branch `claude/epic-curie-xg7s3d`. Two sūkta head lines are damaged (`೨೨`, `22` where 72 and 77 are expected): the head-line number decides, with a NOTE.

## Source and inputs
`vol26/html/rig_26.md` (compiled and verified by another session, Nov 25 2026; not changed here), as `vol26/html/_layout.json` records:
- pp. 1–377 (front matter, preface, contents and body to p. 377): the user's machine-read file `rig_26_1.md`;
- pp. 378–808: the user's machine-read file `rig_26_2.md`;
- pp. 810–894 (end of Sūkta 9.97, 9.98–9.100): scan transcription with Saṃhitā, Pada and Sāyaṇa blocks from the Wikisource index (`rig_26_part2.filled.md`); these pages carry `[?]` marks from the scan reading (132 in the file);
- Saṃhitā/Pada/Sāyaṇa blocks of pp. 99–808 (Sūktas 9.44–9.97 start) replaced from Wikisource (`review/ws_fill_log.tsv`); Sūktas 9.90, 9.91, 9.96, 9.97 keep the machine-read blocks; pp. 1–98 have the Sanskrit as the machine read it. The original machine-read form is `rig_26.machine_read.md`.
Front matter (no window covers it): preface file lines 1–542 (begins at its page 20; the pages before are not in the supplied text), contents lines 543–724 (not translated), body from line 728 (`<!-- page 1 -->`). Pictures: `vol26/html/figures/` (105; the first two are the title page and cover).

`html_pages.py`: 873 pages, printed 1–894. Printed pages without a running head (lesson 67, not chased): 43, 44, 75, 105, 145, 155, 156, 280, 351, 471, 477, 595, 617, 645, 649, 657, 729, 750, 781, 809, 812. Heads corrected by the offset rule: line 28060 (`795`→775), line 29061 (`300`→800). **Two heads are renumbered wrongly by the offset rule**: line 2465 (head `44`, used as 45) and line 6816 (head `೧೫೬`, used as 157): the heads really missing are 43 and 45, and 155 and 157, so the English headings "Printed p. 42 / 45" and "154 / 157" each hold two printed pages and the page break inside them is one page off. Not repaired (shared tool; no text is lost). The label anomaly at p. 496 (Wikisource bhāṣya ending with the first line of Ṛk 5 of 9.78) is not a fault.

## Outputs
`vol26/Rigveda_Samhita_Vol26_English_Translation.md`, `…_Kannada_Text.md`; `review/notes.tsv`; cost log `parts/batch_costs.md`. No PDFs in this session.

## How it is made
By Sonnet agents, one per batch of three windows of 6 pages, no Batch API (`docs/prompts/VOL26_AGENT_PROMPT.md`). Conventions in `volcfg.json` as Vol 21.

## Status
Nov 25 2026: prepared; `batch.py audit 26` passes at "Done through printed p. 0". No window translated yet.

## Open items
1. (user) Preface: to be translated into `vol26/work/preface/en.md`; installing it is a logged repair after the user's yes.
2. (user) w0107 (pp. 107–112): for four Pratipadārtha lemmas that the Kannada line prints damaged (`ದೇವನೀತೆಯೇ`, `ಪಿತ್ರಾವತೀ`, `ಅಂಜೃಃ`, `ಅತ್ಯಕ್ರಮಾತ್`) the agent wrote the Saṃhitā block's form without a NOTE (its own report); decide whether to keep them or restore the line's form with a NOTE.
3. (user) Second reading of the scan pages 810–894 (`review/repair_log.md`).

## Publication (print PDF)
Not built.

## Metrics (fill at the end of the volume; compare with the previous volume)
| windows | pages | hand-fixes by kind (merged heads / garbled labels / stray lines / hyphen joins / other-script letters) | gate failures | `[?]` | inline mismatches | accent lines unmatched | QA sample (pages, errors, minors) | agent tokens / cost |
|---|---|---|---|---|---|---|---|---|

## Lessons from this volume

## Pointers
`docs/prompts/VOL26_AGENT_PROMPT.md`, `vol26/html/_layout.json`, `vol26/review/repair_log.md`.
