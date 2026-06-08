---
name: ai-capability-signaling
description: >-
  Make a website consumable by AI agents and answer engines beyond plain HTML — llms.txt
  and llms-full.txt, clean Markdown "twins" of key pages, copy-for-AI and raw-view
  affordances, and machine-readable metadata. Works for any business, B2B or B2C, product
  or service. Use when the request is to make a site AI-readable or agent-ready, expose
  content to LLMs and agents, set up Markdown versions or copy-for-AI, or implement
  agentic engine optimization. Forward-looking and low-cost; pairs with llms-txt,
  ai-retrievability, and structured-data.
metadata:
  version: 0.1.0
---

# AI Capability Signaling

Beyond being *reachable* (**ai-crawler-access**), *readable* (**ai-retrievability**), and
*parseable* (**structured-data**), you can proactively publish **agent-friendly
representations** of your content. As AI assistants and autonomous agents increasingly
fetch, summarize, and act on the web, these signals help them consume your content
correctly and represent your brand accurately. This skill is the forward edge of AEO —
sometimes called "agentic engine optimization." It works for any business, B2B or B2C.

**Honest framing up front:** most of these are *emerging* and *low-adoption* today. Engines
still consume ordinary HTML for the most part, and few broadly honor signals like
`llms.txt`. Do this work because it is **cheap, future-facing, and differentiating** — not
because it guarantees citations. Land the proven levers first (**answer-engineering**,
**evidence-and-citations**, authority, **structured-data**), then add these.

## When to use this skill

- Making a site "AI-readable" / "agent-ready" beyond standard SEO/AEO.
- Setting up Markdown versions of pages, `llms.txt`, or copy-for-AI affordances.
- Helping agents and users feed your content to assistants accurately.
- Future-proofing for an agent-consumed web.

## Before you start

Read `aeo-foundation.md` for the priority pages and prompts — signal the content that
matters, not everything. The dedicated **llms-txt** skill handles that file in depth; this
skill is the broader umbrella. Details on every format are in
[references/ai-readable-formats.md](references/ai-readable-formats.md).

## The signals

1. **`llms.txt` and `llms-full.txt`.** A curated, Markdown map of your key pages (and an
   optional full-content version) at the site root. Cheap to publish; see **llms-txt** for
   the file itself and its current, limited reception.
2. **Markdown twins.** A clean Markdown rendering of each important page — stripped of
   nav, ads, and boilerplate — served alongside the HTML (e.g. a `.md` companion URL or via
   content negotiation). Gives agents pure, unambiguous content. Used effectively by
   documentation platforms.
3. **Copy-for-AI / raw view.** UX affordances — "copy page as Markdown," a raw/plain-text
   view — so a human can hand your page to an assistant accurately and completely. Highest
   value on docs and long-form pages people paste into chat.
4. **Machine-readable metadata.** Clean per-page metadata (title, author, published and
   updated dates, summary) and structured content feeds (RSS/JSON). Optionally surface
   per-page token counts so agents can budget context.
5. **Capability descriptions.** Plainly state what the product, service, or API does in
   terms an agent can use to recommend or operate it correctly. For API/tooling brands this
   extends to agent/tool manifests (e.g. an MCP server) — so agents can actually *use* you.
6. **Parity.** Whatever agent-readable version you publish must match the human page.
   Drift between the two is worse than not having it.

## Workflow

1. **Pick the pages.** From the foundation, list the priority pages worth exposing (key
   answers, docs, product/comparison pages). Don't twin the whole site.
2. **Choose formats per page.** `llms.txt` for the whole site (always, it's cheap);
   Markdown twins for top content; copy-for-AI on docs/long-form; metadata everywhere.
3. **Publish `llms.txt` / `llms-full.txt`.** Hand off to **llms-txt** for the file.
4. **Generate Markdown twins** for the priority pages and wire up a stable convention
   (companion URL or content negotiation). Automate so they stay in sync.
5. **Add copy-for-AI / raw affordances** where users paste content into assistants.
6. **Expose clean metadata** and ensure it agrees with the visible page.
7. **Set expectations and monitor.** Treat as forward-looking; revisit as engine and agent
   adoption grows.

## Output format

- A **capability-signaling plan**: which formats for which pages, and why.
- The **`llms.txt`** (via llms-txt) and a **sample Markdown twin** for a priority page.
- **Copy-for-AI** implementation guidance for the relevant templates.
- A **parity/sync note** describing how the agent-readable versions stay current.
- `(assumption)` tags where page priorities or platform capabilities were unknown.

## Common pitfalls

- Treating any of this as a citation guarantee — it is forward-looking, not proven ROI.
- **Markdown twins drifting** from the live page (stale or contradictory content).
- Over-investing here while the proven AEO levers are still weak.
- Exposing machine content that is incomplete or out of date.
- Twinning everything instead of the pages that matter.

## Related Skills

- **llms-txt** — the `llms.txt` / `llms-full.txt` file in depth, with honest expectations.
- **ai-retrievability** — being readable at all (server-rendered, clean HTML) comes first.
- **structured-data** — machine-readable entities and facts via schema.
- **answer-engineering** — the actual content quality these formats expose.
