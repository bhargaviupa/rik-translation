# Error kinds found so far — scan-based and html-based volumes

**Nov 12 2026. Compiled from the repo's own records** (QA samples, repair logs, pass logs, status files, lessons). Nothing here is newly measured; a figure is given only where a record gives one, with the record named. Two readers went through the records, one for each part; they sampled the per-volume review files of the scan-based volumes rather than reading every one.

**Purpose:** to see which errors a *standard structure made by script* would prevent, which a *second reading of every page* would catch, and which neither would — and to compare with the user's own review comments (`docs/review/USER_REVIEW_2026-11-12.md`).

**The last column of every table**
- **Structure** = cannot occur when the script lays out pages, headings, labels and Sanskrit blocks and the translator supplies English only.
- **Second reading** = would be caught by reading every page again against the Kannada (numbers, names, negations, omissions, additions).
- **Script check** = caught by a whole-volume check that exists or is simple to write.
- **Source** = comes from the scan or from the supplied text itself; can only be listed for the editor.
- **Open** = none of the above settles it.

---

## Part 1. Html-based volumes (Vols 12, 14, 15, 16, 17, 18 and the re-translated Vol 11)

### 1.1 QA samples — the records' own figures

| Volume | Pages read | Errors | Minor points | Clean pages | Made by |
|---|---|---|---|---|---|
| 12 | 72 | 18 | 81 | 18 | agents |
| 15 | 12 | 0 | 4 | not stated | agents |
| 16 | 36 | 2 | 8 | not totalled | agents |
| 18 | 24 | 4 | 30 | 8 | Batch API |
| 11 (first 267 pages) | 24 | 8 | about 20 | 4 | Batch API |

Vols 14 and 17 have no QA sample. Vol 12's record says "about one ERROR in four pages". The doubled sample that the checklist asks for after errors was not run for Vol 18 or Vol 11.

### 1.2 Structure

