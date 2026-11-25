# Vol 25 — status

*Update at the end of every working session. Rules: `CLAUDE.md`. Route: agents (Sonnet, three windows per agent), `docs/prompts/VOL24_AGENT_PROMPT.md` loop.*

## Scope
Ṛgveda-saṃhitā Part 25: Aṣṭaka 6 adhyāyas 5–7 (from the opening page "ಅಥ ಷಷ್ಠಾಷ್ಟಕೇ ಪಂಚಮೋಽಧ್ಯಾಯಃ") = Maṇḍala 8 Sūkta 68 to Maṇḍala 9 Sūkta 43 (79 sūktas; the end is read from the last running head: the contents page, PDF 1–12, is not transcribed). Printed pp. 1–877 (printed = PDF page − 12). `"mandalas": [8, 9]`. Branch `claude/cool-cannon-y26h5a`.

## Source and inputs
No machine-read text exists. Kannada text transcribed from the scans by Sonnet agents (other session, branch `claude/wonderful-bardeen-h655ql`, merged to `main`), PDF 13–889, with the Saṃhitā, Pada and Sāyaṇa-bhāṣya blocks skipped; assembled by `tools/rv/scan_assemble.py` into `vol25/html/rig_25.md` (844 pages; printed 1–877; 33 printed numbers have no page of their own, see `html_pages.py`; 980 `[?]` marks; running-head anomalies: p. 293 read for 298, 339 for 338, a head read 466 where 97 belongs). The three Sanskrit layers were filled by `tools/rv/ws_fill.py 25 --write` from the Wikisource index (Nov 25 2026): **72 of 79 sūktas filled**; not filled (counts disagree, report `review/ws_fill_report.tsv`): 8.70, 8.76, 8.86, 8.93, 8.96, 9.5, 9.41 (user, Nov 25: leave for now). The wiki's “ " pratīka marks were dropped from the bhāṣya. The scan transcription's numerals are not known to be correct: every `[?]` is a question for the user, not settled from memory.

## Plan
`volcfg.json` `source` ends at printed p. 42, a window boundary before the first unfilled sūkta (8.70, header on p. 45). Extend `source` (a logged change) only through filled text. Preface and contents (PDF 1–12) are not transcribed: not translated.

## Status
Done through printed p. 0 (nothing translated yet).

## Open items
1. (user) the 7 unfilled sūktas (see above).
2. (user) 980 `[?]` marks in the transcription (to be listed in `review/questions.tsv`).
3. (user) the end of the volume (9.43?) and the preface/contents transcription.
4. Finishing checklist not started.
