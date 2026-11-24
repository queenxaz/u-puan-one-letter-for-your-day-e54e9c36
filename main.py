#!/usr/bin/env python3
"""One Letter for Your Day -- writes a single letter to entry.txt.

The letter is U, for "unhinged": the word for a day that went gloriously
off the rails. If the primary write fails for any reason, the fallback
letter C (for "chaotic") is written instead, so the entry is always one
single valid letter, A to Z, and nothing else.
"""

import os

LETTER = "U"    # unhinged
FALLBACK = "C"   # chaotic


def output_path():
    directory = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return os.path.join(directory, "entry.txt")


def write_letter(letter):
    # The gate requires exactly one character, A to Z, and nothing else:
    # no word, no gloss, no punctuation, no trailing newline.
    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(letter)


def main():
    try:
        write_letter(LETTER)
    except OSError:
        write_letter(FALLBACK)


if __name__ == "__main__":
    main()
