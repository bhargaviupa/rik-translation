# Vol 22 — independent QA sample (English vs Kannada)

- Date: 2026-11-27
- Checker: independent read-only check (branch `claude/hopeful-fermi-kypcts`)
- Files: E = `vol22/Rigveda_Samhita_Vol22_English_Translation.md`, K = `vol22/Rigveda_Samhita_Vol22_Kannada_Text.md`
- Method: for each page, the English between `### Printed p. N` and the next page heading was read side by side with the Kannada between `<!-- printed N -->` and the next mark (both extracted by line number). Checked: (1) numbers and references (ṛk, sūkta, Nirukta / Āśvalāyana / Taittirīya / Ṛ. Saṃ. references), (2) names, technical terms, quotations, (3) negations, attribution, who does what to whom, (4) omissions and additions in Pratipadārtha, Bhāvārtha, Anuvāda, Special Topics, introduction and colophon; that every announced quotation follows. Saṃhitā/Pada/Sāyaṇa blocks were checked only for being the right block in the right place (not letter by letter). The Gist of the bhāṣya (translator's English from the Sanskrit) was read against the Sanskrit block for sense. `**GLOSS**` markers (p. 1) are the intended marker of `tools/rv/gloss_marker.py` and are not counted.
- Pages (24): (a) 1, 55, 109, 164, 218, 273, 327, 382, 436, 491, 545, 600; (b) Special Topics: 116, 163, 187, 198, 221, 295, 381, 392, 428, 440, 516, 550.

## Per page

**p. 1** — E 343–377, K 380–410. Invocation verses, title block, Part 22, Aṣṭaka 5 Adhyāya 3, Sūktas 20–31, Introduction (sūktas 18–31 = 14; Part 21; Part 5 pp. 569-582; Part 16 pp. 631-683), Sūkta 20 bhāṣya opening. No findings.

**p. 55** — E 2715–2755, K 2134–2158. Ṛk 5 (Sūkta 25) Pada, bhāṣya, Gist, all 16 Pratipadārtha items, Bhāvārtha, Wilson. No findings.

**p. 109** — E 5070–5123, K 3823–3855. End of Ṛk 9 Pratipadārtha (negation "न—do not become helpers" kept), Bhāvārtha, Ṛk 10 blocks, Gist, Pratipadārtha (नकिः / न रीरमत् negations kept). No findings.

**p. 116** — E 5410–5456, K 4059–4090. Special Topic (avama/madhyama/parama), Ṛk 17 blocks, Gist, Pratipadārtha incl. "(O Indra)", Bhāvārtha. No findings.

**p. 163** — E 7597–7637, K 5689–5721 (with end of p. 162: E 7575–7596, K 5680–5688). Pratipadārtha tail, Bhāvārtha, Wilson, Special Topic (Yāska on sudatraḥ, Ni. 6-14), Ṛk 23 blocks, Gist.
- ERROR: the item "नः—" that ends the p. 162 list in K (K 5688 `ನಃ—`, continued K 5692 `ನಮಗೆ`) is missing from E's p. 162 list, and its Kannada gloss has been turned into a Sanskrit headword with no meaning: E 7601 `- नमगॆ (*namagè*)—`. Correct: `- नः (*naḥ*)—to us` (as the last item after वरूत्रीभिः), no item "नमगॆ".

**p. 164** — E 7638–7685, K 5722–5753. Ṛk 23 Pratipadārtha (all 16 items), Bhāvārtha incl. "(the earth)", Wilson, Ṛk 24 blocks, Gist. No findings.

**p. 187** — E 8648–8685, K 6393–6418. Pratipadārtha, Bhāvārtha, Wilson, Special Topic (Tai. Ā. 10-63; Smṛti verse; modern science), Ṛk 2 Saṃhitā line 1. No findings.

**p. 198** — E 9148–9190, K 6748–6783. Bhāvārtha, Wilson, Special Topic (Ṛbhus), Ṛk 2 blocks, Gist, Pratipadārtha (ends at धत्थ— as K does). No findings.

**p. 218** — E 10061–10102, K 7404–7446. Bhāṣya tail, Gist, Pratipadārtha (14 items), Bhāvārtha incl. "(at dawn)", Wilson, Special Topic (bīriṭe, two meanings; Ni. 5-28; Taiṭīki).
- MINOR: Gist E 10070 `so let they come` — ungrammatical; read "so let them come".

**p. 221** — E 10165–10182, K 7527–7564. Special Topic on the Vasus (Ni. 12-41, Ni. 12-43, Ni. 2-5; eight Vasus; Vājasaneya Saṃhitā), Ṛk 4 Saṃhitā. Prose complete.
- MINOR (formatting): Saṃhitā line E 10179 `विश्वे॑ अ॒भि संति॑  ॒` carries a stray detached accent mark `॒` before the line break.

**p. 273** — E 12372–12409, K 9325–9366. Nirukta quotation (Ni. 10-6) and its explanation, cross-reference to the third Ṛk's Special Topics, Ṛk 2 blocks, Gist, Pratipadārtha.
- ERROR (Gist): E 12398 `The rest is to be supplied.` renders `शेषः प्रत्यक्षकृतः` ("the rest is in direct address", i.e. the remainder of the Ṛk addresses Rudra in the second person). Correct sense: "The rest is in direct address (to Rudra)."

**p. 295** — E 13213–13254, K 9947–9975. Special Topics (yāsāṃ rājā varuṇaḥ; Taittirīya Śruti twice; samrāja; dhṛtavrata), Ṛk 4 blocks, Gist, Pratipadārtha. No findings.

**p. 327** — E 14326–14361, K 10838–10861. Bhāṣya, Gist, Pratipadārtha, Bhāvārtha, Wilson, Special Topic (Sārameya; Saramā and the Paṇis; Maṇḍala 10, Sūkta 108). No findings.

**p. 381** — E 16512–16549, K 12423–12456. Pratipadārtha tail, Bhāvārtha, Wilson, Special Topic (naṃsaṃte, Ni. 4-13), Ṛk 6 blocks, Gist.
- MINOR (formatting): Saṃhitā line E 16534 `स्व॒स्तिभिः॒ ॑` carries a stray detached accent mark `॑`.

**p. 382** — E 16550–16594, K 12457–12493. Pratipadārtha incl. "(O Maruts)", Bhāvārtha, Wilson, Sūkta 59 heading, bhāṣya, Gist, Anuvāda (fourth anuvāka, fourth sūkta, 12 Ṛks; metres as K gives them, K's "first and fifth" kept as printed).
- MINOR: E 16560 `- जुषंतॆ (*juṣaṃtè*)—may they enjoy` — the Kannada spelling ಜುಷಂತೆ has been carried into the headword with a Kannada short e; the Pada form is जुषंत (*juṣaṃta*).

**p. 392** — E 17037–17080, K 12865–12902. Ṛk 10 blocks (Ā. 2-18), Gist, Pratipadārtha, Bhāvārtha, Wilson, Special Topic (Gṛhamedhīya, Āśvalāyana Ā. 2-18). No findings.

**p. 428** — E 18130–18171, K 13838–13877. Special Topic (na śaradaḥ; Wilson's note, quoted in English; K's misprint "a ong time" correctly read "a long time"), Ṛk 3 blocks (Ṛ. 1-61-9), Gist, Pratipadārtha. No findings.

**p. 436** — E 18470–18513, K 14127–14155. Ṛk 2 blocks (Ṛ. 1-161-6, Ai. Brā. 5-14), Gist, Pratipadārtha, Bhāvārtha (Varuṇa absent in K's Bhāvārtha and in E alike).
- MINOR (Gist): E 18490 `since they too share in the particle` renders `तेषामपि निपातभाक्त्वात्`; निपातभाक् here means having an incidental share (in the praise), not "particle". Read: "since they too have an incidental share (in the hymn)".

**p. 440** — E 18644–18686, K 14255–14286. Pratipadārtha, Bhāvārtha, Wilson, Special Topic (Mitra-Varuṇa animal offering, puroḍāśa, yājyā, Āśvalāyana Ā. 3-8), Ṛk 6 blocks. No findings.

**p. 491** — E 20640–20678, K 15815–15847. Bhāvārtha, Wilson, Ṛk 2 blocks, Gist, Pratipadārtha. No findings.

**p. 516** — E 21702–21745, K 16572–16600. Pada, bhāṣya, Gist, Pratipadārtha, Bhāvārtha, Wilson, Special Topic (omanā, Ni. 6-4).
- MINOR (omission): K 16587 opens the Pratipadārtha with `(ಎಲೈ ಅಶ್ವಿನೀದೇವತೆಗಳೇ)`; E 21719 `- युवोः (*yuvoḥ*)—your` has no "(O Aśvins)" (pp. 116 and 382 keep the equivalent vocative). Correct: `- (O Aśvins) युवोः (*yuvoḥ*)—your`.

**p. 545** — E 22927–22965, K 17441–17474. Sūkta 73 data line (Maṇḍala 7, Anuvāka 5, Aṣṭaka 5, Adhyāya 5, Varga 20, 5 Ṛks, Vasiṣṭha, Aśvins, Triṣṭubh), Ṛk 1 blocks, Gist, Pratipadārtha. No findings.

**p. 550** — E 23135–23179, K 17597–17622. Pada tail, bhāṣya (Ā. 3-8), Gist (five peoples), Pratipadārtha, Bhāvārtha, Wilson, Special Topic (vapā anuvākyā, Ā. 3-8). No findings.

**p. 600** — E 25281–25301, K 19193–19213. Bhāvārtha, Wilson, closing verse, colophon, ending formula, kṣamā verse, blessings.
- ERROR (omission of the Sanskrit layers): the closing Sanskrit of K 19204–19212 (`ವೇದಾರ್ಥಸ್ಯ ಪ್ರಕಾಶೇನ ತಮೋ ಹಾರ್ದಂ ನಿವಾರಯನ್ । …`, the colophon `ಇತಿ ಶ್ರೀಮದ್ರಾಜಾಧಿರಾಜ… ಪಂಚಮೋಽಧ್ಯಾಯಃ ಸಮಾಪ್ತಃ ॥`, `॥ ಓಂ ತತ್ಸತ್ ॥`, `ಯದಕ್ಷರಪದಭ್ರಷ್ಟಂ … ನಮೋಽಸ್ತು ತೇ ॥`, `॥ ಶುಭಂ ಭೂಯಾತ್ ॥ ॥ ಮಂಗಳಂ ॥`) appears in E only as English (E 25290 `May Vidyātīrtha Maheśvara, dispelling the darkness …`, E 25292 `Thus ends the fifth adhyāya …`, E 25296 `Whatever has fallen from syllable or word …`). The Devanagari + IAST lines are missing (p. 1 gives them for the opening verses). Correct: each verse in Devanagari + IAST followed by the English.
- MINOR: E 25300 `**Progress note:** Done through printed p. 600. pp. 595-600 (batch API)` — the trailing `pp. 595-600 (batch API)` is a stray remark after the prescribed progress-note text.

## Summary

- Pages checked: 24. Pages with no findings: 15 (1, 55, 109, 116, 164, 187, 198, 295, 327, 392, 428, 440, 491, 545, 550).
- **ERROR: 3** · **MINOR: 7**
- No number or reference error, no negation or attribution error, no invented content in the Kannada prose renderings was found on the sampled pages. No Kannada prose was found set as a Sanskrit block on these pages.

| # | Page | Sev. | E line | Wrong English (quoted) | Correct reading |
|---|------|------|--------|------------------------|-----------------|
| 1 | 163 (162/163) | ERROR | 7601 | `- नमगॆ (*namagè*)—` (and no `नः` item at the end of p. 162) | `- नः (*naḥ*)—to us` after `वरूत्रीभिः`; K 5688 `ನಃ—` + K 5692 `ನಮಗೆ` |
| 2 | 273 | ERROR | 12398 | `The rest is to be supplied.` | "The rest is in direct address (to Rudra)." (`शेषः प्रत्यक्षकृतः`) |
| 3 | 600 | ERROR | 25290, 25292, 25296 | closing verse, colophon and kṣamā verse in English only | Devanagari + IAST of K 19204–19212 before each English rendering |
| 4 | 218 | MINOR | 10070 | `so let they come` | "so let them come" |
| 5 | 221 | MINOR | 10179 | `संति॑  ॒` (stray accent mark) | `संति॑` |
| 6 | 381 | MINOR | 16534 | `स्व॒स्तिभिः॒ ॑` (stray accent mark) | `स्व॒स्तिभिः॒` |
| 7 | 382 | MINOR | 16560 | `- जुषंतॆ (*juṣaṃtè*)—may they enjoy` | `- जुषंत (*juṣaṃta*)—may they enjoy` |
| 8 | 436 | MINOR | 18490 | `since they too share in the particle` | "since they too have an incidental share (in the hymn)" (`निपातभाक्त्वात्`) |
| 9 | 516 | MINOR | 21719 | `- युवोः (*yuvoḥ*)—your` | `- (O Aśvins) युवोः (*yuvoḥ*)—your` (K 16587 `(ಎಲೈ ಅಶ್ವಿನೀದೇವತೆಗಳೇ)`) |
| 10 | 600 | MINOR | 25300 | `Done through printed p. 600. pp. 595-600 (batch API)` | `**Progress note:** Done through printed p. 600` |
