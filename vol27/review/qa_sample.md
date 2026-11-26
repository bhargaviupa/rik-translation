# Vol 27 — independent QA sample (English vs Kannada)

Date: 2026-11-26. Read-only check; no file other than this one was changed.

Files: `vol27/Rigveda_Samhita_Vol27_English_Translation.md` (E) and `vol27/Rigveda_Samhita_Vol27_Kannada_Text.md` (K). Line numbers are given as E#### / K####.

Method: for each page, the English between its `### Printed p. N` heading and the next one was read side by side with the Kannada between `<!-- printed N -->` and the next mark. Each page was checked for numbers and references, names and terms, quotations, negation and attribution, omissions and additions, whether each Pratipadārtha entry means what the Kannada says, stray running heads and remarks, word-list headwords without Devanagari, and foreign-script letters. A passage under a "Special Topics" heading was checked against the Kannada label (ವಿಶೇಷವಿಷಯಗಳು / ಪೀಠಿಕೆ / ಅನುವಾದವು). Sanskrit blocks were not checked letter by letter.

Selecting the pages: (a) 12 pages spread evenly through the volume; (b) 12 pages that carry a "Special Topics" heading. To pick (b), a script counted the "Special Topics" headings per page in E (152) and the ವಿಶೇಷವಿಷಯಗಳು headings per page in K (145 real headings plus duplicate garbled labels). The 7 pages where E has a heading that K does not (59, 160, 232, 319, 407, 429, 783) were all put into the sample, and 5 more pages were added to spread the sample out. Three whole-file scans were also run: foreign-script letters, Pratipadārtha headwords without Devanagari, and remark phrases. Their results are listed at the end and are marked as outside the sample.

Severity: ERROR means the English is wrong or something is missing or added. MINOR means a small inaccuracy, a formatting fault or a stray remark.

---

## A. Evenly spread pages

### p. 20 (E898–942 / K885–927)
Checked: printed translation of 9.102.1, and the whole of Ṛk 2 (Saṃhitā, Pada, bhāṣya, Gist, Pratipadārtha, Bhāvārtha). **No findings.**

### p. 110 (E5073–5118 / K4745–4792)
Checked: 9.109.6 translation, and the whole of Ṛk 7, including the Yāska quotation in the Gist. **No findings.** (The English silently corrects the Kannada headword ಆನು to अनु, which is correct.)

### p. 200 (E8273–8296 / K9852–9889)
Checked: the commentary on 10.1.1, the Śatapatha quotation and its reference (Śa. Brā. 6-7-3-10), and the start of Ṛk 2. **No findings.**

### p. 300 (E11608–11625 / K13584–13613)
Checked: the introduction to Sūkta 8 (Triśiras), Bṛhaddevatā verses 149–153 with their numbers, the reference (Bṛ. De. ch. 6, Ṛ. Saṃ. 10-9).
- MINOR — E11625 "…(Ṛ. Saṃ. 10-9th sūkta), water **NOTE**". notes.tsv (w0295) says the text "breaks off". It does not: K13613 "ಉದಕ" continues on p. 301 at K13618 "ವನ್ನು ತೆಗೆದುಕೊಂಡು…", and E p. 301 has the continuation ("…took water"). The NOTE is not needed.
- MINOR (formatting, p. 299) — E11597 the Kannada heading ಪೀಠಿಕೆ (K13568) is rendered as a plain line "Introduction.", not as a heading.

### p. 400 (E14856–14901 / K17258–17292)
Checked: 10.12.3 translation and Ṛk 4: Gist, Pratipadārtha, the Pada/bhāṣya layout.
- MINOR — E14889 "- अपः (*apaḥ*)—my sacrificial rite". The vocative that opens the Kannada list, "(ಎಲೈ ಅಗ್ನಿಯೇ)" (K17289, "O Agni"), is dropped.

