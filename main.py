#!/usr/bin/env python3
"""news-image-20261119 entry generator.

Copies the pre-rendered front-page image (entry.png) from this directory
to the make.fun output directory. Standard library only, no network,
deterministic: the output bytes are always identical to entry.png.
Entry date: Thursday 19 November 2026.
"""

import hashlib
import os
import shutil
import sys

SOURCE_NAME = "entry.png"


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, SOURCE_NAME)

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")

    shutil.copyfile(src, dst)

    with open(dst, "rb") as fh:
        digest = hashlib.sha256(fh.read()).hexdigest()
    print(f"wrote {dst} ({os.path.getsize(dst)} bytes, sha256 {digest})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
