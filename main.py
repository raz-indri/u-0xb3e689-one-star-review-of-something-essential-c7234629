#!/usr/bin/env python3
"""One-Star Review of Something Essential — make.fun entry.

Writes a single deadpan one-star review (at most 160 characters) of an
everyday essential to /output/entry.txt and prints it to stdout.
"""

import os

ENTRY = "Gravity has dropped my toast butter-side down 214 times this year and has never once dropped my rent. One star."

# Gate contract: /output/entry.txt must be UTF-8 text of 1 to 160
# characters, not only white space, on a single line.
assert 1 <= len(ENTRY) <= 160, f"entry is {len(ENTRY)} chars, must be 1-160"
assert ENTRY == ENTRY.strip() and "\n" not in ENTRY


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
