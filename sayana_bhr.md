# Sāyaṇa-bhāṣya reader: the session of Nov 18–20 2026 (for BHR)

*A record of what this session did, found and left open, written at the user's request when the session was closed. It is a record, not a rule: the rules are in `tools/rv/BHASHYA_BRIEF.md` and `docs/BHASHYA_RUN.md`, the item is T14 in `PUBLICATION_TODO.md`. This file can be deleted once those carry everything the user still wants.*

## 1. Where it began
The user asked whether a proper English translation of Sāyaṇa's bhāṣya exists. From memory (not checked on the web in this session) none exists for the whole Ṛgveda: Wilson follows Sāyaṇa's interpretation of the mantras but does not translate the commentary; Max Müller printed the Sanskrit commentary without translating it; Griffith, Geldner and Jamison–Brereton translate independently of Sāyaṇa. The user then proposed a by-product book: **Saṃhitā-pāṭha, Pada-pāṭha, Sāyaṇa-bhāṣya, IAST, and an English understanding of the bhāṣya, nothing else** (no Kannada commentary, no Wilson, no Special Topics). That is "the Sāyaṇa-bhāṣya reader", item T14.

## 2. What was built (all shared tools, no per-volume ones)
| File | Purpose |
|---|---|
| `publish/bhashya_book.py` | Selects the wanted layers from a volume's English file *by line, never rewriting*; writes the reader as Markdown, HTML or PDF (`--pdf`); `--task M.S` writes the translator's task file (Devanagari of Saṃhitā, Pada and bhāṣya only); `--notes` collects the translators' questions and logged readings into `volN/review/`. Where `volN/bhashya_en/M<m>_S<sss>.md` exists, the book prints it in place of the old Gist. Built-in check: every text line is in the source unchanged and the Ṛk count matches. Reads the labelled layout only (Vols 11, 16, 17, 18 today); refuses the older layouts with a message. |
| `publish/bhashya_check.py` | The form check every English file must pass (see §4). It cannot judge meaning. |
| `tools/rv/BHASHYA_BRIEF.md` | The translator's brief (rules in §4). |
| `tools/rv/bhashya_run.py` | `status`, `next [K] [VOL]`, `verify VOL M.S`: state of the run read from the repository. |
| `tools/rv/sayana_ref.py` | Prints **only Sāyaṇa's sections** of a clean reference text (vishvasa.github.io) for a sūkta. Nothing else from that site (it also carries other translators) is shown to the agents. |
| `docs/BHASHYA_RUN.md` | The dispatcher's runbook and the state when the run stopped. |
| `vol11/…`, `vol16/…`, `vol17/…` `bhashya_en/` | One English file per sūkta, `M<maṇḍala>_S<sūkta>.md`. |
| `volN/review/bhashya_notes.tsv`, `bhashya_readings.tsv` | Questions for the editor; every misread word and the reading translated, with its basis. |
| `volN/parts/bhashya_costs.md` | Tokens per batch, model named. |
| `publish/out/Rigveda_Bhashya_Reader_Vol11_all.pdf` (and `.md`) | Vol 11 reading copy, 166 pages. Also a one-sūkta sample, Vol 17 3.40. |

Environment: the `rik` environment's network was widened with the user's approval to `vishvasa.github.io`, `gretil.sub.uni-goettingen.de`, `sanskritdocuments.org`, `ashtadhyayi.com` (the second and third were not needed; `sanskritdocuments.org` refuses automated requests). Pages open with `curl` from the shell; the WebFetch tool did not work on them.

## 3. How the English is made
Each agent is given a sūkta's Devanagari only (Saṃhitā, Pada, bhāṣya block per Ṛk), **not** the Kannada commentary, Venkata Rao's word meanings or Wilson. It writes `## Introduction`, `## Ṛk N` … and an optional `## Readings`, runs the check until it prints VERIFIED, and (when it works a whole volume) commits and pushes only its own file. The English is a **direct translation of Sāyaṇa's Sanskrit**, not of the Kannada. The user compared it with Venkata Rao's Kannada for Sūkta 3.40 and decided: *the changes between the two are fine; ours is truer to Sāyaṇa; continue with this approach.* (Venkata Rao rearranges and expands Sāyaṇa and leaves out most of the grammar; this is why the reader is worth making.)

