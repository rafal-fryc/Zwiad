#!/usr/bin/env python3
"""Extract articles from 2024-05-07 Lexology digest HTML."""

import re
import sys

filepath = '/home/rafal/projecty/Zwiad/input/lexology/2024-05-07_Lexology---practical-know-how.html'

with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
    content = f.read()

print(f"File size: {len(content)} chars", file=sys.stderr)

# Extract all anchor elements with href and text
anchors = re.findall(r'<a[^>]+href="([^"]*)"[^>]*>(.*?)</a>', content, re.DOTALL)
print(f"Total anchors: {len(anchors)}", file=sys.stderr)

# Filter for meaningful anchors (substantial text, not just images)
meaningful = []
for href, raw_text in anchors:
    text = re.sub(r'<[^>]+>', '', raw_text).strip()
    text = re.sub(r'\s+', ' ', text)
    if len(text) > 20 and not text.startswith('http'):
        meaningful.append((href, text))

print(f"Meaningful anchors: {len(meaningful)}", file=sys.stderr)
print("---ARTICLES---")
for href, text in meaningful:
    print(f"HREF: {href}")
    print(f"TEXT: {text[:200]}")
    print()
