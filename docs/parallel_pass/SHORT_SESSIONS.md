# Short-session mode (Oct 29)
Pause point (all pushed, branches contain main, none merged): vol3 0bdff53, vol4-a 409e39d, vol4-b 5e8e604, vol5-a bf147d6, vol5-b 3b70e80, vol5-c 5c47921 (claude/pass2-*).
Each worker = a chain of short sessions (one sūkta or ~30 pp.) on the SAME branch, started with source_revision = the branch, template `worker_prompt_template_v2.txt`, YOUR RANGE line unchanged. Resume point = `volN/parts/<id>_state.md`. Work is safe on the branches; merge into main is separate and not needed for continuity.
Coordinator: when a slice session is idle and the part file does not start `RANGE DONE`, spawn the next slice; archive the finished session.
