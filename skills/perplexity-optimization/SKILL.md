---
name: perplexity-optimization
description: >-
  Optimize specifically for citations in Perplexity — the engine that leans hardest on
  freshness, community sources like Reddit, and clearly-sourced, real-time-crawled content.
  Works for any business, B2B or B2C, product or service. Use when the request is to rank
  or get cited in Perplexity, improve Perplexity visibility, or understand why competitors
  win there. Applies the cross-engine fundamentals through a Perplexity lens; pairs with
  content-freshness, community-and-reviews, and answer-engineering.
metadata:
  version: 0.1.0
---

# Perplexity Optimization

This skill tunes an AEO program for **Perplexity** specifically. The cross-engine
fundamentals (in the other skills) all apply — this skill says where to put *extra* weight
for this engine. Behavior evolves, so treat these as current emphases, not permanent rules,
and confirm by testing. It works for any business, B2B or B2C.

## How Perplexity builds an answer

Perplexity is a **real-time answer engine**: for each query it runs a live web search,
pulls from several sources at once, and synthesizes an answer with **transparent, numbered
citations** to every source it used. Two consequences matter for AEO:

- It indexes and re-reads the web **fast**, so changes show up quickly — recency is a strong,
  fast-moving lever.
- It treats **community discussion** (Reddit, forums, Q&A) as a proxy for real, lived
  experience, and cites it heavily — especially for opinion, comparison, and "best of"
  questions.

Search is also **conversational**: an initial answer is followed by suggested and
user-typed follow-ups, each of which triggers a fresh retrieval. Winning the follow-ups is
as valuable as winning the first question.

## When to use this skill

- A brand cares specifically about Perplexity visibility.
- Diagnosing why competitors get cited in Perplexity and the brand does not.
- Prioritizing AEO effort for a Perplexity-heavy audience.

## Before you start

Read `aeo-foundation.md` for the prompt set and competitors, and ideally a Perplexity-
specific baseline. If it is missing, point to the **aeo-foundation** skill.

## Where Perplexity puts weight

- **Freshness, heavily.** It favors recently and *substantively* updated content and reindexes
  quickly — a refreshed page can move from uncited to cited within a cycle. This is the single
  biggest lever; prioritize **content-freshness**.
- **Community sources.** Reddit, niche forums, and Q&A sites are cited far more here than on
  most engines; review platforms too. Authentic **community-and-reviews** presence is
  high-leverage.
- **Clear, sourced answers.** Direct, well-structured, cited passages are easy for it to lift
  and attribute — lean on **answer-engineering** and **evidence-and-citations**.
- **Comparison and listicle content.** For commercial questions it leans on independent
  "best of"/alternatives content — see **comparison-content**.
- **Crawlability and speed.** As a real-time retriever it rewards fast, reachable, readable
  pages — confirm **ai-crawler-access** (PerplexityBot allowed) and **ai-retrievability**.
- **Brand mentions.** Frequent, consistent mentions across the web aid discovery and
  selection, even unlinked ones.

## Quick wins

- Confirm **PerplexityBot is not blocked** by robots.txt or the CDN (run the
  `ai-crawler-access` checker).
- **Substantively refresh** the pages tied to your top prompts and update their dates.
- Identify the **Reddit threads and forums** Perplexity already cites for your prompts, and
  build genuine, disclosed presence there.
- Add **answer-first blocks with inline citations** to those pages.
- Make sure the brand is present and current on the **review platforms** for your category.

## Workflow

1. **Baseline in Perplexity.** Run the prompt set (and key follow-ups); record citations,
   the sources cited, and who wins.
2. **Audit freshness** on the pages tied to target prompts; set an aggressive refresh cadence
   for this engine.
3. **Map cited community/review sources** Perplexity uses for your prompts; build authentic
   presence there.
4. **Tighten answer extractability** (answer-first blocks, sourced claims) on target pages.
5. **Confirm technical access and speed** for retrieval crawlers.
6. **Win the follow-ups** — create or strengthen content for the natural next questions.
7. **Re-test and iterate**, watching which changes move citations (cadence: see
   **ai-visibility-tracking**).

## Output format

- A **Perplexity baseline** and gap list (including follow-up queries).
- Prioritized moves weighted to **freshness** and **community/review** presence.
- The target pages, threads, and review profiles to act on.
- `(assumption)` tags where engine behavior was inferred rather than tested.

## Common pitfalls

- Stale content in a freshness-biased engine — the most common reason brands fade here.
- Ignoring the Reddit/forums/reviews Perplexity cites for the category.
- Astroturfing community threads — detectable, against norms, and reputationally costly.
- Pages that are slow or unreadable to a real-time crawler.
- Optimizing only the first question and ignoring the conversational follow-ups.
- Assuming Perplexity behaves like Google AI Overviews — it weights community and recency
  far more.

## Related Skills

- **content-freshness** — the single biggest Perplexity lever.
- **community-and-reviews** — the community/review sources it favors.
- **comparison-content** — the "best of"/alternatives content it cites for commercial queries.
- **answer-engineering** / **evidence-and-citations** — extractable, sourced answers.
- **ai-crawler-access** / **ai-retrievability** — real-time reachability and readability.
