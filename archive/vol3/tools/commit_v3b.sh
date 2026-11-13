#!/bin/bash
# commit_v3b.sh "UNIT" "PAGES" "EDITLINE" "DONE" "NEXT"
cd /home/user/rik-translation/vol3
echo "$1 ($2): $3" >> review/edits_v3b.txt
sed -i "s|^Done through: .*|Done through: $4.|; s|^Next unit: .*|Next unit: $5.|" parts/v3b_state.md
cd .. && git add -A vol3 && git commit -qm "v3b: $1 ($2) from the print

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01CtcBQSHTxDQuaAbUUddrnA" && for i in 1 2 3 4; do git push -q origin claude/numerals-vol3-b 2>/dev/null && break; sleep $((2**i)); done; git log --oneline -1
