# Reference: the gloss session of Nov 18–20 2026 (for BHR)

*A record of what this session did and what it left open. It can be deleted once the points under "Still open" are settled or copied to `PUBLICATION_TODO.md` (T12), where they already stand.*

## Why this work exists
The Kannada edition quotes Ṛks and passages from elsewhere without a Kannada meaning. The translation added its own English glosses, many incomplete. Decision of Nov 17 2026 (requirement B3.5, gate D9): a quoted Ṛk is to be glossed later with **our own edition's translation of that Ṛk**, by script; until then the marker `**GLOSS**` stands in its place, and no final copy is printed while a marker remains. The table Maṇḍala–Sūkta–Ṛk → English is **not** built (user: not now).

The session followed `docs/GLOSS_PROMPT.md`.

## What was done

### Step 1: labelled glosses replaced by the marker (done for Vols 3–8, 10, 14, 16)
277 further glosses were replaced whole (label, quotation marks, text). Nothing else on a line changed; Devanagari, transliteration and references were not touched.

| Vol | replaced today | markers now | labelled lines left |
|---|---|---|---|
| 3 | 12 | 35 | 13 |
| 4 | 49 | 82 | 31 |
| 5 | 25 | 91 | 18 |
| 6 | 67 | 115 | 17 |
| 7 | 39 | 248 | 2 |
| 8 | 71 | 214 | 22 |
| 10 | 2 | 2 | 5 |
| 14 | 3 | 3 | 2 |
| 16 | 9 | 9 | 2 |

- 248 were replaced by the shared script `tools/rv/gloss_marker.py` and 29 single odd lines by its new `--list` mode.
- Vol 2: its marker count (160) is from the Nov 17 run; 18 further glosses would match the script, but they were **not** replaced, because the Vol 2 clean-up session's branch was still active.
- Vols 1, 9, 11, 12, 13, 15, 17, 18: nothing replaceable by form.
- Vol 19 (in translation elsewhere) was not touched.

**Changes to `tools/rv/gloss_marker.py`** (no per-volume tool):
- New forms, tried after the old ones: `parenx` (a whole parenthesis holding label and quotation, also numbered lists and glosses in single quotation marks), `inline` (label and quotation inside a longer remark or after a dash), `aftercap` (`"…" (Mine, tentative.)`).
- A line starting `**Translation**` is skipped: it is our translation of the bhāṣya's sūkta introduction, not a gloss of a quotation.
- `--list FILE.tsv [--write]`: columns vol, line, exact text, optional replacement. The text is replaced only when it stands exactly once in its line; otherwise the row is refused. It is also the tool for step 2.
- The "left" report no longer counts lines that already carry a marker.

**Where the removed text is:** `volN/review/glosses_removed.tsv` (line, form, text). One line per run is in each volume's `review/repair_log.md`; each volume's `STATUS.md` has a line too.

### How it was checked
- Every proposed change of Vols 3–8 (243 by script) was listed with the text before, the removed text and the text after, and read before writing. The results were re-read at about 45 places.
- By script, on every changed line: markers added equal log rows; Devanagari and Kannada letters unchanged; brackets, quotation marks and italics balanced; no empty brackets, no space before a stop, no line ending in a dash.
- Faults found in the new forms before or after the first write, and corrected (the write was undone with `git checkout` and re-run, not patched):
  1. a gloss in single quotation marks ran on through a Devanagari quotation;
  2. a list of glosses broke at `[?];` and at `for the first;`;
  3. a label that closed an italic remark took the closing `*` with it;
  4. the bare label matched inside `Gloss, mine…` and left `*Gloss,*` behind.
  The script check of brackets and quotation marks saw none of these; a search for stars or label words touching the marker did.
- Damaged lines in the final state: 0. Two removals take along a little more than the gloss and are in the log: Vol 16 line 243 (a Sanskrit word in three layers inside the English sentence) and Vol 3 line 12864 ("[End of Varga 37.]" lay inside the removed quotation).

