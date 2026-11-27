# Vol 29 — independent QA sample 3

Date: 2026-11-26. Reviewer: independent QA agent (read-only; this file is the only file written).

## Method

- Pages: Sample A (spread) 12, 70, 160, 240, 340, 440, 520, 640, 700, 790, 900, 985; Sample B (with a Viśeṣa-viṣaya / Special-Topics section) 5, 66, 103, 144, 221, 298, 357, 413, 441, 487, 556, 810.
- For each page I pulled the section `### Printed p. N` from `vol29/Rigveda_Samhita_Vol29_English_Translation.md` and the section `<!-- printed N -->` from `vol29/Rigveda_Samhita_Vol29_Kannada_Text.md` (with line numbers) and read them side by side, item by item: Pratipadārtha entries (count and meaning), Bhāvārtha, printed English translation, introductions, Special Topics, citations (work and number), footnotes. Where a sentence ran over a page boundary I read the neighbouring page too (pp. 297/298). Doubtful Kannada readings were checked against the raw supplied text `vol29/html/rig_29.md` (pp. 221, 298, 640, 700, 900).
- I scanned all 24 English sections for translator remarks (`[?]`, `[sic]`, "as supplied", bracketed comments, bold labels other than `**NOTE**`/`**GLOSS**`).
- Not checked: the Sanskrit blocks themselves (Saṃhitā, Pada, Sāyaṇa-bhāṣya, Devanagari/IAST correctness) and the Gists of the bhāṣya, as instructed; accents; page-marker placement of blocks grouped per Ṛk; running heads; the contents of `notes.tsv` beyond the rows touching sample pages; references outside the sample. Inline Sanskrit quotations inside the prose were checked only for completeness (one omission found, p. 900), not for spelling. Earlier QA rounds (`qa_sample*.md`) were not read.

## Pages

| Printed p. | Sample | Content compared | Result |
|---|---|---|---|
| 5 | B | Special Topics (seer of the sūkta; जाना, विपन्यया, वयं, उक्तेषु …) | clean |
| 12 | A | Bhāgavata verses (Sanskrit only), one sentence on measures of time | clean |
| 66 | B | Pratipadārtha (15), Bhāvārtha, English, Special Topics (Namuci, Tai. Brā. 1-7-1-5, 6, 7) | clean |
| 70 | A | Pratipadārtha (18), Bhāvārtha, English, Special Topics (Poona edition, Sā. 331) | clean (NOTE present) |
| 103 | B | Pratipadārtha (18), Bhāvārtha, English, Special Topics | clean |
| 144 | B | Special Topics (Ni. 3-15), Pratipadārtha start | clean |
| 160 | A | Pratipadārtha (14), Bhāvārtha, English | clean |
| 221 | B | Special Topics (Chā. U. 6-2-3, Śa. Brā. 11-1-6-2, -3) | 1 MINOR |
| 240 | A | Special Topics (Bṛ. De. 2-27, 78; 2-79; 3-12; 3-13; 3-15; 10-85; 2-72) | clean |
| 298 | B | Bhāvārtha end, English, Special Topics (Śve. U. 1.1, 8-2) | 1 MINOR |
| 340 | A | Special Topics (Sūryā story, Ai. Brā. 4-7-1) | clean |
| 357 | B | English, Special Topics (Tai. Brā. 3-2-1-1, 1-5-2-6, 1-5-2-5; Tai. Saṃ. 5-4-1-3; Ṛ. Saṃ. part 26) | clean |
| 413 | B | Special Topics (Ā. Gṛ. Sū. 1-8-8, Ni. 3-21) | clean |
| 440 | A | Special Topics (vidhavā, devara) | clean |
| 441 | B | Pratipadārtha (11), Bhāvārtha, English, Special Topics (Ā. Gṛ. Sū. 1-8-9) | clean |
| 487 | B | English, Special Topics (Yāska on Vṛṣākapi) | clean |
| 520 | A | Pratipadārtha (8), Bhāvārtha, English, Ṛk 24 heading area | 1 MINOR |
| 556 | B | Pratipadārtha (14), Bhāvārtha, English, Special Topics (pp. 539-540) | clean |
| 640 | A | Special Topics (Māhendra graha story, Ai. Brā. 12-21) | clean |
| 700 | A | Puruṣasūkta vidhāna (four prose paragraphs) | 1 MINOR |
| 790 | A | Gārgī–Yājñavalkya passage, list of worlds | clean |
| 810 | B | Pratipadārtha (11), Bhāvārtha, English, Special Topics start | clean |
| 900 | A | Special Topics (Śa. Brā. 6-3-1-11, 10-4-2-21, 10-4-2-22) | 1 ERROR |
| 985 | A | Pratipadārtha (17), Bhāvārtha, English | clean |

