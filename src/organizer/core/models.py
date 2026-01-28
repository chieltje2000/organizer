"""Data models (design placeholder).

Keep these as simple dataclasses later. Suggested models:
- FileItem: path, name, ext, is_dir, is_hidden, size, mtime
- ShortcutInfo: link_path, target_path, arguments, working_dir, type, is_broken
- PlannedAction: src_path, dest_path, action_type, kind, reason
- Summary: counts + examples buckets (planned/unmatched/skipped/conflicts/errors)
- Config: parsed config sections
"""

from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from typing import List, Optional


class Mode(Enum):
    MOVE = "move"
    COPY = "copy"


class Kind(Enum):
    FILE = "file"
    DIR = "dir"
    SHORTCUT = "shortcut"


class EntryType(Enum):
    FILE = "file"
    DIR = "dir"


class OnExistPolicy(Enum):
    RENAME = "rename"
    SKIP = "skip"
    ERROR = "error"
    OVERWRITE = "overwrite"


class UnmatchedPolicy(Enum):
    IGNORE = "ignore"
    MOVE_TO = "move_to"
    ERROR = "error"


class ShortcutType(Enum):
    LNK = "lnk"
    URL = "url"


@dataclass
class FileItem:
    path: Path
    kind: Kind
    name: str
    ext: str
    is_dir: bool
    is_hidden: bool
    size: Optional[int]
    mtime: Optional[float]


@dataclass
class ShortcutInfo:
    link_path: Path
    target_path: Optional[str]
    url: Optional[str]
    arguments: Optional[str]
    working_dir: Optional[str]
    type: ShortcutType
    is_broken: bool


@dataclass
class PlannedAction:
    src: Path
    dest: Path
    mode: Mode
    kind: Kind
    reason: str
    conflict: Optional[str] = None


@dataclass
class ExampleItem:
    label: str
    src: Optional[str]
    dest: Optional[str]
    reason: Optional[str]

@dataclass
class Summary:
    run_path: Path
    seen_total: int  # alles wat scanner “zag” op top-level, incl dirs/files
    candidates_total: int  # na filters; dit zijn items die aan rules aangeboden worden
    planned_total: int
    planned_files: int
    planned_dirs: int
    planned_shortcuts: int
    unmatched_total: int 
    unmatched_files: int
    unmatched_dirs: int
    unmatched_shortcuts: int
    skipped_total: int # ignore_dirs, ext filter, hidden, entry_type disallowed, etc.
    covered_total: int # items onder geplande dir moves; vooral relevant als recursive later true wordt
    conflicts_total: int
    errors_total: int
    examples_planned: list[ExampleItem]
    examples_unmatched: list[ExampleItem]
    examples_skipped: list[ExampleItem]
    examples_conflicts: list[ExampleItem]
    examples_errors: list[ExampleItem]


@dataclass
class GeneralConfig:
    mode: Mode
    destination_root: Optional[Path]
    dry_run_default: bool


@dataclass
class ScanConfig:
    recursive: bool
    include_hidden: bool
    include_extensions: frozenset[str]
    exclude_extensions: frozenset[str]
    include_entry_types: frozenset[EntryType]
    ignore_dirs: frozenset[str]


@dataclass
class ConflictConfig:
    on_exists: OnExistPolicy
    rename_pattern: str


@dataclass
class SafetyConfig:
    allow_filesystem_root: bool
    blocked_paths: tuple[Path, ...]


@dataclass
class DefaultsConfig:
    unmatched_shortcuts: UnmatchedPolicy
    unmatched_files: UnmatchedPolicy
    unmatched_dirs: UnmatchedPolicy
    unmatched_shortcuts_target: Optional[str]
    unmatched_files_target: Optional[str]
    unmatched_dirs_target: Optional[str]


@dataclass
class ReportingConfig:
    count_unmatched: bool
    examples_per_bucket: int


@dataclass
class RuleConfig:
    name: str
    kind: Kind
    match: dict
    target: str


@dataclass
class Config:
    general: GeneralConfig
    scan: ScanConfig
    conflicts: ConflictConfig
    safety: SafetyConfig
    defaults: DefaultsConfig
    reporting: ReportingConfig
    rules: List[RuleConfig]
