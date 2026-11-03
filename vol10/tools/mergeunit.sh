#!/bin/bash
# usage: mergeunit.sh uNN [nextUnit]  -> merge claude/pass2-vol10-uNN into claude/pass2-vol10, check structure, push, drop its worktree, create next worktree
set -e
U=$1; N=$2; cd /home/user/rik-translation
git merge --no-edit claude/pass2-vol10-$U 2>&1 | tail -1
python3 - <<'P'
import re
t=open('vol10/Rigveda_Samhita_Vol10_English_Translation.md').read()
assert t.count('**Progress note:**')==1 and len(re.findall(r'^#{1,6} ',t,re.M))==878, 'STRUCTURE CHANGED'
print('structure ok; [?] =',t.count('[?]'))
P
git push -q origin claude/pass2-vol10 2>&1 | tail -1 || true
git worktree remove --force /home/user/v10wt/$U 2>/dev/null || true
[ -n "$N" ] && vol10/tools/newunit.sh $N
