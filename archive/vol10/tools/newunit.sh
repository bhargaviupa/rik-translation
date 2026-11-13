#!/bin/bash
# usage: newunit.sh uNN  -> worktree /home/user/v10wt/uNN on branch claude/pass2-vol10-uNN from claude/pass2-vol10 (scans/PDFs/other volumes not checked out)
set -e
U=$1; R=/home/user/rik-translation; W=/home/user/v10wt/$U
mkdir -p /home/user/v10wt; cd $R
GIT_LFS_SKIP_SMUDGE=1 git worktree add --no-checkout -B claude/pass2-vol10-$U $W claude/pass2-vol10 >/dev/null 2>&1
cd $W
git sparse-checkout set --no-cone '/*' '!/vol10/scans/' '!/vol10/*.pdf' '!/vol10/*.docx' '!/*.pdf' '!/*.docx' '!/publish/' '!/vol1/' '!/vol2/' '!/vol3/' '!/vol4/' '!/vol5/' '!/vol6/' '!/vol7/' '!/vol8/' '!/vol9/' '!/vol11/' '!/vol12/' '!/vol13/' '!/vol14/' >/dev/null 2>&1
GIT_LFS_SKIP_SMUDGE=1 git checkout >/dev/null 2>&1
echo $W
