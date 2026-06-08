---
name: structured-data
description: >-
  Add the JSON-LD structured data that helps answer engines parse content and recognize
  entities — Organization, Article, Person, FAQPage, Product, and related schema, applied
  and validated correctly. Works for any business, B2B or B2C, product or service. Use
  when the request is to add schema or structured data for AI, implement JSON-LD, mark up
  FAQs or articles or an organization, improve machine-readability for AI search, or
  validate schema. Reference the shared schema cookbook; pairs with answer-engineering and
  entity-optimization.
metadata:
  version: 0.1.0
---

# Structured Data

This skill adds the **machine-readable markup** that helps answer engines parse a page,
understand its entities, and extract answers with confidence. Structured data does not
force a citation, but it consistently improves how reliably engines interpret content and
recognize the brand — and it is one of the higher-leverage technical moves. It works for
any business, B2B or B2C.

Ready-to-adapt JSON-LD recipes live in the shared
[schema cookbook](../../references/schema-cookbook.md); this skill is the strategy,
workflow, and validation around them.

## When to use this skill

- Adding schema to content meant to be cited or to define the brand entity.
- Marking up FAQs, articles, authors, products, or the organization.
- Auditing and validating existing structured data.
- Reinforcing answer-engineering and entity work with markup.

## Before you start

Read `aeo-foundation.md` for the entity facts (for Organization schema) and the content
types in play. If it is missing, point to the **aeo-foundation** skill.

## Principles

- **JSON-LD**, in a script tag — the format engines handle most reliably (not microdata or
  RDFa).
- **Mark up what is true and visible.** Schema describes on-page content; it does not
  replace it, and marking up content that is not on the page is a quality risk.
- **Connect the entities.** Article references its author (Person); Person is affiliated
  with the Organization. These links help engines verify credibility and build the entity
  graph.
- **Validate before shipping.** Always run markup through a schema validator and a
  rich-results test.

## Priority types for AEO

1. **Organization** — anchors the brand entity, with `sameAs` (pairs with
   **entity-optimization**).
2. **Article / BlogPosting** — content type, author, publish/modified dates.
3. **Person** — author identity and credentials (pairs with **author-authority**).
4. **FAQPage** — Q&A pairs engines can lift directly (pairs with **answer-engineering**).
5. **Product**, **Review / AggregateRating**, **HowTo**, **BreadcrumbList** — as relevant
   to the page.

## Workflow

1. **Audit existing markup.** Inventory which pages have schema, which types, and what is
   missing or invalid.
2. **Map types to pages.** Assign the right schema per template: Organization on the
   home/about page; Article + Person on content; FAQPage where genuine Q&A appears;
   Product/Review on commercial pages.
3. **Implement JSON-LD** from the cookbook, filling real values and connecting
   author/publisher entities.
4. **Keep dates honest.** `datePublished`/`dateModified` should reflect real updates (ties
   to **content-freshness**).
5. **Validate.** Run every page's markup through a validator and rich-results test; fix
   errors and warnings.
6. **Cover broadly.** Aim for consistent schema across the relevant page templates, not a
   one-off.

## Output format

- A **schema audit**: coverage and gaps by page type.
- The **JSON-LD to add** per template, with entity connections in place.
- A **validation note** confirming each block passes.
- `(assumption)` tags on any entity facts to confirm.

## Common pitfalls

- Marking up content that is not actually on the page — a quality and trust risk.
- Orphan schema: Article with no linked author or publisher.
- Inaccurate `dateModified` used to fake freshness.
- Shipping invalid JSON-LD that silently fails — always validate.
- Treating schema as a silver bullet; it aids interpretation, it does not replace good,
  corroborated content.

## Tool

Generate and lightly validate JSON-LD from a small config (Organization, Article, FAQPage, Person):

```bash
python scripts/generate_schema.py --sample organization   # example input
python scripts/generate_schema.py --input org.json         # emit a <script> block + warnings
```

Only mark up content that is visible on the page, then validate with a rich-results test.

> Optional. The script only automates this step; it needs `python3` (standard library only, no install). No Python? Just follow the steps above manually.

## Related Skills

- **entity-optimization** — Organization/`sameAs` markup that anchors the brand entity.
- **author-authority** — Person schema for credentialed authors.
- **answer-engineering** — FAQPage and structure that schema reinforces.
- **ai-retrievability** — ensures the marked-up content is actually crawlable.
