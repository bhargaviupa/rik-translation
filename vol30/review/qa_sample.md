# Vol 30 — independent QA sample (English vs Kannada)

Date: 2026-11-25. Read-only check. No file was edited except this report, and no git changes were made.

Files compared:
- EN = `vol30/Rigveda_Samhita_Vol30_English_Translation.md` (44,431 lines)
- KN = `vol30/Rigveda_Samhita_Vol30_Kannada_Text.md` (48,151 lines)

**Method.** Each page was pulled out of both files by its page mark (`### Printed p. N` in EN, `<!-- printed N -->` in KN) and read side by side. The checks covered:
- numbers and references
- names, terms and quotations
- negation and attribution
- omissions and additions
- each Pratipadārtha gloss against the Kannada gloss
- Bhāvārtha and Special Topics prose
- stray remarks or running heads
- headwords without Devanagari
- foreign-script letters

Sanskrit blocks were not compared letter by letter. A Gist is an English summary of a Devanagari-only block, so it was judged against the Kannada Pratipadārtha and Bhāvārtha of the same Ṛk. Line numbers are file lines.

**What the sample covers.**
- Even spread (12 pages): 20, 130, 240, 350, 470, 580, 700, 810, 920, 1030, 1140, 1250.
- Pages with Special Topics (12 pages): 28, 112, 193, 263, 343, 505, 619, 754, 875, 1001, 1162, 1259.
- Pages 580, 700, 810 and 920 from the even spread also carry Special Topics. In all, 16 of the 24 pages have a Special Topics section.

**Notes on coverage.**
- Pages 368–496 have no Special Topics section in EN. The KN text has none there either, except a prose use of the word on p. 377. That stretch is continuous essay text, so nothing is missing.
- KN p. 343 also holds the text of p. 344: an unmarked running head appears at KN 12995. EN has no p. 344 heading either. The two files agree, so this is not counted as a finding.

---

## Even-spread pages

### p. 20 (EN 508–527; KN 892–925)
Checked:
- the end of the Urvaśī narrative
- the Śatapatha quotation and its reference "Śa. Brā. 11-5-1"
- the cross-reference "pages 7–9"
- the Sūkta 95 header (ṛṣi and deity numbers, Aṣṭaka, Adhyāya, Vargas, ṛk count)
- Ṛk 1 Saṃhitā

Findings: none. All numbers match KN 910–917.

### p. 130 (EN 4776–4826; KN 5104–5144)
Checked: the Gist, 18 Pratipadārtha entries, the Bhāvārtha and the printed English.
- **MINOR**: EN 4802 `सनिता (*sanitā*)—honoured with praises` should match KN 5118 `ಸನಿತಾ—ಸ್ತುತಿಗಳಿಂದ ಸತ್ಕರಿಸಿದನೋ ಅಂತಹ` ("[Uśanas] who honoured [the form] with praises"). The English reads as passive, as if Uśanas were the one honoured. The Bhāvārtha at EN 4810 has it right ("who with his praises refined").

### p. 240 (EN 9180–9223; KN 9261–9296)
Checked: the Pada, the Gist, 16 Pratipadārtha entries and the Bhāvārtha.
- **MINOR**: EN 9223 Bhāvārtha `when he prayed to you`, but the Pratipadārtha at EN 9207 says `when I prayed`. KN 9284 has `ಪ್ರಾರ್ಥಿಸಿದೆನೋ` ("I prayed") and the KN Bhāvārtha at 9293 has `ಪ್ರಾರ್ಥಿಸಿದಾಗಲೂ` (no person). The grammatical person is changed and is inconsistent within the English. (The headword `इत्या` at EN 9215/9218 copies KN `ಇತ್ಯಾ` at 9287–9288 faithfully, so it is not counted.)

### p. 350 (EN 12663–12690; KN 13193–13226)
Checked:
- the Taittirīya quotation and reference
- the door names and the 1-188-5 reference
- Ṛk 6 Saṃhitā, Pada and the start of the bhāṣya
- the Gist
- **MINOR**: KN prints the reference twice: `(ಕೃ, ಸಂ- ೬. ೧. ೧. ೧.)` before the quotation (KN 13198) and `(ಕೃ. ಸಂ. ೬-೧-೧-೧)` after it (KN 13201). EN 12665 keeps only the second. The number itself is correct.

