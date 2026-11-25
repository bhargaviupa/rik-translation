# Vol 23: sample QA of the English against the Kannada text (read-only)

Date: 2026-11-24. Files: `vol23/Rigveda_Samhita_Vol23_English_Translation.md` (E), `vol23/Rigveda_Samhita_Vol23_Kannada_Text.md` (K). Line numbers are 1-based line numbers in each file.

**Method.** I read each sampled page in both files side by side: E `### Printed p. N` against K `<!-- printed N -->`. A section that starts on page N in K but sits on page N±1 in E was followed across the page break. I checked Pratipadārtha entries one by one against the Kannada word list, the Bhāvārtha sentence by sentence, Special Topics and Anuvāda in full, and the sūkta headers (maṇḍala/anuvāka/aṣṭaka/varga, ṛṣi/devatā/chandas). I checked the Gist against the Sanskrit bhāṣya block in K only where a claim looked doubtful. I did not compare Sanskrit blocks letter by letter. A script compared the reference numbers (patterns such as `7-100-5`, `Ā. 8.11`, `Ai. Ā. 5-2-5`, with Kannada digits converted) on each sampled page plus its neighbouring pages. Every difference it reported on the sampled pages was a line split or an en dash, not a changed number.

Sample: 12 evenly spaced pages (20, 90, 170, 250, 330, 420, 500, 580, 650, 720, 790, 840) and 12 pages with Special Topics (3, 64, 110, 159, 203, 296, 361, 452, 551, 663, 757, 825). Spill-over pages were also read: 19, 21, 89, 160, 204, 297, 453, 501, 651, 721, 826 and 827.

## Evenly spaced pages

**p. 20** (E742–769, K781–812; Ṛk 6 end and Ṛk 7, with the Ṛk 6 Pratipadārtha and Bhāvārtha on p. 19 and the Ṛk 7 Pratipadārtha and Bhāvārtha on p. 21). Word lists, Bhāvārtha, English translation and Gist all match.
- MINOR: E782 `अ०हः (*a0haḥ*)`. The Kannada entry is K821 `ಅ೦ಹಃ`, which is `aṃhaḥ`. A zero glyph has been carried into both the Devanagari and the IAST.

**p. 90** (E3697–3725, K3448–3482; Special Topics end of Sūkta 89, introduction and header of Sūkta 90). The reference (Ā. 4-11), the Anuvāda (fifteen sūktas, seven ṛks, the dual from ṛk 5 on means Indra and Vāyu, Ā. 8.11) and the header (Anuvāka 5, Aṣṭaka 5, Adhyāya 6, Varga 12, deity 1-4 Vāyu and 5-7 Indra-Vāyu) all match. No findings.

**p. 170** (E7057–7101, K6610–6649; Ṛk 9 of Sūkta 97).
- MINOR: E7086 `नां (*nāṃ*)—addressed to you two`. The Kannada word list has K6638 `ವಾಂ—ನಿಮ್ಮಿಬ್ಬರನ್ನೂ ಉದ್ದೇಶಿಸಿ`, i.e. headword `vāṃ`, the same as the Pada. The English took the Saṃhitā/bhāṣya spelling `नां` instead of the word-list headword.
- Everything else matches, including "Bṛhaspati" in the Bhāvārtha (K6646 `ಬೃಹಸ್ಪತಿಯೇ`).

**p. 250** (E10042–10072, K9572–9598; Ṛk 6 of Sūkta 104). All 16 Pratipadārtha entries and the Bhāvārtha match. The Gist reproduces the lacuna in the source (`.... .... ....`, K9575), marked with a NOTE. No findings.

