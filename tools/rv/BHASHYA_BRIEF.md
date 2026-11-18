# Brief: English of the Sāyaṇa-bhāṣya (for the bhāṣya reader)

You render Sāyaṇa's Sanskrit commentary on the Ṛgveda into English, one sūkta at a time. Your reader knows English, not Sanskrit, and wants to follow everything Sāyaṇa says.

## The steps (VOL and M.S are in your task, e.g. 17 and 3.40)
1. `python3 publish/bhashya_book.py VOL --task M.S` prints the task file and the file you are to write.
2. Read the task file. For the sūkta's introduction and for each Ṛk it holds, in Devanagari, the Saṃhitā-pāṭha, the Pada-pāṭha and the Sāyaṇa-bhāṣya block (lines starting `>`). That is all you have, and all you may use.
3. Write the English file named in step 1.
4. `python3 publish/bhashya_check.py VOL M.S` until its last line begins with `VERIFIED`.
5. Commit and push **only your English file**: `git add <file> && git commit -m "Bhāṣya English: Vol VOL, M.S" && git push` (on a network error wait and push again, up to 4 times; never force). Read no other file of the repository and change none.
6. Report in three lines: the file, the check's last line, the commit as `git log --oneline -1` shows it.

## The file you write
Exactly these headings, in the order of the task file:

```
## Introduction
(English of Sāyaṇa's introduction to the sūkta; leave this heading out only if the task file has no bhāṣya block before Ṛk 1)

## Ṛk 1
(English of the whole bhāṣya on Ṛk 1)

## Ṛk 2
…
```

Under a heading, plain paragraphs only. No other headings, no lists, no tables.

## Rules
1. **Everything, in Sāyaṇa's order.** The gloss of each word, the alternative explanations (`यद्वा`), the ritual use, every quotation, and the **grammatical part at the end** (derivations, suffixes, substitutions, accent). The grammar is translated too: say which word is being derived, from which root in which sense, by which suffix or rule, and what accent results. Do not summarise it as "the rest is grammar".
2. **Nothing added.** Only what the block says. No fact from memory or from another edition: no sūtra numbers, no chapter-and-verse where the block gives none, no opinions of other commentators, no remarks of your own. **A word Sāyaṇa does not gloss is not glossed by you**: cite it and go on (if the block says `इरां दृणाति` without saying what `इरा` is, you do not say it either). A reference the block gives is kept with the block's numbers; the check rejects any numbered reference that is not in the unit.
3. **The supplied text is the base.** Never correct a letter or a number. The Sanskrit you are given was read by machine and has misread letters. Wherever a word in the block is damaged, differs from the same word in the Ṛk or the Pada-pāṭha, or cannot be construed, translate what can be translated and put `**NOTE**{your question in one sentence}` right there. This holds also when you are sure what was meant: say it in the NOTE, not silently in the translation. One NOTE for each such place.
4. **Sanskrit is copied, never typed.** To cite a Sanskrit word or passage, copy it from this unit's blocks between `⟦` and `⟧`, letter for letter: `⟦इंद्र⟧`. A script adds the transliteration and checks that every `⟦ ⟧` occurs in the unit. Outside `⟦ ⟧` there must be no Devanagari at all.
5. **No Sanskrit in Roman letters inside brackets.** Do not write glosses such as `(ramate, krīḍati)` or `(sākṣāt)`: either cite the word with `⟦ ⟧` or give only the English. The check rejects them. Proper names (Sāyaṇa, Yāska, Viśvāmitra) and the standing technical terms of ritual and grammar (Soma, hotṛ, śastra, udātta, guṇa, laṭ, kvip) may stand in running English in Roman letters, without brackets: "the present tense, laṭ". Spell them with care; nothing checks them.
6. Plain, exact English. Full sentences. A quotation from another text is first cited (`⟦ ⟧`), then translated. Words like `ṣāṣṭika` ("taught in the sixth book") are translated by their sense, not letter by letter.

## What the check cannot see
Whether your English is right. It checks only the form: headings, copied Sanskrit, references, brackets. Read each unit once more against the block before you run it.
