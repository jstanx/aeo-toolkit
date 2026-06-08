---
name: aeo-foundation
description: >-
  Build and maintain the single source-of-truth context file for Answer Engine
  Optimization — the brand entity, offering, audience and personas, the prompts buyers
  ask AI, the competitor/alternative set, differentiators, authority assets, and a
  current AI-visibility baseline. Every other AEO skill reads this file first. Works
  for any business, B2B or B2C, product or service. Use at the start of any AEO
  engagement, when onboarding a brand or client, or whenever another AEO skill needs
  context that does not exist yet. Trigger on requests like "set up our AEO context",
  "what should AI say about us", "define our prompt set", "AEO baseline", or "the agent
  does not know our brand".
metadata:
  version: 0.1.0
---

# AEO Foundation

This skill builds the **foundation file** that every other AEO skill reads first:
`aeo-foundation.md`. Answer Engine Optimization lives or dies on context — to influence
what ChatGPT, Claude, Gemini, Perplexity, and Google AI Overviews say about a brand, an
agent has to know the brand as an *entity*, the *prompts* buyers actually ask, the
*competitors* who get recommended instead, and where the brand *stands today*. Captured
once, this file makes audits sharper, content on-target, and authority work focused. It
works for any business, B2B or B2C, product or service.

The output is a single Markdown file — `aeo-foundation.md` — kept at the root of the
user's AEO workspace. Other skills look for it by name; if it is missing, they should
point the user here.

## When to use this skill

- Starting AEO work on a new brand, product, service, or client.
- Another AEO skill needs the prompt set, entity facts, competitors, or baseline and
  none exists.
- The context is stale — a new competitor emerged, positioning shifted, the brand was
  misrepresented by an engine, or the prompt set has drifted.

## How to build it

Work like an interviewer, not a form. Pull everything you can from what the user already
has — their website, About page, existing schema, review profiles, prior answers — then
ask only for what is genuinely missing, a few questions at a time.

**Completeness is optional.** The user does not need to answer everything, or anything.
Capture what you can, tag gaps with `(assumption)` so later work knows what to verify,
and produce a useful file regardless. A thin foundation today beats a perfect one never;
the file is designed to grow as the engagement learns.

A concrete first move that grounds everything else: **run a quick baseline.** Ask each
major engine a handful of the brand's likely prompts and record what they say, who they
cite, and whether the brand appears at all. That snapshot anchors the whole strategy.

## Integrating an existing context

Many brands already have a context document — a positioning one-pager, a brand/voice
guide, an ICP doc, or a general marketing context file. Reuse it; do not start from
scratch and do not blindly copy it. Best practice:

- **Reference, don't duplicate.** Keep one source of truth per fact. The existing doc
  stays upstream for the general "who/what/why"; `aeo-foundation.md` is a thin AEO layer
  on top of it. Two patterns:
  - **Link** (for living docs the user maintains): point to the existing file for the
    shared sections and only fill the AEO-specific ones here. No drift.
  - **Import once** (for static/one-off docs): map its fields into the shared sections,
    note provenance and date, and maintain forward. Add a "re-sync when the source
    changes" note.
- **Know what carries over vs. what is AEO-only.** Reuse offering, audience/personas,
  positioning, differentiators, voice, proof, and the seed competitor list. The
  AEO-specific layers a normal context doc lacks must still be built: the **target
  prompts** (conversational questions, via **prompt-research**), the **AI-visibility
  baseline**, sharper **entity facts**, and the **technical context**.
- **Sharpen, don't transplant.** AEO needs more specificity than a brand deck: exact,
  web-consistent entity facts and the literal questions people ask AI. Reconcile any
  conflicting facts toward what is true on the public web. Treat the user's competitor
  list as a seed, then verify who engines actually recommend in the baseline.

## Gather areas

Cover as many as the user can provide. Each is optional.

1. **Brand entity** — official name (and disambiguation if the name is generic),
   category, one-line description, founding date, headquarters, key people, and the
   canonical profile URLs (site, LinkedIn, Crunchbase, Wikipedia/Wikidata if any).
2. **Offering** — what it is and does, the category customers file it under, core use
   cases and the jobs it gets done.
3. **Audience & personas** — who asks AI about this category, their context, constraints,
   and the language they use; distinct segments ranked by priority.
4. **Target prompts** — the real conversational questions buyers ask AI across awareness,
   consideration, and decision intent. This becomes the tracked prompt set the other
   skills optimize and measure against. Aim for a focused set of high-value prompts over
   a sprawling one.
5. **Competitor / alternative set** — who else gets recommended for those prompts,
   including the status quo, and the comparison points that matter.
6. **Positioning & differentiators** — the associations you want engines to make with
   the brand, and any unique mechanism or credible "only" claim.
7. **Authority assets** — original data or research, named experts and authors,
   third-party coverage and press, analyst mentions, review-platform presence, and
   notable corroboration that already exists.
8. **Current AI-visibility baseline** — per engine, what is said about the brand today,
   whether it is cited or merely mentioned, the sentiment, who out-cites it, and any
   factual errors to correct.
9. **Voice & boundaries** — claim constraints, regulated or sensitive terms, compliance
   needs (especially for health, finance, legal / YMYL topics).
10. **Technical context** — site platform and rendering (server-side vs client-side),
    CMS, whether AI crawlers are currently allowed, and the state of structured data.

## Output template

Produce the file using the structure in
[templates/aeo-foundation-template.md](templates/aeo-foundation-template.md). Omit a
section only if it truly does not apply; prefer a short `(assumption)`-tagged draft over
a blank. Keep it tight enough to read in a few minutes — it is a working reference, not a
brand bible.

## Maintenance

Treat the file as living. When other AEO work surfaces something — a prompt that
converts, a competitor that keeps winning citations, a misrepresentation an engine keeps
repeating, a new proof asset — update the foundation file and bump the date. The whole
library compounds off this file staying current; re-run the baseline periodically to
track movement.

## Related Skills

- **prompt-research** — expands and prioritizes the target prompt set captured here.
- **ai-visibility-audit** — turns the baseline into a scored, prioritized audit.
- **competitor-ai-analysis** — deepens the competitor/alternative picture.
- **entity-optimization** — acts on the brand-entity facts recorded here.
- All content, authority, technical, platform, and measurement skills read this file for
  audience, prompts, positioning, and proof.
