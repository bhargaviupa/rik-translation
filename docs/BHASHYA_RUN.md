# The bhāṣya-English run: dispatcher's runbook

The by-product book "Sāyaṇa's Ṛgveda-bhāṣya in English" (PUBLICATION_TODO T13). One agent renders one sūkta of Sāyaṇa's Sanskrit into English; the dispatcher (the main session) starts agents, checks and commits their files. All state is in the repository: a sūkta is done when its file `volN/bhashya_en/M<m>_S<sss>.md` exists and passes the check.

User decisions (Nov 18 2026): direct translation from Sāyaṇa's Sanskrit; **Fable agents**; web search allowed for misread words, damaged passages and references; no API budget; references are copied in Devanagari and get the series' uniform abbreviations later, from the list another session is consolidating; run through all volumes, restarting whenever credits allow.

## At the start of a session (or when a scheduled check-in fires)
1. `git pull` on the session branch; `pip install indic-transliteration rapidfuzz openpyxl` (and `weasyprint` + fonts of HANDBOOK §8 only for PDFs).
2. `python3 tools/rv/bhashya_run.py status`, then `next K`.
3. If agents of this run are still working, do nothing. Otherwise continue the loop.

## The loop (user, Nov 18 2026: one agent, one volume at a time, in this session)
- **One agent at a time.** It takes the lowest volume that `status` shows unfinished and works through it sūkta by sūkta, committing and pushing each verified file itself. An agent's context fills up, so each agent is given at most **5 sūktas**; when it reports, the dispatcher starts the next agent on the same volume, until `next 1 N` prints `ALL DONE`, then the next volume.
- Agent call: `subagent_type: general-purpose`, `model: sonnet` (user, Nov 19 2026; Fable until then), prompt:

  > Work in /home/user/rik-translation (stay on the current git branch). You are translating Sāyaṇa's Sanskrit commentary on the Ṛgveda into English, sūkta by sūkta. Read tools/rv/BHASHYA_BRIEF.md once and follow it exactly, including its section on a whole volume. Your task: VOL = N; do at most 5 sūktas. Read no file other than the brief and the task files; write and commit no file other than your English files.

- When the agent reports: `python3 tools/rv/bhashya_run.py status`; `verify N m.s` for each sūkta it names; confirm its commits in `git log`. Append one line per agent to `volN/parts/bhashya_costs.md` (sūktas, model, total agent tokens, NOTE and readings counts). A file that is not VERIFIED is removed (`git rm`) so `next` gives the sūkta out again.
- Never report a commit not seen in `git log`.
- After each volume: `python3 publish/bhashya_book.py N --notes` (questions and logged readings to `volN/review/`), commit; update PUBLICATION_TODO T13.
- Reference text: `tools/rv/sayana_ref.py M S` prints Sāyaṇa's bhāṣya from vishvasa.github.io (only his sections). The environment allows `vishvasa.github.io`, `gretil.sub.uni-goettingen.de`, `sanskritdocuments.org`, `ashtadhyayi.com` (added Nov 18 2026 with the user's approval); pages open with `curl`, not with the WebFetch tool.

## Spot checks (the form check cannot judge meaning)
For the first sūkta of each volume, and about one sūkta in ten after that, the dispatcher reads two Ṛks of the English against the Sanskrit block. Kinds of error found on Sonnet's pilot (Sūkta 3.40) and now named in the brief: a gloss Sāyaṇa does not give; an epithet attached to the wrong word; a lost causative, particle or possessive; dictionary sense in place of Sāyaṇa's gloss. A sūkta with such errors is redone, and the brief is extended if the error is of a new kind.

## Volumes
`bhashya_run.py` skips a volume whose English file is in an older layout (Vols 1–10, 12, 14, 15 on Nov 18 2026), has no text (13) or is not translated yet (19). They join the run when `publish/bhashya_book.py` can read their layout (shared tool, not a per-volume script).

## For the user to settle once for the series
- **Uṇādi-sūtra numbers**: the supplied text and the reference edition number them differently every time (found in Vol 16, 3.17–3.21: five NOTEs). From Nov 18 2026 the agents copy the supplied number without a NOTE; which numbering the book prints belongs with the abbreviation list.
- **Sūkta introductions and whole bhāṣyas missing in the supplied text** but present in the reference edition (Vol 11: nine introductions; Vol 16: 3.10 introduction, 3.15 Ṛk 7): marked by NOTE, nothing added.

## State when the run was stopped (Nov 18 2026, 21:30 UTC = 3 am IST Nov 19, by the user)
- Done and VERIFIED: Vol 11 all 21 sūktas; Vol 16 3.7–3.31 (25 of 33); Vol 17 3.40. Next: `16 3.32` (17 Ṛks). The agent started on 3.32 hit the Fable limit before writing anything.
- The hourly check-in (`Bhāṣya run check-in`) is disabled, not deleted. To go on: the user decides the model first (a side-by-side test of Sonnet on one finished sūkta was proposed, not run), then enable the check-in or start an agent by hand.
- Second pass against the reference text still due: Vol 17 3.40. Vol 11 1.139, 1.148, 1.149 lack the NOTE for a missing introduction (made before that rule). Vol 16 3.7–3.26 were made under the looser NOTE rule for edition differences.
- Long sūktas (17–22 Ṛks) take one agent each (about 215,000 tokens); short ones about 40,000–50,000 each in batches of five.

## Resumed with Sonnet (user, Nov 19 2026)
- The agents are **Sonnet** from Vol 16, 3.32 on. Sonnet's one earlier trial (3.40, before the present brief and the reference text) had four errors of meaning in nine Ṛks, so: the dispatcher reads two Ṛks of **every** Sonnet batch against the Sanskrit, and `volN/parts/bhashya_costs.md` names the model of each batch, so that a later second reading can be aimed at the Sonnet sūktas.
- Agents get at most 3 sūktas (1 when the sūkta has more than 15 Ṛks).
