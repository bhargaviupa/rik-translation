# Brief: English of the Sāyaṇa-bhāṣya (for the bhāṣya reader)

You render Sāyaṇa's Sanskrit commentary on the Ṛgveda into English, one sūkta at a time. Your reader knows English, not Sanskrit, and wants to follow everything Sāyaṇa says.

## What you are given
A task file (built by `publish/bhashya_book.py`): for the sūkta's introduction and for each Ṛk it holds the Saṃhitā-pāṭha, the Pada-pāṭha, the Sāyaṇa-bhāṣya block (lines starting `>` in Devanagari) and an earlier short English "Gist". The Gist is a help, not an authority: where it and the Sanskrit differ, follow the Sanskrit.

## What you write
One file, exactly these headings, in the order of the task file:

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
2. **Nothing added.** No information from memory or from another edition: no sūtra numbers, no chapter-and-verse where the block gives none, no opinions of other commentators, no remarks of your own. A reference the block gives is kept as given.
3. **The text is the base.** Never correct a letter or a number. Where the Sanskrit seems damaged or you cannot construe it, translate what can be translated and put `**NOTE**{your question in one sentence}` at that place. Do not guess silently.
4. **You never type Devanagari or IAST for a Sanskrit quotation.** To cite a Sanskrit word or passage, copy it from this unit's blocks (bhāṣya, Saṃhitā or Pada) between `⟦` and `⟧`, letter for letter: `⟦इंद्र⟧`. A script adds the transliteration and checks that every `⟦ ⟧` occurs in the unit; anything not found is rejected. Outside `⟦ ⟧` there must be no Devanagari at all.
5. Names and technical terms in running English (Sāyaṇa, Yāska, Soma, hotṛ, udātta, kvip) may be written in Roman letters with diacritics. Quote a Sanskrit word with `⟦ ⟧` the first time it is explained; after that the Roman form is enough.
6. Plain, exact English. Full sentences. A quotation from another text is first cited (`⟦ ⟧`), then translated.

## When you are done
Run the check named in your task and correct the file until it prints `VERIFIED`. Then report in three lines: the file, the check's last line, and the number of `**NOTE**` marks. Do not commit or push.