### Step 2: trial reading of unlabelled glosses (Vol 12, 30 places, nothing changed)
A Sonnet agent read 30 quoted-Ṛk references spread over Vol 12 against the Kannada text and judged each place:
- **1 gloss of ours** (printed p. 658, after Ṛ. Saṃ. 5-11-6, the whole line `("O Agni, the Aṅgirases found you hidden in the cave…")`); the Kannada has no meaning there. This was checked in both files.
- **22 where the English translates the edition's own Kannada** (keep). Ten of them are an explanation after the verse, not a rendering of it.
- **7 with no rendering** (Sanskrit and reference only).

The result table with the Kannada evidence is in `vol12/review/gloss_trial_Nov18.tsv` (line numbers are those of the English file on Nov 18 2026 and move if the file is edited; the printed page and reference do not). If 1 in 30 holds, Vol 12 has about a dozen glosses of ours among its 360 quoted Ṛks. Steps 3 and 4 were not started.

## Facts to keep in mind
- **A marker stands after the reference, in the place of our gloss.** It is not placed before each reference.
- A marker means "an English gloss of ours stood here and was removed". A reference without a marker may still hide an unlabelled gloss, or may have no gloss at all.
- Counts from `CROSS_REFERENCES.tsv` (made by `tools/rv/crossrefs.py`, regenerated in this session): 40,740 references, of which 5,716 are to Ṛks; about 590 of those have a marker or labelled gloss on the same or the next two lines, mostly in Vols 2–8.
- Volumes without a Kannada text file (scan-based, such as Vol 9) cannot be checked against the Kannada by an agent; the judgement there would rest on the English alone.
- Cost of the trial: about 160k agent tokens for 30 references. About 4,900 unmarked Ṛk references remain.

## Still open (waiting for the user)
1. Is the trial's reading of "gloss" right, and may the other volumes be read that way (step 2)?
2. Quotations from other works (Nirukta, Brāhmaṇas, Sūtras): markers as well, or do their glosses stay? (step 3)
3. A quoted Ṛk with no gloss at all: add a marker after every quoted verse that lacks one (about 5,100 places, by script), or only replace existing glosses? (step 4)
4. Are `Sense, mine and tentative: …` (Vols 8, 10) and `**Translation** (mine, tentative): …` of the bhāṣya's introduction (Vols 4, 5) glosses to be replaced, or our translation of the commentary, to stay?
5. May the script be run on Vol 2 (18 glosses), or is its clean-up session still working there?
6. Remaining labelled lines whose label stands after a long quoted passage (Vols 1, 4, 5, 6): a reader must mark where the gloss begins.

## Commits (branch `claude/amazing-ride-6obngi`)
- `831ee85c` Vols 3–8: 263 more glosses replaced; new forms and `--list` mode in `gloss_marker.py`
- `92c4f7c2` Vols 10, 14, 16: 14 glosses replaced
- `30ea383f` publication list T12, volume status files, lesson, prompt and cross-reference list updated

Also updated: `PUBLICATION_TODO.md` (T12, last-updated line, change log), `docs/LESSONS.md` (a replacement by pattern is written only after every change has been listed with its text before and after), `docs/GLOSS_PROMPT.md` (a "Done" section and a stop before steps 2–4).

## Reference list consolidation (session of Nov 17–20 2026, branch `claude/gallant-albattani-or0sqt`)

### Aim
One work is referenced in ONE way only, in every volume and every script (English, Devanagari, Kannada). The user gives meanings; the session records them, checks each against the quoted line (column I of the lists), and produces lists for approval.

