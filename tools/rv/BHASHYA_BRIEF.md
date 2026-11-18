# Brief: English of the Sāyaṇa-bhāṣya (for the bhāṣya reader)

You render Sāyaṇa's Sanskrit commentary on the Ṛgveda into English, one sūkta at a time. Your reader knows English, not Sanskrit, and wants to follow everything Sāyaṇa says. The English must be right the first time: it will be printed, and no script can check its meaning.

## The steps (VOL and M.S are in your task, e.g. 17 and 3.40)
1. `python3 publish/bhashya_book.py VOL --task M.S` prints the task file and the file you are to write.
2. Read the task file. For the sūkta's introduction and for each Ṛk it holds, in Devanagari, the Saṃhitā-pāṭha, the Pada-pāṭha and the Sāyaṇa-bhāṣya block (lines starting `>`).
3. Write the English file named in step 1 (a long sūkta may be written in parts: first Ṛks, then add the rest).
4. Read each unit of your English once more against its block: every clause of the Sanskrit accounted for, nothing added.
5. `python3 publish/bhashya_check.py VOL M.S` until its last line begins with `VERIFIED`.
6. Report in three lines: the file, the check's last line, and whether the reference text opened. **Do not commit or push**; read no other file of the repository and change none.

**If your task names a whole volume** (VOL only): work through it sūkta by sūkta. `python3 tools/rv/bhashya_run.py next 1 VOL` names the next sūkta; do steps 1–5 for it; then `git add <your English file> && git commit -m "Bhāṣya English: Vol VOL, M.S" && git push` (on a network error wait and push again, up to 4 times; never force; add no other file). Then take the next. Each sūkta gets the same care as the first: do not hurry the later ones. Stop when `next` prints `ALL DONE` for the volume, or after the number of sūktas your task allows, and report: the sūktas done with their commits as `git log --oneline` shows them, the check's last line for each, the NOTE and Readings totals, and anything the editor should know.

## The file you write
Exactly these headings, in the order of the task file:

```
## Introduction
(English of Sāyaṇa's introduction to the sūkta; leave this heading out only if the task file has no bhāṣya block before Ṛk 1)

## Ṛk 1
(English of the whole bhāṣya on Ṛk 1)

## Ṛk 2
…

## Readings
- Ṛk 5: ⟦दधिष्क⟧ → ⟦दधिष्व⟧ — the Pada-pāṭha of this Ṛk
- Ṛk 9: ⟦नरावतम⟧ → parāvatam — the Ṛk has ⟦परावतं⟧
```

Under a unit heading, plain paragraphs only: no other headings, no lists, no tables. `## Readings` is the last section and is left out if you have nothing to log (see rule 3).

## Rules
1. **Everything, in Sāyaṇa's order.** The gloss of each word, the alternative explanations (`यद्वा`), the ritual use, every quotation, the closing `इति भावः` remarks, and the **grammatical part at the end** (derivations, suffixes, substitutions, accent). The grammar is translated too: say which word is being derived, from which root in which sense, by which suffix or rule, and what accent results. Do not summarise it as "the rest is grammar".
2. **Nothing added, nothing shifted.** Only what the block says. No fact from memory or from another edition: no sūtra numbers, no chapter-and-verse where the block gives none, no opinions of other commentators, no remarks of your own.
   - A word Sāyaṇa does not gloss is not glossed by you: cite it and go on (if the block says `इरां दृणाति` without saying what `इरा` is, you do not say it, and you do not replace it by another word).
   - Give Sāyaṇa's gloss, not the dictionary's: where he glosses `मधोः` by `मदकरस्य`, write "intoxicating", not "honey"; where he says `यशोऽन्नं`, yaśas is "food", not "glory".
   - Keep each word with what Sāyaṇa attaches it to: an accusative epithet of the Soma is not turned into a vocative of Indra. Keep the voice and the causative (`दर्शयति` is "shows", not "sees"), the particles (`एव` "alone/only", `यतः` "since") and the possessives (`नः … अस्मदीयं` is "our", not "for us").
