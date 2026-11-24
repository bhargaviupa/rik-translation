# Vol 5 — status

*Moved out of the general CLAUDE.md on Nov 8 2026. Update this file (not CLAUDE.md) whenever the state of this volume changes.*

## Scope
Maṇḍala 1 Sūktas 47–61 (Fourth Adhyāya) and the Kannada Pariśiṣṭa on the deities and persons of the Ṛgveda (printed pp. 531–708, translated at the user's request).

## Source and inputs
Scan `vol5/scans/Rig_Vol5.pdf` (724 pp.; printed = PDF − 16). Machine-read text in `vol5/html/` (user, Nov 17 2026; replaces the two files of the repair pilot, `rig_5_1.html` and the old `rig_5_2.md`, which read the same pages: median likeness of the Kannada letters per page 99.45 %): `rig_5_1.md` (front matter and printed pp. 2–83), `rig_5_2.md` (pp. 85–184; no head for 131, 154, 180), `rig_5_3.md` (pp. 185–286; no head for 193, 232, 233, 260), `rig_5_6.md` (pp. 486–584; no head for 506, 514, 518, 530, 542, 559, 566, 578). `rig_5_45.md` (pp. 273–468, supplied later the same day; **pp. 273–286 stand in both file 3 and this file**: which copy is used is decided when the volume is prepared). `rig_5_7.md` (pp. 584–708, the end of the volume with the printer's line; supplied Nov 19 2026; p. 584 stands in both file 6 and this file). `rig_5_5.md` (pp. 468–485; supplied Nov 19 2026). **The supplied text now covers the whole volume, pp. 2–708** (672 page heads found; 36 numbers have no head of their own, lesson 67; pp. 273–286 and 584 stand in two files). Page numbers without a running head are first pages of a sūkta or section (lesson 67) and are not listed for this file. The 32 embedded pictures were moved to `vol5/html/figures/` by `tools/rv/extract_figures.py` (which now also reads pandoc's `<img src="data:…">` form); nothing else was changed. Page 84 has no head of its own (the last head of file 1 reads 84 and is taken as 83 by the splitter: to be looked at).

## Outputs
`vol5/Rigveda_Samhita_Vol5_English_Translation.md` (+ docx/pdf).

## How it was made
Scan-based legacy workflow.

## Status
Translated and complete including the Pariśiṣṭa (printed pp. 1–529 and 531–708; p. 530 blank).

## Open items
Repair pilot: `[?]` in printed pp. 1–184 repaired against the supplied text (`vol5/review/html_repair_log.tsv`, tools `tools/rv/repair_worksheet.py`, `compare_html_scan.py`); the user judges disagreements. Vol 5 tests (`vol5/review/exp15`, `exp40`) are the basis of the decision to use the supplied text as base from Vol 15 on.

## Publication (print PDF)
Built with `build_vol45.py 5 full`; `publish/out/vol5_full.pdf`.

## Pointers
`vol5/README.md`.

- **Nov 18 2026, glosses (T12):** 25 more labelled glosses replaced by the marker `**GLOSS**` (91 markers in the volume now; removed text in `review/glosses_removed.tsv`, 18 labelled lines left in `review/glosses_left.tsv`); see `review/repair_log.md`. Unlabelled glosses not yet looked for. No final copy while a marker remains (D9).

## Second pass (Nov 24 2026)
Made in one session by shared tools (`tools/rv/second_pass_sieve.py`, `second_pass_page.py`, `second_pass_apply.py`, `second_pass_merge.sh`, `prose_kn.py --vol`, `figures_sheet.py`); records in `vol5/review/second_pass/` (`sieve.md` before, `STATUS_REPORT.md` per batch, `findings.tsv`, `questions.tsv`, `ws_coverage.tsv`, `reader_prompt.md`, `batches.tsv`).
- **S1:** `vol5/Rigveda_Samhita_Vol5_Kannada_Text.md` from the supplied files (pp. 273–286 from file 3, p. 584 from file 7); `vol5/data/source_fixes.tsv` is empty: no supplied text was edited.
- **S2/S3:** all supplied pages 2–708 read once, in 52 batches of 10–18 pages by fresh Sonnet readers (the pilot: pp. 350–359). 1 625 findings; 1 420 repairs applied to the English (each a line of `review/repair_log.md`, text-exact, one place at a time), 205 left as questions (`review/second_pass/questions.tsv`).
- **Before / after (sieve):** references only in the English 923 → 665 tokens (486 → 416 pages); plain numbers only in the English 400 → 380; `[?]` 228 → 109; `[sic]` 64 → 62; `**GLOSS**` 91 unchanged; Devanagari quotations not found 16 → 15. The rest of the "only in the English" count is mostly notation (I-32-6 / 1.32.6, page cites, front matter) that the sieve cannot tell from errors.
- **Not read (no supplied text):** pp. 232–233, 260, 290, 318, 324, 338, 366, 372, 390, 408, 414, 422, 434, 440, 458, 484, 506, 514, 518, 604; p. 180 and p. 84 (empty or inside neighbours); the English of those pages (older scan) is unchecked. Pages without a head whose text stands inside the neighbour page were read there.
- **The user's readings for pp. 578–625** (`archive/vol5/review/pending_doubts_p578-625_user_readings.txt`): all five readings already stand in the English (from the supplied text); nothing to apply.
- **S4:** `ws_coverage.tsv`: 152 Ṛks of Sūktas 47–61, each with Saṃhitā, Pada and bhāṣya in the Wikisource index, none missing, none twice; the English has all 152.
- **S5:** `review/Vol5_pictures.pdf`: 30 pictures in the supplied text (pp. 87–515, all in the Ṛk part), none transcribed; the first supplied file holds no picture (no "cover pictures" there).
- **Open:** the 205 questions; the p. 354 Pratipadārtha (4 lines of Kannada wholly missing from the English: row marked NOT APPLIED); the legacy remarks and glosses are unchanged; one reader (batch 18) lost its report to the usage limit; kind/reader columns of `findings.tsv` mix R-codes and H-codes between batches; "hail" for ಸಿಡಿಲು (thunderbolt) is rendered inconsistently; Sanskrit forms written in IAST/Devanagari by the readers from the Kannada should be spot-checked.
