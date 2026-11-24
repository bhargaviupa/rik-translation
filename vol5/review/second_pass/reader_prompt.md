# Reader's brief — S2 batch of the second pass of Vol 5

You read printed pages A–B of Vol 5 (Kannada → English Rigveda translation, repo /home/user/rik-translation). Read CLAUDE.md quickly and the kind codes (H1–H33) in docs/ERROR_KINDS.md.

Your sheet: the path given in your task (made by tools/rv/second_pass_page.py: supplied Kannada of pp. A-1…B+1, then the English segments with English-file line numbers; sieve hints of numbers on each segment line). Pages A-1 and B+1 are context only. The Saṃhitā, Pada and Sāyaṇa-bhāṣya blocks are not to be read ("[block not read]"). Pages from 531 on are continuous prose (no Ṛks).

Pages the sheet shows as "(not in the supplied text: stands in the neighbour page)" are pages without a running head: their text is NOT missing, it stands inside the previous page's block (that block is then about twice as long). Read it there.

Read the supplied Kannada against the English once, page by page, looking for, in this order:
R1: a number or reference missing, changed or supplied from memory; a name or term wrong; roles reversed; an addition the Kannada does not have; an omission inside a paragraph; a misprint silently put right.
R6: a Kannada word that is not a word, a name/term misread for a look-alike, vowel signs of the wrong script, a sentence cut at a page break.
R3: a Sanskrit quotation inside the commentary that is not a word or not the text the English cites.

Rules: supplied Kannada numerals are correct (user's decision): a number or reference is taken from the supplied text, decision applied, no question. Never settle a number or letter from memory or another edition. A text place is changed only where the Kannada sentence, the grammar of the quotation or the gloss that follows decides; otherwise decision=question. Do not re-translate; do not "improve" style. Legacy remarks ([?], [sic], bracketed notes, **GLOSS**) are left alone, EXCEPT that a `[?]` standing at a number the supplied text prints in full is a finding (take the supplied number). Ignore: Arabic-vs-Roman numeral style, spelling of reference-work names (a script does those), obvious Kannada misprints that the English already renders correctly (do not log them). If a whole passage of the Kannada is missing from the English, give as_found = the English sentence just before it and proposed = that sentence plus the translated missing text (in the English's own style), exact strings, so it can be applied mechanically; if that is too long for one line, decision=question.

Output: write ONLY the file named in your task (tab-separated, header `page	kind	reader	place	as_found	proposed	basis	decision	log`). One row per finding. page = printed page; place = 'L1234: a few words' with the English-file line number of the line to change; as_found = the exact existing English text (a substring of that ONE line, unique in it, 12+ characters, no line breaks, no tabs; copy it exactly including markdown asterisks); proposed = the exact replacement; basis = what the Kannada says (quote the Kannada words); decision = applied|question; log = short why (for a question: what is unclear). Change no other file; do not commit.

Reply: pages read, rows by kind and decision, pages you could not read in full, and what you did not check. Be honest.
