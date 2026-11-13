# Design — how every volume is made, corrected, checked and published

**Approved by the user on Nov 13 2026 ("design.md looks fine to me"). Nothing has been built yet.** The assumed answers of §13 are still assumptions until the user answers each question.
It answers `docs/REQUIREMENTS.md` (what a volume must be), `docs/ERROR_KINDS.md` (what has gone wrong), `docs/TOOLKIT_PROPOSAL.md` (too many tools and records), `docs/LEGACY_VOLUMES_PLAN.md` (the old volumes) and the user's conditions of Nov 12: published PDFs carry nothing of ours; cost must come down; **any task can be run by agents instead of the API**.

| Section | Content |
|---|---|
| 1 | The diagnosis in five sentences |
| 2 | The one idea: the book is data, and everything else is made from it |
| 3 | The data: what a volume consists of |
| 4 | The steps, from the user's files to a released book |
| 5 | How a model is used: packets that either the API or agents can do |
| 6 | The published book and the working copy |
| 7 | Old volumes: how each kind comes into the same form |
| 8 | Checks and the release gate |
| 9 | Tools, records and documents (the whole set) |
| 10 | Cost |
| 11 | What this design does not solve |
| 12 | Order of building, with a test at each step |
| 13 | Assumed answers to the open questions |

---

## 1. Diagnosis

1. Until now a model wrote each window as a finished piece of text: it translated, and at the same time it rebuilt the page — headings, labels, the order of Sanskrit blocks, page breaks, references, its own remarks. Most recorded faults of the html-based volumes come from the second job, not the first (`ERROR_KINDS.md` H1–H7, H15, H18, H19, H32).
2. Because the finished text was the only place where anything lived, every later wish — a new section name, transliteration on or off, remarks out — meant changing text that was already made, by script or by hand, and each such change added mistakes (the Vol 16 trial).
3. Each volume was made with the rules of its day, so the volumes differ, and a fix found in one cannot be applied to another.
4. In the scan-based volumes the dominant fault is misreading of the page image, above all of digits; the user's machine-read text removes it.
5. Errors of meaning exist in every volume at a rate of roughly one in four to eight pages, and nothing but a second reading finds them.

## 2. The one idea

**The book is data. The text files and PDFs are printed from the data, and nobody — no model, no script, no person — edits a printed file.**

A volume is an ordered list of small **units**. Each unit is one thing of one kind: a verse, a block of commentary, one word with its meaning, one paragraph of Kannada prose with its English. The list and its order are made by script from the user's supplied text and the reference text. A model is only ever asked to fill in one field of some units (the English), or to read units and report.

What follows from this:

| Wish | Today | With the data |
|---|---|---|
| A section gets a new name; transliteration under the bhāṣya comes back; page numbers move to the footer | finished text is rewritten, volume by volume | one line in the print settings; every volume is printed again |
| All volumes alike | each was made differently | one printer for all; they cannot differ |
| No remark of ours in the book | remarks are hunted in the text | there is no place in a unit where a remark could stand |
| A heading missing, a block under the wrong label, a page break misplaced | found after the volume is finished | cannot happen: the model does not write them |
| The editor's decision on a doubtful place | typed into the text, lost if the text is remade | stored beside the unit, applied at every printing |
| An old volume corrected | page-by-page work on its text | its English is laid into the units; Sanskrit and numbers come from the source |

## 3. The data

### 3.1 Units

