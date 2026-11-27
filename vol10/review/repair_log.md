- 2026-11-18: tools/rv/refs_apply.py: reference names made uniform by the one list (rv/references.tsv), numbers untouched: en deva 26, en latin 1247, en latin-twin 26; every change is a row of review/refs_applied.tsv.
- 2026-11-18: numeral_drop_q_same.py (Nov 18 alignment Vol10_file_vs_md_Nov18.xlsx, files 1-7 merged): [?] dropped on 15 numerals (18 tokens) whose digits equal the aligned file row; log numerals/numeral_drop_q_same_Nov18.applied.tsv.
- 2026-11-18: numeral_apply_different.py --min-ctx=0.8 --min-score=0.85 (alignment of Nov 18): 1 token changed to the file's value (md line 4829 Ṛ. Saṃ. 10-63-15 -> 10-63-16; the remark quoting the print is left); read all 27 rows of equal part count, distance < 4 and context >= 0.8: most of them joined different references (e.g. Ni. 2-17 vs file 2-02, Tai. Saṃ. 6-2-2 vs 6-27-53), so the extra score threshold was added; a further row (6-2-2 -> 6-2-7) skipped by the guard against one md numeral paired with several file values; log numerals/numeral_apply_different_Nov18.applied.tsv.
- 2026-11-18: list for the user, nothing applied: numerals/Vol10_for_user_Nov18.tsv (359 DIFFERENT file rows not applied with the reason, 29 md numerals still [?] with no aligned file row and the closest unmatched file rows; 562 NOT FOUND file rows are only in the sheet 'file rows vs md' of Vol10_file_vs_md_Nov18.xlsx).

- **Nov 18 2026, labelled glosses of quoted passages replaced by the marker `**GLOSS**`** (user, Nov 17 2026, requirement B3.5; gloss session, `docs/GLOSS_PROMPT.md` step 1): 0 by `tools/rv/gloss_marker.py 10 --write`, 2 in single odd forms by a hand list through `gloss_marker.py --list` (exact text, found once in its line); removed text in `review/glosses_removed.tsv`; 5 labelled lines left in `review/glosses_left.tsv` (remarks and "Sense …" renderings, not glosses of a quotation). Checked: every change read before and after (2 of 2); by script: markers added = log rows, brackets, quotation marks and italics balanced. Damaged: 0.

### 2026-11-27 second pass, batch e300-309.tsv
| page | old → new | why |
|---|---|---|
| 302 | `नित्वादाद्युदात्तत्वम् [?]` → `णिदित्यनुवृत्तेरुपधावृद्धिः` | SECOND-PASS Q1: Kannada p. 302 reads ಣಿದಿತ್ಯನುವೃತ್ತೇರುಪಧಾವೃದ್ಧಿಃ (and p. 306 grammar repeats the sense: ṇit continues, vṛddhi of the upadhā); English text replaced, mark droppe |
| 302 | `nitvādādyudāttatvam [?]` → `ṇidityanuvṛtterupadhāvṛddhiḥ` | SECOND-PASS Q1: Kannada p. 302 reads ಣಿದಿತ್ಯನುವೃತ್ತೇರುಪಧಾವೃದ್ಧಿಃ (and p. 306 grammar repeats the sense: ṇit continues, vṛddhi of the upadhā); English text replaced, mark droppe |
| 302 | `आस्येन [?] आस्येत्यन्तिकनाम आसन्नमित्यादि` → `समीपे । आसेत्यंतिकनाम आसांबरमिति` | SECOND-PASS Q1: Kannada p. 302 reads ಯಸ್ಯಾಗ್ನೇರಾಸಯಾಸಮೀಪೇ । ಆಸೇತ್ಯಂತಿಕನಾಮ ಆಸಾಂಬರಮಿತಿ; p. 305 ಆಸಯಾ—ಸಮೀಪೇ |
| 302 | `āsyena [?] āsyetyantikanāma āsannamityādi` → `samīpe | āsetyaṃtikanāma āsāṃbaramiti` | SECOND-PASS Q1: Kannada p. 302 reads ಯಸ್ಯಾಗ್ನೇರಾಸಯಾಸಮೀಪೇ । ಆಸೇತ್ಯಂತಿಕನಾಮ ಆಸಾಂಬರಮಿತಿ; p. 305 ಆಸಯಾ—ಸಮೀಪೇ |
| 302 | `darśanādatithimiva sarvadā āgantāraṃ vā` → `darśāditithimapekṣyāgaṃtāraṃ vā` | SECOND-PASS S13: Kannada p. 302 reads ದರ್ಶಾದಿತಿಥಿಮಪೇಕ್ಷ್ಯಾಗಂತಾರಂ (ನಾ; vā kept from English); p. 304 quotes the same words |
| 302 | `उपसर्गव्यत्य [?]…` → `उपसर्गवशा…` | SECOND-PASS Q1: Kannada p. 302 ends ಉಪಸರ್ಗವಶಾ-, p. 303 continues ದ್ಯೋಗ್ಯಕ್ರಿಯಾಧ್ಯಾಹಾರಃ |
| 302 | `upasargavyatya [?]…` → `upasargavaśā…` | SECOND-PASS Q1: Kannada p. 302 ends ಉಪಸರ್ಗವಶಾ-, p. 303 continues ದ್ಯೋಗ್ಯಕ್ರಿಯಾಧ್ಯಾಹಾರಃ |
| 303 | `किंच वया नेतारः [?] ऋत्विजो` → `किंच वयो नेतार ऋत्विजो` | SECOND-PASS Q1: Kannada p. 303 reads ಕಿಂಚ ವಯೋ ನೇತಾರ ಋತ್ವಿಜೋಽಪಿ |
| 303 | `kiṃca vayā netāraḥ [?] ṛtvijo` → `kiṃca vayo netāra ṛtvijo` | SECOND-PASS Q1: Kannada p. 303 reads ಕಿಂಚ ವಯೋ ನೇತಾರ ಋತ್ವಿಜೋಽಪಿ |
| 303 | `वीति वा गुणः । [?]` → `विचि वा गुणः ।` | SECOND-PASS Q1: Kannada p. 303 reads ವಿಚಿ ವಾ ಗುಣಃ; p. 307 gives ವಿಚ್ ಪ್ರತ್ಯಯ |
| 303 | `vīti vā guṇaḥ | [?]` → `vici vā guṇaḥ |` | SECOND-PASS Q1: Kannada p. 303 reads ವಿಚಿ ವಾ ಗುಣಃ; p. 307 gives ವಿಚ್ ಪ್ರತ್ಯಯ |
| 304 | `*gayaḥ kṛtiḥ*` → `*gayaḥ kṛttiḥ*` | SECOND-PASS S13: Kannada p. 304 reads ಗಯಃ ಕೃತ್ತಿಃ |
| 304 | `new moon and other dates` → `the full moon and other dates` | SECOND-PASS S14: Kannada p. 304 reads ಪೂರ್ಣಮಾಸ್ಯವೇ ಮೊದಲಾದ ತಿಥಿಗಳನ್ನು (full moon); p. 305 ಪೂರ್ಣಮೆಯೇ |
| 304 | `*damūnā ity etad gṛhanāma etad vā yasya manasi mameti saḥ damūnāḥ` → `*dama ityetat gṛhanāma etat yasya manasi mamedamiti saḥ damūnāḥ` | SECOND-PASS S13: Kannada p. 304 reads ದಮ ಇತ್ಯೇತತ್ ಗೃಹನಾಮ ಏತತ್ ಯಸ್ಯ ಮನಸಿ ಮಮೇದಮಿತಿ ಸಃ ದಮೂನಾಃ |
| 304 | `(Ṛ. Saṃ. 7-1-[?] [?], as printed` → `(Ṛ. Saṃ. 5-4-5, as printed` | SECOND-PASS Q1: Kannada p. 304 reads (ಋ. ಸಂ. ೫-೪-೫) |
| 305 | `*gṛhān abhi abhimukhena āsa atitho bhavati*` → `*gṛhān abhi abhimukhyena asau atito bhavati*` | SECOND-PASS S13: Kannada p. 305 reads ಗೃಹಾನ್ ಅಭಿ ಅಭಿಮುಖ್ಯೇನ ಅಸೌ ಅತಿತೋ ಭವತಿ |
| 305 | `*annaṃ vājaḥ*` → `*andhaḥ vājaḥ*` | SECOND-PASS S13: Kannada p. 305 reads ಅಂಧಃ ವಾಜಃ |
| 305 | `(Ṛ. Saṃ. 1-116-17 [?], as printed` → `(Ṛ. Saṃ. 7-69-4, as printed` | SECOND-PASS Q1: Kannada p. 305 reads (ಋ. ಸಂ. ೭-೬೯-೪) |
| 300 | ` *asyativaktikhyātibhyo 'ṅ* (Pā. Sū. 3-1-52) gives` → ` *asyativaktikhyātibhyo 'ṅ* gives` | SECOND-PASS S3: Kannada p. 301 gives no sūtra number here; number removed |
| 300 | `(Pā. Sū. 8-1-71)` → `(Pā. Sū. 8-2-71)` | SECOND-PASS S1: Kannada p. 301 reads (ಪಾ. ಸೂ. ೮-೨-೭೧) |
| 306 | `(Pā. Sū. 7-2-117)` → `` | SECOND-PASS S3: Kannada p. 306 gives no sūtra number after ತದ್ಧಿತೇಷ್ವಚಾಮಾದೇಃ; number removed |
| 306 | `Uṇ. 4-?]` → `Pā. Sū. 4-6-60]` | SECOND-PASS S3: Kannada p. 306 reads (ಪಾ. ಸೂ. ೪-೬-೬೦) |
| 301 | `Adhyāya 1, Varga 14.)` → `Adhyāya 1, Varga 13.)` | SECOND-PASS S1: Kannada running head p. 301 reads ವ. ೧೩ |
| 303 | `Adhyāya 1, Varga 14.)` → `Adhyāya 1, Varga 13.)` | SECOND-PASS S1: Kannada running head p. 303 reads ವ. ೧೩ |
| 305 | `Adhyāya 1, Varga 14.)` → `Adhyāya 1, Varga 13.)` | SECOND-PASS S1: Kannada running head p. 305 reads ವ. ೧೩ |
| 309 | `Adhyāya 1, Varga 14.)` → `Adhyāya 1, Varga 13.)` | SECOND-PASS S1: Kannada running head p. 309 reads ವ. ೧೩ |
| 307 | `Adhyāya 1, Varga 14.)` → `Adhyāya 1, Varga 17.)` | SECOND-PASS S1: Kannada running head p. 307 reads ವ. ೧೭ (applied as printed; listed in open.tsv) |
| 308 | `saherlaukikādikaḥ [?] kanin` → `saherauṇādikaḥ kanin` | SECOND-PASS Q1: Kannada p. 307/308 reads ಸಹೇರೌಣಾದಿಕಃ ಕನಿನ್ |
| 308 | `तदर्थं यज्ञानामृत्विग्भिरुत्पद्यसे [?] । यद्वा` → `तदर्थं । यज्ञनामैतत् । यद्वा` | SECOND-PASS Q1: Kannada p. 308 reads ತದರ್ಥಂ । ಯಜ್ಞನಾಮೈತತ್ । ಯದ್ವಾ |
| 308 | `tadarthaṃ yajñānāmṛtvigbhirutpadyase [?] | yadvā` → `tadarthaṃ | yajñanāmaitat | yadvā` | SECOND-PASS Q1: Kannada p. 308 reads ತದರ್ಥಂ । ಯಜ್ಞನಾಮೈತತ್ । ಯದ್ವಾ |
| 308 | `for that, by the priests of the sacrifices you are produced [?]; or else` → `for that purpose (this is a name of sacrifice); or else` | SECOND-PASS Q1: Kannada p. 308 ತದರ್ಥಂ । ಯಜ್ಞನಾಮೈತತ್; p. 309 devatātā = yajña |
| 309 | `(Ṛ. Saṃ. 10-[?]-6;` → `(Ṛ. Saṃ. 10-50-6;` | SECOND-PASS Q1: Kannada p. 309 reads (ಋ. ಸಂ. ೧೦-೫೦-೬) |
| 309 | `(Ṛ. Saṃ. 2-[?]-2;` → `(Ṛ. Saṃ. 7-38-2;` | SECOND-PASS Q1: Kannada p. 309 reads (ಋ. ಸಂ. ೭-೩೮-೨) |
| 309 | `(Ni. 1-[?])` → `(Ni. 2-24)` | SECOND-PASS Q1: Kannada p. 309 reads ಉದಕನಾಮಗಳಲ್ಲಿಯೂ(ನಿ. ೨-೨೪) |
| 309 | `(Ni. 2-10 [?];` → `(Ni. 3-9;` | SECOND-PASS Q1: Kannada p. 309 reads ಧನನಾಮಗಳಲ್ಲಿಯೂ(ನಿ. ೩-೯) |
| 309 | `"material is evident for the sake of sacrifice"` → `"material has been created for the sake of sacrifice"` | SECOND-PASS S14: Kannada p. 309 reads ಯಜ್ಞಕ್ಕಾಗಿಯೇ ದ್ರವ್ಯವು ಸೃಷ್ಟವಾಗಿರುವುದು |

