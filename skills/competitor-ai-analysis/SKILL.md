---
name: competitor-ai-analysis
description: >-
  Analyze how competitors win in AI answers and find the gaps to close — measure share of
  voice across the prompt set, see who gets cited and why, and reverse-engineer the
  sources and signals behind their citations. Works for any business, B2B or B2C, product
  or service. Use when the request is to analyze competitor AI visibility, find out why
  rivals get recommended by ChatGPT or Perplexity, measure share of voice, benchmark AEO
  against competitors, or find citation gaps. Pairs with ai-visibility-audit and
  prompt-research.
metadata:
  version: 0.1.0
---

# Competitor AI Analysis

This skill turns "competitors keep getting recommended and we don't" into a concrete plan.
It measures **share of voice** across the prompt set, identifies **who wins which prompts**,
and reverse-engineers the **sources and signals** behind their citations so you can target
the same ground. It works for any business, B2B or B2C.

## When to use this skill

- Benchmarking AI visibility against named competitors.
- Finding the prompts where rivals dominate and you are absent.
- Understanding *why* a competitor gets cited (which sources, what content, what
  authority).
- Prioritizing where to compete for citations.

## Before you start

Read `aeo-foundation.md` for the competitor set and prompt set. If competitors or prompts
are thin, run **prompt-research** and revisit the foundation first.

## Workflow

1. **Define the field.** Confirm the prompt set and the competitors (direct, indirect, and
   the surprising names engines actually recommend — often not who the brand expects).
2. **Measure share of voice.** Run each prompt across the major engines and tally, per
   competitor: citation rate (linked), mention rate (named), and average position in the
   answer. Compute each brand's share of the total.
3. **Map who wins what.** Identify the prompts each competitor owns and the prompts no one
   owns (open territory — often the best opportunities).
4. **Reverse-engineer the wins.** For prompts a competitor dominates, look at *what is
   being cited*: their own page, a third-party listicle, a review platform, a Reddit
   thread, a news/analyst piece. Note the pattern — is it content quality, structure,
   freshness, entity strength, or off-site corroboration?
5. **Find the gaps.** Contrast their winning signals with the brand's current state
   (from the audit). Each gap becomes a targeted action mapped to a skill.
6. **Prioritize.** Rank opportunities by winnability and business value: open prompts and
   weakly-held prompts first; entrenched, authority-heavy prompts later.

## What to look for behind a competitor's citations

- **Source type** — are they cited via their own content, or via third-party/earned media
  and communities? (The latter signals an authority/PR gap to close.)
- **Content shape** — answer-first structure, comparisons, original data?
- **Entity strength** — Wikipedia/Wikidata presence, consistent facts?
- **Freshness** — recently updated vs. stale?
- **Reviews & community** — strong G2/Capterra/Trustpilot or Reddit presence?

## Output format

- **Share-of-voice table** — citation/mention rate and share per competitor across the set.
- **Win map** — which prompts each competitor owns, and the open prompts.
- **Why-they-win notes** — the dominant source/signal pattern per key prompt.
- **Gap-to-action list** — each gap mapped to the owning skill, prioritized by
  winnability and value.
- `(assumption)` tags where signals were inferred.

## Common pitfalls

- Benchmarking only the competitors you assume matter, missing who engines actually name.
- Counting mentions without looking at *why* — the source pattern is the insight.
- Chasing entrenched prompts while ignoring open territory.
- One-time analysis; competitive position shifts — re-run on a cadence.

## Related Skills

- **prompt-research** — defines the prompt set this is scored against.
- **ai-visibility-audit** — the brand-side readiness picture this contrasts with.
- **digital-pr** / **comparison-content** / **community-and-reviews** — close off-site gaps.
- **ai-visibility-tracking** — monitors share of voice over time.
