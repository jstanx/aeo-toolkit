---
name: llms-txt
description: >-
  Implement the /llms.txt file that summarizes a site's key content for LLMs — with an
  honest read on its current, limited impact. Works for any business, B2B or B2C, product
  or service. Use when the request is to add or create an llms.txt file, set up
  llms-full.txt, decide whether llms.txt is worth doing, or understand whether AI engines
  use it. Pairs with ai-retrievability and structured-data, which matter more today.
metadata:
  version: 0.1.0
---

# llms.txt

This skill implements `/llms.txt` — a proposed plain-Markdown file that points LLMs to a
site's most important content — and, just as importantly, **sets honest expectations about
it**. As of now, adoption is early and major answer engines largely do not parse it, so it
is a low-effort, low-impact best practice rather than a citation lever. The work that
actually moves AI visibility is clean rendering, structure, schema, and authority — do
those first. It works for any business, B2B or B2C.

## When to use this skill

- A user asks to add `llms.txt` / `llms-full.txt`.
- Deciding whether `llms.txt` is worth the effort (it is cheap, so usually a mild yes).
- Setting realistic expectations about what it does today.

## The honest status

- **Engines largely ignore it today.** Independent testing shows the major crawlers usually
  fetch HTML directly and do not rely on `llms.txt`; sites adding it generally see no
  measurable citation change.
- **Adoption is early.** A small minority of sites have it; there is no formal standard that
  engines have committed to honoring.
- **Why do it anyway:** it is a ~30-minute task, it is a clear opt-in signal, and it is
  useful for documentation-heavy sites and for stating brand/entity facts plainly. Treat it
  as cheap insurance, not a growth tactic.
- **Do not let it crowd out the real work** — rendering, structure, schema, freshness, and
  authority are where the gains are.

## What it is

- A Markdown file at the site root: `/llms.txt`.
- A short brand/site description, then curated links to the most important pages
  (docs, key products/services, about), each with a one-line note.
- Optionally `/llms-full.txt` with fuller content for sites that want it.

## Format

```markdown
# Brand Name

> One to three sentence description of what the site/company is and does.

## Key pages
- [Product](https://example.com/product) - what it is
- [Docs](https://example.com/docs) - how to use it
- [About](https://example.com/about) - company facts and contact

## Contact
- Email: hello@example.com
```

Serve it as UTF-8 plain text/Markdown at the root.

## Workflow

1. **Set expectations.** Tell the user up front this is low-impact today and prioritize the
   higher-leverage skills.
2. **Draft the file.** Brand description plus a curated set of the most important links with
   one-line notes; keep it accurate and consistent with the entity facts.
3. **Publish at the root** as `/llms.txt` (and `/llms-full.txt` if useful).
4. **Keep it current** alongside the entity/foundation facts; a stale file is worse than
   none.
5. **Re-evaluate periodically.** If engines begin honoring it more, revisit its priority.

## Output format

- The **`llms.txt` content**, ready to publish.
- A one-line **expectation note** for the user (low impact today).
- A pointer to the higher-leverage skills to do first.

## Common pitfalls

- Expecting a citation boost — there is little evidence of one today.
- Prioritizing it over rendering, schema, and authority work.
- Letting it drift out of sync with the brand's real facts and key pages.

## Tool

Generate a valid `llms.txt` from a small config:

```bash
python scripts/generate_llms_txt.py --sample            # example config
python scripts/generate_llms_txt.py --input site.json   # write the file
```

> Optional. The script only automates this step; it needs `python3` (standard library only, no install). No Python? Just follow the steps above manually.

## Related Skills

- **ai-retrievability** — server-rendered, readable content (matters far more).
- **structured-data** — machine-readable signals engines actually use.
- **entity-optimization** — keep the brand facts in `llms.txt` consistent with the entity.
