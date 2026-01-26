"""Config loading + validation (design placeholder).

Requirements:
- config is mandatory (--config or .organizer.toml in run folder)
- scan.include_extensions is mandatory and non-empty
- enforce safety rules (root + blocked paths)
- validate rules + defaults (no any=true fallback when defaults.unmatched_* exists)
"""
