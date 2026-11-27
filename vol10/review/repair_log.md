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

### 2026-11-27 second pass, batch e182-211.tsv
| page | old → new | why |
|---|---|---|
| 182 | `Ṛ. Saṃ. 1-103-7, as read from the print` → `Ṛ. Saṃ. 1-123-7, as read from the print` | SECOND-PASS S1: Kannada p.182 (ಋ. ಸಂ. ೧-೧೨೩-೭) |
| 183 | `(Ni. 3-9; print "೩-೧೩" or similar, not clear to me)` → `(Ni. 3-13)` | SECOND-PASS S1: Kannada p.183 (ನಿ. ೩-೧೩) |
| 183 | `(Ṛ. Saṃ. 10-63-16, as read from the print "೧೦-೬೩-೧೫".)` → `(Ṛ. Saṃ. 10-63-16.)` | SECOND-PASS S1: Kannada p.183 (ಋ. ಸಂ. ೧೦-೬೩-೧೬); the English remark that the print has 15 is wrong |
| 183 | `[as printed, Uṇ. 4-?]` → `(U. Sū. 4-500)` | SECOND-PASS S3: Kannada p.183 ವಹಿವಸ್ಯರ್ತಿಭ್ಯಶ್ಚಿತ್—(ಉ. ಸೂ. ೪-೫೦೦) |
| 183 | `*vāter ḍit* [print: "ವಾತೇರ್ಡಿತ್"] (U. Sū. 4-573 as read)` → `*vāterḍicca* (U. Sū. 4-573)` | SECOND-PASS S13: Kannada p.183 ವಾತೇರ್ಡಿಚ್ಚ—(ಉ. ಸೂ. ೪-೫೭೩); letters via sp_sanskrit |
| 183 | `*patapum* [print: "ಪತ ಪುಮ್", Pā. Sū. 7-4-19]` → `*pataḥ pum* (Pā. Sū. 7-4-19)` | SECOND-PASS S13: Kannada p.183 ಪತಃ ಪುಮ್—(ಪಾ. ಸೂ. ೭-೪-೧೯); letters via sp_sanskrit |
| 186 | `(Pā. Sū. 7-4-94)` → `(Pā. Sū. 7-4-49)` | SECOND-PASS S1: Kannada p.187 ದೀರ್ಘೋಲಘೋಃ(ಪಾ. ಸೂ. ೭-೪-೪೯) |
| 187 | `*grahijyāvayi…* (Pā. Sū. 6-1-16) gives` → `*grahijyāvayi…* gives` | SECOND-PASS S3: Kannada p.187 ಗ್ರಹಿಜ್ಯಾವಯಿ—ಎಂಬುದರಿಂದ prints no sūtra number; number the print has not is removed |
| 192 | `The queen, being old and ugly, was ashamed to cohabit with the ṛṣi, and` → `The queen, ashamed to cohabit with the old and ugly ṛṣi, and` | SECOND-PASS S15: Kannada p.192 ವೃದ್ಧನಾಗಿಯೂ ಕುರೂಪಿಯಾಗಿಯೂ ಇದ್ದ ಋಷಿಯೊಡನೆ: old and ugly is the ṛṣi, not the queen |
| 192 | `made her a ṛṣi's wife, purified her,` → `made her pure like a ṛṣi's daughter,` | SECOND-PASS S14: Kannada p.192 ಋಷಿಪುತ್ರಿಯಂತೆ ಶುದ್ಧಳನ್ನಾಗಿ ಮಾಡಿ |
| 193 | `वीड्वङ्गान्नै [?] चतुर्युजः` → `वीड्वङ्गान्वै चतुर्युजः` | SECOND-PASS Q1: Kannada p.193 ವೀಡ್ವಂಗಾನ್ವೈ ಚತುರ್ಯುಜಃ: vai (letters copied from the Kannada: ವೈ) |
| 193 | `vīḍvaṅgānnai [?] caturyujaḥ` → `vīḍvaṅgānvai caturyujaḥ` | SECOND-PASS Q1: Kannada p.193 ವೀಡ್ವಂಗಾನ್ವೈ ಚತುರ್ಯುಜಃ: vai (twin of the Devanagari edit) |
| 193 | `U. Sū. 3-94 as read` → `U. Sū. 2-294` | SECOND-PASS S1: Kannada p.193 ರಮೇಸ್ತ ಚ—(ಉ. ಸೂ. ೨-೨೯೪) |
| 193 | `*natn* [print: "ನಟ್"?]` → `*naj*` | SECOND-PASS S13: Kannada p.193 ನಜ್ ಪ್ರತ್ಯಯ; letters via sp_sanskrit |
| 197 | `(Pā. Sū. 6-2-172)` → `(Pā. Sū. 6-2-122)` | SECOND-PASS S1: Kannada p.197 ನಞ್ ಸುಭ್ಯಾಮ್—(ಪಾ. ಸೂ. ೬-೨-೧೨೨) |
| 200 | `(Ṛ. Saṃ. 1-114-1, as read from the print.)` → `(Ṛ. Saṃ. 10-92-9.)` | SECOND-PASS S1: Kannada p.201 ಸ್ತೋಮಂ ವೋ ಅದ್ಯ ರುದ್ರಾಯ… (ಋ. ಸಂ. ೧೦-೯೨-೯) as printed |
| 202 | `(Ṛ. Saṃ. 9-80-2, as read from the print.)` → `(Ṛ. Saṃ. 9-90-5.)` | SECOND-PASS S1: Kannada p.202 ಮತ್ಸಿ ಸೋಮ ವರುಣಂ… (ಋ. ಸಂ. ೯-೯೦-೫) |
| 203 | `(U. Sū. 4-165 as read)` → `(U. Sū. 4-604)` | SECOND-PASS S1: Kannada p.203 ಪುವೋ ಹ್ರಸ್ವಶ್ಚ—(ಉ. ಸೂ. ೪-೬೦೪) |
| 203 | `*hetumati ca* gives *ṇic*` → `*hetumati ca* (Pā. Sū. 3-1-26) gives *ṇic*` | SECOND-PASS S3: Kannada p.203 ಹೇತುಮತಿ ಚ (ಪಾ. ಸೂ. ೩-೧-೨೬) |
| 203 | `(Pā. Sū. 6-2-1)` → `(Pā. Sū. 6-2-2)` | SECOND-PASS S1: Kannada p.203 ಬಹುವ್ರೀಹೌ ಪ್ರಕೃತ್ಯಾ ಪೂರ್ವಪದಂ (ಪಾ. ಸೂ. ೬-೨-೨) |
| 205 | `(Ṛ. Saṃ. 8-41-2, as read from the print.)` → `(Ṛ. Saṃ. 8-69-12.)` | SECOND-PASS S1: Kannada p.205 (ಋ. ಸಂ. ೮-೬೯-೧೨) |
| 205 | `(Ṛ. Saṃ. 3-41-1, as read from the print.)` → `(Ṛ. Saṃ. 2-11-1.)` | SECOND-PASS S1: Kannada p.205 (ಋ. ಸಂ. ೨-೧೧-೧) |
| 206 | `(Ni. 5-24, as printed "೩-೨೪" or similar — doubtful)` → `(Ni. 5-24)` | SECOND-PASS S1: Kannada p.206 (ನಿ. ೫-೨೪) |
| 207 | `(Pā. Sū. 7-1-102)` → `(Pā. Sū. 3-1-102)` | SECOND-PASS S1: Kannada p.207 ಉದೋಷ್ಯಪೂರ್ವಸ್ಯ(ಪಾ. ಸೂ. ೩-೧-೧೦೨) |
| 210 | `(Ṛ. Saṃ. 1-166-50, as read from the print.)` → `(Ṛ. Saṃ. 1-164-50.)` | SECOND-PASS S1: Kannada p.210 (ಋ. ಸಂ. ೧-೧೬೪-೫೦) |
| 210 | `(Chā. U. 3-10-3, as read from the print "೩-೧೦-೩".)` → `(Chā. U. 2-10-5.)` | SECOND-PASS S1: Kannada p.210 (ಛಾ. ಉ. ೨-೧೦-೫) |
| 211 | `(U. Sū. 2-50 as read)` → `(U. Sū. 2-208)` | SECOND-PASS S1: Kannada p.211 ದ್ರುದಕ್ಷಿಭ್ಯಾಮಿನನ್(ಉ. ಸೂ. ೨-೨೦೮) |
| 211 | `(Pā. Sū. 6-1-197)` → `(Pā. Sū. 6-1-192)` | SECOND-PASS S1: Kannada p.211 ಇತ್ಯಾದಿರ್ನಿತ್ಯಮ್(ಪಾ. ಸೂ. ೬-೧-೧೯೨) |

### 2026-11-27 qmark_strip.py: BLOCK 597 marks removed from 310 Sanskrit-block lines (derived data, K9); BARE 14 boilerplate remark lines removed (15 marks); OTHER 1041 marks left

