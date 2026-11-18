# Vol 2 — status

*Moved out of the general CLAUDE.md on Nov 8 2026. Update this file (not CLAUDE.md) whenever the state of this volume changes.*

## Scope
Maṇḍala 1 Sūktas 3–19 (First Adhyāya of the First Aṣṭaka).

## Source and inputs
Old single-file scan (printed = PDF − 15); better scans in `vol2/scans/` have their own page maps (see `vol2/vol2_runbook.md`).

## Supplied machine-read text (user, Nov 18 2026)
`vol2/html/rig_2_2.md`: printed pp. 386–808 (Maṇḍala 1 Sūktas 10–19; 416 pages found), no pictures. **The first half (pp. 1–385) is not here yet:** the file uploaded as `rig_2_1.md` is from another volume (running heads: Maṇḍala 6 Sūkta 59 to Maṇḍala 7 Sūkta 19, pp. 389–841) and was not put in the repository.

## Outputs
`vol2/Rigveda_Samhita_Vol2_English_Translation.md` (+ docx/pdf).

## How it was made
Scan-based legacy workflow. A numeral/`[?]`/accent pass was agreed (user, Oct 27 2026; `vol2/vol2_runbook.md`, review files in `vol2/review/`).

## Status
Translated. The file is closed except for that agreed pass.

**Nov 17 2026: opened for the clean-up pass agreed with the user** (remove our remarks, verify accents; no re-translation). Prompt: `vol2/CLEANUP_PROMPT.md`; proposal: `vol2/review/cleanup_proposal.md` (Step A1 and A2 done for the agreed kinds); every change goes to `vol2/review/repair_log.md`.

## Open items
Old mid-file progress notes and a stray Cyrillic string in the file; varga numerals unreconciled with colophons; expert review wanted; `[?]` (see Vol 1).

## Publication (print PDF)
Built with `publish/build_vol2.py` + `vol2_clean.py`; `publish/out/vol2_full.pdf` (and `.html`).

## Pointers
`vol2/README.md`, `vol2/vol2_runbook.md`, `docs/HISTORY.md`.

## Clean-up of Nov 17 2026 (result)
Removed (logged in `review/removed_remarks.tsv`): old progress notes and closing block (replaced by one trailing progress note); 156 whole process notes; process sentences in 68 mixed notes; 121 "mine and tentative" remarks (glosses kept); 146 `[as printed]` tags; 42 `[accent ?]` tags on verified verses. Kept by the user's decision: `[?]` (429: lists in `review/open_readings.tsv`, `review/refs_marked.tsv`), `[sic]` (143). Later the same day (user): first-person notes removed (73 notes) and all `[as printed…]` brackets without Sanskrit removed (81 places; 22 with Sanskrit or `[sic]` stay). Left by the user's wish: the 23 "tentative" mentions (to be reviewed), `[?]` 413, `[sic]` 142; reading notes without first person stay.
Accents: 176 Ṛks of Sū. 3–19 = 176 in the reference; before: 83 equal, 50 accent differences, 43 letter differences (37 only anusvāra/nasal/final-m style); after: all 176 equal to the reference (93 replaced, `review/verse_corrections.tsv`). Pada-pāṭha: 349 lines, none accented. Verses quoted in the commentary: 3 lines with accents (lines 909, 919, 17362 of the old numbering), unchanged. Tools: `tools/rv/cleanup_remarks.py`, `publish/tools/accents/accent_compare.py`, `accent_replace.py`.
