# Vol 29 — independent QA sample (Kannada → English)

Date: 2026-11-25 (finished 2026-11-26)

## Method

- **Compared:** for each of the 24 sampled printed pages, the Kannada page section of
  `vol29/Rigveda_Samhita_Vol29_Kannada_Text.md` (from `<!-- printed N -->` to the next marker) against the
  English page section of `vol29/Rigveda_Samhita_Vol29_English_Translation.md` (from `### Printed p. N` to the next
  heading of that kind). I read every Kannada prose sentence on the page next to its English: Pratipadārtha
  entries (one by one), Bhāvārtha, the printed English translation, Anuvāda/introductions, Special Topics (Viśeṣa-viṣaya),
  the quotations and their translations, and the reference numbers in brackets.
- **Looked for:** changed or missing numbers and references, wrong names, terms and quotations, reversed negation or
  attribution, omissions and additions, and translator remarks (only `**NOTE**` and `**GLOSS**` are allowed).
- **Not judged, as instructed:** the Sanskrit blocks (Saṃhitā, Pada, Sāyaṇa-bhāṣya), Devanagari/IAST lines and the
  Gists of the bhāṣya. Where a page's Kannada begins or ends mid-sentence, I checked only the part on the page. Where a
  block on the Kannada page sits in a neighbouring English page section, I checked it there (p. 262: the end of the
  Bhāvārtha is in the p. 261 section, English line 6850; present).
- **Volume-wide block check (by count):** Ṛk headings 308 in Kannada and 308 in English; Saṃhitā 309/309, Pada 308/308,
  Sāyaṇa-bhāṣya 332/332, Pratipadārtha 308/308, printed English translation 308/308, Special Topics 109/109. Bhāvārtha
  heading 303 (Kannada, some headings are garbled in the supplied text) against 308 (English). No block is missing from
  the volume by these counts. I did not compare content outside the 24 pages.
- `vol29/html/rig_29.md` was not needed: the Kannada file was clear on every point raised below.
- I made no change to any file except this report. No git commands.

## Pages checked