### 2026-11-27 second pass, batch m1-150.tsv
| page | old → new | why |
|---|---|---|
| i | `(as printed, in small type; the numbers were checked against the reader's OCR, which reads` → `(as printed, in small type): Ṛ. Saṃ. 1-18-1; 1-51-13; 1-112-11; 1-116-7; 1-117-6; 1-126-3;` | SECOND-PASS Q1: Kannada text, the list of the seer Kakṣīvān: ಋ. ಸಂ. ೧-೧೮-೧; ೧-೫೧-೧೩; ೧-೧೧೨-೧೧; ೧-೧೧೬-೭; ೧-೧೧೭-೬; ೧-೧೨೬-೩; ೪-೨೬-೧; ೮-೯-೧೦; ೯-೭೪-೮; ೧೦-೨೫-೧೦; ೧೦-೬೧-೧೬ |
| 5 | `(the word *mīraka* is not understood here, `[?]`)` → `(the word *mīraka* is not understood here)` | SECOND-PASS Q2: Kannada p.5 has ವಿವಿಧಮೀರಕೈರ್ as the English; no word to settle |
| 9 | `; the middle words of the line are read with doubt `[?]`.)` → `.)` | SECOND-PASS Q2: Kannada p.9 has (ಋ. ಸಂ. ೧-೧೭೪-೧) and the passage; doubt note only |
| 30 | `stay unsettled after a zoomed re-view (marked `[?]`);` → `stay unsettled after a zoomed re-view;` | SECOND-PASS Q2: remark describing the marking of doubts; no number or reading depends on the mark; clause shortened |
| 42 | `is read letter by letter and the doubtful places are marked `[?]`.)*` → `is read letter by letter.)*` | SECOND-PASS Q2: remark describing the marking of doubts; no number or reading depends on the mark; clause shortened |
| 46 | `"1-139-2 [?]"` → `"1-139-2"` | SECOND-PASS Q2: reference 1-181-7 stands; the quoted earlier wrong reading needs no mark |
| 46 | `"1-134-4 [?]"` → `"1-134-4"` | SECOND-PASS Q2: reference 1-135-9 stands; the quoted earlier wrong reading needs no mark |
| 46 | `"1-130-2 [?]"` → `"1-130-2"` | SECOND-PASS Q2: reference 1-150-3 stands; the quoted earlier wrong reading needs no mark |
| 53 | `read letter by letter, with doubtful words marked `[?]`.)*` → `read letter by letter.)*` | SECOND-PASS Q2: remark describing the marking of doubts; no number or reading depends on the mark; clause shortened |
| 71 | `confirmed by the OCR unless marked `[?]`.)*` → `confirmed by the OCR.)*` | SECOND-PASS Q2: remark describing the marking of doubts; no number or reading depends on the mark; clause shortened |
| 82 | `are my own readings, `[?]` where doubtful.)*` → `are my own readings.)*` | SECOND-PASS Q2: remark describing the marking of doubts; no number or reading depends on the mark; clause shortened |
| 89 | `*vakṣa[?]dvasu*` → `*vakṣadvasu*` | SECOND-PASS Q1: Kannada p.89 ಯೂಯಾವದನ್ಯಾವಕ್ಷದ್ವಸು: no letters between vakṣa and dvasu |
| 98 | `note that the same verse was cited on p. 89 with the number given there as `[?]`: this rea` → `note that this reading supersedes the number given for the same verse on p. 89.)` | SECOND-PASS Q2: Kannada p.98 (ಋ. ಸಂ. ೧-೧೨೫-೨) confirms the number |
| 113 | `the words "sa[?]īṣaddhasantī" and "vaṃtasthānīyāni" are doubtful in the print;` → `the word "vaṃtasthānīyāni" is as in the Kannada of the page;` | SECOND-PASS Q1: Kannada p.113 has ವಂತಸ್ಥಾನೀಯಾನಿ; the other word is not in the Kannada in that form |
| 113 | ` [?] (the word is unclear in the print)` → `` | SECOND-PASS Q2: Kannada p.113 ವಂತಸ್ಥಾನೀಯಾನಿ agrees |
| 130 | `The reference is printed "೭-೬೩-೪" as I read the glyphs (flat-footed 7), but the user's num` → `The reference is Ṛ. 7-63-4.` | SECOND-PASS Q1: Kannada p.130: ಋ. ೭-೬೩-೪ |
| 134 | `In "abhisṛṣṭānām" the conjunct after *ṣ* is not quite clear, hence [?].` → `"abhisṛṣṭānām" is as in the Kannada.` | SECOND-PASS Q2: Kannada p.134 ಅಭಿಸೃಷ್ಟಾನಾಂ agrees |
| 134 | `, is not settled — the letters after *yac* are unclear, hence [?];` → `, is as in the Kannada (*tadāhuryacchasyata*);` | SECOND-PASS Q1: Kannada p.134 ತದಾಹುರ್ಯಚ್ಛಸ್ಯತ |
| 143 | `the second word of the line is printed as *va*, a hooked cluster (ya-like subscript or the` → `the second word of the line is *vyenī* as in the Kannada; no *syā*` | SECOND-PASS Q1: Kannada p.143 ಏಷಾ ವ್ಯೇನೀ ಭವತಿ (ಋ. ಸಂ. ೫-೮೦-೪) |
| 159 | `, and the words marked [?] are doubtful in the print; the first` → `; the first` | SECOND-PASS Q2: remark describing the marking of doubts; no number or reading depends on the mark; clause shortened |
| 163 | `*tad[?]ā bhavati` → `*tadrā bhavati` | SECOND-PASS Q1: Kannada p.163 ತದ್ರಾ ಭವತಿ ರೂಪವತೀ |
| 177 | `The OCR is garbled; doubtful readings are marked [?].)*` → `The OCR is garbled.)*` | SECOND-PASS Q2: remark describing the marking of doubts; no number or reading depends on the mark; clause shortened |
| 193 | `the first numeral and the lines marked [?] are doubtful in the print.)` → `the first numeral and some lines are doubtful in the print.)` | SECOND-PASS Q2: remark describing the marking of doubts; no number or reading depends on the mark; clause shortened |
| 209 | `pratiṣidhyeta* [?] —` → `pratiṣidhyeta* —` | SECOND-PASS Q2: Kannada p.209 ತತ್ಪ್ರತಿಷಿದ್ಧಂ ಪ್ರತಿಷಿದ್ಧ್ಯೇತ: the quotation stands |
| 216 | `the word "tahye 'ṣām" is odd and kept with [?]` → `the Kannada of the page reads "tarhyeṣām"` | SECOND-PASS Q1: Kannada p.216 ತರ್ಹ್ಯೇಷಾಮನ್ಯೋ ಜನಃ; the Sanskrit block is derived data and is not edited |
| 237 | `the earlier [?] marks on it are resolved` → `the earlier doubts on it are resolved` | SECOND-PASS Q2: remark describing the marking of doubts; no number or reading depends on the mark; clause shortened |
| 237 | ` — "[?]" marks are not needed where the print was clear to me, but the middle` → `; the middle` | SECOND-PASS Q2: remark describing the marking of doubts; no number or reading depends on the mark; clause shortened |
| 241 | `the earlier readings and [?] marks are replaced by these` → `the earlier readings are replaced by these` | SECOND-PASS Q2: remark describing the marking of doubts; no number or reading depends on the mark; clause shortened |
| 247 | `the word marked [?] is doubtful, and` → `one word is doubtful, and` | SECOND-PASS Q2: remark describing the marking of doubts; no number or reading depends on the mark; clause shortened |
| 249 | `ṛks 1–[?] of the 111th Sūkta of the ninth maṇḍala [as printed; the count of ṛks is a small` → `ṛks 1–3 of the 111th Sūkta of the ninth maṇḍala` | SECOND-PASS Q1: Kannada p.249: ೯ ನೇ ಮಂಡಲದ ೧೧೧ ನೇ ಸೂಕ್ತದಲ್ಲಿರುವ ೩ ಋಕ್ಕುಗಳಿಗೆ |
| 250 | `(Ni. 10-4[?]; the last digit is not settled by the zoom.)` → `(Ni. 10-42.)` | SECOND-PASS Q1: Kannada p.249 (ನಿ. ೧೦-೪೨) |
| 255 | `the places marked [?] in the Sanskrit are not settled.` → `some places in the Sanskrit are not settled.` | SECOND-PASS Q2: remark describing the marking of doubts; no number or reading depends on the mark; clause shortened |
| 257 | `several words, marked [?], are doubtful.` → `several words are doubtful.` | SECOND-PASS Q2: remark describing the marking of doubts; no number or reading depends on the mark; clause shortened |
| 258 | `the words marked [?] are small or garbled` → `some words are small or garbled` | SECOND-PASS Q2: remark describing the marking of doubts; no number or reading depends on the mark; clause shortened |
| 279 | `Two places formerly marked [?] were re-read` → `Two places were re-read` | SECOND-PASS Q2: remark describing the marking of doubts; no number or reading depends on the mark; clause shortened |
| 291 | `the earlier [?] marks in the Saṃhitā of p. 290 are therefore resolved` → `the earlier doubts in the Saṃhitā of p. 290 are therefore resolved` | SECOND-PASS Q2: remark describing the marking of doubts; no number or reading depends on the mark; clause shortened |
| 293 | `(Ni. 2-1 [?], as printed "೨-೧")` → `(Ni. 3-2)` | SECOND-PASS Q1: Kannada p.293 ಅಪ್ಪಃ ದಂಸಃ … ಕರ್ಮನಾಮಗಳಲ್ಲಿ (ನಿ. ೩-೨) |
| 299 | `(Ṛ. Saṃ. 8-1-[?]-[?], as printed "೮-೧-೨"? — I have read it so; the first numeral is doubtf` → `(Ṛ. Saṃ. 1-9-2.)` | SECOND-PASS Q1: Kannada p.299 ಏಮೇನಂ ಸೃಜತಾ ಸುತೇ … (ಋ. ಸಂ. ೧-೯-೨) |
| 302 | `, and the readings marked [?] are doubtful in the small type.)*` → `.)*` | SECOND-PASS Q2: remark describing the marking of doubts; no number or reading depends on the mark; clause shortened |
| 308 | `The readings marked [?] — "sahe laukikādikaḥ", "ṛtvigbhir utpadyase" — are small and doubt` → `The readings "sahe laukikādikaḥ", "ṛtvigbhir utpadyase" are small and doubtful.` | SECOND-PASS Q2: remark describing the marking of doubts; no number or reading depends on the mark; clause shortened |
| 309 | `(Ṛ. Saṃ. 10-50-6; the reference numerals are small and doubtful — as read by the OCR "१०-५` → `(Ṛ. Saṃ. 10-50-6.)` | SECOND-PASS Q2: Kannada p.309 (ಋ. ಸಂ. ೧೦-೫೦-೬) agrees |
| 309 | `(Ṛ. Saṃ. 7-38-2; as read by the OCR "२-२०-२" [?].)` → `(Ṛ. Saṃ. 7-38-2.)` | SECOND-PASS Q2: Kannada p.309 (ಋ. ಸಂ. ೭-೩೮-೨) agrees |
| 310 | `(Ṛ. Saṃ. 7-[?]-3, numerals doubtful: the OCR gives "७-३३-३" [?].)` → `(Ṛ. Saṃ. 7-25-3.)` | SECOND-PASS Q1: Kannada p.310 ದ್ಯುಮ್ನಮಧಿ ರತ್ನಂ ಚ ಧೇಹಿ (ಋ. ಸಂ. ೭-೨೫-೩) |
| 310 | `(Ṛ. Saṃ. 4-[?]-4, as read by the OCR "४-४०-४"; the small-type letters are partly doubtful ` → `(Ṛ. Saṃ. 4-40-4.)` | SECOND-PASS Q1: Kannada p.310 (ಋ. ಸಂ. ೪-೪೦-೪) |
| 310 | `(Ni. 3-[?]; OCR "३-१३")` → `(Ni. 3-13)` | SECOND-PASS Q1: Kannada p.310 ಪ್ರಜ್ಞಾನಾಮಗಳಲ್ಲಿ (ನಿ. ೩-೧೩) |
| 311 | `, letters partly doubtful: [?]]` → `]` | SECOND-PASS Q2: Kannada p.311 has the sentence ಅಜರ - ಅಸ್ತೋತಃ । ಜರಾ ಸ್ತುತಿಃ । ಆಸೌ ನ ಕಸ್ಯಾಪಿ ಸ್ತೋತಾ ಭವತಿ ಕಿಂತು ಸರ್ವೈಃ ಸ್ವಯಂ ಸ್ತೂಯತೇ |
| 311 | `(Pā. Sū. 6-3-[?])` → `(Pā. Sū. 8-2-17)` | SECOND-PASS Q1: Kannada p.311 ನಾದ್ಘಸ್ಯ (ಪಾ. ಸೂ. ೮-೨-೧೭) |
| 313 | `āharādīnāṃ satyādipūpasaṃkhyānam iti ratvam*" [as printed, doubtful: [?]]` → `aharādīnāṃ patyādiṣūpasaṃkhyānam iti ratvam*"` | SECOND-PASS Q1: Kannada p.313 ಅಹರಾದೀನಾಂ ಪತ್ಯಾದಿಷೂಪಸಂಖ್ಯಾನಮಿತಿ ರತ್ನಂ (p.316 ರತ್ತ್ವ) |
| 313 | `pāṭhāt*" [?].)*` → `pāṭhāt*".)*` | SECOND-PASS Q2: Kannada p.313 ಕ್ಷೇತಿ ಭೂನಾಮ ಕ್ಷಾ ಕ್ಷಾಮೇತಿ ತನ್ನಾಮಸು ಪಾಠಾತ್ agrees |
| 313 | `of the wealthy [?];` → `of the wealthy;` | SECOND-PASS Q2: Kannada p.315 ಮಹತಾಂ ಧನವತಾಂ agrees |
| 314 | `(Ṛ. Saṃ. 1-[?]-[?]; as read by the OCR "१-१८७-१"; small type, letters partly doubtful [?].` → `(Ṛ. Saṃ. 1-187-1.)` | SECOND-PASS Q1: Kannada p.314 (ಋ. ಸಂ. ೧-೧೮೭-೧) |
| 315 | `(Ni. 1-9 [?]; doubtful letters)` → `(Ni. 1-9; doubtful letters)` | SECOND-PASS Q2: Kannada p.315 (ನಿ ೧-೯) agrees |
| 315 | `(Ni. 1-[?]; OCR "२-५")` → `(Ni. 2-5)` | SECOND-PASS Q1: Kannada p.315 ಇಪ್ಪತ್ತೊಂದು ಪೃಥಿವೀನಾಮಗಳಲ್ಲಿ (ನಿ. ೨-೫) |
| 315 | `", Ni. [?])` → `")` | SECOND-PASS S3: Kannada p.315 gives no Nirukta number after this citation |
| 316 | ` [as read: [?]];` → `;` | SECOND-PASS Q2: Kannada p.316 ಆಹರಾದೀನಾಂ ಪತ್ಯಾದಿಷು ಉಪಸಂಖ್ಯಾನಮ್ has the sūtra |
| 316 | `gives *tu* [?];` → `gives *ślu* in place of *śap*;` | SECOND-PASS Q1: Kannada p.316 ಬಹುಲಂ ಛಂದಸಿ ಎಂಬುದರಿಂದ ಶಪಿಗೆ ಶ್ಲು ಆದೇಶ |
| 317 | `"*tadeva prārthyata*" [?].)*` → `"*tadeva prārthyata*".)*` | SECOND-PASS Q2: remark describing the marking of doubts; no number or reading depends on the mark; clause shortened |
| 318 | `are doubtful [?].)*` → `are doubtful.)*` | SECOND-PASS Q2: remark describing the marking of doubts; no number or reading depends on the mark; clause shortened |
| 320 | `(Ni. 1-[?]; as printed "೧-೩೪"?) and among the names of strength (Ni. 3-9; OCR "२-२४" and "` → `(Ni. 2-24) and among the names of strength (Ni. 3-9). And in the Ṛks 1-27-2, 1-29-8, 1-51-` | SECOND-PASS Q1: Kannada p.320 (ನಿ. ೨-೨೪); (ನಿ ೩-೯); ೧-೨೭-೨; ೧-೨೯-೮; ೧-೫೧-೪; ೧-೫೨-೧೦ ಇತ್ಯಾದಿ ಋಕ್ಕುಗಳಲ್ಲಿಯೂ |
| 321 | `several letters doubtful [?])` → `several letters doubtful)` | SECOND-PASS Q2: remark describing the marking of doubts; no number or reading depends on the mark; clause shortened |
| 323 | `are small and doubtful [?]; the OCR gives the same.` → `are small and doubtful; the OCR gives the same.` | SECOND-PASS Q2: Kannada p.325 gives ತೈ. ಸಂ. ೭-೪-೧೮-೨; ೧-೨-೫-೧; ತೈ. ಬ್ರಾ. ೧-೧-೪-೪ as the English |
| 324 | `(Ṛ. Saṃ. 1-117-21, as read; the numerals are small and doubtful [?].)` → `(Ṛ. Saṃ. 1-117-21.)` | SECOND-PASS Q2: Kannada p.324 (ಋ. ಸಂ. ೧-೧೧೭-೨೧) agrees |
| 325 | `(Ni. 6-11 [?])` → `(Ni. 6-11)` | SECOND-PASS Q2: Kannada p.325 (ನಿ. ೬-೧೧) agrees |
| 325 | `(Tai. Saṃ. 2-6-4-1; as printed "೭-೪-೧೮-೨"? the numerals are doubtful)` → `(Tai. Saṃ. 7-4-18-2)` | SECOND-PASS Q1: Kannada p.325 ಪರಮಂತಂ ಪೃಥಿವ್ಯಾಃ (ತೈ. ಸಂ. ೭-೪ ೧೮-೨) |
| 325 | `(Tai. Saṃ. 3-5-4-1 [?])` → `(Tai. Saṃ. 2-6-4-1)` | SECOND-PASS Q1: Kannada p.325 ಏತಾವತೀ ವೈ ಪೃಥಿವೀ ಯಾವಶೀ ವೇದಿಃ (ತೈ. ಸಂ. ೨-೬-೪-೧) |
| 326 | `(Uṇ. 3-[?])` → `(Uṇ. 2-229)` | SECOND-PASS Q1: Kannada p.326 ವಶಃ ಕಿತ್ (ಉ ಸೂ. ೨-೨೨೯) |
| 328 | `Several small letters are doubtful: [?].)` → `Several small letters are doubtful.)` | SECOND-PASS Q2: remark describing the marking of doubts; no number or reading depends on the mark; clause shortened |
| 330 | `(Ṛ. Saṃ. 2-[?]-2; as read "೨-೩೪-೨" [?].)` → `(Ṛ. Saṃ. 7-38-7.)` | SECOND-PASS Q1: Kannada p.330 ಜಂಭಯಂತೋಹಿಂ ವೃಕಂ (ಋ. ಸ. ೭-೩೮-೭) the verse above |
| 330 | `(Vā. Saṃ. 28-18 [?] and 9-43, as read; **small-type, letters doubtful — I record it as rea` → `(Vā. Saṃ. 28-16 and Ni. 9-43.)` | SECOND-PASS Q1: Kannada p.330 ಊರ್ಜಾಹುತೀ … ( ನಾ. ಸಂ. ೨೮ ೧೬ ಮತ್ತು ನಿ. ೯-೪೩ ) |
| 331 | `(Ṛ. Saṃ. 6-8-4, as read. **The word after "ā" in the second line is not clearly legible in` → `(Ṛ. Saṃ. 6-8-4.)` | SECOND-PASS Q2: Kannada p.331 ಆ ದೂತೋ ಅಗ್ನಿಮಭರದ್ವಿವಸ್ವತೋ (ಋ. ಸಂ. ೬-೮-೪) agrees |
| 334 | `[as read: Ni. 6-14 [?]]` → `[Ni. 6-14]` | SECOND-PASS Q2: Kannada p.337 ತುರ್ವಣಿಸ್ತೂರ್ಣವನಿಃ (ನಿ. ೬-೧೪) |
| 334 | `[Ni. 2-31 [?]]` → `[Ni. 2-24]` | SECOND-PASS Q1: Kannada p.338 ಸಾನು ಸಮುಚ್ಚ್ರಿತಂ ಭವತಿ ಸಮುನ್ನುನ್ನಮಿತಿ ವಾ (ನಿ. ೨-೨೪) |
| 335 | `(Ṛ. Saṃ. 6-[?]-4, as read; numerals doubtful.` → `(Ṛ. Saṃ. 8-68-4.` | SECOND-PASS Q1: Kannada p.335 ಏವೈಶ್ಚ ಚರ್ಷಣೀನಾಮೂತೀ ಹುವೇ ರಥಾನಾಂ (ಋ. ಸಂ. ೮-೬೮-೪) |
| 335 | `(Ni. 1-[?]; as read "೧-೧೨"? [?])` → `(Ni. 2-24)` | SECOND-PASS Q1: Kannada p.335 ನೂರೊಂದು ಉದಕನಾಮಗಳಲ್ಲಿ (ನಿ. ೨-೨೪) |
| 336 | `(Ṛ. Saṃ. 2-43-1, as printed; the first word and the last words are doubtful in my reading:` → `(Ṛ. Saṃ. 2-42-1.)` | SECOND-PASS Q1: Kannada p.336 (ಋ. ಸಂ. ೨-೪೨-೧) |
| 336 | ` [as read; small type: [?]]` → `` | SECOND-PASS Q2: Kannada p.336 ಪ್ರಜಾಂ ವರ್ಷತೀತಿ … ವೃಷಭಃ agrees |
| 336 | `(Ṛ. Saṃ. 9-107-[?], as printed: the numerals "೯-೧೦೭" and the *pāda* are small and doubtful` → `(Ṛ. Saṃ. 9-107-9.)` | SECOND-PASS Q1: Kannada p.337 ಅನೂಪೇ ಗೋಮಾನ್ ಗೋಭಿರಕ್ಷಾಃ (ಋ. ಸಂ. ೯-೧೦೭-೯) |
| 337 | `(Ṛ. Saṃ. 10-94-6 [?], as read "೧೦-೯೪-೬"; the text of the line is as read and doubtful.)` → `(Ṛ. Saṃ. 10-89-6.)` | SECOND-PASS Q1: Kannada p.337 ನ ಯಸ್ಯ ದ್ಯಾವಾಪೃಥಿವೀ ನ ಧನ್ವ … (ಋ. ಸಂ. ೧೦-೮೯-೬) |
| 337 | `are doubtful: [?].)` → `are doubtful.)` | SECOND-PASS Q2: remark describing the marking of doubts; no number or reading depends on the mark; clause shortened |
| 338 | `*upāramante [?] eṣv iti upārāḥ tiṣṭhyāḥ [?] yajamānagṛhā vā*` → `*upāramaṃte eṣvannayaḥ ityuparāḥ dhiṣṇyā yajamānagṛhā vā*` | SECOND-PASS Q1: Kannada p.338 ಉಪಾರಮಂತೇ ಏಷ್ವನ್ನಯಃ ಇತ್ಯುಪರಾಃ ಧಿಷ್ಣ್ಯಾ ಯಜಮಾನಗೃಹಾ ನಾ |
| 338 | `(Ni. 3-30 [?])` → `(Ni. 3-22)` | SECOND-PASS Q1: Kannada p.338 ಸದಸೀ (ನಿ. ೩-೨೨) |
| 338 | `(Uṇ. 4-[?])` → `(Uṇ. 4-641)` | SECOND-PASS Q1: Kannada p.339 ಸ್ತುರೀಭ್ಯಾಂ ತುಟ್ ಚ (ಉ. ಸೂ. ೪-೬೪೧) |
| 340 | `are doubtful: [?].)*` → `are doubtful.)*` | SECOND-PASS Q2: remark describing the marking of doubts; no number or reading depends on the mark; clause shortened |
| 342 | `(Ṛ. Saṃ. 2-31-4 [?], as read "೨-೩೧-೪"; the numerals are small.)` → `(Ṛ. Saṃ. 7-39-4.)` | SECOND-PASS Q1: Kannada p.342 ಅಧ್ವರ ಉಶತೋ ಯಕ್ಷ್ಯಗ್ನೇ (ಋ. ಸಂ. ೭-೩೯-೪) |
| 343 | `(Ni. 1-[?]; as read "೧-೧೨")` → `(Ni. 2-27)` | SECOND-PASS Q1: Kannada p.343 ಇಪ್ಪತ್ತಾರು ಅಶ್ವನಾಮಗಳಲ್ಲಿ (ನಿ. ೨-೨೭) |
| 343 | `(Ṛ. Saṃ. 3-31-2, as read; the numerals are small and doubtful [?].)` → `(Ṛ. Saṃ. 3-31-2.)` | SECOND-PASS Q2: Kannada p.343 (ಋ. ಸಂ. ೩-೩೧-೨) agrees |
| 343 | `(Ṛ. Saṃ. 2-37-3, as read; the numerals are doubtful. The word "*neṣprāt*" is printed as in` → `(Ṛ. Saṃ. 2-37-2.)` | SECOND-PASS Q1: Kannada p.343 ತ್ವಂ ನೇಷ್ಟ್ರಾತ್ ಸೋಮಂ ದ್ರವಿಣೋದಃ ಪಿಬ (ಋ. ಸಂ. ೨-೩೭-೨) |
| 345 | `a few places are doubtful: [?] — esp.` → `a few places are doubtful — esp.` | SECOND-PASS Q2: remark describing the marking of doubts; no number or reading depends on the mark; clause shortened |
| 345 | `praiseworthy [?] or from the destroyer` → `praiseworthy or from the destroyer` | SECOND-PASS Q2: Kannada p.345 ಶಂಸನೀಯಾತ್ agrees |
| 347 | `(Ni. 1-[?]) and among the names of wealth (Ni. 2-15 and "೩-೯")` → `(Ni. 2-15) and among the names of wealth (Ni. 3-9)` | SECOND-PASS Q1: Kannada p.347 ರಶ್ಮಿ ನಾಮಗಳಲ್ಲಿಯೂ (ನಿ. ೨-೧೫); ಧನ ನಾಮಗಳಲ್ಲಿಯೂ (ನಿ. ೩-೯) |
| 348 | `"*tapur yayastu*" [?].)` → `"*tapur yayastu*".)` | SECOND-PASS Q2: Kannada p.348 ತಪುರ್ಯಯಸ್ತು (ಋ. ಸಂ. ೭-೧೦೪-೨) agrees |
| 350 | `are doubtful: [?]. Sense so far:` → `are doubtful. Sense so far:` | SECOND-PASS Q2: remark describing the marking of doubts; no number or reading depends on the mark; clause shortened |
| 351 | `are doubtful: [?].)*` → `are doubtful.)*` | SECOND-PASS Q2: remark describing the marking of doubts; no number or reading depends on the mark; clause shortened |
| 353 | `(Ṛ. Saṃ. 5-62-3 [?], as read; the numerals are doubtful.` → `(Ṛ. Saṃ. 6-37-3.` | SECOND-PASS Q1: Kannada p.353 ಆಸಸ್ರಾಣಾಸಃ ಶವಸಾನಮಚ್ಛೇಂದ್ರಂ (ಋ. ಸಂ. ೬-೩೭-೩) |
| 353 | `(Uṇ. 2-[?])` → `(Uṇ. 2-259)` | SECOND-PASS Q1: Kannada p.353 ಆರ್ತಿ ಸೃಧೃ— (ಉ. ಸೂ. ೨-೨೫೯) |
| 355 | `are doubtful: [?] — e.g.` → `are doubtful — e.g.` | SECOND-PASS Q2: remark describing the marking of doubts; no number or reading depends on the mark; clause shortened |
| 356 | `[a doubtful phrase "*āyaṣvāram agnir hinastīti prasiddham*" — I give the letters as read: ` → `*āyaṣṭāram agnirhinastīti prasiddham*` | SECOND-PASS Q1: Kannada p.356 ಆಯಷ್ಟಾರಮಗ್ನಿರ್ಹಿನಸ್ತೀತಿ ಪ್ರಸಿದ್ಧಂ |
| 357 | `(Ṛ. Saṃ. 2-[?]-[?], as read "೨-೪೧-೨" [?]; small type, doubtful letters: [?].)` → `(Ṛ. Saṃ. 7-39-2.)` | SECOND-PASS Q1: Kannada p.357 ಪ್ರ ವಾವೃಜೇ … ವಾಯುಃ ಪೂಷಾ ಸ್ವಸ್ತಯೇ ನಿಯುತ್ವಾನ್ (ಋ. ಸಂ. ೭-೩೯-೨) |
| 358 | `(Ni. 1-[?]; as read "೧-೩"), of speech (Ni. 1-[?]; "೧-೩೩"), of food (Ni. 2-5; "೨-೯") and of` → `(Ni. 2-5), of speech (Ni. 2-23), of food (Ni. 3-9) and of the cow (Ni. 3-9)` | SECOND-PASS Q1: Kannada p.358 ಪೃಥಿವೀನಾಮ (ನಿ ೨ ೫); ವಾಙ್ನಾಮ (ನಿ. ೨-೨೩); ಅನ್ನ (ನಿ. ೩-೯); ಗೋನಾಮ (ನಿ. ೩-೯) |
| 358 | `(Ni. 1-[?]; as read "೩-೨೪"[?])` → `(Ni. 2-24)` | SECOND-PASS Q1: Kannada p.358 ಮಹಃ ಶಬ್ದವು ಉದಕನಾಮಗಳಲ್ಲಿ (ನಿ. ೨-೨೪) |
| 358 | `[as read: Uṇ. 2-[?]]` → `[Uṇ. 2-239]` | SECOND-PASS Q1: Kannada p.358 ಕೃ ಪೃ ವೃಜಿ- (ಉ. ಸೂ. ೨-೨೩೯) |
| 360 | `"*tuṣṭeme…*"): [?].)*` → `"*tuṣṭeme…*").)*` | SECOND-PASS Q2: remark describing the marking of doubts; no number or reading depends on the mark; clause shortened |
| 362 | `(Ni. 9-42 [?], as read "೯-೪೨")` → `(Ni. 9-42)` | SECOND-PASS Q2: Kannada p.362 (ನಿ. ೯-೪೨) agrees |
| 362 | `(Ṛ. Saṃ. 1-51-14, as read "೧-೩೧-೧೪"; the first line has doubtful letters in the print: [?]` → `(Ṛ. Saṃ. 1-51-14.)` | SECOND-PASS Q2: Kannada p.362 (ಋ. ಸಂ. ೧-೫೧-೧೪) agrees |
| 364 | `several letters doubtful [?]).**` → `several letters doubtful).**` | SECOND-PASS Q2: remark describing the marking of doubts; no number or reading depends on the mark; clause shortened |
| 366 | `at the head is small and doubtful [?];` → `at the head (Ni. 3-12) is small;` | SECOND-PASS Q2: Kannada p.366 head: ನಿ. ೩-೧೨ |
| 367 | `doubtful in places: [?];` → `doubtful in places;` | SECOND-PASS Q2: remark describing the marking of doubts; no number or reading depends on the mark; clause shortened |
| 368 | ` [Doubtful in the small print: [?].]` → `` | SECOND-PASS Q2: remark describing the marking of doubts; no number or reading depends on the mark; clause shortened |
| 368 | `(Ni. 2-[?]; as read "೨-೯")` → `(Ni. 3-9)` | SECOND-PASS Q1: Kannada p.368 ವಾಜ ಶಬ್ದವು ಅನ್ನನಾಮಗಳಲ್ಲಿಯೂ (ನಿ. ೩-೯) |
| 368 | `(Ni. 2-[?], "೨-೯")` → `(Ni. 3-9)` | SECOND-PASS Q1: Kannada p.368 ಸಂಗ್ರಾಮ ನಾಮಗಳಲ್ಲಿಯೂ (ನಿ. ೩-೯) |

