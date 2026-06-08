---
name: ai-referral-analytics
description: >-
  Track the traffic answer engines send to a site — set up analytics to capture and
  attribute referrals from ChatGPT, Perplexity, Gemini, and other AI assistants, including
  the large share that hides in "direct." Works for any business, B2B or B2C, product or
  service. Use when the request is to track AI referral traffic, see visits from ChatGPT or
  Perplexity in GA4, fix AI traffic showing as direct, attribute AI-assistant conversions,
  or measure AI traffic quality. Pairs with ai-visibility-tracking.
metadata:
  version: 0.1.0
---

# AI Referral Analytics

This skill makes **answer-engine traffic visible in analytics**. Citations only matter if
they drive outcomes, but a large share of AI-assistant traffic arrives with no referrer —
from mobile apps, copy-paste, and in-assistant browsers — and lands in "Direct," so most
brands badly undercount it. This skill captures and attributes that traffic and reads its
quality. The examples use GA4 patterns; the approach maps to any analytics platform. It
works for any business, B2B or B2C.

## When to use this skill

- Setting up tracking for AI-assistant referral traffic.
- Recovering AI traffic that is misattributed as Direct.
- Attributing conversions and revenue to AI sources.
- Reporting AI traffic volume and quality alongside visibility metrics.

## Before you start

Read `aeo-foundation.md` for the site/analytics context and the conversions that matter. If
it is missing, point to the **aeo-foundation** skill.

## The core problem

AI-assistant visits often carry **no referrer** (native apps, copy-pasted links,
assistant-embedded browsers), so analytics files them under Direct. Even referred visits
may not be grouped as "AI" by default. Without deliberate setup, AI's contribution is
invisible and undervalued.

## Setup (GA4 patterns)

1. **Use the AI channel grouping if available.** Newer analytics builds include an
   AI-assistant channel that classifies referred traffic from major assistants — enable and
   confirm it.
2. **Create a custom channel group / segment** for AI sources, matching the referrer/source
   domains of the assistants, for example:

   ```
   chatgpt.com|chat.openai.com|openai.com|perplexity.ai|gemini.google.com|
   copilot.microsoft.com|claude.ai|you.com|grok.com|meta.ai|deepseek.com
   ```

   Match on source/referrer to pull these out of generic Direct/Referral buckets.
3. **Tag links you control.** Where you can influence a link the assistant shows (e.g. in
   your own content or feeds), add UTM parameters (`utm_source`, `utm_medium=ai_assistant`)
   for explicit attribution.
4. **Track conversions by this segment.** Attribute sign-ups, leads, or sales to the AI
   segment to measure outcome, not just sessions.
5. **Accept a residual gap.** Some referrer-less AI traffic will remain in Direct; watch
   Direct for unexplained shifts that correlate with AI visibility gains, and report ranges
   rather than false precision.

## Reading the data

- **Volume & trend** — AI sessions over time, by source.
- **Quality** — conversion rate and engagement of AI traffic vs. other channels (often
  high-intent, since the user asked an assistant and clicked through).
- **Source mix** — which assistants actually send traffic for this brand.
- **Tie-back** — correlate referral gains with citation/SOV gains from
  **ai-visibility-tracking**.

## Output format

- The **analytics configuration**: channel group/segment definition and any UTM scheme.
- A **reporting view**: AI sessions, conversions, and quality vs. other channels.
- A **caveat note** on the residual Direct misattribution and how to read it.
- `(assumption)` tags where platform specifics were unknown.

## Common pitfalls

- Assuming Direct is "type-ins" when a chunk is unattributed AI traffic.
- Reporting AI sessions without conversions — volume without value.
- Over-claiming precision when referrer data is inherently incomplete.
- Setting it up once and not revisiting as assistants and referrer behavior change.

## Related Skills

- **ai-visibility-tracking** — the citation/SOV side; pair both for the full picture.
- **ai-visibility-audit** — connects traffic outcomes back to readiness gaps.
- **aeo-foundation** — the conversions and goals worth attributing.
