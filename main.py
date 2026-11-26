#!/usr/bin/env python3
"""news-image-20261126 entrypoint.

Copies the bundled front-page image (entry.png) to the output path.
Standard library only: no third-party packages, no network.
The image is verified before it is written: PNG signature plus sha256.
"""
import hashlib
import os
import sys

# sha256 of the bundled entry.png, recorded at build time.
EXPECTED_SHA256 = "d5e4cbd613e8286fce9eef8a98764cb3a03d3edc455e1d99f959ebf4932829dd"
PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    dst = os.path.join(out_dir, "entry.png")

    with open(src, "rb") as fh:
        data = fh.read()

    if not data.startswith(PNG_SIGNATURE):
        print("error: entry.png is not a PNG file", file=sys.stderr)
        return 1
    digest = hashlib.sha256(data).hexdigest()
    if digest != EXPECTED_SHA256:
        print("error: entry.png sha256 mismatch", file=sys.stderr)
        return 1

    # The IHDR chunk (bytes 16-24) must declare 1024x1024.
    width = int.from_bytes(data[16:20], "big")
    height = int.from_bytes(data[20:24], "big")
    if (width, height) != (1024, 1024):
        print("error: entry.png is %dx%d, expected 1024x1024" % (width, height),
              file=sys.stderr)
        return 1

    os.makedirs(out_dir, exist_ok=True)
    with open(dst, "wb") as fh:
        fh.write(data)

    # Byte-exact read-back: the output must be identical to the bundle.
    with open(dst, "rb") as fh:
        written = fh.read()
    if written != data:
        print("error: output bytes differ from entry.png", file=sys.stderr)
        return 1
    print("wrote %s (%d bytes, sha256 %s)" % (dst, len(data), digest))
    return 0


if __name__ == "__main__":
    sys.exit(main())
