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
Nov 26 2026: **done through printed p. 551** (Sūkta 85 Ṛk 12 Saṃhitā; 30 agent batches of three windows; `batch.py audit 26` passes). Agent tokens: 4997550 (`parts/batch_costs.md`; batch 16 counted with both notices of a resumed agent, possibly too high). Stage check after batch 30 (by script): `check_labels.py 26` 1302 English blocks, 1302 Kannada blocks, 0 not matched, 0 under the label of another section; `## Sūkta` headings 44–85 all present in order, Sūkta 72 headed `Sūkta 22` (open item 5); each sūkta's Ṛk headings run 1…n (44–46: 6; 47–52: 5; 53–60: 4; 61–66: 30; 67: 32; 68–70: 10; 71–74: 9; 75–84: 5; 85: 12 so far) except the doubled `Ṛk 5` in Sūkta 78 (open item 6); no `## Maṇḍala` heading (the volume begins inside Maṇḍala 9, as Vol 21 inside Maṇḍala 6); Sūkta 60 Ṛk 2, Sūkta 67 Ṛk 25 and Sūkta 85 Ṛk 9 read through. 455 `**NOTE**` marks (455 rows in `review/notes.tsv`), 103 `**GLOSS**` marks. From batch 7 on agents copy damaged Pratipadārtha lemmas and damaged printed-English words as printed, each with a NOTE (most of the NOTEs).
Hand repairs: one remark removed in w0100 (`review/repair_log.md`). By agents with `batch.py fix`: page heads for pp. 43, 44/45, 75 added inside long pages (w0037, w0045, w0069; so the wrong renumbering of head `44` noted above is put right in the English), one avagraha join (w0063), one garbled Bhāvārtha label (w0137); w0045 also removed a `[figure: …]` line from its kn.md as a duplicate of a table (right by BRIEF.md; the dispatcher's instruction of batches 4–16 not to remove figure lines was wrong and stopped batch 16 once at an ornament on p. 279; withdrawn). Shared tool: `publish/tools/translit/kannada_to_deva.py` maps the candrabindu U+0C81 (LESSONS). Pages 105, 145, 155, 156 have no running head and stand under the heading of the page before (183 page headings for 187 pages).

## Open items
1. (user) Preface: to be translated into `vol26/work/preface/en.md`; installing it is a logged repair after the user's yes.
2. (user) w0107 (pp. 107–112): for four Pratipadārtha lemmas that the Kannada line prints damaged (`ದೇವನೀತೆಯೇ`, `ಪಿತ್ರಾವತೀ`, `ಅಂಜೃಃ`, `ಅತ್ಯಕ್ರಮಾತ್`) the agent wrote the Saṃhitā block's form without a NOTE (its own report); decide whether to keep them or restore the line's form with a NOTE.
3. (user) Second reading of the scan pages 810–894 (`review/repair_log.md`).
4. (user) w0206 (Sūkta 62 Ṛk 7): the NOTE on the Pratipadārtha word for `ಅಸದಃ` is worded wrongly (the agent's own report): the word cut off at the line end is the Kannada meaning `ಬಂದುಕುಳಿತುಕೊ`, not the lemma.
5. (user) The heading `## Sūkta 22 (Maṇḍala 9)` (p. 430, w0430) stands for Sūkta 72: the head line prints `ಸೂಕ್ತ-೨೨`, the announcement and the particulars line say 72; written by the rule "the head-line number decides", with a NOTE. At Sūkta 77 (p. 484, head line `ಸೂಕ್ತ-22`) the agent of batch 27 wrote `## Sūkta 77` with a NOTE, so the two cases differ. Say whether Sūkta 72's heading should read 72 too (a logged repair).
6. (dispatcher, finishing job) Sūkta 78, p. 496: two `#### Ṛk 5` headings. The supplied text's (Wikisource) bhāṣya of Ṛk 4 ends with the first line of Ṛk 5; the script gave that stray line a Saṃhitā label and a Ṛk heading, so Ṛk 4's Pratipadārtha, Bhāvārtha and English stand under the first `Ṛk 5`. To repair in both volume files together (the audit compares their Saṃhitā label counts).
7. (dispatcher, finishing job) w0594 (Sūkta 86, p. 594–600, Pratipadārtha): one lemma stands glued to its Kannada meaning inside the Sanskrit (`ಅರ್ಭರ್ಷಸಿಒದಗಿಸುತ್ತೀಯೆ`, with a NOTE); the agent says it did this for more than one lemma in batch 33 (pp. 588–606). To be split by a logged repair; agents add the missing dash with `batch.py fix` from batch 34 on.
8. (user) Sūktas 90–91, pp. 644–650 (w0644; the known gap of the supplied text): Sūkta 90 has Ṛk headings 1–4 and 6 only. After Ṛk 4's Pratipadārtha the supplied text lacks Ṛk 4's Bhāvārtha and printed English and all of Ṛk 5 (p. 645 has no running head and its text seems to be absent); there the adhyāya-4 opening and the Sūkta 91 introduction stand a first time (the agent wrote `## Sūkta 91` there), then Ṛk 6 of Sūkta 90 (pp. 646–647), the colophon of the third adhyāya (p. 648), and the opening and Sūkta 91 introduction a second time, followed by Sūkta 91 Ṛks 1–6. So in the English file Ṛk 6 of Sūkta 90 stands under the heading of Sūkta 91. All marked with NOTEs; to be put right when the missing page is supplied (heading moved, first copy of the introduction removed: logged repair in both volume files).

## Publication (print PDF)
Not built.

## Metrics (fill at the end of the volume; compare with the previous volume)
| windows | pages | hand-fixes by kind (merged heads / garbled labels / stray lines / hyphen joins / other-script letters) | gate failures | `[?]` | inline mismatches | accent lines unmatched | QA sample (pages, errors, minors) | agent tokens / cost |
|---|---|---|---|---|---|---|---|---|

## Lessons from this volume

## Pointers
`docs/prompts/VOL26_AGENT_PROMPT.md`, `vol26/html/_layout.json`, `vol26/review/repair_log.md`.