### 2026-11-27 second pass, batch m1-150_2.tsv
| page | old → new | why |
|---|---|---|
| 209 | `pratiṣidhyeta* —` → `pratiṣidhyeta* [?] —` | SECOND-PASS Q2: mark restored: Kannada p.209 reads ತತ್ಪ್ರತಿಷಿದ್ಧಂ ಪ್ರತಿಷಿದ್ಧ್ಯೇತ, not the English wording; earlier decision (findings q115) keeps the mark |

### 2026-11-27 second pass, batch m350-499.tsv
| page | old → new | why |
|---|---|---|
| 369 | `(Ni. 1-[?]; as read "೧-೧೧")` → `(Ni. 2-13)` | SECOND-PASS Q1: Kannada p.369 ವಾಕ್ ಶಬ್ದವು ಐವತ್ತೇಳು ವಾಙ್ಮಾಮಗಳಲ್ಲಿ (ನಿ. ೨-೧೩) |
| 370 | ` [Pā. Sū. 3-2-[?]] gives *kvip*` → ` gives *kvip*` | SECOND-PASS S3: Kannada p.370 ಕ್ವಿಬ್ಬಚಿ— has no sūtra number; removed with its mark |
| 371 | `read from the image, many letters doubtful: [?]).*` → `read from the image).*` | SECOND-PASS Q2: meta-remark on doubt marking; clause removed, no number or reading depends on it |
| 371 | `the Maruts [?] — the leaders` → `the Maruts — the leaders` | SECOND-PASS Q2: Kannada p.371 ನೃಭಿರ್ಮನುಷ್ಯರೇವ ಸದ್ಭೀಃ ಪಶ್ಚಾದ್ದೇವತ್ವಮಾಪನ್ನೈರ್ಮರುದ್ಧಿಃ agrees |
| 371 | `(Tai. Saṃ. [?], Ait. Br. [?]:` → `(Tai. Saṃ. 6-5-5-1, Ait. Br. 3-20:` | SECOND-PASS Q1: Kannada p.371 ತೈ. ಸಂ. ೬ ೫-೫-೧, ಐ. ಬ್ರಾ. ೩-೨೦; p.373 ತೈ ಸಂ. ೬-೫-೫-೧ completes the first |
| 373 | `(Ai. Brā. 3-20 [?])` → `(Ai. Brā. 3-20)` | SECOND-PASS Q2: Kannada p.373 (ಐ. ಬ್ರಾ. ೩-೨೦) agrees |
| 374 | `(Ni. 1-[?]; as read "೧-೨೨")` → `(Ni. 2-27)` | SECOND-PASS Q1: Kannada p.374 ಅತ್ಯಶಬ್ದವು ಅಶ್ವನಾಮಗಳಲ್ಲಿ (ನಿ. ೨-೨೭) |
| 374 | `(Ṛ. Saṃ. 3 [?], numerals unreadable)` → `(Ṛ. Saṃ. 3)` | SECOND-PASS Q1: Kannada p.374 prints only (ಋ. ಸಂ. ೩) for ನೇಂದ್ರಂ ದೇವಮಮಂಸತ |
| 377 | `are partly illegible and are given only as read, with [?]: I do not claim them.)*` → `are given only as read.)*` | SECOND-PASS Q2: meta-remark on doubt marking; clause shortened (Kannada p.377 has the Tai. Saṃ. and Tāṇḍya references) |
| 379 | `(Ni. 2-[?]; as read "೨-೮")` → `(Ni. 3-8)` | SECOND-PASS Q1: Kannada p.379 ಮರ್ತ್ಯ ಶಬ್ದವು ಮನುಷ್ಯನಾಮಗಳಲ್ಲಿ (ನಿ. ೩-೮) |
| 379 | `(Ṛ. Saṃ. 3-14-4 [?], as read "೩-೧೪-೪".)` → `(Ṛ. Saṃ. 5-13-4.)` | SECOND-PASS Q1: Kannada p.379 ತ್ವಮಗ್ನೇ ಸಪ್ರಥಾ ಅಸಿ … (ಋ. ಸಂ. ೫-೧೩-೪) |
| 379 | `(Ṛ. Saṃ. 1-22-15, as read; the first word of the first line is printed "ಸೋನಾ" and I give i` → `(Ṛ. Saṃ. 1-22-15.)` | SECOND-PASS Q2: Kannada p.379 has (ಋ. ಸಂ. ೧-೨೨-೧೫) and first word ಸ್ಯೋನಾ; doubt note only, shortened |
| 379 | `Tai. Saṃ. 6-2-3-2 [?, as read "೬-೨-೩-೨"], and that Rudra wept in Tai. Saṃ. 1-5-1-1 [?],` → `Tai. Saṃ. 6-2-3-2, and that Rudra wept in Tai. Saṃ. 1-5-1-1,` | SECOND-PASS Q2: Kannada p.379 ತೈ. ಸಂ. ೬-೨-೩-೨; p.377 ತೈ. ಸಂ. ೧-೫-೧-೧ (p.379 prints ೧-೫೧-೧, a misprint) |
| 381 | ` is mine and doubtful until the Pada is read: [?]. The Pada is on the next page.)*` → ` is as in the Kannada text.)*` | SECOND-PASS Q2: Kannada p.381 ಅಸ್ಮಾಕಂ ಬ್ರಹ್ಮೋತಯೇಽವಾ agrees |
| 382 | `; a few letters are doubtful, in particular the clause on *brahma parivṛḍhaṃ karma* and "*` → `. Sense:` | SECOND-PASS Q2: meta-remark on doubt marking; clause removed, the Sense translation stays |
| 384 | `(Ni. 2-[?]; as read "೨-೯")` → `(Ni. 3-9)` | SECOND-PASS Q1: Kannada p.384 ಪೃತ್ಸು ಎಂಬ ಪದವು ಸಂಗ್ರಾಮನಾಮಗಳಲ್ಲಿ (ನಿ. ೩-೯) |
| 385 | `), and the Pada words *atimatim*, *araṇebhiḥ* are doubtful in the print: [?]. The OCR` → `). The OCR` | SECOND-PASS Q2: Kannada p.385 Pada ಅತಿಮತಿಂ agrees; doubt note only (Pada ಅರಣಿಭಿಃ, Wikisource-derived line not touched) |
| 386 | `; a few letters of the small type are doubtful: [?].)*` → `.)*` | SECOND-PASS Q2: meta-remark on doubt marking; clause removed |
| 388 | `(Ni. 2-[?]; as read "೨-೮")` → `(Ni. 3-8)` | SECOND-PASS Q1: Kannada p.388 ಪೂರು ಶಬ್ದವು ಮನುಷ್ಯನಾಮಗಳಲ್ಲಿ (ನಿ. ೩-೮) |
| 390 | `read from the image; small type, some letters doubtful: [?]).*` → `read from the image; small type).*` | SECOND-PASS Q2: meta-remark on doubt marking; clause removed |
| 393 | `(Ṛ. Saṃ. 1-[?]-[?], as read "೧-೮೩-೨" [?]; small type, doubtful letters: [?].)` → `(Ṛ. Saṃ. 1-162-7.)` | SECOND-PASS Q1: Kannada p.393 ಮನ್ಮ … (ಋ. ಸ. ೧-೧೬೨-೭), the Ṛk in which manma is explained |
| 396 | `Read from the image; some small-type letters are doubtful: [?] — e.g. "*vīravīrye ca*", "*` → `Read from the image.)*` | SECOND-PASS Q2: meta-remark on doubt marking; doubt clause removed, Sense stays (Kannada p.398 has harivaḥ āgaccha medhātithermeṣa) |
| 398 | `(Ni. 1-[?]; as read "೩-೩೪")` → `(Ni. 2-24)` | SECOND-PASS Q1: Kannada p.398 ರಯಿ ಶಬ್ದವು ಉದಕನಾಮಗಳಲ್ಲಿಯೂ (ನಿ. ೨-೨೪) |
| 398 | `*harivaḥ, āgaccha, medhātither meṣa* [as read, doubtful: [?]]` → `*harivaḥ, āgaccha, medhātither meṣa*` | SECOND-PASS Q2: Kannada p.398 ಹರಿವ ಆಗಚ್ಛ ಮೇಧಾತಿಥೇರ್ಮೇಷ agrees |
| 400 | `read from the image; small type, a few places doubtful: [?]).*` → `read from the image; small type).*` | SECOND-PASS Q2: meta-remark on doubt marking; clause removed |
| 401 | `from others [?], he becomes` → `from others, he becomes` | SECOND-PASS Q2: Kannada p.401 (ಇತರರ ಸಹಾಯವಿಲ್ಲದೇ ಸ್ತುತಿಸುವ ಸಾಮರ್ಥ್ಯವುಳ್ಳ ನಮ್ಮ ಸ್ತುತಿವಾಕ್ಯಗಳಿಂದ …) agrees |
| 401 | `(Ni. 6-14 [?])` → `(Ni. 6-4)` | SECOND-PASS Q1: Kannada p.401 ಜೂರ್ಣಿರ್ಜವತೇರ್ವಾ … ಯಾಸ್ಕಃ । ನಿ. ೬-೪ |
| 404 | `*astam-īke* and mark doubtful: [?] —` → `*astam-īke* —` | SECOND-PASS Q2: Kannada p.404 Pada ಅಸ್ತಂಈಕೇ agrees with the English reading |
| 405 | `; small type, with a few doubtful places: [?]. Sense:` → `; small type. Sense:` | SECOND-PASS Q2: meta-remark on doubt marking; clause removed, Sense stays |
| 406 | `*tālit* [?]` → `*taḷit*` | SECOND-PASS Q1: Kannada p.406 ತಳಿತ್, ಆಸಾತ್ ಮೊದಲಾದ ಹನ್ನೊಂದು ಅಂತಿಕನಾಮಗಳಲ್ಲಿ (sp_sanskrit.py) |
| 407 | `kanyāvāgaiḥ* [as read, doubtful: [?]]` → `tannirvāhaiḥ*` | SECOND-PASS Q1: Kannada p.407 ಅಭಿಷ್ಟಿಭಿಃ— ಅಭಿಮುಖೈಃ ಯಾಗೈಃ ಯದ್ವಾ ತನ್ನಿರ್ವಾಹೈಃ ಯಾಗೈಃ (sp_sanskrit.py) |
| 407 | `the *ā* is nasalized [?]` → `the *ā* is nasalized` | SECOND-PASS Q2: Kannada p.407 ಅಣೋಪ್ರಗೃಹ್ಯಸ್ಯಾ— (ಪಾ. ಸೂ. ೮-೪-೫೭) agrees |
| 408 | `; *avitā* is doubtful in the Pada: [?].)*` → `; the Pada has *avitariti*.)*` | SECOND-PASS Q1: Kannada p.408 Pada ಓಜಿಷ್ಠ । ತ್ರಾತಃ । ಅವಿತರಿತಿ (sp_sanskrit.py) |
| 409 | `: I give them as read with [?]. Sense:` → `: I give them as read. Sense:` | SECOND-PASS Q2: meta-remark on doubt marking; clause removed, Sense stays |
| 410 | `(Ni. 1-[?]; as read "೧-೩೪")` → `(Ni. 2-24)` | SECOND-PASS Q1: Kannada p.410 ಓಜಃ ಎಂಬ ಶಬ್ದವು ಉದಕನಾಮಗಳಲ್ಲಿಯೂ (ನಿ. ೨-೨೪) |
| 410 | `(Ni. 1-[?]; as read "೩-೧೦")` → `(Ni. 2-21)` | SECOND-PASS Q1: Kannada p.410 ಅದ್ರಿ ಶಬ್ದವು ಮೇಘನಾಮಗಳಲ್ಲಿ (ನಿ. ೨-೨೧) |
| 410 | `*adrir ādṛṇāter ātteḥ [?] api vātreyī syāt*` → `*adrirādṛṇātyanena api vātteḥ syāt*` | SECOND-PASS Q1: Kannada p.410 ಅದ್ರಿರಾದೃಣಾತ್ಯನೇನ ಅಪಿ ವಾತ್ತೇಃ ಸ್ಯಾತ್ (ನಿ. ೪-೪) (sp_sanskrit.py) |
| 411 | `*ācāryaḥ kṣīdiṃ [?] bruyāt*` → `*ācāryaścididaṃ brūyāt*` | SECOND-PASS Q1: Kannada p.411 ಆಚಾರ್ಯ ಶ್ಚಿದಿದಂ ಬ್ರೂಯಾತ್ ಇತಿ ಪೂಜಾಯಾಂ (sp_sanskrit.py) |
| 411 | `(*cidityakutsitaḥ* [?])` → `(*cidityavakutsitaḥ*)` | SECOND-PASS Q1: Kannada p.411 ಚಿದಿತ್ಯವಕುತ್ಸಿತಃ (sp_sanskrit.py) |
| 413 | `; small type, a number of places doubtful: [?]. Sense:` → `; small type. Sense:` | SECOND-PASS Q2: meta-remark on doubt marking; clause removed, Sense stays |
| 414 | `(Ni. 3-[?]; as read "೩-೧೯")` → `(Ni. 3-16)` | SECOND-PASS Q1: Kannada p.415 ವಿಪ್ರ ಶಬ್ದವು ಮೇಧಾವಿನಾಮಗಳಲ್ಲಿ (ನಿ. ೩-೧೬) |
| 414 | `(Tai. Saṃ. 2-1-1-1 [?], as read)` → `(Tai. Saṃ. 7-1-1-4)` | SECOND-PASS Q1: Kannada p.415 ತಮಿಂದ್ರೋ ದೇವತಾನ್ನಸೃಜ್ಯತ (ತ್ರೈ. ಸಂ. ೭-೧-೧-೪); ತ್ರೈ is a misprint of ತೈ |
| 416 | `(vārttika on Pā. Sū. 4-3-1 [?])` → `(vārttika, Pā. Sū. 5-2-39-1)` | SECOND-PASS Q1: Kannada p.416 ಯುಷ್ಮದಸ್ಮದ್ಭ್ಯಾಂ ಛಂದಸಿ ಸಾದೃಶ್ಯ ಉಪಸಂಖ್ಯಾನಮ್ (ಪಾ. ಸೂ. ೫-೨-೩೯-೧) |
| 417 | `read from the image; several letters doubtful [?]).**` → `read from the image).**` | SECOND-PASS Q2: meta-remark on doubt marking; clause removed |
| 418 | `; the small type is partly doubtful: [?] — notably the clause on the particle *na* ("*yady` → `. Sense:` | SECOND-PASS Q2: meta-remark on doubt marking; clause removed, Sense stays |
| 421 | `*gayaḥ, kṛdaraḥ* [as read, doubtful: [?]]` → `*gayaḥ, kṛdaraḥ*` | SECOND-PASS Q2: Kannada p.421 ಗಯಃ ಕೃದರಃ ಎಂಬ ಇಪ್ಪತ್ತೆರಡು ಗೃಹನಾಮಗಳಲ್ಲಿ agrees |
| 421 | `names of food (Ni. 2-[?]; as read "೨-೯")` → `names of food (Ni. 3-9)` | SECOND-PASS Q1: Kannada p.421 ಪ್ರಯಸ್ ಶಬ್ದವು ಅನ್ನನಾಮಗಳಲ್ಲಿ (ನಿ. ೩-೯) |
| 421 | `(Ni. 3-9; as read "೩-೩೨" [?])` → `(Ni. 5-5)` | SECOND-PASS Q1: Kannada p.421 ಸಚಾ … ಯಾಸ್ಕರಿಂದ ಸಹ ಎಂಬ ಅರ್ಥ (ನಿ. ೫-೫); p.419 ನಿ. ೫-೫ |
| 421 | `names of battle (Ni. 2-[?]; as read "೨-೯")` → `names of battle (Ni. 3-9)` | SECOND-PASS Q1: Kannada p.421 ವಾಜಸಾತ್ ಶಬ್ದವು ಸಂಗ್ರಾಮನಾಮಗಳಲ್ಲಿ (ನಿ. ೩-೯) |
| 423 | `read from the image; small type, a few doubtful places [?]).*` → `read from the image; small type).*` | SECOND-PASS Q2: meta-remark on doubt marking; clause removed |
| 423 | `*praṣepaṇīyas* [?]` → `*prakṣepaṇīyāḥ*` | SECOND-PASS Q1: Kannada p.423 ಪ್ರಕ್ಷೇಪಣೀಯಾಃ (sp_sanskrit.py) |
| 425 | `(Ni. 1-[?]; as read "೧-೧೦")` → `(Ni. 2-21)` | SECOND-PASS Q1: Kannada p.425 ಅದ್ರಿ ಶಬ್ದವು ಮೇಘನಾಮಗಳಲ್ಲಿಯೂ (ನಿ. ೨-೨೧) |
| 425 | `10-94-1; the first line is printed differently from what I give and the letters are doubtf` → `10-94-1.)` | SECOND-PASS Q2: Kannada p.425 (ಋ. ಸಂ. ೧೦-೯೪-೧) agrees; doubt note only, shortened |
| 426 | `(Ni. 1-[?]; as read "೩-೧೬")` → `(Ni. 2-16)` | SECOND-PASS Q1: Kannada p.426 ಹರಿತ ಶಬ್ದವು ದಿಙ್ನಾಮಗಳಲ್ಲಿಯೂ (ನಿ. ೨-೧೬) |
| 426 | `(Ni. 1-[?]; "೩-೩೨")` → `(Ni. 2-24)` | SECOND-PASS Q1: Kannada p.426 ನದೀ ನಾಮಗಳಲ್ಲಿಯೂ (ನಿ. ೨-೨೪) |
| 426 | `(Ni. 1-[?], as read "೩-೧೪", a list of the vehicles of the gods; the passage is in small ty` → `(Ni. 2-48, a list of the vehicles of the gods.)` | SECOND-PASS Q1: Kannada p.426 ಹರೀ ಇಂದ್ರಸ್ಯ … ನಿಯುತೋ ವಾಯೋಃ (ನಿ. ೨-೪೮) |
| 428 | `read from the image; small type, partly doubtful: [?]).*` → `read from the image; small type).*` | SECOND-PASS Q2: meta-remark on doubt marking; clause removed |
| 430 | `(Ni. 1-[?]; as read "೩-೩೧")` → `(Ni. 2-21)` | SECOND-PASS Q1: Kannada p.430 ಅಶ್ಮನ್ ಶಬ್ದವು ಮೇಘನಾಮಗಳಲ್ಲಿ (ನಿ. ೨ ೨೧) (hyphen missing in print) |
| 431 | `(Ni. 2-[?]; as read "೨-೯")` → `(Ni. 3-9)` | SECOND-PASS Q1: Kannada p.431 ಇಷಂ ಎಂಬ ಶಬ್ದವು ಅನ್ನ ನಾಮಗಳಲ್ಲಿ (ನಿ ೩-೯) |
| 433 | `are small and partly doubtful: [?]. Sense:` → `are small. Sense:` | SECOND-PASS Q2: meta-remark on doubt marking; clause removed, Sense stays |
| 433 | `who walks crooked [?] among us` → `who walks crooked among us` | SECOND-PASS Q2: Kannada p.433 ತ್ವಮಪ್ಯಸ್ಮಾಸು ವಕ್ರಮೂಚರಂತಂ ಶತ್ರುಂ agrees |
| 434 | `(Ni. 1-[?]; as read "೩-೧೪")` → `(Ni. 2-15)` | SECOND-PASS Q1: Kannada p.434 ಗಭಸ್ತಿ ಶಬ್ದವು ರಶ್ಮಿ ನಾಮಗಳಲ್ಲಿಯೂ (ನಿ. ೨-೧೫) |
| 434 | `(Ṛ. Saṃ. 2-33-[?], as read "೨-೩೩-೧"; the first line is printed differently and I give it a` → `(Ṛ. Saṃ. 7-46-1.)` | SECOND-PASS Q1: Kannada p.434 ತಿಗ್ಮಾಯುಧಾಯ ಭರತಾ ಶೃಣೋತು ನಃ (ಋ. ಸಂ. ೭-೪೬-೧) |
| 435 | `(Ni. 1-[?]; as read "೧-೩೪"?)` → `(Ni. 2-24)` | SECOND-PASS Q1: Kannada p.435 ಕ್ಷದ್ಮ ಶಬ್ದವು ಉದಕನಾಮಗಳಲ್ಲಿಯೂ (ನಿ. ೨-೨೪) |
| 435 | `*ahir ayanād eti, ā-hanter vā*; *ahir ayam apīta iro 'hir eti*, *ahir meghaḥ nirhrasitopas` → `*ayanādahiḥ*, *āhaṃtītyahiḥ*; *ahirayanādetyaṃtarikṣe ayamapītaro ahiretasmādeva nirhrasit` | SECOND-PASS Q1: Kannada p.435 ಅಯನಾದಹಿಃ, ಆಹಂತೀತ್ಯಹಿಃ; ಅಹಿರಯನಾದೇತ್ಯಂತರಿಕ್ಷೇ ಅಯಮಪೀತರೋ ಅಹಿರೇತಸ್ಮಾದೇವ ನಿರ್ಹ್ರಸಿತೋಪಸರ್ಗ ಆಹಂತೀತಿ (sp_sanskrit.py) |
| 435 | `(Ni. 1-[?]; as read "೧-೧೦")` → `(Ni. 2-21)` | SECOND-PASS Q1: Kannada p.435 ಅಹಿ ಶಬ್ದವು ಮೇಘ ನಾಮಗಳಲ್ಲಿಯೂ (ನಿ. ೨-೨೧) |
| 435 | `(Ni. 1-[?], "೧-೩೪")` → `(Ni. 2-24)` | SECOND-PASS Q1: Kannada p.435 ಉದಕ ನಾಮಗಳಲ್ಲಿಯೂ (ನಿ. ೨.೨೪) (period for hyphen in print) |
| 435 | `which is naturally sharp [?]"` → `which is naturally sharp"` | SECOND-PASS Q2: Kannada p.435 ಸ್ವಭಾವದಿಂದಲೇ ಹರಿತನಾಗಿರುವ ವಜ್ರಾಯುಧ agrees |
| 435 | `(Ni. 1-[?]; "೧-೩೪")` → `(Ni. 2-24)` | SECOND-PASS Q1: Kannada p.435 ಓಜಶ್ಯಬ್ದವು ಉದಕ ನಾಮಗಳಲ್ಲಿ (ನಿ. ೨-೨೪) |
| 437 | `read from the image; small type, partly doubtful: [?]).*` → `read from the image; small type).*` | SECOND-PASS Q2: meta-remark on doubt marking; clause removed |
| 439 | `(Ni. 11-17 is said also of a certain name [?].` → `(Ni. 11-17) is said also as a proper name.` | SECOND-PASS Q1: Kannada p.439 ಋಭುರ್ವಿಶ್ವಾ ವಾಜ ಇತಿ (ನಿ. ೧೧-೧೭) ಅಂಕಿತನಾಮವಾಗಿಯೂ ಹೇಳಲ್ಪಟ್ಟಿದೆ |
| 439 | `(Ni. 1-[?]; as read "೧-೩೪")` → `(Ni. 2-24)` | SECOND-PASS Q1: Kannada p.439 ಅಕ್ಷಿತ ಶಬ್ದವು ಉದಕನಾಮಗಳಲ್ಲಿ (ನಿ. ೨-೨೪) |
| 440 | `(Ṛ. Saṃ. 8-68-1, as read "೮-೬೮-೧"; small type, doubtful: [?].)` → `(Ṛ. Saṃ. 8-6-1.)` | SECOND-PASS Q1: Kannada p.440 ತುವಿಕೂರ್ಮಿಮೃತೀಷಹಮಿಂದ್ರ ಶವಿಷ್ಠ ಸತ್ಪತೇ (ಋ. ಸಂ. ೮-೬-೧) |
| 440 | `(Ni. 11-[?]; as read "೧೧-೨")` → `(Ni. 5-3)` | SECOND-PASS Q1: Kannada p.440 ಊತಿರವನಾತ್ (ನಿ. ೫-೩) |
| 442 | `read from the image; small type, doubtful places [?]).*` → `read from the image; small type).*` | SECOND-PASS Q2: meta-remark on doubt marking; clause removed |
| 443 | `(Ni. 2-[?]; as read "೨-೩")` → `(Ni. 3-8)` | SECOND-PASS Q1: Kannada p.443 ಆಯವಃ ಎಂಬ ಪದವು ಮನುಷ್ಯನಾಮಗಳಲ್ಲಿ (ನಿ. ೩-೮) |
| 444 | `twenty-[?] names of happiness` → `twenty names of happiness` | SECOND-PASS Q1: Kannada p.444 ಇಪ್ಪತ್ತು ಸುಖನಾಮಗಳಲ್ಲಿ (ನಿ. ೩-೧೬) |
| 445 | `(Uṇ. 2-[?]) gives *kran*` → `(Uṇ. 1-182) gives *kran*` | SECOND-PASS Q1: Kannada p.445 ಸುಸೂಧಾಗೃಧಿಭ್ಯಃ ಕ್ರನ್ (ಉ. ಸೂ. ೧-೧೮೨) |
| 445 | `*ṇyat* [as read *enya*] by *āto yat* [?], with the Uṇādi sense` → `the Uṇādi suffix *enya*` | SECOND-PASS Q1: Kannada p.445 ಇದಕ್ಕೆ ಔಣಾದಿಕ ಏನ್ಯ ಪ್ರತ್ಯಯ (no sūtra āto yat in the Kannada) |
| 445 | `(Uṇ. 2-[?]) gives *ran*` → `(Uṇ. 1-186) gives *ran*` | SECOND-PASS Q1: Kannada p.445 ಋಜೇಂದ್ರ—(ಉ. ಸೂ. ೧-೧೮೬) |
| 446 | `read from the image; small type, partly doubtful: [?]).*` → `read from the image; small type).*` | SECOND-PASS Q2: meta-remark on doubt marking; clause removed |
| 448 | `(Ni. 1-[?]; as read "೩-೩೪")` → `(Ni. 2-24)` | SECOND-PASS Q1: Kannada p.448 ಮಹಃ ಎಂಬ ಶಬ್ದವು ಉದಕನಾಮಗಳಲ್ಲಿ (ನಿ. ೨-೨೪) |
| 449 | `(Kāśikā 6-3-21 [?], as read "೬-೩-೨೧-೨೪"?)` → `(Kāśikā 6-3-21-5)` | SECOND-PASS Q1: Kannada p.449 ದಿವೋದಾಸೇ ಷಷ್ಠ್ಯಾ ಅಲುಕ್ (ಕಾ. ೬-೩-೨೧-೫) |
| 449 | `the Uṇādi *ku* [?]` → `the Uṇādi *ku*` | SECOND-PASS Q2: Kannada p.449 ಇದಕ್ಕೆ ಔಣಾದಿಕ ಕು ಪ್ರತ್ಯಯ agrees |
| 451 | `read from the image; small type, a few doubtful places: [?]).*` → `read from the image; small type).*` | SECOND-PASS Q2: meta-remark on doubt marking; clause removed |
| 451 | `(Parāśara [?])` → `(Parāśara 3-25)` | SECOND-PASS Q1: Kannada p.451 ಪರಾಶರ… ರಣೇ ಯೋಽಭಿಮುಖೋ ಹತಃ (ಪರಾ. ೩-೨೫) |
| 451 | `(Ṛ. Saṃ. 8-96-13 [?])` → `(Ṛ. Saṃ. 8-96-13)` | SECOND-PASS Q2: Kannada p.451 ಋ. ೮-೯೬-೧೩ agrees |
| 452 | `*samatsu* is recorded among the names of battle (Ni. 2-[?]; as read "೨-೯")` → `*samatsu* is recorded among the names of battle (Ni. 3-9)` | SECOND-PASS Q1: Kannada p.452 ಸಮತ್ಸು ಎಂಬ ಪದವು ಸಂಗ್ರಾಮನಾಮಗಳಲ್ಲಿ (ನಿ. ೩-೯) |
| 452 | `*āji* is recorded among the names of battle (Ni. 2-[?]; as read "೨-೯")` → `*āji* is recorded among the names of battle (Ni. 3-9)` | SECOND-PASS Q1: Kannada p.453 ಆಜಿಶಬ್ದವು ಸಂಗ್ರಾಮನಾಮಗಳಲ್ಲಿ (ನಿ. ೩-೯) |
| 453 | `(Parāśara-smṛti 3-9, as read "೩-೩೨" [?])` → `(Parāśara-smṛti 3-25)` | SECOND-PASS Q1: Kannada p.453 ಪರಾಶರಸ್ಮೃತಿ ೩-೨೫ |
| 454 | `, in the region of the Yamunā [as read: *hariyuttaravuḍa*, doubtful: [?]],` → `, in the country through which it flows,` | SECOND-PASS Q1: Kannada p.454 ಅಂಶುಮತೀ ಎಂದು ಪ್ರಸಿದ್ಧವಾದ ನದಿಯು ಹರಿಯುತ್ತಿರುವ ದೇಶದಲ್ಲಿ; no Yamunā in the Kannada |
| 454 | `"the son of Īśvara [?]"` → `"the son of Īśvara"` | SECOND-PASS Q2: Kannada p.454 ಆರ್ಯಶಬ್ದಕ್ಕೆ ಈಶ್ವರಪುತ್ರನೆಂದು agrees |
| 456 | `(Uṇ. 3-[?]) gives the suffix` → `(Uṇ. 2-245) gives the suffix` | SECOND-PASS Q1: Kannada p.456 ಆರ್ತೇರ್ಗುಣಃ ಶೂಟ್ ಚ (ಉ. ಸೂ. ೨-೨೪೫) |
| 457 | `read from the image; small type, many places doubtful: [?]).*` → `read from the image; small type).*` | SECOND-PASS Q2: meta-remark on doubt marking; clause removed |
| 457 | `(Doubtful readings in the small type are marked [?]; the grammar tail` → `(The grammar tail` | SECOND-PASS Q2: meta-remark on doubt marking; clause removed, remark kept |
| 459 | `; the first line has a doubtful word at its start: *yamena* [?].` → `.` | SECOND-PASS Q2: Kannada p.459 ಯಮೇನ ದತ್ತಂ ತ್ರಿತ ಏನಮಾಯುನಕ್ … agrees; doubt clause removed |
| 459 | `(Ni. 2-[?]; as read "೨-೯")` → `(Ni. 3-9)` | SECOND-PASS Q1: Kannada p.459 ಓಜಸಾ ಪದಕ್ಕೆ ನಿರುಕ್ತದಲ್ಲಿ ಬಲನಾಮಗಳಲ್ಲಿ (ನಿ. ೩-೯) |
| 460 | `(Ṛ. Saṃ. 10-86-22, as read "೧೦-೮೬-೨೩" [?]; the small type is hard to read: [?].)` → `(Ṛ. Saṃ. 11-86-22.)` | SECOND-PASS Q1: Kannada p.460 (ಋ. ಸಂ. ೧೧-೮೬-೨೨), impossible Maṇḍala applied as printed, listed in open.tsv |
| 460 | `(Ni. 12-[?])` → `(Ni. 13-3)` | SECOND-PASS Q1: Kannada p.460 ಸರ್ವಸ್ಮಾದ್ಯ ಇಂದ್ರ ಉತ್ತರಸ್ತಮೇತದ್ರೂಮ ಆದಿತ್ಯಂ (ನಿ. ೧೩-೩) |
| 461 | `(Ni. 6-[?]; as read "೬-೧೪")` → `(Ni. 7-14)` | SECOND-PASS Q1: Kannada p.461 ತುರ್ವಣಿ ಶಬ್ದವು ತುರ್ವಣಿಸ್ತೂರ್ಣವನಿಃ (ನಿ. ೭-೧೪); the Sanskrit bhāṣya on p.457 has 6-14 (not touched) |
| 463 | `read from the image; small type, a few places doubtful: [?]).*` → `read from the image; small type).*` | SECOND-PASS Q2: meta-remark on doubt marking; clause removed |
| 465 | `(Uṇ. 2-[?]) gives *thak*` → `(Uṇ. 1-164) gives *thak*` | SECOND-PASS Q1: Kannada p.465 ಪಾತ್ಯ ತುದಿವಚಿ—(ಉ. ಸೂ. ೧-೧೬೪) |
| 465 | `(Kāśikā 6-3-21 [?], as read "೬-೩-೨೧-೨೫")` → `(Kāśikā 6-3-21-5)` | SECOND-PASS Q1: Kannada p.465 ದಿವೋದಾಸೇ ಷಷ್ಠ್ಯಾ ಅಲುಕ್ (ಕಾ. ೬-೩-೨೧-೫) |
| 466 | `read from the image; several letters doubtful [?]).**` → `read from the image).**` | SECOND-PASS Q2: meta-remark on doubt marking; clause removed |
| 466 | `is small and in several places unreadable to me; I give what is legible and mark [?]; the ` → `is small; the sense follows.)*` | SECOND-PASS Q2: meta-remark on doubt marking; clause shortened |
| 466 | `the next three for the Brāhmaṇācchaṃsin, and the last three for the Ukthāvāka [as read; th` → `the three beginning with the third for the Brāhmaṇācchaṃsin, and the three beginning with ` | SECOND-PASS Q1: Kannada p.466 ಆದ್ಯಾಸ್ತಿಸ್ರೋ ಮೈತ್ರಾವರುಣಸ್ಯ । ತೃತೀಯಾದ್ಯಾಸ್ತಿಸ್ರೋ ಬ್ರಾಹ್ಮಣಾಚ್ಛಂಸಿನಃ । ಪಂಚಮ್ಯಾದ್ಯಾಸ್ತಿಸ್ರೋಚ್ಚಾವಾಕಸ್ಯ |
| 466 | `(Ā. Sū. 8-1 [?]; as read "೮-೧೧" in one place and "೮-೧" in another)` → `(Ā. Sū. 7-11)` | SECOND-PASS Q1: Kannada p.466 ಷಷ್ಠೇಽಹನೀಂದ್ರಾಯ ಹಿ ದ್ಯೌರಸುರೋ ಅನಮ್ಮತೇತ್ಯೇವಮೇವ । ಆ. ೭-೧೧ (the 8-1 is the prakṣepaṇīya sūtra) |
| 466 | `(Ai. Ā. 5-1-1 [?])` → `(Ai. Ā. 5-1-1)` | SECOND-PASS Q2: Kannada p.466 ಐ. ಆ. ೫ ೧-೧; p.467 ಐ. ಆ. ೫-೧-೧ agrees |
| 468 | `read from the image; small type, a few places doubtful: [?]).*` → `read from the image; small type).*` | SECOND-PASS Q2: meta-remark on doubt marking; clause removed |
| 468 | `(Pā. Sū. 3-1-89 [?])` → `(Pā. Sū. 3-1-89)` | SECOND-PASS Q2: Kannada p.468 ಪಾ. ೩-೧-೮೯ agrees |
| 469 | `Ni. 1-[?]; as read "೧-೨೦" [?])` → `Ni. 2-21)` | SECOND-PASS Q1: Kannada p.469 ಹನ್ನೆರಡು ಅಹರ್ನಾಮಗಳಲ್ಲಿ (ನಿ. ೨-೨೧) |
| 470 | `so it is known (Ni. 3-[?]).` → `so it is known.` | SECOND-PASS S3: Kannada p.470 ವಿಜ್ಞಾಯತೇ ! ಎಂದು ವ್ಯಾಖ್ಯಾನ ಮಾಡಿರುವರು has no Nirukta number |
| 471 | `names of wealth (Ni. 2-[?]; as read "೨-೯")` → `names of wealth (Ni. 3-9)` | SECOND-PASS Q1: Kannada p.471 ದ್ಯುಮ್ನ ಶಬ್ದವು ಧನನಾಮಗಳಲ್ಲಿ (ನಿ. ೩-೯) |
| 471 | `(Ṛ. Saṃ. 5-3-[?] as read "೫-೩-೧-೧"? [?]; small type, doubtful.)` → `(Ṛ. Saṃ. 4-3-21-1)` | SECOND-PASS Q1: Kannada p.471 ಆ ರುದ್ರಾಸ ಇಂದ್ರವಂತಸ್ಸಜೋಷಸೋ … (ಋ. ಸಂ. ೪-೩-೨೧-೧) |
| 473 | `read from the image; small type, doubtful places [?]).*` → `read from the image; small type).*` | SECOND-PASS Q2: meta-remark on doubt marking; clause removed |
| 475 | `(Ṛ. Saṃ. 1-[?]-[?], as read "೧-೭-೭" [?]; small type.)` → `(Ṛ. Saṃ. 1-7-6)` | SECOND-PASS Q1: Kannada p.475 ತುಂಜೇತುಂಜೇ ಯ ಉತ್ತರೇ ಸ್ತೋಮಾ ಇಂದ್ರಸ್ಯ ವಜ್ರಿಣಃ (ಋ. ಸಂ. ೧-೭-೬) |
| 475 | `(Ni. 1-[?]; "೧-೩೪")` → `(Ni. 2-24)` | SECOND-PASS Q1: Kannada p.475 ನೂರೊಂದು ಉದಕನಾಮಗಳಲ್ಲಿ (ನಿ. ೨-೨೪) |
| 476 | `(Ni. 2-[?]; as read "೨-೯")` → `(Ni. 3-9)` | SECOND-PASS Q1: Kannada p.476 ಶೂಷ ಶಬ್ದವು ಇಪ್ಪತ್ತೆಂಟು ಬಲನಾಮಗಳಲ್ಲಿ (ನಿ. ೩-೯) |
| 476 | `(Ni. 2-[?]; as read "೨-೮")` → `(Ni. 3-8)` | SECOND-PASS Q1: Kannada p.476 ಆಯವಃ … ಮನುಷ್ಯನಾಮಗಳಲ್ಲಿ (ನಿ. ೩-೮) |
| 477 | `[as read: *iṇ sarvadhātubhyaḥ*, Uṇ. 4-[?]] gives *iṇ*` → `gives *in*` | SECOND-PASS Q1: Kannada p.477 ಇನ್ ಸರ್ವಧಾತುಭ್ಯಃ ಎಂಬುದರಿಂದ ಇನ್ ಪ್ರತ್ಯಯ; no Uṇādi number |
| 479 | `; very small and dense type — I transcribe the opening and then give the sense; doubtful p` → `; very small and dense type — I transcribe the opening and then give the sense).*` | SECOND-PASS Q2: meta-remark on doubt marking; clause removed |
| 480 | ` (Taittirīya [?]);` → `;` | SECOND-PASS S3: Kannada p.479/481 gives only “ಜಾಯಾಪತೀ ಅಗ್ನಿಮಾದಧೀಯಾತಾಂ” as a Śruti saying, no work named |
| 481 | `(Tai. Saṃ. 1-1-10-1 [?])` → `(Tai. Saṃ. 1-1-10-1)` | SECOND-PASS Q2: Kannada p.481 (ತೈ ಸಂ. ೧-೧-೧೦-೧) agrees |
| 482 | `samyaggamanuṣṭhitavantau āviṣkaroṣi niṣkṛṣya* [?]` → `samyaganuṣṭhitavaṃtau iti niścinoṣi*` | SECOND-PASS Q1: Kannada p.482 ಯದ್ವಾ ಸಮ್ಯಗನುಷ್ಠಿತವಂತೌ ಇತಿ ನಿಶ್ಚಿನೋಷಿ (sp_sanskrit.py) |
| 484 | `, a few places doubtful: [?] — notably the grammatical clause on *sasahānaḥ*. Sense:` → `. Sense:` | SECOND-PASS Q2: meta-remark on doubt marking; clause removed, Sense stays |
| 486 | `(Ni. 2-[?]; as read "೨-೮")` → `(Ni. 3-8)` | SECOND-PASS Q1: Kannada p.486 ಪೂರವಃ ಎಂಬ ಪದವು ಮನುಷ್ಯನಾಮಗಳಲ್ಲಿ (ನಿ. ೩-೮) |
| 487 | `after the *yañluk*-ending [?]` → `after the *yañluk*-ending` | SECOND-PASS Q2: Kannada p.487 ಯಜ್ಲುಗಂತದ ಮೇಲೆ agrees |
| 490 | `names of battle (Ni. 2-[?]; as read "೨-೯")` → `names of battle (Ni. 3-9)` | SECOND-PASS Q1: Kannada p.490 ಪೃತನಾ ಶಬ್ದವು ನಲವತ್ತಾರು ಸಂಗ್ರಾಮ ನಾಮಗಳಲ್ಲಿ (ನಿ. ೩-೯) |
| 491 | ` (Ni. 4-[?]).` → `.` | SECOND-PASS S3: Kannada p.491 ಅನ್ಯಃ ಎಂಬ ಪದಕ್ಕೆ ನಾನೇಯಃ ಎಂದು ಅರ್ಥ has no Nirukta number |
| 491 | `(Ni. 2-[?]; as read "೨-೯")` → `(Ni. 3-9)` | SECOND-PASS Q1: Kannada p.491 ಶ್ರವಸ್ ಶಬ್ದವು ನಿರುಕ್ತಕಾರರಿಂದ ಧನನಾಮಗಳಲ್ಲಿ (ನಿ. ೩-೯) |
| 491 | `(Ṛ. Saṃ. 2-1-11-1; 6-[?])` → `(Ṛ. Saṃ. 2-1-11-1; Ni. 9-11)` | SECOND-PASS Q1: Kannada p.491 ಯಶಸ್ಸು ಎಂಬ ಅರ್ಥದಲ್ಲಿಯೂ (ಋ. ಸಂ. ೨-೧-೧೧-೧; ನಿ. ೯-೧೧) |
| 491 | `(Ṛ. Saṃ. 5-[?]-[?], as read "೫-೬೨-೩" [?]; same Ṛk as on p. 353.)` → `(Ṛ. Saṃ. 6-37-3.)` | SECOND-PASS Q1: Kannada p.491 ಅಭಿ ಶ್ರವ ಋಜ್ಯಂತೋ ವಹೇಯುಃ (ಋ. ಸಂ. ೬-೩೭-೩); p.353 English cites the same |
| 492 | `*sarvanāmno dve vācye* (Pā. Sū. 8-1-12 [?])` → `*sarvanāmno dve vācye*` | SECOND-PASS S3: Kannada p.492 ಸರ್ವನಾಮ್ನೋ ದ್ವೇ ವಾಚ್ಯೇ has no sūtra number |
| 493 | `*ru* [?];` → `*jha*;` | SECOND-PASS Q1: Kannada p.493 ಪ್ರಥಮಪುರುಷ ಬಹುವಚನದಲ್ಲಿ ಝ ಪ್ರತ್ಯಯ (sp_sanskrit.py) |
| 494 | `read from the image; small type, a few places doubtful: [?]).*` → `read from the image; small type).*` | SECOND-PASS Q2: meta-remark on doubt marking; clause removed |
| 498 | `read from the image; small type, a few places doubtful: [?]).*` → `read from the image; small type).*` | SECOND-PASS Q2: meta-remark on doubt marking; clause removed |
| 499 | `(Ni. 2-[?]; as read "೨-೮")` → `(Ni. 3-8)` | SECOND-PASS Q1: Kannada p.499 ಮರ್ತ್ಯ ಶಬ್ದವು ಮನುಷ್ಯನಾಮಗಳಲ್ಲಿ (ನಿ ೩-೮) |

