"""Copy the front-page image into the make.fun output directory."""

import os
import shutil

src = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
dest_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
if not os.path.isfile(src):
    raise SystemExit(f"error: source image missing: {src}")
size = os.path.getsize(src)
if size > 1048576:
    raise SystemExit(f"error: source image is {size} bytes, larger than 1048576")
os.makedirs(dest_dir, exist_ok=True)
shutil.copyfile(src, os.path.join(dest_dir, "entry.png"))
