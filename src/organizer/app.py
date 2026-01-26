"""App entrypoint.

Design intent:
- Choose an interface (CLI or Tkinter UI).
- Interfaces call into core (plan/execute).
- Core must remain UI-agnostic (no print/input, no tkinter imports).
"""

def main() -> None:
    # PSEUDOCODE ONLY (implementation intentionally left to you):
    #
    # parse args:
    #   --ui (start tkinter)
    #   --config PATH (required unless .organizer.toml in run folder)
    #   --apply (execute; otherwise preview only)
    #
    # if --ui:
    #   start organizer.interfaces.ui_tk.run()
    # else:
    #   start organizer.interfaces.cli.run()
    #
    raise SystemExit(
        "Starter repo: app.main() not implemented yet. "
        "Next: implement core/config.py + interfaces/cli.py wiring."
    )
