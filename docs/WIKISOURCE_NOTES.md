# Wikisource reference: notes on the text (Saṃhitā, Pada, Sāyaṇa-bhāṣya)

*Written Nov 23 2026 from the work of the Sāyaṇa-bhāṣya session. Decision of the user: the text of sa.wikisource.org is the correct base for the Saṃhitā, the Pada-pāṭha and Sāyaṇa's bhāṣya. Where a volume's machine-read text differs from it, the volume's text is the one that was misread. Nothing here has been compared with the printed edition.*

Files and tools: `refs/wikisource/raw/` (the raw wikitext, `tools/rv/ws_pull.py`), `refs/wikisource/index/ws.sqlite` (rebuilt with `python3 tools/rv/ws_index.py build`; not committed), `refs/wikisource/index/checks.tsv`, `tools/rv/ws_vs_refmandala.py` (comparison with `refs/mandala/`), `publish/tools/ws_layers.py` (prototype for the print build, off by default). Reference points: **M.S** sūkta, **M.S.R** Ṛk, **M.S.R.P** paragraph of Sāyaṇa's text (R = 0 is his introduction to the sūkta).

## Spellings that are conventions, not differences of text

1. **न्त्स.** Wikisource writes a त् between a final न् and an initial स: `महान्त्सुपारः` (1.4.10), `मघवन्त्सुवीर्यं` (1.127.11), `अस्मिन्नहन्त्सत्पतिः` (1.100.6), `तान्त्सुकृतो` (1.147.3). It does this 91 times and once with a space. Of the places where Wikisource differs from `refs/mandala` in letters, 87 are an extra त् (68 of them checked word by word: a final न् before स). `refs/mandala` writes the same context three ways: joined `न्स`, spaced `न् स` (38), and `न्त्स` (5). Aufrecht's critical edition (GRETIL, fetched Nov 23 2026) prints it without the त् (`mahān supāraḥ`, `maghavan suvīryam`). It is the traditional spelling of the Śākala recitation text, and Sāyaṇa's own text on Wikisource quotes Ṛk words in this form (6.50.2.1 `पितॄन्त्सुविदत्राँ`, 4.1.3.2 `विद्वान्त्स`). The Pada-pāṭha has no त् (`मघवन् । सुवीर्यम्`): the त् exists only in the connected Saṃhitā. **Decision: keep Wikisource.** A volume whose own text writes `न्स` shows this convention, not a different text. In IAST the Wikisource form is `mahāntsupāraḥ`. (The account of the rule itself is from memory; the evidence above is what was checked.)
2. **Nasals.** `refs/mandala` writes न्, म्, ञ्, ङ् before a consonant, and म् at the end of a word; Wikisource writes ं. 3,377 Ṛks differ from `refs/mandala` only in this and in the next convention.
3. **Place of an accent mark** next to ं, ँ, ः: before it in `refs/mandala` (`याभि॑ः`), after it in Wikisource (`याभिः॑`).
4. **A final consonant printed without virāma** in Sāyaṇa's text (`चित`, `धृतत्वात`) is how the edition prints (user, Nov 22 2026).
5. **रृ against र्ऋ** (`दु॒रेवै॒रृषिं` in `refs/mandala`, `दु॒रेवै॒र्ऋषिं` on Wikisource; 37 places) and an **ऊ** that Wikisource has and `refs/mandala` lacks (8.47.1 and 17 more places): Wikisource kept (user, Nov 23 2026).
6. **The avagraha ऽ** marks the break of a compound in the Pada (`अद्रि॑ऽभिः`) and is printed as a hyphen in IAST (`adri-bhiḥ`).

## Known defects of the source pages (flagged, not supplied from elsewhere)

- **5.5.11:** the accented Saṃhitā lacks its first line (`स्वाहा॒ग्नये॒ वरु॑णाय॒ स्वाहेन्द्रा॑य म॒रुद्भ्य॑ः` is in `refs/mandala`; the page has it only in the plain verse). The Pada lines under 11 are those of Ṛk 10 repeated.
- **9.97 Ṛk 10:** the accented Saṃhitā is missing; the plain lines stand in its place.
- **10.27 Ṛk 1:** the first accented Pada line is missing. The index cannot place this Ṛk; its commentary is filed with the sūkta introduction.
- **Pada typos:** for example the Pada of 1.137.1 reads `सुसुम` for `सुषुम`.
- **Missing sūkta introductions in the volumes:** the supplied text of Vol 11 lacks Sāyaṇa's introduction to about ten sūktas; Wikisource has them.

## What was checked

- The index against an earlier scrape of the HTML pages of the 21 sūktas of Vol 11: the bhāṣya words are identical.
- The index against `refs/mandala/`, all 10,552 Ṛks: 6,974 identical letter for letter and accent for accent; 3,377 identical except conventions 2 and 3 above; 23 same letters with different accent marks; 178 differ in letters (188 places: extra त् 87, रृ/र्ऋ 37, ऊ 18, the rest few). Listed in `refs/wikisource/index/vs_refmandala.tsv`.
- Wikisource and `vishvasa.github.io` agree almost everywhere (they are one text, not two independent checks).
- Not checked: the printed edition; any independent edition of the Pada-pāṭha or of Sāyaṇa's text.
