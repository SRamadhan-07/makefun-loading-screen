#!/usr/bin/env python3
"""Loading Screen Gold - writes a loading-screen tip to /output/entry.txt.

The tip is a single line of at most 200 characters, aimed at stressed
developers and AI coding agents who need a laugh mid-build.
"""

import os

ENTRY_TEXT = "Tip: The bug is never in the library. It is in the line you wrote at 2 a.m. and defended at 9."


def main() -> None:
    output_path = "/output/entry.txt"
    output_dir = os.path.dirname(output_path)
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY_TEXT)


if __name__ == "__main__":
    main()
