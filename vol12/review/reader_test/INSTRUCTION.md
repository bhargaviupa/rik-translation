# Second reading — instruction for the reader

You check an English translation against its Kannada source, one printed page at a time. The book is a 1950 Kannada edition of the Ṛgveda with Sāyaṇa's Sanskrit commentary; the Kannada text is machine-read, so it has some wrong letters of its own. Sanskrit appears in Kannada script in the source and in Devanagari in the English.

Each page file has two parts: `## KANNADA (the source)` and `## ENGLISH (the translation to be checked)`. Read the Kannada sentence by sentence and compare the English with it.

## Report only these faults
1. **meaning** — the English says something the Kannada does not say: a wrong sense, who does what reversed, a quality or action given to the wrong person or thing, a negation lost or added.
2. **term** — a wrong word, name or technical term (grammar, ritual, metre, accent).
3. **addition** — English that has nothing behind it in the Kannada: an explanation, a gloss, or an English translation of a Sanskrit quotation that the Kannada itself does not translate.
4. **omission** — something in the Kannada is missing in the English: a sentence, a clause, a word that matters, a headword, part of a Sanskrit quotation (a quotation cut short or given only in English).
5. **number** — a number or a reference (book-chapter-verse) differs from the Kannada.
6. **silent correction** — the Kannada has a misprint or an odd word and the English quietly gives what it "should" be, without saying so.

## Do not report
Style or better wording; layout, headings, page breaks; transliteration; punctuation and closing marks of quotations; the letters of the Sanskrit blocks themselves; bracketed translator's notes such as "(as supplied)" (they are allowed in this volume); a sentence that begins or ends on the neighbouring page.

## Output
For each page write one file `pNNNN.tsv` (same number as the page file) in the output folder you are given. One finding per line, tab-separated:

`severity` TAB `kind` TAB `English words concerned (quote)` TAB `Kannada words concerned (quote)` TAB `what is wrong, in one sentence`

- `severity` is `ERROR` (the reader of the book would be told something false, or loses or gains content) or `MINOR`.
- `kind` is one of: meaning, term, addition, omission, number, silent correction.
- If a page has no fault, write the single line `OK`.

Be exact and sparing: report what you are sure of after reading the Kannada. Do not correct anything; do not rewrite; only report.
