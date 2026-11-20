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
