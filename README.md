# Vol 11 better scan (temporary storage; never merge this branch; plain git, not LFS: LFS uploads are blocked from cloud sessions)

600 dpi bilevel scan of Vol 11, PDF pages 1-140 (printed p. = PDF - 18), in two parts.
Get it in another session:

    git fetch origin scans-vol11
    git worktree add /tmp/scans origin/scans-vol11
    sh publish/tools/verify11/merge_scans.sh /tmp/scans/scans/11_Rigveda_Samhitha_Volume_11-1-70.pdf /tmp/scans/scans/11_Rigveda_Samhitha_Volume_11-71-140.pdf
