#!/usr/bin/env python3
"""
build-component.py — DISABLED
──────────────────────────────
SideNav-figmamake.html is now a hand-authored static HTML spec sheet.
It is NOT generated from SideNav.html.

Running this script would overwrite the static spec sheet with a stripped
version of the React demo, which is the wrong format for Figma Make.

When to manually update SideNav-figmamake.html:
  - Design token values change (colours, radius, spacing)
  - A new component state is added or renamed
  - The CollapseButton behaviour changes
  - A new breakpoint or shell variant is added

See SideNav-spec.md §17.1 for what to update and when.
"""
import sys
print("ERROR: This script is disabled.")
print("SideNav-figmamake.html is a hand-authored static file — do not auto-generate.")
print("See SideNav-spec.md §17.1 for update guidance.")
sys.exit(1)
