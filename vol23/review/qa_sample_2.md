# Vol 23: second sample QA of the English against the Kannada text (read-only)

Date: 2026-11-24. Files: `vol23/Rigveda_Samhita_Vol23_English_Translation.md` (E), `vol23/Rigveda_Samhita_Vol23_Kannada_Text.md` (K). Line numbers are 1-based line numbers in each file.

**Method.** This sample is separate from `qa_sample.md` and contains none of its 24 pages. For each page I read E `### Printed p. N` against K `<!-- printed N -->`. Where a section crosses a page break, I followed it onto the neighbouring page (pp. 130, 132, 380, 807). Checks made:
- every Pratipadārtha entry, headword and meaning, against the Kannada word list;
- the Bhāvārtha, sentence by sentence;
- Special Topics, Anuvāda, sūkta introductions and Particulars, in full;
- the Gist against the Sanskrit bhāṣya in K, but only where a claim looked doubtful.

I did not compare Sanskrit blocks letter by letter. A script listed the reference numbers on each page of both files (`Ā. 7-2`, `Ni. 6-24`, `8-5-23` and so on, with Kannada and Devanagari digits converted). Every difference it reported came from where a page break falls or from a bhāṣya reference repeated in the Gist, not from a changed number. A second script searched the sampled pages for Pratipadārtha entries with no Devanagari, stray running heads, `[?]`, `[sic]`, "as supplied", "continued" and the short-e artefact `ॆ`/`è`. I also ran a check over the whole volume for non-Devanagari Indic script.

Sample:
- Evenly spread: 45, 131 (p. 130 has no page mark), 190, 230, 280, 345, 401 (p. 400 has no page mark), 470, 530, 610, 690, 770.
- With Special Topics, Anuvāda or a sūkta introduction: 25, 97, 146, 226, 315, 379, 440, 521, 599, 638, 713, 806.

## Evenly spread pages

**p. 45** (E1772–1824, K1738–1777; Ṛk 5 of Sūkta 82). I checked all 18 Pratipadārtha entries, the Bhāvārtha and the Gist. The Gist NOTE (the readings देवनीतिं, देव्यवीतिं and देववीतिं disagree) is already in notes.tsv.
- MINOR: E1808 `तोकॆ (*tokè*)—to our sons`. K1768 has `ತೋಕೆ`, which gives the short-e artefact `ॆ`/`è`; the Pada and Saṃhitā read `तोके`. The earlier sample found the same artefact at E35633 and E11750.

**p. 131** (E5388–5429, K5034–5078; the end of the Sūkta 94 Anuvāda, the Particulars, Ṛk 1). I also read the Anuvāda on p. 130 (E5383–5385, K5024–5038) and the end of the Bhāvārtha on p. 132 (K5081–5082). I checked the references (Ā. 5-10, 7-5, 7-2), the Particulars (Anuvāka 6, Aṣṭaka 5, Adhyāya 6, Vargas 17 and 18, 12 ṛks, metre 1–11 gāyatrī and 12 anuṣṭubh), all 8 Pratipadārtha entries and the Bhāvārtha. They all match.
- MINOR: E5385 (end of the Anuvāda) quotes the sūtra as `इयं वामस्य मन्मन इंद्राग्नी युवामिमे`. The Kannada Anuvāda reads K5037 `ಇಯಂ ನಾಮಸ್ಯ ಮನ್ಮನ…`. The English silently took `वामस्य` from the bhāṣya and gave no NOTE. The reading is very probably right, but this is a letter corrected without a mark.

**p. 190** (E7888–7931, K7376–7415; Ṛk 7 of Sūkta 99). I checked the Gist against the bhāṣya (Abhyudayeṣṭi, Ā. 3-13, the gloss of śipiviṣṭa), the 11 Pratipadārtha entries and the English translation. No findings.

**p. 230** (E9236–9283, K8831–8872; Ṛk 2 of Sūkta 103, the frogs). I checked all 15 Pratipadārtha entries and the Bhāvārtha (the dry leather bag, the waterless lake, the waters of heaven, cows lowing with their calves). No findings.

**p. 280** (E11167–11181, K10662–10694; introduction to Maṇḍala 8 and to the seer Kaṇva). I checked these and they match: 49 sūktas; then 11 Vālakhilya sūktas with 80 ṛks; Sāyaṇa wrote no commentary on them; the Poona Vaidika Saṃśodhana Maṇḍala edition used a Kāśī manuscript; 8-5-23; Bṛ. De. 6-35; verse 36; Pragātha asleep on the lap of Kaṇva's wife. No findings.

