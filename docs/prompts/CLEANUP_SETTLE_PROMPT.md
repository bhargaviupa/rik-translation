# Prompt: settle doubtful words and numbers, and clean up a finished volume (Kannada and English files)

Paste this into a new Claude Code session on the repo `bhargaviupa/rik-translation`, after naming the volume (N) and its branch. It was written from what went wrong, and what worked, while Vols 13, 22, 23, 27, 28 and 30 were translated and checked (Nov 26–27 2026). Read `CLAUDE.md` first; its rules are not repeated in full here.

---

You are cleaning up **Volume N** of the Rigveda translation: its English file (`volN/Rigveda_Samhita_VolN_English_Translation.md`) and its Kannada file (`volN/Rigveda_Samhita_VolN_Kannada_Text.md`). The volume is translated and `python3 tools/rv/batch.py audit N` passes. Your job is to settle the doubtful words and numbers and to repair what checks and readers find, **without asking the user questions and without handing the user a list to review** (user, Nov 25 2026).

## 1. The rules that decide every doubt

1. **The supplied Kannada text is the base.** Never correct a letter or a number from memory, from another edition, or because "the real Pāṇini number is …". Example: the Kannada prints `ಪಾ. ಸೂ. ೬-೧-೧೭೯`; the translation had written 189 from memory; it was set back to 179. A misprint in the print stays as printed.
2. **Numbers come from the supplied Kannada, always** (its numerals are correct). A number the English has and the print has not is removed. An impossible printed number is applied as printed and listed in `volN/review/open.tsv`.
3. **Sanskrit lines are derived data.** Saṃhitā, Pada and Sāyaṇa blocks come from Wikisource; the Devanagari and IAST in the English file are made from the Kannada by script. **Never type Devanagari or IAST.** To put Sanskrit into the English text, copy it from the Kannada file and convert it by script (`tools/rv/convert.py` `kn2deva`, `publish/tools/translit/add_iast.py` `deva_to_iast`; see the helper in section 4). Stray accent marks and Kannada vowel signs inside such lines are not hand-edited.
4. **Wikisource is never edited.** An error in the Kannada's Sanskrit is changed only where the intended reading is certain, and then as a row of `volN/data/source_fixes.tsv` (place, as supplied, corrected, reason, basis, who) plus a line in `volN/review/repair_log.md`.
5. **No translator remarks in the English** (no "as supplied", "as printed", "[sic]", "[?]", running heads, "is not here", "see below", placeholders such as `[[b-intro-none]]`). A place that needs a decision carries `**NOTE**` in the text and one row in `volN/review/notes.tsv`: the number of marks equals the number of rows (an audit gate).
6. **Output files are append-only**; repairs of earlier text are separate edits, each logged in `volN/review/repair_log.md` (date, page, what, why).

## 2. How to settle a doubt (the default rule, no questions)

For every row of `volN/review/notes.tsv` that has no decision:
- the question speaks of a Kannada misprint, misreading, garbled or damaged word and the English has the sense the Kannada intends → **English kept**, a row in `volN/review/kn_misprints.tsv`;
- any other doubt → **English kept unchanged**, a row in `volN/review/decided_by_default.tsv`;
- omissions are not added; `questions.tsv` stays empty.

`python3 tools/rv/notes_resolve.py N` previews, `--write` applies (the `**NOTE**` marks and the text are not changed; the `decision` column is filled). Before running it, look for NOTEs whose premise is **false**: a NOTE saying "long quotation not located in the supplied text" was wrong twice (Vol 13 pp. 643 and 645; Vol 28 p. 300): the passage stood in the Kannada file. Search the Kannada file for the first and last words; if found, restore the whole passage (section 4), remove the mark **and** its row (and its row in `decided_by_default.tsv`).

