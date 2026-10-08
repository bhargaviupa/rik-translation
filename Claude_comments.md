# Claude's Comments — Volume 2 Translation Sessions

Remarks I made in the chat while working on `Rigveda_Samhita_Vol2_English_Translation.md`. Compiled from the conversation as I can see it; messages from the earliest part of the session survive only as a summary, so those are condensed, not quoted.

## 1. Sūkta 6 — what was done (printed pp. 202–257)

- Sūkta 6 ("yuñjanti bradhnam aruṣam") is finished and pushed to `claude/hopeful-turing-9r66zc`. All ten Riks (6.1–6.10) are in the three-layer format.
- The last part of Rik 6.8 (pp. 244–245) was completed from pages I had viewed but not yet written. Rik 6.9 covers pp. 245–251 and Rik 6.10 covers pp. 251–257.
- Grammar pages are summarized in outline, with every sūtra I could read kept in three layers. The dense accent-precedence argument on pp. 251–256 is outline only.
- Page 257 closes Sūkta 6 and begins Sūkta 7. The Sūkta 7 heading and first lines are not yet translated. No PR has been opened.

## 2. Corrections I made to my own drafts

- Rik 6.10's grammar notes first contained Pāṇini and Uṇādi details I had filled in from memory. I re-read p. 252 at higher zoom and rewrote that block from the actual print.
- I changed the *cavā-yoge prathamā* reference to Pāṇini 8-1-59 (the standard number; the print's numeral is small).
- Standard sūtra numbers I accepted without comment: 1-1-55, 2-4-71, 6-4-22, 6-4-37, 6-4-105, 7-1-1, 8-1-19. I did not check the rest.

## 3. Open flags recorded in the file

- **Varga numbering:** the closing note on p. 257 reads "eighth varga". The p. 201 note was read "tenth", and the small page-header numerals disagree again. I recorded the discrepancy and did not reconcile it.
- **Uncertain numerals:** reference numerals (Nirukta, Nighaṇṭu, Uṇādi, Phiṭ, some Pāṇini numbers) are marked [?] wherever they are not certain, throughout Sūkta 6.
- **Clipped readings:** a few clipped word-starts in Riks 6.5–6.7 (pp. 227, 230, 236).
- **Garbled passages:** Skandasvāmī passages on pp. 206–207.
- **Not yet cleaned:** the older progress notes inside the file (around lines 170, 385, 501) and a stray Cyrillic string on p. 29.

## 4. Reducing cost — what I recommended

The cost comes mostly from reading page images, plus the long conversation being re-read every turn. My suggestions, roughly in order of impact:

1. **One fresh session per sūkta.** Context grows with every page image, and `CLAUDE.md` plus the progress note already carry the position.
2. **A cheaper model for transcription** (Sonnet or Haiku, chosen with `/model`), keeping a larger one for review. Risk: accuracy on Kannada-script Sanskrit may drop, so test it on one sūkta and compare.
3. **Zoom only where needed.** I often rendered at 150 dpi and then re-rendered crops at 230–260 dpi, roughly doubling the image reads. Crop only dense bhāṣya or numeral blocks, never grammar pages.
4. **Short notes on grammar pages** (2–4 lines naming the words and sūtras) instead of detailed outlines. Sūkta 6 had about 15 such pages.
5. **View each page once and write immediately,** instead of viewing a page in one turn and writing it later.
6. **Batch the writes** — a whole Rik or a 4–6 page run per call.

## 5. What I did about it

I added a "Cost-saving rules" section to `CLAUDE.md` (commit `0b26250`, pushed) covering the points above, and a pointer from convention 5. The instruction to view the page image before writing is unchanged. I did not test the new rules.

## 6. Steps I asked you to take

1. Start a new session on this repo and branch `claude/hopeful-turing-9r66zc`.
2. Pick a cheaper model with `/model` (I suggested starting with Sonnet).
3. First prompt: "Follow CLAUDE.md and translate Sūkta 7 from printed page 257. Stop at the end of the sūkta and write the progress note."
4. Check Sūkta 7's opening pages yourself (Rik texts, Kannada-to-Devanagari conversion, [?] flags). If accuracy drops, switch back and tell me which pages were weak.
5. Repeat for Sūkta 8 in another new session.

## 7. Where to find `/model`

I couldn't see your screen, so this was based on how the interface usually works. In the Claude app or claude.ai/code, type `/model` in the message box, or choose the model when starting a new session. In the terminal CLI, type `/model` at the prompt. In the desktop app or an IDE extension, `/model` in the chat input works too, and there is usually a model selector beside it. The choice applies to the current session only.
