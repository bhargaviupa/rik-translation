# Vol 29: independent QA sample, round 2

Date: 2026-11-26
Files checked: `vol29/Rigveda_Samhita_Vol29_English_Translation.md` (English), `vol29/Rigveda_Samhita_Vol29_Kannada_Text.md` (Kannada), with spot checks in `vol29/html/rig_29.md` (raw supplied text).
I did not read `vol29/review/qa_sample.md`. No file other than this report was changed.

## Method

- A small script cut out each sampled page: the Kannada from `<!-- printed N -->` to the next marker, and the English from `### Printed p. N` to the next heading, with English line numbers. I read every page section in full, side by side.
- For each page I compared the Kannada prose with the English: Pratipadārtha (entry by entry), Bhāvārtha, the printed English translation, Anuvāda/introductions/particulars, Special Topics (Viśeṣa-viṣaya) and footnotes. I looked for changed numbers and references, names, terms and quotations, reversed negation or attribution, omissions and additions, and translator remarks.
- Numbers: a script compared the multiset of numerals (Kannada, Devanagari and Arabic digits) per page, Kannada against English. Running heads, Sanskrit blocks (`>`) and headings were excluded. I checked each difference by hand. Where a number looked doubtful I checked the raw text in `html/rig_29.md`.
- Translator remarks: I grepped the whole English file for `[?]`, `[sic`, `as supplied`, `as printed`, `stray line` and bracketed editor or translator notes. There were no hits. Only `**NOTE**` and `**GLOSS**` marks occur on the sampled pages.
- Page-boundary text: blocks are grouped per Ṛk, so text can sit on a neighbouring page section. Where a page opened mid-sentence (pp. 3, 226, 410) I checked that the text is in the neighbouring English section. It was in all three cases.

**Not checked:** the Sanskrit blocks (Saṃhitā, Pada, Sāyaṇa-bhāṣya), the Devanagari/IAST of inline Sanskrit, the Gists of the bhāṣya, the accents, and the front matter. Pages outside the sample were not checked, except for the `( (*` pattern, which I counted across the whole file. Whether the supplied Kannada matches the print was checked only where a number looked wrong (p. 585).

## Pages

Sample A is spread over the volume; Sample B pages contain a Special Topics section (665 is in A, so B uses 732 instead).

| Sample | Printed p. | English line | Content compared | Result |
|---|---|---|---|---|
| B | 3 | 67 | Introduction (end), Anuvāda, particulars | OK (the omitted "ಸೂಕ್ತ—೨೨" line is already in notes.tsv, p. 1) |
| A | 48 | 986 | Introduction (Mitra, Varuṇa), references | OK |
| B | 100 | 2288 | English tr., Special Topics, Nirukta quote | OK |
| A | 140 | 3730 | Pratipadārtha, Bhāvārtha, English tr., Anuvāda | OK |
| B | 169 | 5005 | English tr., Introduction to Sū. 81 | 1 MINOR |
| A | 226 | 6136 | Introduction (yajña), Śa. Brā. quotes | OK |
| B | 246 | 6539 | Pratipadārtha, Bhāvārtha, English tr., Special Topics | OK |
| A | 318 | 8135 | Verse table 93–108 (Sanskrit only) | OK (numbers 93–108 match) |
| B | 331 | 8673 | Pratipadārtha, Bhāvārtha, English tr., Special Topics | OK |
| B | 399 | 10733 | Pratipadārtha, Bhāvārtha, English tr., Special Topics | OK |
| A | 410 | 11102 | Special Topics (end, in the p. 409 section), Pratipadārtha | OK |
| B | 458 | 12720 | Special Topics (Indra's and Indrāṇī's speech, Mādhavabhaṭṭa) | OK |
| A | 498 | 14229 | Bhāvārtha, English tr., Pratipadārtha | OK |
| B | 548 | 15924 | English tr., Special Topics, Pratipadārtha | OK |
| A | 585 | 17200 | Introduction (Indrāṇī), references | 1 ERROR, 2 MINOR |
| A | 665 | 19437 | Pratipadārtha, Bhāvārtha, English tr., Special Topics | OK |
| B | 732 | 21056 | Pratipadārtha, Bhāvārtha, English tr., Special Topics | OK |
| B | 758 | 21587 | Bhāvārtha, English tr., Special Topics | 1 MINOR |
| A | 760 | 21616 | Special Topics (Gītā, Śaṅkara, Gāyatrī) | 1 MINOR (formatting, systematic) |
| A | 868 | 23931 | Special Topics (Sādhyas, yajña) | 1 MINOR |
| B | 934 | 25332 | Special Topics (paridhi, samidh, paśu) | OK |
| A | 960 | 26176 | Pratipadārtha, Bhāvārtha, English tr. | OK |
| B | 1001 | 28016 | English tr., Special Topics | OK |
| A | 1020 | 28783 | Bhāvārtha (end), English tr., Pratipadārtha | OK |