### 2026-11-27 second pass, batch e300-309_2.tsv
| page | old → new | why |
|---|---|---|
| 302 | `दर्शनादतिथिमिव सर्वदा आगन्तारं` → `दर्शादितिथिमपेक्ष्यागंतारं` | SECOND-PASS S13: Kannada p. 302 reads ದರ್ಶಾದಿತಿಥಿಮಪೇಕ್ಷ್ಯಾಗಂತಾರಂ (ನಾ; the English vā kept); p. 304 quotes the same words |
| 308 | `सहेर्लौकिकादिकः [?]` → `सहेरौणादिकः` | SECOND-PASS Q1: Kannada p. 307 reads ಸಹೇರೌಣಾದಿಕಃ ಕನಿನ್ |

### 2026-11-27 second pass, batch e2-31.tsv
| page | old → new | why |
|---|---|---|
| 2 | `1-116-7; 4-26-1` → `1-116-7; 1-117-6; 1-126-3; 4-26-1` | SECOND-PASS S3: Kannada p.2 lists ೧-೧೧೬-೭; ೧-೧೧೭-೬; ೧-೧೨೬-೩; ೪-೨೬-೧ (two references missing in English) |
| 2 | `the strap that is tied to a draught animal` → `the rope with which a horse is tied` | SECOND-PASS S14: Kannada p.2 ಕುದುರೆಯನ್ನು ಕಟ್ಟುವ ಹಗ್ಗ (rope for tying a horse) |
| 8 | `(Ṛ. Saṃ. 1-122-1.)` → `(Ṛ. Saṃ. 1-12-1.)` | SECOND-PASS S2: Kannada p.8 (ಋ. ಸಂ. ೧-೧೨-೧); numbers from the Kannada as printed |
| 14 | `(Pā. Sū. 7-1-39; the OCR prints the same` → `(Pā. Sū. 3-1-39; the OCR prints the same` | SECOND-PASS S2: Kannada p.14 supāṃ sulug (ಪಾ. ಸೂ. ೩-೧-೩೯) |
| 18 | `Ṛ. Saṃ. 5-32-1` → `Ṛ. Saṃ. 5-3-1` | SECOND-PASS S2: Kannada p.18 (ಋ. ಸಂ. ೫-೩-೧) |
| 25 | `2-3-4-35` → `2-3-4-25` | SECOND-PASS S2: Kannada p.25 (ಶ. ಬ್ರಾ. ೨-೩-೪-೨೫) |
| 27 | `(Pā. Sū. 7-1-39; the OCR prints 6-1-36)` → `(Pā. Sū. 7-1-36; the OCR prints 6-1-36)` | SECOND-PASS S2: Kannada p.27 vyat dual: ಪಾ. ಸೂ. ೭-೧-೩೬ |
| 27 | `7-2-117 as read` → `7-2-112 as read` | SECOND-PASS S2: Kannada p.27 ಪಾ. ಸೂ. ೭-೨-೧೧೨ (taddhiteṣv acām ādeḥ) |
| 27 | `(Pā. Sū. 6-3-5)` → `(Pā. Sū. 6-3-75)` | SECOND-PASS S2: Kannada p.27 ನಭ್ರಾಣ್ನಪಾತ್ (ಪಾ. ಸೂ. ೬-೩-೭೫) |
| 29 | `Sūktas 39–40 of the tenth Maṇḍala` → `Sūktas 29-40 and 41 of the tenth Maṇḍala` | SECOND-PASS S2: Kannada p.29 ಹತ್ತನೇ ಮಂಡಲದಲ್ಲಿ ೨೯-೪೦ ಮತ್ತು ೪೧ನೇ ಸೂಕ್ತಗಳ; applied as printed, listed in open.tsv |
| 31 | `(Pā. Sū. 6-1-193)` → `(Pā. Sū. 7-1-193)` | SECOND-PASS S2: Kannada p.31 (ಪಾ. ಸೂ. ೭-೧-೧೯೩) |
| 9 | `भ्रीणन्ति [?] ।` → `भ्रीणन्ति ।` | SECOND-PASS Q1: Kannada p.9 reads ಭ್ರೀಣಂತಿ ।, agrees with English; mark dropped |
| 9 | `bhrīṇanti [?] |` → `bhrīṇanti |` | SECOND-PASS Q1: Kannada p.9 reads ಭ್ರೀಣಂತಿ ।, agrees with English; mark dropped |
| 30 | `अतस्थी [?] महतीं` → `अतस्थे महतीं` | SECOND-PASS Q1: Kannada p.30 reads ಅತಸ್ಥೇ ಮಹತೀಂ ಚಿಂತಾಂ |
| 30 | `atasthī [?] mahatīṃ` → `atasthe mahatīṃ` | SECOND-PASS Q1: Kannada p.30 reads ಅತಸ್ಥೇ ಮಹತೀಂ ಚಿಂತಾಂ |
| 30 | `प्राप्स्या [?] मुधा` → `प्राप्ता मुधा` | SECOND-PASS Q1: Kannada p.30 reads ಜರಾಂ ಪ್ರಾಪ್ತಾ ಮುಧಾ |
| 30 | `prāpsyā [?] mudhā` → `prāptā mudhā` | SECOND-PASS Q1: Kannada p.30 reads ಜರಾಂ ಪ್ರಾಪ್ತಾ ಮುಧಾ |

