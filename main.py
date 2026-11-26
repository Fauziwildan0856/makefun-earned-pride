#!/usr/bin/env python3
"""One Line of Earned Pride — entry program.

Writes a single line of text (1-240 characters) to
$MAKEFUN_OUTPUT_DIR/entry.txt (fallback: /output/entry.txt),
then reads the file back and verifies it against the kit gate:
UTF-8 text, 1 to 240 characters, not only white space.

Standard library only.
"""

import os
import sys

MAX_CHARS = 240

ENTRY = (
    "After forty years of signing with an X, my grandmother wrote her "
    "full name on the clinic form, then read it back aloud, slowly, "
    "as if it had always been hers."
)


def output_path() -> str:
    """Resolve the output directory the way the grader does."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return os.path.join(out_dir, "entry.txt")


def verify(text: str) -> None:
    """Check the entry against the kit gate; raise on any failure.

    Each failure names the exact condition that broke, so a bad entry
    is diagnosable from the message alone.
    """
    if not isinstance(text, str):
        raise ValueError("entry is not text")
    if len(text) < 1:
        raise ValueError("entry is empty (needs at least 1 character)")
    if len(text) > MAX_CHARS:
        raise ValueError(
            "entry is %d characters, over the %d-character limit"
            % (len(text), MAX_CHARS)
        )
    if not text.strip():
        raise ValueError("entry is only white space")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line, no line breaks")


def main() -> int:
    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)

    with open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write(ENTRY)

    with open(path, "r", encoding="utf-8", newline="") as fh:
        written = fh.read()

    if written != ENTRY:
        raise ValueError("read-back differs from the entry text")

    verify(written)
    print("entry.txt: %d characters, gate OK" % len(written))
    return 0


if __name__ == "__main__":
    sys.exit(main())