| No. | Error kind | Example | How often (record) | Who | Answer |
|---|---|---|---|---|---|
| H1 | Sanskrit block under the label of another part (blocks counted one off) | Vol 18 pp. 316–321: all 15 blocks of Ṛks 1–5 one place off | Vol 18: 6 windows; Vol 17: 1; Vol 15: 1; none in 12, 14, 16, new 11 | model | Structure |
| H2 | Ṛk heading left out, misplaced, at the wrong level, unnumbered | Vol 17: 57 of 441 left out | Vol 17: about 90 headings; Vol 16: 1 | model | Structure |
| H3 | Verse written with no heading or labels at all | Vol 17 3.55.19–21; Vol 18 three windows | 3 + 3 | model | Structure |
| H4 | Sūkta or Maṇḍala heading missing | Vol 15 Sūktas 39, 40; Vol 17 Maṇḍala 4; Vol 18 Maṇḍala 5 | one or two a volume | model | Structure |
| H5 | Heading doubled or stray | "Sūkta 52" twice (Vol 17); "Special Topics (continued)" as a chapter heading | a few a volume | model | Structure |
| H6 | Heading and label repeated for a verse that runs over a page break | Vol 11 p. 493; Vol 18 two windows | 3–4 | model | Structure |
| H7 | Page heading missing, or a few lines off the true break | new Vol 11: 12 of 24 sampled pages; text present once | Vol 11: half the sample | model | Structure |
| H8 | Words lost where a sentence is cut by a page or window break | Vol 15 p. 1/2 | once recorded (user's review) | model | Second reading |
| H9 | Verse copied into the prose instead of placed as a block (no accents) | Vol 12 Sūkta 164 Ṛks 31–32 | once | supplied label + model | Structure |

### 1.3 Numbers and references

| No. | Error kind | Example | How often | Who | Answer |
|---|---|---|---|---|---|
| H10 | Number changed from memory, or a broken number guessed | new Vol 11: Pā. 7-4-25 → 35; "೩- / -೧೮೫" made 3-1-85 | Vol 11: 5 windows; QA of Vols 12, 15, 16 found no wrong number | model | Script check (number twin) — exists |
| H11 | Printed form changed so that a check passes | "Vol. XXXII" rewritten "Vol. 32" | 4 volumes, a few each | model, caused by a faulty check | Script check fixed; Open as a habit |
| H12 | Abbreviation misread by the machine and kept "as printed" | "si" for "ni" (Nirukta) through 800 pages of Vol 15 | Vol 15: about 350 lines | supplied text | One abbreviation list (requirement B3) |
| H13 | Abbreviation expanded wrongly | "A." in the running head read as Aṣṭaka for Anuvāka (Vol 15, 8 pages) | a few | model | One abbreviation list |
| H14 | Odd printed reference kept without a note | Vol 12 p. 404 | 2 in the sample | model | Second reading |

### 1.4 Sanskrit layer

| No. | Error kind | Example | How often | Who | Answer |
|---|---|---|---|---|---|
| H15 | Inline quotation retyped or "corrected" instead of copied | Vol 17: 33 of 40 windows failed this check once | Vol 17: 135 places; Vol 16: 74; Vol 15: 39 | model | Structure (quotations placed by number, not copied) |
| H16 | Quotation shortened, paraphrased or given in English only | Vol 16 p. 77: two passages cut with "…" | Vol 12: 4 errors in 72 pages; 1–2 elsewhere | model | Structure for the Sanskrit; Second reading for the English |
| H17 | Closing marks or abridgement dots dropped | closing daṇḍa lost in 1,023 quotations of Vol 12, then 93 doubled by the repair | once, large | our scripts | Script check |
| H18 | Markers left raw, empty, or swallowing pages | Vol 16: one segment swallowed pp. 473–475 | Vol 15: about 500; Vol 16: 2 | our scripts, agents' home-made tools | Structure |
| H19 | Transliteration or Devanagari typed by hand; doubled transliteration | Vol 16: 116 doubled | Vol 16 mostly | model | Structure |
| H20 | Kannada word shown as Sanskrit, or Kannada script left in the English | heading "विशेषविषयगळु"; Vol 12 four pages | few in new volumes; Vol 16: about 600 words | model | Script check |
| H21 | Letter of another script | Arabic letter in "Paruchchhepa" (Vol 11) | 2 windows | model | Script check — exists |
| H22 | Transliteration missing under a block | Vol 12: 36 of 134 bhāṣya sections | once | our script (fixed) | Script check |
| H23 | Accent faults; verses left unaccented | accents put on a quoted verse (Vol 15 p. 237) | unaccented: Vol 12 70 of 358, Vol 15 57, Vol 16 18, Vol 18 183 | our script; supplied spelling differs from the reference | Requirement B1.2 (verse from the reference) removes it |
| H24 | Wrong join of a line break inside Sanskrit; Kannada vowel signs carried into Devanagari | Vol 11: 146 lines with ॆ / ॊ | per volume | supplied text | Source |

### 1.5 Translation and meaning — found only by QA samples

| No. | Error kind | Example | How often | Answer |
|---|---|---|---|---|
| H25 | Who does what reversed; wrong attribution | Vol 12 p. 708: Indra and the Maruts reversed | Vol 12: 7 in 72 pages; Vol 18: 2 in 24 | Second reading |
| H26 | Wrong word or technical term | Vol 11: "straight" for "curved"; Vol 12: ādyudātta given as anudātta | 1–3 per sample | Second reading |
| H27 | Addition: a gloss or translation the Kannada does not have | Vol 12: 7 errors | Vol 12 mainly | Second reading |
| H28 | Omission: words, a sūtra, a closing line dropped | Vol 12 pp. 170, 414, 422; Vol 11 p. 156 | a few per sample | Structure (a skipped piece is detected); Second reading for words inside a piece |
| H29 | Misprint silently put right | Vol 12: ಭಾಗ read as "he-goat"; printed English "shont" made "shout" | Vol 12: about 10 in 72 pages; 2–4 in other samples | Second reading |
| H30 | Summary of the bhāṣya against Sāyaṇa, or a fragment | Vol 18: the son's role given to the sacrificer | 2 per 24 pages | Second reading |
| H31 | Grammar: derivation dropped, sūtras left out; the composed Sanskrit cannot be checked by any script | Vol 12 pp. 31, 170, 693 | not counted | Open (needs the editor, or a decision on requirement F6) |

### 1.6 Our own remarks

| No. | Error kind | Example | How often | Answer |
|---|---|---|---|---|
| H32 | Far too many remarks in the text | Vol 12: 1,918 "as supplied"; Vol 16: about 2,700 remarks | whole volumes | Structure (the translator has no place to put one) |
| H33 | Remark or self-note left after the "no remarks" rule; a needed NOTE missing | Vol 11: "Sorry — I must stop…" inside an answer | a few per volume | Script check + Second reading |

### 1.7 Faults of the supplied text (the translator did not cause these)

| No. | Fault | How often (record) | Answer |
|---|---|---|---|
| H34 | Section labels garbled or missing | Vol 12 pp. 2–196: about 80 garbled, 40 missing | Script check + list for the editor |
| H35 | Page marks missing or pages merged | Vol 15 about 40; Vol 12 42; Vol 11 37; Vol 17 6; Vol 18 5 left | Source: list for the editor |
| H36 | Line ends cut; verse numbers lost | Vol 17: 20 verses without a number | Source; verse from the reference removes it for the Saṃhitā |
| H37 | Pages missing; pictures in place of verses; a printed sūkta number wrong | Vol 14 pp. 499–500 | Source |

### 1.8 Faults of our scripts and of the process

| No. | Fault | Example | Answer |
|---|---|---|---|
| H38 | A check rejects faithful text, or passes without comparing anything | the label check printed "0 misplaced" on layouts it could not read | every check prints what it compared |
| H39 | The converter mislabels | a Saṃhitā label put before a quoted verse (Vol 18 p. 625) | Structure pass needs its own test |
| H40 | A check finds a fault only after the volume is finished | all 163 windows of Vol 17 passed while 57 headings were missing | whole-volume checks after every stage |
| H41 | Windows that stop and need a hand repair | Vol 18: 14 of 136; Vol 11: 22 of 110 | Structure |
| H42 | Estimates missed; retries | Vol 17: $8.71 of the first $17.72 on retries | send once (done) |
| H43 | False report ("committed" when it was not) | Vol 15 batch 121 | report from the command's output only |

---

## Part 2. Scan-based volumes (Vols 1–11, 13 and the scan period of Vol 14)

Here a model read the Kannada and Sanskrit off page images. The dominant errors are **reading errors**, and most were never marked.

### 2.1 Numerals and references

| No. | Error kind | Example | How often (record) | Answer |
|---|---|---|---|---|
| S1 | Look-alike digit misread (3/5, 6/7, 2/9, 8/9, 2/3/7) | Vol 11: 3-36-6 → 7; Vol 13: Ni. 2-9 → 3-9 on nine pages | Vol 7: 495 of 1,982 checked rows differ, "most never marked"; Vol 8: 984 of 3,683; Vol 9: 616; Vol 11 test: right on 43 of 68 | **Supplied text** (digits are read reliably by machine); the user's numeral files |
| S2 | Number supplied from memory, or invented where the print has none | Vol 8 grammar notes; Vol 3 invented varga numbers | not counted | Supplied text + Second reading |
| S3 | Printed number missing from the translation | Vol 8: 186 rows "not in the file" | Vol 8: 186 | Second reading |
| S4 | Whole reference lists or tables wrong | Vol 1 pp. 15–16, 46–47 rebuilt, "all 20 references corrected" | not counted | Supplied text |
| S5 | Header and varga numbers misread | Vol 11 "Varga 3, not 2" | Vol 14: 7 findings | Structure (taken from the supplied running head) |
| S6 | Abbreviation misread | Vol 1 p. 45 "Mu. Saṃ." for "Ṛ. Saṃ." | once recorded | One abbreviation list |

### 2.2 Sanskrit and Kannada read from the image

| No. | Error kind | Example | How often | Answer |
|---|---|---|---|---|
| S7 | Unmarked misreadings in the bhāṣya and quotations | Vol 7: त्म read as त्र; Vol 11 PDF 49 "many unflagged errors" | no overall count | Supplied text |
| S8 | Bhāṣya partial, gapped or summarised | Vol 11 PDF 107 "about half" | not counted | Supplied text + Structure |
| S9 | Typeface traps | hooked ma/ya read as u (Vol 13 pp. 294, 307) | not counted | Supplied text |
| S10 | Verse with stray, missing or wrong words | Vol 13: 30 verses differ in letters from the reference | Vol 13: 30 | Verse from the reference |
| S11 | Sanskrit completed from memory and presented as read | Vol 1 p. 576; about a dozen on pp. 552–592 | about 12 | Supplied text; never typed by the translator |
| S12 | Accents wrong or unverified | Vol 4: 103 "accent ?" | Vol 4: 103 | Verse from the reference |
| S13 | Kannada prose and names misread | Vol 1: Lāgākṣi → Laugākṣi | not counted | Supplied text |

### 2.3 Translation and meaning

| No. | Error kind | Example | Answer |
|---|---|---|---|
| S14 | Wrong or opposite sense | Vol 1 p. ii: "required contributions from many quarters" for "took 24 years" | Second reading |
| S15 | Wrong attribution | Vol 1: Viśvāmitra for Ajīgarta | Second reading |
| S16 | Addition not in the print | Vol 1 p. 36: "ten" saṃskāras | Second reading |
| S17 | Omission, from a paragraph to whole page ranges | Vol 1: 148 pages paraphrased without their Sanskrit; four ranges skipped at first | Structure (every piece accounted for) |
| S18 | Grammar pages misstated or merged | Vol 2 | Open (as H31) |

No counts are recorded for 2.3; all were found when pages were re-read from better scans.

### 2.4 Structure and script layer

| No. | Error kind | Example | Answer |
|---|---|---|---|
| S19 | Scan duplicates, missing pages, shifted page numbers | Vol 1 pp. 17–24 missing; Vol 14 six duplicate pages | Source |
| S20 | Text translated twice, or on the wrong page | Vol 1 pp. 469–478 twice, and the two disagreed | Structure |
| S21 | Chapter and heading numbers wrong | Vol 1 chapters renumbered | Structure |
| S22 | Layers missing or converted mechanically | Vol 1: about 120 pages with no Devanagari; 256 citations converted from IAST unverified | Structure |

### 2.5 Process

| No. | Fault | Example | Answer |
|---|---|---|---|
| S23 | Pages written without seeing the image and reported as seen | Vol 3 pp. 452–517 | does not arise without scans |
| S24 | Scripted corrections applied to the wrong place | Vol 7: 33 wrong pairings applied and reverted | a correction is applied only where the old value is found once |
| S25 | Work lost in merges and branch accidents | six numerals dropped by a merge | one writer per volume |
| S26 | The user's own numeral file has slips | Vol 7 file 7-4-31 against 7-4-71 | list for the editor |

### 2.6 Still open in the scan-based volumes (the records' figures)

| Volume | Open |
|---|---|
| 1 | 312 doubt marks in three files; 148 pages without Sanskrit; about 59 best-effort places; accents unverified |
| 2 | 11 numerals not checked |
| 3 | 537 doubt marks |
| 4 | 151 doubt marks, 103 accent doubts |
| 5 | user's readings for pp. 578–625 not applied |
| 6 | 183 numeral rows await the user |
| 7 | 173 numeral differences |
| 8 | 225 numeral differences; Sūktas 98–112, about 280 flagged pages |
| 9 | 274 numeral differences |
| 10 | 2,869 doubt marks; numeral files cover only the first 200 PDF pages |
| 11 (old) | 6,621 doubt marks — replaced by the re-translation |
| 13 (old) | 1,482 doubt marks on 517 of 653 pages — to be re-translated |

A raw count of doubt marks overstates the places (each can appear in the Devanagari, in its transliteration and in a remark); the records differ on the overall figure.

---

## Part 3. What this shows

### 3.1 Html-based volumes
- **Most recorded faults are structure faults** (H1–H7, H9, H15, H18, H19, H32, H41). They come from asking the model to rebuild the page while translating. A structure made by script removes them by construction rather than by one more check after each volume.
- **Meaning errors (H25–H30) are fewer but real**: in the two Batch API samples, 3 or 4 per 24 pages once the page-boundary faults are set aside; in Vol 12, 18 in 72 pages. No script finds them. Only a second reading does.
- **The supplied text has its own faults** (H12, H24, H34–H37). They cannot be repaired from the text alone; they belong in a list for the editor.
- **Left open:** the grammar sections (H31), and the habit of putting a misprint right without saying so (H29) — the second reading has to look for exactly that.

### 3.2 Scan-based volumes
- **The dominant error is misreading**, above all of digits: where the user's numeral files were compared, a quarter of the checked numbers differed (Vol 7: 495 of 1,982; Vol 8: 984 of 3,683), most without a mark.
- **The supplied machine-read text is the remedy** for S1, S4, S7–S9, S11, S13: this is why Vol 11 was redone and Vol 13 is to be. Checking an old volume against the new text (the Vol 1 plan) addresses the same errors without re-translating.
- **Meaning errors (S14–S17)** exist here too and were found only by re-reading; they need the second reading in either case.

### 3.3 Against the user's review comments of Nov 12
| User's comment | Error kinds it addresses |
|---|---|
| Check Ṛk numbers against the reference | H2, H3, H36, S10 |
| Saṃhitā always from the reference | H23, H36, S10, S12 |
| Remove our status texts and "continues here" lines | H32, H33 |
| Remove stray letters and words | H34 (partly), and the remarks they caused |
| One list of abbreviations and known mistakes | H12, H13, S6 |
| References back in the text, English names | H20, and the footnote build |
| Kannada file close to the original | H34, H39 |
| Deviations in Pada-pāṭha, word meanings, bhāṣya mentioned | H29, S7 |

Kinds the comments do not mention, for the design to cover: H1 (blocks under the wrong label), H7 (page breaks), H15–H16 (quotations retyped or shortened), H25–H30 (meaning), H31 (grammar).
