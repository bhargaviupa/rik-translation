# Publishing Vols 1, 2 and 3 — the to-do list

*The one file to open for the state of publication. Last updated: **Nov 17 2026**.*
*Kept current by every session that works on these volumes: a finished point is ticked with its date, a new point is added where it belongs. Counts are from commands run on the date given; estimates are called estimates. Background: `docs/REQUIREMENTS.md` (Part H), `docs/DESIGN.md`, `docs/LEGACY_VOLUMES_PLAN.md`. Other parked points of the project: `TODO.md`.*

Marks: `[ ]` open · `[~]` begun · `[x]` done · **(you)** only the user can do it · **(script)** costs nothing · **(agents)** uses the session allowance · **(scholar)** / **(advice)** someone outside.

---

## 1. Where the three volumes stand today

| | Vol 1 | Vol 2 | Vol 3 |
|---|---|---|---|
| Contents | Pūrva-pīṭhikā, Sāyaṇa's Bhāṣya-bhūmikā, Maṇḍala 1 Sūktas 1–2; printed pp. 1–720 | Maṇḍala 1 Sūktas 3–19 | Maṇḍala 1 Sūktas 20–32; printed pp. 1–647 |
| English | 238,000 words, read from page scans | 322,000 words, from scans | 233,000 words, from scans |
| Doubt marks `[?]` in the English | 104 (+ 14 in the gaps file) | 432 | 110 |
| `[sic]` marks | 0 | 143 | 37 |
| Supplied machine-read text in the repo | **yes** (`vol1/html/`, 3 files) | **no** | **no** |
| Kannada book | text made from the supplied text; not yet in the book format | none | none |
| Checked against the supplied text | 9 pages of 720 (12 corrections); lists made by script for 481 pages, not yet read | not possible yet | not possible yet |
| PDF | old build, review copy | old build, review copy | old build, review copy |
| Known faults on record | pp. 17–24 missing in the source; about 59 best-effort places; chapter headings with unresolved numbers; four page ranges live in a separate "gaps" file | old progress notes and a Cyrillic string inside the text; varga numbers not reconciled with the colophons | Sūktas 29–30 (pp. 452–517) were redone once after image failures |

**Vol 2 (user, Nov 17 2026):** translated and read a second time from the scans by the user and in good condition; page numbers correct; many `[?]` are remarks of ours or questions inside the content and can go; the accents were made without the reference and are to be verified. **Not to be re-translated for now.** Its clean-up runs in its own session: `vol2/CLEANUP_PROMPT.md`.

**None of the three can be published as it is.** The text was read from scans, where about a quarter of the numbers compared so far differed from your numeral files, and no page of Vols 2–3 has been compared with a second source.

---

## 2. What I need from you (nothing below can replace these)

