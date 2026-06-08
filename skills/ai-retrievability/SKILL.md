---
name: ai-retrievability
description: >-
  Make sure answer engines can actually read and extract a page — server-rendered content
  (most AI crawlers do not run JavaScript), clean semantic HTML, fast and stable pages, and
  an internal-linking structure that helps chunking. Works for any business, B2B or B2C,
  product or service. Use when the request is to make a site AI-readable, fix content that
  is invisible to AI crawlers, address JavaScript rendering or SSR for AI, improve semantic
  HTML or page speed for AEO, or structure internal links for AI. Pairs with
  ai-crawler-access and answer-engineering.
metadata:
  version: 0.1.0
---

# AI Retrievability

This skill ensures that once an answer engine reaches a page, it can **actually read and
extract the content**. Access (**ai-crawler-access**) gets the bot to the door; this skill
makes sure there is readable content behind it. The big trap: most dedicated AI crawlers do
**not** execute JavaScript, so content that only appears after client-side rendering is
effectively blank to them — even when it looks fine in a browser and ranks on Google. It
works for any business, B2B or B2C.

## When to use this skill

- Content is reachable but not being read or cited by AI.
- A site is a client-rendered SPA and may be invisible to AI crawlers.
- Improving semantic HTML, page speed, or stability for AEO.
- Structuring internal links to aid passage discovery and chunking.

## Before you start

Read `aeo-foundation.md` for the technical context (platform, rendering, CMS). If it is
missing, point to the **aeo-foundation** skill.

## The retrievability checklist

- **Render server-side.** Deliver the real content in the initial HTML (SSR, static
  generation, or prerendering). Do not rely on client-side JavaScript to inject the main
  content — most AI crawlers will not run it. (Googlebot renders JS; the dedicated AI
  crawlers generally do not — so don't assume Google's behavior.)
- **Test without JavaScript.** View the page with JS disabled (or fetch raw HTML): is the
  main content there? If it is blank, AI crawlers see blank too.
- **Clean, semantic HTML.** One `h1`, logical `h2`/`h3`, real `article`/`section`/list/table
  elements. A high signal-to-noise ratio (content, not a wall of markup) extracts better.
- **Fast and stable.** Reasonable time-to-first-byte and load; reliable responses. Slow or
  error-prone pages get crawled less and cited less; keep payloads lean.
- **Lean pages.** Trim bloated markup and heavy scripts that bury the content or slow the
  fetch.
- **Internal linking for chunking.** Descriptive anchor text and a hub-and-spoke structure
  (pillar pages linking to focused sub-pages and back) help engines find and relate
  passages. Avoid orphan pages.

## Workflow

1. **Test rendering.** Fetch key pages as raw HTML / with JS off. Flag anything whose main
   content depends on client-side rendering.
2. **Fix rendering.** Move critical content to server-side render / static / prerender so it
   is present in the initial HTML.
3. **Clean the HTML.** Enforce semantic structure and heading hierarchy; reduce markup
   bloat.
4. **Check speed and stability.** Measure load and error rates on real pages; fix slow or
   failing templates.
5. **Structure internal links.** Map pillars and clusters; add descriptive internal links;
   resolve orphans.
6. **Re-test.** Confirm the main content is present without JS and pages load cleanly.

## Output format

- A **rendering report**: which pages/templates depend on JavaScript for main content.
- The **fixes**: rendering changes, HTML/structure cleanups, speed/stability issues.
- An **internal-linking plan** (pillars, clusters, anchor text, orphan fixes).
- `(assumption)` tags where platform behavior was unverified.

## Common pitfalls

- Assuming AI crawlers run JavaScript because Googlebot does — they generally do not.
- A page that looks complete in the browser but is blank in raw HTML.
- Bloated markup that buries content and slows fetches.
- Skipped heading levels and non-semantic `div` soup that resist chunking.
- Orphan pages with no internal links in.

## Related Skills

- **ai-crawler-access** — gets crawlers to the page in the first place.
- **answer-engineering** — the structure inside the readable HTML.
- **structured-data** — machine-readable signals layered on clean HTML.
- **ai-visibility-audit** — flags retrievability as a discoverability/interpretability gap.
