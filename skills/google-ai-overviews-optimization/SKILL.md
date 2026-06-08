---
name: google-ai-overviews-optimization
description: >-
  Optimize specifically for Google AI Overviews (and AI Mode) — the answer surface that
  draws most heavily on top-ranking organic pages, structured and list/table formats, and
  E-E-A-T. Works for any business, B2B or B2C, product or service. Use when the request is
  to appear in Google AI Overviews, optimize for Google's AI answers or AI Mode, or
  understand why competitors are featured there. Applies cross-engine fundamentals through a
  Google AIO lens; pairs with answer-engineering and structured-data.
metadata:
  version: 0.1.0
---

# Google AI Overviews Optimization

This skill tunes an AEO program for **Google AI Overviews** (and the related AI Mode). Of
the major surfaces this one is closest to traditional search, so the emphasis is distinct.
The cross-engine fundamentals apply; this skill says where to add weight. Behavior evolves —
treat as current emphasis and confirm by testing. It works for any business, B2B or B2C.

> Scope note: AI Overviews sits on top of Google Search, so classic organic ranking is a
> prerequisite here. This skill covers the *AEO* layer (being selected and extracted for the
> Overview); deep general-SEO work belongs in a dedicated SEO effort.

## How AI Overviews builds an answer

For a query, Google generates an Overview by **drawing on pages that already rank well**,
extracting and synthesizing from several of them, and linking the sources. In **AI Mode**,
Google "fans out" a question into multiple sub-queries and assembles an answer from the
results of each. Two consequences:

- If you don't rank on page one for a query (or its sub-queries), you're rarely eligible for
  its Overview — organic relevance is the gateway.
- Among eligible pages, Google favors **clear, extractable structure** (direct answers,
  lists, tables, steps), strong **E-E-A-T**, and well-marked-up content.

## When to use this skill

- A brand wants to appear in Google AI Overviews / AI Mode.
- Diagnosing why competitors are featured in Overviews and the brand is not.
- Prioritizing AEO for a Google-heavy audience.

## Before you start

Read `aeo-foundation.md` for the prompt set and the brand's current organic-search standing.
If it is missing, point to the **aeo-foundation** skill.

## Where Google AI Overviews puts weight

- **Top organic rankings as a gateway.** Overviews overwhelmingly cite page-one pages.
  Without baseline organic relevance and quality, the other moves underperform.
- **Structured, extractable formats.** Lists, tables, step-by-steps, and direct answers are
  pulled often. Lean on **answer-engineering**.
- **E-E-A-T.** Demonstrated experience and expertise, named authors, trustworthy sourcing —
  see **author-authority** and **evidence-and-citations**.
- **Structured data.** Schema helps Google parse and qualify content — see **structured-data**.
- **Question-shaped, specific intent.** Long-tail, clearly phrased questions (and the
  sub-queries AI Mode fans out to) are well served by matching answer blocks.
- **Freshness** for time-sensitive queries.

## Quick wins

- For each target prompt, check the brand's **organic position**; fix ranking gaps first
  (that's the gateway).
- Add **direct-answer blocks, lists, and comparison tables** to the eligible pages.
- Strengthen **author bylines and schema** (Article + Person + FAQ where genuine) on those
  pages.
- Map the **sub-questions** a query fans out into and ensure you answer them too.

## Workflow

1. **Baseline in Overviews** for the prompt set: where they appear, who is cited, and the
   brand's organic position for each.
2. **Shore up organic relevance** on target queries — the gateway to eligibility.
3. **Restructure for extraction** — direct answers, lists, tables, question headings.
4. **Strengthen E-E-A-T and schema** on those pages.
5. **Target the right queries** — specific, question-based intent, plus their sub-queries.
6. **Re-test and iterate** (cadence: see **ai-visibility-tracking**).

## Output format

- A **Google AIO baseline** with the brand's organic position per target prompt.
- Prioritized moves, led by **organic-ranking gaps** and **structure/format** fixes.
- Target pages, queries, and sub-queries to act on.
- `(assumption)` tags where behavior was inferred rather than tested.

## Common pitfalls

- Chasing Overviews for queries the brand doesn't rank for organically — fix ranking first.
- Prose-only pages with nothing list/table/answer-shaped to extract.
- Weak E-E-A-T on YMYL queries, where Google is most demanding.
- Ignoring AI Mode's sub-queries and answering only the headline question.
- Assuming AIO behaves like Perplexity — it is far more tied to organic ranking and far less
  to community/recency.

## Related Skills

- **answer-engineering** — the list/table/answer structure Overviews pull from.
- **structured-data** — schema that helps Google parse and qualify content.
- **author-authority** / **evidence-and-citations** — the E-E-A-T signals it rewards.
- **gemini-optimization** — the overlapping Google-ecosystem playbook.
- **content-freshness** — recency for time-sensitive Overviews.
