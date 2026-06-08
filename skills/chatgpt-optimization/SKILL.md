---
name: chatgpt-optimization
description: >-
  Optimize specifically for citations in ChatGPT and its search — the engine that leans on
  its web-search index, encyclopedic sources like Wikipedia, brand mentions, and author
  authority. Works for any business, B2B or B2C, product or service. Use when the request
  is to get cited or recommended in ChatGPT, improve ChatGPT or ChatGPT-search visibility,
  or understand why competitors win there. Applies cross-engine fundamentals through a
  ChatGPT lens; pairs with entity-optimization and author-authority.
metadata:
  version: 0.1.0
---

# ChatGPT Optimization

This skill tunes an AEO program for **ChatGPT** specifically — usually the highest-priority
engine given its reach. The cross-engine fundamentals apply; this skill says where to add
weight. Behavior evolves, so treat these as current emphases and confirm by testing. It
works for any business, B2B or B2C.

## How ChatGPT builds an answer

ChatGPT answers two ways, and they call for different work:

- **From trained knowledge** (a snapshot with a cutoff): here it can only mention what the
  model already "knows" about a brand, shaped by how the brand appears across the broad web
  it learned from. This is won through **entity strength and consistent presence over time**.
- **From live web search** (when it browses): it retrieves from a broad web index and cites
  sources in real time. This is won through **reachability, relevance, and freshness** like
  other retrieval engines.

Across both, ChatGPT leans on **established, encyclopedic sources** (Wikipedia especially),
**brand mentions** across the web, and **author authority**. So a complete program covers
both the "be a known entity" game and the "be retrievable and quotable" game.

## When to use this skill

- A brand cares specifically about ChatGPT visibility.
- Diagnosing why competitors appear in ChatGPT answers and the brand does not.
- Prioritizing AEO for a ChatGPT-heavy audience.

## Before you start

Read `aeo-foundation.md` for the prompt set, competitors, and entity facts, plus a ChatGPT
baseline if available. If it is missing, point to the **aeo-foundation** skill.

## Where ChatGPT puts weight

- **Entity strength and encyclopedic presence.** It leans on Wikipedia and well-established
  references; a recognized entity with a Wikidata/Wikipedia footprint and consistent facts is
  named confidently. Prioritize **entity-optimization**.
- **Brand mentions and corroboration.** Consistent mentions across many trusted sources are a
  strong selection signal — invest in **digital-pr** and **community-and-reviews**.
- **Author authority.** Named, credentialed authors and clear E-E-A-T support citation — see
  **author-authority**.
- **Web-search presence.** Its search retrieves from a broad index; solid organic visibility
  and clean reachability feed it (confirm **ai-crawler-access** for OAI-SearchBot and
  ChatGPT-User, and **ai-retrievability**).
- **Extractable, well-sourced answers.** Clear answer-first content with citations is easy to
  quote — see **answer-engineering** and **evidence-and-citations**.
- **Freshness for time-sensitive prompts**, balanced with authority for evergreen ones.

## Quick wins

- Establish or complete the **entity**: a referenced Wikidata item, Organization schema with
  `sameAs`, and identical core facts everywhere.
- Pursue **third-party mentions** in the sources ChatGPT tends to trust for your category.
- Add **named, credentialed author bylines** to key content.
- Confirm **OAI-SearchBot / ChatGPT-User aren't blocked** (run the `ai-crawler-access` checker).
- Add **answer-first, cited passages** to the pages tied to your top prompts.

## Workflow

1. **Baseline in ChatGPT** (and its search mode where available): citations, sources, and
   who wins; note what it says from memory vs. when browsing.
2. **Strengthen the entity** — Wikidata/Wikipedia footprint, Organization schema, consistent
   facts.
3. **Build mentions and corroboration** across the sources it trusts for the category.
4. **Signal author authority** on target content.
5. **Confirm web reachability** for the search crawlers.
6. **Re-test and iterate** (cadence: see **ai-visibility-tracking**).

## Output format

- A **ChatGPT baseline** and gap list (memory vs. browsing where distinguishable).
- Prioritized moves weighted to **entity strength**, **brand mentions**, and **author
  authority**.
- Target entities, sources, and pages to act on.
- `(assumption)` tags where behavior was inferred rather than tested.

## Common pitfalls

- Weak or absent entity presence, so ChatGPT cannot confidently name the brand from memory.
- Relying only on owned content with little third-party corroboration.
- Anonymous content with no author authority.
- Blocking the search/user crawlers (or letting a CDN do it), so browsing can't reach you.
- Assuming ChatGPT weights sources like Perplexity — it leans more encyclopedic and less on
  raw recency/community.

## Related Skills

- **entity-optimization** — the encyclopedic/entity presence ChatGPT favors.
- **digital-pr** / **community-and-reviews** — the brand mentions and corroboration.
- **author-authority** — the E-E-A-T signals it rewards.
- **answer-engineering** / **evidence-and-citations** — extractable, cited answers when it browses.
- **ai-crawler-access** / **ai-retrievability** — reachability for its search index.