**p. 345** (E13744–13785, K14687–14730; the end of Ṛk 9 and Ṛk 10 of Sūkta 8.2). I checked the Pratipadārtha, the Bhāvārtha (ten-fold filter, Maitrāvaruṇa graha, curds at the third pressing) and the start of the Ṛk 10 word list. No findings.

**p. 401** (E16157–16197, K16956–16992; Ṛk 17 of Sūkta 8.3). The Bhāvārtha matches. The Gist NOTE (`द्भुलोकादा` against the Kannada `ದ್ಯುಲೋಕ`) is in notes.tsv.
- ERROR: E16187 `- ऋष्टेभिः (*ṛṣṭebhiḥ*)—with the Maruts of attractive form`. The Kannada word list has K16978 `ಋಷ್ವೇಭಿಃ`, which is ऋष्वेभिः (*ṛṣvebhiḥ*), the same as the Saṃhitā (K16959) and the Pada (K16964). The English headword came from the garbled bhāṣya word `ಋಷ್ಟೇಭಿರ್…` (K16969) instead of the word list. The wrong headword appears nowhere else in E.

**p. 470** (E19055–19096, K19666–19706; Ṛk 30 of Sūkta 8.5). I checked the 8 Pratipadārtha entries, including `उप (*upa*) (come)` for K19687 `ಉಪ (ಆಗತಂ)`, and the Bhāvārtha. No findings.

**p. 530** (E21739–21783, K22165–22206; the end of Ṛk 1 and Ṛk 2 of Sūkta 8.7). The Bhāvārtha, the Gist (taviṣī, yāma, nyahāsata) and the 8 Pratipadārtha entries match.
- MINOR: E21740 `#### Ṛk 1 (continued)`. The Kannada has no heading here (K22166–22169). This is a heading added by the pipeline, of the same kind as the "continued" remarks listed in `qa_sample.md`.

**p. 610** (E25307–25351, K25442–25481; the end of Ṛk 17 and Ṛk 18 of Sūkta 8.9). I checked the Bhāvārtha (Uṣas, the sacrificial Hotṛ, plentiful oblation) and the 11 Pratipadārtha entries. No findings.

