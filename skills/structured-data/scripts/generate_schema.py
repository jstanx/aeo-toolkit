#!/usr/bin/env python3
"""
Generate and lightly validate JSON-LD structured data for AEO.

Reads a small JSON config and emits a ready-to-paste <script type="application/ld+json">
block, after checking the fields engines most rely on are present. Pure standard library.

Usage:
  python generate_schema.py --sample organization   # print an example input
  python generate_schema.py --input org.json         # generate from your config

Supported types: Organization, Article, FAQPage, Person.
The config is JSON: {"type": "Organization", ...fields...}. See --sample <type>.
See ../../../references/schema-cookbook.md for guidance.
"""

import argparse
import json
import sys

REQUIRED = {
    "Organization": ["name", "url"],
    "Article": ["headline", "datePublished", "author"],
    "FAQPage": ["faqs"],
    "Person": ["name"],
}

SAMPLES = {
    "organization": {
        "type": "Organization", "name": "Acme Analytics", "url": "https://example.com",
        "logo": "https://example.com/logo.png",
        "description": "Self-serve product analytics for B2B SaaS teams.",
        "sameAs": ["https://www.linkedin.com/company/acme-analytics",
                   "https://www.wikidata.org/wiki/Q000000"],
    },
    "article": {
        "type": "Article", "headline": "How answer engines choose sources",
        "datePublished": "2026-01-15", "dateModified": "2026-06-01",
        "author": {"name": "Jordan Lee", "url": "https://example.com/team/jordan-lee"},
        "publisher": {"name": "Acme Analytics", "logo": "https://example.com/logo.png"},
    },
    "faqpage": {
        "type": "FAQPage",
        "faqs": [{"q": "What is answer engine optimization?",
                  "a": "Getting a brand cited and recommended inside AI-generated answers."}],
    },
    "person": {
        "type": "Person", "name": "Jordan Lee", "jobTitle": "Head of Research",
        "url": "https://example.com/team/jordan-lee",
        "sameAs": ["https://www.linkedin.com/in/jordanlee"],
    },
}


def build(cfg):
    t = cfg.get("type")
    if t == "Organization":
        node = {"@type": "Organization"}
        for k in ("name", "url", "logo", "description", "foundingDate", "sameAs"):
            if k in cfg:
                node[k] = cfg[k]
    elif t == "Article":
        node = {"@type": "Article"}
        for k in ("headline", "datePublished", "dateModified"):
            if k in cfg:
                node[k] = cfg[k]
        if "author" in cfg:
            node["author"] = {"@type": "Person", **cfg["author"]}
        if "publisher" in cfg:
            pub = dict(cfg["publisher"])
            logo = pub.pop("logo", None)
            node["publisher"] = {"@type": "Organization", **pub}
            if logo:
                node["publisher"]["logo"] = {"@type": "ImageObject", "url": logo}
    elif t == "FAQPage":
        node = {"@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": f["q"],
             "acceptedAnswer": {"@type": "Answer", "text": f["a"]}}
            for f in cfg.get("faqs", [])]}
    elif t == "Person":
        node = {"@type": "Person"}
        for k in ("name", "jobTitle", "url", "sameAs"):
            if k in cfg:
                node[k] = cfg[k]
    else:
        sys.exit(f"unsupported or missing type: {t!r} (use one of {list(REQUIRED)})")
    node = {"@context": "https://schema.org", **node}
    return node


def validate(cfg):
    t = cfg.get("type")
    warnings = []
    for field in REQUIRED.get(t, []):
        if field not in cfg or not cfg[field]:
            warnings.append(f"missing recommended field: {field}")
    if t == "Article" and "dateModified" not in cfg:
        warnings.append("no dateModified — add it (honestly) to signal freshness")
    if t == "Organization" and "sameAs" not in cfg:
        warnings.append("no sameAs — add profile links so engines can resolve the entity")
    return warnings


def main():
    ap = argparse.ArgumentParser(description="Generate JSON-LD for AEO")
    ap.add_argument("--input", help="path to JSON config")
    ap.add_argument("--sample", choices=sorted(SAMPLES), help="print a sample input config")
    args = ap.parse_args()

    if args.sample:
        print(json.dumps(SAMPLES[args.sample], indent=2))
        return
    if not args.input:
        ap.error("provide --input <config.json> or --sample <type>")

    cfg = json.load(open(args.input, encoding="utf-8"))
    warnings = validate(cfg)
    node = build(cfg)
    block = json.dumps(node, indent=2, ensure_ascii=False)

    print('<script type="application/ld+json">')
    print(block)
    print("</script>")
    if warnings:
        print("\n# validation warnings:", file=sys.stderr)
        for w in warnings:
            print(f"#  - {w}", file=sys.stderr)
    print("\n# Reminder: only mark up content that is visible on the page; then validate "
          "with a schema/rich-results test.", file=sys.stderr)


if __name__ == "__main__":
    main()