## Findings

### F1. ERROR: p. 585, line 17202: the English changes a printed number

Kannada (and raw `html/rig_29.md` line 24800–24801): "ಆದರೆ, ೧೦-೮೬-೧೧ ಮತ್ತು / ೨ನೇ ಮಂತ್ರಗಳಲ್ಲಿ ಅವಳ ವಿಷಯವಾಗಿ ಸ್ವಲ್ಪ ವಿಶೇಷವಿವರಣೆಯಿರುತ್ತದೆ."
English: "But in the mantras 10-86-11 and 12 there is some special explanation concerning her."

The print has ೨ ("2nd"), and the English silently gives 12. The reading 12 is probably what the author meant (Ṛ. Saṃ. 10-86-11/12 are about Indrāṇī). But rule 2 and `note_style: NOTE` say the printed number is kept and marked; the English must not supply a number the print does not have.

- old: `in the mantras 10-86-11 and 12 there`
- new: `in the mantras 10-86-11 and 2 **NOTE** there`
- Question for `notes.tsv`: "೧೦-೮೬-೧೧ ಮತ್ತು ೨ನೇ printed; 12 intended?"

### F2. MINOR: p. 585, line 17210: an unclear printed phrase is left out without a mark

Kannada: "ಶ್ರೀ ತ್ರಿಲೋಕಪ್ರಭಾಪುತ್ರ ಇಂದ್ರಾಣಿಯ ಸೌಭಾಗ್ಯವನ್ನು ವರ್ಣಿಸುವ ವಿವರಣೆಯು ಈ ರೀತಿಯಿದೆ—" (raw line 24811 has the same).
English: "The account describing the good fortune of Indrāṇī is as follows—"

"ಶ್ರೀ ತ್ರಿಲೋಕಪ್ರಭಾಪುತ್ರ" is missing from the English. It is unintelligible, perhaps a garbled source name (the quote that follows is Tai. Brā. 2-4-2.7). It should be marked, not dropped.

- old: `The account describing the good fortune of Indrāṇī is as follows—`
- new: `The account describing the good fortune of Indrāṇī is as follows **NOTE**—`
- Question: "ಶ್ರೀ ತ್ರಿಲೋಕಪ್ರಭಾಪುತ್ರ printed before ಇಂದ್ರಾಣಿಯ; meaning unclear (garbled source name?)"

### F3. MINOR: p. 585, line 17206: a truncated word is guessed as "hair"

Kannada: "ಅವಳಿಗೆ ಎಲ್ಲಾ ರೂಪವನ್ನೂ ಹೊಂದುವ ಅತ್ಯುತ್ತಮವಾದ / ರೋಭೂಷಣವುಂಟೆಂದೂ" (raw line 24807 has the same).
English: "she has the most excellent adornment of hair, which takes on all forms."

"ರೋಭೂಷಣ" is most likely ಶಿರೋಭೂಷಣ, "head-ornament", with the first syllable lost. "Hair" is an unmarked guess.

- old: `the most excellent adornment of hair, which takes on all forms`
- new: `the most excellent head-ornament **NOTE**, which takes on all forms`
- Question: "ರೋಭೂಷಣ printed; read as ಶಿರೋಭೂಷಣ"

### F4. MINOR: p. 758, line 21591: an adjective phrase is attached to the wrong noun

Kannada: "ಈ ಮಹಾಪುರುಷನ ಮುಕ್ಕಾಲುಪಾಲು ಗೋಚರಾತೀತವಾದುದೂ ಸ್ವಪ್ರಕಾಶರೂಪವಾದುದೂ ಅದ ಲೋಕದಲ್ಲಿ ಯಾವ ಬದಲಾವಣೆಯನ್ನೂ ಹೊಂದದೆ ನಿಜಸ್ಥಿತಿಯಲ್ಲಿರುತ್ತದೆ."
English: "Three-quarters of this Great Puruṣa, which is beyond perception and self-luminous, remains in that world, in its true state, without undergoing any change."

