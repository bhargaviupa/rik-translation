# Vol 17 — status

*Update this file at the end of every working session. It is the only place for volume-specific state; the general rules live in `CLAUDE.md`.*

## Scope
Maṇḍala 3 Sūktas 40–62 (to the end of Maṇḍala 3) and the beginning of Maṇḍala 4 (Sūktas 1–17 or 18: confirm against the contents when translated), Third Aṣṭaka, Adhyāyas 3–5; printed pp. 1–1007 (final colophon and closing lines on p. 1007). Read from the supplied text (sūkta heading lines, contents, closing lines), not yet checked against a scan.

## Source and inputs
`vol17/html/rig_17.md`: the user's three files (`rig_17_1.md` front matter + pp. 1–326, `rig_17_2.md` pp. 327–676, `rig_17_3.md` pp. 677–1007; supplied Nov 11 2026) merged losslessly with `tools/rv/merge_md.py` (915 page splits identical before and after). Changes made to the supplied text, all mechanical: the 93 embedded pictures were extracted to `vol17/html/figures/` (`figK_lineNNNNN.jpg`, K = part, NNNNN = line in that part) and replaced by `[figure: …]` lines; the converter's three `Pages: N/N` footer lines were removed; **one line `<!-- page 1 -->` was inserted before the opening "ॐ" of the body** (printed p. 1 prints no running head; front matter = lines 1–843: title, contents, list of abbreviations). The page splitter finds 976 of the 1007 printed pages (31 numbers have no head of their own: pages that print no number, or heads the splitter cannot read; the translator marks them). `volcfg.json`: `source` = `rig_17.md@1-1007`, window 6, `mandalas` [3, 4]. No scans, no numeral file. Front-matter scan PDF: not supplied yet (needed only for the print build).

## Outputs
`vol17/Rigveda_Samhita_Vol17_English_Translation.md` and `…_Kannada_Text.md` (empty; progress note "Done through printed p. 1"). Cost log `vol17/parts/batch_costs.md`.

## How it was made
Planned as the **pilot of the Batch API flow** (user decision, Nov 11 2026; API key `RIK_API_KEY`, budget $66): `python3 tools/rv/api_batch.py plan 17 --windows 5` (free: prepares windows, counts tokens, prints the estimate) → `submit 17` (spends money) → `status 17` → `collect 17` (writes each window's `en.md`, logs real cost, runs the gates and commits in page order). Model `claude-sonnet-5-5`, 6-page windows. Nothing has been sent yet. **Conventions decided by the user on Nov 11 2026 for this volume:** Sonnet only; no translator remarks in the English text, one mark `**NOTE**` for every place that needs a decision or a second look, with the question in `review/notes.tsv` (`[?]` and `[sic]` are no longer used; `"note_style": "NOTE"` in `volcfg.json`). No Kannada script in the English text; reference abbreviations in Latin letters. Pratipadārtha: one word per line. Sāyaṇa-bhāṣya block in Devanagari only, followed by a Gist that covers most of the block in English (ritual use, glosses, alternatives, authorities; not the grammatical tail). **Grammar section rendered from the Kannada into Sanskrit** (Devanagari only, one word per line; composed by the translator, so not checkable by the gates: the editor's reading is the check).

## Status
Text prepared, windows planned (Nov 11 2026); **nothing sent to the API, nothing translated: waiting for the user's "start"**. Free plan of the first 5 windows (pp. 1–32): 107k input tokens, about 3,460 per page.

## Open items
0. **To confirm before printing:** the English printed under each verse is headed "English translation (H. H. Wilson)" (`printed_english_label` in `volcfg.json`; one line to change). The edition does not name the translator (Vol 1's plan of the work says only that the main sense is given briefly under "English Translation"); the attribution rests on the edition quoting Wilson's notes on the English and treating Max Müller as a separate opinion, on the style, and on the user's judgement (Nov 11 2026). Not yet compared word for word with Wilson's published text (the site was not reachable from the session).
1. User: say "start" for the pilot; later the front-matter scan PDF for the print build.
2. Dispatcher: confirm scope and Maṇḍala from the text; run the pilot (5 windows), report measured cost per page and gate results before sending more; QA sample of the pilot pages against the Kannada.

## Publication (print PDF)
Not built.

## Pointers
`CLAUDE.md`, `tools/rv/BRIEF.md`, `tools/rv/api_batch.py` (docstring), `docs/LESSONS.md` 31–40.