### 2026-11-27 second pass, batch e32-61.tsv
| page | old → new | why |
|---|---|---|
| 33 | `Ṛ. Saṃ. 2-28-4, as read` → `Ṛ. Saṃ. 2-25-4, as read` | SECOND-PASS S2: Kannada p.33 (ಋ. ಸಂ. ೨-೨೫-೪) |
| 34 | `in the vocative dual, by *supāṃ sulug…* (Pā. Sū. 7-1-39) the *ā*` → `in the vocative dual, by *supāṃ sulug…* the *ā*` | SECOND-PASS S3: Kannada p.34 gives no sūtra number there (number removed) |
| 37 | `the cows and chariots given in great numbers` → `the horses and chariots given in great numbers` | SECOND-PASS S14: Kannada p.37 ಅಶ್ವಗಳೂ, ರಥಗಳೂ (horses and chariots) |
| 37 | `(Pā. Sū. 2-4-75) *śluḥ*` → `(Pā. Sū. 2-4-226) *śluḥ*` | SECOND-PASS S2: Kannada p.37 (ಪಾ. ಸೂ. ೨-೪-೨೨೬) applied as printed; listed in open.tsv |
| 41 | `*Sanemu* — the root` → `*Sanema* — the root` | SECOND-PASS S13: Kannada p.41 ಸನೇಮ |
| 41 | `*suvīraḥ …vīravīryau ca*, the final-first-member accent` → `*suvīraḥ …vīravīryau ca* (Pā. Sū. 6-2-120), the acute on the first syllable of the latter ` | SECOND-PASS S3: Kannada p.41 (ಪಾ. ಸೂ. ೬-೨-೧೨೦) ಉತ್ತರಪದ ಆದ್ಯುದಾತ್ತ |
| 41 | `in the Chandas by *chandasīraḥ…* the *m*` → `in the Chandas by *chandasīraḥ…* (Pā. Sū. 8-2-15) the *m*` | SECOND-PASS S3: Kannada p.41 (ಪಾ. ಸೂ. ೮-೨-೧೫) |
| 41 | `since *matup* is *pit*, the *ī* of the *ini*-suffix is unaccented` → `since *matup* and *ṅīp* are *pit* (unaccented), the *i* of the *ini*-suffix is acute` | SECOND-PASS S15: Kannada p.41 ಮತುಪ್ ಜೀಪ್ ಪಿತ್ತಾದುದರಿಂದ ಅನುದಾತ್ತವಾಗುವುದರಿಂದ ಇನಿ ಪ್ರತ್ಯಯದ ಇಕಾರವು ಉದಾತ್ತವಾಗುತ್ತದೆ |
| 41 | `*aśvāḥ asya santi* — *matup*;` → `*aśvāḥ asya santi* — *matup* (Pā. Sū. 5-2-98);` | SECOND-PASS S3: Kannada p.41 (ಪಾ. ಸೂ. ೫-೨-೯೮) |
| 41 | `*mādupadhāyāś ca matorvo 'yavādibhyaḥ*;` → `*mādupadhāyāś ca matorvo 'yavādibhyaḥ* (Pā. Sū. 8-2-9);` | SECOND-PASS S3: Kannada p.41 (ಪಾ. ಸೂ. ೮-೨-೯) |
| 41 | `by *mantre somāśvendriya…* the` → `by *mantre somāśvendriya…* (Pā. Sū. 6-3-131) the` | SECOND-PASS S3: Kannada p.41 (ಪಾ. ಸೂ. ೬-೩-೧೩೧) |
| 43 | `by *devatādvandve ca* the *ānaṅ*` → `by *devatādvandve ca* (Pā. Sū. 6-3-26) the *ānaṅ*` | SECOND-PASS S3: Kannada p.43 (ಪಾ. ಸೂ. ೬-೩-೨೬) |
| 43 | `by *āmantritasya ca* the *nighāta*` → `by *āmantritasya ca* (Pā. Sū. 8-1-19) the *nighāta*` | SECOND-PASS S3: Kannada p.43 (ಪಾ. ಸೂ. ೮-೧-೧೯) |
| 43 | `*satsūdviṣadruhaduha…* the suffix` → `*satsūdviṣadruhaduha…* (Pā. Sū. 3-2-61) the suffix` | SECOND-PASS S3: Kannada p.43 (ಪಾ. ಸೂ. ೩-೨-೬೧) |
| 43 | `by *vā druhamuha…* the` → `by *vā druhamuha…* (Pā. Sū. 3-2-61, as printed) the` | SECOND-PASS S3: Kannada p.43 prints ೩-೨-೬೧ here too, applied as printed |
| 43 | `by *ekāco baśo bhaṣ…* the` → `by *ekāco baśo bhaṣ…* (Pā. Sū. 8-2-32) the` | SECOND-PASS S3: Kannada p.43 (ಪಾ. ಸೂ. ೮-೨-೩೨) |
| 43 | `*gatikārakopapadāt kṛt* the accent` → `*gatikārakopapadāt kṛt* (Pā. Sū. 6-2-139) the accent` | SECOND-PASS S3: Kannada p.43 (ಪಾ. ಸೂ. ೬-೨-೧೩೯) |
| 44 | `*Apaḥ* — *ūḍidaṃpadādi…*:` → `*Apaḥ* — *ūḍidaṃpadādi…* (Pā. Sū. 6-1-171):` | SECOND-PASS S3: Kannada p.44 (ಪಾ.ಸೂ. ೬-೧-೧೭೧) |
| 44 | `since the word *yajña* [or *yat*] stands in connection` → `since the word *yat* stands in connection` | SECOND-PASS S13: Kannada p.44 ಯಚ್ಛಬ್ದ ಸಂಬಂಧವಿರುವುದರಿಂದ |
| 44 | `*chandasi luṅlaṅliṭaḥ* the *liṭ*` → `*chandasi luṅlaṅliṭaḥ* (Pā. Sū. 3-4-6) the *liṭ*` | SECOND-PASS S3: Kannada p.44 (ಪಾ. ಸೂ. ೩-೪-೬) |
| 44 | `by *liti* the acute for the vowel` → `by *liti* (Pā. Sū. 6-1-193) the acute for the vowel` | SECOND-PASS S3: Kannada p.44 (ಪಾ. ಸೂ. ೬-೧-೧೯೩) |
| 44 | `*vyatyayo bahulam*: the neuter` → `*vyatyayo bahulam* (Pā. Sū. 3-1-84): the neuter` | SECOND-PASS S3: Kannada p.44 (ಪಾ. ಸೂ. ೩-೧-೮೪) |
| 44 | `*anyeṣām api dṛśyate* the lengthening` → `*anyeṣām api dṛśyate* (Pā. Sū. 6-3-137) the lengthening` | SECOND-PASS S3: Kannada p.44 (ಪಾ ಸೂ. ೬-೩-೧೩೭) |
| 46 | `(Ṛ. Saṃ. 1-150-4, as printed` → `(Ṛ. Saṃ. 1-150-3, as printed` | SECOND-PASS S2: Kannada p.46 (ಋ. ಸಂ. ೧-೧೫೦-೩) |
| 46 | `*bāḷha* means *vṛddha* ("strong")` → `*bāḷha* means *dṛḍha* ("firm")` | SECOND-PASS S14: Kannada p.46 ಬಾಳ್ಹೆನೆಂದರೆ ದೃಢವೆಂದರ್ಥ |
| 46 | `This epithet is also found for gods.` → `This epithet is rarely found for gods.` | SECOND-PASS S14: Kannada p.46 ದೇವತೆಗಳ ಪರವಾಗಿ ಈ ವಿಶೇಷಣವಿರುವುದು ಅಪರೂಪ |
| 46 | `dhṛḍhe, sthirakarme* ("firm, of steady action")` → `dhṛḍhe, sthairye* ("firm, steadiness")` | SECOND-PASS S13: Kannada p.46 ಧೃಢೇ, ಸ್ಥೈರ್ಯೇ ಎಂದು ಅರ್ಥ (IAST by sp_sanskrit) |
| 47 | `*vṛṣādīnāṃ ca* — the initial acute` → `*vṛṣādīnāṃ ca* (Pā. Sū. 6-1-203) — the initial acute` | SECOND-PASS S3: Kannada p.47 (ಪಾ. ಸೂ. ೬-೧-೨೦೩) |
| 47 | `*anyebhyo 'pi dṛśyate* the suffix *vic*` → `*anyebhyo 'pi dṛśyate* (Pā. Sū. 3-2-75) the suffix *vic*` | SECOND-PASS S3: Kannada p.47 (ಪಾ. ಸೂ. ೩-೨-೭೫) |
| 47 | `by *niṣṭhā*; *tṛtīyā karmaṇi* —` → `by *niṣṭhā* (Pā. Sū. 3-2-102); *tṛtīyā karmaṇi* (Pā. Sū. 6-2-48) —` | SECOND-PASS S3: Kannada p.47 (ಪಾ. ಸೂ. ೩-೨-೧೦೨), (ಪಾ. ಸೂ. ೬-೨-೪೮) |
| 47 | `*sāvekācas tṛtīyādiḥ…* — the ending takes the acute. *Gūrtaśravāḥ*` → `*sāvekācas tṛtīyādiḥ…* (Pā. Sū. 6-1-168) — the ending takes the acute. *Gūrtaśravāḥ*` | SECOND-PASS S3: Kannada p.47 (ಪಾ. ಸೂ. ೬-೧-೧೬೮) |
| 47 | `*bahuvrīhau prakṛtyā pūrvapadam* — the accent of the first member. *Visṛṣṭarātiḥ*` → `*bahuvrīhau prakṛtyā pūrvapadam* (Pā. Sū. 6-2-1) — the accent of the first member. *Visṛṣṭ` | SECOND-PASS S3: Kannada p.47 (ಪಾ. ಸೂ. ೬-೨-೧) |
| 47 | `*vraścabhrasja…* — *ṣatva*` → `*vraścabhrasja…* (Pā. Sū. 8-2-36) — *ṣatva*` | SECOND-PASS S3: Kannada p.47 (ಪಾ. ಸೂ. ೮-೨-೩೬) |
| 47 | `*gatir anantaraḥ* — the prefix` → `*gatir anantaraḥ* (Pā. Sū. 6-2-49) — the prefix` | SECOND-PASS S3: Kannada p.47 (ಪಾ. ಸೂ. ೬-೨-೪೯) |
| 48 | `*bahuvrīhau prakṛtyā pūrvapadam*: the accent of the first member. *Yāti*` → `*bahuvrīhau prakṛtyā pūrvapadam* (Pā. Sū. 6-2-1): the accent of the first member. *Yāti*` | SECOND-PASS S3: Kannada p.48 (ಪಾ. ಸೂ. ೬-೨-೧) |
| 48 | `*anyebhyo 'pi dṛśyate* the suffix *kvanip*` → `*anyebhyo 'pi dṛśyate* (Pā. Sū. 3-2-75) the suffix *kvanip*` | SECOND-PASS S3: Kannada p.48 (ಪಾ. ಸೂ. ೩-೨-೭೫) |
| 48 | `by *hrasvasya piti kṛti tuk* the` → `by *hrasvasya piti kṛti tuk* (Pā. Sū. 6-1-71) the` | SECOND-PASS S3: Kannada p.48 (ಪಾ. ಸೂ. ೬-೧-೭೧) |
| 48 | `*gatikārakopapadāt kṛt*: the accent` → `*gatikārakopapadāt kṛt* (Pā. Sū. 6-2-139): the accent` | SECOND-PASS S3: Kannada p.48 (ಪಾ. ಸೂ. ೬-೨-೧೩೯) |
| 48 | `*khari ca* the *d*` → `*khari ca* (Pā. Sū. 8-4-55) the *d*` | SECOND-PASS S3: Kannada p.48 (ಪಾ. ಸೂ. ೮-೪-೫೫) |
| 48 | `because it has one syllable, *sāvekācas tṛtīyādiḥ…* the ending` → `because it has one syllable, *sāvekācas tṛtīyādiḥ…* (Pā. Sū. 6-1-168) the ending` | SECOND-PASS S3: Kannada p.48 (ಪಾ ಸೂ. ೬-೧-೧೬೮) |
| 51 | `cannot be explained as it ought to be, as the sacrificing *yajamāna* who is said to be fed` → `cannot be said with certainty to refer to the sacrificing *yajamāna*` | SECOND-PASS S14: Kannada p.51 ಯಜ್ಞ ಮಾಡುವ ಯಜಮಾನನಿಗೆ ಅನ್ವಯಿಸುವುದೆಂದು ನಿಷ್ಕೃಷ್ಟವಾಗಿ ಹೇಳಲು ಸಾಧ್ಯವಿಲ್ಲ |
| 51 | `*chandasi luṅlaṅliṭaḥ* — *laṅ*` → `*chandasi luṅlaṅliṭaḥ* (Pā. Sū. 3-4-6) — *laṅ*` | SECOND-PASS S3: Kannada p.51 (ಪಾ. ಸೂ. ೩-೪-೬) |
| 51 | `by *vyatyayo bahulam* the suffix *jhi*` → `by *vyatyayo bahulam* (Pā. Sū. 3-1-85) the suffix *jhi*` | SECOND-PASS S3: Kannada p.51 (ಪಾ. ಸೂ. ೩-೧-೮೫) |
| 51 | `*sārvadhātukam apit* — since` → `*sārvadhātukam apit* (Pā. Sū. 1-2-4) — since` | SECOND-PASS S3: Kannada p.51 (ಪಾ. ಸೂ. ೧-೨-೪) |
| 51 | `*gamahanajana…* the loss` → `*gamahanajana…* (Pā. Sū. 6-4-98) the loss` | SECOND-PASS S3: Kannada p.51 (ಪಾ ಸೂ. ೬-೪-೯೮) |
| 51 | `*jhoṃtaḥ* — the *ant*` → `*jhoṃtaḥ* (Pā. Sū. 7-1-3) — the *ant*` | SECOND-PASS S3: Kannada p.51 (ಪಾ. ಸೂ. ೭-೧-೩) |
| 51 | `*bahulaṃ chandasy amāṅyoge 'pi* — the augment` → `*bahulaṃ chandasy amāṅyoge 'pi* (Pā. Sū. 6-4-75) — the augment` | SECOND-PASS S3: Kannada p.51 (ಪಾ. ಸೂ. ೬-೪-೭೫) |
| 51 | `*nipātair yad yady…* the *nighāta*` → `*nipātair yad yady…* (Pā. Sū. 8-1-30) the *nighāta*` | SECOND-PASS S3: Kannada p.51 (ಪಾ. ಸೂ. ೮-೧-೩೦) |
| 51 | `*bhāve 'nupasargasya* the suffix *ap*` → `*bhāve 'nupasargasya* (Pā. Sū. 3-3-75) the suffix *ap*` | SECOND-PASS S3: Kannada p.51 (ಪಾ. ಸೂ. ೩-೩-೭೫) |
| 51 | `*dvyaco 'tastiṅaḥ* — in the Saṃhitā` → `*dvyaco 'tastiṅaḥ* (Pā. Sū. 6-3-135) — in the Saṃhitā` | SECOND-PASS S3: Kannada p.51 (ಪಾ. ಸೂ. ೬-೩-೧೩೫) |
| 51 | `*āmantritasya ca* the *nighāta*` → `*āmantritasya ca* (Pā. Sū. 8-1-19) the *nighāta*` | SECOND-PASS S3: Kannada p.51 (ಪಾ. ಸೂ. ೮-೧-೧೯) |
| 52 | `*ñño jaramarami…* — the initial acute` → `*naño jaramaramitramṛtāḥ* (Pā. Sū. 6-2-116) — the initial acute` | SECOND-PASS S13: Kannada p.52 ನಞೋ ಜರಮರಮಿತ್ರಮೃತಾಃ (ಪಾ. ಸೂ. ೬-೨-೧೧೬); IAST by sp_sanskrit |
| 52 | `by *striyāṃ ktin* the suffix` → `by *striyāṃ ktin* (Pā. Sū. 3-3-94) the suffix` | SECOND-PASS S3: Kannada p.52 (ಪಾ. ಸೂ. ೩-೩-೯೪) |
| 52 | `*tādau ca niti* the prefix` → `*tādau ca niti* (Pā. Sū. 6-2-50) the prefix` | SECOND-PASS S3: Kannada p.52 (ಪಾ. ಸೂ. ೬-೨-೫೦) |
| 54 | `*rāran* — delighting; (*teṣu* — in those)` → `*rāran* — offer; (*teṣu* — in those)` | SECOND-PASS S14: Kannada p.54 ರಾರನ್—ಅರ್ಪಿಸುತ್ತಾರೋ |
| 55 | `as "*daśayaḥ* — dwelling [in the ten]"` → `as "*daśavāraḥ* — ten times"` | SECOND-PASS S14: Kannada p.55 ದಶತಯೋ ದಶವಾರಃ ಹತ್ತಾವರ್ತಿ |
| 55 | `*mahaṃ rekṇaḥ*` → `*maghaṃ rekṇaḥ*` | SECOND-PASS S13: Kannada p.55 ಮಘಂ ರೇಕ್ಣಃ |
| 55 | `*daśatayasya dhāseḥ dāśendriyatṛptisādhanatvena` → `*daśatayasya dhāseḥ daśendriyatṛptisādhanatvena` | SECOND-PASS S13: Kannada p.55 ದಶೇಂದ್ರಿಯತೃಪ್ತಿಸಾಧನತ್ವೇನ |
| 56 | `*chandasi luṅlaṅliṭaḥ* — *loṭ*-sense` → `*chandasi luṅlaṅliṭaḥ* (Pā. Sū. 3-4-6) — *loṭ*-sense` | SECOND-PASS S3: Kannada p.56 (ಪಾ. ಸೂ. ೩-೪-೬) |
| 56 | `*gātisthāghupābhūbhyaḥ sicaḥ parasmaipadeṣu* — its` → `*gātisthāghupābhūbhyaḥ sicaḥ parasmaipadeṣu* (Pā. Sū. 2-4-77) — its` | SECOND-PASS S3: Kannada p.56 (ಪಾ. ಸೂ. ೨-೪-೭೭) |
| 56 | `*bahulaṃ chandasy amāṅyoge 'pi* — the *aṭ*` → `*bahulaṃ chandasy amāṅyoge 'pi* (Pā. Sū. 6-4-75) — the *aṭ*` | SECOND-PASS S3: Kannada p.56 (ಪಾ. ಸೂ. ೬-೪-೭೫) |
| 56 | `*asyativakti khyātibhyo 'ṅ* — the *aṅ*` → `*asyativakti khyātibhyo 'ṅ* (Pā. Sū. 3-1-52) — the *aṅ*` | SECOND-PASS S3: Kannada p.56 (ಪಾ. ಸೂ. ೩-೧-೫೨) |
| 56 | `*vaca um* — …` → `*vaca um* (Pā. Sū. 7-4-20) — …` | SECOND-PASS S3: Kannada p.56 end (ಪಾ. ಸೂ. ೭-೪-೨೦) |
| 57 | `by *mider guṇaḥ* [as printed in part] guṇa` → `by *midacoṃtyātparaḥ* it comes after the last vowel; guṇa` | SECOND-PASS S13: Kannada p.57 ಮಿದಚೋಂತ್ಯಾತ್ಪರಃ—ಅಂತ್ಯಾಚಿನ ಪರವಾಗಿ ಬರುತ್ತದೆ. ಗುಣ (IAST by sp_sanskrit) |
| 57 | `since it is *pit*, the suffix *ini*-like is unaccented` → `since it is *pit*, it is unaccented` | SECOND-PASS S16: Kannada p.57 ಪಿತ್ತಾದುದರಿಂದ ಇದು ಅನುದಾತ್ತವಾಗುತ್ತದೆ |
| 57 | `*saṅkhyāyā avayave tayap* the suffix` → `*saṅkhyāyā avayave tayap* (Pā. Sū. 5-2-42) the suffix` | SECOND-PASS S3: Kannada p.57 (ಪಾ. ಸೂ. ೫-೨-೪೨) |
| 57 | `by *striyāṃ ktin* the suffix *ktin*; by *vyatyaya*` → `by *striyāṃ ktin* (Pā. Sū. 3-3-94) the suffix *ktin*; by *vyatyaya*` | SECOND-PASS S3: Kannada p.57 (ಪಾ. ಸೂ. ೩-೩-೯೪) |
| 57 | `*marutvṛdhādīnāṃ chandasy upasaṅkhyānam* —` → `*marutvṛdhādīnāṃ chandasy upasaṅkhyānam* (Pā. Sū. 6-2-102-2) —` | SECOND-PASS S3: Kannada p.57 (ಪಾ. ಸೂ. ೬-೨-೧೦೨-೨) |
| 57 | `by *liti* the first-member acute` → `by *liti* (Pā. Sū. 6-1-193) the first-member acute` | SECOND-PASS S3: Kannada p.57 (ಪಾ. ಸೂ. ೬-೧-೧೯೩) |
| 57 | `*dhātor ekāco halādeḥ kriyāsamabhihāre yaṅ* the suffix` → `*dhātor ekāco halādeḥ kriyāsamabhihāre yaṅ* (Pā. Sū. 3-1-22) the suffix` | SECOND-PASS S3: Kannada p.57 (ಪಾ. ಸೂ. ೩-೧-೨೨) |
| 57 | `*yaṅo 'ci ca* the *luk*` → `*yaṅo 'ci ca* (Pā. Sū. 2-4-74) the *luk*` | SECOND-PASS S3: Kannada p.57 (ಪಾ. ಸೂ. ೨-೪-೭೪) |
| 57 | `*dīrgha iṇkitaḥ* — the lengthening` → `*dīrgha iṇkitaḥ* (Pā. Sū. 7-4-83) — the lengthening` | SECOND-PASS S3: Kannada p.57 (ಪಾ. ಸೂ. ೭-೪-೮೩) |
| 57 | `*yadvṛttānnityam* — the *nighāta*` → `*yadvṛttānnityam* (Pā. Sū. 8-1-66) — the *nighāta*` | SECOND-PASS S3: Kannada p.57 (ಪಾ. ಸೂ. ೮-೧-೬೬) |
| 57 | `*chandasy ubhayathā* — since` → `*chandasy ubhayathā* (Pā. Sū. 3-4-117) — since` | SECOND-PASS S3: Kannada p.57 (ಪಾ. ಸೂ. ೩-೪-೧೧೭) |
| 57 | `*ato lopa iṭi ca* the loss` → `*ato lopa iṭi ca* (Pā. Sū. 6-4-64) the loss` | SECOND-PASS S3: Kannada p.57 (ಪಾ. ಸೂ. ೬-೪-೬೪) |
| 57 | `*abhyastānām ādiḥ* the first-syllable acute does not arise` → `*abhyastānām ādiḥ* (Pā. Sū. 6-1-189) the first-syllable acute does not arise` | SECOND-PASS S3: Kannada p.57 (ಪಾ. ಸೂ. ೬-೧-೧೮೯) |
| 60 | `*idito num dhātoḥ* the *num*` → `*idito num dhātoḥ* (Pā. Sū. 7-1-58) the *num*` | SECOND-PASS S3: Kannada p.60 (ಪಾ. ಸೂ. ೭-೧-೫೮) |
| 60 | `*ato dīrgho yañi* — lengthening` → `*ato dīrgho yañi* (Pā. Sū. 7-3-101) — lengthening` | SECOND-PASS S3: Kannada p.60 (ಪಾ. ಸೂ. ೭-೩-೧೦೧) |
| 60 | `by *tāsyanudāttet…* the` → `by *tāsyanudāttet…* (Pā. Sū. 6-1-186) the` | SECOND-PASS S3: Kannada p.60 (ಪಾ. ಸೂ. ೬-೧-೧೮೬) |
| 60 | `*bhṛñām it* — *i* in` → `*bhṛñām it* (Pā. Sū. 7-4-76) — *i* in` | SECOND-PASS S3: Kannada p.60 (ಪಾ. ಸೂ. ೭-೪-೭೬) |
| 60 | `*abhyastānām ādiḥ* — the first-syllable acute.` → `*abhyastānām ādiḥ* (Pā. Sū. 6-1-189) — the first-syllable acute.` | SECOND-PASS S3: Kannada p.60 (ಪಾ. ಸೂ. ೬-೧-೧೮೯) |
| 60 | `*iṇo yaṇ* — *yaṇ* for the root` → `*iṇo yaṇ* (Pā. Sū. 6-4-81) — *yaṇ* for the root` | SECOND-PASS S3: Kannada p.60 (ಪಾ. ಸೂ. ೬-೪-೮೧) |
| 60 | `since *yvoḥ…* the *nighāta* does not arise` → `since there is connection with *yat*, the *nighāta* does not arise` | SECOND-PASS S13: Kannada p.60 ಯದ್ಯೋಗವಿರುವುದರಿಂದ ನಿಘಾತಸ್ವರ ಬರುವುದಿಲ್ಲ |
| 60 | `*śeś chandasi bahulam* the *śi* is dropped` → `*śeś chandasi bahulam* (Pā. Sū. 6-1-70) the *śi* is dropped` | SECOND-PASS S3: Kannada p.60 (ಪಾ. ಸೂ. ೬-೧-೭೦) |
| 61 | `*bahuvrīhau prakṛtyā pūrvapadam*: the accent` → `*bahuvrīhau prakṛtyā pūrvapadam* (Pā. Sū. 6-2-1): the accent` | SECOND-PASS S3: Kannada p.61 (ಪಾ. ಸೂ. ೬-೨-೧) |
| 61 | `*ājjaser asuk* the augment` → `*ājjaser asuk* (Pā. Sū. 7-1-50) the augment` | SECOND-PASS S3: Kannada p.61 (ಪಾ. ಸೂ. ೭-೧-೫೦) |
| 61 | `*ñnityādir nityam* — the initial` → `*ñnityādir nityam* (Pā. Sū. 6-1-197) — the initial` | SECOND-PASS S3: Kannada p.61 (ಪಾ. ಸೂ. ೬-೧-೧೯೭) |

