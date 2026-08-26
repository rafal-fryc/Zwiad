#!/usr/bin/env python3
"""Fetch archived Lexology digest .eml files from the FileTransfer repo's
`Lexology/` subdirectory and extract HTML bodies + metadata.

Usage: python3 tools/fetch_lexology_emails.py [OUTPUT_DIR]
"""

import json
import re
import sys
from pathlib import Path
from urllib.request import Request, urlopen

sys.path.insert(0, str(Path(__file__).resolve().parent))
from fetch_fpf_emails import (  # noqa: E402
    download_file,
    extract_html_from_eml,
    extract_metadata_from_eml,
)


REPO = "rafal-fryc/FileTransfer"
SUBDIR = "Lexology"


def fetch_subdir_files(repo: str = REPO, subdir: str = SUBDIR) -> list[dict]:
    url = f"https://api.github.com/repos/{repo}/contents/{subdir}"
    req = Request(url, headers={"Accept": "application/vnd.github.v3+json"})
    with urlopen(req) as resp:
        return json.loads(resp.read())


def main() -> None:
    output_dir = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("input/lexology")
    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"Fetching Lexology file list from {REPO}/{SUBDIR}...")
    files = fetch_subdir_files()
    eml_files = [f for f in files if f["name"].endswith(".eml")]
    print(f"Found {len(eml_files)} .eml files")

    for f in sorted(eml_files, key=lambda x: x["name"]):
        name = f["name"]
        safe_name = re.sub(r"[^\w\s.-]", "", name).replace(" ", "-")
        base = safe_name.rsplit(".", 1)[0]

        html_path = output_dir / f"{base}.html"
        meta_path = output_dir / f"{base}.meta.json"

        if html_path.exists():
            print(f"  [skip] {name} (already extracted)")
            continue

        print(f"  [download] {name}...")
        eml_bytes = download_file(f["download_url"])

        html_body = extract_html_from_eml(eml_bytes)
        if html_body:
            html_path.write_bytes(html_body)
            meta = extract_metadata_from_eml(eml_bytes)
            meta["source_filename"] = name
            with open(meta_path, "w") as mf:
                json.dump(meta, mf, indent=2)
            print(f"    -> {html_path.name} + {meta_path.name}")
        else:
            print(f"    [warn] No HTML body found in {name}")

    print(f"\nDone. Files saved to {output_dir}/")


if __name__ == "__main__":
    main()
