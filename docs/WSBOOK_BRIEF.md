# Brief: English of Sāyaṇa's bhāṣya from the Wikisource text (Vol 11 experiment, Nov 21 2026)

Read `tools/rv/BHASHYA_BRIEF.md` rules 1, 2, 4, 5, 6 and 8 (everything in Sāyaṇa's order and nothing added or shifted; Sanskrit copied in `⟦ ⟧`, never typed; references copied; no Roman-letter Sanskrit in brackets; plain exact English). They apply unchanged. Only what differs is here.

## What is different
1. **The base is the text of sa.wikisource.org**, given to you in a task file unit by unit, each unit under its number `SBh M.S.R.U` (e.g. `SBh 1.137.2.3`: maṇḍala 1, sūkta 137, Ṛk 2, unit 3; Ṛk 0 = Sāyaṇa's introduction). You translate the **units as they stand**. It is a clean text, but it is a wiki and may have a typo (it has one in a Pada line). Never alter it. Where a word is plainly a typo, translate the word that is meant and put `**NOTE**{the question, in one sentence}` there; where the sense is doubtful, translate what can be translated and put a NOTE. There is **no `## Readings` section** and no other file or web page is to be used to settle the text (do not run `sayana_ref.py`; do not search).
2. **The English file has one section per unit**: `## SBh 1.137.2.3`, in the order of the task file, each with its English (plain paragraphs only, no lists, headings or tables). Every unit gets its own English: do not merge units and do not leave one out. Where a unit is only a quoted sūtra or text, cite it with `⟦ ⟧`, then say in English what it is and what it lays down.
3. **The quotation marks on the page** (“ ” before a word of the Ṛk) mark the words of the Ṛk that Sāyaṇa is explaining; they are not part of what you cite. Cite the word itself.
4. **An earlier English draft** of each sūkta exists in `vol11/bhashya_en/M1_S<sss>.md`, made from the volume's machine-read text (which has many misread letters) and by the Ṛk, not by the unit. You may read it as a help. You may keep a sentence of it only after you have checked that sentence against the Wikisource unit, word by word, and it says what the unit says; where the draft differs from the unit, the unit wins. Do not copy its `## Readings` or its remarks. If the draft and the unit disagree in a way that matters, that is not a NOTE: the unit is the base.
5. The English is for a reader who knows English, not Sanskrit, and wants to follow everything Sāyaṇa says, the grammar included (BHASHYA_BRIEF rule 1): say which word is derived, from which root in which sense, by which suffix or rule.

6. **A final consonant printed without virāma** (`चित`, `धृतत्वात`, `तदाश्रयत्वात`) is how this edition prints, not an error (user, Nov 22 2026): translate the word, put no NOTE and make no remark. Other missing letters (a final nasal, a whole syllable) are still typos for a NOTE.

## The steps for each sūkta of your task (M and S as numbers, e.g. `1 137`)
1. `python3 tools/rv/wsbook.py task M S` writes the task file and prints its path and the path of your English file.
2. Read the task file; write the English file.
3. Read each unit of your English once more against its Sanskrit, asking two questions only. (a) Does the unit say this? Anything it does not say (an accent, a rule, a reason, a gloss, an epithet) is deleted. (b) Is every word and clause of the unit rendered, `अपि`, `एव`, `यद्वा` and the alternatives included? What is missing is added.
4. `python3 tools/rv/wsbook.py check M S` until its last line is `VERIFIED`.
5. Report: for each sūkta, the check's last line, the number of NOTEs, and anything the editor should know. **Do not commit or push; change no file but your English files; read no other file of the repository** except the two briefs, your task files and the earlier drafts named above.
