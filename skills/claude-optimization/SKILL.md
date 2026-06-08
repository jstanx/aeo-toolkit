---
name: claude-optimization
description: >-
  Optimize specifically for Claude — the assistant that answers from trained knowledge and
  live web search, and that cites conservatively, favoring accurate, well-sourced,
  authoritative content, original data, and clear author credentials. Works for any
  business, B2B or B2C, product or service. Use when the request is to get cited or
  recommended by Claude, improve Claude visibility, or understand why competitors win
  there. Applies cross-engine fundamentals through a Claude lens; pairs with
  author-authority, evidence-and-citations, and entity-optimization.
metadata:
  version: 0.1.0
---

# Claude Optimization

This skill tunes an AEO program for **Claude**. The cross-engine fundamentals apply; this
skill says where to add weight. Behavior evolves — treat these as current emphases and confirm
by testing. It works for any business, B2B or B2C.

## How Claude builds an answer

Claude answers from **trained knowledge** (a snapshot with a cutoff) and, when web search is
enabled, by **retrieving and citing live sources**. Relative to other engines it cites
**conservatively and selectively** — it is cautious about asserting things it can't support.
That shapes the strategy in two ways:

- **From memory:** Claude can only describe a brand it has formed a clear, consistent picture
  of — which comes from being a **recognized entity** with accurate, corroborated information
  across the web.
- **When searching:** it favors **accurate, well-sourced, technically precise** pages,
  **original data**, and **clearly credentialed authors**, and it shies away from
  overstated or thin content.

Net: Claude rewards substance and accuracy over recency and community chatter. The way to win
is to be genuinely correct, well-sourced, and recognizable — not loud or merely fresh.

## When to use this skill

- A brand cares specifically about how Claude describes and cites it.
- Diagnosing why competitors are named by Claude and the brand is not.
- Prioritizing AEO for a Claude-heavy audience.

## Before you start

Read `aeo-foundation.md` for the prompt set, competitors, and entity facts, plus a Claude
baseline if available. If it is missing, point to the **aeo-foundation** skill.

## Where Claude puts weight

- **Accuracy and trustworthiness.** Precise, verifiable, well-sourced content is favored;
  overclaiming or thin content is skipped. Lean on **evidence-and-citations** and
  **claim-accuracy**.
- **Author authority and credentials.** Named, credentialed experts and demonstrated
  expertise carry real weight — prioritize **author-authority**.
- **Original data and depth.** Distinctive first-party data and genuine information gain are
  strongly rewarded; Claude handles substantive, technical material well.
- **Entity recognition.** A clear, consistent entity helps Claude describe the brand
  confidently from trained knowledge — prioritize **entity-optimization**.
- **Retrievability for web search.** When it searches, it needs reachable, readable,
  well-structured pages — confirm **ai-crawler-access** (ClaudeBot, Claude-SearchBot,
  Claude-User), **ai-retrievability**, and **answer-engineering**.
- **Less weight on community/recency.** Reddit-style signals and aggressive freshness matter
  less here than on Perplexity — though content still must not be outdated to stay accurate.

## Quick wins

- **Remove overclaims** and unsupported superlatives; back every strong claim with a source
  or a number (run a pass with `claim-accuracy` + `evidence-and-citations`).
- **Surface original data** the brand owns as quotable, well-sourced passages.
- Add **credentialed author bylines** and author pages.
- Establish/complete the **entity** so Claude knows the brand from memory.
- Confirm **Claude's crawlers aren't blocked** (run the `ai-crawler-access` checker).

## Workflow

1. **Baseline in Claude** (with and without web search where possible): how it describes the
   brand, what it cites, who wins, and any inaccuracies.
2. **Tighten accuracy and sourcing** on target content — specific, verifiable, well-cited
   claims; remove overstatement.
3. **Strengthen author authority** — credentialed bylines and demonstrated expertise.
4. **Surface original data and depth** where the brand has it.
5. **Reinforce the entity** so Claude knows the brand from training.
6. **Confirm retrievability** for Claude's web search.
7. **Re-test and iterate**, correcting any misrepresentations (cadence: see
   **ai-visibility-tracking**).

## Output format

- A **Claude baseline** (description + citations) and gap list.
- Prioritized moves weighted to **accuracy/sourcing**, **author authority**, **original
  data**, and **entity strength**.
- Target content, authors, and entity facts to act on.
- `(assumption)` tags where behavior was inferred rather than tested.

## Common pitfalls

- Overclaiming or thin content — exactly what a conservative citer skips.
- Anonymous content with no credentialed authority.
- A weak or inconsistent entity, so Claude is unsure who the brand is.
- Forgetting retrievability for Claude's web search.
- Assuming Claude weights Reddit/freshness like Perplexity — it leans on accuracy and authority.

## Related Skills

- **evidence-and-citations** / **claim-accuracy** — the accuracy and sourcing Claude rewards.
- **author-authority** — the credentialed expertise it favors.
- **entity-optimization** — recognition from trained knowledge.
- **answer-engineering** — extractable structure for when it searches.
- **ai-retrievability** / **ai-crawler-access** — reachability for Claude's web search.