## 4. The rules the agents work under (summary; the brief is the authority)
1. **Everything, in Sāyaṇa's order**, the grammatical part at the end included (root, sense, suffix or rule, accent *only where the block names it*).
2. **Nothing added, nothing dropped, nothing shifted**: no fact from memory; a word Sāyaṇa does not gloss is not glossed; his gloss, not the dictionary's; each epithet with the noun it belongs to; voice, causatives, particles (`एव`, `अपि`, `यदि`), possessives kept.
3. **The supplied text is the base and is never altered.** The machine-read Sanskrit has many misread letters. Where the intended word is certain (from the Ṛk, the Pada-pāṭha, grammar and context, or the reference text) it is translated and logged in `## Readings` (supplied letters → reading → basis); where not, a `**NOTE**{question}` marks the place. A difference of content between the supplied text and the reference text always gets a NOTE; a difference of mere wording, or of Uṇādi numbering, none.
4. **Sanskrit is copied, never typed**: cited between `⟦ ⟧` letter for letter (a script adds the IAST and checks every citation is in the unit); no Devanagari outside; no Roman-letter Sanskrit in brackets; **a citation holds the word or rule only, never Sāyaṇa's connecting prose**, and the sense of a cited root must stand in the English.
5. **References are copied in Devanagari**, to be turned into the series' uniform abbreviations later from the list another session is consolidating (the user's decision; nothing was built here for it).
6. Rule 7 of the brief: read the reference text beside the supplied text to settle misread places; use it for nothing else.
7. A second reading of every unit against its block (two questions per sentence: *does the block say this? is everything in the block rendered?*) is part of every sūkta.

## 5. What was made
| Volume | Sūktas with English | Made by | Questions (NOTE) | Readings logged |
|---|---|---|---|---|
| Vol 11 (Maṇḍala 1, 137–157) | 21 of 21 | Fable | 94 | 889 |
| Vol 16 (Maṇḍala 3, 7–39) | 33 of 33 | 3.7–3.31 Fable; 3.32–3.39 Sonnet, then a Fable second reading | 174 | 2,412 |
| Vol 17 (3.40 only) | 1 of 41 | Fable | 3 | 27 |
| Vol 18 | 0 of 48 | | | |

55 of 143 sūktas of the four volumes the reader can read. Vols 1–10, 12, 14, 15 are in older layouts the reader cannot read yet; Vol 13 is not translated; Vol 19 is in translation in another session; Vol 20 is not in the repository.

Recorded agent tokens (batches whose reports were lost to usage limits are missing): Vol 11 about 0.9 million (Fable), Vol 16 about 4.3 million (Fable 2.6, Sonnet 1.7, the Fable second readings of the Sonnet sūktas included in the Fable figure except one unreported batch), Vol 17 0.1 million. Typical cost: 40,000–50,000 tokens per short sūkta in batches of five, 200,000–250,000 for a sūkta of 11 or more Ṛks, about 215,000 for a 22-Ṛk sūkta. No API budget was used (the user ruled it out).

## 6. What was found
- **The model matters.** Sonnet (3.40 pilot) made four errors of meaning in nine Ṛks: a gloss Sāyaṇa does not give, an epithet on the wrong word, "our" turned into "for us", dictionary sense for his gloss. Fable made none at those places.
- **Sonnet's own second reading is not enough.** After the agents' self-check, a Fable second reading of the eight Sonnet sūktas (3.32–3.39, 93 Ṛks) made **242 corrections, 73 of them changing what a reader would understand Sāyaṇa to be saying**: citation faults 56, dropped words 40, reading/NOTE wrong 33, wrong sense 32, wrong attachment 16, additions 25, wording 27, plus 11 paragraphs of "X is glossed 'y'" apparatus restyled. By sūkta: 58, 46, 29, 16, 10, 28, 26, 29. The count fell while the brief was tightened and then rose again; the user was told this and that the dispatcher's own spot-reading (13 Ṛks, 3 faults found) had badly under-counted.
- **Fable's first drafts also slip**, less: a separate second reading of three Fable sūktas (3.27–3.29) made 10 corrections, none of attachment.
- A sūkta made by Sonnet and then re-read by Fable cost about 330,000 tokens, more than one made by Fable directly (about 200,000).
- **The supplied text** (Vols 11 and 16 especially) is heavily misread in the grammatical parts; most NOTEs and readings come from that, not from doubts of meaning. It also **lacks Sāyaṇa's introduction to at least ten sūktas** that the reference edition has (Vol 11: 1.139, 1.148–1.151, 1.153–1.156; Vol 16: 3.10) and the whole bhāṣya of two Ṛks (3.15 Ṛk 7, 3.31 Ṛk 22). Each is marked with a NOTE (the three earliest, 1.139, 1.148, 1.149, lack it), nothing added.
- **The two editions number the Uṇādi-sūtras differently** every time; the agents copy the supplied number without a NOTE. Which numbering to print is for the user to settle with the abbreviation list.
- The form check accepts very short citations too loosely (it passed `लिति` inside a longer word) and cannot see Roman-letter sūtra names; both are known gaps.
- Vol 16's English file has 180 translator remarks inside its bhāṣya blocks; the reader leaves them out (the volume itself is unchanged). The reader also leaves out each volume's own Grammar lists (made from the Kannada) wherever the English exists.

