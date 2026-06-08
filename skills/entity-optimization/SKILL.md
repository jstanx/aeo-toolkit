---
name: entity-optimization
description: >-
  Make a brand a recognized entity that answer engines can confidently name — a clear
  entity home, Organization schema with sameAs, Wikidata and (where it qualifies)
  Wikipedia presence, consistent facts across the web, and disambiguation. Works for any
  business, B2B or B2C, product or service. Use when the request is to get AI to recognize
  a brand, build an entity or knowledge-graph presence, fix how AI describes or confuses a
  brand, add Organization schema or sameAs, or pursue Wikidata/Wikipedia. Pairs with
  structured-data and author-authority.
metadata:
  version: 0.1.0
---

# Entity Optimization

This skill makes a brand a **recognized entity** — a distinct, verified thing engines can
name with confidence. You can rank for a keyword and still be invisible in AI answers if
the model does not recognize you as an entity in its knowledge graph. Entity optimization
fixes that by giving the web a single, consistent, well-connected definition of who the
brand is. It works for any business, B2B or B2C.

See [references/entity-playbook.md](references/entity-playbook.md) for the Wikidata,
Wikipedia, and `sameAs` details.

## When to use this skill

- A brand is absent from AI answers despite decent search rankings.
- AI describes the brand inaccurately, vaguely, or confuses it with another.
- Establishing knowledge-graph presence (Organization schema, Wikidata, Wikipedia).
- Standardizing brand facts across the web.

## Before you start

Read `aeo-foundation.md` for the brand-entity facts: official name, category, founding,
HQ, key people, and existing profiles. If it is missing, point to the **aeo-foundation**
skill.

## The levers

1. **An authoritative entity home.** Usually the About page — the canonical definition of
   the brand: what it is, its category, founding, location, key people, and what makes it
   distinct, in consistent language. Crawlable and linked from the homepage.
2. **Organization schema with `sameAs`.** Mark up the entity (name, url, logo, description,
   foundingDate) and link every authoritative profile via `sameAs` so engines collapse the
   scattered mentions into one entity. Recipes in the
   [schema cookbook](../../references/schema-cookbook.md).
3. **Knowledge-base presence.** A complete **Wikidata** item (low barrier, machine-readable,
   feeds many systems) and, where the brand genuinely qualifies on notability, a
   **Wikipedia** article (high authority). See the playbook.
4. **Fact consistency (NAP and core facts).** The same name, founding date, HQ,
   leadership, and category everywhere — site, schema, profiles, directories, review
   platforms, press. Engines apply a "majority rule"; contradictions weaken recognition.
5. **Disambiguation.** If the name is generic, always pair it with its category and
   identifiers ("Acme (analytics software)") so the brand is not merged with namesakes.

## Workflow

1. **Audit the entity.** Search the brand across engines and the web; note how it is
   described, what is inconsistent or wrong, and which knowledge bases list it.
2. **Build the entity home.** Write or tighten the About page as the canonical definition.
3. **Implement schema.** Add Organization schema with a complete `sameAs` set; link key
   people with Person schema (see **author-authority**).
4. **Establish knowledge bases.** Create/complete Wikidata; pursue Wikipedia only with
   genuine third-party notability (see the playbook).
5. **Reconcile facts.** Standardize core facts everywhere they appear; correct outdated or
   conflicting listings.
6. **Disambiguate.** Apply the full name-plus-category form in key places.
7. **Monitor.** Recheck periodically; entity facts drift as the company changes.

## Output format

- An **entity audit**: how the brand is currently recognized and where facts conflict.
- The **entity home** content and **Organization/`sameAs`** markup.
- A **knowledge-base plan** (Wikidata now; Wikipedia if/when notable).
- A **fact-reconciliation list** of profiles/directories to correct.
- `(assumption)` tags on any unverified facts.

## Common pitfalls

- Inconsistent core facts across the web — the top reason engines stay uncertain.
- Chasing a Wikipedia article without the independent coverage notability requires.
- Skipping Wikidata, which is lower-friction and directly machine-readable.
- Generic brand name left undisambiguated, so AI conflates it with others.

## Tool

Check whether canonical entity facts appear consistently across profiles (live URLs or local files):

```bash
python scripts/check_entity_consistency.py --sample
python scripts/check_entity_consistency.py --input entity.json
```

> Optional. The script only automates this step; it needs `python3` (standard library only, no install). No Python? Just follow the steps above manually.

## Related Skills

- **structured-data** — the Organization/Person markup that anchors the entity.
- **author-authority** — people-entities (founders, authors) connected to the brand.
- **digital-pr** — the third-party coverage that builds notability and corroboration.
- **aeo-foundation** — the source of the canonical entity facts.