### p. 500 (E17774–17815 / K20933–20970)
Checked: 10.15.7 translation and Ṛk 8: Gist, Pratipadārtha.
- MINOR — E17806 "- नः (*naḥ*)—our (their) सोम्यासः (*somyāsaḥ*)—those who offered Soma according to rule". Two headwords are merged on one line (K20966 ನಃ—ನಮ್ಮ (ತಮ್ಮ) ಸೋಮ್ಯಾಸಃ—…). They should be two entries.
- **ERROR** (found on the next page, p. 501) — E17818–17831: p. 501 repeats the Pratipadārtha entries already given on p. 500 (naḥ, somyāsaḥ, vasiṣṭhāḥ, pūrve, ye pitaraḥ, somapīthaṃ, anūhire, tebhiḥ, uśadbhiḥ, rarāṇaḥ), mostly with IAST-only headwords (`- *naḥ*—our (your)` etc.). K p. 501 (K20974–20975) has only ಉಶನ್ … ಯಮಃ … ಹವೀಂಷಿ … ಪ್ರತಿಕಾಮಂ … ಅತ್ತು. The repeated block is an addition and should be removed.

### p. 590 (E20388–20391 / K24219–24252)
Checked: the long Kaṭha-Upaniṣad paraphrase (eleven gates, Haṃsavatī Ṛk, prāṇa/apāna, the address to Gautama), including its negations ("not by prāṇa nor by apāna"; "nothing remains"). **No findings.**

### p. 680 (E23754–23795 / K27663–27700)
Checked: the end of the Pratipadārtha of 10.23.5, Bhāvārtha, translation, and Ṛk 6 (Saṃhitā, Pada, bhāṣya, Gist). **No findings.**

### p. 770 (E27428–27475 / K31137–31173)
Checked: the bhāṣya, Gist, Pratipadārtha, Bhāvārtha and translation of 10.28.12, and the opening bhāṣya of Sūkta 29.
- MINOR — E27437 "Sāyaṇa continues his gloss of the previous Ṛk." This is wrong and is also a translator's remark. The bhāṣya on this page continues the gloss of the same Ṛk 12, whose Saṃhitā and first bhāṣya lines are on p. 769 (E27407–27423). The same line also has an IAST-only word, "*sukarmāṇaḥ*".

### p. 860 (E30801–30839 / K34580–34616)
Checked: the end of the Pratipadārtha of 10.34.3, Bhāvārtha, translation, and Ṛk 4 (bhāṣya, Gist). **No findings.**

### p. 930 (E33942–33983 / K37319–37356)
Checked: the Gist, Pratipadārtha (the 18 entries), Bhāvārtha and translation of 10.38.5, and the introduction to Sūkta 39 (Ghoṣā, daughter of Kakṣīvān; sūktas 116–125 of Maṇḍala 1).
- MINOR — E33983 "For some other reason this woman was afflicted with leprosy". K37355 ಕಾರಣಾಂತರದಿಂದ means "for some reason". The word "other" has nothing to refer to. (The introduction is correctly headed "**Introduction**", E33981.)

### p. 985 (E35822–35865 / K39338–39370)
Checked: the bhāṣya tail, Gist, Pratipadārtha, Bhāvārtha and translation of 10.40.10.
- MINOR — E35835 "- ये नरः (*ye naraḥ*)—the husbands who". The opening vocative "(ಎಲೈ ಅಶ್ವಿನೀದೇವತೆಗಳೇ)" (K39348) is dropped.
- MINOR — E35853 "O Ashvin gods". The volume elsewhere spells it "Aśvin" (e.g. E34742).

---

## B. Pages carrying a "Special Topics" heading

### p. 3 (E99–138 / K134–170)
Checked: the Pada, bhāṣya, Gist, Pratipadārtha, Bhāvārtha and translation of 9.101.1, and the Special Topics (the ninth Maṇḍala has many seers). The heading matches K165 ವಿಶೇಷವಿಷಯಗಳು. **No findings.**

