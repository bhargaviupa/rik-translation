# Requirements — Ṛgveda-saṃhitā, Kannada edition → English (DRAFT for the user's review)

**Status: draft, Nov 12 2026. Nothing in the tools or volumes has been changed to match it.** Until the user approves it, the rules in force are still `CLAUDE.md`, `docs/HANDBOOK.md` and `tools/rv/BRIEF.md`. Once approved, this file is the one place for *what* the work must deliver; those files then only say *how*, and point here.

Where each requirement comes from is given in brackets: **[U Nov 12]** = the user's review comments of Nov 12 2026 (`docs/review/USER_REVIEW_2026-11-12.md`, verbatim); **[U Nov 11]**, **[U Nov 9]** = earlier user decisions recorded in the repo; **[rule]** = a standing rule of `CLAUDE.md` / `HANDBOOK.md`. **CHANGE** marks a requirement that differs from what the volumes made so far do. **OPEN** marks a point the user still has to decide (collected in §9).

## 1. What is delivered, per volume
- R1.1 An **English book** (PDF, with its `.html` and `.md` source): the whole volume translated, in the order of the original. [rule]
- R1.2 A **Kannada book** (PDF + `.md`): the text of the original. It **matches the original closely in content**. [U Nov 12] — so nothing of ours stands in it except headings needed to find a sūkta or a Ṛk. OPEN 9.9
- R1.3 **Review lists** for the editor: places needing a decision, deviations from the reference text (§3), repairs made, the result of the checks (§7). [rule]
- R1.4 All volumes look and behave the same: one set of section names, one layout, one front-matter order, one list of abbreviations. A volume that differs is brought into line or is listed as not conforming. [U Nov 12, the concern that volumes deviate]

## 2. Sources and which one governs
- R2.1 **The user's machine-read text** (`volN/html/`) is the base for everything except the Saṃhitā-pāṭha and the portraits: text, cover, contents, board of scholars, preface, abbreviations. [U Nov 12; rule]
- R2.2 **The Saṃhitā-pāṭha is always taken from the reference text** (the accented Maṇḍala files, `refs/mandala/`), not from the supplied text. **CHANGE** (until now the supplied letters were kept and only the accent marks were added from the reference). [U Nov 12]
- R2.3 Where the **Pada-pāṭha, the Pratipadārtha or the Sāyaṇa-bhāṣya** of the supplied text deviates, **we mention it**; we do not silently alter those sections. [U Nov 12] OPEN 9.1 (deviates from what, and where the mention stands)
- R2.4 **Portraits come from Vol 1 for every volume** (king: Vol 1 p. 4; guru: Vol 1 p. 5). [U Nov 12]
- R2.5 No letter or number of the supplied text is "corrected" from memory or from another edition, except as R2.2 says. A place that cannot be settled is marked for the editor (R4.6). [rule]
- R2.6 The translator never types Devanagari or transliteration; scripts make them from the supplied text. [rule]

## 3. The text of a Ṛk (English book)
Each Ṛk has these parts, in this order, each under its own sub-heading. [U Nov 11 for sub-headings; names U Nov 12]

| Part | Heading in the English book | Content |
|---|---|---|
| Verse | Saṃhitā-pāṭha | from the reference (R2.2), accented, **every akṣara set apart**, in every volume [U Nov 11, Nov 12]; transliteration under it |
| Word-text | Pada-pāṭha | as supplied; transliteration under it |
| Commentary | **Sāyaṇa-bhāṣya — Sāyaṇa's Explanation** **CHANGE** | Devanagari **with its transliteration (IAST)** **CHANGE** (removed in Vols 16–18, now required again), followed by an **elaborate gist** in English |
| Word meanings | **Word-to-word meaning** (Pratipadārtha) **CHANGE** | **one word per line** with its meaning |
| Sense | **Gist** (Bhāvārtha) **CHANGE** | English |
| English of the edition | the English printed in the original | reproduced; heading OPEN 9.5 (Wilson attribution unverified) |
| Topics | **Viśeṣa-viṣaya** (Sanskrit form, not the Kannada "Viśeṣaviṣayagaḷu") **CHANGE** | English; every Sanskrit quotation in Devanagari + transliteration + English, with its reference |
| Grammar | Grammar (Vyākaraṇa-prakriyā) | OPEN 9.6 (Sanskrit rendering as in Vols 17–18, or English) |

