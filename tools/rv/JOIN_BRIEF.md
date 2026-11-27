# Brief: mend sentences cut at a page turn (tools/rv/join_pages.py)

You get one file `volN/review/junctions/batch_XX.json`: a list of places in the English translation of a Kannada book. You write one file `volN/review/junctions/out_XX.json` and change nothing else. Do not edit the translation files, do not run git.

**What a place is.** The English was written page by page. Where a sentence of the original runs over a page turn, the translator ended one paragraph with `...` and began the next with `...`, often dropping or repeating words at the break. `a_tail` is the exact end of the paragraph before the break (its last words); `b_head` is the exact beginning of the paragraph after it. `kind` P = a page turn lies between them; `kind` M = a line inside a page that ends in `...` (then `b_head` is only the line that follows, for context). Where given, `kannada_end_of_previous_page` and `kannada_start_of_this_page` are the original Kannada on both sides of the page turn (machine-read: expect small misreadings).

**What you return for each place:** `{"id": N, "a_tail_new": "...", "b_head_new": "...", "reason": "a few words"}` or `{"id": N, "status": "unsure", "reason": "..."}`.

Rules:
1. `a_tail_new` replaces `a_tail`, `b_head_new` replaces `b_head`. Read one after the other they must be continuous, correct English that says what the Kannada says: no `...` or `…` at the break, no word doubled, none missing. The two halves stay two strings (they are joined in print); `a_tail_new` simply ends where the page ends, without closing punctuation if the sentence goes on, and `b_head_new` continues in lower case.
2. Change as little as possible. Usually: delete the dots, fix the capital letter, and repair the few words at the break. If words are missing at the break and the Kannada supplies them, add their plain translation (never more than about 20 words). If the two halves already read well once the dots are gone, do only that.
3. If the first half is in fact a complete sentence, end it with its proper punctuation and let the second begin with a capital; if the second half's opening words only repeat the end of the first, drop the repetition.
4. Kind M: the line ends in dots by habit. If it introduces what follows (a quotation, a list, an example), end it with a colon or a dash as fits; if it is a finished sentence, a full stop; if words are really missing and you cannot supply them from what you are given, answer `unsure`. Return `b_head_new` identical to `b_head` for kind M.
5. Never change, add or drop a figure, a reference number, a Sanskrit or Kannada word, a name, or markdown marks (`>`, `*`, `**`, `"`): keep every one of them exactly, in place. Dots inside a quotation that mark an omission by the original author are not yours to remove: only the dots at the very break.
6. Do not improve the translation elsewhere. Do not explain in the text. No remark of yours goes into the strings.
7. When the Kannada is missing (front matter) work from the English alone; when you cannot make a continuous sentence with confidence, answer `unsure` and say what is missing. An honest `unsure` is better than a guess.
8. Copy the unchanged part of each string exactly, character for character (the script replaces by exact match and refuses an answer in which a figure or an Indic letter differs).

Write `out_XX.json` as a JSON list with one entry for every id of the batch (valid JSON, UTF-8). Then reply with one line: how many changed, how many unsure.
