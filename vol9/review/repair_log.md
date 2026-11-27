- 2026-11-18: tools/rv/refs_apply.py: reference names made uniform by the one list (rv/references.tsv), numbers untouched: en deva 44, en latin 1809, en latin-twin 44; every change is a row of review/refs_applied.tsv.
- 2026-11-18: numeral_apply_different.py --min-ctx=0.8 --min-score=0.85 (alignment of Nov 18): nothing applied; all 8 rows of equal part count, distance < 4 and context >= 0.8 read; 10-?? -> 10-16 skipped (the same token is also paired with 10-15 from the neighbouring file page), Pā. Sū. 6-2-172 -> 6-2-171 left for the user (Vol 10's file reads the same sūtra 7-1-172); log numerals/numeral_apply_different_Nov18.applied.tsv.
- 2026-11-18: list for the user, nothing applied: numerals/Vol9_for_user_Nov18.tsv (281 DIFFERENT file rows not applied with the reason, 10 md numerals still [?] with no aligned file row and the closest unmatched file rows; 622 NOT FOUND file rows are only in the sheet 'file rows vs md' of Vol9_file_vs_md_Nov18.xlsx).
- 2026-11-26: tools/rv/refs_apply.py: reference names made uniform by the one list (rv/references.tsv), numbers untouched: en kannada 1; every change is a row of review/refs_applied.tsv.

### 2026-11-27 qmark_strip.py: BLOCK 765 marks removed from 501 Sanskrit-block lines (derived data, K9); BARE 2 boilerplate remark lines removed (2 marks); OTHER 555 marks left

### 2026-11-27 second pass, batch m1-150.tsv
| page | old → new | why |
|---|---|---|
| 2 | `*(printed "paṅkti"?: the box reads* chandaḥ—… *[?]; the bhāṣya says Triṣṭubh)*` → `*(printed "paṅkti"; the bhāṣya says Triṣṭubh)*` | SECOND-PASS Q1: [q17] Kannada p.2 prints "ಛಂದಃ-ಪಂಕ್ತಿಃ" (chandaḥ paṅktiḥ) |
| 4 | `(Pā. 6-?-? [?],` → `(Pā. 3-3-56-4,` | SECOND-PASS Q1: [q18] Kannada p.4 and p.8 print the citation for savāya "chandasi jana/java-sanau vaktavyau" as Pā. 3-3-56-4 |
| 7 | `*jñityādir nityam* [Pā. number not clearly read, [?]])` → `*jñityādir nityam*, Pā. Sū. 6-1-197)` | SECOND-PASS Q1: [q21] Kannada p.7: "ಇತ್ಯಾದಿರ್ನಿತ್ಯಮ್ (ಪಾ. ಸೂ. 6-1-197)" |
| 8 | `Pā. numbers unclear [?];` → `Pā. Sū. 3-3-56-4;` | SECOND-PASS Q1: [q22] Kannada p.8: "ಸವಾಯ—ಛಂದಸಿ ಜವಸನ್ ವಕ್ತವ್ಯೌ (ಪಾ. ಸೂ. 3-3-56-4)" |
| 10 | `; the last clauses are tersely worded and a little doubtful [?])*` → `)*` | SECOND-PASS Q2: [q23] meta-remark clause removed with its mark; the sense-given-from-the-print statement stays |
| 12 | `khaṇḍas 33 and 34 [as printed, [?]]` → `khaṇḍas 33 and 34` | SECOND-PASS Q2: [q24] Kannada p.12: "ಐತರೇಯ ಬ್ರಾಹ್ಮಣದ 3-33 ಮತ್ತು 34ನೇ ಖಂಡಗಳಲ್ಲಿ" agrees |
| 14 | `thirty [?]` → `old age` | SECOND-PASS Q1: [q25] Kannada p.14: "ಮುಪ್ಪನ್ನೂ ಉಂಟುಮಾಡುತ್ತಾ" (mupp, old age); "thirty" was a misreading |
| 15 | `Ni. 3-2 [as printed, [?]]` → `Ni. 5-7` | SECOND-PASS Q1: [q26] Kannada p.15: "ಅರ್ಥವನ್ನು ಹೇಳಿರುವುದಕ್ಕಾಗಿ ಒಂದು ಋಕ್ಕನ್ನು ಉದಾಹರಿಸಿರುವರು. (ನಿ. 5-7)" |
| 18 | `Pā. citation partly legible, "Ma. 8-1-12(?)" [?])` → `Pā. Sū. 8-1-12-11)` | SECOND-PASS Q1: [q27] Kannada p.18 prints "ಮ. 8-1-12-11" for the rule on anyānyā doubling; abbreviation ಮ. read as Pā. (number 8-1-12 is Pāṇini) |
| 23 | `Pā. Sū. 6-1-?? [?]` → `Pā. Sū. 6-1-37-6` | SECOND-PASS Q1: [q28] Kannada p.23/26: "ದುರಃ ... ಪಾ. 6-1-37-6" |
| 24 | `twenty-eight [?] names of food (Ni. 2-8 as printed [?])` → `twenty-eight names of food (Ni. 3-9)` | SECOND-PASS Q1: [q29,q30] Kannada p.24: "ಇಪ್ಪತ್ತೆಂಟು ಅನ್ನನಾಮಗಳಲ್ಲಿಯೂ (ನಿ. 3-9)" |
| 25 | `(the Ṛk cited as in the print; its reference is doubtful [?])` → `(Ṛ. Saṃ. 7-63-1)` | SECOND-PASS Q1: [q31] Kannada p.25: "ಯೋ ವಾಂ ದೂತೋ ನ ಧಿಷ್ಣ್ಯೌ (ಋ. ಸಂ. 7-63-1)" |
| 28 | `*U* is a filler [?].` → `The word *u* is used in the sense of "and" (*ca*).` | SECOND-PASS Q1: [q32] Kannada p.28: "ಉಶಬ್ದಶ್ಚಾರ್ಥೇ" |
| 28 | `*Pā. Sū. 6-4-?? [?]*` → `*Pā. Sū. 7-1-39-1*` | SECOND-PASS Q1: [q33] Kannada p.28: "ಉರ್ವಿಯಾ । ಇಯಾಡಿಯಾಜೀಕಾರಾಣಾಮುಪಸಂಖ್ಯಾನಂ । ಪಾ. 7-1-39-1" |
| 29 | `twenty-eight [?] names of wealth beginning with *dhana* (Ni. 2-0 as printed [?])` → `twenty-eight names of wealth beginning with *dhana* (Ni. 3-9)` | SECOND-PASS Q1: [q35,q36] Kannada p.29: "ಮೊದಲಾದ 28 ಧನನಾಮಗಳಲ್ಲಿ ಮಘಶಬ್ದವು (ನಿ. 3-9)" |
| 32 | `Phiṭ-sūtra 9-00 as cited [?]` → `Phiṭ-sūtra 4-10` | SECOND-PASS Q1: [q37] Kannada p.32: "ತ್ವಂ । ತ್ವಸಮಸಿಮನೇಮೇತ್ಯನುಚ್ಚಾನಿ । ಫಿ. 4-10" |
| 33 | `(Ni. 2-10 as read [?]), the word *kṣatra*` → `(Ni. 3-9), the word *kṣatra*` | SECOND-PASS Q1: [q38] Kannada p.33: "ಕ್ಷತ್ರಾಯ—ಮಘಂ, ರೇಕ್ಣಃ ಎಂಬ ಧನನಾಮಗಳಲ್ಲಿ (ನಿ. 3-9)" |
| 33 | `(Ni. 2-10 as read [?]), so it denotes wealth` → `(Ni. 3-9), so it denotes wealth` | SECOND-PASS Q1: [q39] Kannada p.33: "ಶ್ರವಸ್ ಶಬ್ದವು ಧನನಾಮಗಳಲ್ಲಿ (ನಿ. 3-9)" |
| 34 | `(Ni. 11-18 as read [?])` → `(Ni. 11-10)` | SECOND-PASS Q1: [q40] Kannada p.34: "ಮಹಚ್ಚ ಶ್ರವಣೀಯಂ ಯಶಃ (ನಿ. 11-10)" |
| 34 | `(Ni. 94-11 as read [?])` → `(Ni. 9-11)` | SECOND-PASS Q1: [q41] Kannada p.34: "ಶ್ರವಃ ಪ್ರಶಂಸಾಂ ಇಚ್ಛಮಾನಃ (ನಿ. 9-11)" |
| 34 | `(Ni. 10-6 as read [?])` → `(Ni. 10-3)` | SECOND-PASS Q1: [q42] Kannada p.34: "ಶ್ರವ ಇತ್ಯನ್ನನಾಮ ... (ನಿ. 10-3)" |
| 34 | `Phiṭ 4-10 "*tva sama sima…*" as read [?]` → `Phiṭ-sūtra 78 "*tva sama sima…*"` | SECOND-PASS Q1: [q43] Kannada p.34: "ತ್ವ ಸಮಸಿಮ ನೇಮೇತ್ಯನುಚ್ಚಾನಿ (ಫಿ. ಸೂ. 78)" (p.32 prints ಫಿ. 4-10 for the same rule; both are printed numbers, the page-34 one is used here) |
| 35 | `number as read "4-556" [?]` → `number 4-557` | SECOND-PASS Q1: [q44] Kannada p.35: "(ಉ. ಸೂ. 4-557) ಸೂತ್ರದಿಂದ ಇನ್ ಪ್ರತ್ಯಯ" |
| 35 | `*thak*[?]` → `*thap*` | SECOND-PASS Q1: [q45] Kannada p.35: "ಇದಕ್ಕೆ ಔಣಾದಿಕ ಥಪ್ ಪ್ರತ್ಯಯ" |
| 38 | `(Ni. 2-10 as read [?])` → `(Ni. 3-9)` | SECOND-PASS Q1: [q48] Kannada p.38: "ಭಗ ಶಬ್ದವು ಇಪ್ಪತ್ತೆಂಟು ... ಧನನಾಮಗಳಲ್ಲಿ (ನಿ. 3-9)" |
| 40 | `Pā. Sū. 4-1-?? [?]` → `Pā. Sū. 4-1-85-2` | SECOND-PASS Q1: [q51] Kannada p.40: "ಪೃಥಿವ್ಯಾ ಇಞ್ (ಪಾ. ಸೂ. 4-1-85-2)" |
| 41 | `(Ni. 6-7 [?])` → `(Ni. 6-7)` | SECOND-PASS Q2: [q53] Kannada p.42: "ಪಾಥೋಂತರಿಕ್ಷಂ ಪಥಾ ವ್ಯಾಖ್ಯಾತಂ (ನಿ. 6-7)" agrees |
| 42 | `(Ni. 6-6 as read [?])` → `(Ni. 6-7)` | SECOND-PASS Q1: [q55] Kannada p.42: "ಪಾಥೋಂತರಿಕ್ಷಂ ಪಥಾ ವ್ಯಾಖ್ಯಾತಂ (ನಿ. 6-7)" |
| 46 | `Ni. 3-22 [as read, "3-22", [?]]` → `Ni. 3-13` | SECOND-PASS Q1: [q59] Kannada p.46: "ಹದಿನಾರು ರೂಪನಾಮಗಳಲ್ಲಿಯೂ (ನಿ. 3-13)" |
| 46 | `[as printed "Pā. 6-1-198" [?]]` → `[as printed "Pā. 6-1-198"]` | SECOND-PASS Q2: [q60] Kannada p.46: "ಆಮಂತ್ರಿತಸ್ಯ (ಪಾ. ಸೂ. 6-1-198)" agrees |
| 48 | `" [?]; I give` → `"; I give` | SECOND-PASS Q2: [q63] Kannada p.48 Pada prints ಯಾಃ (the second one), agreeing with the reading given |
| 50 | `*ākāro 'tre* [?]` → `*ākāro 'tra*` | SECOND-PASS Q1: [q66] Kannada p.50: "ಆಕಾರೋಽತ್ರ ಪಾದಪೂರಣಃ" |
| 53 | `Pā. Sū. 6-4-56 as read [?]` → `Pā. Sū. 7-4-69` | SECOND-PASS Q1: [q70] Kannada p.53: "ದೀರ್ಘ ಇಣಃ ಕಿತಿ । ಪಾ. 7-4-69" |
| 55 | `(Ni. 2-3 as read [?])` → `(Ni. 3-8)` | SECOND-PASS Q1: [q71] Kannada p.55: "ಇಪ್ಪತ್ತೈದು ನಾಮಗಳಲ್ಲಿ ಮರ್ತ್ಯಶಬ್ದವು (ನಿ. 3-8)" |
| 57 | `Pā. Sū. 9-0-41 as read [?]` → `Pā. Sū. 4-1-41` | SECOND-PASS Q1: [q74] Kannada p.57/61: "ಸುಮಂಗಲಾತ್ಸಂಜ್ಞಾಯಾಂ ... 4-1-41" (p.57 abbreviation ಸಾ. read as Pā.; p.61 prints ಪಾ ಸೂ. 4-1-41) |
| 58 | `(Ni. 1-12 as read [?])` → `(Ni. 2-24)` | SECOND-PASS Q1: [q76] Kannada p.58: "ಋತ ಶಬ್ದವು ಉದಕನಾಮಗಳಲ್ಲಿ (ನಿ. 2-24)" |
| 59 | `(Ni. 3-6 as read [?])` → `(Ni. 3-13)` | SECOND-PASS Q1: [q79] Kannada p.59: "ಇಪ್ಪತ್ತು ಸುಖನಾಮಗಳಲ್ಲಿ ... (ನಿ. 3-13)" |
| 60 | `(Ni. 2-7 as read [?])` → `(Ni. 3-9)` | SECOND-PASS Q1: [q81] Kannada p.60: "ಅನ್ನನಾಮಗಳಲ್ಲಿ (ನಿ. 3-9)" |
| 60 | `(Ni. 6-9 as read [?])` → `(Ni. 9-5)` | SECOND-PASS Q1: [q82] Kannada p.60: "ಮಂಗಲ ಶಬ್ದದ ಅರ್ಥವನ್ನು ವಿವರಿಸುವುದರಲ್ಲಿ (ನಿ 9-5)" |
| 60 | `*āto 'ñjñiti*[?]` → `*acoññiti*` | SECOND-PASS Q1: [q83] Kannada p.60: "ಅಚೋಞ್ಞಿತಿ ಸೂತ್ರದಿಂದ" (sp_sanskrit.py: acoññiti) |
| 64 | `having loose joints [?]` → `having loose joints` | SECOND-PASS Q2: [q90] Kannada p.64: "ಶಿಥಿಲವಾದ ಸಂಧಿಬಂಧಗಳುಳ್ಳದ್ದಾಗಿ" agrees |
| 65 | `(Ni. 2-7 as read [?])` → `(Ni. 3-9)` | SECOND-PASS Q1: [q93] Kannada p.65: "ಇಪ್ಪತ್ತೆಂಟು ಅನ್ನನಾಮಗಳಲ್ಲಿಯೂ (ನಿ. 3-9)" |
| 65 | `(Ni. 1-12 as read [?])` → `(Ni. 2-24)` | SECOND-PASS Q1: [q94] Kannada p.65: "ನೂರೊಂದು ಉದಕ ನಾಮಗಳಲ್ಲಿಯೂ, (ನಿ. 2-24)" |
| 66 | `noted as printed [?].)*` → `noted as printed.)*` | SECOND-PASS Q2: [q96] Kannada p.66 prints "ಆವಃ—ವಸ ನಿವಾಸೇ ಧಾತು" agreeing with the note |
| 68 | `1-3-91 as read [?]` → `1-3-91 as read` | SECOND-PASS Q2: [q99] Kannada p.69: "ದ್ಯುದ್ಭೋ ಲುಜಿ (ಪಾ. ಸೂ. 1-3-91)" agrees |
| 68 | `(Ni. 1-19 as read [?])` → `(Ni. 2-16)` | SECOND-PASS Q1: [q100] Kannada p.68: "ದಿಕ್ಕುಗಳ ... ಅಶಾ ಎಂಬ ಶಬ್ದವು (ನಿ. 2-16)" |
| 69 | `(Ni. 3-?? as read [?])` → `(Ni. 2-28)` | SECOND-PASS Q1: [q102] Kannada p.69: "ಅರುಣ್ಯೋ ಗಾವ ಉಷಸಃ (ನಿ. 2-28)" |
| 74 | `Pā. Sū. 6-1-?? [?]` → `Pā. Sū. 6-1-114` | SECOND-PASS Q1: [q108] Kannada p.74: "ಈಡವಂದ ವೃಶಂಸದುಹಾಂ ಣ್ಯತಃ (ಪಾ ಸೂ 6-1-114)" |
| 75 | `Pā. Sū. 6-1-?? as read [?]` → `Pā. Sū. 6-1-178` | SECOND-PASS Q1: [q110] Kannada p.75: "ಜ್ಯಾಶ್ಚಛಂದಸಿ ಬಹುಲಂ (ಪಾ. ಸೂ. 6-1-178)" |
| 76 | `Pā. Sū. 4-2-65 as read [?]` → `Pā. Sū. 8-2-65` | SECOND-PASS Q1: [q112] Kannada p.76: "ಮೋಶ್ಚ । ಪಾ. 8-2-65" |
| 77 | `(Ni. 2-7 as read [?])` → `(Ni. 3-9)` | SECOND-PASS Q1: [q115] Kannada p.77: "ಇಪ್ಪತ್ತೆಂಟು ಅನ್ನನಾಮಗಳಲ್ಲಿ (ನಿ. 3-9) ಆಯುಃ" |
| 78 | `; the Sanskrit is doubtful [?]]` → `]` | SECOND-PASS Q2: [q116] meta-remark clause removed; Kannada p.78 prints the Nirukta Sanskrit clearly (asur iti prajñā nāma ...) |
| 81 | `(Ni. 3-18 as read [?])` → `(Ni. 3-19)` | SECOND-PASS Q1: [q121] Kannada p.81: "ರೇಭಃ (ನಿ. 3-19)" |
| 82 | `[read as printed, small [?]]` → `[read as printed, small]` | SECOND-PASS Q2: [q124] Kannada p.82 has the words (ಪರೋಕ್ಷರೂಪೇಣ ಪ್ರಥಮಪುರುಷೇಣ) as in the English |
| 82 | `from the small type; doubtful [?]]` → `from the small type]` | SECOND-PASS Q2: [q125] Kannada p.82: "ಹೋತ್ರಾಖ್ಯಂ ಋತ್ವಿಕ್ ಕುತ್ಸನಾಮಾ ವಾ ಋಷಿಃ ಉದ್ಗಮಯತಿ ಉಚ್ಚಾರಯತಿ" agrees |
| 84 | `Pā. Sū. 64-78 as read [?]` → `Pā. Sū. 6-4-78` | SECOND-PASS Q1: [q126] Kannada p.84: "ಅಭ್ಯಾಸಸ್ಯಾಸವರ್ಣೇ (ಪಾ. ಸೂ. 6-4-78)" |
| 87 | `śākapūṇinā paritam* [reading of the last word doubtful [?]]` → `śākapūṇinā paṭhitaṃ*` | SECOND-PASS Q1: [q127] Kannada p.87: "ಶಾಕಪೂಣಿನಾ ಪಠಿತಂ" (sp_sanskrit.py: paṭhitaṃ) |
| 88 | `[*śleṣman* (phlegm) [?]]` → `[*śleṣman* (phlegm)]` | SECOND-PASS Q2: [q128] Kannada p.88: "ಶ್ಲೇಷ್ಮ" agrees |
| 88 | `'*udarka ity ūrdhva ucyate yadvā yadvāyor* [?] …'` → `'*udarkaityudbhava ucyate yādṛk vāyoḥ* …'` | SECOND-PASS Q1: [q129] Kannada p.88: "ಉದರ್ಕಇತ್ಯುದ್ಭವ ಉಚ್ಯತೇ ಯಾದೃಕ್ ವಾಯೋಃ" (letters from the Kannada, IAST by sp_sanskrit.py) |
| 91 | `"Dhā. 1-?-?? [?]"` → `"Dhā. 19, 63-67"` | SECOND-PASS Q1: [q130] Kannada p.91: "ಜನೀಜ್ಞಷ್‌ನಸುರಂಜೋಽಮಂತಾಶ್ಚ । ಧಾ. 19, 63-67" (the only Dhātupāṭha number of the page) |
| 93 | `(Ni. 2-?? as read "2-10" [?])` → `(Ni. 3-9)` | SECOND-PASS Q1: [q131] Kannada p.93: "(ನಿ. 3-9). ಉಕ್ತವಾಗಿರುವುದರಿಂದ ಧನವೆಂದು" |
| 95 | `(Ni. 2-1 [as read, [?]])` → `(Ni. 3-2)` | SECOND-PASS Q1: [q132] Kannada p.95: "ಇಪ್ಪತ್ತಾರು ಕರ್ಮವಾಚಕಗಳಲ್ಲಿ (ನಿ. 3-2)" |
| 99 | `he who rends the darkness [?].` → `he who rends the darkness.` | SECOND-PASS Q2: [q133] Kannada p.99: "ರುಣದ್ವ್ಯಾವೃಣೋತೀತಿ ರುದಂಧಕಾರಾದಿ । ತದ್ದೃಣಾತಿ ವಿದಾರಯತೀತಿ ರುದ್ರಃ" agrees |
| 99 | `*saṃkhyāsupūrvasya* [Pā. Sū. 5-4-140 as read, [?]]` → `*saṃkhyāsupūrvasya*` | SECOND-PASS S3: [q134] Kannada p.99: "ಸಂಖ್ಯಾ ಸುಪೂರ್ವಸ್ಯೇತಿ" has no number there; number removed with its mark |
| 101 | `makes them rule [?] by his works` → `makes them weep by his works` | SECOND-PASS Q1: [q135] Kannada p.101: "ಶತ್ರುಗಳು ಅಳುವಹಾಗೆ ಕಾರ್ಯಗಳನ್ನು ಮಾಡಿ ಅವರು ಅಳುವಂತೆ ಮಾಡುವವನು" |
| 101 | `the Kauṣītaki [Brāhmaṇa — as read, '*kauṣohanisathi*', doubtful [?]]` → `the Kaṭhopaniṣad` | SECOND-PASS Q1: [q136] Kannada p.101: "ಕಠೋಪನಿಷತ್ತಿನಲ್ಲಿ ಪ್ರಸಿದ್ಧವಾದ ಇತಿಹಾಸವನ್ನು ಅನುಸರಿಸಿಯೂ" |
| 101 | `(Ni. 10-? as read [?])` → `(Ni. 10-7)` | SECOND-PASS Q1: [q137] Kannada p.101: "ರುದ್ರಶಬ್ದಾರ್ಥನಿರ್ವಚನವನ್ನು ಮಾಡಿರುವರು (ನಿ. 10. 7)" |
| 101 | `(Ni. 2-9 as read [?])` → `(Ni. 3-9)` | SECOND-PASS Q1: [q138] Kannada p.101: "ಬಲವುಳ್ಳವನು ಎಂದು ಅರ್ಥ (ನಿ. 3-9)" |
| 103 | `Paribh. 33 [?]` → `Paribh. 37` | SECOND-PASS Q1: [q139] Kannada p.103: "ಏಕದೇಶವಿಕೃತಮನನ್ಯವತ್ (ಪರಿಭಾ. 37)" |
| 108 | `(references printed as a cluster of small numerals — 1-5-1-3, 2-5-1-3 [?], 3-1-6-1 [?], 1-` → `(1-5-1-3; 7-5-15-3; 2-5-9-1; 2-6-7-1; 3-3-2-1; 5-4-10-5; 6-6-6-1); the Kāṭhaka Saṃhitā (8-` | SECOND-PASS Q1: [q140,q141,q142,q143] Kannada p.108: "ತೈತ್ತಿರೀಯಸಂಹಿತಾ (1-5-1-3; 7-5-15-3; 2-5-9-1; 2-6-7-1; 3-3-2-1; 5-4-10-5; 6-6-6-1); ಕಾಠಕಸಂಹಿತಾ (8-15) ಶತಪಥಬ್ರಾಹ್ಮಣ (1-1-4-1 |
| 108 | `(Ṛ. Saṃ. 8-10-24-? as read [?])` → `(Ṛ. Saṃ. 8-52-1)` | SECOND-PASS Q1: [q144] Kannada p.108: "ವಿವಸ್ವಾನ್ (ಋ. ಸಂ. 8-52-1)" |
| 108 | `(Atharva 8-10-24-? [?]` → `(Atharva 8-10-24` | SECOND-PASS Q1: [q145] Kannada p.108: "ವೈವಸತ್ವನೆಂದೂ (ಅಥ. 8-10-24; ಶತ ಬ್ರಾ. 13-4-3-3)" |
| 108 | `(Ṛ. Saṃ. 9-?-? as read [?])` → `(Ṛ. Saṃ. 8-51-1)` | SECOND-PASS Q1: [q146] Kannada p.108: "ಸಾಂವರಣಿ (ಋ. ಸಂ. 8-51-1)" |
| 108 | `*dyaicotastijaḥ* [as printed, [?]]` → `*dvaco 'tastijaḥ*, Pā. Sū. 6-3-135` | SECOND-PASS Q1: [q147] Kannada p.108: "ದ್ವಚೋಽತಸ್ತಿಜಃ (ಪಾ ಸೂ. 6-3-135)" (sp_sanskrit.py: dvaco 'tastijaḥ) |
| 108 | `with *dus*[?]` → `with *dus*` | SECOND-PASS Q2: [q148] Kannada p.108: "ಉತ್ತಮಪುರುಷ ಬಹುವಚನದಲ್ಲಿ ದುಸ್ ಪ್ರತ್ಯಯ" agrees |
| 109 | `Pā. Sū. 3-3-94 as read [?]` → `Pā. Sū. 3-3-98` | SECOND-PASS Q1: [q149] Kannada p.109: "ಸ್ತ್ರಿಯಾಂಕ್ತಿನ್ (ಪಾ. ಸೂ. 3-3-98)" |
| 111 | `*udveśi* [as printed, [?]] (?)` → `*uddeśisi*` | SECOND-PASS Q1: [q150] Kannada p.111: "ಉದ್ದೇಶಿಸಿ । ಸುಮ್ನಾಯನ್ ಇತ್—" |
| 36 | `; a `[?]` marks a number that is not a valid reference` → `` | SECOND-PASS Q2: [q46] meta-remark clause "a [?] marks a number that is not a valid reference" removed with its mark (brief: meta-remarks) |
| 37 | `; a `[?]` marks a number that is not a valid reference` → `` | SECOND-PASS Q2: [q47] meta-remark clause "a [?] marks a number that is not a valid reference" removed with its mark (brief: meta-remarks) |
| 38 | `; a `[?]` marks a number that is not a valid reference` → `` | SECOND-PASS Q2: [q49] meta-remark clause "a [?] marks a number that is not a valid reference" removed with its mark (brief: meta-remarks) |
| 39 | `; a `[?]` marks a number that is not a valid reference` → `` | SECOND-PASS Q2: [q50] meta-remark clause "a [?] marks a number that is not a valid reference" removed with its mark (brief: meta-remarks) |
| 40 | `; a `[?]` marks a number that is not a valid reference` → `` | SECOND-PASS Q2: [q52] meta-remark clause "a [?] marks a number that is not a valid reference" removed with its mark (brief: meta-remarks) |
| 41 | `; a `[?]` marks a number that is not a valid reference` → `` | SECOND-PASS Q2: [q54] meta-remark clause "a [?] marks a number that is not a valid reference" removed with its mark (brief: meta-remarks) |
| 42 | `; a `[?]` marks a number that is not a valid reference` → `` | SECOND-PASS Q2: [q56] meta-remark clause "a [?] marks a number that is not a valid reference" removed with its mark (brief: meta-remarks) |
| 43 | `; a `[?]` marks a number that is not a valid reference` → `` | SECOND-PASS Q2: [q57] meta-remark clause "a [?] marks a number that is not a valid reference" removed with its mark (brief: meta-remarks) |
| 44 | `; a `[?]` marks a number that is not a valid reference` → `` | SECOND-PASS Q2: [q58] meta-remark clause "a [?] marks a number that is not a valid reference" removed with its mark (brief: meta-remarks) |
| 46 | `; a `[?]` marks a number that is not a valid reference` → `` | SECOND-PASS Q2: [q61] meta-remark clause "a [?] marks a number that is not a valid reference" removed with its mark (brief: meta-remarks) |
| 47 | `; a `[?]` marks a number that is not a valid reference` → `` | SECOND-PASS Q2: [q62] meta-remark clause "a [?] marks a number that is not a valid reference" removed with its mark (brief: meta-remarks) |
| 48 | `; a `[?]` marks a number that is not a valid reference` → `` | SECOND-PASS Q2: [q64] meta-remark clause "a [?] marks a number that is not a valid reference" removed with its mark (brief: meta-remarks) |
| 49 | `; a `[?]` marks a number that is not a valid reference` → `` | SECOND-PASS Q2: [q65] meta-remark clause "a [?] marks a number that is not a valid reference" removed with its mark (brief: meta-remarks) |
| 50 | `; a `[?]` marks a number that is not a valid reference` → `` | SECOND-PASS Q2: [q67] meta-remark clause "a [?] marks a number that is not a valid reference" removed with its mark (brief: meta-remarks) |
| 51 | `; a `[?]` marks a number that is not a valid reference` → `` | SECOND-PASS Q2: [q68] meta-remark clause "a [?] marks a number that is not a valid reference" removed with its mark (brief: meta-remarks) |
| 52 | `; a `[?]` marks a number that is not a valid reference` → `` | SECOND-PASS Q2: [q69] meta-remark clause "a [?] marks a number that is not a valid reference" removed with its mark (brief: meta-remarks) |
| 55 | `; a `[?]` marks a number that is not a valid reference` → `` | SECOND-PASS Q2: [q72] meta-remark clause "a [?] marks a number that is not a valid reference" removed with its mark (brief: meta-remarks) |
| 56 | `; a `[?]` marks a number that is not a valid reference` → `` | SECOND-PASS Q2: [q73] meta-remark clause "a [?] marks a number that is not a valid reference" removed with its mark (brief: meta-remarks) |
| 57 | `; a `[?]` marks a number that is not a valid reference` → `` | SECOND-PASS Q2: [q75] meta-remark clause "a [?] marks a number that is not a valid reference" removed with its mark (brief: meta-remarks) |
| 58 | `; a `[?]` marks a number that is not a valid reference` → `` | SECOND-PASS Q2: [q77] meta-remark clause "a [?] marks a number that is not a valid reference" removed with its mark (brief: meta-remarks) |
| 59 | `; a `[?]` marks a number that is not a valid reference` → `` | SECOND-PASS Q2: [q80] meta-remark clause "a [?] marks a number that is not a valid reference" removed with its mark (brief: meta-remarks) |
| 60 | `; a `[?]` marks a number that is not a valid reference` → `` | SECOND-PASS Q2: [q84] meta-remark clause "a [?] marks a number that is not a valid reference" removed with its mark (brief: meta-remarks) |
| 61 | `; a `[?]` marks a number that is not a valid reference` → `` | SECOND-PASS Q2: [q86] meta-remark clause "a [?] marks a number that is not a valid reference" removed with its mark (brief: meta-remarks) |
| 62 | `; a `[?]` marks a number that is not a valid reference` → `` | SECOND-PASS Q2: [q87] meta-remark clause "a [?] marks a number that is not a valid reference" removed with its mark (brief: meta-remarks) |
| 63 | `; a `[?]` marks a number that is not a valid reference` → `` | SECOND-PASS Q2: [q88] meta-remark clause "a [?] marks a number that is not a valid reference" removed with its mark (brief: meta-remarks) |
| 64 | `; a `[?]` marks a number that is not a valid reference` → `` | SECOND-PASS Q2: [q91] meta-remark clause "a [?] marks a number that is not a valid reference" removed with its mark (brief: meta-remarks) |
| 65 | `; a `[?]` marks a number that is not a valid reference` → `` | SECOND-PASS Q2: [q95] meta-remark clause "a [?] marks a number that is not a valid reference" removed with its mark (brief: meta-remarks) |
| 66 | `; a `[?]` marks a number that is not a valid reference` → `` | SECOND-PASS Q2: [q97] meta-remark clause "a [?] marks a number that is not a valid reference" removed with its mark (brief: meta-remarks) |
| 67 | `; a `[?]` marks a number that is not a valid reference` → `` | SECOND-PASS Q2: [q98] meta-remark clause "a [?] marks a number that is not a valid reference" removed with its mark (brief: meta-remarks) |
| 68 | `; a `[?]` marks a number that is not a valid reference` → `` | SECOND-PASS Q2: [q101] meta-remark clause "a [?] marks a number that is not a valid reference" removed with its mark (brief: meta-remarks) |
| 69 | `; a `[?]` marks a number that is not a valid reference` → `` | SECOND-PASS Q2: [q103] meta-remark clause "a [?] marks a number that is not a valid reference" removed with its mark (brief: meta-remarks) |
| 70 | `; a `[?]` marks a number that is not a valid reference` → `` | SECOND-PASS Q2: [q105] meta-remark clause "a [?] marks a number that is not a valid reference" removed with its mark (brief: meta-remarks) |
| 73 | `; a `[?]` marks a number that is not a valid reference` → `` | SECOND-PASS Q2: [q107] meta-remark clause "a [?] marks a number that is not a valid reference" removed with its mark (brief: meta-remarks) |
| 74 | `; a `[?]` marks a number that is not a valid reference` → `` | SECOND-PASS Q2: [q109] meta-remark clause "a [?] marks a number that is not a valid reference" removed with its mark (brief: meta-remarks) |
| 75 | `; a `[?]` marks a number that is not a valid reference` → `` | SECOND-PASS Q2: [q111] meta-remark clause "a [?] marks a number that is not a valid reference" removed with its mark (brief: meta-remarks) |
| 76 | `; a `[?]` marks a number that is not a valid reference` → `` | SECOND-PASS Q2: [q113] meta-remark clause "a [?] marks a number that is not a valid reference" removed with its mark (brief: meta-remarks) |
| 78 | `; a `[?]` marks a number that is not a valid reference` → `` | SECOND-PASS Q2: [q117] meta-remark clause "a [?] marks a number that is not a valid reference" removed with its mark (brief: meta-remarks) |
| 79 | `; a `[?]` marks a number that is not a valid reference` → `` | SECOND-PASS Q2: [q119] meta-remark clause "a [?] marks a number that is not a valid reference" removed with its mark (brief: meta-remarks) |
| 81 | `; a `[?]` marks a number that is not a valid reference` → `` | SECOND-PASS Q2: [q123] meta-remark clause "a [?] marks a number that is not a valid reference" removed with its mark (brief: meta-remarks) |
| 60 | `Pā. Sū. 1-6 [?]` → `Pā. Sū. 3-1-26` | SECOND-PASS Q1: [q85] Kannada p.60: "ಹೇತುಮತಿ ಚ (ಪಾ. ಸೂ. 3-1-26)" |
| 63 | `Pā. Sū. 1-484 [?]` → `Pā. Sū. 1-4-84` | SECOND-PASS Q1: [q89] Kannada p.63: "ಅನುರ್ಲಕ್ಷಣೇ । ಪಾ. 1-4-84" |
| 69 | `Pā. Sū. 13-9 [?]` → `Pā. Sū. 1-3-91` | SECOND-PASS Q1: [q104] Kannada p.69: "ದ್ಯುದ್ಭ್ಯೋ ಲುಜಿ (ಪಾ. ಸೂ. 1-3-91)" |
| 76 | `Pā. Sū. 2-65 [?]` → `Pā. Sū. 8-2-65` | SECOND-PASS Q1: [q114] Kannada p.76: "ಮೋಶ್ಚ । ಪಾ. 8-2-65" |
| 78 | `Pā. Sū. 34-91 [?]` → `Pā. Sū. 3-4-91` | SECOND-PASS Q1: [q118] Kannada p.79: "ಸನಾಭ್ಯಾಂವಾಮಾ (ಪಾ. ಸೂ. 3-4-91)" |
| 79 | `Pā. Sū. 8-65 [?]` → `Pā. Sū. 8-2-65` | SECOND-PASS Q1: [q120] Kannada p.79: "ಮೋಶ್ಚ (ಪಾ. ಸೂ. 8-2-65)" |
