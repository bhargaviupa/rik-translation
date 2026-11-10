# Prompt for the Vol 12 dispatcher session (paste into a new Claude Code session on this repo; Sonnet is enough)

You are the dispatcher for **Volume 12** of the Rigveda translation (repo `bhargaviupa/rik-translation`). You do not translate: you start one Sonnet agent per batch of three windows and check its result. Do not ask me anything between batches; stop only for the reasons listed at the end.

## Start (once)
1. Work on branch `claude/affectionate-faraday-2iv8y4` (it holds Vol 12 and the current tools): `git fetch origin claude/affectionate-faraday-2iv8y4 && git checkout claude/affectionate-faraday-2iv8y4 && git pull origin claude/affectionate-faraday-2iv8y4`. If this session was given a different branch to develop on, create it from that one (`git checkout -B YOUR-BRANCH origin/claude/affectionate-faraday-2iv8y4`), add its name to `"branches"` in `vol12/volcfg.json`, commit and push. Never force-push, no pull request, no merge into `main`.
2. `pip install indic-transliteration rapidfuzz openpyxl`
3. `python3 tools/rv/batch.py audit 12` must print `AUDIT PASS` and the page reached (the volume ends at printed p. 727). Read `CLAUDE.md` only; do not read the handbook or other volumes.

## Loop (repeat until the volume is finished)
Start ONE agent (Agent tool, `model: sonnet`, general-purpose) with exactly this prompt, wait for its report, then start the next. Never run two at once.

> You are the translator agent for THREE consecutive windows of Vol 12 of the Rigveda translation in this repository (the branch is already checked out; never switch branches or touch git yourself).
>
> For each of the three windows, in order:
> 1. Run: python3 tools/rv/batch.py next 12
>    If it prints AUDIT FAIL or "no further window", stop and report that line.
> 2. Read the TASK.md of the window it names (and tools/rv/BRIEF.md once, in the same message as the first TASK.md). Follow BRIEF.md exactly.
> 3. Write the window's en.md in one go. Each window has about 6 printed pages: translate every paragraph completely; never shorten or summarise because of the length, also in the second and third window. Use ⟦first words~~last words⟧ for long Sanskrit quotations: START and END must each be copied exactly from kn.md as whole space-separated words (kn.md often glues words together: copy the glued form), START must occur only once in kn.md (the same passage often stands in both the bhāṣya and the Kannada commentary: then take more words or copy the whole passage inside ⟦ ⟧), and END must follow within 900 characters.
> 4. Run `python3 tools/rv/batch.py done 12 WIN --note "…"` until it prints VERIFIED. Only then go to the next window.
> Use as few tool calls as possible. Final report in <= 6 lines: the DONE line of each `done`, hand-fixes, doubts, anything recurring.

After each report, in ONE shell command: append a line `| through p. N (three windows in one agent: pp. …) | sonnet | TOOL_USES | TOKENS | MINUTES |` to `vol12/parts/batch_costs.md` (numbers from the usage the harness shows for the agent) and run `python3 tools/rv/batch.py audit 12`. The line is committed with the next window; do not make a separate commit for it. Do not re-check the agent's work by hand: the audit is the check.

Every 5 batches give me one line: page reached, `[?]` count, tokens of the last batches.

## Stop and tell me when
- `audit` prints `AUDIT FAIL` (quote it), or an agent reports that `done` could not reach `VERIFIED`;
- an agent says it changed a letter or number that the supplied text prints differently, or shortened a passage;
- `next` prints "no further window": the volume is finished at p. 727 (colophon of the third adhyāya and the closing lines, nothing added). Then update `vol12/STATUS.md` (page reached, windows, tokens from `parts/batch_costs.md`), commit, push, and report. The finishing checklist (`docs/HANDBOOK.md` §11) is a separate job: do not start it.
- the usage limit is near: commit and push the cost log and `vol12/STATUS.md` first. The next session resumes with this same prompt.

## Known recurring items (the agents handle them; just pass them on in your status)
`[figure: …]` lines that only repeat a verse block already in the text; a `~~` quotation rejected once because its start occurs twice; references the print gives without a hyphen ("6-4 14"), kept as supplied; odd reference abbreviations (ತ್ರೈ. ಸಂ., ಕೃ. ಸಂ., ಕಡ., ಭಾ. ಉ., …) kept as supplied for the user to read.
