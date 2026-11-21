# Requirements — Ṛgveda-saṃhitā (Kannada edition) in English

**Draft 4, Nov 21 2026 — for the user's review.** Draft 3 (Nov 12) was extended on Nov 21 with Parts I–M and with requirements gathered from the other documents of the repository (a survey of the rules, design, to-do and status files). `docs/DESIGN.md` was approved by the user on Nov 13. Nothing in the tools or volumes has been changed to match this document; where a requirement is not yet decided by the user it is marked *proposed* or listed in Part F.
Until it is approved, the rules in force remain `CLAUDE.md`, `docs/HANDBOOK.md` and `tools/rv/BRIEF.md`. Once approved, this is the one place that says *what* a volume must be; the other files say only *how* it is made and point here.

**How to read it**

| Part | What it answers |
|---|---|
| A. Volume structure | What does a finished volume contain, from the cover to the last page, and in what order? |
| B. Generic rules | What holds everywhere in a volume, whatever the section? |
| C. Specific rules | What holds for one particular section (the verse, the commentary, the contents page …)? |
| D. Checks | How do we know a volume meets A–C? |
| E. Working rules | How the work itself is carried out (unchanged rules, kept short). |
| F. Open questions | What the user still has to decide. |
| G. Effect on existing volumes | What each finished volume would need. |
| H. Publication readiness | What is still missing before any volume can actually be published. |
| I. Second reading | What the second reading must find, which kinds of error need which reader, how each reader is measured, and what it cannot do. |
| J. Human reading | Which readings only a person can do, who does them, and where each decision is recorded. |
| K. The Sāyaṇa-bhāṣya reader | A second book: Saṃhitā, Pada, Sāyaṇa's bhāṣya in Devanagari, transliteration and full English; how it is made, checked and built, and how a volume refers to it. |
| L. The volumes | One row per volume: scope, source, layout family, standing deviations. Replaces the table of Part G. |
| M. Older volumes (1–10) | The method for bringing the scan-based volumes to these requirements. |
| N. The form of a volume, stated completely | Exactly how a volume reads, from the first page to the last, in rules that refer to no other volume. |

Marks used: **NEW** = differs from the volumes made so far. **(F3)** = see open question 3 in Part F. The source of every requirement is listed in the appendix; the user's review comments of Nov 12 are kept verbatim in `docs/review/USER_REVIEW_2026-11-12.md`.

---

## A. Volume structure

### A1. What is delivered for each volume
1. **English book** — PDF, with its `.html` and `.md`.
2. **Kannada book** — PDF and `.md`: the text of the original, matching it closely in content. (F9)
3. **Review lists** for the editor: places that need a decision, deviations from the reference text, repairs made, results of the checks. Every volume folder holds the same records under the same names: `STATUS.md`, `review/notes.tsv`, `review/repair_log.md`, `data/source_fixes.tsv`, `review/page_flags.md`, the accent and inline-mismatch reports, `contents_check.md`, `qa_sample.md`, `parts/costs.md`, `volcfg.json` and `pubcfg.json`. `CROSS_REFERENCES.tsv/.md` at the root list every reference of every volume by page and line.

**Two layers, kept apart:**
- **The published books** (the PDFs in `publish/out/`) are as professional as a printed book can be. They contain **no known error, no comment of ours, no note by the model, no mark of doubt, no trace of how the files were made.**
- **The working files** (the `.md` files and review lists inside `volN/`) hold everything else: open questions, the editor's decisions, repairs, results of checks, faults of the supplied text.

**`publish/out/` holds releases only** (a release meets Part H2 in full). A **review copy** is marked as such on every page and stays inside the volume's own folder, `volN/review/`. (Decided Nov 13 2026.)

Every volume has the same structure, section names, layout and abbreviations. A volume that differs is brought into line or listed as not conforming.

### A2. Front matter — the same order in every volume **NEW**

| No. | Page | What it shows | Taken from |
|---|---|---|---|
| 1 | Cover | Cover picture with **this volume's number in Kannada**. One English line below: volume number, Maṇḍala, Aṣṭaka (as in Vol 15). | the volume's supplied file |
| 2 | King | Portrait of the king. | Vol 1, p. 4 — for all volumes |
| 3 | Guru | Portrait of the guru, with the English translation of its text. | Vol 1, p. 5 — for all volumes |
| 4 | Scholars | List of the board of scholars. | as Vol 15, p. 6 |
| 5 | Present day | Present king and present guru: placeholders. | — |
| 6 | Translation credentials | **New layout: half page picture, half page text** (like Vol 15, p. 2). | new design |
| 7 | Copyright | Copyright, ISBN and the like. **No reference to Claude in the copyright.** A **Thank-you section**. (F8) | `publish/release.json` |
| 8 … | Contents | Contents in English, as in Vol 1. | supplied file |
| next | **Preface to the English edition** | By the translator-editor (the user). **A placeholder page in every volume until the text is written.** (F15) | the user |
| next | Preface / Introduction of the original | As the volume has it. No Kannada headings. | supplied file |
| next | Abbreviations | The volume's list, with Sanskrit in place of the Kannada text. | supplied file |

