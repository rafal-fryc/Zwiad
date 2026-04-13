#!/usr/bin/env python3
"""Single source of truth for URL normalization across the Zwiad pipeline.

Both `tools/update_reports_index.py` and `pipeline/scripts/dedup-findings.sh`
import / shell out to this module so URL dedup behavior stays consistent.

CLI:
    python3 tools/url_norm.py <url>
        Prints the normalized form to stdout.

    python3 tools/url_norm.py --batch < urls.txt
        Reads URLs from stdin (one per line) and prints normalized forms.

Library:
    from tools.url_norm import normalize_url
    norm = normalize_url("http://example.com/foo?utm_source=x")
"""

import re
import sys


def normalize_url(url: str) -> str:
    """Strip tracking params and canonicalize a URL.

    Rules:
    - http:// → https:// (force scheme)
    - Strip ?utm_*=... and &utm_*=... params
    - Strip Lexology-style ?g=... and &g=... tracking params
    - Drop trailing ? and trailing /
    - Whitespace trim
    """
    if not url:
        return ""
    url = url.strip()
    url = re.sub(r"^http://", "https://", url)
    url = re.sub(r"[?&]utm_[^&]*", "", url)
    url = re.sub(r"[?&]g=[^&]*", "", url)
    url = re.sub(r"\?$", "", url)
    url = re.sub(r"/$", "", url)
    return url


def main() -> int:
    if len(sys.argv) < 2:
        print("Usage: url_norm.py <url> | url_norm.py --batch < urls.txt", file=sys.stderr)
        return 2
    if sys.argv[1] == "--batch":
        for line in sys.stdin:
            print(normalize_url(line.rstrip("\n")))
        return 0
    print(normalize_url(sys.argv[1]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
