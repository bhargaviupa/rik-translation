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

### 2026-11-27 second pass, batch m24-173.tsv
| page | old → new | why |
|---|---|---|
| 111 | `(Ni. 2-10 as read [?])` → `(Ni. 3-9)` | SECOND-PASS Q1: [q24] Kannada p.111 prints (ನಿ. ೩-೯) for the wealth-names |
| 113 | `chandasi pareccāyāmapi*, Pā. Sū. 3-1-?? as read [?]` → `chandasi pareccāyāmapi*, Pā. Sū. 3-1-8-1` | SECOND-PASS Q1: [q25] Kannada p.113 prints (ಪಾ. ಸೂ. ೩-೧-೮-೧) after ಛಂದಸಿ ಪರೇಚ್ಛಾಯಾಮಪಿ |
| 114 | `from the sacrifice [?];` → `from the sacrifice;` | SECOND-PASS Q2: [q26] Kannada p.114 has ದೇವಾ ವೈ ಯಜ್ಞಾದ್ರುದ್ರಮಂತರಾಯನ್, agreeing |
| 114 | `(Tai. Saṃ. 3-6-1-3 as read [?])` → `(Tai. Saṃ. 2-6-8-3)` | SECOND-PASS Q1: [q27] Kannada p.114 prints ತೈ.ಸಂ. ೨-೬ ೮-೩ (hyphen missing), p.115 ೨-೬-೮-೩ |
| 116 | `(Ni. 2-?? as read [?])` → `(Ni. 3-9)` | SECOND-PASS Q1: [q28] Kannada p.116 prints (ನಿ. ೩-೯) after ಕ್ರೋಧನಾಮಗಳಲ್ಲಿ |
| 116 | `Pā. Sū. 61-49-?? as read [?]` → `Pā. Sū. 6-1-49` | SECOND-PASS Q1: [q29] Kannada p.116 prints ಸಿದ್ಧತೇರಪಾರಲೌಕಿಕೇ (ಪಾ. ಸೂ. ೬-೧-೪೯) |
| 117 | `Pā. Sū. 6-1-17 as read [?]; elision` → `Pā. Sū. 4-1-85-3; elision` | SECOND-PASS Q1: [q30] Kannada p.117 prints ದೇವಾದ್ಯಞ್ (ಪಾ.ಸೂ. ೪-೧-೮೫-೩), p.115 ಪಾ. ೪-೧-೮೫. ೩ |
| 120 | `(Ni. 1-10 as read [?])` → `(Ni. 2-21)` | SECOND-PASS Q1: [q31] Kannada p.120 prints (ನಿ. ೨-೨೧) for the cloud-names |
| 123 | `(Ni. 3-?? as read [?])` → `(Ni. 2-11)` | SECOND-PASS Q1: [q32] Kannada p.123 prints (ನಿ. ೨-೧೧) for the house-names |
| 123 | `*nābhyastācchatuḥ*, Pā. Sū. 7-1-78 as read [?])` → `*nābhyastācchatuḥ*)` | SECOND-PASS S3: [q33] Kannada p.123 has ನಾಭ್ಯಸ್ತಾಚ್ಛತುಃ ಎಂಬುದರಿಂದ with no number |
| 123 | `acute by Pā. Sū. 6-1-?? as read [?])` → `acute by Pā. Sū. 6-1-214)` | SECOND-PASS Q1: [q34] Kannada p.123 prints ಈಡವಂದ-- (ಪಾ.ಸೂ ೬-೧-೨೧೪) |
| 127 | `(Ni. 1-1 as read [?])` → `(Ni. 3-9)` | SECOND-PASS Q1: [q35] Kannada p.127 prints (ನಿ. ೩-೯) after ಇಪ್ಪತ್ತೆಂಟು ಧನನಾಮಗಳಲ್ಲಿ |
| 128 | `Pā. Sū. 8-491 as read [?]` → `Pā. Sū. 3-4-91` | SECOND-PASS Q1: [q36] Kannada p.128 prints ಸವಾಭ್ಯಾಂ ನಾಮೌ (ಪಾ. ಸೂ. ೩-೪-೯೧) |
| 132 | `*ārdhadhātukasyeḍ valādeḥ*, Pā. Sū. 7-2-35 as read [?], the augment` → `*ārdhadhātukasyeḍ valādeḥ*, the augment` | SECOND-PASS S3: [q37] Kannada p.132 has ಅರ್ಧಧಾತುಕಸ್ಯೇಡ್ವಲಾದೇಃ ಎಂಬುದರಿಂದ with no number |
| 132 | `Pā. Sū. 8-2-4 as read [?]:` → `Pā. Sū. 8-2-4:` | SECOND-PASS Q1: [q38] Kannada p.132 prints (ಪಾ. ಸೂ. ೮-೨-೪) after ಉದಾತ್ತಸ್ವರಿತಯೋರ್ಯಣಃ… |
| 132 | `*caṅi*, Pā. Sū. 1-11 as read [?]` → `*caṅi*, Pā. Sū. 6-1-11` | SECOND-PASS Q1: [q39] Kannada p.132 prints ಚಜಿ (ಪಾ. ಸೂ. ೬-೧-೧೧) |
| 134 | `(Ni. 2-7 as read [?]); and` → `(Ni. 3-9); and` | SECOND-PASS Q1: [q40] Kannada p.134 prints (ನಿ. ೩-೯) after ಇಪ್ಪತ್ತೆಂಟು ಅನ್ನನಾಮಗಳ ಮಧ್ಯದಲ್ಲಿ |
| 134 | `(Ni. 2-3 as read [?])` → `(Ni. 3-8)` | SECOND-PASS Q1: [q41] Kannada p.134 prints ಆಯುಶ್ಶಬ್ದವು ಮನುಷ್ಯವಾಚಕಗಳಲ್ಲಿ (ನಿ. ೩-೮) |
| 135 | `(Ni. 2-?? as read [?]) among the ten` → `(Ni. 3-9) among the ten` | SECOND-PASS Q1: [q42] Kannada p.135 prints ಭಾಮತೇ (ನಿ. ೩-೯) |
| 136 | `Pā. Sū. 3-9-?? as read [?]` → `Pā. Sū. 3-4-74` | SECOND-PASS Q1: [q43] Kannada p.136 prints ಕ್ರೋಧಿಕರಣೇ ಚ (ಪಾ. ಸೂ. ೩-೪-೭೪) |
| 139 | `(Ni. 10-?? as read [?])` → `(Ni. 10-15)` | SECOND-PASS Q1: [q44] Kannada p.139 prints ಮೃಳತಿರ್ದಾನಕರ್ಮ ವಾ ಪೂಜಾಕರ್ಮ ವಾ (ನಿ. ೧೦-೧೫) |
| 140 | `Pā. Sū. 7-1-39 as read [?]` → `Pā. Sū. 7-1-39` | SECOND-PASS Q1: [q46] Kannada p.140 prints ಸುಪಾಂ ಸುಲುಕ್ (ಪಾ. ಸೂ. ೭ ೧-೩೯), hyphen missing |
| 142 | `(Tai. Saṃ. 25-11 as read [?])` → `(Tai. Saṃ. 2-5-11-9)` | SECOND-PASS Q1: [q47] Kannada p.142/143 prints ತೈ.ಸಂ. ೨-೫-೧೧-೯ after ಬ್ರಾಹ್ಮಣಾಯಾಧಿಬ್ರೂಯಾತ್ |
| 143 | `1-114-1 [and] 1-114-2-3 [as printed, "1-114-2-3-?" read as 2 and 3 [?]]` → `1-114-2-3` | SECOND-PASS Q1: [q48] Kannada p.143 prints only ೧-೧೧೪-೨-೩ ನೇ ಋಕ್ಕುಗಳಲ್ಲಿ; the English 1-114-1 is not in the print and goes with the doubtful form |
| 143 | ` [the Sanskrit of this passage is in small type and corrupt in the print [?]]` → `` | SECOND-PASS Q2: [q49] meta-remark clause removed with its mark (brief: meta-remarks) |
| 144 | `dyaicotastijaḥ*, Pā. Sū. 6-3-?? as read [?]` → `dyaicotastijaḥ*, Pā. Sū. 6-3-135` | SECOND-PASS Q1: [q50] Kannada p.144 prints ದ್ವ್ಯಚೋತಸ್ತಿಜಃ (ಪಾ. ಸೂ. ೬-೩-೧೩೫) |
| 147 | `(Ni. 2-7 as read [?])` → `(Ni. 3-9)` | SECOND-PASS Q1: [q51] Kannada p.147 prints (ನಿ. ೩-೯) after ಇಪ್ಪತ್ತೆಂಟು ಅನ್ನನಾಮಗಳ ಮಧ್ಯದಲ್ಲಿ |
| 147 | `*ito 'tyāt kar* [as printed, [?]]` → `*midacoṃtyāt paraḥ*` | SECOND-PASS Q1: [q52] Kannada p.147 has ಮಿದಚೋಂತ್ಯಾತ್ಪರಃ ಎಂಬುದರಿಂದ ಅಂತ್ಯಾಚ್ಚಿನ ಪರವಾಗಿ (um augment after the last vowel); Sanskrit made by sp_sanskrit.py |
| 147 | `*sarvadhātubhya asun*, Pā. Sū. 3-4-?? as read [?];` → `*sarvadhātubhya asun*;` | SECOND-PASS S3: [q53] Kannada p.147 has ಸರ್ವಧಾತುಭ್ಯ ಅಸುನ್ ಎಂಬುದರಿಂದ with no number |
| 147 | `*bhāve 'nupasargasya*, Pā. Sū. 3-3-?? as read [?]` → `*bhāve 'nupasargasya*, Pā. Sū. 3-3-75` | SECOND-PASS Q1: [q54] Kannada p.148 prints ಭಾವೇಽನುಪಸರ್ಗಸ್ಯ (ಪಾ. ಸೂ. ೩-೩-೭೫) |
| 147 | `*svādiṣv asarvanāmasthāne*, Pā. Sū. 1-4-?? as read [?],` → `*svādiṣv asarvanāmasthāne*,` | SECOND-PASS S3: [q55] Kannada p.148 has no svādiṣv sūtra with a number (it prints ತಸೌ ಮತ್ವರ್ಥೇ ಪಾ. ಸೂ. ೧-೪-೧೯, listed in open.tsv) |
| 149 | `The three Ṛks addressed to Aditi [as read: *aditestisra ṛcaḥ*, the print's wording is doub` → `The first three Ṛks (*āditastisra ṛcaḥ*) are` | SECOND-PASS Q1: [q56] Kannada p.149 reads ಆದಿತಸ್ತಿಸ್ರ ಋಚಃ, with the Kannada prose ಈ ಸೂತ್ರದ ಮೊದಲನೆಯ ಮೂರು ಋಕ್ಕುಗಳನ್ನು (the first three Ṛks) |
| 149 | `(Ā. Sū. 8-6 as read [?]). In the one-day` → `(Ā. Sū. 3-8). In the one-day` | SECOND-PASS Q1: [q57] Kannada p.149 prints ಆ. ೩-೮ after ಶಂ ನೋ ಭವ ಚಕ್ಷಸಾ ಶಂ ನೋ ಅಹ್ನಾ |
| 149 | `*anuvākyā* (Ā. Sū. 8-8 as read [?])` → `*anuvākyā* (Ā. Sū. 9-8)` | SECOND-PASS Q1: [q58] Kannada p.149 prints ಆ. ೯-೮ after ಯಾಜ್ಯಾನುವಾಕ್ಯಾಃ |
| 149 | ` (Ā. Sū. 8-6 as read [?]). And in the *ekāhe*` → `. And in the *ekāhe*` | SECOND-PASS S3: [q59] Kannada p.149 prose (the anuvāda) gives no number there |
| 149 | ` (Ā. Sū. 8-8 as read [?]) shows this` → ` shows this` | SECOND-PASS S3: [q60] Kannada p.149 prose (the anuvāda) gives no number there |
| 153 | `(Tai. Ā. 1-14-1-? as read [?])` → `(Tai. Ā. 1-14-1)` | SECOND-PASS Q1: [q61] Kannada p.153 prints (ತೈ ಆ. ೧-೧೪-೧) |
| 154 | `*divo dyāvā*, Pā. Sū. 6-3 as read [?]` → `*divo dyāvā*, Pā. Sū. 6-3-29` | SECOND-PASS Q1: [q62] Kannada p.154 prints ದಿವೋ ದ್ಯಾವಾ (ಪಾ. ಸೂ ೬-೩-೨೯) |
| 154 | `*gameḥ dve ca*, Pā. Sū. 3-2-?? as read [?]` → `*gameḥ dve ca*, Pā. Sū. 3-2-178-3` | SECOND-PASS Q1: [q63] Kannada p.154 prints ಗಮೇರ್ದ್ವೇ ಚ (ಪಾ ಸೂ. ೩-೨-೧೭೮-೩) |
| 154 | `[as printed: *ādyudāttaś ca*, Pā. 6-1-?? [?]]` → `Pā. Sū. 6-1-189` | SECOND-PASS Q1: [q64] Kannada p.154 prints ಅಭ್ಯಸ್ತಾನಾಮಾದಿಃ (ಪಾ ಸೂ ೬-೧-೧೮೯) ಎಂಬುದರಿಂದ ಆದ್ಯುದಾತ್ತಸ್ವರ at this place |
| 154 | `*kvasuś ca*, Pā. Sū. 3-2-107 as read [?]` → `*kvasuś ca*, Pā. Sū. 3-2-106` | SECOND-PASS Q1: [q65] Kannada p.154 prints ಕ್ವಸುಶ್ಚ (ಪಾ. ಸೂ. ೩-೨-೧೦೬) |
| 154 | `Pā. Sū. 6-4-131 as read [?]` → `Pā. Sū. 6-4-31` | SECOND-PASS Q1: [q66] Kannada p.155 prints ವಸೋಃ ಸಂಪ್ರಸಾರಣಂ (ಪಾ. ಸೂ. ೬-೪-೩೧) |
| 156 | ` (this alternative is in small type, partly doubtful [?])` → `` | SECOND-PASS Q2: [q67] Kannada p.156/158 carries the alternative (ಹಲಾವಯವಭೂತಾನಿ ಕರ್ಷಣಾಯ); meta-remark clause removed with its mark |
| 157 | `'*naraḥ*' and so on (Ni. 2-?? as read [?])` → `'*naraḥ*' and so on (Ni. 3-7)` | SECOND-PASS Q1: [q68] Kannada p.157 prints ಮರ್ಯಾಃ… ಇಪ್ಪತ್ತೈದು ಮನುಷ್ಯನಾಮಗಳ ಮಧ್ಯದಲ್ಲಿ … (ನಿ. ೩-೭) |
| 157 | `twenty-five [as read] names of man (Ni. 2-?? as read [?])` → `twenty-five [as read] names of man (Ni. 3-8)` | SECOND-PASS Q1: [q69] Kannada p.157 prints ಮನುಷ್ಯನಾಮಗಳಲ್ಲಿ (ನಿ. ೩-೮) ನರಃ |
| 159 | `*samāsasya*, Pā. Sū. 6-1-223 as read [?])` → `*samāsasya*)` | SECOND-PASS S3: [q70] Kannada p.159 has ಸಮಾಸಸ್ಯ ಎಂಬುದರಿಂದ with no number |
| 162 | `*ājjaser asuk*, Pā. Sū. 7-1-50 as read [?])` → `*ājjaser asuk*)` | SECOND-PASS S3: [q71] Kannada p.162 has ಆಜ್ಜಸೇರಸುಕ್ ಎಂಬುದರಿಂದ with no number |
| 163 | `*ato guṇe*, Pā. Sū. 6-1-97 as read [?],` → `*ato guṇe*,` | SECOND-PASS S3: [q72] Kannada p.163 has ಅತೋ ಗುಣೇ ಎಂಬುದರಿಂದ with no number |
| 165 | `(Ni. 2-1 as read [?])` → `(Ni. 3-2)` | SECOND-PASS Q1: [q73] Kannada p.165 prints ಇಪ್ಪತ್ತಾರು ಕರ್ಮನಾಮಗಳಲ್ಲಿ (ನಿ. ೩-೨) |
| 168 | `*yasya vibhāṣā*, Pā. Sū. 6-2-15 as read [?]` → `*yasya vibhāṣā*, Pā. Sū. 7-2-15` | SECOND-PASS Q1: [q74] Kannada p.168 prints ಯಸ್ಯ ವಿಭಾಷಾ (ಪಾ. ಸೂ. ೭-೨-೧೫) |
| 168 | `*hṛgrahor bhaś chandasi*, Pā. Sū. 8-2-32 as read [?],` → `*hṛgrahor bhaś chandasi*,` | SECOND-PASS S3: [q75] Kannada p.168 has ಹೃಗ್ರಹೋರ್ಭಶ್ಚಂದಸಿ ಎಂಬುದರಿಂದ with no number |
| 170 | `[Uṇ. 4-?? as read, [?]]` → `(Uṇ. 4-202)` | SECOND-PASS Q1: [q76] Kannada p.170 prints ಪಾತೇರ್ಬಲೇ ಜುಟ್ಚ । ಉ. ೪-೨೦೨ |
| 172 | `draw up the water (Ni. 2-?? as read [?])` → `draw up the water (Ni. 7-24)` | SECOND-PASS Q1: [q77] Kannada p.172 prints (ನಿ. ೭-೨೪) after the explanation of ಹರಯಃ |
| 172 | `*sampadādibhyaḥ kvip*, Vārt. 3-3-108 as read [?],` → `*sampadādibhyaḥ kvip*, Vārt. 2233,` | SECOND-PASS Q1: [q78] Kannada p.172 prints ಸಂಪದಾದಿಭ್ಯಃ ಕ್ವಿಪ್ (ವಾ. ೨೨೩೩) |
| 173 | `*jñityādir nityam*, Pā. Sū. 6-1-193 as read [?]` → `*jñityādir nityam*, Pā. Sū. 6-1-197` | SECOND-PASS Q1: [q79] Kannada p.173 prints ಇತ್ಯಾದಿರ್ನಿತ್ಯಮ್ (ಪಾ. ಸೂ. ೬-೧-೧೯೭) |
| 176 | `*ur at*, Pā. Sū. 7-4-66 as read [?],` → `*ur at*,` | SECOND-PASS S3: [q80] Kannada p.176 has ಉರತ್ ಸೂತ್ರದಿಂದ with no number |
| 178 | `वर्ग—९, १०, ११, १२ ॥ *(small numerals as printed; read 9, 10, 11, 12 — [?]; the print appe` → `वर्ग—८, ९, १०, ११, १२ ॥` | SECOND-PASS Q1: [q81] Kannada p.178 prints ವರ್ಗ-೮, ೯, ೧೦, ೧೧, ೧೨ (five numerals); Devanagari made by sp_sanskrit.py from the Kannada |
| 181 | `Sūktas 116–125 [as read: "1-116-?" to "1-126-?"] (altogether 11 sūktas, ... Ṛks) [the nume` → `Sūktas 116–125 (altogether 146 Ṛks), Sūkta 126, Ṛks 1–5 (5 Ṛks), and Maṇḍala 9, Sūkta 74 (` | SECOND-PASS Q1: [q82] Kannada p.181 prints ಪ್ರಥಮಮಂಡಲದ ೧೧೬-೧೨೫ ನೆಯ ಸೂಕ್ತಗಳಿಗೂ (ಒಟ್ಟು ೧೪೬ ಋಕ್ಕುಗಳು) ೧೨೬ ನೆಯ ಸೂಕ್ತದಲ್ಲಿ ೧-೫ ಋಕ್ಕುಗಳಿಗೂ (೫) ೯ನೆಯ ಮಂಡಲದಲ್ಲಿ ೭೪ ನೆಯ ಸೂಕ್ತಕ್ಕೂ (೯) ಒಟ್ಟ |
| 181 | `Ṛ. Saṃ. 1-126-3-? ; 1-126-3-? ; 8-?-? ; 2-10-? ; 10-?-? ; 1-126-3-? ; 1-126-3-? ; 6-26-1-?` → `Ṛ. Saṃ. 1-126-2; 1-126-3; 6-26-1; 7-9-10; 11-25-10; 1-117-6; 1-211-13; 1-116-7; 9-74-8; 1-` | SECOND-PASS Q1: [q83] Kannada p.181 prints ಋ. ಸಂ. ೧-೧೨೬-೨; ೧-೧೨೬-೩; ೬-೨೬-೧; ೭-೯-೧೦; ೧೧-೨೫-೧೦; ೧-೧೧೭-೬; ೧-೨೧೧-೧೩; ೧-೧೧೬-೭; ೯-೭೪-೮; ೧-೧೨೬-೪; ೧-೧೮-೧ : ೧-೧೧೨-೧೧; ೧೦-೬೧-೧೬; ೧೦-೧೪೩-೧ |
| 181 | `altogether twenty-?? Ṛks in the 10th maṇḍala of the Ṛgveda, Sūktas 20–26? [as read: "10-20` → `altogether 66 Ṛks in the 10th maṇḍala of the Ṛgveda, Sūktas 20–26` | SECOND-PASS Q1: [q84] Kannada p.181 prints ಹತ್ತನೆಯ ಮಂಡಲದ ೨೦-೨೬ ಸೂಕ್ತಗಳಲ್ಲಿರುವ ಒಟ್ಟು ೬೬ ಋಕ್ಕುಗಳಿಗೆ ಋಷಿಯು |
| 181 | `Ṛ. Saṃ. 1-126-3-? and others *(numerals not legible)* [?]` → `Ṛ. Saṃ. 1-51-3; 1-112-19; 1-116-1; 1-117-20; 8-9-15; 10-39-7; 10-65-12; 10-20-10; 10-23-7;` | SECOND-PASS Q1: [q85] Kannada p.181 prints ಋ. ಸಂ. ೧-೫೧-೩; ೧-೧೧೨-೧೯ : ೧-೧೧೬-೧ : ೧-೧೧೭-೨೦ : ೮-೯-೧೫; ೧೦-೩೯-೭; ೧೦-೬೫-೧೨; ೧೦-೨೦-೧೦; ೧೦-೨೩-೭; ೧೦-೨೩-೬ : ೧೦-೨೪-೪ |
| 182 | `(Ni. 3-?? as read [?]) and among` → `(Ni. 2-10) and among` | SECOND-PASS Q1: [q86] Kannada p.182 prints ಹದಿನಾರು ಅಂತರಿಕ್ಷನಾಮಗಳಲ್ಲಿಯೂ (ನಿ. ೨-೧೦) |
| 183 | `*nalopo naṅaḥ*, Pā. Sū. 6-3-73 as read [?])` → `*nalopo naṅaḥ*)` | SECOND-PASS S3: [q87] Kannada p.184 has ನಲೋಪೋಽನಞಃ ಎಂಬುದರಿಂದ with no number |
| 184 | `*idito num dhātoḥ*, Pā. Sū. 7-1-58 as read [?],` → `*idito num dhātoḥ*,` | SECOND-PASS S3: [q88] Kannada p.184 has ಇದಿತೋ ನುಮ್ ಧಾತೋಃ ಎಂಬುದರಿಂದ with no number |
| 184 | `*kvip vaci…*, Pā. Sū. 3-2-76 as read [?]` → `*kvip vaci…*, Pā. Sū. 3-2-178-1` | SECOND-PASS Q1: [q89] Kannada p.184 prints ಕ್ವಿಬ್‌ವಚಿಪ್ರಚ್ಛಾ- (ಪಾ. ಸೂ. ೩-೨-೧೭೮-೧) |
| 185 | `*parasmaipadānāṃ ṇalatusus…*, Pā. Sū. 3-4-82 as read [?],` → `*parasmaipadānāṃ ṇalatusus…*,` | SECOND-PASS S3: [q90] Kannada p.185 has ಪರಸ್ಮೈಪದಾನಾಂ—ಸೂತ್ರದಿಂದ with no number |
| 186 | `(Ai. Brā. 1-8 as read [?])` → `(Ai. Brā. 4-7)` | SECOND-PASS Q1: [q91] Kannada p.186/188 prints ಐ.ಬ್ರಾ. ೪-೭ for ಪ್ರಜಾಪತಿರ್ವೈ ಸೋಮಾಯ ರಾಜೇ |
| 187 | `(Ni. 6-16? as read [?])` → `(Ni. 6-16)` | SECOND-PASS Q1: [q92] Kannada p.187 prints ನಿರುಕ್ತದಲ್ಲಿ (ನಿ. ೬-೧೬) |
| 187 | `'*vivāk*' (Ni. 2-?? as read [?])` → `'*vivāk*' (Ni. 3-9)` | SECOND-PASS Q1: [q93] Kannada p.188 prints ವಿವಾಕ್ ಎಂಬ ನಲವತ್ತುನಾಲ್ಕು ಸಂಗ್ರಾಮನಾಮಗಳಲ್ಲಿ (ನಿ. ೩-೯) |
| 187 | `(Ni. 7-?? as read [?])` → `(Ni. 9-23)` | SECOND-PASS Q1: [q94] Kannada p.188 prints ಆಜಿ ಶಬ್ದ ಮತ್ತು ಪ್ರಧನ ಶಬ್ದಗಳ ಅರ್ಥವಿವರಣೆಯು (ನಿ ೯-೨೩) |
| 188 | `(Ai. Brā. 4-7-1 [as read; [?]])` → `(Ai. Brā. 4-7-1)` | SECOND-PASS Q1: [q95] Kannada p.188 prints (ಐ.ಬ್ರಾ. ೪-೭-೧) |
| 190 | `*ūtiyūtijūtisātihetikīrtayaś ca*, Pā. Sū. 3-3-97 as read [?]` → `*ūtiyūtijūtisātihetikīrtayaś ca*, Pā. Sū. 3-3-96` | SECOND-PASS Q1: [q96] Kannada p.190 prints (ಪಾ. ಸೂ. ೩-೩-೯೬) |
| 190 | `*chandasy ubhayathā*, Pā. Sū. 3-4-117 as read [?]` → `*chandasy ubhayathā*, Pā. Sū. 3-4-116` | SECOND-PASS Q1: [q97] Kannada p.190 prints ಛಂದಸ್ಯುಭಯಥಾ (ಪಾ. ಸೂ. ೩-೪-೧೧೬) |
| 191 | `*parasmaipadānāṃ ṇalatusus…*, Pā. Sū. 3-4-82 as read [?],` → `*parasmaipadānāṃ ṇalatusus…*,` | SECOND-PASS S3: [q98] Kannada p.191 has ಪರಸ್ಮೈಪದಾನಾಂ—ಸೂತ್ರದಿಂದ with no number |
| 191 | `*aco 'ñṇiti*, Pā. Sū. 7-2-115 as read [?];` → `*aco 'ñṇiti*;` | SECOND-PASS S3: [q99] Kannada p.191 has ಅಚೋಞ್ಞಿತಿ ಸೂತ್ರದಿಂದ with no number |
| 193 | `gives up his wealth [?],` → `gives up his wealth,` | SECOND-PASS Q2: [q102] Kannada p.193 bhāvārtha ಧನವನ್ನು (ಬಹಳ ಕ್ಲೇಶದಿಂದ ಕೊಡುವಂತೆ) agrees |
| 193 | `1-116-3, 1-117-14, 6-62-6 [as read; [?]]` → `1-116-3, 1-117-4, 6-62-6` | SECOND-PASS Q1: [q103] Kannada p.193 prints ಋ. ಸಂ. ೧-೧೧೬-೩; ೧-೧೧೭-೪; ೬-೬೨-೬ |
| 193 | `the name of Tugra occurs, and also, as *Taugrya*, in Ṛ. Saṃ. 1-182-5-? ; 1-182-5-? [as rea` → `the name of Tugra occurs in Ṛ. Saṃ. 8-3-23; 8-74-14, and also, as *Taugrya*, in Ṛ. Saṃ. 1-` | SECOND-PASS Q1: [q104] Kannada p.193-194 prints ತುಗ್ರನೆಂಬ ಹೆಸರು ಋ. ಸಂ. ೮-೩-೨೩; ೮-೭೪-೧೪ … ಶೌಗ್ರನೆಂಬ ಹೆಸರು ೧-೧೧೭-೧೫; ೧-೧೧೮-೬; ೧-೧೧೨-೫; ೧-೧೧೨-೬; ೭-೫-೨೨; ೧೦-೩೯-೪ |
| 194 | `Ṛ. Saṃ. 1-116-? ; 1-117-? ; 1-182-5-? ; 1-182-5-? ; 6-5-22-? ; 10-39-4-? [numerals too sma` → `Ṛ. Saṃ. 1-117-15; 1-118-6; 1-112-5; 1-112-6; 7-5-22; 10-39-4` | SECOND-PASS Q1: [q105] Kannada p.194 prints the six references 1-117-15; 1-118-6; 1-112-5; 1-112-6; 7-5-22; 10-39-4 (six, as the English has six places) |
| 196 | `(Ni. 4-?? as read [?])` → `(Ni. 4-17)` | SECOND-PASS Q1: [q106] Kannada p.196 prints ರಯಿರಿತಿ ಧನಾಮ ರಾತೇರ್ದಾನಕರ್ಮಣಃ (ನಿ. ೪-೧೭) |
| 197 | `Pā. Sū. 6-2-13 as read [?]` → `Pā. Sū. 7-2-13` | SECOND-PASS Q1: [q107] Kannada p.197 prints ಕೃಸೃಭ್ಯ— (ಪಾ. ಸೂ. ೭-೨-೧೩) |
| 197 | `*ugidacāṃ sarvanāmasthāne 'dhātoḥ*, Pā. Sū. 7-1-70 as read [?];` → `*ugidacāṃ sarvanāmasthāne 'dhātoḥ*;` | SECOND-PASS S3: [q108] Kannada p.197 has ಉಗಿತ್ತಾದುದರಿಂದ ನುಮಾಗಮ with no number |
| 197 | `*hal-ṅyābbhyo dīrghāt sutisyapṛktaṃ hal*, Pā. Sū. 6-1-68 as read [?],` → `*hal-ṅyābbhyo dīrghāt sutisyapṛktaṃ hal*,` | SECOND-PASS S3: [q109] Kannada p.197 has ಹಲ್ ಜ್ಯಾಭ್ಯೋ—ಸೂತ್ರದಿಂದ with no number |
| 197 | `*saṃyogāntasya lopaḥ*, Pā. Sū. 8-2-23 as read [?];` → `*saṃyogāntasya lopaḥ*;` | SECOND-PASS S3: [q110] Kannada p.197 has ಸಂಯೋಗಾಂತ ಲೋಪದಿಂದ with no number |
| 197 | `*bahulaṃ chandasi*, Pā. Sū. 7-3-97 as read [?],` → `*bahulaṃ chandasi*,` | SECOND-PASS S3: [q111] Kannada p.197 has ಬಹುಲಂ ಛಂದಸಿ ಎಂಬುದರಿಂದ with no number |
| 198 | `*ano nuṭ*, Pā. Sū. 6-3-?? as read [?]` → `*ano nuṭ*, Pā. Sū. 8-2-16` | SECOND-PASS Q1: [q112] Kannada p.198 prints ಅನೋ ನುಟ್ (ಪಾ. ಸೂ. ೮-೨-೧೬) |
| 200 | `(Ni. 1-?? as read [?]) — *kṣapaḥ*` → `(Ni. 2-18) — *kṣapaḥ*` | SECOND-PASS Q1: [q113] Kannada p.200 prints ಕ್ಷಪಶಬ್ದವು (ನಿ. ೨-೧೮) |
| 200 | `'*haya*' and so on (Ni. 1-?? as read [?])` → `'*haya*' and so on (Ni. 2-27)` | SECOND-PASS Q1: [q114] Kannada p.200 prints (ನಿ. ೨-೨೭) ಪತಂಗಶಬ್ದವು |
| 200 | `'*viyat*' and so on (Ni. 1-?? as read [?])` → `'*viyat*' and so on (Ni. 2-10)` | SECOND-PASS Q1: [q115] Kannada p.200 prints ಧನ್ವಶಬ್ದವು (ನಿ ೨-೧೦) |
| 202 | `*udāttayaṇo hal-pūrvāt*, Pā. Sū. 6-1-164 as read [?]` → `*udāttayaṇo hal-pūrvāt*, Pā. Sū. 6-1-174` | SECOND-PASS Q1: [q116] Kannada p.202 prints ಉದಾತ್ತಯಣೋ ಹಲ್ಪೂರ್ವಾತ್ (ಪಾ. ಸೂ ೬-೧-೧೭೪) |
| 203 | `*āmantritasya ca*, Pā. Sū. 1-198 as read [?]` → `*āmantritasya ca*, Pā. Sū. 6-1-198` | SECOND-PASS Q1: [q117] Kannada p.203 prints ಅಮಂತ್ರಿತಸ್ಯ (ಪಾ ಸೂ ೬-೧-೧೯೮) |
| 206 | `nighāta, since *tiṅ* after *tat*, Pā. Sū. 8-1-28 as read [?])` → `nighāta, since *tiṅ* after *tat*)` | SECOND-PASS S3: [q118] Kannada p.206 has ತಿಙತಿಙಃ ಎಂಬುದರಿಂದ ನಿಘಾತಸ್ವರ with no number |
| 206 | `*hṛgrahor bhaś chandasi*, Pā. Sū. 8-2-32 as read [?],` → `*hṛgrahor bhaś chandasi*,` | SECOND-PASS S3: [q119] Kannada p.206 has ಹೃಗ್ರಹೋರ್ಭಶ್ಚಂದಸಿ ಎಂಬುದರಿಂದ with no number |
| 207 | `Pā. Sū. 3-2-67 as read [?] [as printed "*vasvekājāḍ…*"]` → `Pā. Sū. 7-2-67` | SECOND-PASS Q1: [q120] Kannada p.207 prints ವಸ್ವೇಕಾಚಾ- (ಪಾ. ಸೂ. ೭-೨-೬೭) |
| 208 | `That horse made victory for his [son's/grandson's — doubtful [?]] ... This is here set for` → `That horse made for him a mighty victory. This is here set forth.` | SECOND-PASS Q1: [q121] Kannada p.208 (Sāyaṇa) ಸ ಚಾಶ್ವಸ್ತಸ್ಯ ಪ್ರೌಢಂ ಜಯಂ ಚಕಾರ: the horse made a great victory for him |
| 210 | `(Ni. 1-?? as read [?]) — '*paidvaḥ` → `(Ni. 2-27) — '*paidvaḥ` | SECOND-PASS Q1: [q122] Kannada p.210 prints ಪೈದ್ವಃ ಎಂಬ ಪದವು ಅಶ್ವನಾಮಗಳಲ್ಲಿ (ನಿ. ೨-೨೭) |
| 211 | `*yadvṛttān nityam*, Pā. Sū. 8-1-66 as read [?],` → `*yadvṛttān nityam*,` | SECOND-PASS S3: [q123] Kannada p.211 has ಯದ್ವೃತ್ತಾನ್ ಎಂಬುದರಿಂದ ನಿಘಾತಸ್ವರಪ್ರತಿಷೇಧ with no number |
| 212 | `*bahuvrīhau prakṛtyā pūrvapadam*, Pā. Sū. 6-2-1 as read [?])` → `*bahuvrīhau prakṛtyā pūrvapadam*)` | SECOND-PASS S3: [q124] Kannada p.212 has ಬಹುವ್ರೀಹೌ ಪ್ರಕೃತ್ಯಾ ಪೂರ್ವಪದಂ ಎಂಬುದರಿಂದ with no number |
| 212 | `*ūṭ id dyādoḥ*, Pā. Sū. 6-1-?? as read [?]` → `*ūṭ id dyādoḥ*, Pā. Sū. 7-1-100` | SECOND-PASS Q1: [q125] Kannada p.212 prints ಋತ ಇದ್ಧಾತೋಃ (ಪಾ. ಸೂ. ೭-೧-೧೦೦) for the i for ṛ of the root |
| 212 | `*bahulaṃ chandasi*, Pā. Sū. 6-1-34 as read [?],` → `*bahulaṃ chandasi*,` | SECOND-PASS S3: [q126] Kannada p.212 has ಬಹುಲಂ ಛಂದಸಿ ಎಂಬುದರಿಂದ ಸಂಪ್ರಸಾರಣ with no number |
| 212 | `*yato 'nāvaḥ*, Pā. Sū. 61-213 as read [?]` → `*yato 'nāvaḥ*, Pā. Sū. 6-1-213` | SECOND-PASS Q1: [q127] Kannada p.212 prints ಯತೋಽನಾವಃ (ಪಾ ಸೂ. ೬-೧-೨೧೩) |
| 213 | `long ago, ... [the text is doubtful here: *kaṃsāśirohitajñānaḥ* [?]] praised` → `long ago, with his knowledge hidden by darkness (*tamasā tirohitajñānaḥ*), praised` | SECOND-PASS Q1: [q128] Kannada p.213 (Sāyaṇa) reads ಕಕ್ಷೀವಾನೃಷಿಃ ಪುರಾ ತಮಸಾತಿರೋಹಿತಜ್ಞಾನಃ ಸನ್ |
| 215 | `(Ni. 2-9 as read [?])` → `(Ni. 3-9)` | SECOND-PASS Q1: [q129] Kannada p.215 prints ಪಾಜಃ ಎಂಬ ಪದವು (ನಿ. ೩-೯) ಬಲನಾಮಗಳಲ್ಲಿ |
| 216 | `it is [the mark] of being pleasing [?].` → `it does not leak out.` | SECOND-PASS Q1: [q130] Kannada p.216 prints ಇದರಲ್ಲಿ ಮದ್ಯವನ್ನು ಹಾಕಿಡುವುದರಿಂದ ಅದು ಸೋರಿಹೋಗದಂತೆ ಇರುತ್ತದೆ |
| 216 | `as if by the form of ... [reading doubtful [?]] —` → `as water comes from a well, because the horse's hoof is round like the form of a well —` | SECOND-PASS Q1: [q131] Kannada p.216 prints ಕುದುರೆಯ ಗೊರಸು ಭಾವಿಯ ಆಕಾರದಂತೆ ದುಂಡಾಗಿ ಇರುವ ಕಾರಣ ಭಾವಿಯಿಂದ ನೀರು ಒದಗಿಬರುವಹಾಗೆ |
| 219 | `*śeṣe lopaḥ*, Pā. Sū. 7-2-90 as read [?],` → `*śeṣe lopaḥ*,` | SECOND-PASS S3: [q132] Kannada p.219 has ಶೇಷೇ ಲೋಪಃ ಎಂಬುದರಿಂದ with no number |
| 219 | `*ṛduror ap*, Pā. Sū. 3-3-576 as read [?]` → `*ṛduror ap*, Pā. Sū. 3-3-57` | SECOND-PASS Q1: [q133] Kannada p.219 prints ಋದೋರಪ್ (ಪಾ. ಸೂ ೩-೩-೫೭) |
| 219 | `*adiprabhṛtibhyaḥ śapaḥ*, Pā. Sū. 2-4-72 as read [?]` → `*adiprabhṛtibhyaḥ śapaḥ*, Pā. Sū. 2-4-73` | SECOND-PASS Q1: [q134] Kannada p.219 prints ಅದಿಪ್ರಭೃತಿಭ್ಯಃ ಶಪಃ (ಪಾ. ಸೂ ೨-೪-೭೩) |
| 219 | `*sārvadhātukam apit*, Pā. Sū. 1-2-4 as read [?],` → `*sārvadhātukam apit*,` | SECOND-PASS S3: [q135] Kannada p.219 has ಸಾರ್ವಧಾತುಕಮಪಿತ್ ಎಂಬುದರಿಂದ with no number |
| 219 | `*aci śnudhātubhruvāṃ yvoriyaṅuvaṅau*, Pā. Sū. 6-4-77 as read [?]` → `*aci śnudhātubhruvāṃ yvoriyaṅuvaṅau*, Pā. Sū. 6-4-73` | SECOND-PASS Q1: [q136] Kannada p.219 prints ಅಚಿಶ್ನುಧಾತುಭ್ರುವಾಂ (ಪಾ. ಸೂ. ೬-೪-೭೩) |
| 219 | `*tasthasthamipāṃ tāṃtaṃtāmaḥ*, Pā. Sū. 3-4-101 as read [?],` → `*tasthasthamipāṃ tāṃtaṃtāmaḥ*,` | SECOND-PASS S3: [q137] Kannada p.219 has ತಸ್ಥಸ್ಥ—ಎಂಬುದರಿಂದ ತಮಾದೇಶ with no number |
| 220 | `*tudādibhyaḥ śaḥ*, Pā. Sū. 3-1-77 as read [?],` → `*tudādibhyaḥ śaḥ*,` | SECOND-PASS S3: [q138] Kannada p.220 has ತುದಾದಿಭ್ಯಃ ಶಃ ಎಂಬುದರಿಂದ with no number |
| 222 | `twelve names of day (*ahar*) (Ni. 1-?? as read [?])` → `twelve names of day (*ahar*) (Ni. 2-21)` | SECOND-PASS Q1: [q139] Kannada p.222 prints ಘ್ರಂಸ ಶಬ್ದವು ಹನ್ನೆರಡು ಅಹರ್ನಾಮಗಳಲ್ಲಿ (ನಿ. ೨-೨೧) |
| 223 | `names of day (Ni. 1-?? as read [?]).` → `names of day (Ni. 2-20).` | SECOND-PASS Q1: [q140] Kannada p.223 prints ಫ್ರಂಸ ಶಬ್ದವೂ ಅಹರ್ನಾಮಗಳಲ್ಲಿ ಪಠಿತವಾಗಿರುವುದು (ನಿ. ೨-೨೦) |
| 224 | `(Ni. 2-7 as read [?]). '*pituḥ` → `(Ni. 3-9). '*pituḥ` | SECOND-PASS Q1: [q141] Kannada p.224 prints ಪಿತುಶಬ್ದವು (ನಿ. ೩-೯) ಅನ್ನ ನಾಮಗಳಲ್ಲಿ |
| 224 | `(Ni. 1-?? as read [?]): the word *pitu*` → `(Ni. 9-25): the word *pitu*` | SECOND-PASS Q1: [q142] Kannada p.224 prints ಪಿತುರಿತ್ಯನ್ನನಾಮ ಪಾತೇರ್ವಾ, ಪಿಬತೇರ್ವಾ ಪ್ಯಾಯತೇರ್ವಾ (ನಿ. ೯-೨೫) |
| 226 | `*tad asyāsty asmin*, Pā. Sū. 5-2-94 as read [?],` → `*tad asyāsty asmin*,` | SECOND-PASS S3: [q143] Kannada p.226 has ತದಸ್ಯಾಸ್ತಿ ಸೂತ್ರದಿಂದ ಮತುಪ್ with no number |
| 226 | `*ugitaś ca*, Pā. Sū. 4-1-6 as read [?],` → `*ugitaś ca*,` | SECOND-PASS S3: [q144] Kannada p.226 has ಉಗಿತಶ್ಚ ಎಂಬುದರಿಂದ with no number |
| 227 | `*pṛṣodarādīni yathopadiṣṭam*, Pā. Sū. 6-3-109 as read [?])` → `*pṛṣodarādīni yathopadiṣṭam*)` | SECOND-PASS S3: [q145] Kannada p.226/227 has ಪೃಷೋದರಾದೀನಿ ಯಥೋಪದಿಷ್ಟಮ್ ಎಂಬುದರಿಂದ with no number |
| 227 | `*gatir anantaraḥ*, Pā. Sū. 6-2-49 as read [?],` → `*gatir anantaraḥ*, Pā. Sū. 6-2-46,` | SECOND-PASS Q1: [q146] Kannada p.227 prints ಗತಿರನಂತರಃ (ಪಾ. ೬-೨-೪೬) |
| 227 | `*striyāṃ ktin*, Pā. Sū. 3-3-94 as read [?],` → `*striyāṃ ktin*,` | SECOND-PASS S3: [q147] Kannada p.227 has ಸ್ತ್ರೀಯಾಂ ಕ್ತಿನ್ ಎಂಬುದರಿಂದ with no number |
| 228 | `you impelled (that well, after the father [?])` → `you impelled (you brought, afterwards, that well)` | SECOND-PASS Q1: [q148] Kannada p.229 prints ಅನುದೇಥಾಂ—ಪ್ರೇರಿಸಿದಿರಿ (ತಂದಿರಿ ಅನಂತರ ಆ ಬಾವಿಯನ್ನು) |
| 230 | `Ṛ. Saṃ. 1-85-11-? [numerals partly illegible [?]]` → `Ṛ. Saṃ. 1-85-11` | SECOND-PASS Q1: [q149] Kannada p.230 prints ಋ. ಸಂ. ೧-೮೫-೧೧ |
| 230 | `*tudādibhyaḥ śaḥ*, Pā. Sū. 3-1-77 as read [?],` → `*tudādibhyaḥ śaḥ*, Pā. Sū. 3-1-67,` | SECOND-PASS Q1: [q150] Kannada p.230 prints ತುದಾದಿಭ್ಯಃ ಶಃ (ಪಾ. ಸೂ. ೩-೧-೬೭) |
| 230 | `*āto ṅitaḥ*, Pā. Sū. 7-2-81 as read [?],` → `*āto ṅitaḥ*,` | SECOND-PASS S3: [q151] Kannada p.230 has ಆತೋಜಿತಃ ಎಂಬುದರಿಂದ with no number |
| 231 | `*hetumati ca*, Pā. Sū. 3-1-66 as read [?],` → `*hetumati ca*, Pā. Sū. 3-1-26,` | SECOND-PASS Q1: [q152] Kannada p.231 prints (ಪಾ. ಸೂ. ೩-೧-೨೬) ಎಂಬುದರಿಂದ ಣಿಚ್ |
| 231 | `*eco 'yavāyāvaḥ*, Pā. Sū. 6-1-78 as read [?],` → `*eco 'yavāyāvaḥ*,` | SECOND-PASS S3: [q153] Kannada p.231 has ಏಚೋಯವಾಯಾವಃ ಸೂತ್ರದಿಂದ with no number |
| 235 | `5-64-5-? [?]` → `5-74-5` | SECOND-PASS Q1: [q154] Kannada p.235 prints ಋ. ಸಂ. ೫-೭೪-೫; ೭-೬೮-೬ ಮೊದಲಾದ |
| 235 | `7-?-? [?]` → `7-68-6` | SECOND-PASS Q1: [q155] Kannada p.235 prints ಋ. ಸಂ. ೫-೭೪-೫; ೭-೬೮-೬ ಮೊದಲಾದ |
| 235 | ` [the Sanskrit here is small type, partly doubtful [?]]` → `` | SECOND-PASS Q2: [q156] meta-remark clause removed with its mark (brief: meta-remarks) |
| 236 | `(Ni. 2-7 as read [?])` → `(Ni. 3-9)` | SECOND-PASS Q1: [q157] Kannada p.236 prints (ನಿ. ೩-೯) ಉಕ್ತವಾಗಿರುವುದರಿಂದ ಅನ್ನವೆಂದೂ ಅರ್ಥ |
| 236 | `*ur at*, Pā. Sū. 7-4-66 as read [?],` → `*ur at*,` | SECOND-PASS S3: [q158] Kannada p.236 has ಉರತ್ ಸೂತ್ರದಿಂದ with no number |
| 236 | `*tasthasthamipāṃ tāṃtaṃtāmaḥ*, Pā. Sū. 3-4-101 as read [?];` → `*tasthasthamipāṃ tāṃtaṃtāmaḥ*;` | SECOND-PASS S3: [q159] Kannada p.236 has ತಮಾದೇಶ with no sūtra number |
| 236 | `*tudādibhyaḥ śaḥ*, Pā. Sū. 6-1-39 as read [?];` → `*tudādibhyaḥ śaḥ*;` | SECOND-PASS S3: [q160] Kannada p.236 has ತುದಾದಿಯಾದುದರಿಂದ ಶ ವಿಕರಣ with no number |
| 236 | `*śemuchādīnām*, Pā. Sū. 7-1-59 as read [?],` → `*śemuchādīnām*, Pā. Sū. 7-1-56,` | SECOND-PASS Q1: [q161] Kannada p.236 prints ಶೇಮುಚಾದೀನಾಮ್ (ಪಾ ಸೂ. ೭-೧-೫೬) |
| 237 | `*idito num dhātoḥ*, Pā. Sū. 7-1-58 as read [?],` → `*idito num dhātoḥ*,` | SECOND-PASS S3: [q162] Kannada p.237 has ಇದಿತ್ತಾದುದರಿಂದ ನುಮಾಗಮ with no number |
| 241 | `*tad asyāsty asmin*, Pā. Sū. 5-2-94 as read [?];` → `*tad asyāsty asmin*;` | SECOND-PASS S3: [q163] Kannada p.241 has no number there |
| 241 | `*jyāvṛñbhyām ūthan*, Uṇ. 2-?? as read [?],` → `*jyāvṛñbhyām ūthan*, Uṇ. 1-163,` | SECOND-PASS Q1: [q164] Kannada p.241 prints ಜ್ಯವೃಞ್ಭ್ಯಾಮೂಥನ್ (ಉ.ಸೂ ೧-೧೬೩) |
| 241 | `*vido laṭo vā*, Pā. Sū. 3-4-83 as read [?],` → `*vido laṭo vā*,` | SECOND-PASS S3: [q165] Kannada p.241 has ಲಡರ್ಥದಲ್ಲಿ ಶತೃಪ್ರತ್ಯಯ ಬಂದಾಗ with no number for this sūtra (ವಿದೇಃ ಶತುರ್ವಸುಃ is given 7-1-36) |
| 241 | `*hoḍhaḥ*, Pā. Sū. 1-4-1 as read [?],` → `*hoḍhaḥ*,` | SECOND-PASS S3: [q166] Kannada p.241 has ಹೋಢಃ ಎಂಬುದರಿಂದ with no number |
| 242 | `*asaṃyogāl liṭ kit*, Pā. Sū. 1-2-5 as read [?],` → `*asaṃyogāl liṭ kit*,` | SECOND-PASS S3: [q169] Kannada p.242 has ಅಸಂಯೋಗಾಲ್ಲಿಟ್ ಕಿತ್ ಎಂಬುದರಿಂದ with no number |
| 242 | `*idito num dhātoḥ*, Pā. Sū. 7-1-58 as read [?],` → `*idito num dhātoḥ*,` | SECOND-PASS S3: [q170] Kannada p.242 has ಇದಿತೋನುಮ್ ಧಾತೋಃ ಎಂಬುದರಿಂದ with no number |
| 244 | `the *ṭi* elision by Pā. Sū. 6-4-?? as read [?])` → `the *ṭi* elision by Pā. Sū. 6-4-167)` | SECOND-PASS Q1: [q171] Kannada p.244 prints ಅಪತ್ಯಾರ್ಥೇಽಣ್ಯನ್ । ಪಾ. ೬-೪-೧೬೭ । ಇತಿ ಪ್ರಕೃತಿಭಾವಾಟ್ಟಲೋಪಾಭಾವಃ |
| 244 | ` (Ni. 2-1 as read [?]), *daṃsaḥ*` → `, *daṃsaḥ*` | SECOND-PASS S3: [q172] Kannada p.244 has ಇಪ್ಪತ್ತಾರು ಕರ್ಮನಾಮಗಳಲ್ಲಿ ದಂಸಃ with no number |
| 246 | `eight hundred and ten [?]` → `eight hundred and ten` | SECOND-PASS Q2: [q173] Kannada p.246 prints ಒಂಬತ್ತು ಸಲ ತೊಂಬತ್ತು 9X90=810 (ಎಂಟನೂರು ಹತ್ತು), agreeing |

