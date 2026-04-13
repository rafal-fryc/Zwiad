#!/usr/bin/env python3
"""Parse the Lexology digest HTML and extract relevant articles."""
import re
import sys

with open('/home/rafal/projecty/Zwiad/pipeline/runs/2026-04-13T22-26-28/emails/Lexology---practical-know-how-0.html', 'r', encoding='utf-8') as f:
    content = f.read()

print(f"File size: {len(content)} chars")

# Check if it's truly single-line
lines = content.split('\n')
print(f"Number of lines: {len(lines)}")
for i, line in enumerate(lines[:5]):
    print(f"Line {i}: {len(line)} chars")

# Try to find article patterns - look for section headers and article links
# Lexology emails typically have section headers and article links

# Find all URLs
urls = re.findall(r'href=["\']([^"\']+)["\']', content)
print(f"\nTotal URLs found: {len(urls)}")
for url in urls[:20]:
    print(f"  URL: {url[:100]}")

# Look for article titles - typically in <strong> or <a> tags
titles = re.findall(r'<strong[^>]*>([^<]+)</strong>', content)
print(f"\nStrong tags found: {len(titles)}")
for t in titles[:10]:
    print(f"  Strong: {t[:100]}")

# Look for h2/h3 tags (section headers)
headers = re.findall(r'<h[23][^>]*>([^<]+)<', content)
print(f"\nHeaders: {len(headers)}")
for h in headers[:20]:
    print(f"  Header: {h[:100]}")

# Look for article patterns with data attributes
articles = re.findall(r'data-title="([^"]+)"', content)
print(f"\nData-title attributes: {len(articles)}")
for a in articles[:10]:
    print(f"  Article: {a[:100]}")