In "…ವಾದುದೂ …ವಾದುದೂ ಅದ (=ಆದ) ಲೋಕದಲ್ಲಿ", the "-ದೂ … ಆದ" phrase qualifies ಲೋಕ: the world (heaven, *divi*) is what is beyond perception and self-luminous. The English reads ಅದ as "that" and gives the qualities to the three-quarters.

- old: `Three-quarters of this Great Puruṣa, which is beyond perception and self-luminous, remains in that world, in its true state, without undergoing any change.`
- new: `Three-quarters of this Great Puruṣa remain in their true state, without undergoing any change, in the world that is beyond perception and self-luminous.`

### F5. MINOR: p. 868, line 23941: the label "Main purport" is left out

Kannada: "ಮುಖ್ಯಾಭಿಪ್ರಾಯವುಈ ಋಕ್ಕಿನಲ್ಲಿ ದೇವತೆಗಳು ಯಜ್ಞಪಶುವನ್ನು … ನೆರವೇರಿಸಿದರು ಎಂಬ ವಿಷಯವು ಉಕ್ತವಾಗಿದೆ."
English: "In this Ṛk it is stated that the gods performed the sacrifice after preparing …"

The word "ಮುಖ್ಯಾಭಿಪ್ರಾಯವು" (the main purport) is not rendered. Elsewhere it is rendered, e.g. line 12730 "The main purport is this:".

- old: `In this Ṛk it is stated that the gods performed the sacrifice after preparing`
- new: `The main purport: in this Ṛk it is stated that the gods performed the sacrifice after preparing`

### F6. MINOR: p. 169, line 5016: a singular author becomes a group

Kannada: "…ವಿಶ್ವಕರ್ಮನೆಂದು ಹೆಸರು ಎಂದು ನಿರುಕ್ತಕಾರರ ನಿರ್ವಚನವಿರುತ್ತದೆ."
English: "The etymologists of the Nirukta explain that he is named Viśvakarman …"

ನಿರುಕ್ತಕಾರರು is the honorific plural for the author of the Nirukta, Yāska, one person.

- old: `The etymologists of the Nirukta explain that`
- new: `The author of the Nirukta explains that`

### F7. MINOR (formatting, systematic): p. 760, line 21620, and 11 other lines: broken brackets around the IAST

English: `… स्थितो जगत् ॥ ( (*athavā bahunaitena … sthito jagat ‖ (*)`

There is a stray "( " before the IAST and a "(*)" after it, where the normal pattern is `(*…*)`. The Kannada has no brackets here. The same pattern `( (*…‖ (*)` occurs on 12 lines of the file: 5589, 6474, 7094, 10005, 16587, 20824, 21299, 21620, 23053, 23460, 23612, 25096. It always follows a quotation ending in "॥" or "।", so it looks like a fault in the shared converter (`tools/rv/`), not in a translator's text. Rule 7 says to fix it in the tool. A fix for line 21620:

- old: `जगत् ॥ ( (*athavā`
- new: `जगत् ॥ (*athavā`
- old: `sthito jagat ‖ (*)`
- new: `sthito jagat ‖*)`

### Observations, not counted (no action needed)

- p. 3: the particulars line "ಸೂಕ್ತ—೨೨" is not in the English. This is already listed in `notes.tsv` (window w0001, p. 1).
- Kannada misprints that the English silently reads correctly, which is acceptable: p. 48 "ಎಂಬ ಮಕ್ಕಳಲ್ಲಿ" → "in the Ṛks"; p. 331 "ಈ ಯುಕ್ತಿಗೆ" → "For this Ṛk"; p. 399 "ಈ ಮುಕ್ಕಿಗೆ" → "for this Ṛk"; p. 498 "ರಾಕ್ಷಸಂಹಿಕನಾದ" → "the harmer of the Rākṣasas".
- p. 226, line 6146 (ಹನಸವಾದಂತೆ) and p. 246, line 6577 (the Bhāvārtha leaves out the object of "produced") are correctly marked `**NOTE**`.
- The printed English translations keep the print's typos ("yonr", p. 399; "conditon", p. 732). That is correct.

## Counts

- Pages checked: 24. Pages with no finding: 19.
- ERROR: 1 (F1, p. 585: number 12 for the printed ೨).
- MINOR: 6 (F2–F7; F7 is one tool fault on 12 lines).
- NOTE (editor's decision): 0 new. F1–F3 each propose a `**NOTE**` for the editor.
- Translator remarks found: 0.
