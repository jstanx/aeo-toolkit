---
name: prompt-research
description: >-
  Find and prioritize the conversational prompts and questions buyers actually ask AI
  assistants about a category, then build the tracked prompt set the rest of an AEO
  program optimizes and measures against. Works for any business, B2B or B2C, product or
  service. Use when the request is to research AI prompts, figure out what people ask
  ChatGPT or Perplexity about a topic, build a prompt set, map AI search intent, or
  decide which queries to target for AI visibility. Pairs with aeo-foundation (stores the
  set) and competitor-ai-analysis (scores it).
metadata:
  version: 0.1.0
---

# Prompt Research

This skill discovers the **real questions buyers ask AI** in a category and turns them
into a prioritized, tracked prompt set. It is the AEO counterpart to keyword research, but
the unit is a natural-language question, not a keyword, and the search is a conversation,
not a single lookup. The output drives everything downstream: which answers to engineer,
which gaps to close, and what to measure. It works for any business, B2B or B2C.

## When to use this skill

- Building the initial prompt set for a brand or category.
- Expanding or refreshing an existing set as the market shifts.
- Mapping prompts to funnel intent before planning content.
- Deciding which queries are worth optimizing and tracking.

## Before you start

Read `aeo-foundation.md` for the brand, audience, and any prompts already captured. If it
is missing, point to the **aeo-foundation** skill. The set you produce should be written
back into the foundation file.

## How AI questions differ from keywords

- People ask **full questions**, often with context and constraints ("best X for a
  10-person team on a budget"), not two-word keywords.
- Search is a **conversation** — an initial question plus follow-ups — so map sequences,
  not just single queries.
- The highest-value prompts carry **buyer intent and constraints** that trigger a
  recommendation, which is where AI visibility converts.

## Workflow

1. **Build persona constraints.** For each priority persona from the foundation, note
   their context, experience level, risk points, budget, and the language they use. These
   constraints shape the questions they ask and the answers that satisfy them.
2. **Mine real questions.** Gather actual phrasing from where demand already shows:
   customer and sales/support conversations, reviews, community threads, the "related
   questions" and follow-ups engines suggest, and your own testing of the assistants.
   Real questions beat brainstormed ones.
3. **Generate across intent.** For each persona, draft prompts spanning awareness
   (problem space), consideration (approaches, "best X", comparisons, alternatives), and
   decision (brand-specific, "X vs Y", fit, pricing).
4. **Add the conversation layer.** For key prompts, note the natural follow-ups; those are
   additional surfaces to win.
5. **Prioritize ruthlessly.** Score by buyer intent and business fit. A focused set of
   high-value prompts outperforms a sprawling list of low-intent ones — concentrate effort
   where a recommendation changes a decision.
6. **Baseline.** Run the prioritized prompts across the major engines and record current
   presence (cited / mentioned / absent), who wins, and sentiment. This is the starting
   line for measurement.
7. **Record.** Write the set into the foundation file using
   [templates/prompt-set.md](templates/prompt-set.md).

## Prioritization

Rank each candidate prompt on:

- **Intent** — how close to a decision (decision > consideration > awareness for
  conversion; keep some awareness prompts for reach).
- **Fit** — how well the brand can credibly be the answer.
- **Winnability** — whether competitors own it immovably or there is room.
- **Volume/representativeness** — how many real buyers ask something like it.

Keep the working set tight; depth of optimization on the right prompts beats breadth.

## Output format

- The **prioritized prompt set**, grouped by persona and intent, each tagged with the
  action it influences.
- A **baseline** note per top prompt: current brand presence and who out-cites you.
- The set written back into `aeo-foundation.md`.
- `(assumption)` tags on any prompts inferred rather than observed.

## Common pitfalls

- Tracking 100+ vanity prompts instead of mastering the 15–25 that matter.
- Writing keyword stubs instead of how people actually talk to AI.
- All awareness prompts, no decision-stage prompts where recommendations convert.
- Never baselining, so progress can't be measured.

## Related Skills

- **aeo-foundation** — stores the prompt set and personas.
- **competitor-ai-analysis** — scores share of voice across this set.
- **ai-visibility-audit** — diagnoses why you do or don't win these prompts.
- **answer-engineering** / **comparison-content** — create answers to these questions.
- **ai-visibility-tracking** — monitors the set over time.