All numbers and references on the 24 pages agree with the Kannada (the Kannada's "ಇ. ಬೃ- ೧೨-೨೧" on p. 640 is rendered "Ai. Brā. 12-21", in line with `rv/references.tsv` row "I. Brā. → Ai. Brā." and the neighbouring "ಐ. ಬ್ರಾ. ೧೨-೨೨"; number unchanged). No negation or attribution reversals found. No translator remarks except one bare label (p. 520, below).

## Findings

### ERROR 1 — p. 900, English line 24544: part of the Śatapatha quotation omitted

Kannada (lines 32112–32116):
> ಪ್ರಜಾಪತಿಸ್ತ್ರಯ್ಯಾ ವಿದ್ಯಯಾ ಸಹಾಪಃ ಪ್ರಾನಿಶತ್…॥ ತದ್ಯಾನಿ ತ್ರೀಣಿ ಪ್ರಥಮಾನಿ । ಇಮೇ ತೇ ಲೋಕಾ … ಸರ್ವಾಣಿ ಛಂದಾಗ್ಂಸಿ ತ್ರಯೀ / **ವಿದ್ಯಾಥ ಯಾನಿ ಚತ್ವಾರ್ಯುತ್ತಮಾನಿ ದಿತಸ್ತಾನೀಮೇ ಚ ವೈ ಲೋಕಾ ದಿಶಶ್ಚ / ಪ್ರಜಾಪತಿರಥೈಷಾ ತ್ರಯೀ ವಿದ್ಯಾ ॥** (ಶ. ಬ್ರಾ. ೬-೩-೧-೧೧)

English (line 24544) stops at "… सर्वाणि छंदाग्ंसि त्रयी विद्या" and goes straight to "(Śa. Brā. 6-3-1-11)": the words "-था यानि चत्वार्युत्तमानि … प्रजापतिरथैषा त्रयी विद्या ॥" are missing (an eye-skip from the first "त्रयी विद्या" to the second). The English paraphrase that follows ("All these together formed the directions") translates the missing words, so only the quotation is cut. Same reading in `html/rig_29.md` line 38271. The replacement below is the Kannada transliterated by `indic_transliteration`; better to re-make it with the pipeline (inline `⟦ ⟧` copy) than to paste it by hand.

- old: `सर्वाणि छंदाग्ंसि त्रयी विद्या (*`
- new: `सर्वाणि छंदाग्ंसि त्रयी विद्याथ यानि चत्वार्युत्तमानि दितस्तानीमे च वै लोका दिशश्च प्रजापतिरथैषा त्रयी विद्या ॥ (*`
- old: `chaṃdāgṃsi trayī vidyā*) (Śa. Brā. 6-3-1-11)`
- new: `chaṃdāgṃsi trayī vidyātha yāni catvāryuttamāni ditastānīme ca vai lokā diśaśca prajāpatirathaiṣā trayī vidyā ‖*) (Śa. Brā. 6-3-1-11)`

### MINOR 1 — p. 221, English line 6020: "Hiraṇyagarbha" given as "The golden egg"

Kannada (line 8085): "ಸಲಿಲದ ಮೇಲೆ ಹಿರಣ್ಯಗರ್ಭವು ಒಂದು ಸಂವತ್ಸರ ಕಾಲ ತೇಲಾಡುತ್ತಿತ್ತು." = "On the waters Hiraṇyagarbha floated for a year."
English: "The golden egg floated on the water for a year."
The quoted Sanskrit speaks of the hiraṇmaya āṇḍa, so the sense is close, but the commentator names Hiraṇyagarbha, and the next sentence goes on to "the egg in the form of the golden womb".

- old: `The golden egg floated on the water for a year.`
- new: `Hiraṇyagarbha floated on the water for a year.`

### MINOR 2 — p. 298, English line 7692: a stray "in" makes the Bhāvārtha sentence ungrammatical

Kannada (pp. 297–298, lines 10606, 10611): "ಯಾವ ಈ ಸುವರ್ಣಾಂಡದಲ್ಲಿ ಸಕಲ ಭೂತಗಳೂ ಸ್ಥಾಪಿತವಾಗಿವೆಯೋ ಅಂತಹ ಅದ್ವಿತೀಯವಾದ ಈ ಬ್ರಹ್ಮಾಂಡವು … ನಾಭಿಯಲ್ಲಿ ಸ್ಥಾಪಿತವಾಗಿದೆ." = "this golden egg, in which all beings are established, that unique Brahma-egg is established in the navel …".
English (p. 297 end + p. 298): "In this golden egg, in which all beings / are established, in that unique Brahma-egg, is established in the navel of the unborn primal principle." The sentence has no subject; the egg is what is established.

- old: `are established, in that unique Brahma-egg, is established`
- new: `are established, that unique Brahma-egg is established`

(The p. 297 half, "In this golden egg, in which all beings", would then read better as "This golden egg, in which all beings"; it is outside the sample, so I only point to it.)

### MINOR 3 — p. 520, English line 15295: bare label "**Verse 23**" not in the Kannada

Kannada (lines 19268–19273): the English translation of Ṛk 23 is followed directly by "#### ಋಕ್ ೨೪". The English has "**Verse 23**", then "**NOTE**" (notes.tsv w0517 p. 520: Saṃhitā ॥ ೨೩ ॥ vs Pada ॥ ೨೫ ॥), then "#### Ṛk 24". The bold label is the only bold mark in the sample other than NOTE/GLOSS. It is already listed in `review/repair_log.md` ("the bare `**Verse 23**` mark after Ṛk 23 of Sūkta 87"), but it is still in the text, and it reads as a heading for a verse 23 placed in front of Ṛk 24. The NOTE should stay; the label should go (or the editor decides to keep it).

- old: `**Verse 23**\n\n**NOTE**\n\n#### Ṛk 24`
- new: `**NOTE**\n\n#### Ṛk 24`

(`\n` = line break; the three-line block occurs once.)

### MINOR 4 — p. 700, English line 20527: "parameśanna" for ಪರಮಾನ್ನ

Kannada (line 25603): "ಹಾಲಿನಿಂದ ಸಿದ್ಧಪಡಿಸಿದ ಪರಮಾನ್ನದಿಂದಲೂ" = "with paramānna (rice cooked in milk) prepared with milk". "parameśanna" is not a word; the Kannada clearly reads ಪರಮಾನ್ನ (raw text line 29860 the same).

- old: `with parameśanna prepared with milk`
- new: `with paramānna prepared with milk`

### NOTE (for the editor; no change proposed)

- p. 640, line 18873: "(Ai. Brā. 12-21)" for the Kannada "(ಇ. ಬೃ- ೧೨-೨೧)". The name follows `rv/references.tsv` ("I. Brā. → Ai. Brā.", user decision Nov 14 2026); the number is as printed. No row for this change appears in `review/refs_applied.tsv`; just checking it is intended.
- The `**NOTE**` marks seen on pp. 70, 160, 298, 520, 556 and 640 are existing editor questions; I did not judge them.

## Counts

- Pages checked: 24 (12 + 12).
- ERROR: 1 (p. 900, part of a Śatapatha quotation omitted).
- MINOR: 4 (pp. 221, 298, 520, 700).
- NOTE: 1 (p. 640 reference name).
- Clean pages: 19.
