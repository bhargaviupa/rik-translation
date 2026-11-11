# Vol 18 — status

*Update this file at the end of every working session. It is the only place for volume-specific state; the general rules live in `CLAUDE.md`.*

## Scope
Not confirmed: to be read from the supplied text (title page, contents, first running heads, closing lines). Vol 17 covers Maṇḍala 3 Sūktas 40–62 and Maṇḍala 4 Sūktas 1–18 (Third Aṣṭaka, Adhyāyas 3–5), so Vol 18 is expected to continue Maṇḍala 4 from Sūkta 19; `volcfg.json` has `mandala` 4 and `mandalas` [4, 5] as a starting assumption only.

## Source and inputs
**Waiting for the user's machine-read text.** What was done for Vol 17, in this order (all mechanical, each recorded here when done):
1. Put the supplied file(s) in `vol18/html/`. Embedded pictures → `vol18/html/figures/figK_lineNNNNN.jpg` with `[figure: …]` lines in the text; the converter's `Pages: N/N` footer lines removed.
2. Several files → one: `python3 tools/rv/merge_md.py vol18/html/rig_18.md PART1.md PART2.md … --write` (refuses unless the page split is identical), then delete the parts.
3. `python3 tools/rv/html_pages.py vol18/html/rig_18.md`: how many printed pages are recognised, which numbers have no head. If printed p. 1 has no running head, insert one line `<!-- page 1 -->` before the first line of the body.
4. Find the volume's own preface (ಪೀಠಿಕೆ) in the front matter and note its line range: it is translated separately (`python3 tools/rv/api_front.py 18 FIRST LAST preface`, then `--install`), because no window covers the pages before printed p. 1.
5. Set `source` in `volcfg.json` to the real printed-page range (now a placeholder `rig_18.md@1-999`) and confirm scope and Maṇḍala from the text.

## Outputs
`vol18/Rigveda_Samhita_Vol18_English_Translation.md` and `…_Kannada_Text.md` (empty; progress note "Done through printed p. 0"). Cost log `vol18/parts/batch_costs.md`.

## How it will be made
Batch API route as for Vol 17 (`RIK_API_KEY`): `python3 tools/rv/api_batch.py plan 18 --windows K` (free: prepares windows, counts tokens, prints the estimate) → `submit 18` (spends money: only after the user has seen the estimate) → `status 18` → `collect 18`. Conventions carried over from Vol 17 in `volcfg.json`: Sonnet, 6-page windows, `**NOTE**` marks instead of remarks, no Kannada script in the English text, sub-heading layout, bhāṣya block in Devanagari only with a Gist that covers most of it, Pratipadārtha one word per line, printed English headed "English translation (H. H. Wilson)" (still to be confirmed by the user), grammar sections (if the volume has any) rendered in Sanskrit.

## Status
Set up only (Nov 11 2026). No text supplied, nothing translated, nothing sent.

## Open items
1. User: supply the machine-read text (and, later, the front-matter scan PDF for the print build).
2. Dispatcher: steps 1–5 above; then a free `plan` and the estimate to the user before anything is sent. Budget note: Vol 17 has cost about $0.027 per page so far including retries; the script fixes made during Vol 17 should lower that, to be measured on Vol 17's last stages.

## Publication (print PDF)
Not built.

## Pointers
`CLAUDE.md`, `vol17/STATUS.md` (what happened on the first batch-API volume), `tools/rv/BRIEF.md`, `tools/rv/api_batch.py`, `docs/LESSONS.md` 41–50.
