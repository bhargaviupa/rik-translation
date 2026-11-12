# Requirements — Ṛgveda-saṃhitā (Kannada edition) in English

**Draft 2, Nov 12 2026 — for the user's review. Nothing in the tools or volumes has been changed to match it.**
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

Marks used: **NEW** = differs from the volumes made so far. **(F3)** = see open question 3 in Part F. The source of every requirement is listed in the appendix; the user's review comments of Nov 12 are kept verbatim in `docs/review/USER_REVIEW_2026-11-12.md`.

---

## A. Volume structure

### A1. What is delivered for each volume
1. **English book** — PDF, with its `.html` and `.md`.
2. **Kannada book** — PDF and `.md`: the text of the original, matching it closely in content. (F9)
3. **Review lists** for the editor: places that need a decision, deviations from the reference text, repairs made, results of the checks.

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
| next | Preface / Introduction | As the volume has it. No Kannada headings. | supplied file |
| next | Abbreviations | The volume's list, with Sanskrit in place of the Kannada text. | supplied file |

Vol 15 was built in another order (preface before the guru's portrait); it is to be corrected.
The credits of the original edition are either marked clearly as taken from the original or combined with our own credits page. (F8)

### A3. Body

**First page of the Ṛks:** an Om picture at the top.

**A Maṇḍala** begins with its heading. **A sūkta** begins with its heading, followed by what the original prints before the first verse (Sāyaṇa's introduction, the Kannada introduction, the particulars of the sūkta).

**A Ṛk** has these parts, in this order, each under its own sub-heading:

| No. | Part | Heading in the English book | In short (details in Part C) |
|---|---|---|---|
| 1 | Verse | **Saṃhitā-pāṭha** | from the reference text, accented, every akṣara set apart; transliteration |
| 2 | Word-text | **Pada-pāṭha** | as supplied; transliteration |
| 3 | Commentary | **Sāyaṇa-bhāṣya — Sāyaṇa's Explanation** **NEW** | Sanskrit, transliteration **NEW**, then an elaborate English summary (F2) |
| 4 | Word meanings | **Word-to-word meaning** **NEW** (was Pratipadārtha) | one word per line |
| 5 | Sense | **Gist** **NEW** (was Bhāvārtha) | English |
| 6 | English of the edition | heading to be settled (F5) | reproduced from the original |
| 7 | Topics | **Viśeṣa-viṣaya** **NEW** (was Viśeṣaviṣayagaḷu) | English, with quotations and references |
| 8 | Grammar | **Grammar (Vyākaraṇa-prakriyā)** | (F6) |

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

### B2. Sanskrit
1. Sanskrit is given in three layers: Devanagari, transliteration (IAST), English. This now includes the Sāyaṇa-bhāṣya again. **NEW** for Vols 16–18
2. Devanagari and transliteration are made by script from the supplied text. The translator does not type them.
3. No Kannada script in the English book: not in headings, references or abbreviations.

### B3. References and abbreviations
1. References stand **in the text**, where the original has them, written with **English abbreviations**. **NEW** (Many were moved to footnotes.)
2. **One list for all volumes** gives every work cited: the Kannada form in the print, the English form we use, the full title. It starts from the bibliography of Vol 1 (PDF p. 39), which is to be checked for completeness.
3. The same list records the **known mistakes**: misprints of the original, misreadings of the machine text (for example the letter read "si" is "ni" = Nirukta), and mistakes of the translation.
4. Every volume uses exactly the abbreviations of that list.

### B4. Nothing of ours in the text
1. **No text about the making of the file:** no status lines at page breaks, no "the Sāyaṇa-bhāṣya from p. 235 continues here", no remarks on how the print looks.
2. **Stray letters and words** of the supplied text (loose figures, page signatures, fragments) are removed. **NEW** (They were kept and noted.) (F4)
3. **One mark only** for a place that needs the editor's decision: `NOTE`. Its question is in the volume's review list. No `[?]`, no `[sic]`, no "as supplied". (F7)

### B5. Deviations
Where the Pada-pāṭha, the Word-to-word meaning or the Sāyaṇa-bhāṣya of the supplied text deviates, it is mentioned, not silently altered. (F1)

### B6. Completeness
1. Every page, every sūkta and every Ṛk of the original is present once, in order.
2. Nothing is added that the original does not have, apart from the headings of Part A and the English itself.

---

## C. Specific rules (one section each)

### C1. Saṃhitā-pāṭha
- Text from the reference (B1.2), with accents.
- Every akṣara set apart, in every volume (the look piloted in Vol 17).
- The Ṛk number is checked against the reference: none missing, none misplaced.
- Where the supplied verse differs from the reference in a letter: (F10).

### C2. Pada-pāṭha
- As supplied, with transliteration.
- A deviation is mentioned (B5).

### C3. Sāyaṇa-bhāṣya — Sāyaṇa's Explanation
- The Sanskrit as supplied, with its transliteration. **NEW**
- Followed by an **elaborate summary in English** that covers most of the commentary. The grammatical tail need not be explained.
- A deviation is mentioned (B5).

### C4. Word-to-word meaning
- Each word on its own line, with its meaning.

### C5. Gist
- The sense of the verse in English, from the Kannada.

### C6. English of the edition
- Reproduced from the original. Heading: (F5).

### C7. Viśeṣa-viṣaya
- English. Every Sanskrit quotation in three layers, with its reference in the text (B3.1).

### C8. Grammar
- (F6): Sanskrit rendering as begun in Vol 17, or English.

### C9. Contents
- In English, as in Vol 1; the page numbers shown are those of our book.

### C10. Abbreviations page
- The volume's own list, with Sanskrit in place of the Kannada, and in agreement with the one list of B3.2.

### C11. Preface / Introduction
- Translated in full. No Kannada headings.

---

## D. Checks (when is a volume done?)

| No. | Check | Covers |
|---|---|---|
| D1 | The structure of Part A is produced by script, not written by the translator. | A2, A3 |
| D2 | Every page is read a second time against the Kannada: numbers and references, names, negations, omissions, additions. | B1, B6 |
| D3 | Ṛk numbers against the reference: every Ṛk present once, in order. | C1, B6 |
| D4 | Every Sanskrit block under the heading of its own part. | A3 |
| D5 | Same number of verses in the English and the Kannada book; no page without its mark. | B6 |
| D6 | Every abbreviation is in the one list. | B3 |
| D7 | Nothing of B4 left in the text; no Kannada script in the English book. | B2, B4 |
| D8 | A sample of pages read by a different model; findings repaired and logged. | all |

Each check reports how many items it compared. A volume that was not checked is "not checked", never "clean".
D1 and D2 are agreed in principle; how they work is for the design document.

---

## E. Working rules (unchanged)
- Finished text is changed only by logged repairs.
- Work is committed and pushed; no force-push; `main` only when the user asks.
- API money is spent only after the user has seen the estimate.
- Rights, ISBN and publisher live only in `publish/release.json`.
- The reference texts are for private study; the repository stays private.
- Reports say what was verified and how.

---

## F. Open questions for the user

| No. | Question | Concerns |
|---|---|---|
| F1 | **Deviations.** Deviation from what — the reference verse (a word spelt differently from the Saṃhitā)? And is the mention a line in the book, or an entry in the review list only? | B5, C2, C3 |
| F2 | **Two "Gists".** If Bhāvārtha becomes "Gist", what is the summary of the bhāṣya called? Proposal: it stands under "Sāyaṇa's Explanation" as "Summary". | A3, C3 |
| F3 | **Footer.** One line such as "Kannada edition p. 235 · Maṃ. 3, Anu. 1, Va. 14"? When one of our pages holds parts of two original pages, both numbers? | A4 |
| F4 | **Stray letters.** Removed without trace, or removed from the book and listed in the review list? | B4.2 |
| F5 | **Heading of the edition's English.** "English translation (H. H. Wilson)" rests on the wording only and is not verified. | C6 |
| F6 | **Grammar.** Keep the Sanskrit rendering begun in Vol 17, or English? | C8 |
| F7 | **Older volumes.** Do B4.1–B4.3 apply to Vols 1–16 by clean-up, or only when a volume is redone? (The Vol 16 trial showed that removing remarks by script damages sentences.) | B4 |
| F8 | **Credits.** One combined page or two? Wording of the thanks; where the AI assistance is mentioned once it leaves the copyright lines. | A2 |
| F9 | **Kannada book.** May it carry our added sūkta and Ṛk headings and page marks, or the original text only? | A5 |
| F10 | **Verse differences.** When the supplied verse differs from the reference, is the difference listed for the editor? | C1 |

---

## G. Effect on the volumes already made

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

The scan-based volumes (1–10, 13) are not in this table: what they need depends on F7 and on the error list (`docs/ERROR_KINDS.md`, in preparation).

---

## Appendix: where each requirement comes from

| Requirement | Source |
|---|---|
| A2, A4, B1.2–3, B2.1 (bhāṣya), B3, B4.1–2, B5, C1 (number check), C3, C4, new names in A3, A5 | user's review comments, Nov 12 2026 |
| A3 sub-headings; akṣara spacing; B4.3; elaborate summary; B2.3 | user decisions, Nov 11 2026 |
| C9, C11, Om on the first page of Ṛks | user decisions, Vol 15 review, Nov 9 2026 |
| A1, B1.1, B1.4, B2.2, B6, E | standing rules (`CLAUDE.md`, `docs/HANDBOOK.md` §2, §7, §8, §11) |
| D1, D2 | agreed in principle in the session of Nov 12 2026 |
| D3–D8 | existing checks and the lessons of Vols 17, 18, 11 (`docs/LESSONS.md`) |