### 2026-11-27 second pass, batch m500-579.tsv
| page | old → new | why |
|---|---|---|
| 502 | `small type, doubtful places [?])` → `small type)` | SECOND-PASS Q2: meta-remark on doubt marking; clause removed |
| 503 | `read from the image; doubtful places [?].)` → `read from the image.)` | SECOND-PASS Q2: meta-remark on doubt marking; clause removed |
| 504 | `(Ni. 2-[?]; as read "೨-೯")` → `(Ni. 3-6)` | SECOND-PASS Q1: Kannada p.504 ಪೃತನಾ ಶಬ್ದವು (ನಿ. ೩. ೬) ಸಂಗ್ರಾಮನಾಮಗಳಲ್ಲಿ |
| 505 | `(Ṛ. Saṃ. 6-24-3, as read "೬-೨೪-೫"; the second line has a doubtful word at its start: [?].)` → `(Ṛ. Saṃ. 6-24-3.)` | SECOND-PASS Q1: Kannada p.505 (ಋ. ಸಂ. ೬-೨೪-೩) agrees with the English; doubt clause removed |
| 508 | `without asking [? the way]` → `without concealment` | SECOND-PASS Q1: Kannada p.508 ಸ್ವಯಮೇವಾಪ್ರಚ್ಛನ್ನತೇನಾಗತೇ: apracchanna = not concealed |
| 509 | `Parāśara-smṛti 3-23 [?], as read "೩-೨೩"` → `Parāśara-smṛti 3-25` | SECOND-PASS Q1: Kannada p.509 (ಪರಾಶರಸ್ಮೃತಿ ೩-೨೫) |
| 511 | `(Ṛ. Saṃ. [?], as read "೮-೪-[?]" [?]; the reference is not clear; small type. The line is g` → `Citing this Ṛk, he` | SECOND-PASS S3: Kannada p.511 gives no reference after the verse ತ್ವಾಮಿಂದ್ರ ಮತಿಭಿಃ…; number removed with its marks |
| 512 | `that which brings about being [?],` → `that which gives delight,` | SECOND-PASS Q1: Kannada p.512 ಭವದ್ರಮಯತೀತಿ ವಾ … ಸಂತೋಷಕರವಾದುದು |
| 514 | `small type, doubtful places [?])` → `small type)` | SECOND-PASS Q2: meta-remark on doubt marking; clause removed |
| 516 | `(Ni. 2-[?]; as read "೨-೯")` → `(Ni. 3-9)` | SECOND-PASS Q1: Kannada p.516 ಎಂಬ ಪದವು ಅನ್ನನಾಮಗಳಲ್ಲಿ (ನಿ. ೩-೯) |
| 516 | `(Ni. 1-[?]; as read "೧-೧೪"?)` → `(Ni. 2-14)` | SECOND-PASS Q1: Kannada p.516 ಋತ ಶಬ್ದವು ಉದಕನಾಮಗಳಲ್ಲಿ (ನಿ. ೨-೧೪) |
| 518 | `(Ṛ. Saṃ. 3-[?]-[?]; 3-[?]; 5-[?]; 8-[?]…: the list of numerals is small and not reliably r` → `(Ṛ. Saṃ. 2-18-3; 2-20-3; 3-53-5; 4-17-18; 4-23-6; 6-21-5; 6-45-1, 6; 7-21-9; 8-4-7; 8-45-1` | SECOND-PASS Q1: Kannada p.518 ಋ. ಸಂ. ೨-೧೮-೩; ೨-೨೦-೩; ೩-೫೩-೫; ೪-೧೭-೧೮; ೪-೨೩-೬; ೬-೨೧-೫; ೬-೪೫-೧, ೬; ೭-೨೧-೯; ೮-೪-೭; ೮-೪೫-೧; ೮-೫೦-೧೧; ೪-೧೭-೧೭; ೮-೮೭-೧೧; ೮-೮೧-೩೨ ಇತ್ಯಾದಿ |
| 519 | `a discrepancy in the print, not resolved here: [?].` → `a discrepancy in the print.` | SECOND-PASS Q2: meta-remark on doubt marking; clause removed |
| 520 | `small type, a few places doubtful: [?])` → `small type)` | SECOND-PASS Q2: meta-remark on doubt marking; clause removed |
| 521 | `Ṛ. Saṃ. 10-[?]-[?] (as read "೧೦-೧೦೨-೩" [?]), etc.` → `Ṛ. Saṃ. 10-108-8, 10, etc.` | SECOND-PASS Q1: Kannada p.522 ಋ. ಸಂ. ೧೦-೧೦೮-೮,೧೦ ಮೊದಲಾದ ಋಕ್ಕುಗಳಲ್ಲಿ |
| 522 | `Ṛ. Saṃ. 1-[?]-[?]; 8-[?]-[?]; 3-[?]-[?]; Bṛhad-devatā [?], Aitareya Brāhmaṇa [?], Pañcaviṃ` → `Ṛ. Saṃ. 1-45-3; 1-139-9; 3-31-7; Chāndogya Upaniṣad 1-2-10; Atharva-veda 18-4-8; Pañcaviṃś` | SECOND-PASS Q1: Kannada p.522 ಋ. ಸಂ. ೧. ೪೫-೩; ೧-೧೩೯-೯; ೩-೩೧-೭; ಛಾ. ಉ. ೧-೨-೧೦; ಅ. ವೇ ೧೮-೪-೮; ಪಂಚವಿಂಶಬ್ರಾಹ್ಮಣ ೨೦-೧೧-೧; ತೈ. ಸಂ. ೭-೧-೪-೧ |
| 524 | `small type, a few places doubtful: [?])` → `small type)` | SECOND-PASS Q2: meta-remark on doubt marking; clause removed |
| 527 | `(Ni. 2-[?]; as read "೨-೯")` → `(Ni. 3-9)` | SECOND-PASS Q1: Kannada p.527 ಬಲನಾಮಗಳಲ್ಲಿ ಪಠಿತವಾಗಿರುವುದರಿಂದ (ನಿ. ೩-೯) ಬಾಧವೆಂದರೆ ಬಲ |
| 527 | `(Ni. 2-[?]; as read "೨-೧")` → `(Ni. 3-1)` | SECOND-PASS Q1: Kannada p.527 ಧೀ ಶಬ್ದವು ಕರ್ಮನಾಮಗಳಲ್ಲಿ ಪಠಿತವಾಗಿರುವುದರಿಂದ (ನಿ ೩-೧) |
| 529 | `given as printed [?];` → `given as printed;` | SECOND-PASS Q2: Kannada p.529 Saṃhitā ದೂರೇ ಚತ್ತಾಯ ಛಂತ್ಸದ್ಗಹನಂ ಯದಿನಕ್ಷತ್ agrees with the English |
| 529 | `-grahas [?], when` → `-grahas, when` | SECOND-PASS Q2: Kannada p.529 ಮಾನಸಗ್ರಹಭಕ್ಷಣಾನಂತರಂ agrees |
| 529 | `section 'gārhapatye juṣṭastīti' [?]:` → `section 'gārhapatye juhvatīti':` | SECOND-PASS Q1: Kannada p.529 ಗಾರ್ಹಪತ್ಯೇ ಜುಹ್ವತೀತಿ ಖಂಡೇ (sp_sanskrit.py) |
| 529 | `(Ā. Sū. 8-13." The reading of this small-type sūtra reference is doubtful: [?].)*` → `(Ā. Sū. 8-13)".)*` | SECOND-PASS Q2: Kannada p.529 ಋ. ೮-೧೩: number agrees; doubt clause removed |
| 531 | `1-132-6; 1-[?]-[?]; 3-[?]-[?]; and` → `1-122-3; 1-132-6; 3-53-1; and` | SECOND-PASS Q1: Kannada p.531 ಋ. ಸಂ. ೧-೧೨೨-೩; ೧-೧೩೨-೬; ೩-೫೩-೧ |
| 531 | `(Ni. 1-[?] and 10-10; as read "೧-೩೧", "೧೦-೧೦")` → `(Ni. 3-21 and 10-10)` | SECOND-PASS Q1: Kannada p.531 (ನಿ. ೩-೨೧ ಮತ್ತು ನಿ. ೧೦-೧೦) |
| 531 | `Tai. Saṃ. 5-84-1, "೩-೨-೧೧-೨" [?].)` → `Tai. Saṃ. 2-2-12-2.)` | SECOND-PASS Q1: Kannada p.531 (ಋ. ಸಂ. ೫-೮೪-೧, ತೈ. ಸಂ ೨-೨-೧೨-೨) |
| 532 | `(Ni. 2-[?]; as read "೨-೯")` → `(Ni. 3-9)` | SECOND-PASS Q1: Kannada p.532 ಪೃತನಾ ಎಂದರೆ ಯುದ್ಧವೆಂದರ್ಥವು (ನಿ ೩-೯) |
| 534 | `read from the image; several letters doubtful [?])` → `read from the image)` | SECOND-PASS Q2: meta-remark on doubt marking; clause removed |
| 534 | `(Ṛgvidhāna 1-25, as read "೧-೩೨" [?])` → `(Ṛgvidhāna 1-25)` | SECOND-PASS Q1: Kannada p.534 (ಋಗ್ವಿಧಾನ. ೧-೨೫) |
| 536 | `(Pā. [?], number not legible to me)` → `(Pā. 7-1-6)` | SECOND-PASS Q1: Kannada p.536 ಶೀಜೋ ರುಟ್ । ಪಾ. ೭-೧-೬ (p.540 grammar prints ೭-೧-೯; the Sāyaṇa-block reference is the one cited here) |
| 536 | ` The wording of the second half is partly doubtful [?].)*` → `)*` | SECOND-PASS Q2: meta-remark on doubt marking; clause removed |
| 536 | `(Ni. 3-22, as read "೩-೩೦" [?])` → `(Ni. 3-22)` | SECOND-PASS Q1: Kannada p.536 ರೋದಸೀ ಎಂದರೆ ದ್ಯಾವಾ ಪೃಥಿವಿಗಳು (ನಿ. ೩-೨೨) |
| 537 | `(Ni. 11-50, as read "೧೧-೩೦" [?])` → `(Ni. 11-50)` | SECOND-PASS Q1: Kannada p.537 ರುದ್ರಪತ್ನಿಯೆಂದೂ (ನಿ. ೧೧-೫೦) |
| 538 | `(Ni. 3-5, as read "೩-೨೩" [?]) [the quotation's wording partly doubtful, [?]] —` → `(Ni. 3-5) —` | SECOND-PASS Q1: Kannada p.538 ಶ್ಮಶಾನಂ ಶ್ಮಶಯನಂ (ನಿ. ೩-೫); meta doubt clause removed |
| 539 | `*prādīnāṃ hrasvaḥ* [?] (Pā. [?])` → `*pvādīnāṃ hrasvaḥ* (Pā. Sū. 7-3-80)` | SECOND-PASS Q1: Kannada p.539 ಪ್ವಾದೀನಾಂ ಹ್ರಸ್ವಃ (ಪಾ. ಸೂ. ೭-೩-೮೦); IAST by sp_sanskrit.py |
| 541 | `; the closing grammatical citations are doubtful [?].)` → `.)` | SECOND-PASS Q2: meta-remark on doubt marking; clause removed |
| 541 | `pervading, spread out [?];` → `pervading, spread out;` | SECOND-PASS Q2: Kannada p.541 ವೇಷ್ಟನಶೀಲೇನ ಸರ್ವವ್ಯಾಪ್ತೇನ … ಅತಿವಿಸ್ತೃತೇನೇತ್ಯರ್ಥಃ agrees |
| 542 | `(Ni. 2-21, as read "೨-೩೦" [?])` → `(Ni. 2-21)` | SECOND-PASS Q1: Kannada p.542 ಅದ್ರಿಶಬ್ದವು ಮೇಘನಾಮಗಳಲ್ಲಿ (ನಿ. ೨-೨೧) |
| 542 | `(Ṛ. Saṃ. 7-[?]-[?], as read "೭-೧೯-೩೨" [?]; the Saṃhitā reading of the first line is doubtf` → `(Ṛ. Saṃ. 7-18-21.)` | SECOND-PASS Q1: Kannada p.542 (ಋ. ಸಂ. ೭-೧೮-೨೧); doubt clause removed |
| 543 | `(Pā. 8-[?]-[?], as read "೮-೩-೧೮")` → `(Pā. Sū. 8-2-15)` | SECOND-PASS Q1: Kannada p.543 ಛಂದಸೀರಃ (ಪಾ. ಸೂ. ೮-೨-೧೫) |
| 543 | `(Uṇ. [?])` → `(Uṇ. Sū. 4-530)` | SECOND-PASS Q1: Kannada p.543 ಖರ್ಜಪಿಞ್ಚಾದಿಭ್ಯ ಊರೋಲಟೌ (ಉ. ಸೂ. ೪-೫೩೦) applied as printed (Sāyaṇa block p.541 has ಉ. ೪-೯೦) |
| 544 | `wretched, [fit for those who have gone to their destruction] [?].")` → `wretched, to be reached by the dead.")` | SECOND-PASS Q1: Kannada p.544 ಅರ್ಮಕೇ ಕುತ್ಸಿತೇ ಗತಾಸುಭಿರರಣೀಯೇ / ಮೃತರಾದವರ … |
| 545 | `(Ni. 2-[?], as read "೨-೯" [?])` → `(Ni. 3-9)` | SECOND-PASS Q1: Kannada p.545 ಶರ್ಧ ಶಬ್ದವು ಬಲನಾಮಗಳಲ್ಲಿ ಪಠಿತವಾಗಿದೆ. (ನಿ. ೩-೯) |
| 545 | `does not give *luk* [?];` → `does not give *luk*;` | SECOND-PASS Q2: Kannada p.545 ಅತೋಹೇಃ ಎಂಬುದರಿಂದ ಹಿಗೆ ಲುಕ್ ಬರುವುದಿಲ್ಲ agrees |
| 547 | `*ṛta idhātoḥ* [as read?] / *ṛta ut* [?] — the *ṛ* becomes *ra* [as read];` → `*acira ṛtaḥ* — the *ṛ* becomes *ra*;` | SECOND-PASS Q1: Kannada p.547 ಅಚಿರ ಋತಃ ಎಂಬುದರಿಂದ ಋಕಾರಕ್ಕೆ ರೇಫಾದೇಶ (IAST by sp_sanskrit.py) |
| 547 | `a root used only in the sūtra [?];` → `a root used only in the sūtra;` | SECOND-PASS Q2: Kannada p.547 ಸೂತ್ರಮಾತ್ರಪ್ರಯುಕ್ತವಾದ ಧಾತು agrees |
| 548 | `; several words doubtful [?].)` → `.)` | SECOND-PASS Q2: meta-remark on doubt marking; clause removed |
| 548 | `as in the Naighaṇṭuka passage [?])` → `as in the Naighaṇṭuka passage)` | SECOND-PASS Q2: Kannada p.548 ಅಂಭೃಣ ಇತಿ ಮಹನ್ನಾಮ ಅಂಭೃಣೋ ಮಾಹಿನ ಇತಿ ತತ್ರ ಪಾಠಾತ್ agrees |
| 548 | `(red-spiked [?])` → `(dusky red)` | SECOND-PASS Q1: Kannada p.548 ಪಿಶಂಗಭೃಷ್ಟಿಂ-ಮಾಸಲುಕೆಂಪಾಗಿರುವ |
| 548 | `(huge, or with a hard, thick, tongue [?])` → `(very big, or loudly screeching)` | SECOND-PASS Q1: Kannada p.548 ಭಾವಾರ್ಥ (ಬಹಳ ದೊಡ್ಡದಾದ ಅಥವಾ ಘಟ್ಟಿಯಾದ ಕಿರುಚುತ್ತಿರುವ) |
| 549 | `twenty-odd [?] names` → `twenty-five names` | SECOND-PASS Q1: Kannada p.549 ಇಪ್ಪತ್ತೈದು ಮಹನ್ನಾಮಗಳಲ್ಲಿ |
| 550 | `"the pot-bellied" [refs] — as "swellings (mounds) made of pots" [?] they compare [refs];` → `he has eggs (Ṛ. Saṃ. 6-40-10, 11), that is, young ones hatched from eggs (compare 10-12-11` | SECOND-PASS Q1: Kannada p.550 ಮೊಟ್ಟೆಗಳಿವೆ (೬-೪೦-೧೦, ೧೧). ಎಂದರೆ ಮೊಟ್ಟೆಗಳಿಂದಾದ ಮರಿಗಳು (೧೦-೧೨-೧೧ ನ್ನು ಹೋಲಿಸಿ) |
| 551 | `a suitable *yojana* for Pipru [?]` → `a warrior matched to Pipru` | SECOND-PASS Q1: Kannada p.551 ಪಿಪುವಿಗೆ ಅನುರೂಪನಾದ ಯೋಧನನ್ನು ಆರ್ಯನು ಕಂಡನು |
| 551 | `the black Pipru, a kind of dark-coloured [?], to Ṛjiśvan` → `Pipru, who had the form of a wild beast, to Ṛjiśvan` | SECOND-PASS Q1: Kannada p.551 ಕಾಡುಮೃಗರೂಪನಾದ ಪಿಪುವನ್ನು ಇಂದ್ರನು ಋಜಿಶ್ವನಿಗೆ ಒಪ್ಪಿಸಿದನು |
| 552 | `"one who goes in the water" [?]` → `"one who shines"` | SECOND-PASS Q1: Kannada p.552 ವರ್ಚಿ ಎಂದರೆ ಹೊಳೆಯುತ್ತಿರುವವನು |
| 552 | `7-104 and 10-85 [as read, [?]]` → `7-104 and 10-87` | SECOND-PASS Q1: Kannada p.552 ೭-೧೦೪ ಮತ್ತು ೧೦-೮೭ ನೆಯ ಸೂಕ್ತಗಳಲ್ಲಿ |
| 552 | `dog, owl, cuckoo, [*kokila* [?]] and other birds` → `dog, vulture, owl and other birds` | SECOND-PASS Q1: Kannada p.552 ನಾಯಿ, ರಣಹದ್ದು, ಗೂಬೆ ಮತ್ತು ಇತರ ಪಕ್ಷಿಗಳ ರೂಪಗಳಿರುವವು |
| 553 | `toes without feet [?]` → `no toes` | SECOND-PASS Q1: Kannada p.553 ಬೆರಳುಗಳಿಲ್ಲ |
| 553 | `cause omission and confusion [?]` → `cause omissions and faults` | SECOND-PASS Q1: Kannada p.553 ಲೋಪದೋಷಗಳನ್ನುಂಟುಮಾಡುತ್ತವೆ |
| 554 | `Agni is prayed to burn, to drive away or to destroy those who play with fields [?], and th` → `Agni, who dispels darkness and is the lord of the sacrifice, is their sworn enemy; Agni hi` | SECOND-PASS Q1: Kannada p.554 ಕತ್ತಲನ್ನು ಹೋಗಲಾಡಿಸುವವನೂ, ಯಾಗಕ್ಕೆ ಯಜಮಾನನೂ ಆದ ಅಗ್ನಿಗೂ ಇವರಿಗೂ ಬದ್ಧದ್ವೇಷ; ಇವರನ್ನು ದಹಿಸು, ಓಡಿಸು ಅಥವಾ ನಾಶಮಾಡು … (೧೦-೮೭-೩, ೬) |
| 554 | `having a crest [?], and` → `having a crest, and` | SECOND-PASS Q2: Kannada p.554 ಹರಿದ್ರವರ್ಣದ ಕಿರೀಟವುಳ್ಳ agrees |
| 554 | `a class of Piśācas who eat the flesh of women [?];` → `a class of corpse-eating Piśācas;` | SECOND-PASS Q1: Kannada p.554 ಆದುದರಿಂದ ಅವೂ ಒಂದು ಜಾತಿಯ ಹೆಣ ತಿನ್ನುವ ಪಿಶಾಚಿಗಳು |
| 556 | `given as in the Saṃhitā with [?].)*` → `given as in the Saṃhitā.)*` | SECOND-PASS Q2: meta-remark on doubt marking; mark removed |
| 556 | `p. 557; because the print is small and several words here are doubtful I mark the whole pa` → `p. 557. Sense so far:` | SECOND-PASS Q2: meta-remark on doubt marking; clause removed |
| 556 | `the great Vṛtra [?];` → `the great Vṛtra;` | SECOND-PASS Q2: Kannada p.556 Sāyaṇa ಮಹಾಂತಂ ವೃತ್ರಂ agrees |
| 556 | `in the form of a *trasa*-man [?]` → `in the form of Tvaṣṭṛ (*tvaṣṭarūpeṇa*)` | SECOND-PASS Q1: Kannada p.556 ಸ ಚ ತ್ವಷ್ಟರೂಪೇಣ (IAST by sp_sanskrit.py) |
| 557 | `; doubtful words marked [?].)` → `.)` | SECOND-PASS Q2: meta-remark on doubt marking; clause removed |
| 557 | ` The printed passage is partly compressed and some words are doubtful [?].)*` → `)*` | SECOND-PASS Q2: meta-remark on doubt marking; clause removed |
| 558 | `are to be used by the Hotṛ's assistant, the Acchāvāka [?], when reciting` → `are to be recited when reciting` | SECOND-PASS Q1: Kannada p.558 ಈ ಸೂಕ್ತದ ಮೊದಲಿನ ಎರಡು ಋಕ್ಕುಗಳನ್ನು ಪಠಿಸಬೇಕೆಂದು: Kannada names no Acchāvāka |
| 558 | `(Āś. [refs] [?])` → `(Āś. 8-1)` | SECOND-PASS Q1: Kannada p.558 ಎಂಬ ಸೂತ್ರದಿಂದ ವಿವೃತವಾಗಿರುವುದು (ಆ. ೮-೧) |
| 558 | `(Ni. 1-[?], as read "೨-೩೦")` → `(Ni. 2-21)` | SECOND-PASS Q1: Kannada p.558 ಅದ್ರಿಶಬ್ದವು ಮೇಘನಾಮಗಳಲ್ಲಿಯೂ (ನಿ. ೨-೨೧) |
| 559 | `(Ni. 1-[?], as read "೧-೩")` → `(Ni. 2-1)` | SECOND-PASS Q1: Kannada p.559 ಪಠಿತವಾಗಿರುವುದರಿಂದ (ನಿ. ೨-೧) ಭೂಮಿಯೆಂದರ್ಥವು |
| 559 | `Ṛ. Saṃ. 1-[?]-[?] [as read "೧-೯೫-೧" [?]]` → `Ṛ. Saṃ. 1-95-1` | SECOND-PASS Q1: Kannada p.559 ಋ. ಸಂ. ೧-೯೫-೧ ರಲ್ಲಿ ಹೇಳಿರುವ ಪೂರ್ವೇತಿಹಾಸ |
| 559 | `(Ṛ. Saṃ. 1-[?]-[?], as read "೧-೯೫-೨" [?]. The itihāsa passage is partly illegible in the s` → `(Ṛ. Saṃ. 1-95-5.)` | SECOND-PASS Q1: Kannada p.559 (ಋ. ಸಂ. ೧-೯೫-೫) after ಉಭೇ ತ್ವಷ್ಟುರ್ಬಿಭ್ಯತುಃ; doubt clause removed |
| 560 | `(Ṛ. Saṃ. 1-31-3; the Saṃhitā text of this quotation is doubtful in several letters [?].)` → `(Ṛ. Saṃ. 1-31-3.)` | SECOND-PASS Q2: Kannada p.560 (ಋ. ಸಂ. ೧-೩೧-೩) agrees; doubt clause removed |
| 560 | `(Ni. 2-[?], as read "೨-೯")` → `(Ni. 3-9)` | SECOND-PASS Q1: Kannada p.560 ಇಪ್ಪತ್ತೆಂಟು ಬಲನಾಮಗಳಲ್ಲಿ ಪಠಿತವಾಗಿರುವುದರಿಂದ (ನಿ. ೩-೯) |
| 561 | `it being a *para* [?], *an* is substituted for the stem` → `when it follows, *av* is substituted for the stem` | SECOND-PASS Q1: Kannada p.561 ಅದು ಪರವಾದಾಗ ಪ್ರಕೃತಿಗೆ ಅವ್ ಎಂಬ ಆದೇಶ ಬರುತ್ತದೆ (IAST by sp_sanskrit.py) |
| 563 | `; doubtful words marked [?].)` → `.)` | SECOND-PASS Q2: meta-remark on doubt marking; clause removed |
| 563 | `(Āś. [refs] [?])` → `(Āś. 8-1)` | SECOND-PASS Q1: Kannada p.563 ಪೌಂಸ್ಯಾ । ಆ. ೮-೧ । ಇತಿ |
| 564 | `(Āś. [refs] [?])` → `(Āś. 8-1)` | SECOND-PASS Q1: Kannada p.564 ವಿವೃತವಾಗಿರುವುದು (ಆ. ೮-೧) |
| 564 | `a house in which all stay for sleep [?],` → `a house in which all dwell,` | SECOND-PASS Q1: Kannada p.564 ಸಮಸ್ತರೂ ವಾಸಮಾಡುವ … ಗೃಹ |
| 564 | `(Ni. 2-[?], as read "೨-೭")` → `(Ni. 3-9)` | SECOND-PASS Q1: Kannada p.564 ವಾಜವೆಂದರೆ ಅನ್ನವು ಅಥವಾ ಆಹಾರವು (ನಿ. ೩-೯) |
| 566 | `read from the image; doubtful letters [?])` → `read from the image)` | SECOND-PASS Q2: meta-remark on doubt marking; clause removed |
| 566 | `The last ṛk, with the fourth pāda of sixteen [?] syllables *tvaṃ no vāyo*, is` → `The last ṛk, *tvaṃ no vāyo*, of sixty-four syllables, is` | SECOND-PASS Q1: Kannada p.566 ತ್ವಂ ನೋ ವಾಯೋ ಎಂಬ ಅರವತ್ತುನಾಲ್ಕು ಅಕ್ಷರಗಳುಳ್ಳ ಕೊನೆಯ ಋಕ್ಕು |
| 566 | `Varga 24 [as read, [?]]` → `Varga 23` | SECOND-PASS Q1: Kannada p.566 ವರ್ಗ—೨೩ |
| 567 | `; doubtful words marked [?].)` → `.)` | SECOND-PASS Q2: meta-remark on doubt marking; clause removed |
| 569 | `(Ni. 10-22, as read "೧೦-೩" [?].)` → `(Ni. 10-2.)` | SECOND-PASS Q1: Kannada p.569 ಕಮನ್ಯಂ ಮಧ್ಯಮಾದೇವಮವಕ್ಷ್ಯತ್ । (ನಿ. ೧೦-೨) |
| 569 | `(Ṛ. Saṃ. 10-[?]-[?], as read "೧೦-೯೪-೪" [?].)` → `(Ṛ. Saṃ. 1-140-4.)` | SECOND-PASS Q1: Kannada p.569 ಅಶವಃ ॥ (ಋ. ಸಂ. ೧-೧೪೦-೪) ಎಂಬ ಋಕ್ಕಿನಲ್ಲಿ ಜುವಃ … |
| 570 | `(Ni. 2-[?], as read "೨-೯" [?])` → `(Ni. 3-9)` | SECOND-PASS Q1: Kannada p.570 ಪ್ರಯಃ-ಅಂಧಃ, ವಾಜಃ ಇತ್ಯಾದ್ಯನ್ನ ನಾಮಗಳಲ್ಲಿ ಪಠಿಸಿದೆ (೩-೯) |
| 570 | `(Ni. 2-[?], as read "೨-೧೫" [?])` → `(Ni. 7-15)` | SECOND-PASS Q1: Kannada p.570 ಊರ್ಧ್ವ ಉಚ್ಚ್ರಿತೋ ಭವತಿ । (ನಿ. ೭-೧೫) |
| 571 | `(Ṛ. Saṃ. 7-39-2 [as read]; the first words are doubtful in several letters [?].)` → `(Ṛ. Saṃ. 7-39-2.)` | SECOND-PASS Q2: Kannada p.571 (ಋ. ಸಂ. ೭-೩೯-೨) agrees; doubt clause removed |
| 571 | `(Ni. 5-28, as read "೫-೨೫" [?])` → `(Ni. 5-28)` | SECOND-PASS Q1: Kannada p.571 ನಿಯುತ ವೆಂದು ಹೆಸರು ಪ್ರಸಿದ್ಧವಾಗಿದೆ (ನಿ. ೫-೨೮) |
| 571 | `(Ṛ. Saṃ. 8-101-10 [as read, [?]])` → `(Ṛ. Saṃ. 8-101-10)` | SECOND-PASS Q2: Kannada p.571 (ಋ. ಸಂ. ೮-೧೦೧-೧೦) agrees |
| 572 | `(Pā. Sū. 6-2-[?])` → `(Pā. Sū. 6-2-103-2)` | SECOND-PASS Q1: Kannada p.572 ಮರುದ್ವೃಧಾದೀನಾಂ ಛಂದಸ್ಯುಪಸಂಖ್ಯಾನಂ (ಪಾ. ಸೂ. ೬-೨-೧೦೩-೨) as printed |
| 573 | `; the small type is partly doubtful [?].)` → `.)` | SECOND-PASS Q2: meta-remark on doubt marking; clause removed |
| 573 | `Ni. 4-9 [?]]` → `Ni. 4-19]` | SECOND-PASS Q1: Kannada p.573 ಕ್ರಾಣಾಃ ಕುರ್ವಾಣಾ ಇತಿ ಯಾಸ್ಕಃ । ನಿ. ೪-೧೯ |
| 575 | `(Ni. 4-24, as read "೪-೩೮" [?])` → `(Ni. 4-24)` | SECOND-PASS Q1: Kannada p.575 ಮಂದೀ ಮಂದತೇಃ ಸ್ತುತಿಕರ್ಮಣಃ (ನಿ. ೪-೨೪) |
| 575 | `(Ṛ. Saṃ. 10-[?]-1, as read "೧೦-೩೦-೧" [?].)` → `(Ṛ. Saṃ. 10-50-1.)` | SECOND-PASS Q1: Kannada p.575 (ಋ. ಸಂ. ೧೦-೫೦-೧) ಪ್ರ ವೋ ಮಹೇ ಮಂದಮಾನಾಯಾಂಧಸೋ… |
| 575 | `(Ni. 11-[?], as read "೧೧-೧")` → `(Ni. 11-9)` | SECOND-PASS Q1: Kannada p.575 ಮೋದಮಾನಾಯ, ಸ್ತೂಯಮಾನಾಯ … (ನಿ. ೧೧-೯) |
| 576 | `(Ṛ. Saṃ. 3-[?]-[?], as read "೩-೩೯-೩" [?].)` → `(Ṛ. Saṃ. 3-55-15.)` | SECOND-PASS Q1: Kannada p.576 ಸಧ್ರೀಚೀನಾ ಪಥ್ಯಾ೩ ಸಾ ವಿಷೂಚೀ … (ಋ. ಸಂ. ೩-೫೫-೧೫) |
| 577 | `ಇರಧ್ಯೈ [sic; the printed second form is different in the Kannada print and is not legible ` → `ಇರಧಧ್ಯೈ [*iradhadhyai*]` | SECOND-PASS Q1: Kannada p.577 regarded as a shortened form for ಇರಧಧ್ಯೈ (IAST by sp_sanskrit.py) |
| 577 | `(Ṛ. Saṃ. 8-2-[?], as read "೮-೨-೨೩" [?]; the first words of the quotation are doubtful [?].` → `(Ṛ. Saṃ. 8-7-25.)` | SECOND-PASS Q1: Kannada p.577 ವಿದ್ಯುದ್ಧಸ್ತಾ ಅಭಿದ್ಯವಃ ಶಿಪ್ರಾಃ … (ಋ. ಸಂ. ೮-೭-೨೫) |
| 578 | `(Ni. 1-[?], as read "೧-೧೧" [?])` → `(Ni. 2-23)` | SECOND-PASS Q1: Kannada p.578 ಇಳಾ, ಗೌಃ (ನಿ. ೨-೨೩) ಇತ್ಯಾದಿ ವಾಜ್ ನಾಮಗಳಲ್ಲಿ |
| 578 | `(U. Sū. 1-12, as read "೧-೧೩" [?])` → `(U. Sū. 1-12)` | SECOND-PASS Q1: Kannada p.578 ಉಂದೇರಿಚ್ಚಾದೇಃ (ಉ ಸೂ. ೧-೧೨) |
| 578 | `*āṅ-kuṭ-* [?] (Pā. Sū. 8-4-[?]) gives` → `*aṭ kupvā* gives` | SECOND-PASS Q1: Kannada p.578 ಅಟ್ ಕುಪ್ವಾ—ಎಂಬುದರಿಂದ ಣತ್ವ: Kannada gives no sūtra number there; number removed (IAST by sp_sanskrit.py) |

### 2026-11-27 second pass, batch m500-579_2.tsv
| page | old → new | why |
|---|---|---|
| 508 | `read from the image; doubtful places [?].)*` → `read from the image.)*` | SECOND-PASS Q2: meta-remark on doubt marking; clause removed (the mark of q25 is this clause; the first edit settled the unmarked "[? the way]") |
