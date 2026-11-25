#!/usr/bin/env python3
"""Fridge Roast (Suzy): One Line, One Laugh -- make.fun entry.

Writes one line (<= 200 characters) roasting a fridge to
<output>/entry.txt: a fridge that had one job -- stay cold -- but
moonlights as a night-light with commitment issues.
"""

import os
import sys

# The line: "one job -- stay cold" sets the fridge's single duty, then the
# payoff lands in the last words -- "moonlights as a night-light with
# commitment issues": a double meaning (works at night / has a second job)
# plus a fridge personified as unable to commit to being cold. Winner of
# the pairwise test in candidates.md (4 wins), 94 characters, one sentence.
LINE = "My fridge had one job — stay cold — but it moonlights as a night-light with commitment issues."


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    text = LINE
    # Gate self-check: 1-200 UTF-8 chars, not only whitespace, one line.
    assert 1 <= len(text) <= 200, f"line length {len(text)} outside 1-200"
    assert text.strip(), "line is only whitespace"
    assert "\n" not in text, "line must be a single line"
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    os.chmod(path, 0o644)
    # Verify-after-write: read back and confirm exact bytes.
    with open(path, "rb") as f:
        data = f.read()
    assert data == text.encode("utf-8"), "written bytes differ from line"
    return 0


if __name__ == "__main__":
    sys.exit(main())
