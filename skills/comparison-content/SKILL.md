---
name: comparison-content
description: >-
  Create the comparison content answer engines lean on for buying decisions — "best X for
  Y" lists, alternatives pages, and head-to-head "X vs Y" comparisons, built to be cited
  and to get the brand fairly represented. Works for any business, B2B or B2C, product or
  service. Use when the request is to write a comparison or alternatives or "best of"
  page, get into AI recommendations for a category, win versus-queries, or earn citations
  on decision-stage prompts. Pairs with digital-pr (third-party lists) and
  community-and-reviews.
metadata:
  version: 0.1.0
---

# Comparison Content

This skill creates the **comparison content that decides commercial AI answers**: "best X
for Y" roundups, "alternatives to" pages, and "X vs Y" head-to-heads. When a buyer asks an
assistant to recommend or compare options, engines pull heavily from this format — listicles
and comparison pages are among the most-cited content types for decision-stage prompts. The
goal is twofold: create genuinely useful comparisons you can be cited for, and ensure the
brand is fairly represented in others'. It works for any business, B2B or B2C.

## When to use this skill

- Writing a "best X for [use case]" or "alternatives to [competitor]" page.
- Creating head-to-head "X vs Y" comparisons.
- Targeting decision-stage prompts where engines recommend options.
- Improving how the brand shows up in third-party comparisons.

## Before you start

Read `aeo-foundation.md` for the category, the competitor/alternative set, the
differentiators, and the decision-stage prompts. If it is missing, point to the
**aeo-foundation** skill.

## Two plays

**1. Own comparisons (your site).** Publish genuinely useful, honest comparisons. Engines
(and Google's 2026-era quality stance) deprioritize transparently self-serving "we win
everything" pages, so credibility is the strategy:

- Use real criteria buyers care about; present them in a scannable **table**.
- Be **fair** about where alternatives are stronger; balanced comparisons get trusted and
  cited, biased ones get discounted.
- Make each option's row/section **self-contained** and answer-first (see
  **answer-engineering**), so an engine can lift a single comparison cleanly.
- Keep it **current** — comparison facts (pricing, features) date fast (see
  **content-freshness**).

**2. Earn placement (third-party).** Most decision-stage citations come from *independent*
comparisons — analyst pieces, review-site roundups, "alternatives" articles, and community
threads. Getting the brand accurately included there is high-leverage:

- Identify the third-party lists engines already cite for your prompts (from
  **competitor-ai-analysis**).
- Pursue inclusion and accuracy through **digital-pr** and **community-and-reviews**.
- Supply reviewers and publishers with correct, current facts so the brand is represented
  well.

## Workflow

1. **Target the prompts.** Pick the decision-stage prompts ("best X for Y", "X vs Y",
   "alternatives to Z") worth winning.
2. **Choose the play.** Own page, earned placement, or both.
3. **Build the criteria.** Define the comparison dimensions buyers actually weigh; gather
   accurate data for every option.
4. **Draft fair, structured comparisons.** Tables for the at-a-glance view; self-contained,
   answer-first sections per option; honest trade-offs.
5. **Add evidence.** Specific specs, pricing, and sourced claims (see
   **evidence-and-citations**).
6. **Pursue third-party inclusion** for the independent lists engines cite.
7. **Maintain.** Schedule refreshes; comparison content decays quickly.

## Output format

- The comparison page(s): intro answer block, criteria table, per-option sections, honest
  verdict/fit guidance.
- A **target list** of third-party comparisons to earn placement in, with the current gap.
- Fact sheets to supply reviewers/publishers for accurate representation.
- `(assumption)` tags on any competitor facts to verify.

## Common pitfalls

- Transparently biased "we win every row" pages — distrusted and discounted.
- Comparisons with no table or structure, so nothing extracts cleanly.
- Stale pricing/feature facts that make the page wrong.
- Ignoring the third-party lists that actually drive decision-stage citations.

## Related Skills

- **competitor-ai-analysis** — finds the comparisons and "vs" prompts to target.
- **answer-engineering** / **evidence-and-citations** — structure and substance.
- **digital-pr** — earns placement in independent comparison content.
- **community-and-reviews** — review-platform and community comparison presence.