- R3.1 Two parts would now both be called "Gist" (the gist of the bhāṣya and the Bhāvārtha). OPEN 9.2
- R3.2 Sanskrit is given in three layers everywhere: Devanagari, transliteration, English. [rule; R3 table restores it for the bhāṣya]
- R3.3 **The Ṛk numbers are checked against the reference**: every Ṛk of every sūkta present once, in order, under its own number; none missing, none misplaced (this failed in Vol 18 and Vol 17). [U Nov 12]
- R3.4 A new Maṇḍala and every sūkta has its heading; the last sūkta of an adhyāya ends with the colophon and closing lines of the original, nothing added. [rule]

## 4. What must not be in the text
- R4.1 **No text of ours about the making of the file**: no status lines at page breaks, no "the Sāyaṇa-bhāṣya from p. 235 continues here", no "window ends", no remarks on how the print looks. [U Nov 12; U Nov 11]
- R4.2 **The page numbers of the original are not in the body of the page.** **CHANGE** (they are now printed as "p. N" marks). [U Nov 12]
- R4.3 The running head of the original (page number, Maṇḍala–Anuvāka–Varga) **goes to the footer** of our page, so that a reader can still find the page of the Kannada book. [U Nov 12] OPEN 9.3 (exact form)
- R4.4 **References are in the text, not in footnotes**, and are written with **English names/abbreviations, not Kannada**. **CHANGE** (many were moved to footnotes in the Vol 15 build). [U Nov 12]
- R4.5 **Stray letters and words** of the supplied text (page signatures, loose figures, fragments) are **removed**. **CHANGE** (they were kept and noted). [U Nov 12: "guess we should remove"] OPEN 9.4 (are they listed somewhere?)
- R4.6 A place that needs the editor's decision carries one mark only, `NOTE`, and its question is in the volume's list. No `[?]`, `[sic]`, "as supplied". [U Nov 11] OPEN 9.7 (does this hold for the older volumes too)
- R4.7 No Kannada script in the English book (headings, references, abbreviations). [U Nov 11; U Nov 12 for headings and abbreviations]

## 5. References and abbreviations
- R5.1 **One place** collates every work cited and its abbreviation: the Kannada form in the print, the English form we use, the full title. The starting point is the bibliography of Vol 1 (PDF p. 39), to be checked for completeness. [U Nov 12]
- R5.2 The same place records the **common mistakes**: of the original (misprints of an abbreviation), of the machine reading (e.g. the letter read "si" is "ni" = Nirukta; "mi./ma./pu. saṃ." = Ṛ. Saṃ.), and of the translation. [U Nov 12; existing `tools/rv/refs_fix.py`]
- R5.3 **Every volume uses exactly the abbreviations of that list.** A check reports any abbreviation in a volume that is not in it. [U Nov 12]
- R5.4 The volume's own page of abbreviations is given in the book with **Sanskrit (Devanagari) in place of the Kannada text**. [U Nov 12]

