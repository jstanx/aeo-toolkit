#!/usr/bin/env python3
"""
Generate a valid /llms.txt from a small JSON config. Pure standard library.

Usage:
  python generate_llms_txt.py --sample            # print an example config
  python generate_llms_txt.py --input site.json   # generate llms.txt

Config JSON:
  {
    "name": "Brand",
    "summary": "One to three sentence description.",
    "sections": [
      {"title": "Key pages",
       "links": [{"title": "Product", "url": "https://example.com/product", "note": "what it is"}]}
    ],
    "contact": {"email": "hello@example.com"}
  }
See ../SKILL.md for honest expectations — llms.txt is low-impact today.
"""

import argparse
import json
import sys

SAMPLE = {
    "name": "Acme Analytics",
    "summary": "Self-serve product analytics for B2B SaaS teams. Track activation, "
               "retention, and funnels without SQL.",
    "sections": [
        {"title": "Key pages", "links": [
            {"title": "Product", "url": "https://example.com/product", "note": "what it does"},
            {"title": "Docs", "url": "https://example.com/docs", "note": "how to use it"},
            {"title": "About", "url": "https://example.com/about", "note": "company facts"},
        ]},
    ],
    "contact": {"email": "hello@example.com"},
}


def render(cfg):
    lines = [f"# {cfg['name']}", ""]
    if cfg.get("summary"):
        lines += [f"> {cfg['summary']}", ""]
    for section in cfg.get("sections", []):
        lines.append(f"## {section['title']}")
        for link in section.get("links", []):
            note = f" - {link['note']}" if link.get("note") else ""
            lines.append(f"- [{link['title']}]({link['url']}){note}")
        lines.append("")
    contact = cfg.get("contact") or {}
    if contact:
        lines.append("## Contact")
        for k, v in contact.items():
            lines.append(f"- {k.capitalize()}: {v}")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def validate(cfg):
    warnings = []
    if not cfg.get("name"):
        warnings.append("missing 'name'")
    if not cfg.get("summary"):
        warnings.append("missing 'summary' (a 1–3 sentence description is recommended)")
    if not cfg.get("sections"):
        warnings.append("no 'sections' — add curated links to your most important pages")
    return warnings


def main():
    ap = argparse.ArgumentParser(description="Generate llms.txt")
    ap.add_argument("--input", help="path to JSON config")
    ap.add_argument("--sample", action="store_true", help="print a sample config")
    args = ap.parse_args()

    if args.sample:
        print(json.dumps(SAMPLE, indent=2))
        return
    if not args.input:
        ap.error("provide --input <config.json> or --sample")

    cfg = json.load(open(args.input, encoding="utf-8"))
    for w in validate(cfg):
        print(f"# warning: {w}", file=sys.stderr)
    sys.stdout.write(render(cfg))


if __name__ == "__main__":
    main()
