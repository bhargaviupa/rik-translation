# Applying the editor's decisions to the English text — instruction

You get a packet: a JSON list of items. Each item is one English paragraph of a translation of a Kannada edition of the Ṛgveda (`text`), with one or more marks `⟨NOTE:k⟩` in it. For each mark there is a note: the `question` the translator had asked at that place, and the `decision` now taken. `by` is `user` (the editor answered after looking at the printed book) or `rule` (the editor's rule: where a word does not match the verse, the verse's form is right).

Your job: for each item, make the paragraph say what the decision requires, changing as little as possible.

## How to read a decision
- "Correct", "Yes", "Seems to be correct" and the like: what the English already does is right. No change.
- A word or a phrase (often in Kannada script, sometimes in rough Latin spelling): this is the right reading at that place. If the paragraph shows another form there, put the right one. If the paragraph already shows it, no change.
- A named work ("Atharva Veda", "Shvetashvatara upanishad", "Use R.Sam"): the abbreviation in the paragraph stands for that work. Use these forms: Ṛ. Saṃ. (Ṛgveda-saṃhitā), Tai. U., Tai. Ā., Śve. U. (Śvetāśvatara Upaniṣad), A. Ve. (Atharvaveda). Change the abbreviation only; keep the numbers exactly.
- "the verse's form, as printed from the reference": the question says which form the verse has. If the question names that form and the paragraph shows a different one, put the verse's form. If you cannot tell the exact form from the question and the helper, make no change and say so.

## Sanskrit: never type it yourself
Sanskrit in the paragraph stands as Devanagari followed by its transliteration in italics in parentheses, for example `घृतस्नू (*ghṛtasnū*)`. When a decision requires another Sanskrit form, take the Devanagari and the transliteration from the note's `helper` list (it gives every Kannada-script word of the decision and the question as `kannada`, `devanagari`, `iast`). Replace both the Devanagari and the transliteration in parentheses. Do not type Devanagari or transliteration that is not in the helper or already in the paragraph. If the helper does not have what you need, make no change and say so.

## English wording
Change the English words only when the decision changes the meaning (for example the question says a word was read as "name" and the decision says it is the word for "cow"). Otherwise leave every English word as it is. Do not improve, shorten or re-punctuate anything. Do not add remarks or brackets. Keep every `⟨NOTE:k⟩` mark exactly where it is (a script removes them afterwards).

## Output
Write one JSON file (path given to you), a list with one object per item, in the packet's order:
`{"unit": "...", "para": N, "result": "NOCHANGE" or the full new paragraph text, "changed": "one line: what you changed and for which note, or why nothing was changed"}`
`unit` and `para` are copied from the item. The file must be valid JSON (UTF-8).
