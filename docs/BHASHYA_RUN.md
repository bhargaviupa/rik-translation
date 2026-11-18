# The bhāṣya-English run: dispatcher's runbook

The by-product book "Sāyaṇa's Ṛgveda-bhāṣya in English" (PUBLICATION_TODO T13). One agent renders one sūkta of Sāyaṇa's Sanskrit into English; the dispatcher (the main session) starts agents, checks and commits their files. All state is in the repository: a sūkta is done when its file `volN/bhashya_en/M<m>_S<sss>.md` exists and passes the check.

User decisions (Nov 18 2026): direct translation from Sāyaṇa's Sanskrit; **Fable agents**; web search allowed to settle damaged readings; no API budget; references are copied in Devanagari and get the series' uniform abbreviations later, from the list another session is consolidating; run through all volumes, restarting whenever credits allow.

## At the start of a session (or when a scheduled check-in fires)
1. `git pull` on the session branch; `pip install indic-transliteration rapidfuzz openpyxl` (and `weasyprint` + fonts of HANDBOOK §8 only for PDFs).
2. `python3 tools/rv/bhashya_run.py status`, then `next K`.
3. If agents of this run are still working, do nothing. Otherwise continue the loop.

## The loop
- Keep up to **3 agents** working at a time, each on a different sūkta, in the order `next` gives.
- Agent call: `subagent_type: general-purpose`, `model: fable`, prompt:

  > Work in /home/user/rik-translation. You are translating Sāyaṇa's Sanskrit commentary on one Ṛgveda sūkta into English. Read tools/rv/BHASHYA_BRIEF.md once and follow it exactly. Your task: VOL = N, M.S = m.s. Read no file other than the brief and the task file the first step prints; write no file other than your English file; do not commit.

- When an agent reports: `python3 tools/rv/bhashya_run.py verify N m.s`. Only on VERIFIED: `git add` that one file, commit `Bhāṣya English: Vol N, m.s`, push; append a line to `volN/parts/bhashya_costs.md` (sūkta, model, total agent tokens, NOTE count, readings count). If it is not VERIFIED, send the agent the check's output once; if it still fails, delete the file and let `next` give the sūkta out again.
- Never report a commit not seen in `git log`. Never two agents on one sūkta.
- After each volume: `python3 publish/bhashya_book.py N --notes` (questions and logged readings to `volN/review/`), commit; update PUBLICATION_TODO T13.

## Spot checks (the form check cannot judge meaning)
For the first sūkta of each volume, and about one sūkta in ten after that, the dispatcher reads two Ṛks of the English against the Sanskrit block. Kinds of error found on Sonnet's pilot (Sūkta 3.40) and now named in the brief: a gloss Sāyaṇa does not give; an epithet attached to the wrong word; a lost causative, particle or possessive; dictionary sense in place of Sāyaṇa's gloss. A sūkta with such errors is redone, and the brief is extended if the error is of a new kind.

## Volumes
`bhashya_run.py` skips a volume whose English file is in an older layout (Vols 1–10, 12, 14, 15 on Nov 18 2026), has no text (13) or is not translated yet (19). They join the run when `publish/bhashya_book.py` can read their layout (shared tool, not a per-volume script).
