#!/bin/bash
# usage: newunit.sh uNN  -> creates worktree /home/user/v10wt/uNN on branch claude/pass2-vol10-uNN from the current claude/pass2-vol10 (scans not copied)
set -e
U=$1; R=/home/user/rik-translation; W=/home/user/v10wt/$U
mkdir -p /home/user/v10wt
cd $R
GIT_LFS_SKIP_SMUDGE=1 git worktree add --no-checkout -B claude/pass2-vol10-$U $W claude/pass2-vol10 >/dev/null 2>&1
cd $W
git sparse-checkout init --no-cone >/dev/null 2>&1
printf '/*\n!/vol10/scans/\n!/*.pdf\n!/*.docx\n!/publish/\n!/vol1/\n!/vol2/\n!/vol3/\n!/vol4/\n!/vol5/\n!/vol6/\n!/vol12/\n!/vol13/\n!/vol14/\n' > .git/info/sparse-checkout 2>/dev/null || true
GIT_LFS_SKIP_SMUDGE=1 git checkout >/dev/null 2>&1 || GIT_LFS_SKIP_SMUDGE=1 git read-tree -mu HEAD
echo $W