Vol 15 was built in another order (preface before the guru's portrait); it is to be corrected.
The front matter also holds the English-typeset **title page** and the original's **permission page**; the cover is the real scan (HANDBOOK §8). A colophon at the end of an adhyāya's last sūkta is given in three layers, with the Kannada closing line.
**This layout may change again** (user, Nov 13 2026); it is one setting of the printer and is listed in `TODO.md`.
The credits of the original edition are either marked clearly as taken from the original or combined with our own credits page. (F8)

### A3. Body

**First page of the Ṛks:** an Om picture at the top.

**A Maṇḍala** begins with its heading. **A sūkta** begins with its heading, followed by what the original prints before the first verse (Sāyaṇa's introduction, the Kannada introduction, the particulars of the sūkta).

**A Ṛk** has these parts, in this order, each under its own sub-heading:

| No. | Part | Heading in the English book | In short (details in Part C) |
|---|---|---|---|
| 1 | Verse | **Saṃhitā-pāṭha** | from the reference text, accented, every akṣara set apart; transliteration |
| 2 | Word-text | **Pada-pāṭha** | as supplied; transliteration |
| 3 | Commentary | **Sāyaṇa-bhāṣya — Sāyaṇa's Explanation** **NEW** | Sanskrit, transliteration **NEW**, then an elaborate English **Summary** |
| 4 | Word meanings | **Word-to-word meaning** **NEW** (was Pratipadārtha) | one word per line |
| 5 | Sense | **Gist** **NEW** (was Bhāvārtha) | English |
| 6 | English of the edition | **English translation** | reproduced from the original |
| 7 | Topics | **Special Topics** (decided Nov 13 2026; the Kannada "Viśeṣaviṣayagaḷu" is not shown) | English, with quotations and references |
| 8 | Grammar | **Grammar (Vyākaraṇa-prakriyā)** | rendered in Sanskrit |

Parts 6–8 appear only where the original has them.

**End of an adhyāya and of the volume:** the colophon and closing lines of the original, nothing added.

### A4. The page (print)
- **Footer:** the page number of the Kannada original and its Maṇḍala–Anuvāka–Varga line, so a reader can find the place in the Kannada book. (F3)
- **Body:** no page numbers of the original. **NEW** (They are now printed as "p. N" marks in the text.)
- **Footnotes:** not used for references. **NEW**

### A5. Kannada book
The text of the original, page by page, with its Sanskrit in Kannada script. Nothing of ours stands in it beyond what is needed to find a page, a sūkta or a Ṛk. (F9)

---

## B. Generic rules (hold everywhere in a volume)

### B1. Which source governs
1. **The user's supplied text of the volume** is the base for everything, with the two exceptions below: the text, cover, contents, list of scholars, preface, abbreviations.
2. **Exception — the verse:** the Saṃhitā-pāṭha always comes from the reference text. **NEW**
3. **Exception — portraits:** from Vol 1, for all volumes.
4. Outside these exceptions, no letter and no number is corrected from memory or from another edition.
5. **No number where the print has none.** A printed number (Pāṇini, Uṇādi, Nirukta, a verse number) is copied as printed, even if another edition numbers differently; where the print has none, none is written.
6. **A departure from the supplied text is a record, not an edit.** The supplied text is never edited. Every place where the book differs from it (a garbled label, "si" for "ni", a stray figure, a missing page mark, a misread word with a certain reading) is a row of the volume's list: place, as supplied, as printed, reason, who decided (`volN/data/source_fixes.tsv`; for a word, supplied letters → reading → basis). The Kannada book is printed with that list applied.
7. **A reading may be settled from another text, never altered by it.** The reference text and a clean edition of Sāyaṇa may be consulted to settle a misread word; other people's translations are not read. What was consulted is the basis of the logged reading.
8. **An editor's decision is stored beside its unit** and applied at every printing, so that it survives a rebuild (DESIGN §3.1).

### B2. Sanskrit
1. Sanskrit is given in three layers: Devanagari, transliteration (IAST), English. **The Sāyaṇa-bhāṣya is the exception in the volumes** (user, Nov 11 2026; `no_iast_blocks` in `volcfg.json`, Vols 11 and 17–21): there it stands in Devanagari only, followed by its Gist. Its three layers, with the full English of Sāyaṇa's text, belong in the Sāyaṇa-bhāṣya reader (Part K; user, Nov 21 2026). Vols 12, 14 and 15 keep their earlier form, and Vol 16 is transitional, until brought into line (G, L).
2. Devanagari and transliteration are made by script from the supplied text. The translator does not type them.
   **Transliteration is made when the book is printed and is not stored in the volume files** (user decision, Nov 11 2026, recorded on the branch `claude/dreamy-cerf-z4h3f4`; it now covers the Sāyaṇa-bhāṣya too, by the comment of Nov 12).
3. No Kannada script in the English book: not in headings, references or abbreviations.
4. **No letter of another script** (Tamil, Telugu, Malayalam, Bengali, Arabic, Cyrillic, private-use) in any English or Kannada file, and no Devanagari in the Kannada book. Where the supplied Kannada holds such a letter or a Telugu digit by misreading, it is rewritten letter for letter as Kannada and logged (B1.6).
5. **Rendering:** no missing glyph or dotted circle (◌) in a PDF; the accent mark stands after the visarga or anusvāra; the Pada-pāṭha is unaccented; the svarita stroke is set in a font that draws it (Lohit Devanagari, decided Oct 2026).

### B3. References and abbreviations
1. References stand **in the text**, where the original has them, written with **English abbreviations**. **NEW** (Many were moved to footnotes.)
2. **One list for all volumes** gives every work cited: the Kannada form in the print, the English form we use, the full title. It starts from the bibliography of Vol 1 (PDF p. 39), which is to be checked for completeness.
3. The same list records the **known mistakes**: misprints of the original, misreadings of the machine text (for example the letter read "si" is "ni" = Nirukta), and mistakes of the translation.
4. Every volume uses exactly the abbreviations of that list.
5. **A Ṛk quoted from elsewhere in the Saṃhitā is glossed with our own edition's translation of that Ṛk** (user, Nov 17 2026): the English that stands under the verse in the volume where the edition comments on it, taken by script from one table Maṇḍala–Sūkta–Ṛk → English; never a gloss composed on the spot and never another translator's. Where that volume is not made yet, the gloss is a **placeholder**, filled by script once the Ṛk's translation exists. Quotations from other works are glossed by the translator. **NEW**
6. **One form per work.** One work has one abbreviation in every volume and every script, with no "or" forms (decided Nov 19–20 2026: for example Ā. Sū. only, Ath. Saṃ. only). The list (`rv/references.tsv`) is made by the references review; about 31 Kannada forms and full names in it are proposals still to be confirmed (`reference_bhr.md`).
7. **The legend** (the list of abbreviations printed in the volume) is generated from that one list, in the same order, in the Kannada, Devanagari and English forms, and printed in **every** volume, including those whose print has none. *Proposed (LEGEND_UNIFY_PROMPT; C10 and F19):* whether it shows all works or only those the volume cites is open.
8. **Reference numbers are never changed by the names step**, and the script proves it. A number marked `[?]` is corrected only from the user's numerals file; no reference is corrected by hand. Every change of a name is a row of `volN/review/refs_applied.tsv`. A printed number that differs from the standard one is kept; a concordance is used only after the user is asked.
9. **An abbreviation not in the list** is transliterated letter for letter and gets a `NOTE`.

### B4. Nothing of ours in the text
1. **No text about the making of the file:** no status lines at page breaks, no "the Sāyaṇa-bhāṣya from p. 235 continues here", no remarks on how the print looks.
2. **Stray letters and words** of the supplied text (loose figures, page signatures, fragments) are removed. **NEW** (They were kept and noted.) (F4)
3. **One mark only** for a place that needs the editor's decision: `NOTE`, **in the working files only**. Its question is in the volume's review list. No `[?]`, no `[sic]`, no "as supplied". The published book shows none of it (A1). (F7) *Exception for the time being:* `**GLOSS**` marks a quoted Ṛk whose gloss is still a placeholder (B3.5); the release gate refuses while one remains (D9). Whether quotations from other works are marked too is open (F18).
4. **When a `NOTE` is used.** Only for a real doubt. Not for a certain machine slip, a garbled label or a stray line (those are B1.6 records). A misprint of the print is translated by its best reading and gets a `NOTE`; it is never silently put right. The note is short and factual. How a misprint shows in the published book is open (F20).
5. **Removing a remark or turning it into a `NOTE`** is done by script, removes words only, adds none, logs the original in a list so that no information is lost, and is checked afterwards by reading a sample before and after. (The removal of "as supplied" from Vol 16 on Nov 12 2026 broke about 70 sentences.)

### B5. Deviations
1. **The verse.** The book prints the Saṃhitā of the reference text (B1.2). The Pada-pāṭha, the word meanings and the bhāṣya are given as the edition has them.
2. **The reference is the correct source of the verse** (decided by the user, Nov 13 2026, after checking six differing places of Vol 17 against the printed book: in all six the book agreed with the reference). Every difference of the supplied verse is therefore taken as a misreading of the machine text: the reference is printed and **no footnote is given**. A footnote on the Ṛk is printed only where the editor records that the printed book really differs (`volN/data/verse_decisions.tsv`, decision "edition"). All differences are kept as a record in `volN/review/verse_misreadings_settled.tsv`.
3. **Pada-pāṭha, Word-to-word meaning, Sāyaṇa-bhāṣya.** These are given as the edition has them and are never altered to agree with the reference verse. **Exception (user, Nov 14 2026, `TODO.md` 4):** a word of the Pada-pāṭha or the word meanings that does not match the verse follows the verse. Any other disagreement is listed for the editor. (F1, second half)
4. **Where Sāyaṇa and the Kannada gloss differ,** the Gist follows Sāyaṇa and the place gets a `NOTE`. **Where the verse of the edition and the Kannada book differ,** the Kannada book's verse is corrected from the reference word by word, only the differing words, in the edition's spelling habit; places that would move words across a line, or where a word is missing, are left (user, Nov 13 2026; Vol 17: 374 words in 257 verses, listed).

### B6. Completeness
1. Every page, every sūkta and every Ṛk of the original is present once, in order.
2. Nothing is added that the original does not have, apart from the headings of Part A and the English itself.
3. A sentence cut by a page or window break is complete. A picture (`[figure: …]`) that holds a verse the text lacks is transcribed; one that only repeats a block is dropped. A large embedded table or index is flagged to the editor, never silently transcribed or skipped.
4. A page with no running head is generally the first page of a sūkta, a Maṇḍala or a chapter, not a missing page. Only absent text is missing (lesson 67). A sūkta introduction or a bhāṣya that the supplied text lacks is marked with a `NOTE`; nothing is added (H2.6).
5. Dvipada Ṛks are counted by printed units: a four-pāda Ṛk printed "5 (10)" counts as two reference verses, so that the Ṛk-number check gives no false alarm.

---

## C. Specific rules (one section each)

### C1. Saṃhitā-pāṭha
- Text from the reference (B1.2), with accents.
- Every akṣara set apart, in every volume (the look piloted in Vol 17).
- The Ṛk number is checked against the reference: none missing, none misplaced.
- Where the edition's verse differs from the reference: stated under the verse (B5.1), once confirmed (B5.2).
- The Kannada book's verse has its own akṣara-spacing pattern.
- Ṛk numbers follow B6.5 for dvipada Ṛks.

### C2. Pada-pāṭha
- As supplied, with transliteration.
- A deviation is mentioned (B5).

### C3. Sāyaṇa-bhāṣya — Sāyaṇa's Explanation
- The Sanskrit as supplied, with its transliteration. **NEW**
- Followed by an **elaborate summary in English** that covers most of the commentary. The grammatical tail need not be explained. The Gist of the bhāṣya states: the viniyoga with its sūtra; who is addressed and what is asked; the gloss of each word; every alternative ("ಯದ್ವಾ"); each authority with its reference; for an introduction, seer, deity and metre.
- The full English of Sāyaṇa's text, with the grammar, is the work of the reader of Part K, not of the volume. How a volume refers to it is K7.
- A deviation is mentioned (B5).

### C4. Word-to-word meaning
- Each word on its own line, with its meaning.

### C5. Gist
- The sense of the verse in English, from the Kannada.

### C6. English of the edition
- Reproduced from the original. Heading: (F5).

### C7. Special Topics
- English. Every Sanskrit quotation in three layers, in full, never summarised or shortened; its closing daṇḍa and abridgement dots belong to it; with its reference in the text (B3.1). A quotation the Kannada does not translate is glossed only as B3.5 says (F18).

### C8. Grammar
- (F6, decided Nov 13 2026 as "I think"): Sanskrit rendering as begun in Vol 17. Complete: one word per line, headword first, then the derivation; roots, affixes, sūtra texts and references copied letter for letter; nothing added or dropped; no English inside it. The Sanskrit is composed by the translator from the Kannada (written in Kannada script inside `⟪ ⟫`, shown in Devanagari only); no script can check it, so it is read under HR3 and by reader R2.

### C9. Contents
- In English, as in Vol 1; the page numbers shown are those of our book.

### C10. Abbreviations page
- The legend of B3.7: generated from the one list of B3.2, in the same form in every volume; the Kannada forms of the print are replaced by Devanagari. (This replaces "the volume's own list"; F19.)

### C11. Preface / Introduction
- Translated in full. No Kannada headings. The Pīṭhike at the front of a volume is the "Preface"; the opening chapter of the body is the "Introduction" and begins on a new page (lesson 26).
- In the Contents a number that is wrong in the print stays as printed, the link is set right, and a footnote records it. There is no separate sūkta index in the English book unless H3.6 adds one.

---

## D. Checks (when is a volume done?)

| No. | Check | Covers |
|---|---|---|
| D1 | The structure of Part A is produced by script, not written by the translator. | A2, A3 |
| D2 | Every page is read a second time by the readers of Part I (R1–R6): numbers and references, names, negations, omissions, additions; the Sanskrit of the grammar section; the Sanskrit and the Kannada words of the supplied text. | B1, B6, C3, C8, Part I |
| D3 | Ṛk numbers against the reference: every Ṛk present once, in order. | C1, B6 |
| D4 | Every Sanskrit block under the heading of its own part. | A3 |
| D5 | Same number of verses in the English and the Kannada book; no page without its mark. | B6 |
| D6 | Every abbreviation is in the one list. | B3 |
| D7 | Nothing of B4 left in the text; no Kannada script in the English book. | B2, B4 |
| D8 | A sample of pages read by a different model, not told what to expect; findings repaired and logged; hand repairs get the same QA; **the sample is doubled if it finds an error**. Size: see F21. | all |
| D9 | **Release gate:** the release PDF is built only when D1–D8 pass, no `NOTE` is open, no gloss of a quoted Ṛk is still a placeholder (B3.5), and no known error is listed as unrepaired; the rights statements of `publish/release.json` are filled; it is checked for any leftover mark, bracketed comment or working text. A volume that quotes Ṛks of later Maṇḍalas does not go to print before those volumes are translated, unless the user allows an exception (T12). | A1, H1, H2 |
| D10 | Every figure and reference number of the Kannada appears once, unchanged, in the English; the translator cannot alter it. Every Sanskrit block equals its source letter for letter; every difference between the reference verse and the edition's has a recorded state; every unit that needs English has it, none empty or doubled. | B1, B6 |
| D11 | The number of Ṛks of a sūkta equals its Ṛk headings; the sūkta count equals the contents; heading levels are correct; accent defects are flagged and unaccented lines listed, never accented by hand. | C1, B6 |
| D12 | No character of another script (B2.4); `[?]` counts equal in both files; page marks are monotonic; no `XXX`, no empty `⟦⟧`. | B2 |
| D13 | A correction made to one language file is made to the other. | A5 |
| D14 | The built PDF is looked at as the reader sees it: the first 20 pages and one body page of each book, cover and title together, no ◌. | A4, B2.5 |

Each check reports how many items it compared. A volume that was not checked is "not checked", never "clean".
D1 and D2 are agreed in principle; how they work is for the design document.

---

## E. Working rules (extended Nov 21 2026)
- Finished text is changed only by logged repairs.
- Work is committed and pushed; no force-push; `main` only when the user asks.
- API money is spent only after the user has seen the estimate.
- Rights, ISBN and publisher live only in `publish/release.json`.
- Built PDFs are kept in the repository (`publish/out/` for final copies) and every rebuild is committed; page scans are not (user decision, Nov 12 2026). **Word files and built HTML are not kept; a volume folder holds its `.md` files and what they are made from, not built copies** (user decision, Nov 13 2026).
- The reference texts are for private study; the repository stays private.
- Reports say what was verified and how.
- Output files are append-only with one trailing progress note, written only by `tools/rv/batch.py`; repairs of earlier text are separate edits in `volN/review/repair_log.md`.
- One writer per volume; one long job at a time. No per-volume tools: a fix goes into the shared tool, and a hand-fix used twice becomes a script change. Per-volume scripts of the old method are frozen in `archive/`.
- **Every task can be run by the API or by agents**, at the user's choice (user, Nov 12 2026). The API key stays in `RIK_API_KEY` and is never printed; spending only after the user has seen the estimate.
- Each volume has `volN/STATUS.md` (template `docs/STATUS_TEMPLATE.md`); the root `PUBLICATION_TODO.md` is ticked by every session that finishes something.
- Images and transcriptions of the print go public only with the user's approval.
- A Word file is not kept; it may be made on request with pandoc and is not committed (F22).

---

## F. Open questions for the user

| No. | Question | Concerns |
|---|---|---|
| F1 | **Deviations.** *First half decided Nov 13 2026:* a difference between the reference Saṃhitā and the edition's Saṃhitā is stated in the book (B5.1). *Still open:* when the Pada-pāṭha, a word meaning or the bhāṣya disagrees with the verse in some other way, is that printed too, or listed for you only? (assumed: listed only) | B5, C2, C3 |
| F2 | **Two "Gists".** *Decided Nov 13 2026:* the summary of the bhāṣya stands under "Sāyaṇa-bhāṣya — Sāyaṇa's Explanation" as "Summary"; Bhāvārtha is "Gist". | A3, C3 |
| F3 | **Footer.** *Decided Nov 13 2026:* one line such as "Kannada edition p. 235–236 · Maṃ. 3, Anu. 1, Va. 14"; both page numbers when our page holds parts of two original pages. | A4 |
| F4 | **Stray letters.** *Decided Nov 13 2026:* removed from the book and listed in the review list. | B4.2 |
| F5 | **Heading of the edition's English.** *Decided Nov 13 2026:* neutral: "English translation", no name. Whose it is (Wilson, or Wilson adapted by the editor) stays to be verified and is said in the Note on this translation when known. | C6 |
| F6 | **Grammar.** *Decided Nov 13 2026:* Sanskrit ("I think": the user's present view; a change means those sections are translated again). | C8 |
| F7 | **Older volumes.** *Decided Nov 13 2026:* no general clean-up. A volume is brought to these requirements when it is picked up, and only then. | B4 |
| F8 | **Credits.** *Decided Nov 13 2026:* two pages for now: the original's credits, marked as such, and ours. *Still open:* the wording of the thanks and where the method is stated (H1.5). | A2 |
| F9 | **Kannada book.** *Decided Nov 13 2026:* it carries added sūkta and Ṛk headings and page marks. | A5 |
| F10 | **Verse differences.** *Decided Nov 13 2026:* stated in the book (B5.1). | C1 |
| F11 | **Rights (H1.1–H1.3).** Kept as an open point (user, Nov 13 2026): who can be approached for the rights in the edition, the portraits and the reference text; whether a lawyer's view is wanted. It blocks publishing, not building. | H1 |
| F12 | **Length.** *Decided Nov 13 2026:* volumes are not split, for now. *Consequence, open:* several volumes exceed what print-on-demand printers accept (H3.1); this returns when a printer is chosen. | H3 |
| F13 | **Release standard.** *Decided Nov 13 2026:* as proposed: second reading of every page, then 48 pages read by a different model and a sample by a scholar, with no error of meaning left unrepaired. | H2 |
| F14 | **Places that cannot be settled.** *Decided Nov 13 2026:* a plain editorial footnote ("text damaged in the source"). | A1, H2 |
| F15 | **Your preface to the English edition.** Open ("I don't know yet", Nov 13 2026). Until decided: a placeholder page after the Contents and before the original's preface. | A2, H2.4 |
| F16 | **Review copies.** *Decided Nov 13 2026:* `publish/out/` holds final copies only. Review copies stay inside the volume's folder (`volN/review/`). The PDFs in `publish/out/` today are all review copies and move when the new printer is built. | A1 |
| F17 | **Which differences are real.** *Decided Nov 13 2026:* the reference is taken as correct; a difference of the supplied verse is a misreading and gets no footnote, unless the editor records that the printed book really differs. | B5 |
| F18 | **Glosses and `GLOSS` marks.** B3.5 (our edition's Ṛk) and the translator's brief (a quotation the Kannada does not translate is not glossed) differ. Open (T12): is the trial's reading of "gloss" right; are quotations from other works marked too; is a marker added to about 5,100 quoted Ṛks that have no gloss; are "Sense, mine and tentative…" and the bhāṣya-introduction translations glosses. | B3.5, B4.3, C7 |
| F19 | **The legend.** Proposed: one generated legend in every volume (B3.7). Open: all works, or only those cited. | B3, C10 |
| F20 | **A printer's misprint in the published book.** Legacy volumes kept it with `[sic]`; the published book may carry none. How is it shown, if at all? | B4.4 |
| F21 | **Size of the QA sample.** The Handbook: 12 stratified pages plus 12 Special Topics pages. F13: 48 pages. REPO_REVIEW: about 5% of pages. One rule to be chosen. | D8, H2.2 |
| F22 | **Word files.** The Handoff says a Word file is regenerated on request; E says none are kept. Proposed: made on request, not committed. | E |
| F23 | **Spelling of the printed verse** (इन्द्र or इंद्र): the reference and the edition differ. | C1 |
| F24 | **Take the Sāyaṇa-bhāṣya out of the English volumes?** *Decided in principle Nov 21 2026 (user):* whenever a few sūktas are finished in the reader, they are applied to the corresponding volume; **a tool that makes this switch is required** (K7). *Still open:* the setting's design (K7, "I will think about it"). | A3, C3, K7 |
| F25 | **Uṇādi numbering.** The supplied text and the reference edition number the Uṇādi-sūtras differently; which is printed in the reader? | K3 |
| F26 | **Older volumes.** Open: order of the supplied texts; whether to run the free reader measurement first; Vol 13 re-translation or a two-way experiment on 30 pages; whether the old wording is kept where a reader finds nothing; what happens to the old scan-based Vol 11. | Part M |

---

## G. Effect on the volumes already made

*Superseded in part by Part L (one row per volume, Vols 1–21). Corrections of Nov 21 2026: the column "Vols 17, 18, new 11" also holds Vols 19–21 and the finished Vol 11 (which is no longer "new"); Vol 13 is not a legacy volume to be corrected but an unstarted re-translation (decided Nov 11 2026).*

| Requirement | Vols 12, 14–16 | Vols 17, 18, new 11 |
|---|---|---|
| Verse from the reference (B1.2) | to change | to change |
| Transliteration under the bhāṣya (C3) | present (removed in Vol 16 on Nov 12: to restore) | to restore |
| Elaborate summary of the bhāṣya (C3) | short or missing | present |
| New section names (A3) | to change | to change |
| Word-to-word meaning one per line (C4) | partly | present |
| Nothing of ours in the text (B4.1) | many remarks remain | done |
| Stray letters removed (B4.2) | to change | to change |
| References in the text, English abbreviations (B3.1) | to change in the print build | mostly done |
| Original page numbers out of the body, into the footer (A4) | to change in the print build | to change in the print build |
| Front-matter order (A2) | Vol 15 built in the old order | not built yet |

**The scan-based volumes (1–10, 13)** need all of the above and, first, the correction of their reading errors and a Kannada book each (none exists for Vols 2–10 and 13). What goes wrong in them is in `docs/ERROR_KINDS.md`, Part 2; a proposal for doing it at low cost is in `docs/LEGACY_VOLUMES_PLAN.md`. It depends on the supplied machine-read text of those volumes.

---

## H. Publication readiness — what is missing before a volume can be published **NEW**

Parts A–G describe the book. This part lists what a *published* book needs beyond that. It was added on Nov 12 2026 at the user's request ("think carefully as to what we are missing if we want to actually publish these documents soon"). Facts marked *(to verify)* were looked up on the web on Nov 12 2026 from secondary sources and must be confirmed before anyone relies on them; nothing here is legal advice.

**The four items marked BLOCKING stop publication of every volume, however good the text is. They need the user, and probably a lawyer, not more translation work.**

### H1. Rights and permissions

| No. | Requirement | Why | State today |
|---|---|---|---|
| H1.1 **BLOCKING** | **The rights in the 1949–52 Kannada edition are established in writing**: who holds them (the editor's heirs, the Palace, the publisher), and either their permission or evidence that the work is in the public domain. | In India copyright in a literary work lasts for the author's life plus 60 years *(to verify)*. The edition was published 1947–52; its editor H. P. Venkata Rao's year of death was not found. If he died after 1965, the work is still protected. Translating it and, even more, reprinting its Kannada text both need the owner's permission. | Recorded in the repo only as "permissions status — to be confirmed". |
| H1.2 **BLOCKING** | **The source of the accented Saṃhitā may be published.** Either the maintainer of the reference text permits it, or another source with a licence that allows publication is used, or every verse is verified against a public-domain printed edition. | Requirement B1.2 makes the reference text the source of every verse. That text carries the note "personal study and research only, not to be reposted" (`refs/mandala/README.md`). The Vedic text itself is ancient; the terms attach to this digital edition. | Unresolved. Until now only accent marks were taken from it. |
| H1.3 **BLOCKING** | **Portraits and cover art are cleared**: the king's and the guru's portraits, the cover of each volume; and the consent of the present king and present guru before their portraits and names appear (page 5 of the front matter). | Using a living person's portrait and title implies their blessing. | Placeholders. |
| H1.4 | **The English printed under each verse is identified.** If it is H. H. Wilson's (died 1860), it is in the public domain and is credited by name; if it is the edition's own, it falls under H1.1. | The heading "English translation (H. H. Wilson)" rests on the wording only. | Not verified against a Wilson edition. |
| H1.5 **BLOCKING** | **The statement about how the translation was made is decided**, with advice: what the copyright line claims, and where the AI assistance is stated. | The user wants no reference to Claude in the copyright line (A2, page 7). That is the user's choice. Three things follow from it: (a) where copyright is registered, the US Copyright Office requires AI-generated material beyond a trivial amount to be disclosed and protects only the human contribution *(to verify for the current rules; India's position is not settled)*; (b) retailers such as Amazon ask at upload whether a book contains AI-generated content; (c) readers of a sacred text are owed an honest account of the method. A "Note on this translation" can carry it without touching the copyright line. | Open (F8). |
| H1.6 | Fonts are licensed for commercial print and are named in the colophon. | Printers and retailers may ask. | The fonts in use are open-licence families *(to verify per font)*. |

### H2. Editorial readiness

| No. | Requirement | State today |
|---|---|---|
| H2.1 | **No `NOTE` mark, comment or known error in a published book** (A1). Every question in a volume's list is decided by the editor before release; the release build refuses to run while a question is open or a known error is unrepaired. | Counted Nov 20 2026 (`root_tasks_bhr.md`): Vol 17 383 open (88 of 471 decided); Vol 11 471; Vol 18 333. Counts are kept in each `volN/STATUS.md`. |
| H2.2 | **A release standard, stated in numbers:** all checks of Part D pass; the second reading is done; a QA sample of a stated size finds no error of meaning; what was found is repaired. | No volume meets it. The last three samples found 4, 8 and 18 errors. |
| H2.3 | **A scholar of Sanskrit and Kannada reads a sample of every volume** and is named in the book. | The records say "outside expert review still wanted". |
| H2.4 | **A "Note on this translation"** in every volume: the source edition, what is reproduced and what is translated, the transliteration scheme (including the edition's habit of writing the anusvāra, as in "iṃdra"), what is kept as printed, known limitations, how to report an error. | Not written. |
| H2.5 | **One vocabulary for the whole series:** names of deities, seers, metres and ritual terms are spelt and translated the same way in every volume; one English spelling style. | No such list; volumes were made at different times by different models. |
| H2.6 | **Pages missing from the source are obtained or declared**: from a printed copy or a library scan, or stated on the page where they fall. | Missing page marks: Vol 17 six, Vol 18 five, Vol 11 one undecided; Vol 1 pp. 17–24 and Vol 14 pp. 499–500 missing in the source. |
| H2.7 | **Edition and errata:** each PDF carries a version and date; corrections after release are listed; a volume can be rebuilt exactly from the repository. | Not in place. |
| H2.8 | **The series is described:** how many volumes the original has, which are published, what "Volume 17" means to a buyer. | The original Ṛgveda set is described elsewhere as thirty volumes *(to verify)*; the repo holds Vols 1–18. |

### H3. Making the physical book

| No. | Requirement | State today |
|---|---|---|
| H3.1 | **Page count within the printer's limit.** Decide: split each volume into parts, or change the format (larger page, smaller type, word lists in two columns). | Our review PDFs run from 666 to about 1,780 pages (Vol 17 English review copy, `TODO.md`). Print-on-demand limits are roughly 800–1,200 pages depending on printer, paper and binding *(to verify with the printer chosen)*. The restored transliteration under the bhāṣya (C3) makes the books longer still. |
| H3.2 | **A standard page size** offered by the printer. | The build uses 6.5 × 9.5 inches, which is not a common print-on-demand size. |
| H3.3 | **Print-ready files to the printer's specification:** fonts embedded, images at print resolution, inner margin wide enough for a thick book, colour pages decided (portraits). | PDFs are review copies; portraits are scans of unknown resolution. |
| H3.4 | **A full cover:** front, spine and back to the printer's template, with the barcode. | Front cover scans only. |
| H3.5 | **A printed proof is read** before release: accents sitting on their letters, Kannada conjuncts, line breaks inside Sanskrit, page breaks inside a verse. | Only screen images have been looked at. |
| H3.6 | **Finding aids:** contents with our page numbers; running heads showing Maṇḍala and sūkta; a table that leads from Maṇḍala–Sūkta–Ṛk to Aṣṭaka–Adhyāya–Varga and to the page; a list of all volumes. Optional: index of first words of verses, of deities and seers; glossary. | Contents and a sūkta index exist in the build; the rest does not. |
| H3.7 | **Electronic edition decided:** PDF only, or an e-book as well; searchable and accessible text. | Not decided. |

### H4. Registration and distribution

| No. | Requirement | State today |
|---|---|---|
| H4.1 | **A publisher of record**: the user as self-publisher, or an imprint. | `publish/release.json` is empty. |
| H4.2 | **ISBNs:** one for each volume in each format (and for each part, if volumes are split). India's national agency issues them to Indian citizens free of charge *(to verify; the per-volume and per-format rule is to be confirmed with the agency)*. | None. |
| H4.3 | **Legal deposit:** copies delivered to the National Library, Kolkata, and three other public libraries within 30 days of publication *(to verify)*. | — |
| H4.4 | **Catalogue data for each volume:** title, series, volume, contributors and their roles (Sāyaṇa, the Kannada editor, the translator), languages, subjects, description, price. | Not written. |
| H4.5 | **How it is sold or given:** channel, price, and whether a free edition exists beside the printed one; the licence a reader receives. | Not decided. |

### H5. Standing of the work
- H5.1 A sacred text and a royal and monastic foundation are named on the first pages. The book must not suggest an endorsement that was not given (H1.3).
- H5.2 The commentary's and the 1950 editor's views are reproduced, not ours; the Note on this translation says so.

### H6. The shortest sound route to a first published volume (proposal)
1. Settle H1.1–H1.3 and H1.5 first. They take calendar time, cost no translation work, and decide whether the Kannada book can be published at all.
2. Answer the open questions of Part F, so that the format is fixed once.
3. Choose **one pilot volume** already translated from the supplied text (Vol 17 or 18) and bring it to the release standard (H2.2): standard structure, second reading, editor's decisions on its `NOTE` list, a scholar's sample.
4. Choose the printer and page size (H3.1–H3.2), build, read a printed proof.
5. Register (H4) and release. Then the same route for the other volumes, with the format no longer changing.

---

## I. Second reading **NEW**

*Draft Nov 21 2026, from `docs/ERROR_KINDS.md` (kind codes H1–H43, S1–S26 are those of that file) and `docs/DESIGN.md` §5.4. Not yet decided by the user.*

### I1. Purpose
- I1.1 The second reading finds the errors that no script can: errors of **meaning**, and errors in **Sanskrit that makes no sense**. Layout, numbers, references, accents and letters of another script are settled by structure and script checks (Part D), not by a reader.
- I1.2 The user's priority (Nov 21 2026): the English is mostly accurate; **the glaring errors are in the Sanskrit** (the grammar section composed from the Kannada, and misread words in the supplied Sanskrit). The readers for Sanskrit (R2, R3) therefore rank equal with the reader for English (R1).
- I1.3 Every reader returns **findings only**, never a rewritten text. A reader never changes the supplied text (B1).

### I2. The readers
One reader is one instruction with one input and one list of error kinds. They are run separately, so that each can be measured and each can be given to a different model.

| Reader | Reads | Against | Looks for | Kinds |
|---|---|---|---|---|
| **R1 Meaning** | the English of a unit | the Kannada of the unit | reversed roles or wrong attribution; wrong word or term; opposite sense; addition (a gloss or fact the Kannada does not have); omission of words, a sūtra or a closing line inside a piece; a misprint silently put right; the bhāṣya summarised against Sāyaṇa; a printed number missing or supplied from memory; words lost at a page break; an odd reference kept without a note; a quotation given in English only or shortened; a leftover remark or a missing `NOTE` | H8, H14, H16 (English part), H25–H30, H33, S2, S3, S14–S16 |
| **R2 Grammar** | the Sanskrit of the grammar section (composed from the Kannada) | the Kannada grammar section | a word that is not a real form; a word that does not match the Kannada word it renders; derivation, root, suffix or sūtra dropped or invented; sūtras left out | H31, S18 |
| **R3 Sanskrit sense** | the Devanagari of the supplied bhāṣya, quotations, Pada-pāṭha and word meanings | itself, the Ṛk, the Pada-pāṭha, the reference text (for settling only) | a word that is not a word (misread letters such as त्म/त्र); a letter pattern of a known typeface trap; a proposed reading with its basis | H24, S7, S9 (and S11 where text was completed from memory) |
| **R4 Gist** (Vol 17 onwards) | the English Gist | the Devanagari bhāṣya block | "does the block say this?" and "is everything in the block rendered?" for each sentence; the grammatical tail is not required | H30 for the Gist form |
| **R5 Words** | the word-to-word meanings and the deviations noted | the Kannada word meanings, the Pada-pāṭha | a meaning that differs from the Kannada; a deviation of the Pada-pāṭha not mentioned (user, Nov 12) | H29, S7 |
| **R6 Kannada text** | the Kannada of each unit as supplied (prose, names, word meanings, Pada-pāṭha in Kannada script where present) | itself in context: the sentence, the Ṛk, the Sanskrit beside it | a word that is not a Kannada word (broken conjunct, stray vowel sign); a real word that makes no sense where it stands; a name or term misread for a look-alike (for example Lāgākṣi read Laugākṣi); Kannada vowel signs carried into Devanagari; a proposed reading with its basis | H24, S7, S9, S13 |

The abbreviation check (H12, H13, S6: a form not in `rv/references.tsv`, for example "si" for "ni") is a **script** check (D6); a reader may report one it sees, but is not relied on for it.

### I3. How a reader works
- I3.1 Work is cut into **packets** (DESIGN §4): a numbered list of units with their text. The answer is a file of findings with the same numbers.
- I3.2 A finding has: unit number; **kind code** from `ERROR_KINDS.md`; the words concerned, quoted from the unit; what the reader would write instead; and its **basis** (the Kannada words, the Ṛk, the Pada-pāṭha). A finding without a basis is a question, not an error.
- I3.3 Two questions per sentence for R1 and R4: does the source say this? is everything in the source rendered?
- I3.4 A reader that finds nothing marks the unit "read by R*n*, model, date". A volume is "second-read" only when every unit carries the mark of every reader that applies to it (R2 only where the unit has a grammar section, R4 only from Vol 17; R6 every unit).
- I3.5 Every packet reports how many units it compared (D, last line). Unread units are "not read", never "clean".

### I4. What is done with a finding (DESIGN §5.4, extended)
| Finding | Settled by |
|---|---|
| R1: different wording proposed, unit small | translated again with the finding as a hint, read once more. One round only. |
| R2: wrong or missing Sanskrit | the grammar section of that unit is composed again with the finding as a hint; read once more by R2. One round only. |
| R3: a misread word with a certain reading | recorded as a reading (supplied letters → reading → basis, as in `bhashya_readings.tsv`); the supplied text is **not** altered |
| R3: not certain | `**NOTE**{question}` for the editor |
| R6: a corrupted Kannada word with a certain reading | recorded as a reading (supplied letters → reading → basis); the supplied text is **not** altered, and the Kannada book is changed only by a logged repair after the editor decides (HR2) |
| R6: not certain, or a name or term that may be a valid look-alike | `**NOTE**{question}` for the editor, settled against the print |
| Still disagreed, or a question of judgement | a question for the editor, with both wordings |
| A fault of the supplied text | list for the editor (H34–H37) |

### I5. Measurement before a reader is trusted
- I5.1 Each reader is **measured on pages with known errors**, as was done for R1 on 72 pages of Vol 12 (18 known errors: Sonnet found 10, Haiku 7, about 13,500 agent tokens a page). The share of known errors found is the reader's score, written into the design.
- I5.2 **R2, R3 and R6 have never been measured.** There is no answer key for them. First step: the user marks real and false findings on a sample (one sūkta with grammar sections, one volume of supplied bhāṣya, a sample of Kannada pages for R6); the real ones become the key.
- I5.3 A cheaper model is used only if its score is as good. Models are compared on the same sample, with cost, before any volume is run.
- I5.4 The release standard (F13, H2.2) stays: second reading of every page, then 48 pages read by a different model and a sample by a scholar.

### I6. Limits (stated so that nobody relies on more than the reader can give)
- I6.1 **A reader sees only the supplied text.** A misreading shared by the Kannada and the Sanskrit of the supplied text is invisible unless it makes a non-word. Only the user, with the print, can settle such a place.
- I6.2 **One reading finds about half.** Where a kind matters (I1.2), two readers of different models are used.
- I6.3 **A reader's Sanskrit and Kannada are not authority.** R6 finds non-words and words that do not fit; it cannot see a misread that gives another valid name or term.  R2, R3 and R6 findings are proposals; the composed Sanskrit of the grammar remains the editor's to read before release (CLAUDE.md rule 1).
- I6.4 **Cost is estimated, not measured.** About a third to a half of translation for R1 (DESIGN §7). No figure for R2–R6. Nothing is sent to the API before the user has seen the estimate; every reader must be runnable by agents as well.

### I7. Not built yet
The packets, the findings file, the marks of I3.4, the instructions for R2–R6, and the measurements of I5. Until they are, D2 is carried out by hand or by the Vol 12 method.

## J. Human reading **NEW**

*Draft Nov 21 2026. Gathers what Parts B, D, F, H and I say about the people who read; adds nothing the user has not decided except where marked "proposed".*

### J1. Readers
| Role | Who | Reads |
|---|---|---|
| Editor | the user | the `NOTE` list; places where the supplied text and the print may differ; the composed Sanskrit of the grammar sections; the release PDF |
| Scholar | a reader of Sanskrit and Kannada, not yet named (H2.3) | a sample of every volume |
| Proof reader | the editor, or a person the editor names (H3.5) | the printed proof of one volume |

### J2. Readings
| No. | Reading | Reader | Produces | Source |
|---|---|---|---|---|
| HR1 | Decide every `NOTE` question | Editor | a decision per question in `volN/review/notes.tsv`, carried out as a logged repair | B4.3, H2.1 |
| HR2 | Settle places a model reader flagged and only the print can settle (shared misreads, verse differences, damaged source) | Editor | decision: reading, "edition differs" (`verse_decisions.tsv`), or "text damaged in the source" | B5.2, F14, I6.1 |
| HR3 | Read the composed Sanskrit of each grammar section against the Kannada | Editor, or a Sanskrit reader the editor names | accepted, or a correction with its reason | C8, I6.3 |
| HR4 | Mark a sample of a model reader's findings real or false | Editor | the answer key for that reader | I5.2 |
| HR5 | Scholar's sample | Scholar | a list of errors by kind code | H2.3, F13 |
| HR6 | Proof the printed book | Proof reader | a list of faults of layout and script | H3.5 |
| HR7 | Release reading | Editor | approval, or a list of faults | A1, D9 |

### J3. Recording
- J3.1 A reading counts only if it is recorded in a file of the volume's folder, with the reader's role, the date and the number of items compared. A unit nobody read is "not read", never "clean" (Part D).
- J3.2 A decision never alters the supplied text; it is carried out as a logged repair (`volN/review/repair_log.md`, E).
- J3.3 Every finding carries a kind code of `docs/ERROR_KINDS.md` and a basis (the Kannada words, the print page, the Ṛk or the Pada-pāṭha); without a basis it is a question.
- J3.4 *Proposed:* the editor's decision is final for its place; a finding of the scholar or the proof reader is a proposal until the editor accepts it.
- J3.5 *Proposed:* a sample that finds an error is followed by a sample twice its size (the checklist asks for it; it was not run for Vol 18 or the new Vol 11).

## K. The Sāyaṇa-bhāṣya reader **NEW**

*Drafted Nov 21 2026 from `sayana_bhr.md`, `tools/rv/BHASHYA_BRIEF.md`, `docs/BHASHYA_RUN.md` and the user's statement of Nov 21 2026 that the bhāṣya in Devanagari, transliteration and full English meaning is to be a separate book, made in its own session. Item T14 of `PUBLICATION_TODO.md`. The facts of the state are those of the record of Nov 18–20 2026 and are not recounted.*

### K1. What the book is
- K1.1 A by-product book, **"Sāyaṇa's Ṛgveda-bhāṣya in English: reader"**. For each Ṛk it holds: the Saṃhitā-pāṭha, the Pada-pāṭha, Sāyaṇa's bhāṣya in **Devanagari**, its **transliteration**, and the **full English** of Sāyaṇa's text.
- K1.2 It holds nothing else: no Kannada commentary of Venkata Rao, no word meanings, no printed English, no Special Topics. The volumes remain Venkata Rao's voice; the reader is Sāyaṇa's own.
- K1.3 It is **built from the volumes by script**: Sanskrit layers are selected by line, never rewritten, and the output is checked line by line against the volume. The English of the bhāṣya is the only text written for the book.

### K2. Content and order of a Ṛk
Sūkta introduction of Sāyaṇa where the print has one; then for each Ṛk, in this order: Saṃhitā-pāṭha (from the reference, B1.2), Pada-pāṭha, bhāṣya in Devanagari, its transliteration (made at print, B2.2), English of the bhāṣya. The grammatical part at the end of the bhāṣya is translated too, in Sāyaṇa's order. An optional `## Readings` section lists misread words and the reading translated (B1.6).

### K3. Rules for the English of the bhāṣya
1. **A direct translation of Sāyaṇa's Sanskrit, not of the Kannada.** The translator is given the Devanagari only (Saṃhitā, Pada, bhāṣya), not the Kannada commentary, Venkata Rao's word meanings, or Wilson.
2. **Complete and in his order.** Nothing added, nothing dropped, nothing shifted: no fact from memory; a word Sāyaṇa does not gloss is not glossed; his gloss is given, not the dictionary's; each epithet stays with its noun; voice, causatives, particles (एव, अपि, यदि) and possessives are kept.
3. **Sanskrit is copied, never typed.** A citation stands between `⟦ ⟧`, letter for letter; a script adds the transliteration and checks that every citation is in the unit. A citation holds the word or rule only, never Sāyaṇa's connecting prose, and the sense of a cited root stands in the English. No Devanagari outside the citations.
4. **References** are copied in Devanagari, to be turned into the series' abbreviations by script from the one list (B3.2). A printed number is kept as printed (B1.5). *Open (F25):* the Uṇādi numbering of the supplied text and of the reference edition differ.
5. **Misreadings.** The supplied Sanskrit has many misread letters. Where the intended word is certain (from the Ṛk, the Pada-pāṭha, grammar and context, or the reference text) it is translated and logged in `## Readings`; where not, a `**NOTE**{question}` marks the place. A difference of content between the supplied text and the reference text always gets a `NOTE`; a difference of wording, or of Uṇādi numbering, does not. The supplied text is never altered.
6. **Missing text.** A sūkta introduction or a Ṛk's bhāṣya that the supplied text lacks but the reference edition has is marked with a `NOTE`; nothing is added.
7. **No remarks.** Remarks of a volume's translator inside a bhāṣya block are left out of the reader; the volume is unchanged.

### K4. Making and checking
- K4.1 One file per sūkta, `volN/bhashya_en/M<m>_S<sss>.md`. It must pass `publish/bhashya_check.py` (form: every citation is in the unit letter for letter, transliteration present, nothing outside the rules). The check cannot judge meaning; it is known to accept very short citations too loosely and not to see Roman-letter sūtra names.
- K4.2 **The model matters.** Measured on this work (`sayana_bhr.md` §6): a Sonnet draft made four errors of meaning in nine Ṛks where Fable made none; a Fable second reading of eight Sonnet sūktas (93 Ṛks) made 242 corrections, 73 of them changing what a reader would understand Sāyaṇa to say; a dispatcher's spot reading and the agent's own self-check under-count badly. A sūkta drafted by Sonnet and re-read by Fable cost about 330,000 tokens, one drafted by Fable about 200,000.
- K4.3 **Therefore:** every sūkta is read a second time by a model that did not write it, and the model of each step is recorded in `volN/parts/bhashya_costs.md`. The reading asks, per sentence: does the block say this? is everything in the block rendered? Its findings are settled as in I4. How the remaining sūktas are best made is open (the user is considering a better way; the figures above are the evidence to design from).
- K4.4 **Human reading:** a scholar of Sanskrit reads a sample of the reader (HR5). A reading of Sāyaṇa that is the translator's or a reader's proposal is not authority (I6.3).
- K4.5 Questions for the editor go to `volN/review/bhashya_notes.tsv`; every reading logged goes to `volN/review/bhashya_readings.tsv`.
- K4.6 References copied before the reference corrector changed the supplied text must be brought to the corrected forms by script, not by hand (the check currently fails 139 citations in 43 of 55 files for this reason).

### K5. Building
- K5.1 `publish/bhashya_book.py` writes the reader as Markdown, HTML or PDF, for one sūkta, some, or a volume. Where the English of the bhāṣya exists it is printed; where it does not, the book **says so** and shows the volume's Gist, never presenting an unfinished sūkta as finished.
- K5.2 The volume's own Grammar list (made from the Kannada) is left out where Sāyaṇa's grammar is translated.
- K5.3 The book carries a coverage statement: which sūktas have English, which are made, read and checked.
- K5.4 The book is a reading copy until the release standard (H2) is met for it, and carries the rights position of H1; it holds none of the 1949–52 edition's commentary (K1.2), but the supplied Sanskrit and the accented verses fall under H1.2.

### K6. The reader needs, to be complete
**The switch tool of K7**; a stable address for every Ṛk (Maṇḍala.Sūkta.Ṛk), shown in the reader and used by the volumes; the reader's own copy of the Sanskrit blocks, checked line by line against the volume; support for the older layouts (Vols 1–10, 12, 14, 15), which the script cannot read yet; the two known gaps of the check (K4.1).

### K7. How a volume refers to the reader — the switch
*Principle decided Nov 21 2026 (user, F24): as sūktas are finished in the reader they are applied to the corresponding volume; the tool for this switch is a requirement. The design below is a proposal; the user will return to it (not decided).*

- K7.1 `volcfg.json` gets a setting, **`bhashya`**: `block` (the volume prints Sāyaṇa's Devanagari block with its Gist, as now) or `reference` (the volume prints one line per Ṛk, "Sāyaṇa: bhāṣya reader M.S.R", with the page of the reader).
- K7.2 **The data are never deleted.** The blocks and Gist stay in the units and files, which the audits and gates (`tools/rv/batch.py`) expect; the setting changes only what is printed. The Kannada book is unchanged either way.
- K7.3 **Per-sūkta fallback.** `reference` takes effect for a sūkta only where the reader holds that sūkta's English, checked (K4.1) and second-read (K4.3). Elsewhere the block and Gist are printed.
- K7.4 The Special Topics stay in the volume; they analyse the bhāṣya in Venkata Rao's voice.
- K7.5 The default is `block`. Whether any volume is set to `reference` is F24. A trial is a **copy** of one volume (Vol 11, where both exist) built as a review PDF, with no original changed.
- K7.6 *Requirement of the tool (user, Nov 21 2026):* it takes the sūktas finished in the reader (K4.1 and K4.3 passed) and switches exactly those in the corresponding volume, reports which sūktas it switched and which it left, and can switch a sūkta back; it works from the data and never deletes them (K7.2).
- K7.7 *Not built:* the printer (`rv/printer.py`) has no such setting today; the section is identified in the units by its label, so a print-time filter is small. The cost of making the whole reader is not known; the measured figure is about 11,000 tokens per Ṛk (second readings included), which for the whole Saṃhitā would be of the order of 100 million tokens (an extrapolation that uses an unverified count of Ṛks).

### K8. State (Nov 20 2026, from `sayana_bhr.md`)
55 of 143 sūktas of the volumes the script can read have English (Vol 11: 21 of 21; Vol 16: 33 of 33; Vol 17: 1 of 41, the pilot 3.40; Vol 18: none). 43 of the 55 files fail the check (K4.6). The other 88 sūktas of Vols 17 and 18 are not started. Counts live in `volN/review/` and `volN/parts/`, not here.

---

## L. The volumes **NEW**

*One row per volume. Stable facts only: counts of open items live in each `volN/STATUS.md`. From the status files of Nov 21 2026; figures are theirs. Families: **L1** legacy scan (read from images, older layouts); **L2** older html form (agent flow, remarks kept); **L3** transitional (Vol 16); **L4** the Vol 17 form (`NOTE`, bhāṣya block in Devanagari only, grammar in Sanskrit, sub-headings).*

| Vol | Scope | Source | Family | Standing deviations and gaps |
|---|---|---|---|---|
| 1 | Pūrva-pīṭhikā, Bhāṣya-bhūmikā, Maṇḍala 1 Sū. 1–2 | scans; supplied text in 3 files (pp. 1–720) | L1 | pp. 17–24 missing in the source; 148 pages without Sanskrit; Kannada file made from the HTML form, to be remade from the markdown; a separate Gaps file inserted at build time (to be merged); supplies the portraits and bibliography for all volumes |
| 2 | Maṇḍala 1 Sū. 3–19, Aṣṭaka 1 Adhyāya 1 | scans; supplied text whole (pp. 2–808) | L1 | the user's second reading is trusted, not re-translated; `[?]` and `[sic]` kept by the user's decision; accents replaced from the reference for 176 Ṛks |
| 3 | Maṇḍala 1 Sū. 20–32, Adhyāya 2 | scans; supplied text whole (pp. 2–647) | L1 | Sū. 29 Ṛk 6–7 and Sū. 30 (pp. 452–517) were once written without the page images and are to be redone from the supplied text |
| 4 | Maṇḍala 1 Sū. 33–46, Adhyāya 3 | scans; supplied text whole (pp. 2–608) | L1 | accent doubts; GLOSS markers |
| 5 | Maṇḍala 1 Sū. 47–61, Adhyāya 4, Pariśiṣṭa | scans; supplied text pp. 2–708 in 7 files | L1 | pp. 273–286 and 584 stand in two files; the user's readings for pp. 578–625 not applied |
| 6 | Maṇḍala 1 Sū. 62–80, Adhyāya 5 | scans; supplied text whole (pp. 2–619) | L1 | p. 82 a separate file; numeral rows await the user |
| 7 | Maṇḍala 1 Sū. 81–94, Adhyāya 6 | scans only | L1 | no supplied text yet; numeral file of the user |
| 8 | Maṇḍala 1 Sū. 95–112, Adhyāya 7 | scans (and an alternate scan on a branch) | L1 | no supplied text yet; numeral differences; about 280 flagged pages |
| 9 | Maṇḍala 1 Sū. 113–121, Adhyāya 8 | scans | L1 | no supplied text yet; numeral differences |
| 10 | Maṇḍala 1 Sū. 122–136, Aṣṭaka 2 Adhyāya 1 | scans (purged from the tree) | L1 | no supplied text yet; Kannada script inside the English file; the user's numeral files cover the first 200 PDF pages only |
| 11 | Maṇḍala 1 Sū. 137–157, Aṣṭaka 2 Adhyāya 2 | supplied text (re-translated); the old scan version is kept as such | L4 | p. 211/212 undecided; ten sūkta introductions lacking in the supplied text; front matter is title and credits only |
| 12 | Maṇḍala 1 Sū. 158–165, Adhyāya 3 | supplied text (p. 1 absent) | L2 | many "as supplied" remarks; Saṃhitā lines unaccented; no second reading |
| 13 | Maṇḍala 1 Sū. 166–183 (expected), Adhyāya 4 | **not yet supplied**; old scan text in `vol13/legacy/` | planned L4 | to be re-translated (decided Nov 11 2026), not corrected |
| 14 | Maṇḍala 1 to Maṇḍala 2 Sū. 23, Adhyāyas 5–6 | supplied text (p. 1 and pp. 499–500 missing) | L2 | pp. 499–500 missing in the source; several sūkta and Ṛk headings missing |
| 15 | Maṇḍala 2 Sū. 24–43, Maṇḍala 3 Sū. 1–6, Adhyāyas 7–8 | supplied text | L2 | baseline of the older html form; front matter built in the old order; p. 235 missing, pp. 495–496 truncated |
| 16 | Maṇḍala 3 Sū. 7–39, Aṣṭaka 3 Adhyāyas 1–2 | supplied text (p. 1 absent) | L3 | about 70 sentences with broken punctuation (undecided: repair or undo); remarks remain; bhāṣya transliteration removed; possible missing text at six places |
| 17 | Maṇḍala 3 Sū. 40–62, Maṇḍala 4 Sū. 1–18, Adhyāyas 3–5 | supplied text | L4 (pilot) | six pages without head; printed-English label "English translation (H. H. Wilson)"; pilot for the release standard |
| 18 | Maṇḍala 4 Sū. 19–58, Maṇḍala 5 Sū. 1–8, Adhyāyas 6–8 | supplied text | L4 | label "Printed English" kept (user, Nov 11); front matter partly built |
| 19 | Maṇḍala 5 Sū. 9–62, Aṣṭaka 4 Adhyāyas 1–3 | supplied text | L4 (agent route) | in translation in another session; preface untranslated |
| 20 | Maṇḍala 5 Sū. 63–87 with Pariśiṣṭa, Maṇḍala 6 Sū. 1–28, Adhyāyas 5–6 | supplied text, 2 files joined by hand | L4 (agent route) | p. 339 has no text; OCR-damaged sūkta numbers; `**GLOSS**` for unexplained quotations; imprint placeholders |
| 21 | Maṇḍala 6 Sū. 29–75, Maṇḍala 7 Sū. 1–19, Adhyāyas 7–8 and Aṣṭaka 5 Adhyāyas 1–2 | supplied text, 2 files joined | L4 (agent route) | no reference verses yet for Maṇḍalas 6–7, so B1.2 cannot be met; no abbreviations list |

- L.1 Each volume's own `STATUS.md` is the only place for its changing state (E).
- L.2 A volume is brought to these requirements when it is picked up, and only then (F7).
- L.3 Pages without a running head are not chased (B6.4); the printed-English label differs between volumes until F5 is applied everywhere.

---

## M. Older volumes (1–10) **NEW**

*From `docs/LEGACY_VOLUMES_PLAN.md`, `docs/LEGACY_SCAN_WORKFLOW.md` and `docs/DESIGN.md` §7. A proposal, not decided; the open points are F26.*

- M1 **They depend on the supplied machine-read text.** Vols 1–6 have it; Vols 7–10 and 13 do not yet. Nothing below can be done for a volume without it.
- M2 **Three sieves**, each cheaper than the next: (1) by script, no model: the Kannada book from the supplied text; the Saṃhitā from the reference; Sanskrit blocks, references and figures from the source and not from the old English; (2) a reader that only reports (Part I), run on what remains; (3) correction only where something was found.
- M3 **The Kannada book** of Vols 2–10 and 13 is made by script from the supplied text (A5).
- M4 **Numbers** are settled from the user's numeral file (treated as always correct) or from the supplied text. A number is replaced only where its old value is found once and unambiguously; the rest are listed (never "corrected" by a pattern applied at many places).
- M5 **Alignment.** The old English is laid into the units where it can be aligned; units that cannot be are translated again. Whether the old wording is kept where a reader finds nothing is F26.
- M6 **Legacy conventions to convert** (each with its removed text logged, B4.5): `[?]` and `[sic]` (to `NOTE`, B4.3), "as supplied", glosses labelled "mine and tentative" (to `**GLOSS**`, B3.5), grammar as a 2–4 line English note (to the Sanskrit of C8), bhāṣya as a Gist of 25 words or fewer (to C3).
- M7 **Rules of the scan period** that hold for any volume still read from images: if an image view returns no image, stop and report, never write that page; the Kannada digit key (2/3/7, 3/5, 6/7, 8/9); the numeral method of Oct 2026 (two machine readers agreeing; the eye only where they differ).
- M8 **Vol 13** is not corrected but re-translated (decided Nov 11 2026); its old text is kept in `vol13/legacy/`. **Old Vol 11** (scan-based) is replaced by the re-translation.

## N. The form of a volume, stated completely **NEW**

*Nov 21 2026. This part describes, without reference to any other volume, exactly what a volume of the current form contains and in what order. It was written from the Vol 17 files (the pilot of the form) and states what those files show; Parts A and C give the same matter in outline and are to be brought into line with it. Names in the working files (the "data names") differ in some places from the names printed in the book; both are given. Anything the original print does not have is not made up: "where the original has it" means the part is present only then.*

### N1. The order of a volume
1. **Front matter** (A2): cover, portraits, scholars, credits, copyright, contents, the translator-editor's preface, the abbreviations (B3.7).
2. **Preface of the original edition** ("Preface (Pīṭhike)" in the working file): the whole text, translated, in the order of the print.
3. **Opening of the volume:** the invocation line of the original ("Om. Śrī 1. …"), the verses that stand at its head, the title line of the volume ("Ṛgveda Saṃhitā with Sāyaṇa's commentary, Part N"), the statement of which chapters, Maṇḍalas and sūktas it holds, and the introduction to the first chapter, all as the original prints them.
4. **The body:** one Maṇḍala heading wherever a Maṇḍala begins; then its sūktas in order (N2); the introduction of a new chapter (adhyāya) stands before its first sūkta.
5. **Closing:** the colophon and closing verses of the last chapter, with the closing line of the original and its Kannada closing mark, nothing added (A3, B6).
6. The book ends with the original's last words; no remark of ours follows.

### N2. A sūkta
A sūkta begins with its heading, "Sūkta N (Maṇḍala M)", and holds, in this order:
1. **Sāyaṇa's introduction to the sūkta**, where the original has it: his Sanskrit block in Devanagari (the label "॥ सायणभाष्यम् ॥ (Sāyaṇa-bhāṣya)"), followed by its **Gist of the bhāṣya** in English.
2. **The Kannada introduction** of the sūkta ("Anuvāda"), in English, where the original has it.
3. **The particulars** of the sūkta, in one line, in this form: Maṇḍala; Anuvāka; Sūkta; Aṣṭaka; Adhyāya; Varga(s); number of Ṛks in the sūkta; seer; deity; metre. A sentence in the original that states the same is kept as translated; the line is added where the original gives the facts in a table or in running text.
4. **The Ṛks**, in order (N3).
5. Anything the original prints after the last Ṛk of the sūkta (a closing remark, a note, a colophon) in its place.

### N3. A Ṛk
A Ṛk begins with its heading, "Ṛk N", and holds these parts, each under its own sub-heading, in this order. A part is present only where the original has it, except 1 to 3, 5, 6 and 8, which every Ṛk has.

| No. | Part | Working-file label | Printed label | Content |
|---|---|---|---|---|
| 1 | Verse | ॥ संहितापाठः ॥ (Saṃhitā-pāṭha) | Saṃhitā-pāṭha | the verse, accented, from the reference text (B1.2): Devanagari, then its transliteration in italics, one line per pāda, the closing "॥ N ॥" with the Ṛk number |
| 2 | Word-text | ॥ पदपाठः ॥ (Pada-pāṭha) | Pada-pāṭha | the words of the verse separated by "।", ending "॥ N ॥", Devanagari then transliteration; unaccented |
| 3 | Commentary | ॥ सायणभाष्यम् ॥ (Sāyaṇa-bhāṣya) | Sāyaṇa-bhāṣya — Sāyaṇa's Explanation | Sāyaṇa's Sanskrit for this Ṛk in Devanagari, as supplied, set as a quotation; **no transliteration under it in the working file** (the reader of Part K carries it) |
| 4 | Summary of the commentary | Gist of the bhāṣya | Summary | English: an elaborate summary that covers most of the block (the grammatical tail need not be explained); it states who is addressed, the use (viniyoga) with its sūtra, the gloss of each word, every alternative, each authority with its reference |
| 5 | Word meanings | प्रतिपदार्थ (Pratipadārtha) | Word-to-word meaning | one word per line: the Sanskrit word in Devanagari, its transliteration in italics in brackets, a dash, its meaning in English |
| 6 | Sense | भावार्थ (Bhāvārtha) | Gist | the sense of the verse in English, from the Kannada |
| 7 | English of the edition | English translation (label as decided, F5) | English translation | the English the original prints under the verse, reproduced |
| 8 | Special topics | विशेषविषयगळु (Special Topics) | Special Topics | the original's notes on the Ṛk, in English; see N5 |
| 9 | Grammar | Grammar | Grammar (Vyākaraṇa-prakriyā) | where the original has it; see N6 |

If the commentary of one Ṛk is long, parts 3 and 4 may alternate: a block of the commentary, then its summary, then the next block, then its summary; the order of the blocks is the order of the original.

### N4. Rules for the parts
1. **Verse (1) and Pada-pāṭha (2):** every akṣara is set apart in the printed book (C1); the verse and the Pada-pāṭha are never merged into the text of another part; a verse quoted in running text is not printed as a verse block and carries no accents of its own.
2. **Commentary (3):** the Sanskrit is copied letter for letter from the supplied text by script; the translator never types it. Where the supplied text holds a misread letter, the book prints it as supplied and the intended reading is logged (B1.6).
3. **Summary (4):** a Sanskrit word cited in it is copied from the commentary block, printed in Devanagari with its transliteration in italics in brackets, followed by its sense. A paragraph states what Sāyaṇa says, not what the translator thinks. The summary of a block that holds only grammar says so in one sentence and does not repeat the grammar.
4. **Word meanings (5):** one word per line, as a list, in the order the original prints them; the words are those the original lists, none added and none dropped.
5. **Sense (6):** follows the Kannada; where Sāyaṇa and the Kannada differ it follows Sāyaṇa and the place gets a `NOTE` (B5.4).
6. **English of the edition (7):** reproduced as printed, in the original's English, with its own spelling and punctuation; it is never altered to agree with the Sense.
7. **Quotations in any English part:** every Sanskrit quotation is given in full in Devanagari, followed by its transliteration in italics in brackets, and its reference in the text in the form of B3. The translator places a quotation by copying it from the Kannada text; he never types Sanskrit.

### N5. Special topics
1. It is the original's discussion, in English, in the order of the original, each topic opening with the Sanskrit word or phrase it discusses (Devanagari and transliteration), then a dash, then the explanation.
2. Every Sanskrit quotation in it follows N4.7, with its reference.
3. A Ṛk quoted from elsewhere in the Saṃhitā is glossed as B3.5 says; until that gloss exists a `**GLOSS**` marker stands (working files only, B4.3).
4. A reference to another part of the same work ("explained earlier in part 11, p. 633") is kept as the original has it.

### N6. Grammar
1. Present only where the original has a grammar section for the Ṛk.
2. It is in **Sanskrit**, composed by the translator from the Kannada, written in the working file in Kannada script inside `⟪ ⟫` and printed in Devanagari only; there is no English in it.
3. **One word per line**: the headword in Devanagari, a dash, then its derivation: the root and its sense, the suffix or rule, the form, the accent where the commentary names it. Sūtra texts, roots and references are copied from the commentary letter for letter.
4. It is complete: no derivation in the Kannada is dropped and none is added.
5. No script can check composed Sanskrit; it is read by the editor (HR3) and by the grammar reader (R2).

### N7. Page marks and breaks
1. The page of the original is marked "Printed p. N" at the exact place where that page begins, even in the middle of a sentence or a block; the page marks of the preface are in Roman numerals.
2. A Ṛk that runs over a page break is not repeated: where a page of the original begins inside its parts, the mark stands there and the text goes on; when a part of the Ṛk continues after another part (N3, last paragraph), the heading reads "Ṛk N (continued)".
3. In the printed book the page marks do not stand in the body; they move to the footer (A4).
4. A page of the original with no running head is the first page of a sūkta, a Maṇḍala or a chapter; it is not a missing page.

### N8. Marks and remarks
1. The English holds no remark of ours: no "as supplied", no bracketed comment, no `[?]`, no `[sic]`.
2. A place that needs the editor's decision carries `**NOTE**` immediately after the words concerned, with its question in the volume's list (B4.3); a place whose gloss is a placeholder carries `**GLOSS**`.
3. A printed number, Sanskrit word or reference is never corrected from memory; where the print has no number, none is written.

### N9. Files
1. The English file ends with exactly one line: **Progress note:** Done through printed p. N.
2. The Kannada file holds the text of the original with its Sanskrit in Kannada script and the headings and page marks of A5, and no more.
3. Every Ṛk of the original appears once, in order, and the Saṃhitā of each is the reference's (B1.2, D3).

## Appendix: where each requirement comes from

| Requirement | Source |
|---|---|
| A2 (preface to the English edition); A1 two layers, D9 release gate | user, Nov 12 2026 (later messages) |
| B5.1 (difference of the edition's verse stated in the book) | user, Nov 13 2026 |
| A2, A4, B1.2–3, B2.1 (bhāṣya), B3, B4.1–2, B5, C1 (number check), C3, C4, new names in A3, A5 | user's review comments, Nov 12 2026 |
| A3 sub-headings; akṣara spacing; B4.3; elaborate summary; B2.3 | user decisions, Nov 11 2026 |
| C9, C11, Om on the first page of Ṛks | user decisions, Vol 15 review, Nov 9 2026 |
| A1, B1.1, B1.4, B2.2, B6, E | standing rules (`CLAUDE.md`, `docs/HANDBOOK.md` §2, §7, §8, §11) |
| D1, D2 | agreed in principle in the session of Nov 12 2026 |
| D3–D8 | existing checks and the lessons of Vols 17, 18, 11 (`docs/LESSONS.md`) |
| N | the Vol 17 files (`vol17/Rigveda_Samhita_Vol17_English_Translation.md`, `volcfg.json`, `rv/printer.py`), read Nov 21 2026 |
| K, L, M; additions to B–F | survey of the repository's documents, Nov 21 2026 (`CLAUDE.md`, `HANDBOOK`, `LESSONS`, `BRIEF`, `BHASHYA_BRIEF`, `DESIGN`, `LEGACY_*`, `TODO`, `PUBLICATION_TODO`, `sayana_bhr.md`, `reference_bhr.md`, volume `STATUS.md` files); user, Nov 21 2026 (bhāṣya in Devanagari, transliteration and full English belongs in a separate book) |
| H | added Nov 12 2026 at the user's request; facts marked *(to verify)* from a web search of that day |
| I (second reading) | user, Nov 21 2026 (Sanskrit errors are the glaring ones); `docs/ERROR_KINDS.md`; `docs/DESIGN.md` §5.4; F13 |
| J (human reading) | Parts B, D, F, H, I as cited; J3.4 and J3.5 proposed Nov 21 2026 |
