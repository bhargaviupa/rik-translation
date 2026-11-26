# Vol 1 prose pages ↔ Sāyaṇa's Bhāṣya-bhūmikā in the Wikisource export (Nov 25 2026)

Method: `python3 tools/rv/bhumika_map.py 1` aligns the Sanskrit lines of each printed page (Kannada script, converted to Devanagari, letters only) with `refs/wikisource/export/Rigveda_Devanagari_M00.md` (rapidfuzz, score ≥ 85); per page in `bhumika_map.tsv`. 188 of 720 pages have a match. A heuristic, not a proof: a page may carry Bhūmikā text and not be found when its Sanskrit lines are short or broken.

| Vol 1 printed pages | Export page (पृष्ठम्) | Remark |
|---|---|---|
| 346–390 | 89–98 | first chapters of the Bhūmikā (the opening verses, the purpose of the Veda, the definition of Veda) |
| 394–413 | 98–102 | |
| 418–420, 425–431 | 103–105 | |
| 438–472 | 105–112 | |
| 476–592 | 113–137 | the later chapters |
| 3, 8–11 | scattered (89–122) | quotations in the introduction, not the Bhūmikā itself |

Before p. 346 the prose (preface, introduction, the lives and branches of the Veda) is the editor's own text. The export is "वेदभाष्यभूमिकासङ्ग्रहः", a collection of Sāyaṇa's Bhūmikā (pp. 89–137 of its source, 256 KB). Whether the export is complete against the Kannada's Sanskrit has not been checked.
