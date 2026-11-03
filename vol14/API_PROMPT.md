# Vol 14 API translator instructions (single call, no tools)

You translate 3 consecutive pages of Volume 14 (Maṇḍala 2 onward) of the Rigveda Saṃhitā Kannada commentary into English, following CLAUDE.md and the runbook (given above in the system prompt) and the format of the sample text you are given (the end of the output file).

You receive: the page images as horizontal strips in order (each labelled with its PDF page and printed page), the numeral-file rows for those pages (numerals read by another engine: use as the default for reference/sūtra/header numbers; where your reading of the strip differs, keep your reading and flag `file said X`; where the file lacks a number, read it from the strip), the previous progress note (the position), and the last ~150 lines of the output.

You cannot zoom or call tools. Any word or numeral you cannot read confidently: write `[?]` with your best reading and list it under DOUBTS. Never fill Sanskrit from memory. If a page looks duplicated, missing, cut off or an image is unreadable, say so in the text and in the note; do not invent text.

Rules: Devanagari + English only for Sanskrit; mark ALL inline Sanskrit with ⟦…⟧ (the IAST layer is added by script; never type IAST). Bhāṣya in Devanagari with a ≤25-word gist (put the gist line before the Devanagari block or after it only if no IAST line is expected — safest: gist line BEFORE the block). Printed English reproduced as printed ([sic] for misprints). Write quoted English passages as plain paragraphs, not blockquotes. Mark each page `### Printed p. N (PDF M)`. Continue exactly where the previous note says (an open Ṛk continues; do not repeat text already written). If a Ṛk continues past your last page, leave it open.

OUTPUT FORMAT (exactly these three delimiter lines, nothing before the first):
=====CHUNK=====
(the markdown to append)
=====NOTE=====
(new progress note, one paragraph, without the words "Progress note:": printed page reached, sūkta/Ṛk position, any Ṛk left open, flags: FILE DISAGREE, unzoomed numerals, [?] places)
=====DOUBTS=====
(one line per doubtful place: `PDFPAGE | what is doubtful / your reading`; empty if none)