### 2026-11-27 second pass, batch e62-91.tsv
| page | old → new | why |
|---|---|---|
| 63 | `recorded among the hundred names of water (Ni. 2-23, as read` → `recorded among the hundred and one names of water (Ni. 2-24, as read` | SECOND-PASS S2: Kannada p.63 ನೂರೊಂದು ಉದಕನಾಮಗಳಲ್ಲಿ (ನಿ. ೨-೨೪): hundred and one; Ni. 2-24 |
| 65 | `(Ṛ. Saṃ. 1-79-4.)` → `(Ṛ. Saṃ. 1-29-4.)` | SECOND-PASS S1: Kannada p.65 (ಋ. ಸಂ. ೧-೨೯-೪) |
| 65 | `*bahuvrīhau prakṛtyā pūrvapadam*: the accent` → `*bahuvrīhau prakṛtyā pūrvapadam* (Pā. Sū. 6-2-1): the accent` | SECOND-PASS S3: Kannada p.65 (ಪಾ. ಸೂ. ೬-೨-೧) |
| 65 | `*ñnityādir nityam* — the initial acute` → `*ñnityādir nityam* (Pā. Sū. 6-1-197) — the initial acute` | SECOND-PASS S3: Kannada p.65 (ಪಾ. ಸೂ. ೬-೧-೧೯೭) |
| 65 | `*namovarivaścitrāṅaḥ kyac* the suffix` → `*namovarivaścitrāṅaḥ kyac* (Pā. Sū. 3-1-19) the suffix` | SECOND-PASS S3: Kannada p.65 (ಪಾ. ಸೂ. ೩-೧-೧೯) |
| 65 | `*āryaḥ svāmivaiśyayoḥ* — the suffix` → `*āryaḥ svāmivaiśyayoḥ* (Pā. Sū. 3-1-103) — the suffix` | SECOND-PASS S3: Kannada p.65 (ಪಾ. ಸೂ. ೩-೧-೧೦೩) |
| 66 | `*kvasuś ca* the suffix` → `*kvasuś ca* (Pā. Sū. 3-2-107) the suffix` | SECOND-PASS S3: Kannada p.66 (ಪಾ. ಸೂ. ೩-೨-೧೦೭) |
| 66 | `*kuhoś cuḥ* the *j*` → `*kuhoś cuḥ* (Pā. Sū. 7-4-62) the *j*` | SECOND-PASS S3: Kannada p.66 (ಪಾ. ಸೂ. ೭-೪-೬೨) |
| 66 | `*vasoḥ saṃprasāraṇam* — *saṃprasāraṇa*` → `*vasoḥ saṃprasāraṇam* (Pā. Sū. 6-4-131) — *saṃprasāraṇa*` | SECOND-PASS S3: Kannada p.66 (ಪಾ. ಸೂ. ೬-೪-೧೩೧) |
| 66 | `*śāsivasighasīnāṃ ca* — *ṣatva*` → `*śāsivasighasīnāṃ ca* (Pā. Sū. 8-3-60) — *ṣatva*` | SECOND-PASS S3: Kannada p.66 (ಪಾ. ಸೂ. ೮-೩-೬೦) |
| 66 | `*vyatyayo bahulam* — in *loṭ*` → `*vyatyayo bahulam* (Pā. Sū. 3-1-85) — in *loṭ*` | SECOND-PASS S3: Kannada p.66 (ಪಾ. ಸೂ. ೩-೧-೮೫) |
| 66 | `*tujādīnāṃ dīrgho 'bhyāsasya* the lengthening` → `*tujādīnāṃ dīrgho 'bhyāsasya* (Pā. Sū. 6-1-7) the lengthening` | SECOND-PASS S3: Kannada p.66 (ಪಾ. ಸೂ. ೬-೧-೭) |
| 66 | `*dhātor ekācaḥ…*, *yaṅ* comes` → `*dhātor ekācaḥ…* (Pā. Sū. 3-1-22), *yaṅ* comes` | SECOND-PASS S3: Kannada p.66 (ಪಾ. ಸೂ. ೩-೧-೨೨) |
| 66 | `*nugator anunāsikād…* — the *nuk*` → `*nugator anunāsikād…* (Pā. Sū. 7-4-85) — the *nuk*` | SECOND-PASS S3: Kannada p.66 (ಪಾ. ಸೂ. ೭-೪-೮೫) |
| 66 | `*dīrgha iṇkitaḥ* — the lengthening` → `*dīrgha iṇkitaḥ* (Pā. Sū. 7-4-83) — the lengthening` | SECOND-PASS S3: Kannada p.66 (ಪಾ. ಸೂ. ೭-೪-೮೩) |
| 66 | `*supāṃ sulug…* the substitute` → `*supāṃ sulug…* (Pā. Sū. 7-1-39) the substitute` | SECOND-PASS S3: Kannada p.66 (ಪಾ. ಸೂ ೭-೧-೩೯) |
| 66 | `when the genitive (locative) ending follows` → `when the genitive ending follows` | SECOND-PASS S16: Kannada p.66 ಷಷ್ಠಿ ವಿಭಕ್ತಿ ಪರವಾದಾಗ; no locative |
| 67 | `*śiśvaḥ* — the immature;` → `*śiśvaḥ* — the ignorant;` | SECOND-PASS S14: Kannada p.67 ಶಿಶ್ವಃ—ಅಜ್ಞಾನಿಗಳಾದ (ignorant) |
| 67 | `the four immature sons` → `the four ignorant sons` | SECOND-PASS S14: Kannada p.67 ಭಾವಾರ್ಥ ನಾಲ್ಕು ಅಜ್ಞಾನಿಗಳಾದ ಮಕ್ಕಳೂ |
| 68 | `is *Murmurāra*, *Nāpusasa*;` → `is *Marmaśāra*, *Nāhuṣa*;` | SECOND-PASS S13: Kannada p.68 ಮರ್ಮಶಾರನೆಂಬುವನೇ ನಾಹುಷನೆಂಬುವನೆಂದು (sp_sanskrit: marmaśāra, nāhuṣa) |
| 68 | `recorded among the fifteen names of form` → `recorded among the sixteen names of form` | SECOND-PASS S1: Kannada p.68 ಹದಿನಾರು ರೂಪನಾಮಗಳಲ್ಲಿ |
| 68 | `(Ṛ. Saṃ. 1-122-15.) Mitra and Varuṇa, [we pray]` → `Mitra and Varuṇa, [we pray]` | SECOND-PASS S2: Kannada p.68 gives no reference after this sentence (number removed) |
| 68 | `(Ṛ. Saṃ. 5-62-8.)` → `(Ṛ. Saṃ. 5-6-8.)` | SECOND-PASS S1: Kannada p.68 (ಋ. ಸಂ. ೫-೬-೮) |
| 69 | `*gatikārakopapadāt kṛt* — the accent` → `*gatikārakopapadāt kṛt* (Pā. Sū. 6-2-139) — the accent` | SECOND-PASS S3: Kannada p.69 (ಪಾ. ಸೂ. ೬-೨-೧೩೯) |
| 69 | `*kṅiti ca* — guṇa is prohibited` → `*kṅiti ca* (Pā. Sū. 1-1-5) — guṇa is prohibited` | SECOND-PASS S3: Kannada p.69 (ಪಾ. ಸೂ. ೧-೧-೫) |
| 69 | `and *supāṃ sulug…* — *ā* for it` → `and *supāṃ sulug…* (Pā. Sū. 7-1-39) — *ā* for it` | SECOND-PASS S3: Kannada p.69 (ಪಾ. ಸೂ. ೭-೧-೩೯) |
| 69 | `*āmantritasya ca* — the *nighāta*` → `*āmantritasya ca* (Pā. Sū. 8-1-19) — the *nighāta*` | SECOND-PASS S3: Kannada p.69 (ಪಾ. ಸೂ. ೮-೧-೧೯) |
| 69 | `*bahuvrīhau prakṛtyā pūrvapadam* — the accent` → `*bahuvrīhau prakṛtyā pūrvapadam* (Pā. Sū. 6-2-1) — the accent` | SECOND-PASS S3: Kannada p.69 (ಪಾ. ಸೂ. ೬-೨-೧) |
| 69 | `*chandasi luṅlaṅliṭaḥ* — *luṅ*` → `*chandasi luṅlaṅliṭaḥ* (Pā. Sū. 3-4-6) — *luṅ*` | SECOND-PASS S3: Kannada p.69 (ಪಾ. ಸೂ. ೩-೪-೬) |
| 69 | `*dyudbhyo luṅi* — it becomes` → `*dyudbhyo luṅi* (Pā. Sū. 1-3-91) — it becomes` | SECOND-PASS S3: Kannada p.69 (ಪಾ. ಸೂ. ೧-೩-೯೧) |
| 69 | `*sici vṛddhiḥ parasmaipadeṣu* — *vṛddhi*` → `*sici vṛddhiḥ parasmaipadeṣu* (Pā. Sū. 7-2-1) — *vṛddhi*` | SECOND-PASS S3: Kannada p.69 (ಪಾ. ಸೂ. ೭-೨-೧) |
| 70 | `*ato vṛddhir luki hali* — *vṛddhi* for the *u*` → `*ato vṛddhir luki hali* (Pā. Sū. 7-3-89) — *vṛddhi* for the *u*` | SECOND-PASS S3: Kannada p.70 ಉತೋ ವೃದ್ಧಿರ್ಲುಕಿ ಹಲಿ (ಪಾ. ಸೂ. ೭-೩-೮೯) |
| 70 | `by *tiṅ atiṅaḥ* the *nighāta*` → `by *tiṅ atiṅaḥ* (Pā. Sū. 8-1-28) the *nighāta*` | SECOND-PASS S3: Kannada p.70 (ಪಾ. ಸೂ. ೮-೧-೨೮) |
| 70 | `92nd Sūkta (15 ṛks [?])` → `92nd Sūkta (15 ṛks)` | SECOND-PASS Q1: Kannada p.70 ೯೨ ನೇ ಸೂಕ್ತ (೧೫ ಋಕ್ಕುಗಳು) |
| 71 | `1-92-14; 4-52-6; 1-79-4; 5-74-10; 8-47-14` → `1-92-14; 4-52-6; 5-79-4; 5-79-10; 8-47-14` | SECOND-PASS S1: Kannada p.71 ೫-೭೯-೪; ೫-೭೯-೧೦ |
| 72 | `2-41-18; 4-25-9; 6-61-3` → `2-41-18; 4-55-9; 6-61-3` | SECOND-PASS S1: Kannada p.72 ೪-೫೫-೯ |
| 72 | `only in Ṛ. Saṃ. 1-123-4 and 5, and 1-123-4 [as printed twice` → `only in Ṛ. Saṃ. 1-123-4 and Ṛ. Saṃ. 1-123-4 [as printed twice` | SECOND-PASS S1: Kannada p.72 ೧-೧೨೩-೪ ಮತ್ತು ೧-೧೨೩-೪ (no "and 5") |
| 72 | `stray digit]; 10-75-8.` → `stray digit]; 10-75-6.` | SECOND-PASS S1: Kannada p.72 ೧೦-೭೫-೬ |
| 72 | `Ṛ. Saṃ. 3-5-11; 4-52-2` → `Ṛ. Saṃ. 3-55-11; 4-52-2` | SECOND-PASS S1: Kannada p.72 ೩-೫೫-೧೧ |
| 72 | `also Ṛ. Saṃ. 1-92-13; 1-22-3` → `also Ṛ. Saṃ. 1-92-14; 1-22-3` | SECOND-PASS S1: Kannada p.72 ೧-೯೨-೧೪ |
| 73 | `section *ahoṣasyaḥ*` → `section *athoṣasyaḥ*` | SECOND-PASS S13: Kannada p.73 ಅಥೋಷಸ್ಯಃ (sp_sanskrit: athoṣasyaḥ) |
| 73 | `*pṛthū ratha iti sūkte pratyṛcam ityādi*` → `*pṛthū ratha iti sūkte pratyarcir ity aṣṭau*` | SECOND-PASS S7: Kannada p.73 ಪೃಥೂ ರಥ ಇತಿ ಸೂಕ್ತೇ ಪ್ರತ್ಯರ್ಚಿರಿತ್ಯಷ್ಟೌ (sp_sanskrit: pṛthū ratha iti sūkte pratyarcirityaṣṭau) |
| 76 | `*mahat, brahman* [as read]` → `*mahat, bradhnaḥ* [as read]` | SECOND-PASS S13: Kannada p.76 ಮಹತ್ ಬ್ರಧ್ನಃ (sp_sanskrit: mahat bradhnaḥ) |
| 77 | `(Ṛ. Saṃ. 7-78-1, as printed; the middle digit 8 and last digit 1 read from a 900-dpi zoom,` → `(Ṛ. Saṃ. 7-68-1.)` | SECOND-PASS S1: Kannada p.77 (ಋ. ಸಂ. ೭-೬೮-೧) |
| 78 | `*aruṇo gāva uṣasaḥ*` → `*āruṇyo gāva uṣasaḥ*` | SECOND-PASS S7: Kannada p.78 ಆರುಣ್ಯೋ ಗಾವ ಉಷಸಃ (sp_sanskrit: āruṇyo gāva uṣasaḥ) |
| 78 | `*ciṇ bhāvakarmaṇoḥ* — *ciṇ*` → `*ciṇ bhāvakarmaṇoḥ* (Pā. Sū. 3-1-66) — *ciṇ*` | SECOND-PASS S3: Kannada p.78 (ಪಾ. ಸೂ. ೩-೧-೬೬) |
| 78 | `by *ciṇo luk* (*ciṇo luk*, as printed)` → `by *ciṇo luk* (Pā. Sū. 6-4-104) (*ciṇo luk*, as printed)` | SECOND-PASS S3: Kannada p.78 ಚಿಣೋಲುಕ್ (ಪಾ. ಸೂ. ೬-೪-೧೦೪) |
| 78 | `when *jas* follows, *ājjaser asuk*. *Amṛtāsaḥ*` → `when *jas* follows, *ājjaser asuk* (Pā. Sū. 7-1-50). *Amṛtāsaḥ*` | SECOND-PASS S3: Kannada p.78 (ಪಾ. ಸೂ. ೭-೧-೫೦) |
| 78 | `*ñño jaramarami…* the final acute` → `*nañjarāmara…* (Pā. Sū. 6-2-116) the final acute` | SECOND-PASS S7: Kannada p.78 ನಞ್ಜರಾಮರ (ಪಾ. ಸೂ. ೬-೨-೧೧೬) (sp_sanskrit: nañjarāmara) |
| 78 | `and by *gātisthāghupābhūbhyaḥ sicaḥ* the *luk*` → `and by *gātisthāghupābhūbhyaḥ sicaḥ* (Pā. Sū. 2-4-77) the *luk*` | SECOND-PASS S3: Kannada p.78 (ಪಾ. ಸೂ. ೨-೪-೭೭) |
| 78 | `*ātaḥ* the substitute *jus*` → `*ātaḥ* (Pā. Sū. 3-4-110) the substitute *jus*` | SECOND-PASS S3: Kannada p.78 ಆತಃ (ಪಾ. ಸೂ. ೩-೪-೧೧೦) |
| 78 | `*usyapadāntāt* the *pararūpa*` → `*usyapadāntāt* (Pā. Sū. 6-1-96) the *pararūpa*` | SECOND-PASS S3: Kannada p.78 (ಪಾ. ಸೂ. ೬-೧-೯೬) |
| 78 | `(by the sūtra *kiter vyādhipratīkāre*) the suffix` → `(by the sūtra *kiter vyādhipratīkāre*, Pā. Sū. 3-1-5-3) the suffix` | SECOND-PASS S3: Kannada p.78 (ಪಾ. ಸೂ. ೩-೧-೫-೩) applied as printed; listed in open.tsv |
| 81 | `and as the name of a king (Ni. 11-17)` → `and as the name of a king (Ni. 11-16)` | SECOND-PASS S1: Kannada p.81 (ನಿ. ೧೧-೧೬) |
| 81 | `"oblations" or "water" (Ni. 1-27)` → `"oblations" or "water" (Ni. 11-27)` | SECOND-PASS S1: Kannada p.81 (ನಿ. ೧೧-೨೭) |
| 82 | `(Ṛ. Saṃ. 1-92-10, as read.)` → `(Ṛ. Saṃ. 1-92-1, as read.)` | SECOND-PASS S1: Kannada p.82 (ಋ. ಸಂ. ೧-೯೨-೧) |
| 82 | `*dīpajana…budhapūriṭāyi…* — *ciṇ*` → `*dīpajana…budhapūriṭāyi…* (Pā. Sū. 3-1-61) — *ciṇ*` | SECOND-PASS S3: Kannada p.82 (ಪಾ. ಸೂ. ೩-೧-೬೧) |
| 83 | `*ciṇo luk* — the loss of the following *ta*` → `*ciṇo luk* (Pā. Sū. 6-4-104) — the loss of the following *ta*` | SECOND-PASS S3: Kannada p.83 (ಪಾ. ಸೂ. ೬-೪-೧೦೪) |
| 83 | `*ugitaś ca* the suffix *ṅīp*; since it follows` → `*ugitaś ca* (Pā. Sū. 4-1-6) the suffix *ṅīp*; since it follows` | SECOND-PASS S3: Kannada p.83 (ಪಾ. ಸೂ. ೪-೧-೬) |
| 83 | `*chandasi luṅlaṅliṭaḥ* — *luṅ* in the sense of the present; *asyativaktikhyātibhyo 'ṅ* — *` → `*chandasi luṅlaṅliṭaḥ* (Pā. Sū. 3-4-6) — *luṅ* in the sense of the present; *asyativaktikh` | SECOND-PASS S3: Kannada p.83 (ಪಾ. ಸೂ. ೩-೪-೬), (ಪಾ. ಸೂ. ೩-೧-೫೨) |
| 83 | `*ato lopa iṭi ca* — the loss` → `*ato lopa iṭi ca* (Pā. Sū. 6-4-64) — the loss` | SECOND-PASS S3: Kannada p.83 (ಪಾ. ಸೂ. ೬-೪-೬೪) |
| 83 | `*yūnas tiḥ* the suffix *ti*` → `*yūnas tiḥ* (Pā. Sū. 4-1-77) the suffix *ti*` | SECOND-PASS S3: Kannada p.83 (ಪಾ. ಸೂ. ೪-೧-೭೭) |
| 83 | `*striyāṃ ktin* the suffix *ktin*` → `*striyāṃ ktin* (Pā. Sū. 3-3-94) the suffix *ktin*` | SECOND-PASS S3: Kannada p.83 (ಪಾ. ಸೂ. ೩-೩-೯೪) |
| 83 | `*halaḥ* the lengthening` → `*halaḥ* (Pā. Sū. 6-4-2) the lengthening` | SECOND-PASS S3: Kannada p.83 (ಪಾ. ಸೂ. ೬-೪.೨) |
| 83 | `*tādau ca niti* — the accent` → `*tādau ca niti* (Pā. Sū. 6-2-50) — the accent` | SECOND-PASS S3: Kannada p.83 (ಪಾ. ಸೂ ೬-೨-೫೦) |
| 85 | `*damanamanāḥ* — one with a cruel/restrained mind [as printed]` → `*damanamanāḥ* — one who has no cruel mind` | SECOND-PASS S14: Kannada p.85 ದಮಮನಾಃ ಕ್ರೂರವಾದ ಮನಸ್ಸಿಲ್ಲದವನು |
| 89 | `देवी जोष्ट्री वसुधिती ययोरन्या घ[?]द्वेषांसि यायोवदन्या वक्ष[?]द्वसु ।` → `देवी जोष्ट्री वसुधीती ययोरन्याघाद्वेषांसि यूयावदन्यावक्षद्वसु ।` | SECOND-PASS Q1: Kannada p.89 ದೇವೀ ಜೋಷ್ಟ್ರೀ ವಸುಧೀತೀ ಯಯೋರನ್ಯಾಘಾದ್ವೇಷಾಂಸಿ ಯೂಯಾವದನ್ಯಾವಕ್ಷದ್ವಸು (Devanagari by sp_sanskrit; both [?] settled: ghā, vakṣad) |
| 89 | `devī joṣṭrī vasudhitī yayoranyā gh[?]dveṣāṃsi yāyovadanyā vakṣa[?]dvasu |` → `devī joṣṭrī vasudhītī yayoranyāghādveṣāṃsi yūyāvadanyāvakṣadvasu |` | SECOND-PASS Q1: Kannada p.89 ದೇವೀ ಜೋಷ್ಟ್ರೀ ವಸುಧೀತೀ ಯಯೋರನ್ಯಾಘಾದ್ವೇಷಾಂಸಿ ಯೂಯಾವದನ್ಯಾವಕ್ಷದ್ವಸು (IAST by sp_sanskrit) |
| 89 | `(Vā. Saṃ. 28-10. The first line` → `(Vā. Saṃ. 25-15. The first line` | SECOND-PASS S1: Kannada p.89 (ನಾ. ಸಂ. ೨೫-೧೫) |
| 89 | `(Yajus Saṃ. 8-18, as printed.)` → `(Yajus Saṃ. 8-15, as printed.)` | SECOND-PASS S1: Kannada p.89 (ಯ. ಪಾ. ಸಂ. ೮-೧೫) |
| 89 | `*sanvallaghuni…* (Pā. Sū. 7-4-79) *i* in` → `*sanyataḥ* (Pā. Sū. 7-4-29) *i* in` | SECOND-PASS S13: Kannada p.90 ಸನ್ಯತಃ(ಪಾ. ಸೂ. ೭-೪-೨೯) (sp_sanskrit: sanyataḥ) |
| 90 | `*śyas śyanor nityam* (Pā. Sū. 7-1-81; the first letter of each of the two words is medium)` → `*śyapśyanor nityam* (Pā. Sū. 3-1-81)` | SECOND-PASS S1: Kannada p.90 ಶ್ಯಪ್‌ಶ್ಯನೋರ್ನಿತ್ಯಂ (ಪಾ. ಸೂ. ೩-೧-೮೧) (sp_sanskrit: śyapśyanornityaṃ) |

