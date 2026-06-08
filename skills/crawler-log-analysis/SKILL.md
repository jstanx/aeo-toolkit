---
name: crawler-log-analysis
description: >-
  Analyze server or CDN access logs to see how AI crawlers actually behave on a site —
  which AI bots visit, how often, what they fetch, their HTTP status mix, and whether any
  are blocked or erroring. Works for any business, B2B or B2C, product or service. Use when
  the request is to analyze AI crawler logs, check if GPTBot or ClaudeBot or PerplexityBot
  are crawling, measure AI crawl coverage, or diagnose why AI is not fetching pages. Ships
  a log-parsing tool. Pairs with ai-crawler-access and ai-retrievability.
metadata:
  version: 0.1.0
---

# Crawler Log Analysis

`robots.txt` says what AI crawlers are *allowed* to do; **logs say what they actually do.**
This skill reads server/CDN access logs to reveal the ground truth of AI crawling — which
bots visit, how often, what they fetch, and whether they are getting blocked or erroring.
It turns "we think AI can crawl us" into evidence. It works for any business, B2B or B2C.

## When to use this skill

- Confirming whether AI crawlers (especially retrieval bots) actually reach the site.
- Diagnosing AI invisibility that traces to blocks or errors at the server/CDN.
- Measuring crawl coverage (are key pages being fetched?) and frequency (freshness).
- Spotting suspicious or spoofed bot traffic.

## Before you start

Read `aeo-foundation.md` for the priority pages (so you can judge coverage). Obtain access
logs in **combined format** (which includes the user-agent) — common format omits it and
won't show bots. Logs may come from the web server (nginx/Apache) or the CDN.

## What to look for

- **Which AI bots appear** — retrieval bots (OAI-SearchBot, Claude-SearchBot,
  PerplexityBot) matter most; they produce citations and referral traffic.
- **Frequency and recency** — how often each bot visits, and when it was last seen
  (informs freshness expectations).
- **What they fetch** — are your high-value pages among the top fetched paths? Coverage
  gaps mean important content isn't being read.
- **Status mix** — lots of 403/429/5xx for a bot signals a block or error, not access.
- **Absence** — a retrieval bot that never appears is a red flag to investigate.
- **Spoofing** — user-agents can be faked; verify important bots by published IP ranges.

## Tool

This skill ships a log parser (pure standard library):

```bash
python scripts/parse_crawler_logs.py access.log
cat access.log | python scripts/parse_crawler_logs.py -
python scripts/parse_crawler_logs.py access.log --top 10
```

It reports, per AI bot: hit count, HTTP status mix (flagging mostly-error bots), last-seen
timestamp, and top fetched paths — plus which retrieval bots were *not* seen.

> Optional. The script only automates this step; it needs `python3` (standard library only, no install). No Python? Just follow the steps above manually.

## Workflow

1. **Collect logs** (combined format) over a meaningful window — at least a couple of
   weeks, since AI crawl cadence varies.
2. **Run the parser** and read the per-bot summary.
3. **Interpret:** Are retrieval bots visiting? Are key pages in their top paths? Any
   error-heavy bots? Any expected bot missing entirely?
4. **Act:** route blocks/errors to **ai-crawler-access**; route unfetched-but-important
   pages to **ai-retrievability**; record crawl frequency to inform **content-freshness**.
5. **Re-check** after fixes and periodically as crawler behavior shifts.

## Output format

- A **per-bot activity summary** (hits, status mix, last seen, top paths).
- **Coverage gaps** — important pages AI bots are not fetching.
- **Problems** — blocked/error-heavy bots and absent retrieval bots.
- **Actions** routed to the owning skills.
- `(assumption)` tags where log scope or format limited the analysis.

## Common pitfalls

- Using common-format logs (no user-agent) and seeing nothing — use combined format.
- Trusting user-agent strings without IP verification.
- Sampling too short a window to see real crawl patterns.
- Ignoring status codes — "lots of hits" that are all 403s is a block, not coverage.

## Related Skills

- **ai-crawler-access** — set and fix the access policy these logs reveal.
- **ai-retrievability** — make the fetched pages readable and reachable.
- **content-freshness** — use observed crawl cadence to time refreshes.
- **ai-visibility-tracking** — pair crawl evidence with citation outcomes.