**p. 690** (E28783–28807, K28643–28680; Ṛk 18 of Sūkta 8.13). The Bhāvārtha (Trikadruka = Jyotis, Go, Āyus) and the Special Topics (Yāska's two quotations, Ni. 1-10) match sentence by sentence. No findings.

**p. 770** (E32483–32526, K32001–32037; Ṛk 8 of Sūkta 8.18). The 13 Pratipadārtha entries (`दैन्व्या` as printed in K) and the Bhāvārtha match. No findings.

## Pages with Special Topics, Anuvāda or an introduction

**p. 25** (E950–990, K961–1004; the end of Sūkta 82, then the bhāṣya, Anuvāda and Particulars of Sūkta 83). I checked these and they match: the Anuvāda (13th sūkta of anuvāka 5, ten ṛks, Praśāstṛ, Ā. 7-9) and the Particulars (Vargas 4 and 5, Indra and Varuṇa, Jagatī). No findings. E963 gives "Aryaman" where the Kannada Bhāvārtha misprints `ಅರಮ್ಯನೂ` (K973). This is an obvious misprint and is not counted.

**p. 97** (E3986–4029, K3718–3758, and p. 98 E4031–4033, K3760–3762; Ṛk 5 of Sūkta 90, Special Topics). I checked all 15 Pratipadārtha entries, the Bhāvārtha and the Special Topics reference (Ā. 8-11). They match.
- MINOR: E3999 (Gist) and E4028 (Special Topics) have "Aindravāya tṛca". The Kannada has K3755 `ಐಂದ್ರವಾಯವತೃಚ` and the bhāṣya K3724 `ಐಂದ್ರವಾಯವಸ್ತ್ರಚಃ`, both *Aindravāyava*. The syllable *-va* has been dropped.

**p. 146** (E6052–6087, K5672–5707; Special Topics of Ṛk 2, bhāṣya of Ṛk 3 of Sūkta 95). The Special Topics (Sārasvata animal sacrifice, vapā anuvākyā, Ā. 3-7) match.
- ERROR (script): the Devanagari Sāyaṇa block contains Telugu letters: E6077 `సరస్वान्`, E6078 `సరస్వాన్ … यजमानेభ్యो`, E6080 `సారస్వతే తృచేశ్యా ఉక్తో వिनियోగో న విరుధ్యతే`. The Telugu comes from the supplied Kannada text (K5704–5707), and the converter passed it through unchanged. The printed volume would show Telugu script inside a Devanagari block. These are the only three lines in E with Telugu characters.
- MINOR: E6084 (Gist) quotes the sūtra `"sa vāvṛdhe naryo yoṣaṇāsu yasya vrataṃ paśavo yanti sarve"` in hand-typed IAST, with no Devanagari. E6085 does the same with `"vi mamṛjīta"`. Rule 1 says inline Sanskrit is copied inside ⟦ ⟧ so that it gets all three layers. The bhāṣya also reads K5699 `ಸ ನಾವೃಧ…`; the English silently gives `vāvṛdhe`.

**p. 226** (E9126–9137, K8688–8716; introduction to Sūkta 103, the frogs).
- ERROR (omission): E9132 gives only an English paraphrase, "Vasiṣṭha, desiring rain, praised Parjanya. The frogs rejoiced along with him. … (Ni. 9-6)". The Sanskrit quotation of the Nirukta is missing: K8693–8694 `ವಸಿಷ್ಠೋ ವರ್ಷಕಾಮಃ ಪರ್ಜನ್ಯಂ ತುಷ್ಟಾವ । ತಂ ಮಂಡೂಕಾ ಅನ್ವಮೋದಂತ । ಸ ಮಂಡೂಕಾನನುಮೋದಮಾನಾನ್ ದೃಷ್ಟ್ವಾ ತುಷ್ಟಾವ ॥`. It has no Devanagari or IAST anywhere in E. (The second quotation on the page, Ni. 9-5, is given in full at E9134.)
- MINOR: E9130 puts this text under `##### विशेषविषयगळु (Special Topics)`. The Kannada has no Special Topics heading. Its line K8692 `ಪಿ ೯ ೦ ಕೆ .` is a garbled `ಪೀಠಿಕೆ` (Introduction), so the section should be headed as an introduction.
- The rest matches: the etymology of maṇḍūka (majjana, mad, mand, maṇḍ, maṇḍa + okas, mud) and Ni. 9-5.

**p. 315** (E12549–12558, K13500–13533; Special Topics on गल्बया, Sūkta 8.1). The Yāska passage (Ni. 6-24), the paraphrase (the wild beast angered by harassment, "who does not pray to the lord?") and the explanation of गल्ला/धमनी match sentence by sentence. No findings.

**p. 379** (E15242–15269, K16107–16138, and p. 380 E15270–15281, K16139–16161; bhāṣya, Anuvāda and Particulars of Sūkta 8.3). I checked these and they match: the Anuvāda (24 ṛks, Medhyātithi Kāṇva, metres, 21–24 the dānastuti of Pākasthāman son of Kurayāṇa), the references (Ai. Ā. 5-2-4, Ā. 5-15, 7-3, 7-12) and the Particulars.
- ERROR (meaning reversed, Gist): E15264 says "…with the exception of the praises of gifts; the seventh and eighth are taken up separately (*uddhāraḥ*)." The bhāṣya (K16117) has `ಸಪ್ತಮಷ್ಟಮ್ಯೋಶ್ಚೋದ್ಧಾರಃ` and the Kannada Anuvāda (K16135) `ಏಳು ಮತ್ತು ಎಂಟನೆಯ ಋಕ್ಕುಗಳನ್ನು ಬಿಟ್ಟು`: the 7th and 8th are left out. The English Anuvāda at E15268 renders it correctly, so the Gist contradicts it.
- MINOR: in the same line, E15264 renders `ಬಾರ್ಹತತೃಚಾಶೀತೌ` (K16117) as "for the Bārhata tṛca-and-pragātha series". The *aśīti* (the "eighty" Bṛhatī tṛcas) is lost. The earlier sample found the same slip with the Uṣṇih tṛcāśīti at E30230.

**p. 440** (E17722–17738, K18422–18460; the opening of Adhyāya 8 and Sūkta 8.5). I checked these and they match: the Anuvāda (39 ṛks, Brahmātithi, 1–36 Gāyatrī, 37–38 Bṛhatī, last Anuṣṭubh, five half-verses praising the gift of Kuśu son of Cedi, Ā. 4-15) and the Particulars.
- MINOR: E17731 `(This is) the ?-th sūkta.**NOTE**`. The Kannada has K18427 `ಇದನೆಯ ಸೂಕ್ತವು.`, plainly a misprint for `ಐದನೆಯ` (fifth), as the Anuvāda itself says two lines later. The `?` is a placeholder left in the English text; the NOTE question is in notes.tsv (w0438).
- MINOR: E17733 heads the Anuvāda `##### विशेषविषयगळु (Special Topics)` and starts it with "Translation:". The Kannada is K18428 `ಅನುವಾದವು—` (Anuvāda), and there is no Special Topics heading.
- MINOR: E17737 (Particulars) "the praise of the gift of Kaśu (Kuśu) of the Cedis". The Kannada has only K18451 `ಚೈದ್ಯಸ್ಯ ಕುಶೋರ್ದಾನಸ್ತುತಿಃ`. The form "Kaśu" was added from outside the supplied text.

**p. 521** (E21340–21384, K21796–21839; Ṛk 41 of Sūkta 8.6). The Gist (pūrvajāḥ, the root skuñ, Ni. 6-22), all 9 Pratipadārtha entries (`चोषुक्यसे` as printed in K21814), the Bhāvārtha and the Special Topics (`ववनीयं` as printed in K21830, Ni. 6-22) match. No findings.

**p. 599** (E24810–24854, K25002–25042; Special Topics of Ṛk 7 and Ṛk 8 of Sūkta 8.9). The Special Topics (Pravargya, Ā. 4-7), the Gist (the change of *la* to *ra* in raghu-, the causative cyava), the 10 Pratipadārtha entries and the Bhāvārtha match. No findings.

**p. 638** (E26408–26445, K26504–26542; the end of Ṛk 1 and the start of Ṛk 2 of Sūkta 8.12). The Special Topics (ईमहे can also mean "we worship", and so in the next two ṛks) and the Gist (Daśagva, Adhrigu, svarṇara, वेमहे = याचामहे) match. No findings.

**p. 713** (E29861–29896, K29605–29644; Special Topics of Ṛk 7 of Sūkta 8.14). The Cāturviṃśika day, the Brahman priest's paryāsa tṛca and the ahargaṇa from the second day all match, with Ā. 7-2 and Ā. 7-1. The start of the Ṛk 8 word list matches. No findings.

**p. 806** (E34101–34148, K33455–33496, and p. 807 E34149–34150, K33497–33502; Ṛk 27 of Sūkta 8.19). The Gist (Ābhiplavika ukthya, Praśāstṛ, optional stotriya, Ā. 7-8), the 12 Pratipadārtha entries, the Bhāvārtha and the Special Topics (three ṛks, Ā. 7-8) match.
- MINOR: E34147 ends without a full stop, and the continuation on p. 807 begins with a stray full stop: E34150 `. This is set out in…`. This is a punctuation slip at the page break.

## Totals

- Pages checked: 24 sampled pages (12 evenly spread, 12 with Special Topics, Anuvāda or an introduction). Spill-over text on pp. 98, 130, 132, 380 and 807 was also read.
- ERRORs: 4.
  1. p. 226: the Sanskrit Nirukta quotation (Ni. 9-6) is dropped; only an English paraphrase remains (E9132, K8693–8694).
  2. p. 401: wrong Pratipadārtha headword `ऋष्टेभिः` for `ಋಷ್ವೇಭಿಃ` (E16187, K16978).
  3. p. 379: the Gist reverses *uddhāra* ("taken up separately" instead of "left out", E15264, K16117 and K16135).
  4. p. 146: Telugu script inside the Devanagari Sāyaṇa block (E6077, E6078, E6080).
- MINORs: 11. By page: p. 45 (1), p. 131 (1), p. 530 (1), p. 97 (1), p. 146 (1), p. 226 (1), p. 379 (1), p. 440 (3), p. 806 (1). The silently corrected misprint on p. 25 is noted but not counted.
- In the sampled pages I found no wrong or dropped Ā./Ai. Ā./Ni./Bṛ. De./Ṛ. Saṃ. numbers, no reversed negation or attribution in the Bhāvārtha or the word lists, and no dropped Bhāvārtha sentences. No Pratipadārtha entry on the sampled pages lacks Devanagari.
