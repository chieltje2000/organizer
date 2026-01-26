"""Scanning & filtering (design placeholder).

Pipeline:
- list entries in run_path
- skip ignore_dirs
- if entry is file: require ext in include_extensions and not in exclude_extensions
- if entry is dir: include only when include_entry_types contains 'dir'
- ALWAYS count unmatched (no rule) in summary (reporting.count_unmatched=true)
"""