### p. 470 (EN 15339–15384; KN 17280–17316)
Checked: the Gist, 18 Pratipadārtha entries, the Bhāvārtha and the printed English.
- **MINOR**: EN 15353 `अनानुकृत्या (*anānukṛtyā*)—by the weapon free of imitation (incomparable)`. KN 17289–90 has `ಅನಾನುಕೃತ್ಯಾ—ಅನುಕರಣರಹಿತವಾದ (ಅನುಪಮವಾದ)` only. "by the weapon" is added here; it belongs to the next entry, रण्या (EN 15354).
- **MINOR**: the Gist at EN 15347 says `of the Hautyādika class` for `ಜೌಹೋತ್ಯಾದಿಕಃ` (KN 17283). This should be "of the juhoty-ādi (third) class".

### p. 580 (EN 18997–19041; KN 21245–21290)
Checked: the bhāṣya, the Gist, 7 Pratipadārtha entries, the Bhāvārtha, the printed English, and Special Topics (sūtra quotation and reference Ā. 9-11).
- **ERROR**: the Gist at EN 19010 says `In the Āprī-type recitation (अप्पोर्यामे (*apporyāme*))`. KN 21251 prints `ಅಪ್ಪೋರ್ಯಾಮೇ`, and the KN Special Topics at 21279 reads `ಅಪ್ತೋರ್ಯಾಮವೆಂಬ ಯಾಗದಲ್ಲಿ` ("in the sacrifice called Aptoryāma"). The English Special Topics at EN 19033 itself says "Aptoryāma sacrifice". `review/notes.tsv` row w0578 also says the word is read as *Aptoryāma*. The Gist names the wrong rite: Āprī is something else.
- **MINOR**: EN 19033 has `supplementary (atiriktokta) mantra` where KN 21279 has `ಅತಿರಿಕ್ತೋಕ್ಷಮಂತ್ರ` (atiriktoktha). The transliteration is wrong.

### p. 700 (EN 23222–23253; KN 25664–25700)
Checked: 12 Pratipadārtha entries, the Bhāvārtha, the printed English, and Special Topics (Tai. Brā. 3-7-5-4, Ni. 3-9, the samudra etymology).

Findings: none.

### p. 810 (EN 26602–26643; KN 29759–29801)
Checked:
- the printed English
- Special Topics (Sautrāmaṇī, Ā. 3-9)
- Ṛk 6 Saṃhitā, Pada, bhāṣya and Gist
- the first 5 Pratipadārtha entries

Findings: none.

### p. 920 (EN 30610–30635; KN 33817–33849)
Checked: 8 Pratipadārtha entries (including the "or" alternative), the Bhāvārtha, the printed English, and the Sūkta 141 introduction with the Ṛgvidhāna ślokas 50–52.
- **ERROR**: EN 30634 starts the third śloka with `१ ॥ बिल्वोदुंबर…` (IAST `*1 ‖ bilvo…*`). KN 33847 `ಬಿಲ್ವೋದುಂಬರಪಾಲಾಶೀಸ್ತಥಾ…` has no such number. A number has been added where the print has none.
- **MINOR**: EN 30629 adds a `विशेषविषयगळु (Special Topics)` heading to the Sūkta 141 introduction. KN 33840–33842 has only `ನೂರ ನಲವತ್ತೊಂದನೆಯ ಸೂಕ್ತವು` and the garbled `ಜೀ ಱ ಕೆ` (= ಪೀಠಿಕೆ, "Introduction"). The word "Introduction" itself is not rendered. The same pattern is on p. 193.

### p. 1030 (EN 34816–34862; KN 38040–38081)
Checked: the Pada, the Gist, 9 Pratipadārtha entries, the Bhāvārtha and the printed English.

Findings: none.

### p. 1140 (EN 39079–39110; KN 42383–42420)
Checked:
- the Anuvāda (anuvāka 12, 17th sūkta, four Ṛks, ṛṣi, deity, metre, Anukramaṇī)
- the header (Sūkta 168, Adhyāya 8, Varga 26)
- Ṛk 1 and its Gist

Findings: none.

