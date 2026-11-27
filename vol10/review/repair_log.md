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
