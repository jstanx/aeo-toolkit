#!/usr/bin/env python3
"""
Check whether a site's robots.txt allows the major AI crawlers — the ones that
produce AI citations and referral traffic, plus the training and user-triggered
bots. Pure standard library, no dependencies.

Usage:
  python check_ai_crawlers.py example.com
  python check_ai_crawlers.py https://example.com/
  python check_ai_crawlers.py --robots-file ./robots.txt    # offline / testing

Notes:
  - robots.txt is advisory. A CDN/WAF (e.g. Cloudflare) can still block a bot even
    when robots.txt allows it. Pass --live to additionally probe the homepage with
    each bot's user-agent and report the HTTP status (best-effort).
  - If robots.txt is missing, the default is "allowed".
See ../../../references/ai-crawlers.md for the full landscape and access strategy.
"""

import argparse
import sys
import urllib.request
import urllib.robotparser
from urllib.parse import urlparse

# (user-agent, category). Categories: retrieval bots produce live citations/traffic.
AI_BOTS = [
    ("OAI-SearchBot", "retrieval"),
    ("ChatGPT-User", "user-triggered"),
    ("GPTBot", "training"),
    ("Claude-SearchBot", "retrieval"),
    ("Claude-User", "user-triggered"),
    ("ClaudeBot", "training"),
    ("PerplexityBot", "retrieval"),
    ("Perplexity-User", "user-triggered"),
    ("Google-Extended", "training (Gemini)"),
    ("Applebot-Extended", "training"),
    ("Bytespider", "training"),
    ("CCBot", "training (Common Crawl)"),
    ("Meta-ExternalAgent", "training"),
]

UA = "aeo-crawler-check/1.0 (+https://github.com/jstanx/aeo-toolkit)"


def normalize(site):
    if not site.startswith(("http://", "https://")):
        site = "https://" + site
    p = urlparse(site)
    return f"{p.scheme}://{p.netloc}"


def fetch_robots(base):
    url = base + "/robots.txt"
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=15) as r:
            if r.status == 200:
                return r.read().decode("utf-8", "replace"), None
            return None, f"robots.txt returned HTTP {r.status}"
    except Exception as e:  # noqa: BLE001 - report any fetch failure
        return None, str(e)


def live_status(base, ua):
    req = urllib.request.Request(base + "/", headers={"User-Agent": ua}, method="HEAD")
    try:
        with urllib.request.urlopen(req, timeout=15) as r:
            return str(r.status)
    except urllib.error.HTTPError as e:
        return str(e.code)
    except Exception as e:  # noqa: BLE001
        return f"err:{type(e).__name__}"


def main():
    ap = argparse.ArgumentParser(description="Check AI-crawler access via robots.txt")
    ap.add_argument("site", nargs="?", help="domain or URL, e.g. example.com")
    ap.add_argument("--robots-file", help="parse a local robots.txt instead of fetching")
    ap.add_argument("--live", action="store_true", help="also probe homepage per bot UA")
    args = ap.parse_args()

    base = normalize(args.site) if args.site else None

    if args.robots_file:
        robots = open(args.robots_file, encoding="utf-8").read()
        source = args.robots_file
    elif base:
        robots, err = fetch_robots(base)
        source = base + "/robots.txt"
        if robots is None:
            print(f"No robots.txt readable at {source} ({err}).")
            print("Default behavior: ALL crawlers allowed. (Check CDN/WAF separately.)")
            robots = ""  # empty robots => allow all
    else:
        ap.error("provide a site or --robots-file")

    rp = urllib.robotparser.RobotFileParser()
    rp.parse(robots.splitlines())

    print(f"AI-crawler access for {source}\n")
    print(f"{'bot':<20} {'category':<22} {'robots':<10}" + ("  live" if args.live else ""))
    print("-" * (52 + (8 if args.live else 0)))

    blocked_retrieval = []
    for bot, category in AI_BOTS:
        allowed = rp.can_fetch(bot, "/")
        verdict = "allowed" if allowed else "BLOCKED"
        if not allowed and category == "retrieval":
            blocked_retrieval.append(bot)
        row = f"{bot:<20} {category:<22} {verdict:<10}"
        if args.live and base:
            row += "  " + live_status(base, bot)
        print(row)

    print()
    if blocked_retrieval:
        print("WARNING: retrieval/citation bots are blocked in robots.txt: "
              + ", ".join(blocked_retrieval))
        print("These are the bots that produce AI citations and referral traffic.")
    else:
        print("OK: no retrieval/citation bots are blocked in robots.txt.")
    print("\nReminder: robots.txt is advisory — confirm your CDN/WAF is not blocking "
          "these bots too (use --live for a best-effort probe).")


if __name__ == "__main__":
    main()