### p. 1250 (EN 43082–43115; KN 46595–46636)
Checked: the printed English, the Sūkta 186 bhāṣya and Gist, the Anuvāda, the header (Varga 44, 3 Ṛks) and Ṛk 1.
- **MINOR**: the heading at EN 43098 reads `##### Anuvāda (Kannada)`. KN 46609 has only `ಅನುವಾದವು—`. "(Kannada)" is a translator label. Other pages are not consistent: p. 1140 (EN 39081) uses `##### Anuvāda`, and p. 1259 (EN 43509) puts `Anuvāda:` inline.

---

## Special Topics pages

### p. 28 (EN 795–831; KN 1190–1226)
Checked: 18 Pratipadārtha entries, the Bhāvārtha, the printed English, and Special Topics (Nirukta 3-20 and 3-21 on *vaitasa*).
- **ERROR**: EN 815 `मे मम तन्नः (*me mama tannaḥ*)—of my body`. KN 1199–1200 has two entries: `ಮೇ-ನನ್ನ । ತನ್ನಃ-ಶರೀರಕ್ಕೆ` (मे—my; तन्नः—to the body). The English merges them and turns the Kannada gloss ನನ್ನ ("my") into an invented Sanskrit headword मम.
- **ERROR**: EN 828 `he has given the two words *śepaḥ*–वैतसः`. KN 1220 has `ಶೇಷಃ-ವೈತಸಃ` (śeṣaḥ). The reading is changed from memory to śepaḥ, against rule 2 of the CLAUDE.md file, and the word has no Devanagari. (The Nirukta quotation at EN 829 keeps शेपो/शेषः as supplied.)

### p. 112 (EN 4014–4033; KN 4417–4453)
Checked: the Bhāvārtha, the printed English, and Special Topics (the Nirukta quotation with Ni. 2-12, the Śantanu, purohita and hotrāya glosses).
- **ERROR**: EN 4025 `Yāska has given the Nirukta for this quarter-verse`. KN 4434 has `ಯಾಸ್ಕರು ಈ ಮುಕ್ಕಿಗೆ ನಿರುಕ್ತವನ್ನು ಹೇಳಿದ್ದಾರೆ`, where ಮುಕ್ಕಿಗೆ is a misprint of ಋಕ್ಕಿಗೆ ("for this Ṛk"). The whole Ṛk is quoted at EN 4026, so "quarter-verse" is a wrong term.
- Not counted: the reference at KN 4441 is printed in Telugu script (`వి. ೨-೧೨`). EN gives "(Ni. 2-12)" with a **NOTE**, which matches notes.tsv row w0110. This is handled correctly.

### p. 193 (EN 7212–7240; KN 7465–7496)
Checked: the Ṛgvidhāna ślokas (Adhyāya 4, ślokas 6–9), the paraphrase, and the Bṛhaddevatā ślokas (Adhyāya 8, ślokas 13–15).
- **MINOR**: EN 7216 adds a `Special Topics` heading. KN 7468–7470 has the sūkta title and `ಜೀರಿಕೆ` (= ಪೀಠಿಕೆ, which EN 7218 renders correctly as "Introduction."). This is the same structural addition as on p. 920.

### p. 263 (EN 9839–9861; KN 10034–10066)
Checked: the end of the Pratipadārtha, the Bhāvārtha, the printed English, and Special Topics (pajreva, ṛbhū na, parpharat, kṣayat).
- **MINOR**: the page heading at EN 9839 splits the entry `आपत् (*āpat*)—` (EN 9837, end of p. 262) from its gloss. The gloss then stands as a loose line, ` has come to the desired place` (EN 9840), not as a list item. KN 10037 continues the gloss in running text, which is normal.
- **MINOR**: the Special Topics headwords at EN 9854 `Pajreva`, 9856 `Ṛbhū na`, 9858 `Vāyuḥ na parpharat` and 9860 `Kṣayat rayāṇāṃ` are in IAST only, with no Devanagari. KN 10054, 10057, 10060 and 10064 print them in script (ಪಜ್ರೇವ, ಋಭೂ ನ, ವಾಯುಃ ನ ಪರ್ಫರತ್, ಕ್ಷಯತ್ ರಯಾಣಾಂ).

