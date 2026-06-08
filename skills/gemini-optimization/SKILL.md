---
name: gemini-optimization
description: >-
  Optimize specifically for Google Gemini — the assistant tied into Google's ecosystem,
  drawing on Google search and entities (Knowledge Graph), strong E-E-A-T, and Google
  surfaces like YouTube. Works for any business, B2B or B2C, product or service. Use when
  the request is to get cited or recommended in Gemini, improve Gemini visibility, or
  understand why competitors win there. Applies cross-engine fundamentals through a Gemini
  lens; pairs with entity-optimization and google-ai-overviews-optimization.
metadata:
  version: 0.1.0
---

# Gemini Optimization

This skill tunes an AEO program for **Google Gemini**. The cross-engine fundamentals apply;
this skill says where to add weight. Behavior evolves — treat as current emphasis and confirm
by testing. It works for any business, B2B or B2C.

## How Gemini builds an answer

Gemini sits inside **Google's ecosystem** and grounds answers in Google's understanding of
the web: its search index, the **Knowledge Graph** (entities and their relationships), and
Google-owned surfaces — notably **YouTube**. In practice it benefits from the same forces as
Google AI Overviews, plus a strong pull toward **recognized entities** it can ground facts
on and toward **video** where relevant. Because of that overlap, run this with
**google-ai-overviews-optimization** when a brand cares about Google's AI answers broadly —
this skill adds the Gemini-specific emphases on entity grounding and Google surfaces.

## When to use this skill

- A brand cares specifically about Gemini visibility.
- Diagnosing why competitors appear in Gemini answers and the brand is not.
- Prioritizing AEO for a Google-ecosystem audience.

## Before you start

Read `aeo-foundation.md` for the prompt set, entity facts, and Google-search standing. If it
is missing, point to the **aeo-foundation** skill.

## Where Gemini puts weight

- **Google entity presence.** A strong **Knowledge Graph** entity with consistent facts lets
  Gemini ground and name the brand confidently — prioritize **entity-optimization** (Wikidata,
  Wikipedia where notable, Organization schema, NAP consistency).
- **Organic and structured content.** Like Overviews, it favors well-ranking, well-structured
  pages — see **google-ai-overviews-optimization** and **answer-engineering**.
- **Google surfaces, including YouTube.** Video on YouTube with strong titles, descriptions,
  chapters, and transcripts is a Google-owned signal Gemini can draw on — see **multimodal-aeo**.
- **E-E-A-T and trust.** Named authors, accuracy, and sourcing — see **author-authority** and
  **claim-accuracy**.
- **Freshness** for time-sensitive prompts.

## Quick wins

- Establish/complete the **Knowledge Graph entity**: referenced Wikidata item, Organization
  schema with `sameAs`, consistent core facts everywhere.
- Apply the **Google AI Overviews** structure/E-E-A-T playbook to target pages.
- Add or optimize **YouTube** content (titles, descriptions, chapters, uploaded transcripts)
  for prompts where video is a natural answer.
- Verify entity-fact consistency with the `entity-optimization` checker.

## Workflow

1. **Baseline in Gemini** for the prompt set: citations, sources, who wins.
2. **Strengthen the Google entity** — Knowledge Graph footprint, Organization schema,
   consistent facts.
3. **Apply the Google AIO playbook** — organic relevance plus structured, extractable content.
4. **Build relevant YouTube/video presence** where the audience and prompts support it.
5. **Signal E-E-A-T** on target content.
6. **Re-test and iterate** (cadence: see **ai-visibility-tracking**).

## Output format

- A **Gemini baseline** and gap list.
- Prioritized moves weighted to **entity/Knowledge Graph**, **Google-ecosystem surfaces
  (incl. YouTube)**, and **structured content**.
- Target entities, pages, and surfaces to act on.
- `(assumption)` tags where behavior was inferred rather than tested.

## Common pitfalls

- Weak Knowledge Graph entity, so Gemini is unsure who the brand is.
- Ignoring YouTube as a Google-owned source Gemini can pull from.
- Treating Gemini wholly separately from Google AI Overviews — they overlap heavily.
- Thin E-E-A-T on demanding (YMYL) topics.

## Related Skills

- **entity-optimization** — the Knowledge Graph presence Gemini leans on.
- **google-ai-overviews-optimization** — the overlapping Google playbook.
- **multimodal-aeo** — the YouTube/video signal Gemini can draw on.
- **answer-engineering** / **structured-data** — structure and markup Google favors.
- **author-authority** — the E-E-A-T signals it rewards.