| No. | What | Needed for | State |
|---|---|---|---|
| U1 | **Machine-read text of Vol 2 and Vol 3** (as for Vols 11–19), uploaded to `vol2/html/`, `vol3/html/` | the Kannada books; correcting numbers and Sanskrit by script; the reading against the Kannada | [ ] |
| U2 | **Rights in the 1949–52 Kannada edition** in writing: who holds them, and permission or proof of public domain | publishing anything at all | [ ] |
| U3 | **Permission for the accented verses** (the reference text says "personal study only"), or another source that may be published | every verse in every volume | [ ] |
| U4 | **Portraits and cover**: the old king's and guru's portraits from Vol 1 cleared; the present king's and guru's pictures, names and consent; credentials picture | front matter pp. 2–6 | [ ] |
| U5 | **Statement of how the translation was made** and the copyright line, with advice | copyright page | [ ] |
| U6 | **Your preface** to the English edition (one per volume, or one for the series) | front matter | [ ] |
| U7 | **Publisher of record, ISBNs** (one per volume and format), price, how it is sold | copyright page, cover barcode | [ ] |
| U8 | **Printer and page size**; split long volumes or not (Vol 1's old PDF has about 1,250 pages, beyond most print-on-demand limits) | final layout, cover spine | [ ] |
| U9 | **A scholar of Sanskrit and Kannada** to read a sample of each volume, named in the book | release standard | [ ] |
| U10 | **Decisions on the questions** each volume will raise (Vol 17 raised 471) | no open question may be printed | [ ] |
| U11 | Decisions still parked that change the look of all volumes: spelling of the verse (इन्द्र or इंद्र), layout of the pages before the preface, whether the edition's English is H. H. Wilson's | fixing the format once | [ ] |

U2–U5 take calendar time and need no translation work: they can start today.

---

## 3. The work, in order — per volume

The route is the approved design: the Kannada book and the structure come from the supplied text by script; the existing English is laid into that structure; numbers and Sanskrit are corrected from the supplied text; the English is then read against the Kannada; you decide the questions; the book is built.

### Step 1 — Supplied text and Kannada book
| | Vol 1 | Vol 2 | Vol 3 |
|---|---|---|---|
| 1.1 Supplied text in the repo **(you)** | [x] Nov 11 | [ ] | [ ] |
| 1.2 Pages checked: every printed page found, missing numbers listed **(script)** | [x] | [ ] | [ ] |
| 1.3 Kannada text made from it **(script)** | [x] prose pp. 1–605, Ṛk part from p. 606 | [ ] | [ ] |
| 1.4 Verses taken from the reference; the Kannada verse corrected from it **(script)** | [ ] | [ ] English side by the clean-up session; the shared accent tool does not read Vol 2's layout yet | [ ] |
| 1.5 Front matter read: title pages, board, preface, contents, abbreviations **(script + agents)** | [ ] | [ ] | [ ] |

### Step 2 — Structure and the existing English laid into it
| | Vol 1 | Vol 2 | Vol 3 |
|---|---|---|---|
| 2.1 Volume cut into units (sūkta, Ṛk, part) **(script)** | [ ] needs a new kind of unit: 605 pages are continuous prose with chapters, not sūktas (**tool work**) | [ ] | [ ] |
| 2.2 Old English placed into the units; proof that every paragraph is placed once **(script)** | [ ] Vol 1 also has to take in the gaps file (pp. 95–167, 191–205, 261–283, 288–295) | [ ] | [ ] |
| 2.3 What cannot be placed is listed; those passages are re-translated **(agents)** | [ ] | [ ] | [ ] |

*Risk, not yet tried:* the old volumes use older headings and labels than Vol 17. How much of the English places cleanly is unknown until one volume is tried. If much of it does not, re-translating that volume from the supplied text may be cheaper than repairing it (as was decided for Vols 11 and 13).

### Step 3 — Corrections that need no reading of meaning
| | Vol 1 | Vol 2 | Vol 3 |
|---|---|---|---|
| 3.1 Pada-pāṭha, bhāṣya and quoted Sanskrit replaced by the supplied text's **(script)** | [ ] | [ ] | [ ] |
| 3.2 Numbers and references compared and corrected where the place is certain; the rest listed **(script)** | [~] 20 one-digit corrections made; 461 candidates listed | [ ] | [ ] |
| 3.3 Abbreviations brought to the one list (`docs/REFERENCES.md`) **(script)** | [ ] | [ ] | [ ] |
| 3.4 `[?]`, `[sic]`, remarks, old progress notes: each settled from the supplied text, or turned into a question for you **(script + agents)** | [~] 1 settled | [ ] by the clean-up session (remarks removed, no supplied text needed) | [ ] |
| 3.5 Layout brought to the agreed form: section names, word meanings one per line, no page marks in the body **(script)** | [ ] | [ ] | [ ] |

### Step 4 — Reading the English against the Kannada
| | Vol 1 | Vol 2 | Vol 3 |
|---|---|---|---|
| 4.1 Every page read once by a second reader that only lists faults **(agents, or API)** | [ ] | [ ] | [ ] |
| 4.2 Listed faults corrected, each logged **(agents)** | [~] 9 pages | [ ] | [ ] |
| 4.3 Sample read by stronger readers; errors found are repaired and the sample doubled if any are of meaning **(agents)** | [ ] | [ ] | [ ] |

*Cost, estimate:* about 13,500 agent tokens per page read (measured on Vol 12), so roughly 9–10 million tokens for a volume of 700 pages; by the Batch API about $0.01 a page (not measured). A Sonnet reader found 10 of 18 known errors in the test: one reading does not find everything.

### Step 5 — Your decisions
| | Vol 1 | Vol 2 | Vol 3 |
|---|---|---|---|
| 5.1 Question list given to you as a spreadsheet **(script)** | [ ] | [ ] | [ ] |
| 5.2 You answer; answers carried out and logged **(you, then agents)** | [ ] | [ ] | [ ] |
| 5.3 No question, remark or known error left in the text **(script gate)** | [ ] | [ ] | [ ] |
| 5.4 Pages missing in the source obtained or declared | [ ] pp. 17–24 | [ ] not known yet | [ ] not known yet |

### Step 6 — The books
| | Vol 1 | Vol 2 | Vol 3 |
|---|---|---|---|
| 6.1 Front matter in the agreed order, with your preface, contents with our page numbers, abbreviations | [ ] | [ ] | [ ] |
| 6.2 "Note on this translation" (source, what is reproduced, transliteration, known limits) | [ ] | [ ] | [ ] |
| 6.3 Review copies, English and Kannada, in `volN/review/` **(script)** | [ ] | [ ] | [ ] |
| 6.4 Scholar's sample read; findings repaired **(scholar)** | [ ] | [ ] | [ ] |
| 6.5 Final PDFs to the printer's specification in `publish/out/`; full cover with spine and barcode | [ ] | [ ] | [ ] |
| 6.6 Printed proof read by you (accents, conjuncts, page breaks) **(you)** | [ ] | [ ] | [ ] |
| 6.7 ISBN, legal deposit, catalogue data, release | [ ] | [ ] | [ ] |

---

## 4. Work on the tools, once for all three

| No. | What | State |
|---|---|---|
| T1 | Units for continuous prose with chapters (Vol 1 pp. 1–605): structure, import and printing | [ ] |
| T2 | Import of the older English layouts (headings and labels of Vols 1–3) into units | [ ] |
| T3 | Replacement of scan-read Sanskrit and numbers from the supplied text, with a list of what could not be settled | [ ] (a first script exists for references in Vol 1) |
| T4 | The second reading as a regular step, runnable by agents or by the API | [ ] |
| T5 | Question list out to a spreadsheet and answers back in | [~] done by hand for Vol 17 |
| T6 | Release gate: refuses to build a final copy while a question or known fault is open | [ ] |
| T7 | Final-copy build: printer's page size, margins, cover, version and date in each PDF | [ ] |
| T8 | One vocabulary for the series: names of deities, seers, metres, ritual terms spelt the same in every volume | [ ] |

---

## 5. Suggested order

1. **Now, by you:** start U2–U5 (rights, verses, portraits, statement); upload the text of Vols 2 and 3 (U1).
2. **Vol 1 first**, since its text is here: T1–T3, then steps 1.4–3.5 on Vol 1. This shows how much of the old English places cleanly and settles whether Vols 2–3 are corrected or re-translated.
3. Second reading (T4, step 4) of Vol 1; your decisions (step 5).
4. Vols 2 and 3 by the same route once their text is here.
5. Printer and page size (U8), scholar's sample, final build, proof, release.

## 6. Change log
- Nov 17 2026: the user's assessment of Vol 2 recorded; prompt for its clean-up session written (`vol2/CLEANUP_PROMPT.md`).
- Nov 17 2026: file created. Counts of `[?]` and `[sic]` and the state of the Vol 1 re-check taken from the repository on that day.
