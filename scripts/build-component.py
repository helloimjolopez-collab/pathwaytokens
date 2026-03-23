#!/usr/bin/env python3
"""
build-component.py
──────────────────
Generates SideNav-component.html from SideNav.html by stripping the
"Component Documentation" section.

The cut is marker-based, not line-number-based, so it stays correct as
the source file grows.

  Cut starts at:  the line containing @COMPONENT_ONLY_END
  Resumes at:     the line containing "end right column"
                  (the JSX closing div that follows the annotations zone)

Usage:
  python3 scripts/build-component.py

Run from the repo root.
"""

import sys
from pathlib import Path

REPO_ROOT    = Path(__file__).parent.parent
SOURCE       = REPO_ROOT / "SideNav.html"
OUTPUT       = REPO_ROOT / "SideNav-component.html"
CUT_MARKER   = "@COMPONENT_ONLY_END"
RESUME_MARKER = "end right column"


def build():
    lines = SOURCE.read_text(encoding="utf-8").splitlines(keepends=True)

    cut_idx = next((i for i, l in enumerate(lines) if CUT_MARKER in l), None)
    if cut_idx is None:
        print(f"ERROR: '{CUT_MARKER}' not found in {SOURCE.name}"); sys.exit(1)

    resume_idx = next((i for i, l in enumerate(lines) if i > cut_idx and RESUME_MARKER in l), None)
    if resume_idx is None:
        print(f"ERROR: '{RESUME_MARKER}' not found after cut point"); sys.exit(1)

    kept = lines[:cut_idx] + lines[resume_idx:]
    OUTPUT.write_text("".join(kept), encoding="utf-8")
    print(f"✓ {OUTPUT.name} written ({len(kept)} lines, {len(lines)-len(kept)} stripped)")


if __name__ == "__main__":
    build()
