#!/usr/bin/env python3
"""
Validate every inline <script>...</script> block in dashboard.html by running
each one through `node -c` independently.

Why not a single sed/grep extraction of "the" <script> block: dashboard.html
has more than one inline <script> tag (a tiny theme-flash-prevention snippet
plus the main dashboard script). A naive sed range address
(/<script>/,/<\/script>/) latches onto the FIRST <script> it finds and does
not close on that same line even if its own </script> is right there — it
keeps scanning until the LAST </script> in the file, sweeping the <style>
block and markup in between into the "JS" file and failing validation on
every run. This checks each block on its own instead.
"""
import re
import subprocess
import sys
import pathlib
import tempfile

ROOT = pathlib.Path(__file__).resolve().parent.parent
HTML_PATH = ROOT / "dashboard.html"


def main() -> int:
    html = HTML_PATH.read_text()
    blocks = re.findall(r"<script(?:\s[^>]*)?>(.*?)</script>", html, re.S)

    ok = True
    checked = 0
    with tempfile.TemporaryDirectory() as tmp:
        for i, code in enumerate(blocks):
            code = code.strip()
            if not code:
                continue  # external/empty <script> tag, nothing to check
            path = pathlib.Path(tmp) / f"check_{i}.js"
            path.write_text(code)
            result = subprocess.run(["node", "-c", str(path)], capture_output=True, text=True)
            if result.returncode != 0:
                print(f"FAILED: script block {i} has a syntax error:\n{result.stderr}")
                ok = False
            else:
                checked += 1

    if not ok:
        return 1
    print(f"OK: validated {checked} inline <script> block(s) in {HTML_PATH.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
