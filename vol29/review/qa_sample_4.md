# Vol 29 — independent QA sample 4

Date: 2026-11-26. Reviewer: independent QA agent (read-only; this file is the only file written).

## Method

- Page sections were cut by script from the English file (`### Printed p. N` up to the next header) and from the Kannada file (`<!-- printed N -->` up to the next marker), with file line numbers kept. Each pair was then read side by side in full.
- Compared: Pratipadārtha (entry by entry), Bhāvārtha, the printed English translation, Special Topics (Viśeṣa-viṣaya), introductions and running prose. Checked for changed or missing numbers and references, names and terms, quotations, negations, who-says-what, omissions, additions, and translator remarks.
- Numbers were also checked by script: every number in the Kannada prose of each page (Kannada digits converted, Sanskrit `>` blocks and the script's `*[ … ]*` lines skipped) was compared with the numbers in the English prose of the same page. No number is missing. The only numbers found in the English but not in the Kannada prose are references taken from the bhāṣya and repeated in the Gists (pp. 22, 370, 395, 550, 560, 1015), "Part 12" on p. 237 (in the Kannada it is in a `*[ … ]*` line) and nothing else. On p. 779 the stray print marks `೦`, `9`, `೪` and on p. 897 the stray `xxix 57` are left out, correctly.
- Searched every sample section for translator remarks (`[?]`, `[sic]`, "as supplied", "as printed", bracketed comments). None were found. The only marks are `**NOTE**` and `**GLOSS**`.
- Not checked: the Saṃhitā, Pada and Sāyaṇa blocks, the Devanagari/IAST inline Sanskrit, the Gists (apart from a look for remarks), accents, pages outside the sample, and the raw `html/rig_29.md` (the Kannada file was taken as the source; I looked up only the one reference on p. 745 there). Earlier QA reports (`qa_sample*.md`) were not read. For the p. 745 reference I read `review/notes.tsv` and `review/notes_resolved.tsv`.

## Pages

| Sample | Page | Content checked | Result |
|---|---|---|---|
| A | 22 | Special Topics (prathame/pūrve yuge), Ṛk 4 | clean |
| A | 110 | Pratipadārtha (17 entries), Bhāvārtha, English tr. | clean |
| A | 200 | Prose on mahinā viśvacakṣāḥ, adhiṣṭhāna/ārambhaṇa | clean |
| A | 290 | English tr., Special Topics, Chā. U. and Ka. U. quotations | clean |
| A | 395 | Pratipadārtha (16), Bhāvārtha, English tr. | clean |
| A | 470 | Pratipadārtha (14), Bhāvārtha, English tr. | clean |
| A | 560 | English tr., Ṛk 15 head | clean |
| A | 680 | Bhāvārtha (of Ṛk 16, Kannada on p. 679), English tr., Pratipadārtha Ṛk 17 | clean |
| A | 745 | Special Topics (Gārgī–Akṣara passage, Ś. U. verse) | 1 ERROR, 1 MINOR, 1 NOTE |
| A | 850 | Special Topics (ṛtavya bricks, Śa. Brā. quotations) | clean |
| A | 955 | Pratipadārtha (end), Bhāvārtha, English tr. | clean |
| A | 1015 | Pratipadārtha (9), Bhāvārtha, English tr. | clean |
| B | 20 | Special Topics (Brahmaṇaspati, asataḥ sat) | clean |
| B | 82 | Pratipadārtha (17), Bhāvārtha, English tr., Special Topics, intro to Sūkta 75 | 1 NOTE |
| B | 156 | Special Topics (Ni. 5-3) | clean |
| B | 237 | English tr., Special Topics (Vācaspati, three points) | clean |
| B | 323 | Pratipadārtha (10), Bhāvārtha, English tr., Special Topics | 1 NOTE |
| B | 370 | Pratipadārtha (11), Bhāvārtha, English tr., Special Topics (stomas) | clean |
| B | 425 | Bhāvārtha, English tr., Special Topics (Ni. 3-21) | clean |
| B | 463 | Pratipadārtha (15), Bhāvārtha, English tr., Special Topics | 1 MINOR |
| B | 550 | Pratipadārtha (15), Bhāvārtha, English tr., Special Topics | clean |
| B | 779 | Prose, English tr., Special Topics (tripād) | clean |
| B | 897 | Pratipadārtha (11), Bhāvārtha, English tr., Special Topics | clean |
| B | 1007 | Bhāvārtha, English tr., Special Topics (Ni. 9-9) | clean |

## Findings

### 1. ERROR, p. 745: wrong name of the work in a reference (English line 21313)

- Kannada (line 27061), after the quotation `ತದ್ವಾ ಏತದಕ್ಷರಂ ಗಾರ್ಗ್ಯದೃಷ್ಟಂ … ಓತಶ್ಚ ಪ್ರೋತಶ್ಚೇತಿ ।`: `(ಬ್ರ. ತಾ ೩-೮-೧೧)`
- English: `(Pa. Brā. 3-8-11)`
- The printed abbreviation `ಬ್ರ. ತಾ` is garbled. `notes_resolved.tsv` (w0744, p. 745) settled it as *Tā. Brā.* ("Medium"), and the reference list then made that *Pa. Brā.*. But the passage is Yājñavalkya speaking to Gārgī about the Akṣara. It continues straight on from the quotation two paragraphs earlier (English line 21307), which the Kannada itself cites as `ಬೃ. ಉ. ೩-೮.೯` (Bṛ. U. 3-8.9), and the number 3-8-11 is the next section of the same passage. The garbled `ಬ್ರ. ತಾ` most likely stands for `ಬೃ. ಆ` (Bṛhad-āraṇyaka). The Tāṇḍya (Pañcaviṃśa) Brāhmaṇa has no such passage. The number is printed and is not touched.
- old: `(Pa. Brā. 3-8-11)`
- new: `(Bṛ. U. 3-8-11)`
- The editor confirmed the Tā. Brā. reading on Nov 26, so this needs the editor's decision again. If it is changed, `reference_guesses.tsv` row 189 should be corrected too.

### 2. MINOR, p. 745: "face death" weakens the sense (English line 21321)

- Kannada (line 27077): `ಉತ್ಪನ್ನವಾದ ಜಗತ್ತಿನಲ್ಲಿ ದೇವಮಾನವಾದಿಗಳಾರೂ ಸಾವನ್ನು ಎದುರಿಸಲಾರರು.` (no one can withstand or resist death).
- English: "In the world that has come into being, neither gods nor men and the like can face death." This can be read as "dare not face death". The point is that no one can escape it.
- old: `neither gods nor men and the like can face death`
- new: `neither gods nor men and the like can withstand death`

### 3. MINOR, p. 463: "biting" is left out (English line 12912)

- Kannada (line 16983): `ಕಾಡುಹಂದಿಯನ್ನು ಬೇಟೆನಾಯಿಯು ಅಟ್ಟಿಸಿಕೊಂಡುಹೋಗಿ ಅದನ್ನು ಕಿವಿಯನ್ನು ಕಚ್ಚಿ ಹಿಡಿದುತರುವಂತೆ` (biting it by the ear and holding it).
- English: "As a hunting dog chases a wild boar and brings it, holding it by the ear, …"
- old: `brings it, holding it by the ear,`
- new: `brings it, seizing it by the ear with its teeth,`

### 4. NOTE, p. 82: a garbled reference was dropped (English line 2103)

- Kannada (line 3007), after `ನದ್ಯಃ ಕಸ್ಮಾನ್ನದನಾ ಭವಂತಿ ಶಬ್ದವತ್ಯಃ ।`: `*[stray line as supplied: (૨. ૬-૭૪)]*`. The script marks this as a stray line, and it is in Gujarati digits, so it cannot be read.
- English: the quotation stands without a reference.
- This is most likely the Nirukta reference for Yāska's etymology of *nadī*, but the print cannot be read with certainty. Under the rule "no number where the print has none", leaving it out is defensible. Editor's decision: leave it out, or restore it from the raw text if the user's numerals file has it.

### 5. NOTE, p. 323: script artifact in the inline Sanskrit (English line 8360)

- English line 8360 begins `ा ॥ त्वमग्ने राजा …` (*ā ‖ …*). The Kannada (line 11642) has no such leading sign. This is derived Sanskrit, outside the scope of this check, and should go to the tool owner (`check_inline.py` / `convert.py`), not to a hand edit.

### 6. NOTE, p. 745: "Tai. U." for a Śvetāśvatara verse (English line 21317)

- `सर्वेंद्रियगुणाभासं …` is cited `(ತೈ. ಉ. ೩-೧೭)` → `(Tai. U. 3-17)`, exactly as printed. The verse is Śvetāśvatara Upaniṣad 3.17. On p. 744 the Kannada introduces the next citation `(Tai. U. 6-5)` as Śvetāśvatara too. So `ತೈ. ಉ.` here seems to be the print's (or a misread) abbreviation for Śvetāśvatara. The English follows the print, which is correct under the rules. Editor's decision whether the reference list should map it.

## Counts

- Pages checked: 24 (12 in Sample A, 12 in Sample B).
- ERROR: 1 (p. 745, `Pa. Brā. 3-8-11` should be `Bṛ. U. 3-8-11`)
- MINOR: 2 (pp. 745, 463)
- NOTE: 3 (pp. 82, 323, 745)
- Translator remarks found: 0
- Numbers changed or missing: 0
