"""Planner (design placeholder).

Responsibilities:
- build PlannedAction list from scanned items
- resolve destination paths (in-place vs destination_root)
- resolve conflicts using conflicts.on_exists (rename/skip/error/overwrite)
- enforce folder policy: if a dir is planned, do NOT plan items under it
- produce Summary: planned/unmatched/skipped/conflicts (+ examples)
"""