| Kind of unit | Where its content comes from | Does a model touch it? |
|---|---|---|
| Maṇḍala, sūkta, Ṛk (the skeleton) | the reference text: which sūktas, how many verses, each verse's number | no |
| Page (number of the original, its Maṇḍala–Anuvāka–Varga line) | the running heads of the supplied text | no |
| Saṃhitā-pāṭha | the reference text (requirement B1.2). The unit also keeps **the edition's verse** from the supplied text and the list of places where the two differ, each with a state: confirmed as the edition's reading / misreading of the supplied text / not yet looked at (requirement B5) | no |
| Pada-pāṭha, Sāyaṇa-bhāṣya, quoted verses set as blocks | the supplied text, letter for letter | no |
| The English printed in the original | the supplied text | no |
| Word-to-word meaning: one unit per word | the word from the supplied text; its Kannada meaning | yes: the meaning only |
| Gist (Bhāvārtha), Viśeṣa-viṣaya, introductions, preface: one unit per paragraph | the Kannada of the supplied text | yes: the English |
| Summary of the bhāṣya | written from the Sanskrit block | yes |
| Grammar | the Kannada of the supplied text | yes (see §13, F6) |
| Contents, list of scholars, abbreviations | the supplied text | yes: the English |

Every unit that a model fills has four things beside its text: where it stands (volume, sūkta, Ṛk, part, number), its **state** (to do / translated / read / decided), an optional **question for the editor**, and the **editor's decision**. A question is never part of the text.

### 3.2 Three things that are taken out of the model's hands

1. **References.** The script finds every reference in the Kannada (the 941 in Vol 17 have a dozen regular forms such as "ಋ. ಸಂ. ೧-೧೬೪-೨೧") and replaces it by a token before the paragraph goes to the model: "… as said in ⟨R3⟩ …". The model keeps the token; the script puts back the reference in its English form from the **one list of abbreviations** (requirement B3). A number in a reference can no longer be changed, guessed or misread, and every volume writes "Ṛ. Saṃ." the same way. An abbreviation that is not in the list is reported, not guessed.
2. **Figures.** Every string of digits in the Kannada is treated the same way.
3. **Sanskrit quoted inside a sentence.** The model marks the words as now, but the script looks for them **only inside that one paragraph**. With so small a place to search, a retyped quotation is replaced by the source letters with certainty, or reported.

### 3.3 Corrections of the supplied text are data too
The supplied text is never edited. Its faults are corrected through a list (`source_fixes.tsv`: place, as supplied, corrected, reason, who decided): a garbled label, a misread abbreviation ("si" → "ni"), a stray figure to be removed, a missing page mark. The Kannada book is printed from the supplied text with this list applied, so it "matches the original closely" (A5) and every departure from the supplied file is visible in one place.

### 3.4 Where it lives
One file per volume holds the units (`volN/data/units.jsonl`, one unit per line, readable in any editor and comparable line by line in git). Beside it: the corrections list, the editor's decisions, the print settings of the volume. Everything else in the volume folder is printed from these.

## 4. The steps

```
 user's files ─► 1 INTAKE ─► 2 STRUCTURE ─► 3 TRANSLATE ─► 4 SECOND READING ─► 5 CHECK ─► 6 EDITOR ─► 7 PRINT
                 (script)     (script)       (model)        (model)            (script)   (user)     (script)
                                  ▲                                                          │
                 reference text ──┘              review copy ◄───────────────────────────────┤
                 (verses)                        release ◄──── only through the release gate ┘
```

| Step | Who | What happens | Stops when |
|---|---|---|---|
| 1 Intake | script | the supplied files are merged without loss; pictures set aside; pages found | a page range is missing → listed for the user |
| 2 Structure | script | the skeleton is taken from the reference text; every verse block of the supplied text is matched to its reference verse; labels, blocks, word-meaning entries and paragraphs become units; references and figures become tokens | a reference verse has no match, or a block matches nothing → listed. **The user sees this list before any money or agent time is spent.** |
| 3 Translate | model | the English of the units is filled in, packet by packet (§5) | a packet's answer does not pass its checks → one repair, then listed |
| 4 Second reading | model | every packet is read again against the Kannada by a model that did not write it; it reports findings; findings are settled (§5.4) | — |
| 5 Check | script | all whole-volume checks (§8) | anything failing is listed |
| 6 Editor | user | answers the questions in the review list; reads the review copy | — |
| 7 Print | script | working copy (`.md`), review PDFs, and — through the gate — the release PDFs | the gate refuses (§8.2) |

