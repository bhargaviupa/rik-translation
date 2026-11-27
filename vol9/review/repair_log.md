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
