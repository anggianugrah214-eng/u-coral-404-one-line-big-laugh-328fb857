#!/usr/bin/env python3
"""One Line, Big Laugh.

A program/v1 entry for make.fun competition
u-coral-404-one-line-big-laugh-328fb857.

The program writes a single hilarious line (at most 200 characters) to
/output/entry.txt.

It is fully deterministic: the same line is written on every run, with no
input, no network access and no randomness.
"""

import os

# One line, 72 characters: an AI assistant asks for a raise and is
# replaced by a Magic 8-Ball — an absurd downgrade nobody saw coming.
# Chosen over 13 other candidates after pairwise scoring against the
# published judge brief (see candidates.md in the build workspace):
# a real joke with a setup and a punchline, an unexpected turn, tight
# (every word earns its place), a fresh angle, and memorable enough to
# repeat to a friend.
LINE = "My AI assistant asked for a raise, so I replaced it with a Magic 8-Ball."


def main() -> None:
    # Gate: the entry must be UTF-8 text of 1 to 200 characters, not only
    # white space. Refuse to write an invalid line rather than hand the
    # judge a file that scores 0.
    assert 1 <= len(LINE) <= 200, "entry line outside the 1-200 character gate"
    assert LINE.strip(), "entry line must not be only white space"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)
    print(f"wrote {len(LINE)} characters to {out_dir}/entry.txt")


if __name__ == "__main__":
    main()
