---
name: content-freshness
description: >-
  Keep content fresh in the way answer engines reward — a substantive update cadence,
  real refreshes (not cosmetic date changes), and a system for spotting decay. Works for
  any business, B2B or B2C, product or service. Use when the request is to update or
  refresh content for AI, set a content-freshness or update cadence, improve recency
  signals, decide what to re-publish, or fix stale pages that lost AI citations. Pairs
  with answer-engineering and evidence-and-citations.
metadata:
  version: 0.1.0
---

# Content Freshness

This skill keeps content **current enough to keep getting cited**. Recency is a strong
signal in AI answers — recently, substantively updated pages are cited markedly more, and
some engines lean heavily on freshness because they retrieve in real time. But the signal
rewards *real* updates: engines compare versions, so changing a date without changing the
substance does nothing. This skill builds a cadence and a refresh method that earn the
recency advantage honestly. It works for any business, B2B or B2C.

## When to use this skill

- Setting an update cadence for a content library.
- Deciding which existing pages to refresh and how.
- Recovering pages that used to be cited and went quiet.
- Building freshness into an editorial process.

## Before you start

Read `aeo-foundation.md` for the priority topics and prompt set — freshness effort should
concentrate on the content tied to high-value prompts. If it is missing, point to the
**aeo-foundation** skill.

## Principles

- **Substantive over cosmetic.** A refresh must change real content — new data, new
  examples, revised guidance, added sections — not just the visible date. Engines detect
  the difference.
- **Match cadence to volatility.** Fast-moving topics (pricing, news, anything dated)
  need frequent updates; evergreen guides need less; reference/definition pages least.
- **Prioritize by value.** Refresh the pages that target high-value prompts and already
  have traction before touching the long tail.
- **Recency is a tiebreaker, not a substitute.** Freshness lifts content that is also
  well-structured, evidenced, and authoritative — it does not rescue thin pages.

## Suggested cadence (adapt per topic)

| Content type | Typical refresh |
|---|---|
| Time-sensitive (pricing, stats, news, "in 2026") | Frequent — monthly to quarterly |
| Commercial / high-value guides | Quarterly to twice a year |
| Evergreen pillars | Twice a year |
| Reference / definitions | Annually, or when facts change |

## Workflow

1. **Inventory and flag.** List priority pages with their last substantive update and
   target prompts. Flag anything stale relative to its type, and anything that lost AI
   visibility.
2. **Diagnose decay.** For pages that slipped, check what changed: outdated facts, a year
   in the title, superseded guidance, or a competitor publishing fresher work.
3. **Refresh substantively.** Update statistics and examples, add new sections or
   questions from the prompt set, correct anything outdated, and re-verify citations. Pull
   in **evidence-and-citations** for new data and **answer-engineering** for any
   restructuring.
4. **Update the date honestly.** Set `dateModified` (and any visible "updated" line) to
   reflect the real change — see the schema cookbook.
5. **Signal the update.** Ensure the page is re-crawlable (sitemap, internal links) so
   engines pick up the new version.
6. **Schedule the next pass.** Assign each page a cadence so freshness is systematic, not
   reactive.

## Output format

- A **refresh plan**: which pages, what to change, target cadence, and owner.
- For each refreshed page, a note on the **substantive changes** made.
- Flags for pages that should be **consolidated or retired** rather than refreshed.
- `(assumption)` tags where update history was unknown.

## Common pitfalls

- Cosmetic date bumps with no real change — detected and ineffective.
- Refreshing low-value pages while flagship content goes stale.
- Treating freshness as a fix for thin or unstructured content.
- No schedule, so freshness happens only when someone remembers.

## Related Skills

- **answer-engineering** — restructure sections during a refresh.
- **evidence-and-citations** — swap in current data and live sources.
- **ai-visibility-tracking** — surfaces pages losing citations, triggering refreshes.
- **structured-data** — keep `dateModified` accurate and honest.
