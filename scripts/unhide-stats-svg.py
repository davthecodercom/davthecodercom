#!/usr/bin/env python3
"""Make github-readme-stats SVGs visible without CSS animations."""

from __future__ import annotations

import re
import sys
from pathlib import Path


def unhide(text: str) -> str:
    text = text.lstrip()
    if text.startswith("<svg") and "xmlns=" not in text.split(">", 1)[0]:
        text = text.replace("<svg", '<svg xmlns="http://www.w3.org/2000/svg"', 1)
    text = re.sub(r"\.stagger\s*\{[^}]*\}", ".stagger { opacity: 1; }", text)
    return text


def main() -> None:
    if len(sys.argv) < 2:
        raise SystemExit("usage: unhide-stats-svg.py <svg> [<svg> ...]")
    for raw in sys.argv[1:]:
        path = Path(raw)
        path.write_text(unhide(path.read_text()))


if __name__ == "__main__":
    main()