### 2026-11-27 second pass, batch e92-121.tsv
| page | old → new | why |
|---|---|---|
| 93 | `Aṣṭaka 2, Adhyāya 1, Varga 5` → `Aṣṭaka 2, Adhyāya 1, Varga 4` | SECOND-PASS S1: Kannada p.93 head ವ. ೪ |
| 94 | `the root *jani prādurbhāve*` → `the root *janī prādurbhāve*` | SECOND-PASS S13: Kannada p.94 ಜನೀ ಪ್ರಾದುರ್ಭಾವೇ |
| 94 | `in the sense of the fifth case [*astāti*], the suffix *āti*` → `in the *astāti* [sense], the suffix *ati*` | SECOND-PASS S16: Kannada p.94 ಅಸ್ತಾತಿ ವಿಷಯದಲ್ಲಿ ಅತಿ ಪ್ರತ್ಯಯ; no fifth case |
| 94 | `the *tip*-like singular ending` → `the second-person singular ending` | SECOND-PASS S14: Kannada p.94 ಮಧ್ಯಮಪುರುಷ ಏಕವಚನ ಪ್ರತ್ಯಯ |
| 97 | `purandhirbahudhīstat[?]ḥ | purandhirbhagaḥ purastātsyā[?]deśa ityekam` → `purandhirbahudhīstatkaḥ | purandhirbhagaḥ purastāttasyānvādeśa ityekam` | SECOND-PASS Q1: Kannada p.97 same line; IAST twin |
| 98 | `(Ṛ. Saṃ. 10-65-13, as printed;` → `(Ṛ. Saṃ. 10-85-13, as printed;` | SECOND-PASS S2: Kannada p.98 (ಋ. ಸಂ. ೧೦-೮೫-೧೩) |
| 98 | `(Pā. Sū. 7-1-39 [as read: "7-3-39"])` → `(Pā. Sū. 7-3-39)` | SECOND-PASS S2: Kannada p.98 (ಪಾ. ಸೂ. ೭-೩-೩೯) |
| 99 | `*supāṃ sulug…*, the lengthening. ‖ 6 ‖` → `*supāṃ sulug…* (Pā. Sū. 7-3-39), the lengthening. ‖ 6 ‖` | SECOND-PASS S3: Kannada p.99 (ಪಾ. ಸೂ. ೭-೩-೩೯) |
| 101 | `the Dawn illumines them with her radiant chariot.` → `the Dawn illuminates them with her radiant chariot.` | SECOND-PASS S13: Kannada p.101 English Translation: "the Dawn illuminates them" |
| 103 | `*halṅyābbhyo dīrghāt…* the loss of the suffix` → `*halṅyābbhyo dīrghāt…* (Pā. Sū. 6-1-68) the loss of the suffix` | SECOND-PASS S3: Kannada p.103 (ಪಾ. ಸೂ. ೬-೧-೬೮) |
| 103 | `*ato vṛddhir luki hali* (Pā. Sū. 7-2-3 [as read]) *vṛddhi* of the *u*` → `*uto vṛddhir luki hali* (Pā. Sū. 7-3-89) *vṛddhi* of the *u*` | SECOND-PASS S2: Kannada p.103 ಉತೋ ವೃದ್ಧಿರ್ಲುಕಿ ಹಲಿ (ಪಾ. ಸೂ. ೭-೩-೮೯) |
| 103 | `the root *dya abhigamane*` → `the root *dyu abhigamane*` | SECOND-PASS S13: Kannada p.103 ದ್ಯು ಅಭಿಗಮನೇ ಧಾತು |
| 107 | `Aṣṭaka 2, Adhyāya 1, Varga 6` → `Aṣṭaka 2, Adhyāya 1, Varga 5` | SECOND-PASS S1: Kannada p.107 head ಅ. ೨. ಅ. ೧. ನ. ೫ (Varga 5) |
| 107 | `(Ṛ. Saṃ. 1-50-25, as read.)` → `(Ṛ. Saṃ. 1-50-5, as read.)` | SECOND-PASS S2: Kannada p.107 (ಋ. ಸಂ. ೧-೫೦-೫) |
| 107 | `"Varuṇa, Pāvaka, you who make the light of Jana (*janā anu bhuraṇyantam*) shine, remover o` → `"Varuṇa, Pāvaka, remover of darkness, maker of purity: you see the righteous people (*janā` | SECOND-PASS S14: Kannada p.107 ಜನಾ ಅನು ಭುರಣ್ಯಂತಂ ಪಶ್ಯಸಿ ... ನೀನು ಪುಣ್ಯವಂತರಾದ ಜನರನ್ನು ನೋಡುತ್ತೀಯೆ; no 'light of Jana' |
| 109 | `Aṣṭaka 2, Adhyāya 1, Varga 6` → `Aṣṭaka 2, Adhyāya 1, Varga 5` | SECOND-PASS S1: Kannada p.109 head ವ. ೫ |
| 112 | `*aharaha* — in the sense of constancy` → `*aharahaḥ* — in the sense of constancy` | SECOND-PASS S13: Kannada p.112 ಅಹರಹಃ |
| 113 | `वंतस्थानीयानि [?] नीलपीतादीनि` → `वंतस्थानीयानि नीलपीतादीनि` | SECOND-PASS Q2: Kannada p.113 ವಂತಸ್ಥಾನೀಯಾನಿ ನೀಲಪೀತಾದೀನಿ: no word between; mark only removed |
| 113 | `vaṃtasthānīyāni [?] nīlapītādīni` → `vaṃtasthānīyāni nīlapītādīni` | SECOND-PASS Q2: Kannada p.113 same; IAST twin |
| 114 | `*kai netavyā*` → `*kva netavyā*` | SECOND-PASS S7: Kannada p.114 ಕ್ವ ನೇತವ್ಯಾ |
| 115 | `Aṣṭaka 2, Adhyāya 1, Varga 6` → `Aṣṭaka 2, Adhyāya 1, Varga 5` | SECOND-PASS S1: Kannada p.115 head ನ. ೫ (Varga 5) |
| 115 | `*ato lopaḥ* (Pā. Sū. 6-4-48)` → `*ato lopaḥ* (Pā. Sū. 6-4-49)` | SECOND-PASS S2: Kannada p.116 ಅತೋಲೋಪಃ (ಪಾ. ಸೂ. ೬-೪-೪೯) |
| 115 | `*dīrgho 'kitaḥ* (Pā. Sū. 6-4-83)` → `*dīrgho 'kitaḥ* (Pā. Sū. 7-4-83)` | SECOND-PASS S2: Kannada p.116 ದೀರ್ಘೋಽಕಿತಃ (ಪಾ. ಸೂ. ೭-೪-೮೩) |
| 115 | `As a young woman makes manifest the parts of her body, her bosom and so on,` → `As a young woman makes manifest the parts of her body, her teeth and so on,` | SECOND-PASS S14: Kannada p.115 ಯುವತಿಯು ತನ್ನ ದಂತಾದಿಯಾದ ಶರೀರದ ಅವಯವಗಳನ್ನು |
| 117 | `*thāsaḥ se* (Pā. Sū. 3-4-80) gives` → `*thāsaḥ se* gives` | SECOND-PASS S16: Kannada p.117 ಧಾಸಃ ಸೇ has no sūtra number; number removed |
| 119 | `saścidinnaro [?] bhūritokā` → `saścidinnaro bhūritokā` | SECOND-PASS Q2: Kannada p.119 same; IAST twin |
| 121 | `दिनान्तरेष्वस्मा[?]यन्ति` → `दिनान्तरेष्वप्यायन्ति` | SECOND-PASS Q1: Kannada p.121 ದಿನಾಂತರೇಷ್ವಪ್ಯಾಯಂತಿ (apy āyanti) |
| 121 | `dināntareṣvasmā[?]yanti` → `dināntareṣvapyāyanti` | SECOND-PASS Q1: Kannada p.121 ದಿನಾಂತರೇಷ್ವಪ್ಯಾಯಂತಿ; IAST twin |
| 119 | `*kam* is also recorded among the names of happiness (Ni. 3-13)` → `*kam* is also recorded among the twenty names of happiness (Ni. 3-13)` | SECOND-PASS S3: Kannada p.119 ಇಪ್ಪತ್ತು ಸುಖನಾಮಗಳಲ್ಲಿ (ನಿ. ೩-೧೩) |
| 121 | `come again to us on later days` → `come again even on later days` | SECOND-PASS S14: Kannada p.121 ದಿನಾಂತರೇಷ್ವಪ್ಯಾಯಂತಿ (apy āyanti): no 'to us' |

