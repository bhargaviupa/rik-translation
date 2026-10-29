#!/bin/sh
# commit_w4b.sh "MESSAGE" -- commit everything and push the w4b branch
cd "$(dirname "$0")/../.." && git add -A && git commit -qm "$1

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01CtcBQUa5NuaJ3RtxtgmLda" && git push -qu origin claude/pass2-vol4-b 2>&1 | grep -v '^remote:' ; git log --oneline -1
