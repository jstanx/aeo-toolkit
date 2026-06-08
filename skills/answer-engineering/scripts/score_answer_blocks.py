#!/usr/bin/env python3
"""
Score a page for answer-engine extractability: question-style headings, a 40–60 word
direct answer right after each heading, short paragraphs, and use of lists/tables.
Works on Markdown or HTML, from a file or a URL. Pure standard library.

Usage:
  python score_answer_blocks.py page.md
  python score_answer_blocks.py page.html
  python score_answer_blocks.py --url https://example.com/page

See ../references/answer-patterns.md for the patterns this checks.
"""

import argparse
import re
import sys
import urllib.request
from html.parser import HTMLParser

QUESTION_STARTS = ("how", "what", "why", "when", "where", "who", "which", "is", "are",
                   "can", "do", "does", "should", "will")


def is_question(heading):
    h = heading.strip().lower()
    return h.endswith("?") or h.split(" ")[0] in QUESTION_STARTS


def word_count(text):
    return len(re.findall(r"\b\w+\b", text))


def sentences(text):
    return [s for s in re.split(r"(?<=[.!?])\s+", text.strip()) if s]


class _Extractor(HTMLParser):
    """Linearize HTML into ('heading'|'block'|'list'|'table', text) events."""
    def __init__(self):
        super().__init__()
        self.events = []
        self._tag = None
        self._buf = []
        self._skip = 0

    def handle_starttag(self, tag, attrs):
        if tag in ("script", "style"):
            self._skip += 1
        if tag in ("h1", "h2", "h3", "h4", "p", "li"):
            self._flush()
            self._tag = tag

    def handle_endtag(self, tag):
        if tag in ("script", "style") and self._skip:
            self._skip -= 1
        if tag == self._tag:
            self._flush()
        if tag in ("ul", "ol"):
            self.events.append(("list", ""))
        if tag == "table":
            self.events.append(("table", ""))

    def handle_data(self, data):
        if self._skip or not self._tag:
            return
        self._buf.append(data)

    def _flush(self):
        if self._tag and self._buf:
            text = re.sub(r"\s+", " ", "".join(self._buf)).strip()
            if text:
                kind = "heading" if self._tag in ("h1", "h2", "h3", "h4") else "block"
                self.events.append((kind, text))
        self._tag, self._buf = None, []


def parse_markdown(text):
    events = []
    for raw in text.splitlines():
        line = raw.rstrip()
        m = re.match(r"^(#{1,4})\s+(.*)$", line)
        if m:
            events.append(("heading", m.group(2).strip()))
        elif re.match(r"^\s*[-*+]\s+|^\s*\d+\.\s+", line):
            events.append(("list", line.strip()))
        elif "|" in line and re.search(r"\|.*\|", line):
            events.append(("table", line.strip()))
        elif line.strip():
            events.append(("block", line.strip()))
    return events


def to_sections(events):
    """Group into [(heading, first_block, has_list_or_table)] sections."""
    sections, cur = [], None
    for kind, text in events:
        if kind == "heading":
            if cur:
                sections.append(cur)
            cur = {"heading": text, "first_block": None, "has_list_table": False}
        elif cur is not None:
            if kind == "block" and cur["first_block"] is None:
                cur["first_block"] = text
            if kind in ("list", "table"):
                cur["has_list_table"] = True
    if cur:
        sections.append(cur)
    return sections


def main():
    ap = argparse.ArgumentParser(description="Score answer-block extractability")
    ap.add_argument("path", nargs="?", help="Markdown or HTML file")
    ap.add_argument("--url", help="fetch and score a URL")
    args = ap.parse_args()

    if args.url:
        req = urllib.request.Request(args.url, headers={"User-Agent": "aeo-score/1.0"})
        content = urllib.request.urlopen(req, timeout=20).read().decode("utf-8", "replace")
        is_html = True
    elif args.path:
        content = open(args.path, encoding="utf-8").read()
        is_html = args.path.lower().endswith((".html", ".htm")) or "<html" in content.lower()
    else:
        ap.error("provide a file path or --url")

    if is_html:
        p = _Extractor()
        p.feed(content)
        events = p.events
    else:
        events = parse_markdown(content)

    sections = to_sections(events)
    if not sections:
        sys.exit("no headings/sections found to score")

    good_answer = good_question = 0
    print("Answer-block scorecard\n")
    for s in sections:
        wc = word_count(s["first_block"]) if s["first_block"] else 0
        q = is_question(s["heading"])
        answer_ok = 40 <= wc <= 60
        good_answer += answer_ok
        good_question += q
        flags = []
        if not q:
            flags.append("heading not a question")
        if s["first_block"] is None:
            flags.append("no text block after heading")
        elif not answer_ok:
            flags.append(f"first block {wc}w (aim 40–60)")
        long_paras = s["first_block"] and len(sentences(s["first_block"])) > 5
        if long_paras:
            flags.append("opening block >5 sentences")
        status = "OK" if not flags else "; ".join(flags)
        print(f"- {s['heading'][:60]!r}: {status}")

    n = len(sections)
    print(f"\nSections: {n}")
    print(f"Question-style headings: {good_question}/{n}")
    print(f"40–60 word answer blocks: {good_answer}/{n}")
    score = round(100 * (good_question + good_answer) / (2 * n))
    print(f"Extractability score: {score}/100")
    if score < 70:
        print("\nFix: lead each section with a question heading and a 40–60 word "
              "self-contained answer (see answer-engineering).")


if __name__ == "__main__":
    main()