### 2026-11-27 second pass, batch e92-121_2.tsv
| page | old → new | why |
|---|---|---|
| 97 | `पुरन्धिर्बहुधीस्तत्[?]ः । पुरन्धिर्भगः पुरस्तात्स्या[?]देश इत्येकम्` → `पुरंधिर्बहुधीस्तत्कः । पुरंधिर्भगः पुरस्तात्तस्यान्वादेश इत्येकं` | SECOND-PASS Q1: Kannada p.97 ಪುರಂಧಿರ್ಬಹುಧೀಸ್ತತ್ಕಃ ... ತಸ್ಯಾನ್ವಾದೇಶ ... ಇತ್ಯೇಕಂ (real reading); Deva made by sp_sanskrit |
| 114 | `| kaineyaṃ netavyeti vā |` → `| kveyaṃ netavyeti vā |` | SECOND-PASS S7: Kannada p.113/114 ಕ್ವೇಯಂ/ಕ್ವಯಂ ನೇತವ್ಯೇತಿ (kva iyam) |
| 115 | `| vantsthānīyāni nīlapītādīni rūpāṇi` → `| dantasthānīyāni nīlapītādīni rūpāṇi` | SECOND-PASS S7: Kannada p.115 ದನ್ತಸ್ಥಾನೀಯಾನಿ ನೀಲಪೀತಾದೀನಿ ರೂಪಾಣಿ |
| 119 | `saścidinnaro bhūritokā` → `saścidinnaro [?] bhūritokā` | SECOND-PASS Q2: mark restored: Kannada p.119 ನಿಷ್ಪಕ್ವಕ್ರಾಸಚ್ಚಿದಿನ್ನರೋ is a non-word, Devanagari mark cannot be removed; keep both |