## 6. The book: order of the front matter (same in every volume)
[U Nov 12; replaces the order of `HANDBOOK.md` §8 — Vol 15's order is wrong and is to be corrected]

| Page | Content | Source |
|---|---|---|
| P1 | Cover picture with **this volume's number in Kannada**; one English line below with the volume number, Maṇḍala, Aṣṭaka (as Vol 15) | supplied file of the volume |
| P2 | Portrait of the king | Vol 1 p. 4 |
| P3 | Portrait of the guru, with the English translation of its text | Vol 1 p. 5 |
| P4 | List of scholars | as Vol 15 p. 6 |
| P5 | Present king and present guru: placeholders | — |
| P6 | Translation credentials: **new layout, half page picture and half page text** (like Vol 15 p. 2) | new design |
| P7 | Copyright, ISBN and the like; **no reference to Claude in the copyright**; a **Thank-you section** | `publish/release.json` |
| P8 … | Contents in English, as in Vol 1 | supplied file |
| then | Preface or Introduction, as the volume has it; **no Kannada headings** | supplied file |
| then | Abbreviations (R5.4) | supplied file |
| then | Start of the Ṛks, **an Om picture at the top** | — |

- R6.1 The credits of the original edition: either marked clearly as taken from the original, or combined with our own credits page. OPEN 9.8
- R6.2 Where the thanks and the mention of the AI assistance stand, once it leaves the copyright lines. OPEN 9.8

## 7. Checking (what "done" means for a volume)
- R7.1 **The structure is made by script**, not by the translator: page breaks, sūkta and Ṛk headings, section labels and Sanskrit blocks come from the Kannada file; the translator supplies English only. (Agreed in principle Nov 12; design to follow.)
- R7.2 **Every page is read a second time** against the Kannada, for numbers and references, names, negations, omissions and additions. (Agreed in principle Nov 12; design to follow.)
- R7.3 Whole-volume checks, each of which **prints how many items it compared**: Ṛk numbers against the reference (R3.3); every block under its own label; Saṃhitā count equal in both books; pages without a heading; abbreviations against the list (R5.3); nothing of R4 left in the text.
- R7.4 A sample of pages is read by a different model, and its findings are repaired and logged. [rule]
- R7.5 Reports say what was checked and how; a volume that was not checked is "not checked", never "clean". [rule; lesson of Nov 12]

## 8. Working rules (unchanged, listed for completeness)
Finished text is changed only by logged repairs; work is committed and pushed; no force-push; `main` only when the user asks; API money is spent only after the user has seen the estimate; rights, ISBN and publisher live only in `publish/release.json`; the reference texts in `refs/mandala/` are for private study and the repository stays private. [rule]

## 9. Open questions for the user
1. **R2.3, deviations.** For the Pada-pāṭha there may be a reference to compare with; for the Pratipadārtha and the bhāṣya we have none. Does "deviation" mean (a) these sections disagree with the reference Saṃhitā (a word spelt differently from the verse), or (b) something else? And is the mention a line under the section, or an entry in the review list only?
2. **R3.1, two Gists.** If Bhāvārtha becomes "Gist", what is the gist of the bhāṣya called? Proposal: "Sāyaṇa's Explanation — summary" for the bhāṣya, "Gist" for the Bhāvārtha.
3. **R4.3, footer.** One line per page of ours such as "Kannada edition p. 235 · Maṃ. 3, Anu. 1, Va. 14"? When one of our pages holds parts of two original pages, both numbers?
4. **R4.5, stray letters.** Removed without trace, or removed from the book and listed in the review list?
5. **Heading of the edition's own English.** "English translation (H. H. Wilson)" rests on the wording only; not verified.
6. **Grammar sections.** Keep the Sanskrit rendering begun in Vol 17, or English?
7. **Older volumes.** Do R4.1, R4.5 and R4.6 apply to Vols 1–16 as they are, by clean-up, or only when a volume is redone? (The Vol 16 trial showed that removing remarks by script damages sentences.)
8. **Credits (R6.1, R6.2).** One combined page or two; and the wording of the thanks.
9. **Kannada book (R1.2).** May it carry our added sūkta and Ṛk headings and page marks, or the original text only?
10. **Scope of the Saṃhitā rule (R2.2).** When the supplied verse differs from the reference in a letter, is the difference listed for the editor?

## 10. What changes for volumes already made (summary of the CHANGE marks)
| Requirement | Vols 12, 14–16 | Vols 17, 18, new 11 |
|---|---|---|
| Saṃhitā from the reference (R2.2) | change | change |
| Transliteration under the bhāṣya (R3) | have it (Vol 16 removed Nov 12) | **restore** |
| Elaborate gist of the bhāṣya | short or missing | have it |
| New section names (R3) | change | change |
| Word-to-word meaning one per line | partly | have it |
| No remarks of ours (R4.1) | many remain | done |
| Original page numbers out of the body, into the footer (R4.2–4.3) | change (print build) | change (print build) |
| References in the text, English names (R4.4) | change (print build) | mostly done |
| Stray letters removed (R4.5) | change | change |
| Front-matter order (R6) | change (Vol 15 built in the old order) | not built yet |
