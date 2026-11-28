# Publishing the volumes — the to-do list

*The one file to open for the state of publication of **all volumes (1–30)**. Last updated: **Nov 27 2026**. (T14, the Sāyaṇa-bhāṣya reader, added Nov 18–20 2026: see `sayana_bhr.md`).*
*Kept current by every session: a finished point is ticked with its date, a new point is added where it belongs, the counts in §1 are refreshed. Counts are from commands run on the date given; estimates are called estimates. Background: `docs/REQUIREMENTS.md` (Part H), `docs/DESIGN.md`, `docs/LEGACY_VOLUMES_PLAN.md`. Other parked points of the project: `TODO.md`. State of one volume in detail: `volN/STATUS.md`.*

Marks: `[ ]` open · `[~]` begun · `[x]` done · `—` does not apply · **(you)** only the user can do it · **(script)** costs nothing · **(agents)** uses the session allowance · **(scholar)** / **(advice)** someone outside.

**No volume can be published today.** Three things stop every volume whatever the state of its text: the rights (U2–U5 below), the open questions and remarks in the text, and the missing final build (front matter, printer's format, cover).

---

## 1. Where each volume stands (counted Nov 17 2026)

`[?]` = doubt marks in the English; "remarks" = `[sic]` plus "as printed / as supplied" wording; NOTE = questions for the editor in the new style.

| Vol | Contents | English made from | Words | `[?]` | Remarks | NOTE | Supplied text here | Kannada book | Group |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Pūrva-pīṭhikā, Bhāṣya-bhūmikā, Maṃ. 1 Sū. 1–2 | scans | 238,000 | 104 | 44 | — | yes (3 files) | text made, not in book form | A |
| 2 | Maṃ. 1 Sū. 3–19 | scans; **read a second time by the user, in good condition**; clean-up Nov 17 (our remarks out, verses from the reference) | 322,000 → 360,640 words counted by split on Nov 17 (old figure from another count) | 429 (kept for your review: 237 on Devanagari lines, 62 after references, 57 IAST twins, 43 explaining the marks, 30 other) | `[sic]` 143 kept; ‘as printed’ about 600 left | — | no | none | A |
| 3 | Maṃ. 1 Sū. 20–32 | scans | 233,000 | 110 | 689 | — | **yes, whole volume (Nov 18)** | none | A |
| 4 | Maṃ. 1 Sū. 33–46 | scans | 218,000 | 151 | 628 | — | **yes, whole volume (Nov 19)** | none | A |
| 5 | Maṃ. 1 Sū. 47–61 and the Pariśiṣṭa | scans | 270,000 | 231 | 396 | — | partly: pp. 2–468 and 486–584 (Nov 17); pp. 469–485 and 585–708 not yet | none | A |
| 6 | Maṃ. 1 Sū. 62–80 | scans | 238,000 | 575 | 691 | — | no | none | A |
| 7 | Maṃ. 1 Sū. 81–94 | scans | 229,000 | 341 (Nov 27; was 1,958) | 416 | — | no | none | A |
| 8 | Maṃ. 1 Sū. 95–112 | scans | 336,000 | 368 (Nov 27; was 4,632) | 510 | — | no | none | A |
| 9 | Maṃ. 1 Sū. 113–121 | scans | 204,000 | 1,921 | 391 | — | no | none | A |
| 10 | Maṃ. 1 Sū. 122–136 | scans | 282,000 | 1,870 | 739 | — | no | none | A |
| 11 | Maṃ. 1 Sū. 137–157 | supplied text (re-translated Nov 12) | 177,000 | 0 | 0 | 471 | yes | yes | C |
| 12 | Maṃ. 1 Sū. 158–165 | supplied text | 246,000 | 0 | 2,301 | — | yes | yes | B |
| 13 | Maṃ. 1 Sū. 166–183 (expected) | **not translated** (old scan text set aside, to be redone) | — | — | — | — | no | none | D |
| 14 | Maṃ. 1 Sū. 185 – Maṃ. 2 Sū. 23 | supplied text (pp. 499–500 missing) | 322,000 | 57 | 1,718 | — | yes | yes | B |
| 15 | Maṃ. 2 Sū. 24 – Maṃ. 3 Sū. 6 | supplied text | 252,000 | 79 | 821 | — | yes | yes | B |
| 16 | Maṃ. 3 Sū. 7–39 | supplied text; layout converted Nov 12, about 70 places with broken punctuation | 271,000 | 4 | 318 | 17 | yes | yes | B |
| 17 | Maṃ. 3 Sū. 40 – Maṃ. 4 Sū. 18 | supplied text | 316,000 | 0 | 0 | 471 (88 decided, 383 open) | yes | yes; **in the new structure, review copies built** | C |
| 18 | Maṃ. 4 Sū. 19 – Maṃ. 5 Sū. 8 | supplied text | 255,000 | 0 | 1 | 333 | yes | yes | C |
| 19 | Maṃ. 5 Sū. 9–62 | supplied text; **in translation** (another session; p. 7 of 852 on Nov 17) | — | — | — | — | yes | in progress | C |

### 1a. Kannada Text file and PDF content choice, per volume (counted Nov 27 2026 with `grep` on the files and `tools/rv/element_scan.py`; the table of §1 above is of Nov 17 and covers Vols 1–19 only)
Families of the English file: **A** current `#####` headings (Vols 11, 16–30), **B** bold-line labels (10, 12, 14, 15), **C** four older dialects (1–9). The choice itself: `--without printed_en,grammar` (REQUIREMENTS A6, `docs/PDF_ELEMENTS.md`). `special` and `grammar` only after the `LONG` warnings have been read (D24).

| Vol | Kannada Text file (pages with text) | English file family | PDF content choice (A6): Kannada / English | Note | Kannada PDF, review copy (Nov 28) |
|---|---|---|---|---|---|
| 1 | 707 pages | C | yes / no (F51) | older file (scan-based, 13 gap marks) | 798 pages, check passes |
| 2 | 800 pages | C | yes / no (F51) | older file (8 gap marks) | 829 pages, check passes |
| 3 | 646 pages | C | yes / no (F51) | whole, no gaps | 616 pages, check passes |
| 4 | 602 pages | C | yes / no (F51) | 5 pages have no page of their own in the supplied text (187, 227, 304, 326, 534) | 539 pages, check passes |
| 5 | 691 pages | C | yes / no (F51) | 35 gap marks (older file) | 739 pages, check passes |
| 6 | 614 pages | C | yes / no (F51) | older file (4 gap marks) | 540 pages, check passes |
| 7 | — | C | no file / no (F51) | no supplied text: upload `vol7/html/rig_7_1.md`, … | 506 pages, check passes |
| 8 | — | C | no file / no (F51) | no supplied text: upload `vol8/html/rig_8_1.md`, … | 711 pages, check passes |
| 9 | — | C | no file / no (F51) | no supplied text: upload `vol9/html/rig_9_1.md`, … | 525 pages, check passes |
| 10 | — | B | no file / yes (tested on 15; `bhashya` sections long) | no supplied text: upload `vol10/html/rig_10_1.md`, … | 660 pages, check passes |
| 11 | 695 pages | A | yes / yes | 689 pages, check passes |
| 12 | 726 pages | B | yes / yes (tested on 15; `bhashya` sections long) | 689 pages, check passes |
| 13 | — | — | no file / no English file | file empty; waits for its re-translation and text | 657 pages, check passes |
| 14 | 950 pages | B | yes / yes (tested on 15; `bhashya` sections long) | 936 pages, check passes |
| 15 | 800 pages | B | yes / yes (tested on 15; `bhashya` sections long) | 865 pages, check passes |
| 16 | 880 pages | A | yes / yes | 995 pages, check passes |
| 17 | 1001 pages | A | yes / yes | 1102 pages, check passes |
| 18 | 846 pages | A | yes / yes | 953 pages, check passes |
| 19 | 850 pages | A | yes / yes | 847 pages, check passes |
| 20 | 841 pages | A | yes / yes | 847 pages, check passes |
| 21 | 833 pages | A | yes / yes | 892 pages, check passes |
| 22 | 600 pages | A | yes / yes | complete (pages 1–600, no gaps; Kannada file of the translation, on `main`); my partial script file (221 pages) was superseded | 811 pages, check passes |
| 23 | 813 pages | A | yes / yes | 993 pages, check passes |
| 24 | 797 pages | A | yes / yes | 950 pages, check passes |
| 25 | 873 pages | — | yes / no English file | 5 pages have no page of their own (217, 475, 574, 575, 681); no English file | 1073 pages, check passes |
| 26 | 881 pages | A | yes / yes | curated file of the translation (main), not the script one | 934 pages, check passes |
| 27 | 982 pages | A | yes / yes | 1118 pages, check passes |
| 28 | 671 pages | A | yes / yes | pages 162, 604, 605 are missing from the supplied text (see change log) | 782 pages, check passes |
| 29 | 1024 pages | A | yes / yes | 1031 pages, check passes |
| 30 | 1279 pages | A | yes / yes | 1492 pages, check passes |

Groups: **A** read from page scans (older layout, many doubt marks, no Kannada book). **B** from the supplied text, older style with remarks in the text. **C** from the supplied text, new style (no remarks, questions listed). **D** to be translated.

Notes of the user on single volumes:
- **Vol 2 (Nov 17 2026):** in good condition; page numbers correct; many `[?]` are remarks of ours or questions inside the content and can go; accents to be verified against the reference. Not to be re-translated for now. Clean-up in its own session: `vol2/CLEANUP_PROMPT.md`.
- **Vols 11 and 13 (Nov 11–12 2026):** too many doubt marks in the scan-based text; redone from the supplied text (Vol 11 done, Vol 13 waiting for its text).

---

## 2. What I need from you

| No. | What | Needed for | State |
|---|---|---|---|
| U1 | **Machine-read text** of Vols 2, 3, 4, 6, 7, 8, 9, 10 and 13, and the rest of Vol 5 (pp. 469–485 and pp. 585–708) | the Kannada books; correcting numbers and Sanskrit by script; reading against the Kannada; translating Vol 13 | [ ] |
| U2 | **Rights in the 1949–52 Kannada edition** in writing: who holds them, and permission or proof of public domain | publishing anything at all | [ ] |
| U3 | **Permission for the accented verses** (the reference text says "personal study only"), or another source that may be published | every verse in every volume | [ ] |
| U4 | **Portraits and cover**: the old king's and guru's portraits cleared; the present king's and guru's pictures, names and consent; credentials picture | front matter | [ ] |
| U5 | **Statement of how the translation was made** and the copyright line, with advice | copyright page | [ ] |
| U6 | **Your preface** to the English edition (one per volume, or one for the series) | front matter | [ ] |
| U7 | **Publisher of record, ISBNs** (one per volume and format), price, how it is sold | copyright page, cover | [ ] |
| U8 | **Printer and page size**; split long volumes or not (review copies run to 1,750 pages) | final layout, spine | [ ] |
| U9 | **A scholar of Sanskrit and Kannada** to read a sample of each volume, named in the book | release standard | [ ] |
| U10 | **Decisions on each volume's questions.** Vol 17: 383 open, 6 answers wanted in script (rows 6, 11, 13, 16, 21, 60), 1 lost (row 15), 39 abbreviation forms; Vol 11: 471; Vol 18: 333 | no open question may be printed | [~] Vol 17: 88 decided |
| U11 | Decisions that change the look of all volumes: spelling of the verse (इन्द्र or इंद्र), layout of the pages before the preface, whether the edition's English is H. H. Wilson's | fixing the format once | [ ] |
| U12 | Vol 16: repair the 70 places with broken punctuation, or undo the removal of "as supplied" | Vol 16 | [ ] |
| U13 | Pages missing in the source: Vol 1 pp. 17–24, Vol 14 pp. 499–500; page 211/212 of Vol 11 | completeness | [ ] |

U2–U5 take calendar time and need no translation work: they can start today.

---

## 3. The steps, and where each volume is

One route for all volumes (the approved design): the Kannada book and the structure come from the supplied text by script; the English is laid into that structure; numbers and Sanskrit are settled from the supplied text and the reference; the English is read against the Kannada; you decide the questions; the book is built. What differs between the groups is how much each step has to do.

| Step | What | Who |
|---|---|---|
| S1 | Supplied text in the repo, pages checked | you, script |
| S2 | Kannada text made from it; verses from the reference | script |
|  | *(Nov 26 2026) whole-volume Kannada Text files by `tools/rv/kn_full.py`: [x] 3, 4, 25; 22, 26 and 28 came with the curated files of their translations on main (Vol 22: 600 pages, complete); [ ] 7, 8, 9, 10, 13 (no supplied text in the repository) **(you)**; older scan-based files stay for 1, 2, 5, 6 — per volume: §1a* | script |
| S3 | Volume cut into units; English laid in, every paragraph placed once | script |
| S4 | Scan-read Sanskrit and numbers replaced from the supplied text (group A only) | script |
| S5 | Marks and remarks out of the text: settled, removed, or turned into a question | script, agents |
| S6 | English read against the Kannada once; faults repaired | agents (or API) |
| S7 | Your decisions on the questions carried out; none left | you, agents |
| S8 | Front matter, your preface, contents, abbreviations, note on the translation | you, script |
| S9 | Review copies (English and Kannada) in `volN/review/` | script |
| S10 | Scholar's sample read and repaired | scholar |
| S11 | Final copies in `publish/out/`, cover, printed proof, ISBN, release | you, script |

| Vol | S1 | S2 | S3 | S4 | S5 | S6 | S7 | S8 | S9 | S10 | S11 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [x] | [~] text made; verses not yet from reference | [ ] needs prose units (T1) | [~] 20 references, 12 Sanskrit corrections on 9 pages | [~] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| 2 | [ ] | [ ] | [ ] | [~] **Saṃhitā verses of Sū. 3–19 now equal to the reference (93 of 176 replaced, Nov 17)**; Pada and quoted verses unaccented | [~] remarks removed by kind (Nov 17: 156+68 notes, 121 tentative, 146 `[as printed]`); `[?]`, `[sic]` kept for you; about 380 notes with first-person/reading remarks still to decide | [x] by the user, from scans | [ ] | [ ] | [ ] | [ ] | [ ] |
| 3 | [x] Nov 18 | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| 4 | [x] Nov 19 | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| 5 | [~] 5 files, pp. 2–468 and 486–584 | [ ] | [ ] | [~] pp. 1–184 | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| 6 | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| 7 | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| 8 | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| 9 | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| 10 | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| 11 | [x] | [x] | [~] run as a check Nov 17: 16 paragraphs not placed once, 38 parts without a Kannada label, 2 bhāṣya blocks differ | — | [x] | [~] 48 of 696 pages sampled | [ ] 471 open | [~] title, preface | [ ] old-format PDFs only | [ ] | [ ] |
| 12 | [x] | [x] | [ ] | — | [ ] 2,301 remarks | [~] 72 pages sampled (18 errors found) | [ ] | [ ] | [ ] old-format PDFs only | [ ] | [ ] |
| 13 | [ ] | [ ] | [ ] to be translated first (`vol13/CONTINUE_PROMPT_HTML.md` is for the API; an agent version is needed) | — | — | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| 14 | [x] | [x] | [ ] | — | [ ] 57 `[?]`, 1,718 remarks | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| 15 | [x] | [x] | [ ] | — | [ ] 79 `[?]`, 821 remarks | [ ] | [ ] | [ ] | [ ] old-format PDFs only | [ ] | [ ] |
| 16 | [x] | [x] | [ ] | — | [~] layout converted; U12 open | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| 17 | [x] | [x] | [x] Nov 13 | — | [x] | [ ] | [~] 88 of 471 | [~] in the agreed order, placeholders for what you supply | [x] | [ ] | [ ] |
| 18 | [x] | [x] | [ ] | — | [x] | [~] 54 pages sampled | [ ] 333 open | [~] | [ ] old-format PDFs only | [ ] | [ ] |
| 19 | [x] | [~] | [ ] | — | — | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |

*Risks not yet tried:*
- **Group A, step S3:** the scan-based volumes use older headings and labels. How much of their English places cleanly into the structure is unknown until one volume is tried. Where much does not, re-translating from the supplied text may be cheaper (as decided for Vols 11 and 13). Vol 2 is the exception: the user trusts its text.
- **Group B, step S5:** removing remarks by pattern damaged about 70 sentences in Vol 16. Any further removal is done one kind at a time with a read sample (the method in `vol2/CLEANUP_PROMPT.md`).
- **Step S6, cost (estimate):** about 13,500 agent tokens per page read (measured on Vol 12); about $0.01 a page by the Batch API (not measured). A Sonnet reader found 10 of 18 known errors: one reading does not find everything.

---

## 4. Work on the tools, once for all volumes

| No. | What | Needed by | State |
|---|---|---|---|
| T1 | Units for continuous prose with chapters (Vol 1 pp. 1–605; the Pariśiṣṭa of Vol 5) | Vols 1, 5 | [ ] |
| T2 | Import of the older English layouts into units | groups A, B | [ ] |
| T3 | Replacement of scan-read Sanskrit and numbers from the supplied text, with a list of what could not be settled | group A | [ ] (a first script exists for references in Vol 1) |
| T4a | **Word-meaning check in the second pass of every volume** (`pratipada_check.py N --source`, then `pratipada_apply.py N`, REQUIREMENTS I6a 1a). Reports made Nov 24 2026 for Vols 12, 14–21 (`volN/review/pratipada_check_source.tsv`); nothing applied yet; Vol 13 has no `html/rig_13.md` (not checked) | all | [ ] |
| T4 | The second reading as a regular step, runnable by agents or by the API | all | [ ] |
| T5 | Question list out to a spreadsheet and answers back in | all | [~] by hand for Vol 17 |
| T6 | Release gate: no final copy while a question or known fault is open | all | [ ] |
| T7 | Final-copy build: printer's page size, margins, cover, version and date in each PDF | all | [~] Nov 26 2026: footer (page number, Kannada-edition page, REVIEW COPY) in every builder, PDF check `publish/pdf_check.py`; the rest open |
| T8 | One vocabulary for the series: deities, seers, metres, ritual terms spelt the same in every volume | all | [ ] |
| T9 | The shared accent tool reads the older layouts (it finds no verse in Vol 2) | group A | [x] Nov 17 2026: `accent_compare.py` and `accent_replace.py` read the Vol 2 layout; other group-A volumes to be tried |
| T10 | Translation step in the new form (units instead of windows) | Vols 13, 19 onwards | [ ] |
| T12 | **Glosses of quoted Ṛks.** *Decided by the user, Nov 17 2026:* the gloss of a Ṛk quoted from elsewhere is **our own edition's translation of that Ṛk**, taken by script from one table Maṇḍala–Sūkta–Ṛk → English; where that volume is not made yet, a **placeholder** stands, filled once the translation exists; **a final copy is not printed while a placeholder remains** (requirement B3.5, gate D9). Quotations from other works stay the translator's. **Done Nov 17 2026:** `CROSS_REFERENCES.tsv` / `.md` at the root list every reference of every volume by page and line (40,746: 5,715 to Ṛks, 23,909 grammatical sūtras, 11,122 other works; `tools/rv/crossrefs.py`, run again after changes); 682 labelled glosses in Vols 2–8 replaced by the marker `**GLOSS**` (`tools/rv/gloss_marker.py`; removed text kept in `volN/review/glosses_removed.tsv`). **Left:** 427 labelled lines of Vols 2–8 and 86 of the other volumes in forms the script does not replace (`volN/review/glosses_left.tsv` for Vols 2–8; a reading is needed, some are remarks and not glosses); glosses that carry no label, as in Vols 10–18 where they are woven into the prose, cannot be found by script. **Nov 18 2026 (gloss session, step 1):** 277 more labelled glosses replaced (further forms added to `gloss_marker.py`; single odd lines by its `--list` mode, exact text found once in the line): Vol 3 +12, 4 +49, 5 +25, 6 +67, 7 +39, 8 +71, 10 +2, 14 +3, 16 +9. Markers now: Vol 2 160, 3 35, 4 82, 5 91, 6 115, 7 248, 8 214, 10 2, 14 3, 16 9 (959). Labelled lines still left (remarks, translations of the bhāṣya's introduction, labels standing after a long quoted passage; `glosses_left.tsv`): Vol 1 20, 2 41, 3 13, 4 31, 5 18, 6 17, 7 2, 8 22, 9 34, 10 5, 12 3, 14 2, 15 1, 16 2, 17 2, 18 3. Vol 2 not touched (18 more would match; its clean-up session's branch is still active). **Step 2 trial** (30 quoted Ṛks spread over Vol 12, read against the Kannada by an agent): 1 gloss of ours, 22 places where the English translates the edition's Kannada explanation (keep), 7 with no rendering. **Waiting for you:** (a) is the trial's reading of "gloss" right, and shall the volumes be read this way; (b) quotations from other works (Nirukta, Brāhmaṇas): markers too, or stay; (c) a quoted Ṛk with no gloss at all: add a marker, or only replace existing glosses; (d) are `Sense, mine and tentative: …` (Vol 8, 10) and `**Translation** (mine, tentative): …` of the bhāṣya's introduction (Vols 4, 5) glosses. Not built (user: not now): the table from the volumes made; finding the quoted Ṛks and their references in each volume (count first: how many carry a usable reference, how many glosses are incomplete); replacing glosses; the placeholder and its gate. Consequence: a volume that quotes Ṛks of later Maṇḍalas cannot go to print before those volumes are translated, unless you allow an exception. | all | [ ] |
| T11 | Review PDFs still in `publish/out/` moved to their volume folders | all | [x] Nov 25 2026: 28 PDFs moved to `volN/review/` (Vol 13's old builds to `vol13/legacy/`); all builders write there now |
| T14 | **By-product book: Sāyaṇa-bhāṣya reader** (Saṃhitā, Pada, bhāṣya, English Gist, Grammar, particulars; the rest left out), built by `publish/bhashya_book.py` from a volume's English file | all | [~] Nov 18 2026: **the English of the bhāṣya is being made by Fable agents, direct from Sāyaṇa's Sanskrit** (runbook `docs/BHASHYA_RUN.md`; one file per sūkta in `volN/bhashya_en/`; a reference text of Sāyaṇa from vishvasa.github.io settles misread words, logged in `volN/review/bhashya_readings.tsv`; open questions in `volN/review/bhashya_notes.tsv`). **Vol 11 done (21 sūktas)**; **Vol 16 done (33 sūktas; 3.7–3.31 by Fable, 3.32–3.39 by Sonnet from Nov 19)**; Vol 17: 3.40 done (made before the reference text: second pass due); Vol 18 not begun. Run stopped by the user at 3 am IST Nov 19 2026; choice of model (Fable or Sonnet) to be decided by the user before it goes on. Script made; sample `publish/out/Rigveda_Bhashya_Reader_Vol17_S40.md`. Runs on the labelled layout (tried: Vols 11, 16, 17, 18); refuses the older layouts (tried: Vols 5, 12), which wait for T2. Found in Vol 17: the Kannada Anuvāda and the particulars stand inside the Sāyaṇa block of 16 sūkta introductions (the reader takes them out; the volume itself still has them); Sū. 3.42 and 3.62 have no particulars; 4 Grammar sections only. Open **(you)**: is the Gist full enough to stand as the English of the bhāṣya, or is a fuller rendering wanted? |
| T15 | **Second pass of the legacy volumes** (Kannada book from the supplied text, sieve, reading in page batches, repairs, coverage of the Wikisource layers, pictures) — `tools/rv/sp_apply.py`, `sp_report.py`, `docs/SECOND_PASS_REPORT.md` | Vols 1–6 | [~] **Vol 6: read and repaired Nov 24 2026** (618 pages, 1,188 findings, 871 applied; 314 questions and the open items of `vol6/review/second_pass/STATUS_REPORT.md` await the editor); **Vol 1: read and repaired Nov 25 2026** (720 pages, 1,812 findings, 1,548 applied; open items in `vol1/review/second_pass/open.tsv`); Vol 5 in progress in another session; Vols 2–4 not started; **Vol 8: Kannada book made and `[?]` marks resolved from the supplied text Nov 27 2026** (4,616 → 368; `vol8/review/second_pass/STATUS_REPORT.md`; page-by-page reading of pp. 242–832 for other faults not done) |
| T16 | **Content choice for the PDFs (REQUIREMENTS A6):** `publish/tools/elements.py` + `--without` in `publish/volbook.py`. | all with a Kannada file; English families A, B | [x] Nov 27 2026 built and tried at the HTML stage (Vols 11, 15, 17); **[ ] tried on a real PDF** (WeasyPrint not installed in the cloud session) **(script)** |
| T17 | Whole-volume Kannada Text files: `tools/rv/kn_full.py` (one tool; refuses to overwrite; gates on page markers, digits, letters). | Vols 3, 4, 25 done by it; 7–10, 13, 22, 26, 28 came from other sessions | [x] tool; [ ] 7, 8, 9, 10, 13 **(you: upload)** |
| T18 | **Rebuild the PDFs built before Nov 27 2026**: a page mark glued to the line above was lost (Vol 17 Kannada: 5 pages). Check `id="pN"` count against the md (D23), then make that check a script. | all built PDFs | [ ] **(script)** |
| T19 | Review the `LONG` sections before `special`/`grammar`/`bhashya` are left out of a PDF: Vol 5 Kannada grammar (6,262 lines), Vol 16 grammar (1,817), Vol 28 Kannada bhāṣya (703), Vol 15 bhāṣya (415 Kannada, 266 English). | Vols 5, 15, 16, 28 | [ ] **(agents / you)** |
| T20 | Reference names in the new Kannada files (Vols 3, 4, 22, 25): `refs_apply.py N --scripts kannada` preview = 762 changes, 683 flagged; a reader looks first. | Vols 3, 4, 22, 25 | [ ] **(agents)** |
| T21 | Legacy English Vols 1–9 into the layout of family A, so that the choice covers them. | Vols 1–9 | — parked by the user Nov 27 2026 (F51) |
| T22 | **Kannada review PDFs of all volumes** (`python3 publish/build_all.py N --kan`; 19 new `kannada_only` configs made by `publish/pubcfg_kan.py` from `publish/kan_titles.tsv`). Built Nov 28 2026 for all 30 volumes: page counts in §1a, `publish/BUILD_STATUS.md`; `publish/marks_check.py` finds no lost page mark in any of them except Vol 1 (mark `1`, Vol 1 build path). | all | [x] built; [ ] looked at (D14: only Vol 3 has been looked at page by page) |
| T23 | **Press and year for the title page of the Kannada books**: only where the volume's colophon gives them (Vols 2, 3, 5, 6, 13, 14, 16). **Missing, not guessed:** Vols 4, 7, 8, 9, 10, 12, 22, 24, 25, 26, 28, 29 (`publish/kan_titles.tsv`, then `rm volN/pubcfg.json; python3 publish/pubcfg_kan.py N`). | 12 volumes | [ ] **(you)** |
| T24 | **Contents page of the Kannada book for Vols 23, 27, 30** (`contents` in their pubcfg: the start/end words are not in their supplied text, the parser stops); the books are built without it (the build prints a WARNING). Their `supplied_md` pointed at Vol 21's file (corrected). **Not checked:** which of the other volumes' Kannada books carry a contents page (the new configs of Vols 2–10, 12–14, 16, 22, 24–26, 28, 29 have no `contents` setting at all). | Vols 23, 27, 30; the new configs | [ ] **(script / agents)** |
| T25 | Vol 1 Kannada book: page mark `1` of the md is not in the built PDF (`marks_check.py 1`). | Vol 1 | [ ] **(script)** |

---

## 5. Suggested order

1. **Now, by you:** U2–U5 (rights, verses, portraits, statement); upload the texts of U1 in the order you want the volumes published.
2. **A first volume to the end**, so that the format is fixed once and steps S8–S11 are proven: **Vol 17** is furthest (structure done, review copies built); it needs your remaining decisions (U10), a reading (S6) and the final build.
3. **Vol 2** clean-up (running in its own session), then its Kannada book when its text is here.
4. **Vol 1**: tool work T1–T3, then S2–S7. This also shows whether the other scan-based volumes are corrected or re-translated.
5. **Vols 11, 18** (new style): S3, S6, S7. **Vols 12, 14, 15, 16** (older style): S3, S5, S6, S7.
6. **Vols 3–10, 13** as their texts arrive; **Vol 19** when its translation is finished.

## 6. Change log
- Nov 28 2026: **Vol 22's Kannada Text file on `main` is complete** (pages 1–600 consecutive, no gap marks, 61 sūkta headings, 471 Ṛk headings; the English file has 472 Ṛk headings: one to look at). It replaces the partial script file of Nov 26 (221 pages); the PDF built from it has 811 pages, check passes. My records that called Vol 22 partial are corrected; `vol22/review/kn_gaps.md` and `kn_full_notes.md` (of the superseded script file) removed.
- Nov 28 2026: **Kannada review PDFs built for all 30 volumes** (T22): 19 new configs (`publish/pubcfg_kan.py`, `kan_titles.tsv`), `build_all.py --kan`, list of cited works taken from the Kannada text when there is no English file, no press/year printed where unknown (T23). Found and fixed: Vol 13's Kannada file had a stale progress note that made the build cut the volume to 5 pages (logged repair; the builder now strips only a closing note line); the configs of Vols 23, 27, 30 pointed at Vol 21's supplied file. Vol 7 came to `main` with its Kannada file (565 pages, made by the second pass). Not yet done: T23, T24, T25, a reading of the PDFs (D14).
- Nov 27 2026: **Content choice for the PDFs** (REQUIREMENTS A6, D23, D24, F50, F51; `docs/PDF_ELEMENTS.md`): `publish/tools/elements.py`, `--without` / `pubcfg "without"` in `publish/volbook.py`; `tools/rv/element_scan.py` shows which elements each volume's files carry (Kannada files uniform; English families A, B, C). Tried at the HTML stage on Vols 11, 15, 17 (Vol 17: 441 printed-English sections left out of the Kannada and the English PDF, all 1,001 page marks kept). Found and fixed: page marks glued to the line above were lost in the Kannada PDF (T18).
- Nov 26 2026: **Kannada Text files made for Vols 3, 4, 25 and (partly) 22** by `tools/rv/kn_full.py` (T17) and merged to `main` with the Vol 26 conflict resolved in favour of the curated file; Vols 7, 8, 9, 10, 13 still wait for text.
- Nov 26 2026: Vol 1: sentences cut at page turns mended (`tools/rv/join_pages.py`: 177 mended, 90 gaps listed for translation); the edition's own English of Sāyaṇa's preface no longer printed beside ours; contents page links the headings inside chapters. Review PDF 1,102 pages. **For you:** does "one English, ours" also remove the edition's printed English under each Ṛk (REQUIREMENTS A4 print rule 8)?
- Nov 26 2026: the user's review of the Vol 1 PDF carried out for all volumes in the shared print step (`publish/printfix.py`, `publish/style_footer.css`; REQUIREMENTS A4 print rules 1–6, B4.6c): contents as one table format, two-line headings with the original's name in the footer, joined page turns, list numbering, smaller Sanskrit with the transliteration on its own line, no restyling of bold lead-ins; own notes and dotted leaders removed from Vol 1. Vol 1 (1,191 pages) and Vol 21 rebuilt. Open: one question on the Sāyaṇa contents (bold heads).
- Nov 26 2026: the PDF rules decided on Vol 1 written into `docs/REQUIREMENTS.md` (A4 footer, B2.6 quotation once in Devanagari, B4.6 generic remarks, D19 PDF check, M5a) and into the tools for all volumes: `tools/rv/cleanup_remarks.py N all`, `publish/style_footer.css` (old builders and `volbook.py`), `publish/pdf_check.py N`. Vol 21 review copies rebuilt with the new footer. Vols 2–10: dry-run counts only, nothing written.
- Nov 25 2026: Vol 1: generic remarks removed from the English (457 lines, logged; new kinds `paren` and `session` in `tools/rv/cleanup_remarks.py`, usable for Vols 2–10); `[?]`/`[sic]` listed in `vol1/review/open_readings.tsv` (66); review PDF rebuilt with the old builder (1,275 pages). Verse layers not yet from the reference.
- Nov 25 2026: T11 done: every PDF moved out of `publish/out/` into `volN/review/` (Vol 13's two old builds to `vol13/legacy/`); `volbook.py`, the legacy builders and `bhashya_book.py` now write review copies there. Survey of the route to PDFs for all volumes made; the choice of the one printer (`volbook.py` or `rv print`) waits for the user.
- Nov 27 2026: **Vol 7 `[?]` pass done** (Kannada book pp. 2–567 from the supplied text in two files; `[?]` 1,939 → 341 by `qmark_strip.py` (176) and 12 reader batches; 20 word-meaning fixes; tokens 3.15M). Bhāṣya English, remark clean-up, PDF not done.
- Nov 27 2026: **Vol 8 `[?]` pass done** (supplied text in two files, Kannada book pp. 2–832, `[?]` 4,616 → 368 by `qmark_strip.py` (1,409) and 26 reader batches; 21 word-meaning fixes; tokens 5.0M). Bhāṣya English, remark clean-up, PDF not done.
- Nov 24 2026: **Vol 5 second pass done** (S0–S6: Kannada book from the supplied text, all supplied pages 2–708 read in 52 batches, 1 420 repairs applied, 205 questions in `vol5/review/second_pass/questions.tsv`, Wikisource coverage of the 152 Ṛks checked, 30 pictures listed). Bhāṣya English not made; 20 pages are not in the supplied text. See `vol5/STATUS.md`.
- Nov 19 2026: supplied text of Vol 6 complete (p. 82 added as its own file; whole volume pp. 2–619).
- Nov 19 2026: supplied text of Vol 5 complete (file 5, pp. 468–485, added; whole volume pp. 2–708).
- Nov 19 2026: supplied text of Vol 5, file 7 (pp. 584–708) added; only pp. 468–485 are still missing.
- Nov 19 2026: supplied text of Vol 6, file 1 (pp. 2–81) added; the volume is complete except printed p. 82, which is in none of the three files.
- Nov 19 2026: supplied text of Vol 2 complete (file 1, pp. 2–385, added; whole volume pp. 2–808).
- Nov 19 2026: supplied text of Vol 6, files 2 and 3 (pp. 83–619), put in `vol6/html/`; file 1 (pp. 1–82) still wanted.
- Nov 19 2026: supplied text of Vol 4 (whole volume, pp. 2–608) put in `vol4/html/`.
- Nov 18 2026: the two supplied HTML files (Vol 1 file 2, Vol 3 file 1) converted to markdown at the user's request; the page splitter reads pandoc's header marks. Vol 2 pp. 1–385 still wanted (the file uploaded twice as `rig_2_1.md` is of another volume: Maṇḍala 6–7, pp. 389–841).
- Nov 18 2026: supplied text of Vol 3 (whole volume, pp. 2–647) and of Vol 2 pp. 386–808 put in the repository; Vol 2 pp. 1–385 still wanted (the file uploaded for it was from another volume).
- Nov 18 2026: T13 numbers pass run on Vols 7–10 (3 numbers changed, 22 `[?]` dropped; lists for the user made).
- Nov 18 2026: T13 names done for Vols 1–18 (reference corrector run); 13 places held; numbers pass still to run.
- Nov 18 2026: T13 added: reference corrector (script and agent) built and tried on Vols 2, 4, 11, 14, 17 (audit and import proofs unchanged; the trial changes were undone, no volume is changed); list of doubtful reference numbers made.
- Nov 18 2026: prompt for the Vol 20 translation session written (`vol20/CONTINUE_PROMPT_HTML.md`); the small tool fixes of the Vol 19 session brought to `main`.
- Nov 18 2026 (gloss session): 277 more labelled glosses replaced by `**GLOSS**` in Vols 3–8, 10, 14, 16 (959 markers in all); trial reading of 30 quoted Ṛks of Vol 12; four questions wait for the user (T12).
- Nov 18 2026: prompt for the session that continues the gloss work written: `docs/GLOSS_PROMPT.md`.
- Nov 17 2026: cross-reference list made for all volumes; labelled glosses of Vols 2–8 replaced by `**GLOSS**` (682).
- Nov 17 2026: T12 added and decided by the user (glosses of quoted Ṛks from our own edition; placeholder and print gate).
- Nov 17 2026: Vol 5 supplied text, files 1, 2, 3, 45 and 6, put in `vol5/html/`.
- Nov 17 2026: file created for Vols 1–3; the user's assessment of Vol 2 recorded and the prompt for its clean-up session written; the same day extended to all volumes (1–19), with counts taken from the repository on that day.
- Nov 17 2026 (Vol 2 clean-up): remarks removed by kind and logged (`vol2/review/removed_remarks.tsv`, `repair_log.md`); `[?]`, `[sic]` kept by your decision (lists: `open_readings.tsv`, `refs_marked.tsv`); the Saṃhitā text of all 176 Ṛks of Sū. 3–19 now equals the reference (93 replaced, `verse_corrections.tsv`); T9 done.
- Nov 19 2026: Vol 21 (Maṇḍala 6 Sūktas 29–75, Maṇḍala 7 Sūktas 1–19): English translation finished through printed p. 841 (`vol21/`, branch `claude/elegant-rubin-ivuybj`); open: 372 NOTEs, 164 GLOSS markers, preface, front matter, print PDF.
- Nov 24 2026: Vol 24 (Maṇḍala 8 Sūktas 21–67, Aṣṭaka 6 adhyāyas 2–4): English translation finished through printed p. 797 (`vol24/`, branch `claude/hopeful-heisenberg-418lwb`, by agents); open: 524 NOTEs, 52 GLOSS markers, front matter, print PDF; preface translated and installed, finishing checklist done except front matter/PDF (Nov 24 2026).
- Nov 26 2026: Vol 29 (Maṇḍala 10 Sūktas 72–94, Aṣṭaka 8 adhyāyas 3–4): English translation finished through printed p. 1024 and finishing checklist done (`vol29/`, branch `claude/hopeful-heisenberg-418lwb`): all 1024 page markers, preface installed, Kannada headings, contents check, accent report (not applied), two QA rounds (48 pages, 2 ERROR / 11 MINOR repaired). Open: 934 NOTEs, 144 GLOSS markers, source defects (pp. 321, 588 …) for the user's better copy, front matter and print PDF (need the front-matter scan). Not merged into main.
- Nov 26 2026 (user): **Vols 1 and 3–10 stay as the old scan-based translations** (no re-translation from machine-read text for now). Still waiting for text or decision: Vol 13 (not translated), Vols 22, 25, 26 (partly translated on other branches).
- Nov 27 2026: **Vol 13 translated** (re-translated from the supplied text, replacing the old scan-based translation kept in `vol13/legacy/`; Maṇḍala 1 Sūktas 166–183; pp. 1–657 with a preface; 222 NOTE settled by the default rule; one batch of 110 windows, about $8.25; QA samples of 48 pages repaired). **With this, Vols 2 and 11–30 all have a finished English translation on `main`** (checked Nov 27 2026 from the progress notes); Vols 1 and 3–10 stay as the older scan-based translations, as the user decided (their English files are not under the `Rigveda_Samhita_VolN_English_Translation.md` name on `main`). Open: front matter and PDFs for the new volumes.
- Nov 27 2026: **Vol 22 translated** (Maṇḍala 7 Sūktas 20–80; pp. 1–600 with a preface; 87 NOTE, 4 GLOSS; pp. 1–120 by agents, pp. 121–600 by the Batch API for about $4.4). Branch `claude/hopeful-fermi-kypcts`, not merged to `main`. Open: NOTE questions, finishing checklist (QA sample), front matter and PDFs.
- Nov 26 2026: **Vol 28 translated** by the Batch API route (Maṇḍala 10 Sūktas 41–71; pp. 1–674 with a preface; 174 NOTE; one batch of 112 windows, cost about $7.2). Branch `claude/vol28`, not merged to `main`. Pages 162, 604 and 605 are missing from the supplied text. Open: NOTE questions, finishing checklist (QA sample), front matter and PDFs.
- Nov 26 2026: **Vol 27 translated** (Maṇḍala 9 Sūktas 101–114, Maṇḍala 10 Sūktas 1–40; pp. 1–992; 481 NOTE, 9 GLOSS; preface translated and installed; pp. 1–794 by the Batch API ($7.57 with the preface), pp. 795–992 by Sonnet agents after the API budget was spent; 60 certain Pratipadārtha corrections applied before translation). Branch `claude/zen-euler-5ntywc`, partly on `main` (up to p. 794). Open: NOTE questions, finishing checklist, PDFs.
- Nov 25 2026: **Vol 30 translated** by the Batch API route (the last volume of the edition: Maṇḍala 10 Sūktas 95–191; pp. 1–1288; 305 NOTE; preface translated and installed; one batch of 212 windows, real cost $11.81 + $0.22 direct; 83 certain Pratipadārtha corrections applied before translation). Branch `claude/zen-euler-5ntywc`, not merged to `main`. Open: NOTE questions, finishing checklist, PDFs. The Rigveda translation is complete up to the volumes still waiting for their text (Vol 22 has missing pages).
- Nov 24 2026: **Vol 23 translated** by the Batch API route (Maṇḍala 7 Sūktas 81–104, Maṇḍala 8 Sūktas 1–20; pp. 1–856; 173 NOTE, 0 GLOSS; preface translated and installed; one batch of 129 windows, real cost $7.17 + $0.15 direct requests; 66 certain Pratipadārtha corrections applied from the Pada reference; pp. 372–373 recovered from misread running heads). Branch `claude/zen-euler-5ntywc`, not merged to `main`. Open: NOTE questions, finishing checklist, PDFs. Vol 22 waits for its missing pages (381 scan pages).
- Nov 19 2026: **Vol 20 translated** (Maṇḍala 5 Sūktas 63–87 with the Pariśiṣṭa, Maṇḍala 6 Sūktas 1–28; pp. 1–844; 399 NOTE, 139 GLOSS; preface translated and installed, 13 notes) and merged to `main`. Review PDFs built with `publish/volbook.py 20` (`publish/out/vol20_full_Eng.pdf` 1,450 pp., `vol20_full_Kan.pdf` 937 pp.; no ◌ in `pdftotext`): front matter = title page and credits only, no cover, board, contents or abbreviations; `vol20/pubcfg.json` has the year/imprint copied from Vol 18's pattern and the Vol 20 preface's date (30-3-1953) — placeholders until the user confirms (`publish/release.json` stays the only place for rights/ISBN). Not done: finishing checklist (docs/HANDBOOK.md §11), QA sample, second reading, accent report, front-matter translation (`api_frontmatter.py` needs the API; agents could do it), Pariśiṣṭa/preface notes.
- Nov 18 2026: T14 added: `publish/bhashya_book.py` and a sample of the bhāṣya reader (Vol 17, Sūkta 40).
- Nov 18 2026: T14: English of the Sāyaṇa-bhāṣya made for all 21 sūktas of Vol 11 (Maṃ. 1 Sū. 137–157) and for 3.40; found: the supplied text of Vol 11 lacks Sāyaṇa's introduction to at least nine sūktas that the reference edition has.
- Nov 19 2026: T14: run stopped as the user asked (3 am IST). 47 of 143 sūktas of the ready volumes have the English of the bhāṣya (Vol 11: 21; Vol 16: 25; Vol 17: 1); questions and readings lists built for Vols 11, 16, 17.
- Nov 19 2026: T14: Vol 16 complete (English of the bhāṣya for all 33 sūktas; 185 questions, 2,352 readings logged). Run paused for the user's choice of model after a reading of the Sonnet sūktas.
- Nov 26 2026: **Vol 26 translated** by the agent route (Maṇḍala 9 Sūktas 44–100 with the introduction to the maṇḍala, Aṣṭaka 7 adhyāyas 1–4; pp. 1–894; `vol26/`, branch `claude/epic-curie-xg7s3d`; 939 NOTE, 151 GLOSS; 49 batches, about 8.5M agent tokens). Open (`vol26/STATUS.md`): the heading of Sūkta 72 printed as 22, a doubled Ṛk 5 in Sūkta 78, the gap of the supplied text in Sūktas 90–91 (p. 645) and at p. 809, the second reading of the scan pages 810–894; finishing checklist and PDFs not started. Two small shared-tool changes to bring to `main`: `publish/tools/translit/kannada_to_deva.py` (candrabindu U+0C81), `tools/rv/batch.py` (`"doubt_check": "kn_only"`).