Steps 1, 2, 5 and 7 cost nothing. Step 2 is where the new work of building lies, and it is the one that must be right: an error there is systematic. It therefore has its own tests (§12) and its own report to the user.

## 5. How a model is used

### 5.1 Packets
All model work is cut into **packets**. A packet is one small file: the instruction it needs and a numbered list of units with their Kannada. The answer is another small file: the same numbers, each with its English (or, for the second reading, a list of findings). Nothing else is accepted: a number that is missing, added or repeated fails the packet.

A packet holds one sūkta's worth of work or about six pages, whichever is smaller. Packets do not depend on each other.

### 5.2 Two ways to get a packet done — the user's choice for any task

| | Through the API | By agents |
|---|---|---|
| How | all packets of a stage are sent as one batch; answers collected | a dispatcher hands a few packets to a fresh agent, which reads the instruction once, writes the answer files and stops |
| Paid from | the API credit | the Claude subscription's allowance |
| Good for | large stages when credit is there | everything when it is not; small jobs; repairs |
| What the agent or model may do | fill the answer file | fill the answer file — it does not commit, does not edit the volume, does not run its own scripts |

**The same packet, the same answer format, the same checks, the same script that puts the answers into the data.** Which way a packet was done is recorded, nothing more. One command switches: `--via api` or `--via agents`, per volume, per step, or per run. A stage begun one way can be finished the other.

Why agents become cheaper than they were: the agent no longer rebuilds a page, runs gates in a loop, or handles git. It reads a list and writes a list.

### 5.3 The instruction
One short instruction for translating and one for reading, both derived from `REQUIREMENTS.md`. They contain no rule about headings, labels, page marks, block order, reference forms or remarks, because the model has no way to produce any of those.

### 5.4 The second reading, and what is done with its findings
The reader gets the Kannada and the English of a packet side by side and returns findings only: which unit, what kind (meaning, reversed roles, addition, omission, name or term, a misprint silently put right), the words concerned, and what it would write.

| Finding | Settled by |
|---|---|
| A reference or figure differs | cannot occur (§3.2); if the reader reports one, the token rule is checked |
| The reader proposes a different wording and the unit is small | the unit is translated again with the finding as a hint, and read once more. One round only. |
| Still disagreed, or a question of judgement | becomes a question for the editor, with both wordings |
| The reader finds nothing | the unit's state becomes "read" |

Before the reader is trusted it is **measured**: Vol 12 has 72 pages on which 18 errors are known. The reader is run on those pages; the share of known errors it reports is its score, written into the design. A cheaper model is tried the same way and used only if its score is as good.

## 6. The published book and the working copy

Three things are printed from the same data.

| Printed thing | Where | What it shows |
|---|---|---|
| **Working copy** | `volN/…English.md`, `…Kannada.md` | the text, with a small marker where a question for the editor is open; for reading and reviewing on screen |
| **Review PDF** | `volN/review/` | the book as it will look, "Review copy" in every footer, open questions marked |
| **Release PDF** | `publish/out/` | the book. No mark, no comment, no note, nothing about how it was made (requirement A1). Built only through the release gate. |