### 2026-11-27 second pass, batch m29-178.tsv
| page | old → new | why |
|---|---|---|
| 247 | `(Ṛ. Saṃ. 1-80-16 [as read; [?]])` → `(Ṛ. Saṃ. 1-80-16)` | SECOND-PASS Q1: [q29] Kannada p.247 prints (ಋ. ಸಂ. ೧-೮೦-೧೬) |
| 247 | `1-116-12 [as read] and 1-117-22 [as read] [the numerals are small [?]].` → `1-116-12 and 1-117-22.` | SECOND-PASS Q1: [q30] Kannada p.247 prints ೧-೧೧೬-೧೨ ಮತ್ತು ೧-೧೧೭-೨೨ |
| 247 | `1-84-13 ; 1-80-16-? ; 1-80-16-? ; 1-117-22 ; 1-116-12 [as read, partly illegible [?]] and ` → `1-80-16 ; 1-84-13 ; 1-84-14 ; 1-116-12 ; 1-117-22 ; 1-119-9 and others; and in the Taittir` | SECOND-PASS Q1: [q31-q33] Kannada p.247 prints the whole list (ಋಗ್ವೇದ ಸಂಹಿತೆಯಲ್ಲಿ ೧-೮೦-೧೬ … ಬೃಹದಾರಣ್ಯಕೋಪನಿಷತ್ ೨-೫-೨೨ ; ೪-೫-೨೮); English list taken from it and the blur note dro |
| 249 | `Uṇ. 1-?? as read [?]` → `Uṇ. 4-442` | SECOND-PASS Q1: [q34] Kannada p.249 prints (ಉ. ಸೂ. ೪-೪೪೨) for ಋತನ್ಯಜ್ಜಿ |
| 250 | `Pā. Sū. 6-2-117 as read [?]` → `Pā. Sū. 7-2-117` | SECOND-PASS Q1: [q35] Kannada p.250 prints ತದ್ಧಿತೇಷ್ವಚಾಮಾದೇಃ (ಪಾ. ಸೂ ೭-೨-೧೧೭) |
| 250 | `, Pā. Sū. 6-4-144 as read [?]]` → `]` | SECOND-PASS S3: [q36] Kannada p.250 prints ನಸ್ತದ್ಧಿತೇ with no number; number removed |
| 250 | `Pā. Sū. 6-4-167 as read [?]` → `Pā. Sū. 6-4-197` | SECOND-PASS Q1: [q37] Kannada p.250 prints ಅನ್ (ಪಾ. ಸೂ. ೬-೪-೧೯೭) for prakṛtibhāva |
| 250 | `Pā. Sū. 6-1-?? as read [?]` → `Pā. Sū. 6-1-161` | SECOND-PASS Q1: [q38] Kannada p.250 prints ಅನುದಾತ್ತಸ್ಯಚಯತ್ರೋ- (ಪಾ. ಸೂ. ೬-೧-೧೬೧) |
| 250 | `, Pā. Sū. 6-1-8 as read [?];` → `;` | SECOND-PASS S3: [q39] Kannada p.250 prints liṭi dhātor anabhyāsasya without a number; number removed |
| 250 | `Pā. Sū. 7-2-116 as read [?]` → `Pā. Sū. 7-1-116` | SECOND-PASS Q1: [q40] Kannada p.250 prints ಅತಉಪಧಾಯಾಃ (ಪಾ. ಸೂ. ೭-೧-೧೧೬) |
| 254 | `, Pā. Sū. 6-1-163 as read [?]` → `` | SECOND-PASS S3: [q41] Kannada p.254 prints citaḥ with no sūtra number; number removed |
| 254 | `, Pā. Sū. 3-2-76 as read [?]` → `` | SECOND-PASS S3: [q42] Kannada p.254 prints kvip ca with no sūtra number; number removed |
| 254 | `, Pā. Sū. 6-3-109 as read [?]` → `` | SECOND-PASS S3: [q43] Kannada p.254 prints pṛṣodarādīni yathopadiṣṭam with no sūtra number; number removed |
| 254 | `, Pā. Sū. 2-4-73 as read [?]` → `` | SECOND-PASS S3: [q44] Kannada p.254 prints bahulaṃ chandasi with no sūtra number; number removed |
| 256 | `(Ni. 2-?? as read [?])` → `(Ni. 3-9)` | SECOND-PASS Q1: [q45] Kannada p.255 prints ಅಭೀಕ … ಸಂಗ್ರಾಮಪದಗಳಲ್ಲಿಯೂ (ನಿ. ೩-೯); the neighbouring quarters reference (English 3-9, Kannada 3-20) is unmarked: see open.tsv |
| 256 | ` (Ni. 5-?? as read [?])` → `` | SECOND-PASS S3: [q46] Kannada p.256 gives the Yāska quotation (ಪುನಃ ಪುನರ್ವರ್ತತೇ…) with no Nirukta number; number removed |
| 257 | `(Ni. 2-?? as read [?])` → `(Ni. 3-11)` | SECOND-PASS Q1: [q47] Kannada p.257 prints ವಜ್ರನಾಮಗಳಲ್ಲಿಯೂ (ನಿ. ೩-೧೧); the stena reference (English 3-9, Kannada 3-19) is unmarked: see open.tsv |
| 259 | ` [as read; the Sanskrit is in small type, partly doubtful [?]]` → `` | SECOND-PASS Q2: [q48] Kannada p.259 prints ಪಾಠಾತ್ ಕೃಪಣ್ಯುರಿತಿ … ಸ್ತುತ್ಯರ್ಥಃ ಇತಿ ಗಮ್ಯತೇ, agreeing with the English; doubt clause removed |
| 259 | `Pā. Sū. 61-171 as read [?]` → `Pā. Sū. 6-1-171` | SECOND-PASS Q1: [q49] Kannada p.259 prints (ಪಾ. ಸೂ.) ೬-೧-೧೭೧) after ಅನುದಾತ್ತಸ್ಯ… |
| 259 | `, Pā. Sū. 2-4-73 as read [?]` → `` | SECOND-PASS S3: [q50] Kannada p.259 prints ಬಹುಲಂ ಛಂದಸಿ with no sūtra number; number removed |
| 259 | `, Pā. Sū. 7-3-52 as read [?]` → `` | SECOND-PASS S3: [q51] Kannada p.259 prints ಚೋಃಕುಃ with no sūtra number; number removed |
| 260 | `Pā. Sū. 6-4-9 as read [?]` → `Pā. Sū. 3-4-9` | SECOND-PASS Q1: [q52] Kannada p.260 prints ತುಮರ್ಥೇಸೇಸೇನಸೇ- (ಪಾ. ಸೂ. ೩-೪-೯) |
| 260 | `, Pā. Sū. 1-1-39 as read [?]` → `` | SECOND-PASS S3: [q53] Kannada p.260 prints ಕೃನ್ಮೇಜಂತಃ with no sūtra number; number removed |
| 261 | `Ni. 11-?? as read [?]` → `Ni. 11-25` | SECOND-PASS Q1: [q54] Kannada p.261 (Sāyaṇa text) and p.262 print ಪರಿತ ಏನಾಂ ತಕತಿ (ನಿ. 11-25) |
| 262 | `(Ni. 11-?? as read [?])` → `(Ni. 11-25)` | SECOND-PASS Q1: [q55] Kannada p.262 prints ಪರಿತ ಏನಾಂ ತಕತಿ (ನಿ. ೧೧-೨೫) |
| 263 | `Pā. Sū. 2-184 as read [?]` → `Pā. Sū. 3-2-184` | SECOND-PASS Q1: [q56] Kannada p.263 prints ಆರ್ತಿಲೂಧೂಸೂಖನಸಹಚರಇತ್ರಃ (ಪಾ. ಸೂ. ೩-೨-೧೮೪) |
| 263 | `Pā. Sū. 7-1-39 as read [?]` → `Pā. Sū. 3-1-39` | SECOND-PASS Q1: [q57] Kannada p.263 prints ಆಜಾ … ಸುಪಾಂ ಸುಲುಕ್ (ಪಾ. ಸೂ. ೩-೧-೩೯); applied as printed (the usual number of this sūtra is 7-1-39), listed in open.tsv |
| 263 | `, Pā. Sū. 6-4-148 as read [?]` → `` | SECOND-PASS S3: [q58] Kannada p.263 prints ಯಸ್ಯೇತಿಚ with no sūtra number; number removed |
| 263 | `Pā. Sū. 6-1-197 as read [?]` → `Pā. Sū. 7-1-197` | SECOND-PASS Q1: [q59] Kannada p.263 prints ಇತ್ಯಾದಿರ್ನಿತ್ಯಮ್ (ಪಾ. ಸೂ. ೭-೧-೧೯೭); applied as printed (elsewhere 6-1-197), listed in open.tsv |
| 264 | `, Pā. Sū. 1-1-39 as read [?]` → `` | SECOND-PASS S3: [q60] Kannada p.264 prints ಕೃನ್ಮೇಜಂತಃ with no sūtra number; number removed |
| 267 | `Tai. Saṃ. 2-3-11-?-? [?])` → `Tai. Saṃ. 2-3-11)` | SECOND-PASS Q1: [q61] Kannada p.267 prints (ಐ. ಬ್ರಾ. ೧-೧೮; ತೈ. ಸಂ. ೨-೩-೧೧) |
| 268 | `, Pā. Sū. 6-4-148 as read [?]` → `` | SECOND-PASS S3: [q62] Kannada p.268 prints ಯಸ್ಯೇತಿಚ with no sūtra number; number removed |
| 268 | `, Pā. Sū. 7-3-112 as read [?]` → `` | SECOND-PASS S3: [q63] Kannada p.268 prints ಆಣ್‌ನದ್ಯಾಃ with no sūtra number; number removed |
| 269 | `Pā. Sū. 2-106 as read [?]` → `Pā. Sū. 3-2-106` | SECOND-PASS Q1: [q64] Kannada p.269 prints ಲಿಟಃ ಕಾನಜ್ವಾ (ಪಾ. ಸೂ. ೩-೨-೧೦೬) |
| 269 | `*citaḥ*, Pā. Sū. 6-1-163 as read [?]` → `*citaḥ*, Pā. Sū. 6-1-193` | SECOND-PASS Q1: [q65] Kannada p.269 prints ಚಿತಃ … (ಪಾ. ಸೂ. ೬-೧-೧೯೩); applied as printed (elsewhere citaḥ is 6-1-163), listed in open.tsv |
| 269 | `Paribhāṣā 40 as read [?]` → `Paribhāṣā 40` | SECOND-PASS Q1: [q66] Kannada p.269 prints (ಪರಿ. ಭಾ. ೪೦) |
| 269 | `Vārt. as read [?]` → `Vārt. 2233` | SECOND-PASS Q1: [q67] Kannada p.269 prints ಸಂಪದಾದಿಭ್ಯಃ ಕ್ವಿಪ್ (ವಾ. ೨೨೩೩) |
| 269 | `Pā. Sū. 7-1-39 as read [?]` → `Pā. Sū. 3-1-39` | SECOND-PASS Q1: [q68] Kannada p.269 prints ದಸ್ರಾ-ಸುಪಾಂ ಸುಲುಕ್ (ಪಾ. ಸೂ. ೩-೧-೩೯); applied as printed, listed in open.tsv |
| 269 | `Pā. Sū. 6-2-172 as read [?]` → `Pā. Sū. 6-2-127` | SECOND-PASS Q1: [q69] Kannada p.269 prints ನಞ್ ಸುಭ್ಯಾಮ್ (ಪಾ. ಸೂ. ೬-೨-೧೨೭) |
| 271 | `'*kriyate teditī kārṣmaṃ śubhāśubhalakṣaṇaṃ karma tadyathā karṣāmā…*' [reading doubtful [?` → `'*kriyate taditi kārṣma śubhāśubhalakṣaṇaṃ karma tadyathā karkāramātiṣṭhati evamāsthitavat` | SECOND-PASS Q1: [q70] Kannada p.271 prints the Skandasvāmin quotation in full (ಕ್ರಿಯತೇ ತದಿತಿ ಕಾರ್ಷ್ಮ … ಕರ್ಕಾರಮಾತಿಷ್ಠತಿ ಏವಮಾಸ್ಥಿತವತೀ); IAST made by sp_sanskrit.py |
| 272 | `(Ni. 1-?? as read [?])` → `(Ni. 2-27)` | SECOND-PASS Q1: [q71] Kannada p.272 prints ಇಪ್ಪತ್ತಾರು ಅಶ್ವವಾಚಕ ಶಬ್ದಗಳಲ್ಲಿ (ನಿ. ೨-೨೭) |
| 273 | `Pā. Sū. 8-21-20 as read [?]` → `Pā. Sū. 8-1-20` | SECOND-PASS Q1: [q72] Kannada p.273 prints ಯುಷ್ಮದಸ್ಮದೋಃ ಷಷ್ಠೀ- (ಪಾ. ಸೂ. ೮-೧-೨೦) |
| 273 | `Pā. Sū. 3-1-?? as read [?]` → `Pā. Sū. 3-1-85` | SECOND-PASS Q1: [q73] Kannada p.273 prints ವ್ಯತ್ಯಯೋ ಬಹುಲಮ್ (ಪಾ. ಸೂ. ೩-೧-೮೫) |
| 277 | `(Ṛ. Saṃ. numerals not readable [?]) is said, in several Ṛks such as these, to have been` → `(Ṛ. Saṃ. 6-16-4, 5, 19) is said, in Ṛ. Saṃ. 7-19-8 and other places, to have been` | SECOND-PASS Q1: [q74] Kannada p.277 prints ದಿವೋದಾಸನೂ ಸಹ ಭರತನೆಂದೂ (ಋ. ಸಂ. ೬-೧೬-೪, ೫, ೧೯) … ಋ. ಸಂ. ೭-೧೯-೮ ಮೊದಲಾದ ಸ್ಥಳಗಳಲ್ಲಿ |
| 277 | `(Ṛ. Saṃ. 1-130-7-? ; 2-12-11-? ; 4-?-? ; 6-26-5-? [numerals not readable [?]])` → `(Ṛ. Saṃ. 1-130-2 ; 2-12-11 ; 6-26-5 ; 7-18-20)` | SECOND-PASS Q1: [q75] Kannada p.277 prints (ಋ. ಸಂ. ೧-೧೩೦-೨ ; ೨-೧೨-೧೧; ೬-೨೬-೫ ; ೭-೧೮-೨೦.) |
| 277 | `Ṛ. Saṃ. 1-112-14 [as read], 1-116-18, 1-130-?, 3-19-6 [as read], 4-26-3 [as read] and othe` → `Ṛ. Saṃ. 1-112-14 ; 1-116-18 ; 1-119-4 ; 1-130-7 to 10 ; 2-19-6 ; 4-26-3 ; 4-30-20 ; 6-26-3` | SECOND-PASS Q1: [q76] Kannada p.277 prints the whole list ಋ. ಸಂ. ೧-೧೧೨-೧೪ ; … ೯-೬೧-೨ ಎಂಬ ಋಕ್ಕುಗಳಲ್ಲಿ |
| 277 | `in the Ṛks 6-26-5-? [?] and others.` → `in the Ṛk 8-13-2.` | SECOND-PASS Q1: [q77] Kannada p.277 prints ಅಗ್ನಿಯನ್ನು ಇವನ ಹೆಸರಿನಿಂದ ಋ. ಸಂ. ೮-೧೩-೨ ಎಂಬ ಋಕ್ಕಿನಲ್ಲಿ ಕರೆದಿರುವುದು |
| 277 | `In Ṛ. Saṃ. 6-26-5-? ; 1-130-7-? ; 6-26-5-? [?] and other places` → `In Ṛ. Saṃ. 1-112-13, 14 ; 1-116-18 ; 6-16-5 ; 6-31-4 and other places` | SECOND-PASS Q1: [q78] Kannada p.277 prints ಋ. ಸಂ. ೧-೧೧೨-೧೩. ೧೪ ; ೧-೧೧೬-೧೮ ; ೬-೧೬-೫ ; ೬-೩೧-೪ ; ಮೊದಲಾದ ಸ್ಥಳಗಳಲ್ಲಿ |
| 277 | `Kā. 6-3-21-2 as read [?]` → `Kā. 6-3-21-5` | SECOND-PASS Q1: [q79] Kannada p.277 prints ದಿವಶ್ಚ ದಾಸೇ ಷಷ್ಠ್ಯಾ ಅಲುಕ್ ವಕ್ತವ್ಯಃ (ಕಾ. ೬-೩-೨೧-೫) |
| 278 | `, Pā. Sū. 2-4-73 as read [?]` → `` | SECOND-PASS S3: [q80] Kannada p.278 prints ಬಹುಲಂ ಛಂದಸಿ with no sūtra number; number removed |
| 278 | `, Pā. Sū. 7-3-84 as read [?]` → `` | SECOND-PASS S3: [q81] Kannada p.278 prints ಸಾರ್ವಧಾತುಕಾರ್ಥಧಾತುಕಯೋಃ with no sūtra number; number removed |
| 278 | `, Pā. Sū. 7-1-39 as read [?], *ā* for the ending; *ugidacāṃ` → `, *ā* for the ending; *ugidacāṃ` | SECOND-PASS S3: [q82] Kannada p.278 prints ಸುಪಾಂ ಸುಲುಕ್ ಸೂತ್ರದಿಂದ (hayantā) with no sūtra number; number removed |
| 278 | `, Pā. Sū. 7-1-70 as read [?]` → `` | SECOND-PASS S3: [q83] Kannada p.278 prints ಉಗಿದಚಾಂ ಸರ್ವನಾಮಸ್ಥಾನೇ with no sūtra number; number removed |
| 278 | `Kā. 6-1-223-1 as read [?]` → `Kā. 6-1-176-1` | SECOND-PASS Q1: [q84] Kannada p.278 prints ರಯಿ ಶಬ್ದಾಚ್ಚ (ಕಾ. ೬-೧-೧೭೬-೧) |
| 278 | `Pā. Sū. 7-1-39 as read [?], *ā*).` → `Pā. Sū. 3-1-85, *ā*).` | SECOND-PASS Q1: [q85] Kannada p.278 prints ಯುಕ್ತಾ … ಸುಪಾಂ ಸುಲುಕ್ (ಪಾ. ಸೂ ೩-೧-೮೫); applied as printed, listed in open.tsv |
| 281 | `'*ahaḥ kasmāt | adaḥ sa*[?]…'` → `'*ahaḥ kasmādupāharaṃtyasmin karmāṇi*'` | SECOND-PASS Q1: [q86] Kannada p.281 prints the Nirukta words ಅಹಃ ಕಸ್ಮಾದುಪಾಹರಂತ್ಯಸ್ಮಿನ್ ಕರ್ಮಾಣಿ; IAST made by sp_sanskrit.py |
| 282 | `, Pā. Sū. 6-2-120 as read [?]` → `` | SECOND-PASS S3: [q87] Kannada p.282 prints ವೀರವೀರ್ಯೌ ಚ (ಪಾ. ಸೂ.) with the number missing; number removed |
| 282 | `, Pā. Sū. 7-1-39 as read [?], *ā* for the ending; *ugidacām*, Pā. Sū. 7-1-70 as read [?],` → `, *ā* for the ending; *ugidacām*,` | SECOND-PASS S3: [q88-q89] Kannada p.282 prints ಸುಪಾಂ ಸುಲುಕ್—ಸೂತ್ರ and ಉಗಿದಚಾಂ—ಸೂತ್ರ (vahantā) with no sūtra numbers; numbers removed |
| 282 | `, Pā. Sū. 7-1-39 as read [?], *ā* for the ending; *bahuvrīhau` → `, *ā* for the ending; *bahuvrīhau` | SECOND-PASS S3: [q90] Kannada p.282 prints ಸಮನಸಾ - ಸುಪಾಂ ಸುಲುಕ್ - ಸೂತ್ರದಿಂದ with no sūtra number; number removed |
| 286 | `Phiṭ-sūtra 1 as read [?]` → `Phiṭ-sūtra 1` | SECOND-PASS Q1: [q91] Kannada p.286 prints ಫಿಷೋಂತ ಉದಾತ್ತಃ (ಫಿ. ಸೂ. ೧) |
| 286 | `, Pā. Sū. 7-3-103 as read [?]` → `` | SECOND-PASS S3: [q92] Kannada p.286 prints ಬಹುವಚನೇಝಲ್ಯೇತ್ with no sūtra number; number removed |
| 286 | `Pā. Sū. 6-1-15 as read [?]` → `Pā. Sū. 9-1-15` | SECOND-PASS Q1: [q93] Kannada p.286 prints ವಚಿಸ್ವಪಿಯಜಾದೀನಾಂಕಿತಿ (ಪಾ ಸೂ. ೯-೧-೧೫); applied as printed (adhyāya 9 does not exist), listed in open.tsv |
| 286 | `Pā. Sū. 6-2-139 as read [?]` → `Pā. Sū. 9-2-13` | SECOND-PASS Q1: [q94] Kannada p.286 prints ಗತಿಕಾರಕೋಪದಾತ್ ಕೃತ್ (ಪಾ. ಸೂ. ೯-೨-೧೩); applied as printed (impossible number), listed in open.tsv |
| 286 | `Pā. Sū. 3-2-170 as read [?]` → `Pā. Sū. 3-1-170` | SECOND-PASS Q1: [q95] Kannada p.286 prints ಕ್ಯಾಚ್ಛಂದಸಿ (ಪಾ. ಸೂ ೩-೧-೧೭೦) |
| 286 | `Pā. Sū. 6-4-48 as read [?]` → `Pā. Sū. 9-4-48` | SECOND-PASS Q1: [q96] Kannada p.286 prints ಅತೋಲೋಪಃ (ಪಾ. ಸೂ. ೯-೪-೪೮); applied as printed (impossible number), listed in open.tsv |
| 288 | `(Ni. 2-?? as read [?])` → `(Ni. 3-9)` | SECOND-PASS Q1: [q97] Kannada p.288 prints ರಣಾಯ … ರಣ ಶಬ್ದವು (ನಿ ೩-೯) |
| 288 | `, Pā. Sū. 6-2-199 as read [?]` → `` | SECOND-PASS S3: [q98] Kannada p.288 prints ಪರಾದಿಶ್ಚಂದಸಿ ಬಹುಲಮ್ with no sūtra number; number removed |
| 290 | `1-116-21 ; 8-24-14-? ; 8-24-14-? ; 8-24-14-? ; 8-24-14-? ; 8-24-14-? ; 10-40-? [as read; n` → `1-116-21 ; 8-8-20 ; 8-24-14 ; 8-46-21 ; 8-46-23 ; 8-50-9 ; 10-40-7.` | SECOND-PASS Q1: [q99] Kannada p.290 prints ಋ. ಸಂ. ೧-೧೧೨-೧೦; ೧-೧೧೬-೨೧ ; ೮-೮-೨೦ ; ೮-೨೪-೧೪; ೮-೪೬-೨೧ ; ೮-೪೬-೨೩ ; ೮-೫೦-೯ ; ೧೦-೪೦-೭ |
| 290 | `(Ni. 4-?? as read [?])` → `(Ni. 3-5)` | SECOND-PASS Q1: [q100] Kannada p.290 prints ಸನಯೇ … ಪ್ರಯುಕ್ತವಾಗಿ ಇರುವುದು. (ನಿ. ೩-೫) |
| 290 | `(Ni. 1-?? as read [?])` → `(Ni. 2-21)` | SECOND-PASS Q1: [q101] Kannada p.290 prints ವಸ್ತೋಃ … ಹನ್ನೆರಡು ಅಹರ್ನಾಮಗಳಲ್ಲಿ (ನಿ. ೨-೨೧) |
| 294 | `(Ni. 3-?? as read [?])` → `(Ni. 3-19)` | SECOND-PASS Q1: [q102] Kannada p.294 prints ಅವತಾತ್ … ಹದಿನಾಲ್ಕು ಕೂಪನಾಮಗಳಲ್ಲಿ (ನಿ. ೩-೧೯) |
| 294 | `(Ni. 1-?? as read [?])` → `(Ni. 2-24)` | SECOND-PASS Q1: [q103] Kannada p.294 prints ವಾಃ … ನೂರೊಂದು ಉದಕನಾಮಗಳಲ್ಲಿ (ನಿ ೨-೨೪) |
| 295 | `1-112-?; 1-116-? ; 1-117-?; 1-118-? ; 1-112-16-? ; 6-?-? ; 10-40-8-? ; 10-40-? [as read; t` → `1-112-16 ; 1-116-22 ; 1-117-20 ; 1-118-8 ; 1-119-6 ; 6-62-7 ; 7-62-8 ; 10-39-13 ; 10-40-8.` | SECOND-PASS Q1: [q104] Kannada p.295 prints ಋ. ಸಂ. ೧-೧೧೨-೧೬ : ೧-೧೧೬-೨೨ : … ೧೦-೪೦-೮ ಎಂಬ ಋಕ್ಕುಗಳಲ್ಲಿ |
| 298 | `(Ni. 1-?? as read [?])` → `(Ni. 7-31)` | SECOND-PASS Q1: [q105] Kannada p.298 prints ಪ್ರಯೋಗಃ (ನಿ. ೭-೩೧) |
| 298 | `*Viśvako nāma rājarṣeḥ putraḥ pramādād upananaṣṭe snehād vipatty-āśaṅkayā kasya pālanaṃ pu` → `*viśvako nāma rājarṣeḥ putraḥ pramādādupananāśa snehādvipattā śaṃkayā tasya pālanaṃ punaśc` | SECOND-PASS Q1: [q106] Kannada p.298 prints the whole passage ವಿಶ್ವಕೋ ನಾಮ ರಾಜರ್ಷೇಃ ಪುತ್ರಃ … ಅವಸ್ಯವ ಇತ್ಯಾದಿನಾ; IAST made by sp_sanskrit.py |
| 298 | `through carelessness [?], afraid` → `through carelessness, afraid` | SECOND-PASS Q2: [q107] Kannada p.298 prints ಪ್ರಮಾದದಿಂದ, agreeing with the English |
| 299 | `, Pā. Sū. 6-1-97 as read [?]` → `` | SECOND-PASS S3: [q108] Kannada p.299 prints ಅತೋ ಗುಣೇ with no sūtra number; number removed |
| 299 | `Pā. Sū. 6-1-173 as read [?]` → `Pā. Sū. 6-1-179` | SECOND-PASS Q1: [q109] Kannada p.299 prints ಶತುರನುಮೋ ನದ್ಯಜಾದೀ (ಪಾ. ಸೂ. ೬-೧-೧೭೯) |
| 299 | `, Pā. Sū. 6-4-77 as read [?]` → `` | SECOND-PASS S3: [q110] Kannada p.299 prints ಅಚಿಶ್ನುಧಾತುಭ್ರುವಾಮ್ with no sūtra number; number removed |
| 299 | `, Pā. Sū. 6-4-148 as read [?]` → `` | SECOND-PASS S3: [q111] Kannada p.299 prints ಯಸ್ಯೇತಿಚ with no sūtra number; number removed |
| 303 | `the Kātyāyana-ites [?],` → `the followers of the Kaṭha branch,` | SECOND-PASS Q1: [q112] Kannada p.303 prints ಕಠಶಾಖೆಯವರು ಎಂದರೆ ಯರ್ಜುರ್ವೇದದ ಕಠಶಾಖೆಯನ್ನು ಅಧ್ಯಯನಮಾಡುವವರು (and ಕಠಾನಾಮಗ್ನಿಹೋತ್ರ in the Sanskrit); the Kaṭha branch, not Kātyāyana |
| 303 | `1-112-5 ; 1-117-4 ; 1-117-4 ; 1-117-5 ; 1-118-6 ; 10-39-9 [as read; the numerals partly le` → `1-112-5 ; 1-116-24 ; 1-117-4 ; 1-118-6 ; 1-119-6 ; 10-39-9.` | SECOND-PASS Q1: [q113] Kannada p.303 prints ಋ. ಸಂ. ೧-೧೧೨-೫ ; ೧-೧೧೬-೨೪ ; ೧-೧೧೭-೪ ; ೧-೧೧೮-೬ ; ೧-೧೧೯-೬ : ೧೦-೩೯-೯ |
| 303 | `Pā. Sū. 2-29 as read [?]` → `Pā. Sū. 6-2-2` | SECOND-PASS Q1: [q114] Kannada p.303 prints ತತ್ಪುರುಷೇತುಲ್ಯಾರ್ಥ— (ಪಾ. ಸೂ. ೬-೨-೨) |
| 303 | `Phiṭ-sūtra as read [?]` → `Phiṭ-sūtra 28` | SECOND-PASS Q1: [q115] Kannada p.303 prints ನ್ರಸಂಖ್ಯಾಯಾಃ (ಫಿ. ಸೂ. ೨೮) |
| 303 | `Pā. Sū. 8-4-53 as read [?]` → `Pā. Sū. 8-4-53` | SECOND-PASS Q2: [q116] Kannada p.304 continues ಆ-4-53) (the first numeral is a damaged glyph of 8); agrees with the English |
| 304 | `, Pā. Sū. 7-2-35 as read [?]` → `` | SECOND-PASS S3: [q117] Kannada p.304 prints ಅರ್ಧಧಾತುಕಸ್ಯೇಡ್ವಲಾದೇಃ with no sūtra number; number removed |
| 306 | `(Ni. 2-1 as read [?])` → `(Ni. 3-2)` | SECOND-PASS Q1: [q118] Kannada p.306 prints (ನಿ. ೩-೨) ದಂಸಪದವು ಉಕ್ತವಾಗಿರುವುದರಿಂದ ದಂಸ ಎಂದರೆ ಕರ್ಮ |
| 307 | `Pā. Sū. 6-4-20 as read [?]` → `Pā. Sū. 7-4-20` | SECOND-PASS Q1: [q119] Kannada p.307 prints ವಚ ಉಮ್ (ಪಾ. ಸೂ. ೭-೪-೨೦) |
| 307 | `Pā. Sū. 3-1-85 as read [?]` → `Pā. Sū. 3-1-86` | SECOND-PASS Q1: [q120] Kannada p.307 prints ವ್ಯತ್ಯಯೋ ಬಹುಲಮ್ (ಪಾ. ಸೂ. ೩ ೧-೮೬) (hyphen missing after 3); applied as printed (elsewhere 3-1-85), listed in open.tsv |
| 307 | `, Pā. Sū. 6-4-77 as read [?]` → `` | SECOND-PASS S3: [q121] Kannada p.308 prints ಅಚಿಶ್ನುಧಾತುಭ್ರುವಾಂ- (aśnuvan) with no sūtra number; number removed |
| 307 | `, Pā. Sū. 6-4-8 as read [?]` → `` | SECOND-PASS S3: [q122] Kannada p.308 prints ಸರ್ವನಾಮಸ್ಥಾನೇಚಾಸಂಬುದ್ಧಿ with no sūtra number; number removed |
| 307 | `, Pā. Sū. 2-4-73 as read [?]` → `` | SECOND-PASS S3: [q123] Kannada p.308 prints ಬಹುಲಂ ಛಂದಸಿ with no sūtra number; number removed |
| 307 | `, Pā. Sū. 6-1-10 as read [?]` → `` | SECOND-PASS S3: [q124] Kannada p.308 prints ಶ್ಲಾ ಎಂಬುದರಿಂದ with no sūtra number; number removed |
| 307 | `, Pā. Sū. 7-4-62 as read [?]` → `` | SECOND-PASS S3: [q125] Kannada p.308 prints ಕುಹೋಶ್ಚುಃ with no sūtra number; number removed |
| 309 | `वर्ग—*(small numerals; read "13, 14, 15, 16, 17" — as printed [?])* ॥` → `वर्ग—१३, १४, १५, १६, १७ ॥` | SECOND-PASS Q1: [q126] Kannada p.309 prints ವರ್ಗ-13, 14, 15, 16, 17; Devanagari numerals made from the Kannada's figures by script |
| 311 | `(Ni. 2-?? as read [?])` → `(Ni. 3-9)` | SECOND-PASS Q1: [q127] Kannada p.311 prints ಇಪ್ಪತ್ತೆಂಟು ಅನ್ನನಾಮಗಳಲ್ಲಿ (ನಿ. ೩-೯) |
| 312 | `(Ni. 11-?? as read [?])` → `` | SECOND-PASS S3: [q128] Kannada p.312 gives ಋಭುರ್ವಿಭ್ವಾ ವಾಜ ಇತಿ ಸುಧನ್ವನ … with no Nirukta number; number removed |
| 312 | `Pā. Sū. 7-1-39 as read [?]` → `Pā. Sū. 3-1-39` | SECOND-PASS Q1: [q129] Kannada p.312 prints ಸುಪಾಂ ಸುಲುಕ್- (ಸಾ, ಸೂ. ೩-೧-೩೯) (ಸಾ for ಪಾ); applied as printed, listed in open.tsv |
| 312 | `Pā. Sū. 5-4-?? as read [?]` → `Pā. Sū. 5-4-2-51` | SECOND-PASS Q1: [q130] Kannada p.312 prints ಪ್ರತ್ನೇ—ನಶ್ಚ ಪುರಾಣೇ ಪ್ರಾತ್ (ಪಾ. ಸೂ. ೫-೪-೨-೫೧); applied as printed (four-part number), listed in open.tsv |
| 313 | `Pā. Sū. 2-102 as read [?]` → `Pā. Sū. 3-2-102` | SECOND-PASS Q1: [q131] Kannada p.313 prints ನಿಷ್ಠಾ (ಪಾ. ಸೂ. ೩-೨-೧೦೨) |
| 313 | `Pā. Sū. 6-2-49 as read [?]` → `Pā. Sū. 6-1-49` | SECOND-PASS Q1: [q132] Kannada p.313 prints ಗತಿರನಂತರಃ (ಪಾ. ಸೂ. ೬-೧-೪೯) |
| 315 | `[*bhūyaṃ tarikṣa* — as printed, doubtful [?]]` → `[*bhūmyaṃtarikṣa*]` | SECOND-PASS Q1: [q133] Kannada p.315 prints (ಭೂಮ್ಯಂತರಿಕ್ಷ) ದ್ಯಾವಾಪೃಥಿವಿಗಳನ್ನಾಗಿ; IAST made by sp_sanskrit.py |
| 317 | `*vāsātyau kṛṣṇau jagato nidhānau dyāvābhūmī cirathas saṃsakhāyau* [as read; doubtful [?]]` → `*vāsātyau kṛṣṇau jagato nidhānau | dyāvābhūmī carathassansakhāyau*` | SECOND-PASS Q1: [q134] Kannada p.317 prints ವಾಸಾತ್ಯೌ ಕೃಷ್ಣೌ ಜಗತೋ ನಿಧಾನೌ । ದ್ಯಾವಾಭೂಮೀ ಚರಥಸ್ಸನ್ಸಖಾಯೌ; IAST made by sp_sanskrit.py |
| 318 | `Ni. 6-30 as read [?]:)*` → `Ni. 3-20:)*` | SECOND-PASS Q1: [q135] Kannada p.318 prints ಎಂದು ನಿರುಕ್ತದಲ್ಲಿ (ನಿ. ೩-೨೦) ಯಾಸ್ಕರು ಉದಾಹರಣೆಯನ್ನು ಕೊಟ್ಟಿರುವರು. ವರ್ತಿಃ |
| 318 | `(Ni. 2-?? as read [?])` → `(Ni. 3-8)` | SECOND-PASS Q1: [q136] Kannada p.318 prints ಇಪ್ಪತ್ತೈದು ಮನಷ್ಯನಾಮಗಳಲ್ಲಿ (ನಿ. ೩-೮) |
| 318 | `Pā. Sū. 5-3-65 as read [?]` → `Pā. Sū. 5-3-65` | SECOND-PASS Q2: [q137] Kannada p.318 prints ವಿನ್ಮತ್ತೋರ್ಲುಕ್ (ಪಾ. ಸೂ ೫:-೩-೬೫) (stray colon), agreeing with the English |
| 318 | `Pā. Sū. 6-4-155 as read [?]` → `Pā. Sū. 6-4-143` | SECOND-PASS Q1: [q138] Kannada p.318 prints ಟೇಃ (ಪಾ. ಸೂ. ೬-೪-೧೪೩) |
| 318 | `, Pā. Sū. 6-1-10 as read [?]` → `` | SECOND-PASS S3: [q139] Kannada p.318 prints ಶ್ಲೌ ಎಂಬುದರಿಂದ with no sūtra number; number removed |
| 318 | `, Pā. Sū. 7-4-78 as read [?]` → `` | SECOND-PASS S3: [q140] Kannada p.318 prints ಬಹುಲಂ ಛಂದಸಿ with no sūtra number; number removed |
| 319 | `Pā. Sū. 1-186 as read [?]` → `Pā. Sū. 6-1-186` | SECOND-PASS Q1: [q141] Kannada p.319 prints ತಾಸ್ಯನುದಾತ್ತೇತ್—(ಪಾ. ಸೂ. ೬-೧-೧೮೬) |
| 323 | `, Pā. Sū. 6-4-148 as read [?]` → `` | SECOND-PASS S3: [q142] Kannada p.323 prints ಯಸ್ಯೇತಿ ಚ with no sūtra number; number removed |
| 323 | `, Pā. Sū. 1-1-47 as read [?]` → `` | SECOND-PASS S3: [q143] Kannada p.323 prints ಮಿದಚೋಂತ್ಯಾತ್ಪರಃ with no sūtra number; number removed |
| 323 | `, Pā. Sū. 1-2-4 as read [?]` → `` | SECOND-PASS S3: [q144] Kannada p.323 prints ಸಾರ್ವಧಾತುಕಮಪಿತ್ with no sūtra number; number removed |
| 326 | `, Pā. Sū. 8-2-31 as read [?]` → `` | SECOND-PASS S3: [q145] Kannada p.326 prints ಹೋಢಃ with no sūtra number; number removed |
| 326 | `, Pā. Sū. 8-2-40 as read [?]` → `` | SECOND-PASS S3: [q146] Kannada p.326 prints ಝುಷಸ್ತಥೋರ್ಧಃ with no sūtra number; number removed |
| 326 | `, Pā. Sū. 8-3-13 as read [?]` → `` | SECOND-PASS S3: [q147] Kannada p.326 prints ಡೋಢೇಲೋಪಃ with no sūtra number; number removed |
| 326 | `, Pā. Sū. 6-3-111 as read [?]` → `` | SECOND-PASS S3: [q148] Kannada p.326 prints ಧೃಲೋಪೇ ಪೂರ್ವಸ್ಯ ದೀರ್ಘೋಽಣಃ with no sūtra number; number removed |
| 327 | `Pā. Sū. 8-3-57 as read [?]` → `Pā. Sū. 3-3-57` | SECOND-PASS Q1: [q149] Kannada p.327 prints ನರಾ … ಯುದೋರಪ್ (ಪಾ. ಸೂ. ೩-೩-೫೭) |
| 327 | `Pā. Sū. 7-1-39 as read [?]` → `Pā. Sū. 3-1-39` | SECOND-PASS Q1: [q150] Kannada p.327 prints ಸುಪಾಂ ಸುಲುಕ್- (ಪಾ. ಸೂ ೩-೧-೩೯); applied as printed, listed in open.tsv |
| 327 | `, Pā. Sū. 8-4-2 as read [?]` → `` | SECOND-PASS S3: [q151] Kannada p.328 prints ಅಟ್‌ಕುಪ್ವಾಜ್—ಸೂತ್ರದಿಂದ with no sūtra number; number removed |
| 331 | `Vārt. as read [?]` → `Pā. Sū. 6-2-103-2` | SECOND-PASS Q1: [q152] Kannada p.331 prints ಮರುದ್ವೃಧಾದೀನಾಂ ಛಂದಸ್ಯುಪಸಂಖ್ಯಾನಮ್ (ಪಾ. ಸೂ ೬-೨-೧೦೩-೨) (the Kannada gives it as Pā. Sū.) |
| 331 | `, Pā. Sū. 6-1-97 as read [?]` → `` | SECOND-PASS S3: [q153] Kannada p.331 prints ಅತೋ ಗುಣೇ with no sūtra number; number removed |
| 331 | `Pā. Sū. 7-2-15 as read [?]` → `Pā. Sū. 7-1-15` | SECOND-PASS Q1: [q154] Kannada p.331 prints ಯಸ್ಯ ವಿಭಾಷಾ (ಪಾ: ಸೂ. ೭-೧-೧೫); applied as printed (elsewhere 7-2-15), listed in open.tsv |
| 332 | `(printed "*ṭuvap bījasantāne*" [?];` → `(printed "*ṭuvap bījasantāne*";` | SECOND-PASS Q2: [q155] Kannada p.332 prints ಊಪಥುಃ-ಟುವಪ್ ಬೀಜಸಂತಾನೇ, agreeing with the English |
| 333 | `For the man who is waiting (*upekṣamāṇāya*, as printed; for the sacrifice [?])` → `For the expectant man (*apekṣamāṇāya*)` | SECOND-PASS Q1: [q156] Kannada p.333 (Sāyaṇa text) prints ಯಜ್ಜನಾಯಾಪೇಕ್ಷಮಾಣಾಯ ಪುರುಷಾಯ, and ಅಪೇಕ್ಷಿಸಿದ ಜನಗಳಿಗಾಗಿ; sp_sanskrit.py gives apekṣamāṇāya; the later unmarked remark on  |
| 333 | `*tat* — that deed [?];` → `*tat* — that deed;` | SECOND-PASS Q2: [q157] Kannada p.333 prints ತತ್-ಅಕರ್ಮವು (misprint for ಆ ಕರ್ಮವು); the Sāyaṇa text of the same page has ತತ್ಕರ್ಮ, confirming 'that deed' |
| 334 | `"*Sautrā[?]ṇi*" for the sacrifice named in the opening of this paragraph: reading doubtful` → `"*Sautrāmaṇi*" for the sacrifice named in the opening of this paragraph.)` | SECOND-PASS Q1: [q158-q159] Kannada p.334 prints ಸೌತ್ರಾಮಣಿ ಎಂಬ ಯಜ್ಞವನ್ನು ಮಾಡುವಾಗ; IAST by sp_sanskrit.py |
| 334 | `(the *kakṣya*) [?]` → `(the *kakṣya*)` | SECOND-PASS Q2: [q160] Kannada p.334 prints ಮನುಷ್ಯ (ಕಕ್ಷೆ)ರ ಗುಂಪಿನಲ್ಲಿ; the Nirukta passage on the same page has both ಕಕ್ಷ್ಯಾ and ಕಕ್ಷ; English form kept |
| 334 | ` *(Reading of the Kannada tail uncertain [?].)*` → `` | SECOND-PASS Q2: [q161] Kannada p.334 tail (ಇದರಿಂದ ಕಕ್ಷೀವಂತನೆಂಬವನು ಉಶಿಕ್ ಎಂಬ ಸ್ತ್ರೀಯ ಪುತ್ರನೆಂದೂ … ತೃಪ್ತಿಪಡಿಸಿರುವನೆಂದೂ) is clear and agrees with the English; doubt note removed |
| 335 | `Pā. Sū. 3-1-94 as the numeral list reads it on this page (it reads 3-1-92 on p. 344; I rea` → `Pā. Sū. 3-1-99` | SECOND-PASS Q1: [q162] Kannada p.335 prints ಅಚೋಯತ್ (ಪಾ. ಸೂ. ೩-೧-೯೯) |
| 335 | `Pā. Sū. 7-1-55 as read [?]` → `Pā. Sū. 7-1-59` | SECOND-PASS Q1: [q163] Kannada p.335 prints ಶೇಮುಚಾದೀನಾಮ್ (ಪಾ. ಸೂ. ೭-೧-೫೯) |
| 338 | `*udāttasvaritayor yaṇaḥ* (as printed [?])` → `*udāttasvaritayor yaṇaḥ* (Pā. Sū. 8-2-4)` | SECOND-PASS Q1: [q164] Kannada p.338 prints ಉದಾತ್ತಸ್ವರಿತಯೋರ್ಯಣಃ—(ಪಾ. ಸೂ. ೮-೨-೪) |
| 340 | `a shining(-skinned) woman [?];` → `a shining(-skinned) woman;` | SECOND-PASS Q2: [q165] Kannada p.340 prints ರುಶತೀಂ ದೀಪ್ತತ್ವಚಂ ಸ್ತ್ರಿಯಂ, agreeing with the English |
| 340 | `being there … (the Aśvins, coming, tell him that while … playing a *vīṇā* they will come; ` → `staying right there [he was told]: 'if you are a brahmin, find out the dawn when it has br` | SECOND-PASS Q1: [q166] Kannada p.340 prints the whole passage (ಅತ್ರೈವ ಸ್ಥಿತಃ ಸನ್ ವ್ಯುಷ್ಟಾಮುಷಸಂ ವಿಜಾನೀಹಿ ಯದಿ ತ್ವಂ ಬ್ರಾಹ್ಮಣೋಽಸೀತಿ । ತಮಶ್ವಿನಾವಾಗತ್ಯೋಚತುಃ । ವ್ಯುಷ್ಟಾಯಾಂ ಹರ್ಮ್ಯಸ್ಯೋಪರ |
| 340 | `Yāska is quoted (Ni. 5-?)` → `Yāska is quoted (Ni. 6-6)` | SECOND-PASS Q1: [q166] Kannada p.340 prints ತದುಕ್ತಂ ಯಾಸ್ಕೇನ । ಕ್ಷೋಣಸ್ಯ ಕ್ಷಯಣಸ್ಯ । ನಿ-೬-೬; unmarked '5-?' in the same remark as q166 |
| 341 | `of the one who was unable to walk [as read [?]];` → `of the one who was unable to walk;` | SECOND-PASS Q2: [q167] Kannada p.341 prints ಕ್ಷೋಣಸ್ಯ—(ಕುರುಡನಾದುದರಿಂದ) ಚಲಿಸಲು ಅಶಕ್ತನಾದ, agreeing with the English |
| 341 | `dīptatvaciṃ [?] striyaṃ` → `dīptatvacaṃ striyaṃ` | SECOND-PASS Q1: [q168] Kannada p.341 prints ದೀಪ್ತತ್ವಚಂ ಶ್ರಿಯಂ and p.340 ದೀಪ್ತತ್ವಚಂ ಸ್ತ್ರಿಯಂ |
| 344 | `*guṇa* for the root's *i*-vowel [?];` → `*guṇa* for the root's *ik* vowel;` | SECOND-PASS Q1: [q169] Kannada p.344 prints ತನ್ನಿಮಿತ್ತವಾಗಿ ಧಾತುವಿನ ಇಕ್ಕಿಗೆ ಗುಣ (ik = the pratyāhāra, not the letter i) |
| 344 | `Pā. Sū. 3-1-92 (as the numeral list reads it; p. 335 reads 99 [?])` → `Pā. Sū. 3-1-92` | SECOND-PASS Q1: [q170] Kannada p.344 prints ಅಚೋಯತ್ (ಪಾ. ಸೂ. ೩-೧-೯೨); p.335 prints ೩-೧-೯೯, each applied as printed, listed in open.tsv |
| 344 | ` (the numeral list reads 153 here and "6-1-2-3" on p. 335 [?])` → `` | SECOND-PASS S3: [q171] Kannada p.344 prints ಯತೋನಾವಃ (ಪಾ. ಸೂ. ೬-೧-೧೩), the number already in the English; the doubt note on other readings removed (p.335 prints ೬-೧-೨೧೩, listed  |
| 344 | `Pā. Sū. 7-2-117 (as the numeral list reads it [?])` → `Pā. Sū. 7-2-117` | SECOND-PASS Q2: [q172] Kannada p.344 prints ತದ್ಧಿತೇಷ್ವಚಾಮಾದೇಃ (ಪಾ ಸೂ.೭-೨-೧೧೭), agreeing with the English |
| 344 | `Pā. Sū. 8-1-731 (as the numeral list reads it [?])` → `Pā. Sū. 8-1-71` | SECOND-PASS Q1: [q173] Kannada p.344 prints ತಿಜಿ ಚೋದಾತ್ತವತಿ (ಪಾ. ಸೂ. ೮-೧-೭೧) |
| 345 | `(carrying across [?]) …` → `(carrying [one] across from troubles) …` | SECOND-PASS Q1: [q174] Kannada p.345-346 prints ತರುತ್ರಂ—(ತೊಂದರೆಗಳಿಂದ) ಪಾರುಮಾಡುವುದೂ ಆದ |
| 346 | `the one that bears [one] over dangers [?])` → `the one that carries [one] across from troubles)` | SECOND-PASS Q1: [q175] Kannada p.346 prints ತರುತ್ರಂ—(ತೊಂದರೆಗಳಿಂದ) ಪಾರುಮಾಡುವುದೂ |
| 346 | `sixteen [?] names of form` → `sixteen names of form` | SECOND-PASS Q2: [q177] Kannada p.346 prints ವರ್ಷ ಶಬ್ದವು ಹದಿನಾರು ರೂಪನಾಮ(ಗಳಲ್ಲಿ) (ನಿ. 3-13), agreeing with the English |
| 346 | `*aśvibhiḥ* [as read [?]]` → `*ātmīyaiḥ*` | SECOND-PASS Q1: [q176] Kannada p.346 prints ವರ್ಪಾಂಸಿ—ಆತ್ಮೀಯೈಃ ಕರ್ಮಭಿಃ ಕೃತಾನಿ ರೂಪಾಣಿ; IAST by sp_sanskrit.py |
| 347 | `iti tat-prastāve* [?] …"` → `iti tatparastādvakṣyati*"` | SECOND-PASS Q1: [q178] Kannada p.347 prints ಇತಿ ತತ್ಪರಸ್ತಾದ್ವಕ್ಷ್ಯತಿ; IAST by sp_sanskrit.py |

### 2026-11-27 second pass, batch m29-133.tsv
| page | old → new | why |
|---|---|---|
| 347 | ` [the Kannada exposition is partly in small type, read with doubt [?]]` → `` | SECOND-PASS Q2: [q29] Meta-remark clause removed with its mark; Kannada p.347 carries the passage |
| 347 | `(Pā. Sū. 6-1-70 (as the numeral list reads it here; p. 352 reads 70 [?]))` → `(Pā. Sū. 6-1-70)` | SECOND-PASS Q1: [q30] Kannada p.347 prints (ಪಾ. ಸೂ. ೬-೧-೭೦) |
| 347 | `root's *i*-vowel [?] by` → `root's *i*-vowel by` | SECOND-PASS Q2: [q31] Kannada p.347 prints ಧಾತುವಿನ ಇಕ್ಕಿಗೆ ಗುಣ, agrees |
| 348 | `(Pā. Sū. 3-2-102 (the list reads 103 on p. 348 and 102 on p. 363 for the same sūtra [?]))` → `(Pā. Sū. 3-2-103)` | SECOND-PASS Q1: [q32] Kannada p.348 prints ನಿಷ್ಠಾ (ಪಾ. ಸೂ. ೩-೨-೧೦೩); Kannada's number taken |
| 348 | `*vṛtyayo bahulam* [as read [?]]` → `*vyatyayo bahulam*` | SECOND-PASS Q1: [q34] Kannada p.348 prints ವ್ಯತ್ಯಯೋ ಬಹುಲಮ್ (IAST by sp_sanskrit.py) |
| 350 | `used in connection [?];` → `used in connection;` | SECOND-PASS Q2: [q35] Kannada p.350 prints ಚವಾಯೋಗೇ ಪ್ರಥಮೇತಿ ನಿಘಾತಪ್ರತಿಷೇಧಃ, agrees |
| 354 | `chaplain of Khela [as read [?]]` → `chaplain of Khela [as read]` | SECOND-PASS Q2: [q36] Kannada p.354 prints ಖೇಲಪುರೋಹಿತಸ್ಯ, agrees |
| 355 | `great-splendoured fish [?]"` → `great-splendoured fish"` | SECOND-PASS Q2: [q37] Kannada p.355 prints ಜಲೇ ಮತ್ಸ್ಯೋ ಮಹಾದ್ಯುತಿಃ, agrees |
| 356 | `*snādīnāṃ hrasvaḥ* (Pā. Sū. 7-3-80 [as read in the numeral list; the first word printed *p` → `*pvādīnāṃ hrasvaḥ* (Pā. Sū. 7-3-80)` | SECOND-PASS Q1: [q38] Kannada p.356 prints ಪ್ವಾದೀನಾಂ ಹ್ರಸ್ವಃ (ಪಾ. ಸೂ. ೭-೩-೮೦) (IAST by sp_sanskrit.py); the unmarked 'snādīnāṃ' at p.357 left, listed in open.tsv |
| 359 | `*ha ca chandasi* [?]` → `*vā ha ca chandasi*` | SECOND-PASS Q1: [q40] Kannada p.359 prints ವಾ ಹ ಚ ಛಂದಸೀತಿ (IAST by sp_sanskrit.py) |
| 362 | `(Pā. Sū. 7-2-4 as the list reads it [?])` → `(Pā. Sū. 7-2-4)` | SECOND-PASS Q1: [q42] Kannada p.362 prints ಕುತಿಹೋಃ (ಪಾ. ಸೂ. ೭-೨-೪) |
| 362 | `(Pā. Sū. 3-1-39; the numeral list reads this sūtra as 3-1-39 on pp. 362–363 and 3-1-39 on ` → `(Pā. Sū. 3-1-39)` | SECOND-PASS Q1: [q43] Kannada p.362 prints ಸುಪಾಂ ಸುಲುಕ್ (ಪಾ. ಸೂ. ೩-೧-೩೯) |
| 362 | `an *avagraha* would be present [?];` → `an *avagraha* would be present;` | SECOND-PASS Q2: [q44] Kannada p.362 prints ಇದನ್ನು ಅನುಸರಿಸಿದರೆ ಅವಗ್ರಹವಿದ್ದೇ ಇದೆ, agrees |
| 364 | `medical treatment [as read [?]]` → `medical treatment [as read]` | SECOND-PASS Q2: [q45] Kannada p.364 prints ಭೈಷಜ್ಯಲಕ್ಷಣೈಃ ಕರ್ಮಭಿಃ, agrees |
| 364 | `(in the form of a bright wealth [?], beauty [?])` → `(in the form of a thousand Ṛks, wealth, beauty)` | SECOND-PASS Q1: [q46] Kannada p.364 prints ಋಕ್ಸಹಸ್ರರೂಪಯಾ ಸಂಪದಾ ಕಾಂತ್ಯಾ; q46 and q47 settled in one edit |
| 365 | `aśmīyaiḥ* [as read [?]]` → `ātmīyaiḥ*` | SECOND-PASS Q1: [q48] Kannada p.365 prints ಆತ್ಮೀಯೈಃ ಭೈಷಜ್ಯರೂಪೈಃ ಕರ್ಮಭಿಃ (IAST by sp_sanskrit.py) |
| 365 | `a thousand [shining things — printed 'śukla' [?]] and Sūryā` → `a thousand Ṛks (staked as the wager) and Sūryā` | SECOND-PASS Q1: [q49] Kannada p.365 prints ಪಣವಾಗಿಟ್ಟಿದ್ದ ಸಹಸ್ರ ಋಕ್ಕುಗಳನ್ನೂ ಸೂರ್ಯಾ ಎಂಬವಳನ್ನೂ |
| 367 | `*sārvadhātukam apit* (Pā. Sū. 1-2-4 as read [?]) makes` → `*sārvadhātukam apit* makes` | SECOND-PASS S3: [q50] Kannada p.367 prints ಸಾರ್ವಧಾತುಕಮಪಿತ್ with no sūtra number; number removed |
| 368 | `with ancient praises [?],` → `with ancient praises,` | SECOND-PASS Q2: [q51] Kannada p.368 prints ಪುರಾತನ ಸ್ತುತಿವಾಕ್ಯಗಳಿಂದ, agrees |
| 370 | `*bahuvacane jhalyet* [as printed; Pā. number illegible in the list [?]],` → `*bahuvacane jhalyet*,` | SECOND-PASS S3: [q52] Kannada p.370 prints ಬಹುವಚನೇ ಝಲ್ಯೇತ್ with no sūtra number; number removed |
| 370 | `(U. Sū. 1-150 as the list reads it [?])` → `(U. Sū. 1-150)` | SECOND-PASS Q1: [q53] Kannada p.370 prints ಇಣ್ ಶೀಜ್ಭ್ಯಾಂ ವನ್ (ಉ. ಸೂ. ೧-೧೫೦) |
| 371 | `(U. Sū. 2-186? [as read, partly illegible [?]])` → `(U. Sū. 2-186)` | SECOND-PASS Q1: [q55] Kannada p.371 prints ಋಜ್ರೇಂದ್ರಾಗ್ರವಜ್ರ (ಉ. ಸೂ. ೨-೧೮೬) |
| 374 | `(Pā. Sū. 3-4-117 [as read; list 3-4-17 [?]])` → `(Pā. Sū. 3-4-107)` | SECOND-PASS Q1: [q57] Kannada p.374 prints ಛಂದಸ್ಯುಭಯಥಾ (ಪಾ. ಸೂ. ೩-೪-೧೦೭); Kannada's number taken |
| 376 | `whose light is uncovered [?].` → `whose light is uncovered.` | SECOND-PASS Q2: [q58] Kannada p.376 prints ವೃಕ ಇತಿ ವಿವೃತಜ್ಯೋತಿಷ್ಕಃ ಸೂರ್ಯ ಉಚ್ಯತೇ, agrees |
| 376 | `as he turns...' [?] —` → `as he turns...' —` | SECOND-PASS Q2: [q59] Kannada p.376 prints ಆದಿತ್ಯೋಽಪಿ ವೃಕ ಉಚ್ಯತೇ ಯದಾವೃಂಕ್ತೇ, agrees |
| 376 | `'Uṣas, desiring a horse [?], was seized by Āditya; the Aśvins freed her'` → `'Uṣas, seized by Āditya, called the Aśvins; the Aśvins freed her'` | SECOND-PASS Q1: [q60] Kannada p.376 prints ಆಹ್ವಯದುಷಾ ಅಶ್ವಿನಾವಾದಿತ್ಯೇನಾಭಿಗ್ರಸ್ತಾ ತಾಮಶ್ವಿನೌ ಪ್ರಮುಮುಚತುರಿತ್ಯಾಖ್ಯಾನಂ |
| 380 | `since the suffix is *jit-* [?] [as read: "*jid-dvāva*"],` → `since the suffix has *jidvadbhāva*,` | SECOND-PASS Q1: [q61] Kannada p.380 prints ಪ್ರತ್ಯಯಕ್ಕೆ ಜಿದ್ವದ್ಭಾವವಿರುವುದರಿಂದ (IAST by sp_sanskrit.py); unmarked '(Pā. Sū. 2-4 [list])' vs Kannada ೨-೪-೭೨ left |
| 381 | `(*vāhana*) [as read [?]]` → `(*vāhana*) [as read]` | SECOND-PASS Q2: [q62] Kannada p.381 prints ಅಶ್ವಿನೋರ್ವಾಹನಾಯ ರಾಸಭಾಯ, agrees |
| 381 | `the father's curse [?];` → `the father's curse;` | SECOND-PASS Q2: [q63] Kannada p.381 prints ಪಿತೃಶಾಪಾನ್ನಷ್ಟೇ ಚಕ್ಷುಷೀ, agrees |
| 383 | `since *īt-va* [?] is` → `since *īt-va* is` | SECOND-PASS Q2: [q64] Kannada p.383 prints ಈತ್ವವು ಪರಸೂತ್ರದಿಂದ ವಿಧಿಸಿರುವುದರಿಂದ, agrees |
| 383 | `[Pā. Sū. 3-4-94 as read [?]]` → `[Pā. Sū. 3-4-9]` | SECOND-PASS Q1: [q65] Kannada p.384 prints ತುಮನರ್ಥೇ ಸೇಸೇನಸೇ… (ಪಾ. ಸೂ. ೩-೪-೯); Kannada's number taken |
| 387 | `*vicchoyīvāyoḥ* [as read [?]]` → `*ecoyavāyāvaḥ*` | SECOND-PASS Q1: [q66] Kannada p.387 prints ಏಚೋಯವಾಯಾವಃ ಎಂಬುದರಿಂದ ಅಯಾದೇಶ (IAST by sp_sanskrit.py) |
| 389 | `the fifth case [?]…` → `the fifth case…` | SECOND-PASS Q2: [q68] Kannada p.389 prints ಪಂಚಮೀ ಕರ್ಮಾಣಂ, agrees |
| 389 | `visīvyati deśāv iti* [as read [?]]` → `visīvyati deśāv iti* [as read]` | SECOND-PASS Q2: [q69] Kannada p.389 prints ವಿಸೀವ್ಯತಿ ದೇಶಾವಿತಿ, agrees |
| 391 | `Uṇ. sū. 4-557 as read [?]]` → `Uṇ. sū. 4-557]` | SECOND-PASS Q1: [q70] Kannada p.391 prints ಇನ್ ಸರ್ವಧಾತುಭ್ಯಃ (ಉ. ಸೂ. ೪-೫೫೭) |
| 391 | `(U. Sū. 4-188 as read [?])` → `(U. Sū. 4-628)` | SECOND-PASS Q1: [q71] Kannada p.391 prints ಸರ್ವಧಾತುಭ್ಯ ಅಸುನ್ (ಉ. ಸೂ. ೪-೬೨೮); Kannada's number taken |
| 392 | `specially attached to [?], i.e. with wasted limbs [?];` → `with the limbs specially attached, i.e. with wasted limbs;` | SECOND-PASS Q1: [q72] Kannada p.392 prints ವಿಷಕ್ತಾಂ ವಿಶೇಷೇಣ ಸಕ್ತಾವಯವಾಂ । ಕೃಶಾವಯವಾಂ; q72 and q73 settled in one edit |
| 393 | `much emaciated [?];` → `much emaciated;` | SECOND-PASS Q2: [q74] Kannada p.393 prints ವಿಷಕ್ತಾಂ—ಬಹಳಕೃಶವಾಗಿದ್ದ, agrees |
| 394 | `fifty-one names of speech (Ni. 1-11 [as read]), among the twenty-six names of action (Ni. ` → `fifty-seven names of speech (Ni. 2-23), among the twenty-six names of action (Ni. 3-2), an` | SECOND-PASS Q1: [q75] Kannada p.394 prints ಐವತ್ತೇಳು ವಾಙ್ನಾಮಗಳಲ್ಲಿಯೂ (ನಿ. ೨-೨೩) ಇಪ್ಪತ್ತಾರು ಕರ್ಮನಾಮಗಳಲ್ಲಿಯೂ (ನಿ. ೩-೨) ಹದಿನಾಲ್ಕು ಪ್ರಜ್ಞಾನಾಮಗಳಲ್ಲಿಯೂ (ನಿ. ೩-೧೩); Kannada's figures t |
| 394 | `(U. Sū. 4-158 as read [?])` → `(U. Sū. 4-438)` | SECOND-PASS Q1: [q76] Kannada p.394 prints ಅವಿತ್ಯಸ್ತಂತ್ರಿಭ್ಯ ಈಃ (ಉ. ಸೂ. ೪-೪೩೮) |
| 394 | `*yaṇ* substituted; the *udātta* standing in the place of the semivowel [?];` → `*yaṇ* substituted in the place of the *udātta*;` | SECOND-PASS Q1: [q77] Kannada p.394 prints ಉದಾತ್ತ ಸ್ಥಾನದಲ್ಲಿ ಯಣಾದೇಶ ಬಂದು |
| 397 | `(Ni. 3-48 as read [?])` → `(Ni. 12-34)` | SECOND-PASS Q1: [q78] Kannada p.397 prints ಮನುರ್ಮನನಾತ್ (ನಿ. ೧೨-೩೪) |
| 399 | `[the root] is *jit* [?],` → `[the root] is *jit*,` | SECOND-PASS Q2: [q79] Kannada p.399 prints ಅಪಿತ್ತಾದ ಸಾರ್ವಧಾತುಕ ... ಜಿದ್ವದ್ಭಾವವಿರುವುದರಿಂದ, agrees |
| 407 | `for the root *sac* in the group [?];` → `for the root *ṣaca samavāye*;` | SECOND-PASS Q1: [q80] Kannada p.407 prints ಛಾಂದಸವಾಗಿ ಷಚ ಸಮವಾಯೇ ಈ ಧಾತುವಿಗೆ ಣ್ವಿ ಪ್ರತ್ಯಯ (IAST by sp_sanskrit.py) |
| 410 | `*a* for the *m* [?];` → `*a* for the *m*;` | SECOND-PASS Q2: [q81] Kannada p.410 prints ವ್ಯತ್ಯಯದಿಂದ ಮಕಾರಕ್ಕೆ ಆತ್ವ, agrees (Kannada ರರಮ್ vs English 'rerām' listed in open.tsv) |
| 412 | `the sacrifice (?) [as read [?]]:` → `the sacrifice:` | SECOND-PASS Q2: [q83] Kannada p.412 prints ವಿದಥಂ ವೇದಯಂತಮತಿಥಿಂ, agrees |
| 412 | `suffix [*athan*?] [?])` → `suffix *atha*)` | SECOND-PASS Q1: [q84] Kannada p.412 prints ರುವಿದಿಭ್ಯಾಂ ಕಿದಿತ್ಯಥಪ್ರತ್ಯಯಃ |
| 415 | `the [third (?) — printed *śaitīyam* [?]] sūkta` → `the third sūkta` | SECOND-PASS Q1: [q85] Kannada p.415 prints ತೃತೀಯಂ ಸೂಕ್ತಂ |
| 415 | `*(small numerals; read "19, 20" — as printed [?])*` → `१८, १९` | SECOND-PASS Q1: [q86] Kannada p.415 prints ವರ್ಗ-೧೮, ೧೯ (Devanagari digits made by sp_sanskrit.py) |
| 416 | `the name for horses is *śyena* [?]]` → `the name for horses is *śyena*]` | SECOND-PASS Q2: [q87] Kannada p.416 prints ಶ್ಯೇನಾ ಇತ್ಯಶ್ವನಾಮ, agrees |
| 419 | `since it is *su*-final [?] and *ugit*, *num*` → `when *su* follows, and since it is *ugit*, *num*` | SECOND-PASS Q1: [q88] Kannada p.419 prints ಸುಪರವಾದಾಗ ಉಗಿತ್ತಾದುದರಿಂದ ನುಮಾಗಮ |
| 423 | `*pravate iti gatikarmā* [as read [?]]` → `*pravate iti gatikarmā* [as read]` | SECOND-PASS Q2: [q89] Kannada p.423 prints ಪ್ರವತೇ ಇತಿ ಗತಿಕರ್ಮಾ, agrees |
| 423 | `yāmaḥ yajñaḥ* [?]` → `yāmaḥ yajñaḥ*` | SECOND-PASS Q2: [q90] Kannada p.423 prints ಯಾಂತಿ ದೇವತಾ ಯಸ್ಮಿನ್ ಸಃ ಯಾಮಾ ಯಜ್ಞಃ, agrees |
| 431 | `U. Sū. 1-154 as read [?]]` → `U. Sū. 1-149]` | SECOND-PASS Q1: [q91] Kannada p.431 prints ಅಶುಪುಷಿ—(ಉ. ಸೂ. ೧-೧೪೯) ಎಂಬುದರಿಂದ ಕ್ವನ್ ಪ್ರತ್ಯಯ; Kannada's number taken |
| 435 | `pressing-chamber [?]` → `pressing-chamber` | SECOND-PASS Q2: [q92] Kannada p.435 prints ಶತದ್ವಾರೇ ಪೀಡಾಯಂತ್ರಗೃಹೇ, agrees |
| 435 | `with cold water [?];` → `with cold water;` | SECOND-PASS Q2: [q93] Kannada p.435 prints ತುಷಾಗ್ನಿಂ ಶೀತೇನೋದಕೇನ, agrees |
| 435 | `know the dawn in the rain [?]'` → `know the risen dawn'` | SECOND-PASS Q1: [q94] Kannada p.435/436 prints ಇಹಾಸೀನಃ ಸನ್ ವ್ಯುಷ್ಟಾಮುಷಸಂ ಜಾನೀಹಿ (vyuṣṭām uṣasam, not 'in the rain') |
| 435 | `shows the dawn [?].` → `shows the dawn.` | SECOND-PASS Q2: [q95] Kannada p.436 prints ಉಷಃಕಾಲ ಸೂಚಕವಾದ ವೀಣಾಧ್ವನಿ, agrees |
| 436 | `vṛṣṭyām uṣasaṃ jānīhi iti andhakāragṛhe praveśitāya kaṇvāya ṛṣaye* [?]` → `vyuṣṭām uṣasaṃ jānīhi iti andhakāragṛhe praveśitāya kaṇvāya ṛṣaye*` | SECOND-PASS Q1: [q96] Kannada p.436 prints ವ್ಯುಷ್ಟಾಮುಷಸಂ ಜಾನೀಹಿ ಇತಿ ಅಂಧಕಾರಗೃಹೇ ಪ್ರವೇಶಿತಾಯ ಕಣ್ಣಾಯ ಋಷಯೇ (IAST by sp_sanskrit.py) |
| 439 | `seized by the Sun [?].` → `seized by the Sun.` | SECOND-PASS Q2: [q97] Kannada p.439 prints ಆದಿತ್ಯನಿಂದ (ಗ್ರಸ್ತಳಾಗಿದ್ದವಳನ್ನು), agrees |
| 439 | `(the sun's) seizure [?];` → `(the sun's) seizure;` | SECOND-PASS Q2: [q98] Kannada p.439 prints ಅಂಹಸಃ—ಆದಿತ್ಯನಿಂದ, agrees |
| 441 | `(Pā. Sū. 7-1-59 as read; compare 7-1-55 at p. 335 [?])` → `(Pā. Sū. 7-1-59)` | SECOND-PASS Q1: [q99] Kannada p.441 prints ಶೇಮುಚಾದೀನಾಮ್ (ಪಾ. ಸೂ. ೭-೧-೫೯) |
| 442 | `[for] the enemy of the *vaiśya*?? [as read [?]]` → `[for] the enemy` | SECOND-PASS Q1: [q100] Kannada p.442 prints ಅರ್ಯೋರೇಃ ಶತ್ರೋಃ and ಆರ್ಯಃ—ಶತ್ರುವಿಗೆ |
| 450 | `*parameśvaryeṇa vithyam āsevitāḥ* [as read; small type [?]] — 'those served with supreme l` → `*paramaiśvaryeṇa nityamāsevitāḥ* — 'those constantly served with supreme lordship'` | SECOND-PASS Q1: [q101] Kannada p.450 prints ಪರಮೈಶ್ವರ್ಯೇಣ ನಿತ್ಯಮಾಸೇವಿತಾಃ, ಪರಮೈಶ್ವರ್ಯದಿಂದ ದಿನಂಪ್ರತಿಯೂ (IAST by sp_sanskrit.py) |
| 451 | `(Pā. Sū. 6-1-160 [as read; the page reads *6-1-100* [?]])` → `(Pā. Sū. 6-1-160)` | SECOND-PASS Q1: [q102] Kannada p.451 prints ಉತ್ತಮ ಶಶ್ವತ್ತಮೌ ಸರ್ವತ್ರ (ಪಾ. ಸೂ. ೬-೧-೧೬೦) |
| 452 | `*(small numerals; read "20, 21" — as printed [?])*` → `२०, २१` | SECOND-PASS Q1: [q103] Kannada p.452 prints ವರ್ಗ—೨೦, ೨೧ (Devanagari digits made by sp_sanskrit.py) |
| 457 | `*mahāvīra* vessel [?],` → `*mahāvīra* vessel,` | SECOND-PASS Q2: [q104] Kannada p.457 prints ಘರ್ಮಂ ಮಹಾವೀರಸ್ಥಂ, agrees |
| 464 | `*anakāra* [?] has come` → `*anakāra* has come` | SECOND-PASS Q2: [q105] Kannada p.464 prints ಅನಕಾರದ ಪರದಲ್ಲಿ ಬಂದಂತಾಗುವುದರಿಂದ, agrees |
| 465 | `— the *a*-ending [?]; the *yatva*` → `— *etva* does not come; the *yatva*` | SECOND-PASS Q1: [q106] Kannada p.465 prints ಓಸಿ ಚ ಎಂಬುದರಿಂದ ಏತ್ವ ಬರುವುದಿಲ್ಲ |
| 465 | `[as read: *cekitthe*? [?]]` → `[on the stem *cekitya*]` | SECOND-PASS Q1: [q107] Kannada p.465 prints ಚೇಕಿತ್ಯ ಎಂಬುದರ ಮೇಲೆ ಲಿಟ್ (IAST by sp_sanskrit.py) |
| 468 | `in place of *śluḥ* [?];` → `in place of *śluḥ*;` | SECOND-PASS Q2: [q108] Kannada p.468 prints ಶ್ಲುವಿಗೆ ಬದಲಾಗಿ ಶವಿಕರಣ, agrees |
| 469 | `(as read; Pā. Sū. 6-2-?? [?])` → `(Pā. Sū. 6-2-21-1)` | SECOND-PASS Q1: [q109] Kannada p.469 prints ದಿವೋದಾಸಾದೀನಾಂ ಛಂದಸ್ಯುಪಸಂಖ್ಯಾನಮ್ (ಪಾ. ಸೂ. ೬-೨-೨೧-೧) |
| 470 | `for friendship (for [the sake of] the Sun [?])` → `for friendship` | SECOND-PASS Q1: [q110] Kannada p.470/471 prints ಸಖ್ಯಾಯ—ಸ್ನೇಹಕ್ಕೋಸ್ಕರ, no mention of the Sun |
| 479 | `*aśvāghasya* [?] *yat*` → `*aghnyādayaś ca*, *yat*` | SECOND-PASS Q1: [q111] Kannada p.479 (Bhāṣya) prints ಪನ ಸ್ತುತ್ । ಅಘ್ನ್ಯಾದಯಶ್ಚೇತಿ ಭಾವೇ ಯತ್ (IAST by sp_sanskrit.py) |
| 496 | `*vikāra-ādeśayoḥ pare ṣaṭkṛṣṇa* [as read [?]] *tanuśirā*` → `*ekādaśinoḥ paraḥ ṣaṭkastanuśirā*` | SECOND-PASS Q1: [q114] Kannada p.496 prints ಏಕಾದಶಿನೋಃ ಪರಃ ಷಟ್ಕಸ್ತನುಶಿರಾ (IAST by sp_sanskrit.py) |
| 498 | `*(small numerals; read "22, 23" — as printed [?])*` → `२२, २३` | SECOND-PASS Q1: [q115] Kannada p.498 prints ವರ್ಗ—೨೨, ೨೩ (Devanagari digits made by sp_sanskrit.py) |
| 503 | `By the rule of the *pareṇa kṛtā* [?]` → `By the rule of residue (*pariśeṣanyāya*)` | SECOND-PASS Q1: [q116] Kannada p.503 prints ಪರಿಶೇಷನ್ಯಾಯದಿಂದ (IAST by sp_sanskrit.py) |
| 504 | `elision by the *ḍā*-substitution [?];` → `elision by the *ḍā*-substitution;` | SECOND-PASS Q2: [q117] Kannada p.504 prints ಡಾದೇಶ. ದಿತ್ವ ಸಾಮರ್ಥ್ಯದಿಂದ ಟಿಗೆ ಲೋಪ, agrees |
| 506 | `*mananīyam ṛjujātam* [as read [?]]` → `*mananīyam arthajātam*` | SECOND-PASS Q1: [q118] Kannada p.506 prints ಮನ್ಮ ಮನನೀಯಮರ್ಥಜಾತಂ ಎಂದು ವೃತ್ತಿಕಾರರು (IAST by sp_sanskrit.py) |
| 509 | `the eight [?] names` → `the eight names` | SECOND-PASS Q2: [q119] Kannada p.509 prints ಪಾಕ ಶಬ್ದವು ಎಂಟು ಪ್ರಶಸ್ಯನಾಮ…, agrees |
| 510 | `accusative [as printed: dual] following with *plural* [?],` → `accusative plural following,` | SECOND-PASS Q1: [q120] Kannada p.510 prints ದ್ವಿತೀಯಾ ಬಹುವಚನ ಪರವಾದಾಗ (accusative plural) |
| 520 | `na kaṃnoteḥ yuvām [?] arthamupakṣayathaḥ` → `na tanoteḥ yuvāmatyarthamupakṣayathāḥ` | SECOND-PASS Q1: [q122] Kannada p.520 prints ನ ತನೋತೇಃ ಯುವಾಮತ್ಯರ್ಥಮುಪಕ್ಷಯಥಾಃ (IAST by sp_sanskrit.py); q122 and q123 are in the same remark |
| 520 | `ity arthaḥ* [as read; small type [?]] — 'the form` → `ity arthaḥ* [as read] — 'the form` | SECOND-PASS Q2: [q123] Kannada p.520 prints the rest of the passage (ಯಸ್ಮೈ ದೇಯಂ ಧನಂ ... ಇತ್ಯರ್ಥಃ), agrees |
| 521 | `the elision of the *ati* [?] occurs` → `the elision of the *ati* occurs` | SECOND-PASS Q2: [q124] Kannada p.521 prints ಛಾಂದಸವಾಗಿ ಅತಿಗೆ ಲೋಪ ಬರುತ್ತದೆ, agrees |
| 526 | `[as read; Pā. Sū. 3-2-171 vārttika? [?]]` → `(Pā. Sū. 3-2-171-1)` | SECOND-PASS Q1: [q125] Kannada p.526 prints ಉತ್ಸರ್ಗಶ್ಛಂದಸಿ (ಪಾ. ಸೂ. ೩-೨-೧೭೧-೧) |
| 530 | `[and] the *āhavanīya* [?] etc.` → `[and] the *ahīna* [rites] etc.` | SECOND-PASS Q1: [q126] Kannada p.530 prints ಸತ್ರಾಹೀನಾದಿಯಾಗ and ಸತ್ರಯಾಗ, ಅಹೀನರೂಪವಾದ ಕ್ರತುಗಳು |
| 533 | `twenty-eight [?] names` → `twenty-eight names` | SECOND-PASS Q2: [q127] Kannada p.533 prints ಇಪ್ಪತ್ತೆಂಟು ಧನನಾಮಗಳಲ್ಲಿ (ನಿ. ೩-೯), agrees (unmarked 'Ni. 2-10 [as read]' differs, in open.tsv) |
| 537 | `*(small numerals; read "24, 25, 26" — as printed [?])*` → `२४, २५, २६` | SECOND-PASS Q1: [q128] Kannada p.537 prints ವರ್ಗ-೨೪, ೨೫, ೨೬ (Devanagari digits made by sp_sanskrit.py) |
| 544 | `twenty-one [?] names of the earth (Ni. 1-?? [as read: 'ನಿ. ೧-೩'])` → `twenty-one names of the earth (Ni. 2-5)` | SECOND-PASS Q1: [q129] Kannada p.544 prints ಇಪ್ಪತ್ತೊಂದು ಪೃಥಿವೀನಾಮಗಳಲ್ಲಿ (ನಿ ೨-೫); Kannada's number taken |
| 547 | `*dhārer ṇiluk ca* [as read; Uṇ. sū. 3-?? [?]],` → `*dhārer ṇiluk ca*,` | SECOND-PASS S3: [q130] Kannada p.547 prints ಧಾರೇರ್ಣಿಲುಕ್‌ಚ—ಎಂಬುದರಿಂದ with no sūtra number; number removed |
| 560 | `asuras who trouble the Śiśnas [?] and the like` → `asuras and others who trouble the righteous` | SECOND-PASS Q1: [q131] Kannada p.560 prints ಶಿಷ್ಟರನ್ನು ಬಾಧೆಮಾಡುವ ಅಸುರರೇ ಮೊದಲಾದವರನ್ನು |
- 2026-11-27: Rigveda_Samhita_Vol9_Kannada_Text.md: 56 Pratipadārtha words corrected by tools/rv/pratipada_apply.py (one letter, confirmed by the supplied Pada block and the Wikisource Pada); each is a row of data/source_fixes.tsv.
| 15 | `2-20` → `9-20` | NUMBER the supplied text reads 9-20 (one digit differs; no other candidate on pages 14-16); 1 occurrence(s) on the page |
| 39 | `6-1-161` → `6-1-171` | NUMBER the supplied text reads 6-1-171 (one digit differs; no other candidate on pages 38-40); 1 occurrence(s) on the page |
| 47 | `76-2-13` → `7-2-13` | NUMBER the supplied text reads 7-2-13 (one digit differs; no other candidate on pages 46-48); 1 occurrence(s) on the page |
| 55 | `3-1-50` → `7-1-50` | NUMBER the supplied text reads 7-1-50 (one digit differs; no other candidate on pages 54-56); 1 occurrence(s) on the page |
| 59 | `8-2` → `8-7` | NUMBER the supplied text reads 8-7 (one digit differs; no other candidate on pages 58-60); 1 occurrence(s) on the page |
| 64 | `2-18` → `2-19` | NUMBER the supplied text reads 2-19 (one digit differs; no other candidate on pages 63-65); 1 occurrence(s) on the page |
| 65 | `1-95-13` → `1-92-13` | NUMBER the supplied text reads 1-92-13 (one digit differs; no other candidate on pages 64-66); 1 occurrence(s) on the page |
| 66 | `1-9` → `1-7` | NUMBER the supplied text reads 1-7 (one digit differs; no other candidate on pages 65-67); 1 occurrence(s) on the page |
| 73 | `1-95-13` → `1-92-13` | NUMBER the supplied text reads 1-92-13 (one digit differs; no other candidate on pages 72-74); 1 occurrence(s) on the page |
| 73 | `6-1-215` → `6-1-213` | NUMBER the supplied text reads 6-1-213 (one digit differs; no other candidate on pages 72-74); 1 occurrence(s) on the page |
| 74 | `8-3-60` → `8-3-68` | NUMBER the supplied text reads 8-3-68 (one digit differs; no other candidate on pages 73-75); 1 occurrence(s) on the page |
| 74 | `6-1-184` → `6-1-189` | NUMBER the supplied text reads 6-1-189 (one digit differs; no other candidate on pages 73-75); 1 occurrence(s) on the page |
| 96 | `1-151-7` → `1-151-2` | NUMBER the supplied text reads 1-151-2 (one digit differs; no other candidate on pages 95-97); 1 occurrence(s) on the page |
| 98 | `1-94` → `1-9` | NUMBER the supplied text reads 1-9 (one digit differs; no other candidate on pages 97-99); 1 occurrence(s) on the page |
| 106 | `10-2` → `10-7` | NUMBER the supplied text reads 10-7 (one digit differs; no other candidate on pages 105-107); 1 occurrence(s) on the page |
| 112 | `2-11-21` → `9-11-21` | NUMBER the supplied text reads 9-11-21 (one digit differs; no other candidate on pages 111-113); 1 occurrence(s) on the page |
| 121 | `10-67-6` → `10-67-7` | NUMBER the supplied text reads 10-67-7 (one digit differs; no other candidate on pages 120-122); 1 occurrence(s) on the page |
| 140 | `10-15` → `10-16` | NUMBER the supplied text reads 10-16 (one digit differs; no other candidate on pages 139-141); 1 occurrence(s) on the page |
| 144 | `6-1-139` → `6-2-139` | NUMBER the supplied text reads 6-2-139 (one digit differs; no other candidate on pages 143-145); 1 occurrence(s) on the page |
| 180 | `5-6-5-3` → `5-6-51-3` | NUMBER the supplied text reads 5-6-51-3 (one digit differs; no other candidate on pages 179-181); 1 occurrence(s) on the page |
| 194 | `1-112-20` → `1-102-20` | NUMBER the supplied text reads 1-102-20 (one digit differs; no other candidate on pages 193-195); 1 occurrence(s) on the page |
| 210 | `6-100-5` → `7-100-5` | NUMBER the supplied text reads 7-100-5 (one digit differs; no other candidate on pages 209-211); 1 occurrence(s) on the page |
| 210 | `1-4` → `1-9` | NUMBER the supplied text reads 1-9 (one digit differs; no other candidate on pages 209-211); 1 occurrence(s) on the page |
| 212 | `4-557` → `4-551` | NUMBER the supplied text reads 4-551 (one digit differs; no other candidate on pages 211-213); 2 occurrence(s) on the page |
| 218 | `6-13` → `6-15` | NUMBER the supplied text reads 6-15 (one digit differs; no other candidate on pages 217-219); 1 occurrence(s) on the page |
| 257 | `3-9` → `3-19` | NUMBER the supplied text reads 3-19 (one digit differs; no other candidate on pages 256-258); 1 occurrence(s) on the page |
| 258 | `1-117-16` → `1-116-16` | NUMBER the supplied text reads 1-116-16 (one digit differs; no other candidate on pages 257-259); 1 occurrence(s) on the page |
| 295 | `1-117-620` → `1-117-20` | NUMBER the supplied text reads 1-117-20 (one digit differs; no other candidate on pages 294-296); 1 occurrence(s) on the page |
| 311 | `10-149-4` → `10-149-5` | NUMBER the supplied text reads 10-149-5 (one digit differs; no other candidate on pages 310-312); 1 occurrence(s) on the page |
| 330 | `1-116-11` → `1-116-1` | NUMBER the supplied text reads 1-116-1 (one digit differs; no other candidate on pages 329-331); 1 occurrence(s) on the page |
| 338 | `10-39-3` → `10-39-5` | NUMBER the supplied text reads 10-39-5 (one digit differs; no other candidate on pages 337-339); 1 occurrence(s) on the page |
| 351 | `1-1` → `12-1` | NUMBER the supplied text reads 12-1 (one digit differs; no other candidate on pages 350-352); 2 occurrence(s) on the page |
| 351 | `1-164-46` → `1-164-47` | NUMBER the supplied text reads 1-164-47 (one digit differs; no other candidate on pages 350-352); 1 occurrence(s) on the page |
| 353 | `6-1-50` → `7-1-50` | NUMBER the supplied text reads 7-1-50 (one digit differs; no other candidate on pages 352-354); 1 occurrence(s) on the page |
| 353 | `6-1-168` → `6-1-18` | NUMBER the supplied text reads 6-1-18 (one digit differs; no other candidate on pages 352-354); 1 occurrence(s) on the page |
| 357 | `6-1-39` → `3-1-39` | NUMBER the supplied text reads 3-1-39 (one digit differs; no other candidate on pages 356-358); 1 occurrence(s) on the page |
| 367 | `6-1-168` → `6-1-18` | NUMBER the supplied text reads 6-1-18 (one digit differs; no other candidate on pages 366-368); 1 occurrence(s) on the page |
| 370 | `1-156` → `1-157` | NUMBER the supplied text reads 1-157 (one digit differs; no other candidate on pages 369-371); 1 occurrence(s) on the page |
| 379 | `7-3-94` → `6-3-94` | NUMBER the supplied text reads 6-3-94 (one digit differs; no other candidate on pages 378-380); 1 occurrence(s) on the page |
| 384 | `3-4-94` → `3-4-9` | NUMBER the supplied text reads 3-4-9 (one digit differs; no other candidate on pages 383-385); 1 occurrence(s) on the page |
| 418 | `4-52-1` → `4-57-1` | NUMBER the supplied text reads 4-57-1 (one digit differs; no other candidate on pages 417-419); 1 occurrence(s) on the page |
| 428 | `6-1-50` → `7-1-50` | NUMBER the supplied text reads 7-1-50 (one digit differs; no other candidate on pages 427-429); 1 occurrence(s) on the page |
| 444 | `7-4-82` → `6-4-82` | NUMBER the supplied text reads 6-4-82 (one digit differs; no other candidate on pages 443-445); 1 occurrence(s) on the page |
| 445 | `6-4-4` → `6-4-41` | NUMBER the supplied text reads 6-4-41 (one digit differs; no other candidate on pages 444-446); 1 occurrence(s) on the page |
| 459 | `3-2-34` → `3-2-74` | NUMBER the supplied text reads 3-2-74 (one digit differs; no other candidate on pages 458-460); 1 occurrence(s) on the page |
| 460 | `3-2-76` → `3-3-76` | NUMBER the supplied text reads 3-3-76 (one digit differs; no other candidate on pages 459-461); 1 occurrence(s) on the page |
| 460 | `6-1-163` → `6-1-167` | NUMBER the supplied text reads 6-1-167 (one digit differs; no other candidate on pages 459-461); 1 occurrence(s) on the page |
| 464 | `3-4-61` → `7-4-61` | NUMBER the supplied text reads 7-4-61 (one digit differs; no other candidate on pages 463-465); 1 occurrence(s) on the page |
| 464 | `6-1-163` → `6-1-167` | NUMBER the supplied text reads 6-1-167 (one digit differs; no other candidate on pages 463-465); 1 occurrence(s) on the page |
| 465 | `6-2-115` → `7-2-115` | NUMBER the supplied text reads 7-2-115 (one digit differs; no other candidate on pages 464-466); 1 occurrence(s) on the page |
| 477 | `6-1-163` → `6-1-167` | NUMBER the supplied text reads 6-1-167 (one digit differs; no other candidate on pages 476-478); 1 occurrence(s) on the page |
| 490 | `7-1-39` → `3-1-39` | NUMBER the supplied text reads 3-1-39 (one digit differs; no other candidate on pages 489-491); 1 occurrence(s) on the page |
| 496 | `6-3` → `6-5` | NUMBER the supplied text reads 6-5 (one digit differs; no other candidate on pages 495-497); 1 occurrence(s) on the page |
| 497 | `2-5` → `7-5` | NUMBER the supplied text reads 7-5 (one digit differs; no other candidate on pages 496-498); 2 occurrence(s) on the page |
| 497 | `6-8` → `6-3` | NUMBER the supplied text reads 6-3 (one digit differs; no other candidate on pages 496-498); 1 occurrence(s) on the page |
| 504 | `6-3-136` → `6-3-133` | NUMBER the supplied text reads 6-3-133 (one digit differs; no other candidate on pages 503-505); 1 occurrence(s) on the page |
| 507 | `7-1-39` → `3-1-39` | NUMBER the supplied text reads 3-1-39 (one digit differs; no other candidate on pages 506-508); 1 occurrence(s) on the page |
| 510 | `6-2-116` → `7-2-116` | NUMBER the supplied text reads 7-2-116 (one digit differs; no other candidate on pages 509-511); 1 occurrence(s) on the page |
| 521 | `7-4-93` → `3-4-93` | NUMBER the supplied text reads 3-4-93 (one digit differs; no other candidate on pages 520-522); 1 occurrence(s) on the page |
| 522 | `3-2-170` → `7-2-170` | NUMBER the supplied text reads 7-2-170 (one digit differs; no other candidate on pages 521-523); 1 occurrence(s) on the page |
| 525 | `6-2-139` → `6-2-159` | NUMBER the supplied text reads 6-2-159 (one digit differs; no other candidate on pages 524-526); 1 occurrence(s) on the page |
| 529 | `7-1-39` → `3-1-39` | NUMBER the supplied text reads 3-1-39 (one digit differs; no other candidate on pages 528-530); 1 occurrence(s) on the page |
| 534 | `3-1-934` → `3-1-134` | NUMBER the supplied text reads 3-1-134 (one digit differs; no other candidate on pages 533-535); 1 occurrence(s) on the page |
| 577 | `2-225` → `2-25` | NUMBER the supplied text reads 2-25 (one digit differs; no other candidate on pages 576-578); 1 occurrence(s) on the page |
| 590 | `4-1-19` → `8-1-19` | NUMBER the supplied text reads 8-1-19 (one digit differs; no other candidate on pages 589-591); 1 occurrence(s) on the page |
| 590 | `8-3-2` → `8-3-3` | NUMBER the supplied text reads 8-3-3 (one digit differs; no other candidate on pages 589-591); 1 occurrence(s) on the page |
| 595 | `6-1-185` → `6-1-155` | NUMBER the supplied text reads 6-1-155 (one digit differs; no other candidate on pages 594-596); 1 occurrence(s) on the page |
| 602 | `6-1-168` → `6-1-18` | NUMBER the supplied text reads 6-1-18 (one digit differs; no other candidate on pages 601-603); 1 occurrence(s) on the page |
