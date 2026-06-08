#!/usr/bin/env python3
"""
Parse web server access logs (common/combined format) and report how AI crawlers actually
behave on a site: which AI bots visit, how often, what they fetch, their HTTP status mix,
and when they last appeared. robots.txt says what's allowed; logs are the ground truth.
Pure standard library.

Usage:
  python parse_crawler_logs.py access.log
  cat access.log | python parse_crawler_logs.py -
  python parse_crawler_logs.py access.log --top 10

See ../../../references/ai-crawlers.md for the bot landscape; pair with ai-crawler-access.
"""

import argparse
import re
import sys
from collections import Counter, defaultdict

# substring match against the user-agent; label -> category
AI_BOTS = {
    "OAI-SearchBot": "retrieval", "ChatGPT-User": "user-triggered", "GPTBot": "training",
    "Claude-SearchBot": "retrieval", "Claude-User": "user-triggered", "ClaudeBot": "training",
    "PerplexityBot": "retrieval", "Perplexity-User": "user-triggered",
    "Google-Extended": "training", "Applebot-Extended": "training",
    "Bytespider": "training", "CCBot": "training", "Meta-ExternalAgent": "training",
}

LINE_RE = re.compile(
    r'"(?P<method>[A-Z]+)\s+(?P<path>\S+)[^"]*"\s+(?P<status>\d{3})\s+\S+'
    r'\s+"[^"]*"\s+"(?P<ua>[^"]*)"')
TS_RE = re.compile(r"\[(?P<ts>[^\]]+)\]")


def match_bot(ua):
    for name in AI_BOTS:
        if name.lower() in ua.lower():
            return name
    return None


def main():
    ap = argparse.ArgumentParser(description="Analyze AI-crawler behavior in access logs")
    ap.add_argument("logfile", help="path to access log, or - for stdin")
    ap.add_argument("--top", type=int, default=5, help="top N fetched paths per bot")
    args = ap.parse_args()

    stream = sys.stdin if args.logfile == "-" else open(args.logfile, encoding="utf-8", errors="replace")

    hits = Counter()
    statuses = defaultdict(Counter)
    paths = defaultdict(Counter)
    last_seen = {}
    parsed = unmatched_ua = 0

    for line in stream:
        m = LINE_RE.search(line)
        if not m:
            continue
        ua = m.group("ua")
        if ua in ("-", ""):
            unmatched_ua += 1
        bot = match_bot(ua)
        if not bot:
            continue
        parsed += 1
        hits[bot] += 1
        statuses[bot][m.group("status")] += 1
        paths[bot][m.group("path")] += 1
        ts = TS_RE.search(line)
        if ts:
            last_seen[bot] = ts.group("ts")

    if not hits:
        print("No AI-crawler hits found. Either no AI bots visited in this window, or the "
              "log lacks user-agents (common format). Use a combined-format log.")
        if unmatched_ua:
            print(f"({unmatched_ua} lines had an empty user-agent.)")
        return

    print("AI-crawler activity from logs\n")
    for bot in sorted(hits, key=lambda b: -hits[b]):
        status_mix = ", ".join(f"{s}:{c}" for s, c in sorted(statuses[bot].items()))
        ok = statuses[bot].get("200", 0)
        total = hits[bot]
        err = total - ok
        flag = "  <-- mostly errors/blocks" if total and err > ok else ""
        print(f"{bot} ({AI_BOTS[bot]}): {total} hits | status {status_mix}{flag}")
        print(f"   last seen: {last_seen.get(bot, 'n/a')}")
        for path, c in paths[bot].most_common(args.top):
            print(f"   {c:>5}  {path}")
        print()

    seen = set(hits)
    retrieval_missing = [b for b, cat in AI_BOTS.items() if cat == "retrieval" and b not in seen]
    if retrieval_missing:
        print("Retrieval/citation bots NOT seen in this window: "
              + ", ".join(retrieval_missing))
        print("If you expect AI citations, confirm they are allowed (ai-crawler-access) and "
              "that key pages are reachable (ai-retrievability).")
    print("\nNote: user-agents can be spoofed — verify important bots by published IP ranges.")


if __name__ == "__main__":
    main()
