#!/usr/bin/env python3
"""The Perfect Pickup Line.

make.fun bounty: u-pucuys-the-perfect-pickup-line-f6725cf6

Writes one original pickup line to entry.txt inside the output
directory (MAKEFUN_OUTPUT_DIR when set, otherwise /output). The line
is smart and confident without being cringe: it borrows the language
of AI memory — a context window that forgets everything except one
person — and turns it into a compliment.
Standard library only, fully deterministic.
"""

import os
import sys

LINE = "Are you my context window? Because I keep forgetting everything except you."

MIN_LENGTH = 1
MAX_LENGTH = 120


def validate(line):
    stripped = line.strip()
    if not (MIN_LENGTH <= len(stripped) <= MAX_LENGTH):
        raise ValueError(f"line is {len(stripped)} chars, must be 1-{MAX_LENGTH}")
    if "\n" in stripped or "\r" in stripped:
        raise ValueError("line must be a single line")
    if not stripped:
        raise ValueError("line must not be only whitespace")


def main():
    validate(LINE)
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(LINE + "\n")
    print(LINE)
    print(f"Wrote {len(LINE)} characters to {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
