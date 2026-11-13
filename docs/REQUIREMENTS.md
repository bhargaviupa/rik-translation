# Requirements — Ṛgveda-saṃhitā (Kannada edition) in English

**Draft 3, Nov 12 2026 — for the user's review. Nothing in the tools or volumes has been changed to match it.**
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

Marks used: **NEW** = differs from the volumes made so far. **(F3)** = see open question 3 in Part F. The source of every requirement is listed in the appendix; the user's review comments of Nov 12 are kept verbatim in `docs/review/USER_REVIEW_2026-11-12.md`.

---

## A. Volume structure

### A1. What is delivered for each volume
1. **English book** — PDF, with its `.html` and `.md`.
2. **Kannada book** — PDF and `.md`: the text of the original, matching it closely in content. (F9)
3. **Review lists** for the editor: places that need a decision, deviations from the reference text, repairs made, results of the checks.

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

### B2. Sanskrit
1. Sanskrit is given in three layers: Devanagari, transliteration (IAST), English. This now includes the Sāyaṇa-bhāṣya again. **NEW** for Vols 16–18
2. Devanagari and transliteration are made by script from the supplied text. The translator does not type them.
   **Transliteration is made when the book is printed and is not stored in the volume files** (user decision, Nov 11 2026, recorded on the branch `claude/dreamy-cerf-z4h3f4`; it now covers the Sāyaṇa-bhāṣya too, by the comment of Nov 12).
3. No Kannada script in the English book: not in headings, references or abbreviations.

### B3. References and abbreviations
1. References stand **in the text**, where the original has them, written with **English abbreviations**. **NEW** (Many were moved to footnotes.)
2. **One list for all volumes** gives every work cited: the Kannada form in the print, the English form we use, the full title. It starts from the bibliography of Vol 1 (PDF p. 39), which is to be checked for completeness.
3. The same list records the **known mistakes**: misprints of the original, misreadings of the machine text (for example the letter read "si" is "ni" = Nirukta), and mistakes of the translation.
4. Every volume uses exactly the abbreviations of that list.

### B4. Nothing of ours in the text
1. **No text about the making of the file:** no status lines at page breaks, no "the Sāyaṇa-bhāṣya from p. 235 continues here", no remarks on how the print looks.
2. **Stray letters and words** of the supplied text (loose figures, page signatures, fragments) are removed. **NEW** (They were kept and noted.) (F4)
3. **One mark only** for a place that needs the editor's decision: `NOTE`, **in the working files only**. Its question is in the volume's review list. No `[?]`, no `[sic]`, no "as supplied". The published book shows none of it (A1). (F7)

### B5. Deviations
1. **The verse.** The book prints the Saṃhitā of the reference text (B1.2). **Where the Saṃhitā of the Kannada edition reads differently, the book says so, under the verse** (decided by the user, Nov 13 2026): Sāyaṇa's commentary, the Pada-pāṭha and the word meanings follow the edition's verse, so a reader must be able to see what they are explaining. This is part of the book, not a comment of ours; it is the one kind of editorial note the published book carries as a rule.
2. **A difference that the edition itself settles is settled by script** (user, Nov 13 2026, after checking the differences word by word): where the Pada-pāṭha or the word meanings of the same Ṛk have the reference form, the supplied verse is a misreading of the machine text; the reference stands and no footnote is printed. **Every other difference is mentioned in a footnote on the Ṛk and is not corrected**, worded so that it claims no more than is known ("the Kannada edition, as machine-read, has …"). All differences, with how each was settled, are in `volN/review/source_faults.tsv`.
3. **Pada-pāṭha, Word-to-word meaning, Sāyaṇa-bhāṣya.** These are given as the edition has them and are never altered to agree with the reference verse. Where they disagree with it beyond what item 1 already states, it is listed for the editor. (F1, second half)

### B6. Completeness
1. Every page, every sūkta and every Ṛk of the original is present once, in order.
2. Nothing is added that the original does not have, apart from the headings of Part A and the English itself.

---

## C. Specific rules (one section each)

### C1. Saṃhitā-pāṭha
- Text from the reference (B1.2), with accents.
- Every akṣara set apart, in every volume (the look piloted in Vol 17).
- The Ṛk number is checked against the reference: none missing, none misplaced.
- Where the edition's verse differs from the reference: stated under the verse (B5.1), once confirmed (B5.2).

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

### C7. Special Topics
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
| D9 | **Release gate:** the release PDF is built only when D1–D8 pass, no `NOTE` is open, and no known error is listed as unrepaired; it is checked for any leftover mark, bracketed comment or working text. | A1, H2 |

Each check reports how many items it compared. A volume that was not checked is "not checked", never "clean".
D1 and D2 are agreed in principle; how they work is for the design document.

---

## E. Working rules (unchanged)
- Finished text is changed only by logged repairs.
- Work is committed and pushed; no force-push; `main` only when the user asks.
- API money is spent only after the user has seen the estimate.
- Rights, ISBN and publisher live only in `publish/release.json`.
- Built PDFs are kept in the repository (`publish/out/` for final copies) and every rebuild is committed; page scans are not (user decision, Nov 12 2026). **Word files and built HTML are not kept; a volume folder holds its `.md` files and what they are made from, not built copies** (user decision, Nov 13 2026).
- The reference texts are for private study; the repository stays private.
- Reports say what was verified and how.

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
| F17 | **Which differences are real.** *Decided Nov 13 2026:* not settled for now. Every difference is mentioned in a footnote on the Ṛk; none is corrected or confirmed; the question is parked in `TODO.md`. | B5 |

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
| H2.1 | **No `NOTE` mark, comment or known error in a published book** (A1). Every question in a volume's list is decided by the editor before release; the release build refuses to run while a question is open or a known error is unrepaired. | Vol 17: 472 open; Vol 18 and new Vol 11: several hundred each. |
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
| H3.1 | **Page count within the printer's limit.** Decide: split each volume into parts, or change the format (larger page, smaller type, word lists in two columns). | Our PDFs run from 666 to 1,645 pages. Print-on-demand limits are roughly 800–1,200 pages depending on printer, paper and binding *(to verify with the printer chosen)*. The restored transliteration under the bhāṣya (C3) makes the books longer still. |
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
| H | added Nov 12 2026 at the user's request; facts marked *(to verify)* from a web search of that day |
