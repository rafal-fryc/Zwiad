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

import sys
from urllib.parse import urlsplit, urlunsplit, parse_qsl, urlencode

_STRIP_PARAMS_PREFIXES = ("utm_",)
_STRIP_PARAMS_EXACT = {"g"}  # Lexology tracking param


def normalize_url(url: str) -> str:
    """Strip tracking params and canonicalize a URL.

    Rules:
    - http:// -> https:// (force scheme)
    - lowercase host, strip leading www.
    - drop utm_* params and the Lexology g= param (order-insensitive)
    - drop fragments, empty query strings, and trailing / on the path
    - whitespace trim
    """
    if not url:
        return ""
    url = url.strip()
    parts = urlsplit(url)
    if parts.scheme not in ("http", "https"):
        return url  # not a web URL; leave untouched
    host = parts.netloc.lower()
    if host.startswith("www."):
        host = host[4:]
    kept = [
        (k, v) for k, v in parse_qsl(parts.query, keep_blank_values=True)
        if not k.lower().startswith(_STRIP_PARAMS_PREFIXES)
        and k.lower() not in _STRIP_PARAMS_EXACT
    ]
    path = parts.path.rstrip("/") if parts.path != "/" else ""
    return urlunsplit(("https", host, path, urlencode(kept), ""))


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