3. **The supplied text is the base; it is never altered, and nothing is settled silently.** The Sanskrit you are given was read by machine and has misread letters. For a damaged or doubtful word:
   - **If the intended word is certain** — it stands in the Ṛk or the Pada-pāṭha of the unit, or the reference text has it (rule 7), or the grammar and context of the block leave no other possibility — translate the intended word and log it in `## Readings`: `- Ṛk N: ⟦the letters as supplied⟧ → the reading you translated — the basis`. The reading is put in `⟦ ⟧` if it stands in the unit; otherwise in Roman letters. No mark in the text.
   - **If it is not certain**, translate what can be translated and put `**NOTE**{your question in one sentence}` at that place. A NOTE is for a doubt that remains, not for every misprint.
   - A difference between the Saṃhitā and the Pada-pāṭha that does not touch the bhāṣya is not your concern: no reading, no NOTE.
4. **Sanskrit is copied, never typed.** To cite a Sanskrit word or passage, copy it from this unit's blocks between `⟦` and `⟧`, letter for letter as supplied (misread letters included): `⟦इंद्र⟧`. A script adds the transliteration and checks that every `⟦ ⟧` occurs in the unit. Outside `⟦ ⟧` there must be no Devanagari at all. Cite the word being explained and each quotation; do not wrap whole sentences of Sāyaṇa's own prose in `⟦ ⟧` in place of translating them.
5. **References are copied too.** A reference in the block (`आ. ५-१०`, `नि. ६-१४`, `पा. २-३-४`) is copied with `⟦ ⟧` exactly as it stands, abbreviation and numbers, where Sāyaṇa has it: `(⟦आ. ५-१०⟧)`. Do not write an English abbreviation for it; a script will put the series' uniform abbreviation there.
6. **No Sanskrit in Roman letters inside brackets.** Not `(ramate, krīḍati)`: either cite the word with `⟦ ⟧` or give only the English. Proper names (Sāyaṇa, Yāska, Viśvāmitra) and the standing technical terms of ritual and grammar (Soma, hotṛ, śastra, udātta, guṇa, laṭ, kvip) may stand in running English in Roman letters, without brackets. Spell them with care (`kṣi`, not `ki`); nothing checks them.
7. **The reference text and the web, to settle the text.** (User, Nov 18 2026.)
   - For every sūkta, run `python3 tools/rv/sayana_ref.py M S` once (M and S as numbers: `1 138`). It prints Sāyaṇa's bhāṣya on the sūkta from another edition (vishvasa.github.io), block by block, and nothing else. Read it beside your task file. It is a clean text: use it to see what a misread word, a damaged passage, a damaged sūtra or quotation, or a doubtful reference in the supplied text was meant to be. Log each such place in `## Readings` with the basis `reference text`.
   - It is another edition. Its spelling, sandhi and nasals differ from the supplied text: that is not a reading and is not logged. **Where it differs in content** — a word of different meaning, a clause, a quotation or a reference (or its numbers) that the supplied text has otherwise, lacks, or has in addition — the supplied text is translated and the difference is put as a `**NOTE**{…}`, every time, references included. A difference of wording that leaves the sense the same (a compound against its analysed form, a particle more or less, another word order) gets no NOTE and no reading. What only the reference text has is never added to the English.
   - If the reference text has an introduction to the sūkta and your task file has no bhāṣya block before Ṛk 1, do not translate it; put `**NOTE**{the supplied text has no introduction to this sūkta; the reference text has one}` at the very start of Ṛk 1.
   - Do not open that site's pages in any other way: they also carry other people's translations, which you must not read or use. If the helper fails, go on without it and say so in your report.
   - For a quoted sūtra or text that is still unclear you may search the web or open `ashtadhyayi.com` or `gretil.sub.uni-goettingen.de` with `curl`; name the site in the basis. Never copy a translation. What stays open becomes a NOTE.
   - In the text a reference is still copied as supplied (rule 5); its corrected form goes in the Readings line.
8. Plain, exact English. Full sentences. A quotation from another text is first cited (`⟦ ⟧`), then translated. Terms like `षाष्टिक` are rendered by their sense ("taught in the sixth book").

## What the check cannot see
Whether your English is right. It checks only the form: headings, copied Sanskrit, references, brackets, the Readings lines. Step 4 is yours.
