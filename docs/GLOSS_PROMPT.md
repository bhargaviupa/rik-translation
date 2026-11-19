# Prompt for the gloss session (paste into a new Claude Code session on this repo)

You continue the work on the **glosses of quoted passages** in the Rigveda translation (repo `bhargaviupa/rik-translation`). Read `CLAUDE.md`, then `PUBLICATION_TODO.md` (point T12), `docs/REQUIREMENTS.md` B3.5 and D9, `CROSS_REFERENCES.md`, and in `docs/LESSONS.md` the entry of Nov 12 2026 on Vol 16 (removing text by pattern left about 70 damaged sentences). No API is used; nothing is re-translated.

## What the user decided (Nov 17 2026)
- The edition quotes verses and passages from elsewhere without a Kannada meaning; the translation added its own glosses, and many are incomplete.
- **A quoted Ṛk is to be glossed with our own edition's translation of that Ṛk** (the English under the verse in the volume where the edition comments on it), by script. Until that exists, **the marker `**GLOSS**` stands in its place**. A final copy is not printed while a marker remains.
- "Replace all glosses with a marker for now", and keep the list of all cross-references at the root.
- **Not now:** building the table Maṇḍala–Sūkta–Ṛk → English and filling the markers. Do not start it unless the user says so.

## Where it stands (Nov 18 2026)
- `CROSS_REFERENCES.tsv` (root; `python3 tools/rv/crossrefs.py` regenerates it): every reference of every volume by page and line; 5,715 are to Ṛks. Column `gloss` says whether a labelled gloss or a marker stands on that line or the next two.
- `tools/rv/gloss_marker.py VOL [--write]` replaced **682 labelled glosses in Vols 2–8** by `**GLOSS**` (exact forms only: see its docstring). Removed text: `volN/review/glosses_removed.tsv`. Lines with a label in a form it does not replace: `volN/review/glosses_left.tsv` (Vols 2–8: 427 lines when made; run the script without `--write` for today's count).
- Not touched: Vols 1 and 9–18 (86 labelled lines in other forms; Vol 9 writes `*Sense (mine):*` before its own rendering of the bhāṣya, which is not a gloss of a quotation).
- **Unlabelled glosses** are the larger part and cannot be found by pattern: in Vols 9–18 almost no quoted Ṛk has a labelled gloss (Ṛk references with a labelled gloss or marker beside them / all Ṛk references: Vol 9 15/561, 10 2/466, 11 0/679, 12 0/360, 14 2/605, 15 1/440, 16 5/206, 17 0/491, 18 0/335); the gloss is woven into the prose ("It says: …") or there is none.
- Vol 2 was cleaned up by another session on Nov 17–18 (remarks removed, verses from the reference); its "mine and tentative" labels were removed and the glosses kept, so in Vol 2 the remaining glosses are now unlabelled. Vol 19 is in translation in another session: do not touch it. Before changing a volume, check that no other session is working on it (`git fetch`; recent commits on that volume; ask the user if unsure).

## Done on Nov 18 2026 (second session)
- Step 1 done for Vols 3–8, 10, 14, 16 (277 more; counts in `PUBLICATION_TODO.md` T12). `gloss_marker.py` has the further forms and `--list FILE.tsv` (vol, line, exact text[, replacement]) for single lines and for step 2. Left: labels that stand *after* a long quoted passage (Vols 1, 4, 5, 6: the gloss must be delimited by reading), Vol 2 (18 would match; ask whether its session is finished).
- Step 2 trial done on Vol 12 (30 places; result in T12). **Do not continue step 2, 3 or 4 before the user has answered the four questions in T12.**

## Start
`git fetch origin main && git merge origin/main` on the branch this session was given; `pip install indic-transliteration rapidfuzz openpyxl`; `python3 tools/rv/crossrefs.py` and `python3 tools/rv/gloss_marker.py $(seq 1 18)` (report only) for today's counts. Never force-push; no pull request; push to `main` only when the user says so.

## Work, in this order

**1. The labelled lines that are left (Vols 3–8 first, then 1, 9–18).**
Read `glosses_left.tsv` of the volume. Sort the lines by form and report the forms with counts and two examples each. For a form that recurs, add it to `FORMS` in `tools/rv/gloss_marker.py` (the shared script; no per-volume tool) and run it; a single odd line is changed by hand as a logged repair. A line that is a remark and not a gloss (for example "Glosses are mine and tentative" in a note about a page) is not a gloss: leave it and list it for the volume's clean-up.

**2. The unlabelled glosses of quoted Ṛks.**
Take the rows of `CROSS_REFERENCES.tsv` with kind `rik` and no gloss. For each, a reader must look at the place: is there an English rendering of the quoted verse next to it that is ours (not the edition's Kannada explanation translated)? This needs reading, so do it by agents (Sonnet), one volume at a time, each agent given a page range and returning a list: line, the exact text of the gloss (copied, so that a script can find it once in the line), or "no gloss" / "the Kannada explains it: keep". Before a whole volume, **try 30 references of one volume, show the user what the agent marked, and wait for a yes**: what counts as a gloss here is a judgement, and the user should see it once.
Then the script replaces exactly the listed text by `**GLOSS**` (refuses when the text is not found exactly once in the line) and logs it as in step 1.

**3. Quotations from other works** (Nirukta, Brāhmaṇas, Sūtras; kind `other`): requirement B3.5 leaves their glosses to the translator. **Ask the user** whether these are to become markers as well or stay; do not change them before the answer.

**4. Where a quoted Ṛk has no gloss at all:** ask the user whether a marker is to be added there too (so that every quoted Ṛk gets its gloss later), or only existing glosses are replaced.

## Rules for every change
- A gloss is replaced whole: label, quotation marks and text; nothing else on the line changes. Devanagari, transliteration and references are never touched.
- Everything removed goes to `volN/review/glosses_removed.tsv` (line, form, text), so that it can be restored or compared later with the edition's own translation.
- After each form or volume: the count of `**GLOSS**` added equals the rows logged; check by script for damage (empty brackets, a bracket or quotation mark without its partner, ` .` ` ,` doubled spaces, a line ending in a dash); **read 30 changes before and after yourself** and report the count damaged. More than one damaged: undo that form and do it differently.
- One line in the volume's `review/repair_log.md` per run (what, how many, how checked). Commit and push after each volume.
- Volumes in the new style (11, 17, 18) already carry `**NOTE**` marks; `**GLOSS**` is a different mark and is not listed in `notes.tsv`.

## At the end of the session
Run `python3 tools/rv/crossrefs.py`; update `PUBLICATION_TODO.md` (T12: counts replaced and left per volume, the two questions of steps 3 and 4 and their answers, "Last updated", change log) and each touched volume's `STATUS.md`; extend `docs/LESSONS.md` if something recurred. Report in a few lines: per volume, markers before and after, lines left, how each change was checked, what waits for the user.

## Stop and ask when
It is unclear whether a passage is our gloss or the commentary's own explanation; a volume is being changed by another session; a replacement would remove something that is not a gloss; the usage limit is near (commit and push first; the next session resumes from the counts the two scripts print).
