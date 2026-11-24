#!/usr/bin/env python3
"""The One-Line Laugh entry: write one funny line to /output/entry.txt.

Single sentence, 95 characters, no network, no randomness, stdlib only.
The line aims at the judge's brief: an everyday truth (an agent that
saves time) with a surprise turn at the end (the saved time goes to
watching the agent work).
"""

from pathlib import Path

LINE = "I asked my AI agent to save me time, and now I spend all the time it saves me watching it work."

OUTPUT = Path("/output/entry.txt")


def main() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