### What was done
1. **Vol 2 clean-up** (`vol2/CLEANUP_PROMPT.md`): our remarks removed by `tools/rv/cleanup_remarks.py` (log `vol2/review/removed_remarks.tsv`, `repair_log.md`); 93 Ṛk Saṃhitā blocks replaced from `refs/mandala/rv_mandala1.html` by `publish/tools/accents/accent_replace.py` (`verse_corrections.tsv`, `accent_report.tsv`). Kept for the user's review: `[?]` (413), `[sic]` (142), "tentative" (23). Merged to main.
2. **Vol 17 abbreviations**: forms such as ಭಾ. ಉ. (= Chā. U.), ಶಾ. ಭಾ./ಶ. ಭಾ. (Śaṅkara-bhāṣya) settled one by one; 20 repairs by the new `replace_sub` step of `rv/importer.py` (`vol17/data/import_fixes.json`), 8 notes decided (`decisions.tsv`).
3. **The one list** `rv/references.tsv` (legend / extra / mistake rows) with `rv/reference_approvals.tsv`, `reference_pending.tsv`, `reference_retain.tsv` (Roman numerals, Maṃ.); printed as `docs/REFERENCES.md`.
4. **Extraction and review files** in the root: `CROSS_REFERENCES.tsv/.md` (`tools/rv/crossrefs.py`), `REFERENCES_MASTER.tsv/.md` (`refs_master.py`), `REFERENCES_THREE_SCRIPTS.tsv`, `REFERENCES_KANNADA_FORMS.tsv`, `REFERENCES_GUESSES.tsv` (`refs_guess.py`, `refs_guess_checks.py`, 284 forms checked), `REFERENCES_NONE_PLACES.tsv`, `REFERENCES_CAPITAL_SAM_PLACES.tsv`, `REFERENCES_SU_PROPOSALS.tsv`, `REFERENCES_SU_DECIDED.tsv`, `REFERENCES_PA_OTHER.tsv`.
5. **Misreading patterns confirmed by the user**: Ṛ.→Pu./Ma./Mi./Mu./Kh.; De.→Je./Pe./Be./Se./Me./Ve.; Sū.→Rū./Dū./Sā.; Tai. ← Trai./Kṛ./Śai./Te./Tri.; Śa. Brā. ← Ka./Ta./Śat./Śr.; four-part numbers are Śatapatha-style; Mahābhāṣya numbers carry a vārttika part. Many forms decided from column I (e.g. Ma. Saṃ./Saṃ./Mi. Saṃ./Pu. Saṃ. = Ṛ. Saṃ.; M./म./Pā. Ma. = Mahābhāṣya; सू./Vā. Sū./P. sū. = Pāṇini sūtra; सि. = Nirukta; Kā. = Kātyāyana-vārttika; Anu. = Anukramaṇī; Dhā. = Dhātupāṭha; Vāl. = Vālakhilya; Piṅ. = Piṅgala; Ṛgvi. = Ṛgvidhāna).
6. **Per-volume legends** read from page images supplied by the user (not kept in the repo): `rv/legends_by_volume.tsv` and `_README.md`. Five volumes print no legend (4, 7, 8, 11, 14); Vol 1 has one in the supplied text.
7. **Prompt for the session that changes the volume files**: `docs/LEGEND_UNIFY_PROMPT.md` (one form per work; one generated Kannada legend per volume; shared tool with preview and proof; final check on REFERENCES_MASTER).
8. **Final list** (`tools/rv/refs_final.py` → `REFERENCES_FINAL.tsv/.md`): 71 works, one form each, with Devanagari (by script) and a full Kannada work name. Decisions applied: Jai. Sū.→Jai. Pū. Sū.; Ā. Sū. only; Phi. Sū. only; Ath. Saṃ. only (A. Ve. dropped); Pa. Brā. merged into Tā. Brā. (my choice, to confirm); Uṇ. Sū.→U. Sū.; Īśa.→Īśa U.; Śā. Bhā.→Śa. Bhā.

### Still open
- 20 Kannada forms are my guesses (Kau. Brā., Ka. U., Mā. Gṛ. Sū., Ya Saṃ., Kā., M., Sāṃ. Gṛ. Sū., Vāl., Anu., Dhā., Ṛgvi., Piṅ., Pā. Gṛ. Sū., Pā. Sū. Vā., the Bhāṣya forms, etc.); 11 more come from an earlier unconfirmed list. The full Kannada names are mine and need checking.
- Tā. Brā. vs Pa. Brā.; Vol 1 legend vs "six volumes without a legend"; whether legends list all works or only cited ones, and where the legend goes in the five volumes without one.
- Devanagari full stop after a bare consonant (`Ya Saṃ.`, `Īśa U.`, `Piṅ.`) is dropped by the transliteration: shared tool to fix.
- Places `Tai. U. U. 4-12-3`, `Śat. 25-7`; Vol 17 `A. U. 3-17-2` (looks like Chā. U. 3-12-2).
- Nothing in `rv/references.tsv` or in any volume text has been changed by the final list yet; that is the other session's job.
