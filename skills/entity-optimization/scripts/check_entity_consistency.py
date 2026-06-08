#!/usr/bin/env python3
"""
Check whether a brand's canonical entity facts appear consistently across its profiles
(site, Wikidata, LinkedIn, Crunchbase, directories, review platforms). Inconsistent or
missing facts weaken how confidently engines recognize and describe the entity.
Pure standard library; works live (URLs) or offline (local HTML files).

Usage:
  python check_entity_consistency.py --sample           # print an example config
  python check_entity_consistency.py --input entity.json

Config JSON:
  {
    "facts": {"name": "Acme Analytics", "founded": "2019", "hq": "Austin"},
    "sources": [
      {"label": "About page", "url": "https://example.com/about"},
      {"label": "Saved profile", "file": "./linkedin.html"}
    ]
  }
See ../references/entity-playbook.md for the consistency strategy.
"""

import argparse
import json
import re
import sys
import urllib.request
from html.parser import HTMLParser

SAMPLE = {
    "facts": {"name": "Acme Analytics", "founded": "2019", "hq": "Austin"},
    "sources": [
        {"label": "About page", "url": "https://example.com/about"},
        {"label": "Saved LinkedIn", "file": "./linkedin.html"},
    ],
}


class _Text(HTMLParser):
    def __init__(self):
        super().__init__()
        self.parts = []
        self._skip = 0

    def handle_starttag(self, tag, attrs):
        if tag in ("script", "style"):
            self._skip += 1

    def handle_endtag(self, tag):
        if tag in ("script", "style") and self._skip:
            self._skip -= 1

    def handle_data(self, data):
        if not self._skip:
            self.parts.append(data)

    def text(self):
        return re.sub(r"\s+", " ", " ".join(self.parts))


def load_source(src):
    if src.get("url"):
        req = urllib.request.Request(src["url"], headers={"User-Agent": "aeo-entity/1.0"})
        raw = urllib.request.urlopen(req, timeout=20).read().decode("utf-8", "replace")
    elif src.get("file"):
        raw = open(src["file"], encoding="utf-8").read()
    else:
        raise ValueError(f"source {src.get('label')!r} needs 'url' or 'file'")
    p = _Text()
    p.feed(raw)
    return p.text()


def main():
    ap = argparse.ArgumentParser(description="Check entity fact consistency across sources")
    ap.add_argument("--input", help="path to JSON config")
    ap.add_argument("--sample", action="store_true", help="print a sample config")
    args = ap.parse_args()

    if args.sample:
        print(json.dumps(SAMPLE, indent=2))
        return
    if not args.input:
        ap.error("provide --input <config.json> or --sample")

    cfg = json.load(open(args.input, encoding="utf-8"))
    facts = cfg.get("facts", {})
    if not facts:
        sys.exit("config needs a non-empty 'facts' object")

    print("Entity consistency check\n")
    print(f"Canonical facts: " + ", ".join(f"{k}={v!r}" for k, v in facts.items()) + "\n")

    missing_counts = {k: 0 for k in facts}
    n_sources = 0
    for src in cfg.get("sources", []):
        label = src.get("label") or src.get("url") or src.get("file")
        try:
            text = load_source(src).lower()
        except Exception as e:  # noqa: BLE001
            print(f"- {label}: could not load ({e})")
            continue
        n_sources += 1
        found, missing = [], []
        for k, v in facts.items():
            (found if str(v).lower() in text else missing).append(k)
            if str(v).lower() not in text:
                missing_counts[k] += 1
        status = "all facts present" if not missing else f"MISSING: {', '.join(missing)}"
        print(f"- {label}: {status}")

    print()
    if n_sources:
        for k, c in missing_counts.items():
            if c:
                print(f"  fact '{k}' absent from {c}/{n_sources} sources — verify consistency")
        if not any(missing_counts.values()):
            print("  All canonical facts found across all reachable sources.")
    print("\nNote: absence may mean the source phrases the fact differently — confirm "
          "manually. Reconcile toward what is true on the public web.")


if __name__ == "__main__":
    main()
