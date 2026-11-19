#!/usr/bin/env python3
"""Write the 19 November 2026 front page to the output directory.

The front page is pre-rendered and stored next to this program as
``entry.png`` (JPEG bytes, 1024 by 1024). This program copies it to the
directory the grader reads -- ``/output`` unless ``MAKEFUN_OUTPUT_DIR``
says otherwise -- and then checks the copy: it must start with the JPEG
magic bytes, stay under the 1 MiB cap, and measure 1024 by 1024 pixels.

Standard library only, no network, deterministic: the same input file
always produces the same output bytes.
"""

import hashlib
import os
import shutil
import struct
import sys
from pathlib import Path

SOURCE = Path(__file__).resolve().with_name("entry.png")
MAX_BYTES = 1_048_576
EXPECT_WIDTH = 1024
EXPECT_HEIGHT = 1024


def jpeg_size(data: bytes) -> tuple[int, int]:
    """Read width and height out of a JPEG's first start-of-frame marker."""
    if data[:2] != b"\xff\xd8":
        raise ValueError("not a JPEG: bad magic bytes")
    pos = 2
    while pos + 4 <= len(data):
        if data[pos] != 0xFF:
            pos += 1
            continue
        marker = data[pos + 1]
        if marker in (0xC0, 0xC1, 0xC2):
            height, width = struct.unpack(">HH", data[pos + 5:pos + 9])
            return width, height
        if marker in (0xD8, 0xD9) or 0xD0 <= marker <= 0xD7:
            pos += 2
            continue
        (length,) = struct.unpack(">H", data[pos + 2:pos + 4])
        pos += 2 + length
    raise ValueError("no start-of-frame marker found")


def main() -> int:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.png"

    shutil.copyfile(SOURCE, target)
    data = target.read_bytes()

    if len(data) > MAX_BYTES:
        raise ValueError(f"entry too big: {len(data)} bytes")
    if data[-2:] != b"\xff\xd9":
        raise ValueError("truncated JPEG: no end-of-image marker")
    width, height = jpeg_size(data)
    if (width, height) != (EXPECT_WIDTH, EXPECT_HEIGHT):
        raise ValueError(f"unexpected size: {width}x{height}")

    digest = hashlib.sha256(data).hexdigest()
    print(f"wrote {target} ({len(data)} bytes, {width}x{height}, sha256 {digest})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
