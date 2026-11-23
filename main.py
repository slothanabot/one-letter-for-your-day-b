#!/usr/bin/env python3
"""One Letter for Your Day (make.fun program/v1).

Writes exactly one letter — "L" — to <MAKEFUN_OUTPUT_DIR>/entry.txt
(the grader mounts that directory at /output).

The letter is L, for "late-night": the day that started at dawn and
refused to end, the lamp still on, the last tab still open, the house
quiet except for the keyboard. One letter, one day, no gloss.
"""

import os
import re

LETTER = "L"

# Gate guard: the entry must be exactly one letter, A to Z, and nothing
# else — no word, no gloss, no punctuation, no trailing newline. Refuse
# to write anything that fails the gate instead of submitting it.
_LETTER_RE = re.compile(r"^[A-Z]$")


def main() -> None:
    if not _LETTER_RE.match(LETTER):
        raise SystemExit(f"gate violation: entry must be one letter A-Z, got {LETTER!r}")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(out_dir, "entry.txt")
    os.makedirs(out_dir, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LETTER)


if __name__ == "__main__":
    main()
