#!/usr/bin/env python3
"""Parse Lexology digest HTML and extract relevant articles."""

import sys
import re
import json
from urllib.parse import urlparse

def main():
    filepath = '/home/rafal/projecty/Zwiad/input/lexology/2024-04-17_Lexology---practical-know-how.html'

    with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
        content = f.read()

    print(f"File size: {len(content)} chars")
    print(f"Number of lines: {content.count(chr(10))}")

    # Extract all links
    all_links = re.findall(r'href="([^"]*)"', content)
    print(f"\nTotal links found: {len(all_links)}")

    # Show unique domain patterns
    domains = set()
    for link in all_links:
        try:
            parsed = urlparse(link)
            domains.add(parsed.netloc)
        except:
            pass
    print(f"\nDomains found: {sorted(domains)}")

    # Extract anchor text with href
    anchors = re.findall(r'<a[^>]+href="([^"]*)"[^>]*>(.*?)</a>', content, re.DOTALL)
    print(f"\nTotal anchor elements: {len(anchors)}")

    # Show anchors with substantial text
    meaningful = [(href, re.sub(r'<[^>]+>', '', text).strip())
                  for href, text in anchors
                  if len(re.sub(r'<[^>]+>', '', text).strip()) > 15]

    print(f"\nAnchors with substantial text: {len(meaningful)}")
    print("\nAll meaningful anchors:")
    for href, text in meaningful:
        print(f"  TEXT: {text[:150]}")
        print(f"  HREF: {href[:200]}")
        print()


if __name__ == '__main__':
    main()