For a doubtful **word** in the Pratipadārtha (word meanings): `python3 tools/rv/pratipada_check.py N --source` compares each word with the Wikisource Pada word of the same Ṛk; `pratipada_apply.py N [--from-page P] --write` applies only the certain one-letter corrections (never a change of ending, sandhi, a voiced/voiceless swap), each logged. Apply it before translating, not after.

## 3. What to look for (the faults that really occurred)

Run these checks in this order; each is free:
1. `python3 tools/rv/batch.py audit N`, `python3 tools/rv/check_labels.py N` (every English block under the label of its own section; English and Kannada block counts), `python3 tools/rv/check_inline.py` (every inline Sanskrit segment occurs in the Kannada), `python3 tools/rv/batch.py rkheads N --dry-run` (must say "nothing to change").
2. **Sūkta and Ṛk structure:** the list of `## Sūkta` headings is complete, in order, no duplicate; each sūkta's Ṛk count equals the Wikisource index (`refs/wikisource/index/ws.sqlite`, table `rik`, columns m, s, r). A "(continued)" heading is not a Ṛk. Typical faults: two Ṛk headings and an empty Saṃhitā heading in front of a verse (the window put the label before the heading); a Ṛk heading, Saṃhitā heading and block placed before the Anuvāda instead of after it; an unnumbered `#### Ṛk`; a sūkta heading in the wrong place (it goes before Sāyaṇa's introduction block, not on the title page of a new aṣṭaka); a sūkta printed twice by the supplied text (keep both, mark with a NOTE).
3. **The particulars line** (Maṇḍala, Anuvāka, Aṣṭaka, Adhyāya, Varga, number of Ṛks, seer, deity, metre) of every sūkta: count the sūktas without "Number of Ṛks" in the English; each such sūkta is either a real gap in the print or a missing line (Vol 22 had eight missing: Sūktas 22–28 and 54). Write a missing line from the Kannada lines; if the Kannada has no deity line, write none.
4. **Labels lost at a page break** in the supplied Kannada (`*ಪದಪಾಠಃ*` or `*ಸಾಯಣಭಾಷ್ಯಂ*` missing before a block at the top of a page): the block count is then one off. Insert the label in the Kannada file (`batch.py fix`), log it.
5. **Page-boundary slips:** a Ṛk's first Saṃhitā line at the foot of a page and its second line at the top of the next: the heading and first line belong on the first page, the second line under the next page heading. A Pratipadārtha entry cut by the page break keeps its marks balanced (`⟪ ⟫`).
6. **Remarks and artefacts:** `grep -n -i "as supplied\|as printed\|sic\|is not here\|supplied text\|\[\[b-"` on the English file; an English line that is only a placeholder.
7. **Sanskrit typed in Latin letters** inside double quotes ("ūti", "vāja", "mitraḥ sūryaḥ"): replace by the copy `⟦…⟧` from the Kannada file, or leave the word out. Letters of another script inside Latin words (Cyrillic р, е in "nare") become Latin.
8. **Kannada prose quoted as a Sanskrit block** in the supplied text (a title page, a Pīṭhike, the Anuvāda and particulars lines inside the introduction block): it shows as Kannada-in-Devanagari. If it is a few lines inside one block (Vol 28 Sūkta 54), un-quote them in the Kannada file and remove the transliterated lines from the English block (the translation stands in Anuvāda/Particulars); if it is a whole page, list it in the repair log and leave it.
9. **A picture line `[figure: …]`** left in the Kannada file: open the picture; if it only repeats verse blocks that are already there, remove the line with `batch.py fix`; otherwise copy its text letter by letter into the Kannada file.
10. **A Pratipadārtha entry with no headword** ("- (they)") or with a Kannada gloss turned into a headword: the headword is the Kannada word before the dash, converted by script.
11. **A closing verse, colophon or blessing** that stands in English only: the Sanskrit lines get their Devanagari and IAST from the Kannada by script, the English rendering stays.
12. **Grammar sections** (Sanskrit composed from the Kannada): only check the sūtra numbers against the Kannada (`೬-೪-೧೪`, not `೬-೪-೧೬`), the entries (none missing), and Kannada words left inside the Sanskrit (they need a Sanskrit rendering, which no gate can check: list them, do not guess).

