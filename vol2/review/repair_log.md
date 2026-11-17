# Vol 2 repair log

- Nov 17 2026: file opened for the agreed clean-up pass (user, Nov 17 2026). Step A1: counts and proposal written (`cleanup_proposal.md`); text unchanged.
- Nov 17 2026: user decision: `[?]` after a number/reference is retained for the user's review (112 marks by script); not removed in Part A.
- Nov 17 2026: user decision: `[?]` on lines with Devanagari retained (237; IAST twins 57 proposed to stay with them).
- Nov 17 2026: user decision: `[sic]` (143) retained.
- Nov 17 2026, kind `oldnotes` (tools/rv/cleanup_remarks.py 2 oldnotes): 3 old mid-file "Progress:"/"Target for next session" note pairs (6 lines) and the closing block (progress note, "This pass", "Open flags", "scan ends here": 6 lines) removed; one trailing `**Progress note:** Done through printed p. 808` written. Checked: git diff shows only removed lines; 30 samples read.
- Nov 17 2026, kind `notes`: 156 whole-line italic notes `*( … )*` in which every clause is a process remark of an exact form (page-header notes, "Saṃhitā accents as printed; Pada unaccented", "English as printed", "re-read from the better scan", "Grammar characterized, sūtras kept", numeral-pass notes) removed whole; notes with any other sentence (content, reading notes, first-person, marks) stay. Page-header notes carried the running head with its varga number: the text of each is in removed_remarks.tsv. Checked: diff shows only these lines removed, no empty notes, no new triple blank lines; 30 samples read before/after (all clean).