**p. 330** (E13188–13230, K14103–14138; Āsaṅga's gift, Sūkta 8.1). Word list, Bhāvārtha ("ten thousand more than other donors", Playoga) and Gist (Prāyogi Āsaṅga as ṛṣi and devatā of the four verses) match. No findings.

**p. 420** (E16947–17006, K17683–17721; Ṛk 7 of Sūkta 8.4). Turvaśa, Yadu, the slaying of Vṛtra and the negatives (`mā bhema`, `mā śramiṣma`) are all rendered correctly. No findings.

**p. 500** (E20417–20457, K20921–20955, with the Bhāvārtha on p. 501). Pratipadārtha and Bhāvārtha match. The Gist reference (Tai. Saṃ. 2-5-3-3, K20947) is correct. No findings.

**p. 580** (E23988–24024, K24235–24266; Ṛk 14 of Sūkta 8.8). Fully matching. No findings.

**p. 650** (E26953–26993, K26979–27014, with p. 651). Bhāvārtha end, Ṛk 13 Pratipadārtha (`धृतं न`, as in the Kannada) and Ṛk 13 Bhāvārtha match. No findings.

**p. 720** (E30176–30219, K29901–29938, with the p. 721 Gist and Anuvāda at E30230–30240 and K29941–29955).
- MINOR: E30219 ends with the fragment "In the Mahāvrata, in the niṣkevalya." The next Gist block (E30230) opens with the same words, so the phrase is printed twice.
- MINOR: E30230 renders `औष्णिहतृचाशीतौ` (K29938) as "for the Uṣṇih tṛca-verses". The *aśīti* (the "eighty" of Uṣṇih tṛcas) is dropped.
- The Anuvāda matches: Goṣūkti and Aśvasūkti, Ai. Ā. 5-2-5, Ā. 7-8, thirteen ṛks.

**p. 790** (E33384–33439, K32813–32873; Ṛk 4 Bhāvārtha, Ṛk 5). Pratipadārtha and Bhāvārtha match.
- ERROR (structure): page 791 has no `### Printed p. 791` heading. Instead its running head is printed inside the Sāyaṇa block as Sanskrit text: E33414 `> आ. ६. आ. १. व. ३०.] ऋग्वेदसंहिता 791.`, taken from K32852 `> ಆ. ೬. ಆ. ೧. ವ. ೩೦.] ಋಗ್ವೇದಸಂಹಿತಾ 791.`. The same defect appears at E3563 (`ऋग्वेदसंहिता '87`, p. 87) and E13050 (`ऋग्वेदसंहिता 827 .`, which is p. 327).
- MINOR: E33418 `(Ā. Gṛ. 1-1-4 **NOTE**)`, notes.tsv row "reference 1-1-4 is not in the supplied text…". The reference is in the source, split across a line break: K32845–32846 `ಆ. ಗೃ. ೧-೧-` / `೪.`. The NOTE's question is unfounded and can be closed.

**p. 840** (E35616–35657, K34855–34891; Maruts, Sūkta 8.20). Word list (including the negation `नकिः येतिरे`, "do not strive at all") and Bhāvārtha match.
- MINOR: E35633 `नकिर्यॆतिरे (*nakiryètire*)`. The inline Sanskrit carries the short-e sign `ॆ` and its non-IAST transliteration `è`. The same artefact appears at E11750 `तर्तूर्यंतॆ (*tartūryaṃtè*)`.

## Pages with Special Topics

**p. 3** (E77–118, K159–197; Uṣas). Pratipadārtha, Bhāvārtha and Special Topics (the particle `u` is a pāda-filler) match. No findings.

**p. 64** (E2595–2670, K2463–2526). Special Topics (Ekādaśin, purodāśa anuvākyā, Ā. 3-7), Anuvāda and header (Sūkta—8, Varga 9, as printed) and the Ṛk 1 word list all match. No findings.

**p. 110** (E4533–4580, K4222–4261, with p. 111).
- ERROR: E4563 `- *śvavasaḥ*—food`. The headword has no Devanagari and the IAST is wrong. The Kannada has K4251 `ಶ್ರವಸಃ—ಅನ್ನವನ್ನು`, which should give `श्रवसः (*śravasaḥ*)`. The volume has six more entries with no Devanagari headword: E5815 `*baraḥ*—` (also with an empty meaning), E8019, E9680, E17490, E18478, E35040.
- Special Topics (Ā. 8-9, Aindravāyava tṛca) and Bhāvārtha match.

**p. 159** (E6573–6617, K6181–6215, with p. 160).
- MINOR: E6617 (Gist) "at the third pressing, for the increase of soma". The bhāṣya has K6214 `ಸ್ತೋಮವೃದ್ದೌ`, i.e. *stoma*-vṛddhi, the increase of the stoma. The Kannada Anuvāda (K6227 `ಸೋಮವೃದ್ಧಿಗಾಗಿ`) has "soma" too, so the English Anuvāda is faithful to it, but the Gist should follow the Sanskrit.
- Special Topics (Anvārambhaṇīyeṣṭi, Ā. 2-8), the deity list and the two different references (Ā. 7-9 in the bhāṣya, Ā. 6-9 in the Anuvāda, both as printed) match.

**p. 203** (E8419–8429, K7886–7921, read on through p. 204, E8431–8443 and K7923–7943; long Special Topics on vaṣaṭkāra). Every sentence is present. The roles are right: the Hotṛ invites, the Adhvaryu offers, the Acchāvāka recites the śastra. The references all match: 7-100-5 to 7-100-7, 7-99-2, 7-100-3, Ai. Brā. 11-5. No findings.

**p. 296** (E11706–11739, K12727–12768, with p. 297).
- MINOR: E11751 `उप क्रमस्व—be gracious to us, come near` drops the bracket that comes before it in the Kannada, K12777–12778 `(ಅಂತಹ ಸಾಮರ್ಥ್ಯವುಳ್ಳ ನೀನು)`, "(you, having such power)". The Bhāvārtha (E11760) does contain it.
- Special Topics (Cāturviṃśika, Praśāstṛ, optional anurūpa pragātha) matches.

**p. 361** (E14459–14493, K15365–15399). Pratipadārtha, Bhāvārtha and Special Topics (Atirātra first paryāya, Ṛks 25–27, Ā. 8-13) match. No findings.

**p. 452** (E18242–18274, K18903–18927, with the p. 451 Pratipadārtha at E18233–18240 and p. 453).
- ERROR: in Special Topics, E18253 "in the Sūtra "The Hotṛ should recite 'aśvinā nāsatyā vāvṛdhānā śubhaspatī'" (Ā. 5-5)". The Kannada quotes the sūtra in Sanskrit: K18926–18927 `ಹೋತಾ ಯಕ್ಷದಶ್ವಿನಾ ನಾಸತ್ಯಾ ವಾವೃಧಾನಾ ಶುಭಸ್ಪತೀ`. The English replaces the quotation with a paraphrase, with no Devanagari and no IAST, and renders `yakṣat` ("shall offer/sacrifice to") as "should recite". The Gist at E18230 has the same paraphrase (bhāṣya K18896).
- Pratipadārtha and Bhāvārtha for Ṛks 11 and 12 match.

**p. 551** (E22655–22687, K23027–23056, with the Gist start on p. 550).
- MINOR: E22662 (Gist) "The block completes the bhāṣya on the preceding verse … The last word printed is समयूयुजन्". This is a translator remark, and it is wrong on two points. The block (K23030–23031) continues the bhāṣya of the same Ṛk 22, not the preceding verse. And `समयूयुजन्` is Sāyaṇa's gloss "they joined", not just "the last word printed".
- Pratipadārtha, Bhāvārtha and Special Topics (Pravargya, Ā. 4-7) match.

**p. 663** (E27543–27577, K27520–27546). Word list, Bhāvārtha and Special Topics (Ṣoḍaśin, Ā. 6-2) match. No findings.

**p. 757** (E31897–31929, K31456–31481). Fully matching (second paryāya, stotriya tṛca, Ā. 6-4). No findings.

**p. 825** (E34951–34991, K34230–34266, with pp. 826–827).
- Pratipadārtha, Bhāvārtha and Special Topics match. The Ṛk 36 word list and Bhāvārtha ("five hundred", E35003 and E35011) follow the Kannada `ಐನೂರು` (K34278). The conflict with Sāyaṇa's "fifty" is already listed in notes.tsv.
- ERROR: in the Ṛk 37 Pratipadārtha, E35036 reads `श्यावः (*śyāvaḥ*)—(continues on the next page)`, and on p. 827 E35039 adds `*Pratipadārtha continued from the previous Ṛk*` and E35040 `- *śyāvaḥ*—Śyāva`. In the Kannada the entry simply runs over the page break (K34308 `ಶ್ಯಾವಃ-` / `ಶ್ಯಾವನು`). The English splits one entry into two, prints the second without Devanagari, and adds two translator remarks, one of them false: it is the same Ṛk, not the previous one.

## Findings across the volume (seen while checking the sample)

- Translator remarks are forbidden in the English from Vol 17 on (CLAUDE.md rule 2), but 13 remain: "(continues on the next page)", "[the sentence continues on the next page]", "(Pratipadārtha continued)" and similar, at E6870, 8310, 9417, 10429, 10471, 14010, 15619, 22797, 22844, 23303, 24737, 35036 and 35039. These are counted as one MINOR, apart from the p. 825 case above.
- 43 printed pages have no page heading in either file: 7, 10, 11, 18, 48, 49, 66, 68, 71, 79, 85, 87, 88, 89, 92, 93, 114, 130, 172–174, 176, 177, 180, 183, 212, 265, 266, 269, 279, 327, 400, 423, 424, 431, 439, 548, 549, 634, 635, 747, 791 and 847. Their text is folded into the neighbouring page. The English follows the Kannada here; the fault is in the supplied page marking, so this is not counted as a finding.

## Totals

- Pages checked: 24 sampled pages, plus 12 spill-over pages read for sections that cross a page break.
- ERRORs: 4. Wrong headword `śvavasaḥ` (p. 110); sūtra quotation paraphrased and mistranslated (p. 452); running head printed inside the bhāṣya and the p. 791 heading missing (p. 790, same defect at pp. 87 and 327); one Pratipadārtha entry split, with false remarks (pp. 825–827).
- MINORs: 10. The 8 page-level items above (pp. 20, 170, 720 (×2), 790, 840, 159, 296), plus the p. 551 remark and the volume-wide translator remarks.
- In the sampled pages I found no wrong or dropped Ṛ. Saṃ./Ā./Śrauta numbers, no reversed negations or attributions, and no dropped Bhāvārtha sentences.
