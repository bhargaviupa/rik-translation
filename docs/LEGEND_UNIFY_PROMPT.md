# Prompt for the legend session: ONE set of reference abbreviations in every volume (user, Nov 19 2026)

Task: make every volume use ONE set of reference abbreviations, in its printed legend and in its text. Change the volume files, by script, and prove nothing else changed.

Read first: CLAUDE.md (rules 2, 3, 5, 7 and "References, uniform in all volumes"), rv/legends_by_volume_README.md, rv/legends_by_volume.tsv, docs/REFERENCES.md, .claude/agents/reference-corrector.md, tools/rv/refs_apply.py (docstring), REFERENCES_THREE_SCRIPTS.tsv.

## Situation
- The one list is `rv/references.tsv`: `legend` rows (the edition's 32 entries), `extra` rows (works the volumes cite that no legend explains, about 30), `mistake` rows (decided misreadings → the form to use). The reference-corrector already makes the NAMES before reference numbers uniform in the English, Devanagari and Kannada text of Vols 1–18 (numbers are never touched).
- Still not uniform: the LEGEND ("ಸಂಕೇತಾಕ್ಷರಗಳ ವಿವರಣೆಯು") that the Kannada volumes print in their front matter. `rv/legends_by_volume.tsv` records what 14 volumes print (Vols 2, 3, 5, 6, 9, 10, 12, 13, 15, 16, 17, 18, 19, 20; read by eye at 150 dpi from one page each). Vol 1's supplied text has a legend too (vol1/html/rig_1_1.md, "xx", about line 987; its English file has a "Key to Abbreviations" table at "Page xx") — it was not among the pages read: read it from the text.
- **Vols 4, 7, 8, 11 and 14 print no legend** (the user, Nov 19 2026). Vols 4, 7, 8 are scan-based and have no Kannada text file; Vols 11 and 14 have supplied text without the heading.
- Every legend explains only the 32 entries, while the volumes cite many more works.

## Decided by the user (Nov 19 2026)
1. **Where the print has variants, the more complete form wins.** So:
   - Jai. Sū. → **ಜೈ. ಪೂ. ಸೂ. (Jai. Pū. Sū.)**: Vols 9, 10, 12, 13, 15, 17, 19 print it; Vols 2, 3, 5, 6, 16, 18, 20 print only ಜೈ. ಸೂ. The list row "Jai. Sū." / "ಜೈ. ಸೂ." is to become "Jai. Pū. Sū." / "ಜೈ. ಪೂ. ಸೂ." and "Jai. Sū." / "ಜೈ. ಸೂ." a decided mistake that reads as the fuller form (and the lower-case/Devanagari twins likewise).
   - Ā. Sū. → "ಆ. ಸೂ. ಅಥವಾ ಆ." (the list's "Ā. Sū. or Ā." already has it; Vols 2 and 5 print only ಆ. ಸೂ.).
   - Phi. Sū. → "ಫಿ. ಅಥವಾ ಫಿ. ಸೂ." (Phi. or Phi. Sū.); Vols 2 and 5 print only ಫಿ. ಸೂ.
   - Atharvaveda → "ಅಥ. ಸಂ. ಅಥವಾ ಅ. ವೇ." (Ath. Saṃ. or A. Ve.), as Vol 5 prints it: one work, two accepted forms, no longer two rows that look like two works.
2. The same one legend is printed in EVERY volume, including the five that have none.

## Goal
1. Define the single set: the `legend` and `extra` rows of rv/references.tsv after the decisions above, one entry per work, with English, Devanagari and Kannada forms (Devanagari made by script from the English, never typed).
2. Replace the legend of every volume that has one (Kannada text, English file, and what the print build uses: rv/printer.py `abbreviations_html`, publish/volbook.py) by that one legend, generated from the list, in the same order everywhere; ADD it to the five volumes that have none, where the others have it (front matter, before the first maṇḍala).
3. Make the abbreviations in the text agree with it: run the reference-corrector (tools/rv/refs_apply.py), English, Devanagari and Kannada, after the list is final (the Jai. Pū. Sū. change above makes it a bigger run: preview first).

## Stop and ask the user BEFORE writing, with the exact numbers
- The Kannada form of each `extra` row: several are guesses of mine from the English or Devanagari (for example ಕಾ., ಅನು., ಧಾ., ಪಿಂ., ಬೃ. ದೇ.). List them for confirmation.
- Whether each volume's legend shows all works or only the works that volume cites; and the order (the edition's alphabetical Kannada order, with the extra rows merged in).
- Where to put the legend in the five volumes that have none.
- Vol 12's legend is printed in another type without dots and has probable misprints (Pā. Sū., Pā. Śi., Ma. Bhā.): it is replaced anyway; list the places in Vol 12's Kannada text where those three works are cited, so the corrector's result there can be checked.

## How (rules)
- One shared tool, not a script per volume (rule 7): for example tools/rv/legend_apply.py, preview first (a table of what it would replace or add in each file), then `--write` per volume. The user approves the preview.
- The supplied text is the base (rule 2): for the html volumes the legend block is replaced or added through a data fixes file read at every run (like volN/data/source_fixes.tsv and import_fixes.json), not by editing volN/html/. Scan-based volumes: edit the volume file and log it.
- Proof built in for every volume written: apart from the legend block and the names before reference numbers, every line, digit and Sanskrit letter of the Kannada and English files is as before; no line added or lost outside the block. The script refuses otherwise.
- Every change is a row of volN/review/refs_applied.tsv or a line of volN/review/repair_log.md. Commit and push after each volume. Do not force-push; do not merge to main unless the user asks.
- Update PUBLICATION_TODO.md (the legend step per volume), rv/legends_by_volume_README.md and docs/LESSONS.md when done. Print counts before and after: legends replaced, legends added, names changed, volumes untouched.

Report to the user: what was changed per volume (counts), what the proof showed, the questions that remain.