### p. 343 (EN 12495–12528; KN 12959–13023)
Checked: the Bhāvārtha, the printed English, and Special Topics (Ni. 8-8 twice, Ṛ. Saṃ. 10-110-3, and five lemma paragraphs).
- **MINOR**: EN 12508 `from the root *iṃdha*` has no Devanagari (KN 12981 `ಇಂಥ`). The same applies to `*yātaḥ*` and `*hūtaḥ*` at EN 12517 (KN 13007 `ಯಾತಶ್ಚ`, `ಹೂತಶ್ಚ`).
- **MINOR**: EN 12511 drops the lemma `आहूयमान ईळितव्यः वंदितव्यश्च—` that heads the KN paragraph at 12990. The English paragraph starts directly with "आजुह्वानः and ईड्यः".

### p. 505 (EN 16748–16763; KN 18557–18594)
Checked: the Bhāvārtha, the printed English, and Special Topics (sahasradhā; pañcadaśāni, the fifteen constituents of the body).

Findings: none.

### p. 619 (EN 20332–20361; KN 22671–22722)
Checked: 13 Pratipadārtha entries (including the bracketed alternative), the Bhāvārtha, the printed English, and Special Topics (the Nirukta on āptya, Ni. 11-2-1).
- **MINOR**: the page boundaries are shifted by one block. The bhāṣya tail and its Gist, which KN prints at the top of p. 619 (KN 22674–22677), sit under EN p. 618 (EN 20323–20330). The Nirukta paraphrase and the reference "(Ni. 11-2-1)", which KN prints on p. 620 (KN 22712–22714), sit under EN p. 619 (EN 20360). No text is lost.

### p. 754 (EN 25057–25067; KN 27793–27827)
Checked: the printed English (end), and Special Topics on asat/sat (the 101 water-names, Ni. 2-24, the root as, the paramāṇu passage).
- **MINOR**: the Sanskrit words in EN 25064 (`sat, sarvam, idam, ṛtam, satyam, gahanam, gabhīram, vyoma`, `Asat, sat`) and the root `as — bhuvi` are in plain or italic IAST, with no Devanagari. KN 27806–27809 prints them in script.

### p. 875 (EN 28865–28907; KN 32118–32157)
Checked: the Pada, the Gist, 10 Pratipadārtha entries, the Bhāvārtha, the printed English, and Special Topics (unmaditāḥ; vātān ā tasthima).

Findings: none.

### p. 1001 (EN 33690–33731; KN 36908–36945)
Checked: the Gist, 18 Pratipadārtha entries, the Bhāvārtha, the printed English and Special Topics.
- **ERROR**: the Gist at EN 33698 says `The deity (Soma) is "prior", that is, first-born, in relation to Savitṛ. For this reason Suparṇa … follows…`. The bhāṣya (KN 36911, `…कादस्माद्देवात्पूर्वः प्रथमभावी सञ्जातः । अतो हेतोः सुपर्णो गरुत्मान्…`) and the KN Pratipadārtha say the opposite. KN 36921–36922 reads `ಪೂರ್ವಃ—ಮೊದಲು । ಜಾತಃ—ಉತ್ಪನ್ನನಾದನು ಆದ್ದರಿಂದ । ಸಃ—ಈ ತಾರ್ಕ್ಷ್ಯನು`. The one born first from Savitṛ is Garutmān/Tārkṣya, not Soma. The Gist reverses the attribution, and it contradicts EN's own Pratipadārtha at EN 33714–33716.

### p. 1162 (EN 39944–39957; KN 43239–43272)
Checked: the printed English, and Special Topics (Astrabudhna and Pṛthu; 10-148; Tai. Brā. 1-7-7-4 and 2-7-5-1; devasava, manuṣyasava and pṛthisava).
- **MINOR**: EN 39951 has `the son of Astrabudhna` and `The name of Astrabudhna`. KN 43250–43251 has `ಅಸ್ತ್ರಬುದ್ಧನ ಪುತ್ರನೆಂದೂ`, `ಅಸ್ತ್ರಬುದ್ಧನೆಂಬುವನ`, i.e. Astrabuddha. The English takes the spelling from the printed English translation, not from the Kannada.
- **MINOR**: EN 39951 has `there he is called Pṛthi instead of Pṛthu`. KN 43255 has `ಪೃಥ್ವಿ ಎಂದು ಕರೆಯಲಾಗಿದೆ` (Pṛthvi). The following KN prose uses ಪೃಥಿ, so the English has normalised the name without a NOTE.

