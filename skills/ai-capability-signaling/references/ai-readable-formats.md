# AI-Readable Formats

Deep reference for `ai-capability-signaling`. Each format, how to implement it, and an
honest read on how much it matters today.

## llms.txt and llms-full.txt

- **What:** a Markdown file at `/llms.txt` summarizing the site and linking key pages; an
  optional `/llms-full.txt` containing the full text of important pages for direct
  ingestion.
- **Implement:** see the **llms-txt** skill for the file format and placement.
- **Reality:** adoption is early and most engines do not yet parse it. Low cost, mild
  upside, useful for docs-heavy sites and for stating brand facts plainly. Not a citation
  lever today.

## Markdown twins

- **What:** a clean Markdown version of a page — just the content, no nav/ads/chrome — so
  an agent gets unambiguous text instead of parsing cluttered HTML.
- **Conventions (pick one and keep it stable):**
  - **Companion URL:** serve `/<path>.md` next to `/<path>` (common on docs platforms).
  - **Content negotiation:** return Markdown when the request's `Accept` header prefers
    `text/markdown`.
- **Keep in sync:** generate twins from the same source as the HTML (build step or
  on-the-fly conversion). A stale twin that contradicts the page is worse than none.
- **Scope:** twin the priority pages (key answers, docs, product/comparison), not the
  whole site.
- **Reality:** helps specific agent and retrieval workflows that prefer clean text; not
  broadly required for citation. Cheap if your stack can generate it.

## Copy-for-AI / raw view

- **What:** UX affordances that let a person hand your page to an assistant accurately:
  a "Copy page as Markdown" button, a "View as plain text/raw" link, or a one-click
  "Open in ChatGPT/Claude" with the page content prefilled.
- **Where it matters most:** documentation, long-form guides, and reference pages people
  routinely paste into chat assistants.
- **Implement:** generate the Markdown (reuse the twin), wire it to a copy button or raw
  endpoint. Keep it to the main content.
- **Reality:** a genuine UX win for AI-using visitors; indirectly improves how accurately
  your content is represented when summarized.

## Machine-readable metadata

- **Per-page metadata:** clear title, author, `datePublished`/`dateModified`, and a short
  summary — consistent with your structured data (see **structured-data**).
- **Feeds:** an RSS/JSON feed of content so agents and aggregators can discover updates.
- **Token counts (optional):** publishing approximate token counts per page lets agents
  budget context windows when ingesting your content.
- **Reality:** metadata and feeds are well-established and low-risk; token-count exposure
  is niche and experimental.

## Capability descriptions (for products, services, APIs)

- **Plain capability statements:** describe what the offering does, who it's for, and how
  to use it, in direct language an agent can lift to recommend or operate it correctly.
  This complements **entity-optimization** (who you are) with what you *do*.
- **Agent/tool manifests:** if you offer an API or tool, exposing it to agents (for
  example via an MCP server) lets agents actually call it — turning "described" into
  "usable." This is an emerging surface most relevant to software/tooling brands.
- **Reality:** capability clarity helps agents represent you accurately now; full
  agent-operability (manifests/MCP) is leading-edge and audience-specific.

## Parity and maintenance checklist

- [ ] Agent-readable versions match the human page (no contradictions).
- [ ] Twins/metadata regenerate automatically from the same source as the HTML.
- [ ] Only priority pages are twinned; the set is documented.
- [ ] `llms.txt` (and `llms-full.txt` if used) reflect current key pages.
- [ ] Copy-for-AI / raw views return clean main content, not chrome.
- [ ] Expectations set: forward-looking, revisit as adoption grows.