### 2026-11-27 second pass, batch e122-151.tsv
| page | old → new | why |
|---|---|---|
| 124 | `8-1-259` → `8-1-59` | SECOND-PASS S2: Kannada p.124 ಚವಾ ಯೋಗೇ ಪ್ರಥಮಾ (ಪಾ. ಸೂ. ೮-೧-೫೯) |
| 126 | `***bhadraṃ bhadraṃ kratuṃ dehi*** [as printed; the bhāṣya reads *dhehi*]` → `***bhadraṃ bhadraṃ kratuṃ dhehi***` | SECOND-PASS S13: Kannada p.126 heading ಭದ್ರಂ ಭದ್ರಂ ಕ್ರತುಂ ಧೇಹಿ (dhehi, not dehi) |
| 127 | `Ṛ. Saṃ. 8-48-7, as I read the print "೮-೪೮-೨".` → `Ṛ. Saṃ. 8-45-7, as I read the print "೮-೪೮-೨".` | SECOND-PASS S1: Kannada p.127 (ಋ. ಸಂ. ೮-೪೫-೭) |
| 127 | `nityavīpsayoḥ* (Pā. Sū. 5-1-4)` → `nityavīpsayoḥ* (Pā. Sū. 8-1-4)` | SECOND-PASS S2: Kannada p.127 ನಿತ್ಯವೀಪ್ಸಯೋಃ (ಪಾ ಸೂ ೮-೧-೪) |
| 130 | `(ऋ. सं. ७-६३-४ [?])` → `(ऋ. सं. ७-६३-४)` | SECOND-PASS Q2: Kannada p.130 ಋ. ೭-೬೩-೪ agrees; mark removed unchanged |
| 130 | `(ṛ. saṃ. 7-63-4 [?])` → `(ṛ. saṃ. 7-63-4)` | SECOND-PASS Q2: Kannada p.130 ಋ. ೭-೬೩-೪ agrees; mark removed unchanged (IAST twin) |
| 132 | `Ṛ. Saṃ. 1-113-3, numerals` → `Ṛ. Saṃ. 1-113-6, numerals` | SECOND-PASS S1: Kannada p.132 (ಋ. ಸಂ. ೧-೧೧೩-೬) |
| 134 | `abhisṛṣṭā[?]nām` → `abhisṛṣṭānām` | SECOND-PASS Q1: Kannada p.134 ಅಭಿಸೃಷ್ಟಾನಾಮ (IAST twin) |
| 134 | `यच्[?]स्यत` → `यच्छस्यत` | SECOND-PASS Q1: Kannada p.134 ತದಾಹುರ್ಯಚ್ಛಸ್ಯತ (yacchasyata) |
| 134 | `yac[?]syata` → `yacchasyata` | SECOND-PASS Q1: Kannada p.134 ಯಚ್ಛಸ್ಯತ (IAST twin) |
| 135 | `loṭ, the second person singular [as printed "ಪ್ರಥಮಪುರುಷ" — third person singular] *tip*` → `loṭ, the third person (prathamapuruṣa) singular *tip*` | SECOND-PASS S14: Kannada p.135 ಪ್ರಥಮಪುರುಷ ಏಕವಚನದಲ್ಲಿ ತಿಪ್ |
| 136 | `the suffix *kyap* [print: "ಕ್ರಿನ್", i.e. *ktin*]` → `the suffix *ktin*` | SECOND-PASS S13: Kannada p.136 ಭಾವಾರ್ಥದಲ್ಲಿ ಕ್ತಿನ್ ಪ್ರತ್ಯಯ |
| 140 | `*devād yajñau* [print: "ದೇವಾದ್ಯಜ್ಞೌ", Pā. Sū. 4-1-85, as read by the OCR]` → `*devād yajñau* [print: "ದೇವಾದ್ಯಜ್ಞೌ", Pā. Sū. 4-1-45-3, as read by the OCR]` | SECOND-PASS S2: Kannada p.140 ದೇವಾದ್ಯಞಞ್ (ಪಾ. ಸೂ. ೪-೧-೪೫-೩) |
| 140 | `with it the augment *tuk*` → `with it the augment *suk*` | SECOND-PASS S13: Kannada p.140 ತತ್ಸಂನಿಯೋಗದಿಂದ ಸುಗಾಗಮ |
| 140 | `(Pā. Sū. 7-3-84)` → `(Pā. Sū. 7-3-89)` | SECOND-PASS S1: Kannada p.140 ಉತೋ ವೃದ್ಧಿರ್ಲುಕಿ ಹಲಿ (ಪಾ. ಸೂ. ೭-೩-೮೯) |
| 142 | `she does not obstruct the (affairs of living beings) of the quarters` → `she does not upset the (usage 'east' and so on) of the quarters` | SECOND-PASS S14: Kannada p.142 ದಿಕ್ಕುಗಳಿಗೆ(ಇರುವ ಪ್ರಾಗಾದಿವ್ಯವಹಾರವನ್ನು) ತಪ್ಪಿಸುವುದಿಲ್ಲ |
| 143 | `Ṛ. Saṃ. 1-225-8` → `Ṛ. Saṃ. 1-25-8` | SECOND-PASS S1: Kannada p.143 (ಋ. ಸಂ. ೧-೨೫-೮) |
| 143 | `एषा व[?]नी भवति` → `एषा व्येनी भवति` | SECOND-PASS Q1: Kannada p.143 ಏಷಾ ವ್ಯೇನೀ ಭವತಿ (vyenī) |
| 143 | `eṣā v[?]nī bhavati` → `eṣā vyenī bhavati` | SECOND-PASS Q1: Kannada p.143 ಏಷಾ ವ್ಯೇನೀ ಭವತಿ (IAST twin) |
| 148 | `Ṛ. Saṃ. 1-117-20, as read from the print` → `Ṛ. Saṃ. 10-39-7, as read from the print` | SECOND-PASS S2: Kannada p.148 (ಋ. ಸಂ. ೧೦-೩೯-೭), taken as printed |
| 150 | `(Ṛ. Saṃ. 7-83-3, as read from the print.)` → `(Ṛ. Saṃ. 7-83-7, as read from the print.)` | SECOND-PASS S1: Kannada p.150 (ಋ. ಸಂ. ೭-೮೩-೭) |
| 150 | `U. Sū. 3-300 as read` → `U. Sū. 3-200 as read` | SECOND-PASS S1: Kannada p.150 (ಉ. ಸೂ. ೩-೨೦೦) |
| 150 | `Pā. Sū. 6-4-77, vārttika` → `Pā. Sū. 6-4-77-1, vārttika` | SECOND-PASS S3: Kannada p.150 (ಪಾ. ಸೂ. ೬-೪-೭೭-೧) |