| # | printed p. | sample | content | result |
|---|---|---|---|---|
| 1 | 30 | A | Special Topics on Aditi and the earth: Ṛgveda, Vājasaneyi, Atharva and Śatapatha quotations | OK (all reference numbers as printed; impossible "18-92-11" kept with NOTE) |
| 2 | 95 | A | Special Topics: Viśvāmitra–rivers dialogue (3.33) in Kannada prose, Ṛks 4–11 | 1 NOTE |
| 3 | 188 | A | Special Topics on Viśvakarman/Prajāpati, Bṛhadāraṇyaka 1-4-1 | 1 NOTE |
| 4 | 262 | A | English translation and Special Topics (Āśvalāyana, Nirukta 10-26) | OK |
| 5 | 372 | A | Special Topics: stomas and viṣṭutis, the numbers table | OK (all 9 numbers and the viṣṭuti lists match) |
| 6 | 455 | A | Phala-śruti end, Anuvāda of the bhāṣya on sūkta 86 (who speaks which Ṛks) | OK (all Ṛk numbers match; attribution of the speeches correct) |
| 7 | 533 | A | Special Topics: Nirukta 7-24 with Durgācārya, uttarāyaṇa/dakṣiṇāyana | OK |
| 8 | 607 | A | Special Topics: Ṛgveda passages on Indra's greatness | OK (references as printed, garbled ones with NOTE) |
| 9 | 718 | A | English translation, Special Topics on Puruṣa-sūkta 1, Śvetāśvatara quotations | OK |
| 10 | 835 | A | Special Topics: daśahotṛ, Sāyaṇa on citti/citta | OK |
| 11 | 940 | A | Special Topics: Śatapatha 6-2-1 on the five animals | OK |
| 12 | 1012 | A | Ṛk 5 of sūkta 94: Pratipadārtha (all 15 entries), Bhāvārtha | OK |
| 13 | 2 | B | Introduction to sūkta 72 (Ādityas, sat/asat) | 1 MINOR |
| 14 | 74 | B | Bhāvārtha, English translation, Special Topics (Nirukta on vayaḥ, suparṇa) | OK |
| 15 | 124 | B | Pratipadārtha (all 14), Bhāvārtha, Special Topics (cross-reference Part 14 pp. 626-631) | OK |
| 16 | 211 | B | Pratipadārtha (all 15), Bhāvārtha, Special Topics (house-building metaphor) | OK |
| 17 | 302 | B | Pratipadārtha (end), Bhāvārtha, Special Topics (two reasons why the Lord is not known) | OK |
| 18 | 364 | B | Pratipadārtha (all 13), Bhāvārtha, Special Topics (Nirukta 11-5) | 1 NOTE (in a Gist) |
| 19 | 411 | B | Pratipadārtha (end), Bhāvārtha, Special Topics (Āśvalāyana Gṛhya 1-8-1) | OK |
| 20 | 434 | B | Pratipadārtha (all 15), Bhāvārtha, Special Topics (Āśvalāyana Gṛhya 1-8-9) | OK |
| 21 | 474 | B | Pratipadārtha (all 14), Bhāvārtha, Special Topics (Yāska on vṛṣākapāyī) | OK |
| 22 | 573 | B | Pratipadārtha (all 12), Bhāvārtha, Special Topics (Nirukta 7.31, Mātariśvan's question) | 1 ERROR, 1 MINOR |
| 23 | 879 | B | Special Topics on the sarvamedha (Śatapatha 13-7-1) | 2 MINOR |
| 24 | 1009 | B | Pratipadārtha (end), Bhāvārtha, Special Topics (green mouths of the stones) | 1 MINOR |

No translator remark outside `**NOTE**`/`**GLOSS**` was found in the prose of the 24 pages; the one remark found is in a
Gist (finding 7).

## Findings

### 1. ERROR — p. 573, English line 16952: who asks whom is reversed

Kannada (Kannada file line 21265–21268):
> ಮಾತರಿಶ್ವನು (ವಾಯುವು) ಒಬ್ಬ ಪುರುಷನನ್ನು ಕುರಿತು-ದೇವತೆಗಳ ಹೋತೃವಾದ ಅಗ್ನಿಗೆ ಇರುವ ವಿಜ್ಞಾನವನ್ನು … ಮನುಷ್ಯಹೋತೃವಾದ ಬ್ರಾಹ್ಮಣನು ಧರಿಸಬಲ್ಲನೇ ಎಂದರೆ ತಿಳಿಯಬಲ್ಲನೇ ಎಂದು ಕೇಳಲಾಗಿ ಅದಕ್ಕೆ ಆ ಪುರುಷನು ಈ ರೀತಿ ಪ್ರತ್ಯುತ್ತರವನ್ನು ಹೇಳಿರುವನು.

("Mātariśvan (Vāyu), addressing a man, asked whether …; when it was asked, that man gave this reply." The reply then
addresses Mātariśvan: "ಎಲೈ ಮಾತರಿಶ್ವನೇ".)

English:
> Mātariśvan (Vāyu) is asked by a man whether the Brahman, …

The English makes the man the questioner and Mātariśvan the one asked, and then says "That man has given this reply",
which no longer fits.

Replacement:
- old: `Mātariśvan (Vāyu) is asked by a man whether the Brahman, the human hotṛ who takes part in the sacrifice, can bear, that is, can know,`
- new: `Mātariśvan (Vāyu) asked a man whether the Brahman, the human hotṛ who takes part in the sacrifice, can bear, that is, can know,`

### 2. MINOR — p. 573, English line 16946: "this Ṛk" left out

Kannada (line 21261): `ಈ ಮುಕ್ಕಿಗೆ ಯಾಸ್ಕರ ನಿರ್ವಚನವು ಈರೀತಿ ಇದೆ—` (ಮುಕ್ಕಿಗೆ is a misprint for ಋಕ್ಕಿಗೆ, "for this Ṛk").
English: `The explanation of this by Yāska is as follows:`

Replacement:
- old: `The explanation of this by Yāska is as follows:`
- new: `Yāska's explanation of this Ṛk is as follows:`

### 3. MINOR — p. 2, English lines 52 and 54: the same word ಸೂಕ್ಷ್ಮವಾಗಿ rendered in two opposite ways

Kannada (lines 74, 78): `… ನಾವು ಹಿಂದೆ ಸೂಕ್ಷ್ಮವಾಗಿ ಬರೆದಿದೇವೆ` and `… ವಿಶೇಷವಿಷಯಗಳಲ್ಲಿ ಸೂಕ್ಷ್ಮವಾಗಿ ವಿವರಿಸುತ್ತೇವೆ.`
English: line 52 "we have written briefly earlier"; line 54 "We shall explain these matters in detail in the Special
Topics". In this author's usage ಸೂಕ್ಷ್ಮವಾಗಿ means "briefly"; "in detail" is the opposite.

Replacement:
- old: `We shall explain these matters in detail in the Special Topics of the respective Ṛks.`
- new: `We shall explain these matters briefly in the Special Topics of the respective Ṛks.`

### 4. MINOR — p. 879, English line 24143: printed numeral "(10)" dropped; "metre" added

Kannada (line 31447): `ಅನ್ನವು ವಿರಾಡ್ರೂಪದಲ್ಲಿರುತ್ತದೆ ವಿರಾಟ್ಟು ದಶಾಕ್ಷರ (೧೦) ವುಳ್ಳದ್ದು.`
English: `Food is in the form of the Virāṭ; the Virāṭ metre has ten syllables.`
The print gives the number as a figure in brackets; the English drops it (the rule is that numbers follow the Kannada).
"metre" is not in the Kannada (harmless, since Virāṭ is a metre).

Replacement:
- old: `Food is in the form of the Virāṭ; the Virāṭ metre has ten syllables.`
- new: `Food is in the form of the Virāṭ; the Virāṭ has ten syllables (10).`

### 5. MINOR — p. 879, English line 24137: the author's bracketed aside lost its brackets

Kannada (lines 31434–31438): the paragraph `[ಪುರುಷಮೇಧ ಮತ್ತು ಸರ್ವಮೇಧಗಳ … ಪುರುಷಮೇಧದ ಸ್ವರೂಪವನ್ನು ವಿವರಿಸಲಾಗುತ್ತದೆ.]` is printed in
square brackets, marking it as the author's aside within the account. The English gives it as an ordinary paragraph.

Replacement (two edits, both strings occur once):
- old: `Although the ritual procedures of the Puruṣa sacrifice` → new: `[Although the ritual procedures of the Puruṣa sacrifice`
- old: `will be described in the Special Topics of the Ṛk.` → new: `will be described in the Special Topics of the Ṛk.]`

### 6. MINOR — p. 1009, English line 28305: ಪಚ್ಚೆವರ್ಣ rendered "pale green"

Kannada (line 36430): `ಸೋಮಲತೆಗಳೂ ಅವುಗಳಿಂದ ಹೊರಸೂಸುವ ರಸವೂ ಪಚ್ಚೆವರ್ಣ ಎಂದರೆ ಹಸಿರುವರ್ಣದ್ದಾಗಿರುವುವು.`
English: `the Soma plants and the juice that flows out from them are pale green, that is, green in colour.`
ಪಚ್ಚೆ is "emerald", not "pale". In the Bhāvārtha on the same page (line 28296) ಪಚ್ಚೆವರ್ಣ is rendered "green".

Replacement:
- old: `are pale green, that is, green in colour`
- new: `are emerald-coloured, that is, green in colour`

### 7. NOTE — p. 364, English line 9610: a translator remark inside a Gist

`(The sentence continues.) ...in accordance with the śruti …` — this is a translator's remark. Gists were outside the
scope of this check, but the rule says the English carries no translator remarks. It is the only occurrence in the
volume (counted with grep). Proposed:
- old: `(The sentence continues.) ...in accordance` → new: `...in accordance`

### 8. NOTE — p. 188, English line 5356: a Kannada misprint corrected silently

Kannada (line 6948–6949): `ಲೋಕದಲ್ಲಿ ಉದಕಗಳು ಶಿಥಿಲವೂ ಅಧ್ರುವಗಳೂ ಆದುದರಿಂದ ಅದರಿಂದ ಉತ್ಪನ್ನವಾದ ಸಕಲ ಭೂತಗಳೂ ಅಶಿಥಿಲವೂ ಅಧ್ರುವಗಳೂ ಆದವು.`
English: `In the world, water is loose and unstable; therefore all beings produced from it became loose and unstable.`
The print has ಅಶಿಥಿಲ ("not loose") for the beings, which contradicts the reasoning; the English gives the evident
reading "loose" with no mark. The meaning in English is right; for the editor: if the volume's practice is to list
such Kannada misprints (`kn_misprints.tsv` in the second-pass convention), this one is not listed. No change to the
English is proposed.

### 9. NOTE — p. 95, English line 2192: "rim of the wheel" for ರಥಚಕ್ರದ ಇರುಚಿ

Kannada (line 3433): `ನಮ್ಮ ರಥಚಕ್ರದ ಇರುಚಿಯ ಮಟ್ಟಕ್ಕಿಂತಲೂ ಕೊಂಚ ಕಡಿಮೆ ಮಟ್ಟದಲ್ಲಿ ಪ್ರವಾಹವನ್ನು ನಿಯಮನಮಾಡಿರಿ.`
English: `Regulate the current to a level a little below the rim of the wheel of our chariot.`
ಇರುಚಿ occurs only here in the volume and its meaning is not certain to me; the Ṛk paraphrased (3.33.9, adho akṣāt)
speaks of the axle, so "rim" may be wrong. For the editor to decide; if the word means axle/hub:
- old: `Regulate the current to a level a little below the rim of the wheel of our chariot.`
- new: `Regulate the current to a level a little below the axle of the wheel of our chariot.`

## Summary

- **ERROR: 1** — p. 573 (line 16952): who asks whom is reversed (Mātariśvan asks the man in the Kannada).
- **MINOR: 5** — p. 573 "this Ṛk" left out; p. 2 ಸೂಕ್ಷ್ಮವಾಗಿ given as "in detail"; p. 879 numeral "(10)" dropped;
  p. 879 brackets of the author's aside lost; p. 1009 "pale green" for ಪಚ್ಚೆವರ್ಣ.
- **NOTE: 3** — p. 364 translator remark in a Gist; p. 188 silent correction of ಅಶಿಥಿಲ; p. 95 meaning of ಇರುಚಿ.

18 of the 24 pages had no finding. All reference numbers, Ṛk numbers and table numbers on the 24 pages agree with the
Kannada, apart from the dropped "(10)" (finding 4). Every Pratipadārtha entry on the sampled pages is present. The
checked part was the Kannada prose; the Sanskrit blocks and Gists were not judged.
