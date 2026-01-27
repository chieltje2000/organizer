# Organizer (starter repo)

A safe file/shortcut organizer (CLI + Tkinter UI), driven by a **required** TOML config.

This repo is intentionally a **starter skeleton**: it contains the *project structure*, config templates,
and clear design boundaries (core vs UI). The actual implementation is left for you to build step-by-step.

## Key safety rules (by design)

- A config file is **always required**.
- `[scan].include_extensions` is **required and must not be empty** (prevents accidental destructive runs).
- Refuses to run in filesystem root (e.g. `C:\\` or `/`) unless you explicitly override.
- Planner first → preview summary → confirm → execute.

## Quick start

1. Put a config in the folder where you want to run, named: `.organizer.toml`
   - Use the included starter config: `.organizer.toml`
   - See all options in: `organizer.config.reference.toml`

2. Create a virtual env and install editable:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   pip install -e .[dev]
   ```

3. Run (CLI / UI will be wired up later):
   ```bash
   organize
   ```

## Repo layout

- `src/organizer/core/` – core logic (no print/input, no tkinter)
- `src/organizer/interfaces/` – CLI and Tkinter UI
- `src/organizer/app.py` – entrypoint that chooses interface

## Next steps to implement (in order)

1. `core/config.py` – load + validate TOML (including safety checks)
2. `core/scan.py` – list entries + apply filters
3. `core/shortcut_resolver.py` – resolve `.lnk` / parse `.url`
4. `core/rules.py` – match operators
5. `core/planner.py` – build plan + resolve conflicts + summary (incl. unmatched counts)
6. `core/executor.py` – execute the plan + write a JSONL log
7. `interfaces/cli.py` – pretty summary + strict YES confirm
8. `interfaces/ui_tk.py` – minimal Tkinter preview/run window

License: MIT (see `LICENSE`)