## 4. How to repair (the mechanics that avoided mistakes)

- **Work on one thing at a time and verify after each edit:** `python3 tools/rv/batch.py audit N` and `check_labels.py N`. After every scripted edit, assert that the old text occurred exactly once; a silent failed replace once duplicated text.
- **To put a Kannada passage into the English as Sanskrit:** take it from the Kannada file (join its lines), then
  `d = convert.kn2deva(text)` (from `tools/rv/convert.py`) and `iast = add_iast.deva_to_iast(d)` (from `publish/tools/translit/add_iast.py`); write `f'{d} (*{iast}*)'`. Do not retype.
- **Never change a letter of the Kannada file** except by `batch.py fix` for a structural fault (a missing label, a figure line, a quoted prose line) or a certain one-letter source fix; a stray line is kept as an italic note, never deleted.
- **A repair that touches the output files is logged at once** in `volN/review/repair_log.md` (one line: date, page, what, why). A repair of earlier text is committed with `git add -A; git commit; git push` after the audit passes.
- **Compare with the supplied text, not with the other file:** the English must say what the Kannada says. Two QA readers found real errors by reading the English page against the Kannada page; the faults were wrong sense ("other than the thunderbolt" for "split by the thunderbolt"), a dropped Sanskrit gloss, a quotation cut to its first and last words, a verb attributed to the wrong subject (dual verb: the two Aśvins protected him), "heaven and earth" for "earth and atmosphere".
- **Do not touch what is derived:** accents (`publish/tools/accents/accent_volume.py` only, report mode unless asked), Devanagari/IAST of blocks, the Wikisource blocks.

## 5. Quality check by an independent reader (the finishing checklist, `docs/HANDBOOK.md` §11)

Start a **read-only** reader agent (model `opus`, `subagent_type: general-purpose`) that may create only `volN/review/qa_sample.md`, with this task: 24 pages (12 spread evenly through the volume, 12 pages that carry a "Special Topics" heading), English page against Kannada page, checking (1) numbers and references, (2) names, terms and quotations, (3) negations, attribution, who does what to whom, (4) omissions and additions (and that a quotation announced in the English is really followed by it). Ask for exact quotations of the wrong English and the correct reading, counts of ERRORs and MINORs, no assumption about what the faults are. If ERRORs are found, run a second reader on 24 other pages (`qa_sample_2.md`). Repair every ERROR and every MINOR that is not in derived Sanskrit; list what is left in `repair_log.md`. **Do not stop at the pages the reader checked:** when a fault is a kind (a missing particulars line, a truncated quotation), count it over the whole volume with a script, as the second Vol 22 reader's remark led to eight missing lines instead of two.

## 6. Learning to pass on (also for later volumes)

- A gate that passes does not mean the page is right: the gates check structure, not sense. The two QA readers found 8 errors in 48 pages of Vol 13 and 6 in 48 of Vol 22 and Vol 28 after every gate had passed.
- A NOTE written by the translator can be wrong: "not located in the supplied text" was false whenever the passage was long. Test the premise before accepting a NOTE.
- The same fault comes back in later windows: when a hand-fix is made twice, change the shared tool (`tools/rv/…`) or its loop, and say so in `docs/LESSONS.md`; never keep a per-volume tool.
- Temporary helper scripts disappear (the session's temp folder was cleared once and a collection loop died silently with an empty log): keep a helper that is used twice under `tools/rv/` and committed.
- Never merge into `main`, open a pull request or spend API money without the user's word; commit and push after every repair; report only what a finished command showed (counts, `git log`).
- Report to the user in a few plain lines: what was repaired, what is left and why, nothing that needs the user's reading.
