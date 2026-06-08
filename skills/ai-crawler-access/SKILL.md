---
name: ai-crawler-access
description: >-
  Make sure answer engines can actually crawl a site, and set a deliberate access policy —
  the AI bot user-agent landscape, robots.txt rules, CDN/WAF (e.g. Cloudflare) allow/block
  configuration, and bot verification. Works for any business, B2B or B2C, product or
  service. Use when the request is to allow or block AI bots, configure robots.txt for
  GPTBot or ClaudeBot or PerplexityBot, check whether AI crawlers can access a site, fix
  AI invisibility caused by blocking, or decide a crawler policy. Reference the shared
  crawler table; pairs with ai-retrievability.
metadata:
  version: 0.1.0
---

# AI Crawler Access

This skill makes a site **reachable by answer engines** and sets a deliberate policy for
which bots get in. It is the most basic AEO prerequisite and a common silent failure: a
brand can do everything else right and still be invisible because a robots.txt rule or a
CDN default is blocking the retrieval crawlers that produce citations. It works for any
business, B2B or B2C.

The full user-agent landscape and configuration details live in the shared
[AI crawlers reference](../../references/ai-crawlers.md); this skill is the strategy and
workflow around it.

## When to use this skill

- Deciding and implementing an AI-bot access policy.
- Diagnosing AI invisibility that traces to blocked crawlers.
- Configuring robots.txt and CDN/WAF rules for AI bots.
- Verifying that real engine crawlers can reach the site.

## Before you start

Read `aeo-foundation.md` for the brand's stance (does it *want* AI visibility?) and the
technical context (platform, CDN). If it is missing, point to the **aeo-foundation** skill.

## The three bot categories (and why they change the decision)

- **Training crawlers** feed future models; blocking them affects training use, not live
  citations.
- **Retrieval / search crawlers** fetch in real time to build answers — these drive
  citations and referral traffic, and are usually the ones you most want to allow.
- **User-triggered fetchers** retrieve a page when a user asks about it — blocking them can
  stop live citation of pages users explicitly request.

See the reference for the current user-agent strings per provider.

## Decision framework

| Goal | Training crawlers | Retrieval / user-triggered |
|---|---|---|
| Maximize AI citations & referrals | Allow | Allow |
| Want citations, avoid training use | Disallow | Allow |
| Stay out of AI entirely | Disallow | Disallow (accepts zero AI visibility) |

Most brands pursuing AEO want the top or middle row. Choose deliberately rather than
inheriting a default.

## Workflow

1. **Audit current access.** Check `robots.txt` for AI user-agents, and check the CDN/WAF
   (some platforms now block AI bots by default on new sites). Look at server/CDN logs for
   which AI bots are actually reaching the site.
2. **Set the policy.** Decide per category using the framework above and the brand's
   stance.
3. **Configure robots.txt.** Allow the retrieval/user-triggered bots you want; allow or
   disallow training bots per policy. (Recipe in the reference.)
4. **Configure the CDN/WAF.** robots.txt is advisory — ensure firewall/bot-management rules
   are not silently blocking retrieval crawlers, and use them to hard-block anything you
   truly want excluded.
5. **Verify legitimacy.** Where a provider publishes official IP ranges, verify real bots
   by IP (and reverse-DNS), since user-agent strings can be spoofed.
6. **Re-test.** Confirm important pages are reachable; recheck periodically as user-agents
   and platform defaults change.

## Tool

This skill ships a checker that fetches a site's `robots.txt` and reports, per major AI
bot, whether it is allowed or blocked — flagging blocked **retrieval** bots (the ones that
produce citations and referral traffic). Pure standard library, no dependencies.

```bash
# Check a live site
python scripts/check_ai_crawlers.py example.com

# Also probe the homepage with each bot's user-agent to catch CDN/WAF blocks
python scripts/check_ai_crawlers.py example.com --live

# Evaluate a local robots.txt (e.g. before deploying a change)
python scripts/check_ai_crawlers.py --robots-file ./robots.txt
```

Use it for the audit step below and after any robots/CDN change. It reads `robots.txt`
only; a clean result there still warrants a CDN/WAF check (use `--live`).

> Optional. The script only automates this step; it needs `python3` (standard library only, no install). No Python? Just follow the steps above manually.

## Output format

- A **current-access audit** (robots.txt + CDN posture + observed bot hits).
- The **chosen policy** per bot category with rationale.
- The **robots.txt and CDN/WAF changes** to make (concrete rules).
- A **verification note** on confirming legitimate crawlers.
- `(assumption)` tags where infrastructure details were unknown.

## Common pitfalls

- A CDN/WAF (or a default-block setting) quietly blocking retrieval crawlers — the silent
  AEO killer.
- Blocking training but assuming that also blocks citation crawlers (different bots).
- Trusting user-agent strings without IP verification.
- Setting a policy once and never rechecking as bots and defaults evolve.

## Related Skills

- **ai-retrievability** — once crawlers reach the page, ensure they can read it.
- **ai-visibility-audit** — flags access problems as a discoverability failure.
- **llms-txt** — a complementary (low-impact) signal alongside access control.