### p. 1259 (EN 43490–43523; KN 46986–47028)
Checked:
- Special Topics (the supplementary mantra)
- the Sūkta 188 bhāṣya and Gist
- the Anuvāda
- the header (Varga 46, 3 Ṛks)
- Ṛk 1
- **MINOR**: the Anuvāda at EN 43509 gives the Anukramaṇī quotation only as an English paraphrase: `"Pra nūnam, a triplet, Āgneya, Śyena, Jātavedasya."`. KN 47005 quotes the Sanskrit `ಪ್ರ ನೂನಂ ತೃಚಮಾಗ್ನೇಯಃ ಶ್ಯೇನೋ ಜಾತವೇದಸ್ಯಂ`, so it should appear in three layers. (The Gist at EN 43507 does carry the Devanagari.)

---

## Whole-volume scans (outside the 24-page sample, not counted in the sample totals)

1. **ERROR (stray Kannada text rendered in Devanagari).** On four pages the Kannada Pratipadārtha and/or Bhāvārtha prose has been left inside the Sāyaṇa-bhāṣya block and transliterated into Devanagari. In each case a proper English Pratipadārtha and Bhāvārtha follow.
   - p. 173: EN 6535–6543 (`(एलैमुद्गलने)के-निन्न । मिथूकृतं-हूडलु …`, with a stray `॥ ८४ ॥`). KN 6760–6769 has the same text inside its `>` block.
   - p. 851: EN 28066–28073 (`॥ प्रतिपदार्थ— यमनपरवागि ॥ सुपलाशे—उत्तमवाद ऎलॆगळिंद…`).
   - p. 857: EN ~28271–28276 (`यमनपरवाद अर्थ / कुमार—ऎलै नचिकेतकुमारने…`).
   - p. 859: EN ~28352.

   The script places these blocks, so the fix belongs in `tools/rv/html_to_kn.py` or in block splitting.
2. **MINOR (Kannada vocatives shown as Sanskrit headwords).** EN 9343 (p. 246) `(ऎलै अश्विनीदेवतॆगळे (*èlai aśvinīdevatègaḷe*))—O Aśvins`, EN 11467 (p. 308) `(ऎलै पणिगळे (*èlai paṇigaḷe*))` and EN 16077 (p. 487) `(ऎलै इंद्रने (*èlai iṃdrane*))`. KN (e.g. 9446) has `(ಎಲೈ ಅಶ್ವಿನೀದೇವತೆಗಳೇ)`, which is Kannada and should simply be rendered "(O Aśvins)".
3. **Telugu script in EN** (4 lines; each is copied from KN):
   - EN 842 and 847 (p. 29, Saṃhitā/Pada `ससు్రुः` = KN 1247, 1252)
   - EN 21435 (p. 651): the whole Pada-pāṭha of Ṛk 4 is the Telugu sentence `కృష్ణుడు, కృష్ణునియొక్క భార్యను…` (KN 23874). It has a NOTE (w0646), but the Pada itself is missing.
   - EN 27152 (p. 824, bhāṣya `प्रो షు सुदाः`; KN 30290)
4. **MINOR pattern (short-e transliteration).** The Kannada short vowel ೆ is carried into Devanagari as ॆ (415 occurrences in EN) and into IAST as `è` (125 occurrences). In Sanskrit words this should be long e. Sample instances: EN 828 `अभीकॆ (*abhīkè*)`, EN 4026 `शमस्यॆ … (*śamasyè*)`, EN 7234 `संख्यॆ (*saṃkhyè*)`, EN 20360 `सप्तॆ (*saptè*)`. This is a shared-tool issue (`publish/tools` transliteration), not a translator one.
5. A scan for "as supplied", `[sic]`, `[?]` and "running head" in EN found nothing. No KN running head was found inside the sampled English text.

---

## Totals (24-page sample)

| | Count |
|---|---|
| Pages checked | 24 (12 evenly spread + 12 with Special Topics; 16 of the 24 have a Special Topics section) |
| Pages with no finding | 7 (20, 700, 810, 1030, 1140, 505, 875) |
| ERROR | 6 (p. 580, p. 920, p. 28 ×2, p. 112, p. 1001) |
| MINOR | 18 |

The whole-volume scans add 1 ERROR pattern (four pages), 1 MINOR pattern (three pages), the 4 Telugu-script lines copied from the source, and the short-e transliteration pattern.