### p. 59 (E2681–2728 / K2561–2600)
Checked: the bhāṣya, Pratipadārtha and Bhāvārtha of 9.106.14, the opening bhāṣya of Sūkta 107 and its Gist, and the passage after it.
- **ERROR** — E2726 "##### विशेषविषयगळु (Special Topics)" followed by E2728 "Translation: This sūkta परीतः … is the fourth sūkta in the seventh Anuvāka…". The Kannada passage is the Anuvāda of the Sūkta's opening bhāṣya: K2599 "ಅನುವಾದವು—ಪರೀತಃ ಎಂಬ ಈ ಸೂಕ್ತವು…". It is not a Special Topics section, so the heading should be Anuvāda, as elsewhere (e.g. E2096).
- MINOR — E2728 "the preceding statement was made at sūkta 66 of this Maṇḍala, त्वं सोमासि". K2600 "ಹಿಂದೆ ಈ ಮಂಡಲದ ತ್ವಂ ಸೋಮಾಸಿ ಎಂಬ ೬೬ ನೇ ಸೂಕ್ತಕ್ಕೆ ಹೇಳಿರುವ" is the first half of a sentence that ends on p. 60, K2605 "…ಭರದ್ವಾಜ ಕಶ್ಯಪ ಮೊದಲಾದ ಸಪ್ತರ್ಷಿಗಳೇ ಈ ಸೂಕ್ತಕ್ಕೂ ಋಷಿಗಳು". The sense is "the seven seers named earlier for Sūkta 66 are the seers of this sūkta too". The English turns the fragment into a statement of its own. (The number 66 is kept correctly; Sāyaṇa's own reference reads 9.67, and the English keeps both as printed.)

### p. 160 (E7328–7377 / K6881–6917)
Checked: the bhāṣya, Gist, Pratipadārtha, Bhāvārtha and translation of 9.113.11, the Special Topics (the heading is right: the Kannada label is garbled as "॥ ಪಟೇಲಪತಂಜಲಿ ॥", K6909), and the opening of Sūkta 114.
- **ERROR** — E7373–7375: the heading "॥ सायणभाष्यम् ॥ (Sāyaṇa-bhāṣya)" is followed by nothing. The bhāṣya block of Sūkta 114 (K6916–6917 "ಯ ಇಂದೋರಿತಿ ಚತುರ್ಯಚಮೇಕಾವಶಂ ಸೂಕ್ತಂ … ಗತಃ ಸೂಕ್ತವಿನಿಯೋಗಃ ॥") is missing.
- **ERROR** — E7377 "the sūkta य इंदोः has eleven (the printed text reads *ekāvaśaṃ*) ... it has four Ṛks". The text means "the eleventh sūkta, of four Ṛks" (ಚತುರೃಚಮೇಕಾದಶಂ ಸೂಕ್ತಂ). "Has eleven" is wrong. The line also carries a translator's remark, an IAST-only word, an ellipsis "...", and a "**NOTE**" fused to the sentence ("stated.**NOTE**").
- MINOR — E7369 "Ānandāḥ, modāḥ, mudaḥ, pramudaḥ: …". The Sanskrit is given in IAST only, without Devanagari (K6910 ಆನಂದಾಃ ಮೋದಾಃ ಮುದಃ ಪ್ರಮುದಃ).

### p. 232 (E9294–9312 / K11040–11071)
Checked: the continuation of the Special Topics of 10.2.7 (Tvaṣṭṛ as Prajāpati, Tai. Brā. 2-1-2-1, devayāna and pitṛyāna).
- **ERROR** — E9296–9298 "##### Gist of the bhāṣya / not applicable here (no bhāṣya block on this page)." The heading is invented, the remark is a translator's, and K p. 232 has neither.
- MINOR — E9300 repeats the Special Topics heading, which already stands at E9290 on p. 231 (K has one heading, on p. 231), and E9302 adds the remark "(Continuing.)". The words āpaḥ, devayāna and pitṛyāna appear in IAST only (E9302, E9308; K11043 ಅಪಃ, K11056 ದೇವಯಾನ, ಪಿತೃಯಾನ).
- MINOR — E9310 "Of the paths one goes to enjoy the fruit of good works, one is devayāna and the other pitṛyāna". The sentence is broken. K11062 means "Of the paths by which one goes to enjoy the fruit of good works, one is devayāna, the other pitṛyāna".

### p. 319 (E12229–12243 / K14264–14296)
Checked: the Bhāvārtha and translation of 10.8.9, and the opening of Sūkta 9 (its relation to 1.23.20–23, the seers, the metre).
- **ERROR** — E12240 "##### विशेषविषयगळु (Special Topics)". This passage is the introduction to Sūkta 9: K14280 has the garbled label "ಪಿ ೯ ೦ ಕೆ." (ಪೀಠಿಕೆ) and K14281 "ಒಂಭತ್ತನೆಯ ಸೂಕ್ತವು." It should be headed **Introduction**, as at E12794 and E33981. Numbers checked: 6th Ṛk = 1.23.20, Ṛks 7–9 = 1.23.21–23, Anuṣṭubh against Gāyatrī; all correct.
- MINOR — E12242 "the presiding deities of water, the *advaitègaḷu***NOTE**, are praised". K14282 ಅದ್ವೈತೆಗಳನ್ನು is a misprint for ಅಬ್ದೇವತೆಗಳನ್ನು / ದೇವತೆಗಳನ್ನು ("deities"; the same page has ಉದಕಾಭಿಮಾನಿದೇವತೆಗಳನ್ನು at K14294). A transliterated Kannada garble in the English is not needed. The line also opens with the redundant phrase "The ninth sūkta."

### p. 407 (E15166–15204 / K17527–17561)
Checked: the Pratipadārtha (17 entries), Bhāvārtha and translation of 10.12.8, and the opening of Sūkta 13 (the Havirdhāna carts, Ṛ. Saṃ. 10-13-5).
- **ERROR** — E15197 "##### विशेषविषयगळु (Special Topics)". This passage is the introduction to Sūkta 13: K17554 has the garbled label "ಪಿ ೯ ೦ ಕೆ." (ಪೀಠಿಕೆ) after K17553 "ಹದಿಮೂರನೆಯ ಸೂಕ್ತವು". It should be headed Introduction.

### p. 429 (E15807–15823 / K18310–18341)
Checked: "Pitṛs, Pitṛlokas and the worship of the Pitṛs", the quotation of 10.14.1 and the four numbered points.
- **ERROR** — E15809 "##### विशेषविषयगळु (Special Topics)". The passage is the introduction to Sūkta 14. It starts unheaded on p. 428 (E15805, after "## Sūkta 14"; K18291 "ಹದಿನಾಲ್ಕನೆಯ ಸೂಕ್ತವು." and the text after it), and K p. 429 has no heading at all. The English puts a Special Topics heading in the middle of the introduction. It should be one "Introduction" heading at E15805. The content itself (points 1–4, the questions listed) matches.

### p. 530 (E18980–19019 / K22110–22148)
Checked: the bhāṣya, Gist, Pratipadārtha, Bhāvārtha and translation of 10.16.14, and the Special Topics (asthi-sañcayana, Ā. Gṛ. Sū. 4-5-3). The heading matches K22145. **No findings.** (The Gist reads "keeping it to the left" for Sāyaṇa's prasavyam, and the Special Topics reads "keeping it to the right" for K22148 ಪ್ರದಕ್ಷಿಣಾಕಾರವಾಗಿ. Each follows its own source; the conflict is in the print.)

### p. 615 (E21028–21068 / K25127–25163)
Checked: the Pratipadārtha, Bhāvārtha and translation of 10.18.9, and the Special Topics (Ā. Gṛ. Sū. 4-2-20). The heading matches K25152. **No findings.**

### p. 753 (E26710–26749 / K30465–30502)
Checked: the bhāṣya tail and Gist of 10.27.24, the Pratipadārtha, Bhāvārtha and translation, and the Special Topics (Yāska on pāduḥ, Ni. 5-19). The heading matches K30497.
- MINOR — E26719 "this motion … by Āditya's decision or by effort, is never stopped". The bhāṣya (K30470 "…ಆದಿತ್ಯೇನ ನಿರ್ವೇದನಾಚ್ಛ್ರಮೇಣ ವಾ ಗಮನಂ ನ ಮುಚ್ಯತೇ") says that the motion is never given up by Āditya *out of weariness or fatigue*. "Decision" and "effort" reverse the sense.

### p. 783 (E27954–27994 / K31630–31668)
Checked: the bhāṣya tail and Gist of 10.29.8, the Pratipadārtha (16 entries), Bhāvārtha and translation, and the opening of Sūkta 30 (Kavaṣa Ailūṣa).
- **ERROR** — E27992–27994 "##### विशेषविषयगळु (Special Topics)" followed by "Introduction. For this sūkta and the next five sūktas the seer is Kavaṣa…". K31663 has the garbled label "ಜೀರಿಕೆ" (ಪೀಠಿಕೆ) after K31662 "ಮೂವತ್ತನೆಯ ಸೂಕ್ತವು.". It should be headed Introduction.
- MINOR — E27994 "the Brāhmaṇas, the ṛṣis and others, did not keep social dealings with him". K31665 "ಋಷಿಗಳೇ ಮೊದಲಾದ ಬ್ರಾಹ್ಮಣರು" means "the Brāhmaṇas, the ṛṣis and others like them", not three separate groups.
- MINOR — E27962 "The word स्मेति (*smeti*) is only a filler of the line." K31634 "ಸ್ಮೇತಿ ಪದಪೂರಣಃ" is *sma iti*: the filler is स्म.

### p. 956 (E34725–34755 / K38234–38270)
Checked: the Pratipadārtha, Bhāvārtha and translation of 10.39.8, and the Special Topics (Kali, the reference 1-112-15, Vandana). The heading matches K38254. **No findings.**

---

## C. Whole-file scans (outside the 24 pages)

- **ERROR** — E18447–18448 (p. 517/518, inside the Pada block of 10.16.4): a stray running head in Telugu script, "> 519	సకలభాష్యము	। మం. १५ २. १. ३७. ४", and a stray line "> १ चन्नबसवण्णन". Both are carried over from K21622. They are not part of the text and should be removed.
- MINOR — E34763 (p. 956/957): Telugu letters inside a Devanagari quotation, "ताभिरू షు ऊतिभिः" and "*tābhirū షు ūtibhiḥ*". It should read षु / ṣu.
- MINOR — 24 Pratipadārtha lines have no Devanagari headword (IAST only, or no headword at all): E1788, E2276, E3118, E3856, E4420, E8578, E10133, E12707, E14592, E17532, E17822–17831 (the duplicate block on p. 501), E18646, E21665, E23151, E31226, E31526.
- MINOR — Remarks left inside the text: "(Continuing.)" at E9302, E10367, E19949; "(reference printed garbled) **NOTE**" at E8874; also E7377 and E9298 (above).
- MINOR — The labels for introductions and Anuvāda passages are not uniform: "Introduction." as a plain line (E52, E7824, E11597), "**Introduction**" (E12794, E18212, E33981), "Introduction:" inline (E17275); for the Anuvāda, "##### Anuvāda", "Anuvāda:", "Translation:" (E2728, E10821) and "The Kannada Anuvāda:" (E8803, E11742).
- No Tamil, Malayalam, Bengali or Gujarati letters, and no stray Kannada script, were found in E (the only Kannada script is the fixed heading word विशेषविषयगळु).

---

## Totals

| | Count |
|---|---|
| Pages compared | 24 (12 evenly spread + 12 with Special Topics) |
| ERROR | 10 (9 from the sample pages: p. 59 ×1, p. 160 ×2, p. 232 ×1, p. 319 ×1, p. 407 ×1, p. 429 ×1, p. 783 ×1, p. 501 repeat found from p. 500 ×1; 1 from the whole-file scan: p. 517/518) |
| MINOR | 20 (16 on sample pages, 4 from the whole-file scans) |
| Sample pages with no finding | 10 (pp. 3, 20, 110, 200, 530, 590, 615, 680, 860, 956) |

Most serious:
1. Introductions (ಪೀಠಿಕೆ) are headed "Special Topics" on pp. 319, 407 and 783, where the Kannada label is garbled ("ಪಿ ೯ ೦ ಕೆ.", "ಜೀರಿಕೆ"). On p. 429 a "Special Topics" heading is placed in the middle of Sūkta 14's introduction, and on p. 59 the Anuvāda is headed "Special Topics". The same pattern probably affects other pages where the source label is garbled.
2. p. 160, Sūkta 114: the Sāyaṇa-bhāṣya block is missing under its heading, and the Gist misreads "the eleventh sūkta" as "has eleven", with a translator's remark and ellipsis left in the text.
3. p. 501: the Pratipadārtha of 10.15.8 already given on p. 500 is repeated with IAST-only headwords (an addition not in the Kannada). Also, p. 232 has an invented "Gist of the bhāṣya: not applicable here" section, and a Telugu running head stands inside the Pada block at E18447.
