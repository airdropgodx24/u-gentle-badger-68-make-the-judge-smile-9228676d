#!/usr/bin/env python3
"""Make the Judge Smile — writes one warm line about a small good thing
that happened today to /output/entry.txt (1-200 characters).

Standard library only, no network, no secrets, reads nothing outside
this repository. The entry is a single fixed line written by the author.
"""

import os

LINE = (
    "This morning a stranger at the bus stop lent me her umbrella, "
    "then waved off my thanks like the rain had been her idea all along."
)


def main():
    # Gate check: the entry must be 1-200 characters including the newline.
    text = LINE + "\n"
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry is {len(text)} characters, must be 1-200")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