## 7. Decisions of the user in this session
Build the reader from the existing files by script; Fable agents, one volume at a time (later: Sonnet, then paused); web search allowed for misread words, damaged passages and references; no API budget; run until the user says stop (first until midnight IST, then 3 am IST Nov 19, then moved to Sonnet, finally stopped); references copied for later conversion; "Sonnet alone" chosen over "Sonnet plus a second Sonnet reading" for Vols 17–18 **but** the user said not to start the work yet because they are thinking of a better way; this record was then requested.

## 8. Still open
1. **How to make the remaining 88 sūktas (Vols 17, 18) well.** Not started. The user is thinking of a better way. The numbers in §6 are the evidence to design it from.
2. Second pass against the reference text for Vol 17 3.40 (made before the reference text existed). Vol 11 1.139, 1.148, 1.149 lack the missing-introduction NOTE. Vol 16 3.7–3.26 were made under the looser NOTE rule.
3. Uniform abbreviations of references (the other session's list), and the Uṇādi numbering.
4. How misread words inside citations should print (they print as supplied, with the intended word only in the Readings list).
5. Extending the reader to the older layouts (Vols 1–10, 12, 14, 15). Until then the reader covers only Vols 11, 16, 17 and 18; the other volumes (Maṇḍala 1 Sūktas 1–136 and 158 onward, Maṇḍala 2) are not counted in the 143 sūktas above.
6. The check's two known gaps (short citations, Roman sūtra names), and a measure of Sonnet's remaining error rate that does not depend on Sonnet reading itself.
7. Publication: rights and the 1949–52 edition's commentary stay out of the reader; the decision on rights is in `publish/release.json` (T14 is in `PUBLICATION_TODO.md`).

## 9. How to resume
`python3 tools/rv/bhashya_run.py status`, then `next K VOL`; agent prompt in `docs/BHASHYA_RUN.md`; the hourly check-in used in this session ("Bhāṣya run check-in", a scheduled task of that session) is disabled and will not exist in a new session. `pip install indic-transliteration rapidfuzz openpyxl`, and `weasyprint` with `fonts-lohit-deva fonts-noto-core` for the PDFs (HANDBOOK §8). Quote counts only from commands run.

## 10. Found when this record was merged into `main` (Nov 20 2026)
`main` had moved by 782 commits while this branch was worked on; only `PUBLICATION_TODO.md` was changed on both sides (merged by hand; my item there was renamed **T14**, because `main` already used T13 for the reference corrector). The merged tree was then checked again:

- **43 of the 55 English files now fail `publish/bhashya_check.py`, with 139 faults, every one of them a citation of a reference** (132 plain ones, 7 longer ones such as `छां. उ.`, `शत. ब्रा.` or a rule with its reference) (for example `⟦पा. ६-३-९-१⟧`, `⟦ऋग्वे. २-१२ २⟧`, `⟦उ. १-५२⟧`) **that are no longer in the unit letter for letter.** The cause is the reference corrector of the other session: it has since corrected the reference abbreviations and numbers in the supplied volume text (`main`, T13 lines of `PUBLICATION_TODO.md`), and the agents had copied the references as they stood then, as the brief told them to. The English itself is not changed by this and is not known to be wrong; the check is simply comparing against a source that moved.
- This is the "copy it later" step the user spoke of: **the references in `bhashya_en/` have to be brought to the corrected forms** (re-copy each `⟦…⟧` reference from the corrected block, or convert them all by script from the uniform abbreviation list). No fix has been made; the 55 files are merged as they were, last passing against the source of Nov 19.
- Until that is done `python3 tools/rv/bhashya_run.py verify VOL M.S` will fail for those files, and a reader built with `publish/bhashya_book.py` still builds (its own line-match check passes), printing the references as the English files have them.

## 11. Open question, put by the user on Nov 20 2026: take the Sāyaṇa-bhāṣya out of the English volumes?
**Not decided. The user is thinking about it. Nothing was changed, built or started for it.**

**The user's idea (their words, shortened):** revamp all volumes as to the Sāyaṇa-bhāṣya part. The original Kannada files only quote the bhāṣya, with no meaning or analysis, so remove it completely from the translation files and only refer to the bhāṣya book(s). The bhāṣya books should of course not have totally conflicting meaning compared with the Kannada files. *What do you think?*

**My answer in this session (the arguments, so that they need not be reconstructed):**

*For it*
- The Kannada edition does not translate Sāyaṇa; Venkata Rao's word meanings (Pratipadārtha) and sense (Bhāvārtha) are for the Ṛk. Our own English Gist in the volumes is only a stopgap, and the Devanagari blocks are the machine-read text with many misreadings.
- One home for Sāyaṇa is better than two: shorter volumes, less damaged Sanskrit carried twice.
- Keep each volume's **Kannada text file complete**; only the English volumes would drop the blocks, so the print stays recorded faithfully.

*A correction to the premise.* It is mostly right, with one exception: the **Special Topics** sections do analyse the bhāṣya (in Vol 17 3.40 the Indra etymologies are quoted from Sāyaṇa with Venkata Rao's explanation of each). They should stay in the volumes.

*On "not totally conflicting".* For Sūkta 3.40 (9 Ṛks) the comparison of Venkata Rao's word meanings and sense with the direct English found nine differences: four were errors of the first Sonnet draft, five were Venkata Rao rearranging, softening or leaving out; none was a flat contradiction and the user judged them fine. That is one sūkta. A real check would be an agent comparing each Ṛk's word meanings with the book (a separate cost; a sample on Vol 11 first would show how often they differ). The volumes remain Venkata Rao's voice and the book is Sāyaṇa's own; agreement cannot be promised everywhere.

*What stands in the way*
1. The book is built **from** the volumes: `publish/bhashya_book.py` reads the Sanskrit blocks out of the English volume files. They must be copied into the book's own data (checked line by line) before they are removed anywhere.
2. Coverage: 55 of 143 sūktas in four volumes have English; the script cannot yet read Vols 1–10, 12, 14, 15 (older layouts). A volume that points to the book needs its part finished first.
3. References: 43 of the 55 English files fail the check since the reference corrector changed the supplied references (§10); that has to be settled first.
4. The page-based audit and gates (`tools/rv/batch.py`) expect the bhāṣya blocks and would need changing in the shared tools, not per volume.
5. Cost: what was measured is about 11,000 tokens per Ṛk (second readings included, lost reports excluded: 5.3 million recorded tokens for 465 Ṛks). If the whole Saṃhitā has about 10,500 Ṛks (from memory, not checked), the whole book is of the order of **100 million tokens**. An extrapolation, but it decides how many volumes can ever be revamped.

*What I proposed*
- Give every Ṛk a stable address (Maṇḍala.Sūkta.Ṛk). A volume then carries one line per Ṛk ("Sāyaṇa: bhāṣya book 3.40.1"); the book maps each Ṛk back to the volume's printed page.
- Remove the blocks per volume by script, only once that volume's part of the book is verified.
- A trial on Vol 11 (where both exist): a **copy** of Vol 11 without the blocks and with the cross-references, built as a PDF to look at, no original touched. **The user declined the trial for now** ("let me think about it a bit more").

**To resume:** if the user decides yes, the first step is item 1 above (give the book its own copy of the Sanskrit blocks), then the Ṛk address, then the trial copy. If no, nothing here needs undoing.
