# Entity Playbook: Wikidata, Wikipedia, and sameAs

Deep reference for `entity-optimization`. The mechanics of making a brand a recognized
entity.

## Why entities matter for AI

Answer engines draw on knowledge graphs (Google's Knowledge Graph, Wikidata, and learned
internal representations) to know *who* a thing is. A recognized entity gets named
confidently and consistently; an unrecognized one gets vague hedges or gets skipped, even
with good content. Entity work is often the unlock for brands that "rank but aren't cited."

## sameAs: connecting the entity

`sameAs` tells engines that a set of URLs all refer to the same entity, collapsing scattered
mentions into one recognized thing. Include the authoritative, stable profiles:

```json
"sameAs": [
  "https://en.wikipedia.org/wiki/Acme_Analytics",
  "https://www.wikidata.org/wiki/Q000000",
  "https://www.linkedin.com/company/acme-analytics",
  "https://www.crunchbase.com/organization/acme-analytics",
  "https://github.com/acme-analytics"
]
```

Only list profiles that genuinely belong to the brand and are kept current. Put `sameAs`
on the Organization schema on the homepage/about page.

## Wikidata (do this first)

Wikidata is the lower-friction, higher-leverage starting point:

- **No notability bar** like Wikipedia — most legitimate organizations can have an item.
- **Machine-readable and openly queried** — many AI and search systems read it directly.
- **Feeds Wikipedia infoboxes** and broader knowledge graphs.

Create a complete, well-referenced item:
- Core statements: instance of (e.g. business/organization), industry, inception,
  headquarters location, official website, founders/key people.
- **Reference every statement** to a reliable source — unreferenced claims are weak and may
  be removed.
- Link out with identifiers (official site, LinkedIn, Crunchbase) so it reconciles with
  other databases.
- Keep it accurate and neutral; Wikidata is collaboratively edited.

## Wikipedia (only when genuinely notable)

Wikipedia is the highest-authority entity source and heavily favored by some engines — but
it has a real **notability** requirement and strict rules:

- Notability is established by **significant coverage in independent, reliable secondary
  sources** — not by the brand itself.
- **Do not** create a promotional autobiography; conflict-of-interest and self-promotion
  edits get reverted, and can backfire.
- The right sequence: earn genuine third-party coverage first (see **digital-pr**), then a
  neutral, well-sourced article becomes possible and defensible.
- If a page exists, keep its facts accurate via proper channels (talk pages, sourced
  edits), respecting Wikipedia's guidelines.

## Fact consistency (the quiet multiplier)

Engines build confidence from agreement across sources. Make these identical everywhere
(site, schema, Wikidata, LinkedIn, Crunchbase, directories, review platforms, press):

- Official name (and its disambiguated form)
- Category / what the brand does (consistent wording)
- Founding date, headquarters
- Key people and titles

A single contradicted fact (two founding dates, two HQs) injects doubt. Audit and reconcile
periodically.

## Disambiguation

For generic or shared names:
- Always present name **plus category**: "Bright (marketing agency)".
- Add contextual identifiers (location, industry, founding year) near the name.
- Use the description field in schema and Wikidata to separate the brand from namesakes.
- Build strong, repeated associations with the category so the entity is unambiguous.

## Quick checklist
- [ ] Crawlable entity home (About page) with canonical facts.
- [ ] Organization schema with complete, accurate `sameAs`.
- [ ] Complete, referenced Wikidata item.
- [ ] Wikipedia only with real independent notability; neutral and sourced.
- [ ] Core facts identical across all profiles and directories.
- [ ] Generic names disambiguated with category + identifiers.