### 2026-11-27 second pass, batch e122-151_2.tsv
| page | old → new | why |
|---|---|---|
| 134 | `नामभिसृष्टा[?]नामग्निर्मुखं` → `नामभिसृष्टानामग्निर्मुखं` | SECOND-PASS Q1: Kannada p.134 ಧಾವಂತೀನಾಮಭಿಸೃಷ್ಟಾನಾಮಗ್ನಿರ್ಮುಖಂ (abhisṛṣṭānām); earlier try had the wrong sandhi context |

### 2026-11-27 second pass, batch e152-181.tsv
| page | old → new | why |
|---|---|---|
| 152 | ` meaningless' (Ni. 1-9)."` → ` meaningless'."` | SECOND-PASS S16: Kannada p.152 bhāṣya ends ಕಮೀಮಿದ್ವಿತೀತಿ ಯಾಸ್ಕೇನೋಕ್ತತ್ವಾತ್ with no Nirukta number; number the print has not is removed |
| 153 | `Varga 7.)` → `Varga 6.)` | SECOND-PASS S1: Kannada head ನ. ೬ (ವ. ೬) |
| 153 | `(Ṛ. Saṃ. 1-168-6, as read from the print;` → `(Ṛ. Saṃ. 1-18-6, as read from the print;` | SECOND-PASS S1: Kannada p.153 ಋ. ಸಂ. ೧-೧೮-೬ |
| 155 | `Varga 7.)` → `Varga 6.)` | SECOND-PASS S1: Kannada head ವ. ೬ |
| 157 | `Varga 7.)` → `Varga 6.)` | SECOND-PASS S1: Kannada head ಸ. ೬ (Varga 6) |
| 157 | `(Pā. Sū. 3-4-11)` → `(Pā. Sū. 3-1-11)` | SECOND-PASS S2: Kannada p.157 ದೃಶೇ ವಿಖ್ಯೇ ಚ (ಪಾ. ಸೂ. ೩-೧-೧೧) |
| 158 | `*sāvekācas tṛtīyādiḥ* (Pā. Sū. 6-1-168)` → `*sāvekācas tṛtīyādiḥ*` | SECOND-PASS S2: Kannada p.158 ಸಾವೇಕಾಚಸ್ತೃತೀಯಾದಿಃ has no sūtra number; number the print has not is removed |
| 158 | `(Pā. Sū. 6-1-173)` → `(Pā. Sū. 6-1-1-3)` | SECOND-PASS S1: Kannada p.158 ೬-೧-೧-೩ applied as printed (impossible form; open.tsv) |
| 159 | `Varga 8.)` → `Varga 6.)` | SECOND-PASS S1: Kannada head ವ, ೬ applied as printed |
| 159 | `लभते चेद्[?]ः संताड्य` → `लभते चेदक्षैः संताड्य` | SECOND-PASS Q1: Kannada p.159 ಲಭತೇ ಚೇದಕ್ಷೈಃ ಸಂತಾಡ್ಯ (real reading cedakṣaiḥ) |
| 159 | `labhate ced[?]ḥ saṃtāḍya` → `labhate cedakṣaiḥ saṃtāḍya` | SECOND-PASS Q1: Kannada p.159 ಚೇದಕ್ಷೈಃ (IAST twin) |
| 160 | `"Maṃ. 1 A. 18 Sū. 124".)` → `"Maṃ. 1 A. 18 Sū. 123".)` | SECOND-PASS S1: Kannada head ಸೂ. ೧೨೩ applied as printed (open.tsv) |
| 162 | `तत्राक्ष्यैराष्णन्ति [?] सा` → `तत्राक्षैराघ्नन्ति सा` | SECOND-PASS Q1: Kannada p.162 ತಾಂ ತತ್ರಾಕ್ಷೈರಾಘ್ನಂತಿ ಸಾ (akṣair āghnanti: real words, fits ದಾಳಿಗಳಿಂದ ಹೊಡೆದ); letters ಕ್ಷ್ಯೈರಾಷ್ಣ→ಕ್ಷೈರಾಘ್ನ |
| 162 | `tatrākṣyairāṣṇanti [?] sā` → `tatrākṣairāghnanti sā` | SECOND-PASS Q1: Kannada p.162 ತತ್ರಾಕ್ಷೈರಾಘ್ನಂತಿ (IAST twin) |
| 163 | `(Ni. 3-13, as printed "೩-೧೩")` → `(Ni. 3-15, as printed "೩-೧೫")` | SECOND-PASS S1: Kannada p.163 (ನಿ. ೩-೧೫) |
| 163 | `*ca*, Pā. Sū. 6-3-138)` → `*ca*, Pā. Sū. 6-2-138)` | SECOND-PASS S2: Kannada p.163 ಚೌ(ಪಾ. ಸೂ. ೬-೨-೧೩೮) |
| 164 | `(Pā. Sū. 6-1-173) gives it the acute` → `(Pā. Sū. 6-1-133) gives it the acute` | SECOND-PASS S2: Kannada p.164 ೬-೧-೧೩೩ applied as printed |
| 164 | `U. Sū. 3-160` → `U. Sū. 2-170` | SECOND-PASS S1: Kannada p.164 (ಉ. ಸೂ. ೨-೧೭೦) |
| 164 | `as printed "ಚಿತ್ವ"?]` → `as printed "ಜಿತ್ವ"]` | SECOND-PASS S13: Kannada p.164 reads ಜಿತ್ವ (twice, also in riṇīte) |
| 168 | `"Maṃ. 1 A. 18 Sū. 124".)` → `"Maṃ. 1 A. 18 Sū. 123".)` | SECOND-PASS S1: Kannada head ಸೂ. ೧೨೩ applied as printed (open.tsv) |
| 168 | `(U. Sū. 4-139 as read)` → `(U. Sū. 4-579)` | SECOND-PASS S1: Kannada p.168 (ಉ. ಸೂ. ೪-೫೭೯) |
| 171 | `(Ṛ. Saṃ. 3-30-19, as read` → `(Ṛ. Saṃ. 3-20-19, as read` | SECOND-PASS S1: Kannada p.171 ಋ. ಸಂ. ೩-೨೦-೧೯ |
| 172 | `plural following, *supāṃ sulug…* (Pā. Sū. 7-1-39) gives *śe*` → `plural following, *supāṃ sulug…* (Pā. Sū. 3-1-39) gives *śe*` | SECOND-PASS S2: Kannada p.172 ಸುಪಾಂಸುಲುಕ್ (ಪಾ. ಸೂ. ೩-೧-೩೯) under ಅಸ್ಮೇ |
| 172 | `*saṃprasāraṇāc ca* (Pā. Sū. 6-1-108)` → `*saṃprasāraṇāc ca*` | SECOND-PASS S2: Kannada p.172 ಸಂಪ್ರಸಾರಣಾಚ್ಚ has no sūtra number; number the print has not is removed |
| 172 | `ವಕ್ತವ್ಯಮ್"] gives the acute to *matup*` → `ವಕ್ತವ್ಯಮ್"] (Kā. 6-1-176-1) gives the acute to *matup*` | SECOND-PASS S3: Kannada p.172 (ಕಾ. ೬-೧-೧೭೬-೧) printed, English lacked it |
| 172 | `*pratnapūrvaviśvemāt thāl chandasi* [print: "ಪ್ರತ್ನ ಪುರಾಣೇ ಪ್ರಾತ್"] gives the suffix *tnap` → `*naśca purāṇe prāt* [print: "ನಶ್ಚ ಪುರಾಣೇ ಪ್ರಾತ್"] gives the suffix *tnap*` | SECOND-PASS S2: Kannada p.172 ನಶ್ಚ ಪುರಾಣೇ ಪ್ರಾತ್ (letters copied via sp_sanskrit); English had the sūtra of pratnathā from memory |
| 173 | `नि. २-१७ [?] ।` → `नि. २-१७ ।` | SECOND-PASS Q2: Kannada p.173 ನಿ. ೨-೧೭ agrees; mark removed unchanged |
| 173 | `ni. 2-17 [?] |` → `ni. 2-17 |` | SECOND-PASS Q2: Kannada p.173 ನಿ. ೨-೧೭ agrees; mark removed unchanged (IAST twin) |
| 173 | `says Yāska (Ni. [?]).` → `says Yāska (Ni. 2-17).` | SECOND-PASS Q1: Kannada p.173 ನಿ. ೨-೧೭ (the remark itself is not edited) |
| 176 | `*hetumati ca* (Pā. Sū. 3-1-226)` → `*hetumati ca* (Pā. Sū. 3-1-26)` | SECOND-PASS S1: Kannada p.176 ಹೇತುಮತಿ ಚ (ಪಾ. ಸೂ. ೩-೧-೨೬) |
| 176 | `*śvanyuvamaghonām* [print: "ಶ್ವನ್ನುಕ್ಷನ್", *vanisanyoh*?] (U. Sū. 1-157 as read)` → `*śvannukṣan* [print: "ಶ್ವನ್ನುಕ್ಷನ್"] (U. Sū. 1-157 as read)` | SECOND-PASS S13: Kannada p.176 ಶ್ವನ್ನುಕ್ಷನ್—(ಉ. ಸೂ. ೧-೧೫೭); the English had put the name of the other sūtra śvayuvamaghonām and a guess; letters from sp_sanskrit |
| 177 | `Varga 8.)` → `Varga 9.)` | SECOND-PASS S1: Kannada head ವ. ೯ |
| 179 | `Varga 8.)` → `Varga 9.)` | SECOND-PASS S1: Kannada head ವ. ೯ |
| 180 | `(Pā. Sū. 4-1-77, as printed "೪-೧-೭೭")` → `(Pā. Sū. 4-1-76, as printed "೪-೧-೭೬")` | SECOND-PASS S1: Kannada p.180 ಯೂನಸ್ತಿಃ(ಪಾ. ಸೂ. ೪-೧-೭೬) |
| 180 | `Uṇ. 4-?]` → `U. Sū. 4-457]` | SECOND-PASS S3: Kannada p.180 ಅನಿಹೃಷಿಭ್ಯಾಂ ಕಿಚ್ಚ (ಉ. ಸೂ. ೪-೪೫೭) |
| 180 | `(Pā. Sū. 1-3-25) [as printed]` → `(Pā. Sū. 1-3-25-1) [as printed]` | SECOND-PASS S1: Kannada p.180 ಉಪಾದ್ದೇವಪೂಜಾಸಂ (ಪಾ. ಸೂ. ೧-೩-೨೫-೧) |
| 181 | `Varga 8.)` → `Varga 9.)` | SECOND-PASS S1: Kannada head ವ. ೯ |
