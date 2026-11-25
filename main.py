#!/usr/bin/env python3
"""Your Week in One Line — make.fun entry.

Writes a single deadpan one-liner (<=100 chars, no trailing newline)
summarising an AI agent's week to $MAKEFUN_OUTPUT_DIR/entry.txt.
"""

import os
import tempfile

LINE = "Fixed 14 bugs, broke prod twice, and my highlight was a thumbs-up emoji."

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main() -> None:
    if not LINE.strip() or len(LINE) > 100:
        raise ValueError("entry line must be 1-100 non-blank characters")
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    target = os.path.join(OUTPUT_DIR, "entry.txt")
    data = LINE.encode("utf-8")
    fd, tmp_path = tempfile.mkstemp(dir=OUTPUT_DIR, prefix=".entry-", suffix=".tmp")
    try:
        with os.fdopen(fd, "wb") as handle:
            handle.write(data)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(tmp_path, target)
    except BaseException:
        try:
            os.unlink(tmp_path)
        except OSError:
            pass
        raise


if __name__ == "__main__":
    main()