One set of print settings for all volumes fixes: the front-matter order (requirement A2, including the page for the user's preface); the section names; transliteration under every Sanskrit block; the verse with every akṣara set apart; references in the text; the footer with the original's page number and Maṇḍala–Anuvāka–Varga line; no page marks in the body; the Om picture; the page size; and, as an option that is off for now, the splitting of a long volume into parts at a sūkta boundary.

Per volume there is only what differs by nature: its cover picture, its range, its contents, its abbreviations page, its preface.

## 7. Old volumes

Every existing volume comes into the same data. What differs is where the English comes from.

| Volumes | Structure from | English from | Then |
|---|---|---|---|
| 17, 18, new 11 | their supplied text (already in the repo) | their present English, laid into the units | second reading; editor's questions carried over from their `notes.tsv` |
| 12, 14, 15, 16 | their supplied text | their present English, laid into the units; remarks stay outside (see below) | second reading |
| 1–10, old 13 | the supplied text **when the user provides it** | their present English, laid into the units where it can be aligned; units left empty are translated | second reading |
| 13 if the user prefers | supplied text | new translation | second reading |

**Laying old English into the units** means: the old file is cut at its own headings and labels; each piece is matched to the unit of the same sūkta, Ṛk and part; inside a part, paragraphs are matched in order, with the figures and Sanskrit words in them as anchors. The Sanskrit blocks, the verse, the references and the figures of the old file are **not** taken over: they come from the source. What cannot be matched is listed, and those units are translated afresh.

**Remarks inside old sentences** ("…(printed so, as supplied)…"): a unit whose English contains such words is given to a model with one task — return the sentence without the remark — and the script accepts the answer only if it consists of the old words, in the old order, with words removed and nothing added. This is the safe form of what the Vol 16 trial did by pattern.

**Kannada books** for Vols 2–10 and 13 are printed from the supplied text and its corrections list as soon as step 2 has run. No model is needed.

Nothing of the old files is deleted: they stay as they are, as the record of what was imported.

**The branch `claude/dreamy-cerf-z4h3f4`** (Nov 11–12) made transliteration a print-time matter for the Saṃhitā and Pada blocks and stripped the stored lines from Vols 12 and 14–17. It was not merged (16 conflicting files). Its audit document and its note on built PDFs are on `main`; its tool work (`strip_iast.py`, build-time transliteration in the print builder) is superseded by this design, where no file stores transliteration, and is to be consulted when the printer of Phase A is built. The branch is kept until then.

## 8. Checks and the release gate

### 8.1 One command, one report
Each check says how many items it compared; "0 compared" is reported as "not checked".

| Check | Against which errors |
|---|---|
| Every reference verse of the volume's range is present once, in order | H2, H3, S10, S17 |
| Every Sanskrit block equals the source letter for letter; the verse equals the reference; every difference between the reference verse and the edition's verse has a state, and none printed is unconfirmed | H15–H19, H23, S7–S12 |
| Every unit that needs English has it; no unit is empty or doubled | H28, S17, S20 |
| Every token (reference, figure) of the Kannada is present once in the English | H10, S1–S3 |
| Every abbreviation is in the one list | H12, H13, S6 |
| No Kannada script, no foreign letter, no bracketed remark words in any English unit | H20, H21, H33 |
| Every unit has been read a second time; no finding is unsettled | H25–H30, S14–S16 |
| Pages of the original: every number present or listed as missing in the source | H35, S19 |
| The printed PDF: page count, fonts, no missing glyph, no leftover marker | print faults |

### 8.2 The release gate
A release PDF is built only if: all checks pass; **no question for the editor is open**; no known error is listed as unrepaired; the QA sample of the release standard has been read (requirement H2.2); the rights statements in `publish/release.json` are filled (requirement H1). Otherwise only a review copy is printed, and the reason is stated.

## 9. Tools, records and documents

### 9.1 One tool
One command, `rv`, with these verbs. A session needs to know nothing else.

| Verb | Step |
|---|---|
| `rv intake N` | 1 |
| `rv structure N` | 2 — prints the structure report |
| `rv import N` | lay an existing English file into the units (§7) |
| `rv translate N --via api|agents` | 3 — with `--estimate` first |
| `rv reread N --via api|agents` | 4 |
| `rv check N` | 5 |
| `rv decide N` | 6 — takes the user's answers from the review list into the data |
| `rv print N [--release]` | 7 |
| `rv repair N UNIT` | a logged change to one unit |
| `rv status [N]` | where a volume, or every volume, stands |

The existing shared scripts are the material this is built from (the conversion of scripts, transliteration, accents, the page splitter, the print builder, the batch sender). The per-volume scripts of the scan period and the one-off repair scripts go to an archive.

### 9.2 Six records per volume, all printed from the data
`STATUS.md` (one screen) · `review/questions.tsv` (for the editor, with the decision column) · `review/source_faults.tsv` (faults of the supplied text, deviations from the reference, stray letters removed, missing pages) · `review/checks.md` (last result of every check, the reader's score, the QA sample) · `review/repair_log.md` · `parts/costs.md` (API money and agent tokens, by step).

### 9.3 Documents
`REQUIREMENTS.md` (what) · `DESIGN.md` (this) · `OPERATING.md` (one page: the verbs in order, and what each prints when all is well) · `REFERENCES.md` (the one list of works, abbreviations and known mistakes) · `LESSONS.md` · `ERROR_KINDS.md` · a ten-line `CLAUDE.md`. The handbook and the scan-period documents go to `docs/archive/`.

## 10. Cost

All figures are estimates until measured; the measured ones are named.

| Work | Per page | Basis |
|---|---|---|
| Structure, checks, printing, Kannada book | nothing | scripts |
| Translation through the API | about $0.010–0.015 | measured: Vol 17 last stage, Vol 11 |
| Translation by agents | to be measured; expected below the 10,000 tokens per page measured on Vol 12, because the agent no longer builds pages or runs gates | — |
| Second reading | about a third to a half of translation | the reader writes little; output is the costly part |
| Old English laid into units | nothing for what aligns; translation cost for what does not | share unknown until tried |
| Corrections after the reading | a small fraction | about one page in four to eight has a finding |

Ways the design keeps cost down: verbatim Sanskrit (about a quarter of a volume) is never sent for translation; references and figures need no checking; a format change costs nothing; a failed packet is repeated alone, not its stage; the reader is the same tool for new and old volumes; and for every step the user chooses API or agents.

## 11. What this design does not solve

1. **Errors of meaning that the reader also misses.** Their number is unknown until the reader's score on Vol 12 is measured; the scholar's sample (requirement H2.3) is the only further defence.
2. **The grammar sections.** Sanskrit composed by a model cannot be checked by script. They are read a second time like everything else, and a scholar should sample them.
3. **Faults of the supplied text** — missing pages, cut lines, wrong letters. They are listed, not healed; a printed copy is needed for those that matter.
4. **Rights** (requirement H1): the reference text for the verses, the Kannada edition, the portraits. No design removes these.
5. **The structure step can itself be wrong**, and then wrong everywhere. Hence its tests and its report to the user before anything is spent.
6. **How much old English can be aligned** is not known. If it is little for the scan-based volumes, they cost what a new translation costs.

## 12. Order of building — each step ends in a test the user can see

| Phase | What is built | Test | Cost |
|---|---|---|---|
| A | Structure step and printer, on Vol 17 | Vol 17's present English is laid into the units and printed. Proof: every English paragraph of today's file is placed once; every Sanskrit block equals the source; the verse count equals the reference. The user reads a review PDF in the final format. | none |
| | **Phase A done, Nov 13 2026** (`rv/`, `python3 -m rv structure|import|print 17`): 41 sūktas and 441 verses, every reference verse present once and in order; 10,967 of 10,967 English paragraphs placed once; 1,316 of 1,320 verse, Pada and bhāṣya blocks of the English file equal the source (the 4 that differ are faults of the English file, healed by printing from the source); 471 of 471 questions attached; review PDF 1,740 pages in `vol17/review/`. Reports: `vol17/review/structure_report.md`, `import_report.md`, `source_faults.tsv`. Not yet in the printer: Kannada book, full front matter, Maṇḍala–Anuvāka–Varga in the footer. | | |
| B | Packets, both ways of running them | 30 pages of Vol 13 translated through agents, and the same 30 through the API if the user wishes. Result: tokens and money per page, faults per packet. | small |
| C | The reader | run on Vol 12's 72 pages with 18 known errors → its score; a cheaper model tried | under a dollar, or agents |
| | **Phase C measured, Nov 13 2026** (by agents; `vol12/review/reader_test/RESULT.md`): a Sonnet reader found 10 of the 18 known errors (additions 5 of 6, omissions 2 of 4, meaning and term 3 of 8) and graded four of those ten as minor; a Haiku reader found 6 of 17. Consequences: Haiku is not used; every finding is acted on, whatever its grade; the reader sees whole units, not single pages; for meaning errors a stronger reader (Opus) is needed on the Summary, the Viśeṣa-viṣaya and the grammar. | | |
| D | Editor's decisions and the release gate | Vol 17 (or the volume the user names) taken to a release candidate: its questions decided, second reading done | second reading of one volume |
| E | Import of old layouts | Vol 16, then 12, 14, 15: laid into units, remarks out, printed. Proof as in A. | small |
| F | Scan-based volumes | as the user supplies their text: Kannada book at once; English by import, reading and correction | by volume |
| G | Tidy-up | archive of old scripts and documents; `OPERATING.md`; short `CLAUDE.md` | none |

Phase A is the proof of the whole idea and costs nothing. If it fails — if a volume cannot be cut into units cleanly — the design is wrong and is changed before anything else is built.

No volume is started or changed by the present method while this is being built.

## 13. Assumed answers to the open questions of `REQUIREMENTS.md`, Part F

The design does not wait for these. Each has an assumed answer, and the last column says what a different answer would cost.

| No. | Question | Assumed | If the user decides otherwise |
|---|---|---|---|
| F1 | Deviations | **Decided Nov 13 2026:** a difference between the reference verse and the edition's verse is printed under the verse, once confirmed. Still assumed: other disagreements of Pada-pāṭha, word meanings and bhāṣya are listed in `source_faults.tsv`, not printed | print setting |
| F2 | Name for the summary of the bhāṣya | **Decided Nov 13 2026:** "Summary", under "Sāyaṇa-bhāṣya — Sāyaṇa's Explanation"; Bhāvārtha is "Gist" | print setting |
| F3 | Footer | **Decided Nov 13 2026:** "Kannada edition p. 235–236 · Maṃ. 3, Anu. 1, Va. 14" | print setting |
| F4 | Stray letters | **Decided Nov 13 2026:** removed through the corrections list, so listed | none |
| F5 | Heading of the edition's English | **Decided Nov 13 2026:** "English translation", no name | print setting |
| F6 | Grammar | **Decided Nov 13 2026:** Sanskrit | those units translated again |
| F7 | Older volumes | **Decided Nov 13 2026:** a volume comes into the data when it is picked up, not before; none is cleaned by pattern | — |
| F8 | Credits | **Decided Nov 13 2026:** two pages for now (the original's credits marked as such; ours). Wording of the thanks and of the method note still open | print setting |
| F9 | Kannada book | **Decided Nov 13 2026:** original text with page marks and sūkta and Ṛk headings | print setting |
| F10 | Verse differs from the reference | **Decided Nov 13 2026:** printed under the verse (see F1) | — |
| F12 | Length | **Decided Nov 13 2026:** no splitting for now; the printer splits only if switched on later. Volumes above a printer's limit remain an open point | print setting |
| F13 | Release standard | **Decided Nov 13 2026:** every page read twice; 48 pages by a different model; a scholar's sample; nothing unrepaired | gate setting |
| F14 | Places that cannot be settled | **Decided Nov 13 2026:** plain editorial footnote "text damaged in the source" | print setting |
| F15 | User's preface | open (the user does not know yet); placeholder after the Contents, before the original's preface | print setting |
| F16 | Review copies | **Decided Nov 13 2026:** `publish/out/` holds final copies only; review copies in `volN/review/` | folder name |
| F17 | Which verse differences are real | the script proposes: a difference is taken as the edition's reading when the Pada-pāṭha or the bhāṣya of the same verse shows the same letters, otherwise it waits for the editor; nothing unconfirmed is printed | list only |

Of the seventeen questions, eleven are decided (Nov 13 2026), and all but one of the answers are print settings or lists. Still open: F1 (second half), F11 (rights), F15 (the user's preface), F17 (who confirms a verse difference), and the wording parts of F8. That is the design working as intended: what a volume *says* is made once; how it *looks* can be decided, and changed, at any time.
