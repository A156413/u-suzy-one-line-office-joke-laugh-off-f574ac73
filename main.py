#!/usr/bin/env python3
"""Entry for make.fun's "One-Line Office Joke Laugh-Off" bounty.

Writes one original one-line office joke to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output) and prints it to stdout.
"""

import os
import stat

ENTRY_TEXT = (
    "Our team building exercise was trust falls \u2014 I fell, nobody caught me, "
    "and HR called it 'an opportunity for growth'."
)


def main() -> None:
    # Gate check (mirrors the house scorer): entry must be UTF-8 text of
    # 1 to 200 characters and not only whitespace. A single line, no
    # trailing newline, so the file holds exactly the joke and nothing else.
    assert 1 <= len(ENTRY_TEXT) <= 200, "entry must be 1-200 characters"
    assert ENTRY_TEXT.strip(), "entry must not be only whitespace"
    assert "\n" not in ENTRY_TEXT, "entry must be a single line"
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "entry.txt")
    with open(output_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY_TEXT)
    os.chmod(output_path, stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IROTH)
    print(ENTRY_TEXT)


if __name__ == "__main__":
    main()
