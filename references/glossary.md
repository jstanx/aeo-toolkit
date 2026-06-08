# AEO Glossary

Shared terminology for the AEO skills. Definitions are practical, not academic.

## Core terms

- **Answer engine** — any system that returns a synthesized answer instead of a list of
  links: ChatGPT, Claude, Gemini, Perplexity, Google AI Overviews, Bing Copilot, and
  similar. Often called an *AI assistant* or *AI search*.
- **AEO (Answer Engine Optimization)** — optimizing a brand and its content to be
  surfaced, cited, and recommended inside answer-engine responses. Used in this repo as
  the umbrella term for the whole discipline.
- **GEO (Generative Engine Optimization)** — near-synonym for AEO, emphasizing
  generative AI engines and citation share across them. The term used in the foundational
  academic research. This repo treats AEO and GEO as the same practice.
- **LLMO (Large Language Model Optimization)** — a narrower framing focused on how an LLM
  understands and extracts from your content. A subset of AEO.
- **AI SEO** — informal catch-all for "SEO adapted to AI search." Overlaps AEO heavily;
  many of the same fundamentals apply.

## How answers get built

- **Training data** — the broad web a model learned from during training. Influences what
  a model "knows" by default, with a knowledge cutoff.
- **Retrieval / RAG (Retrieval-Augmented Generation)** — live web search the assistant
  runs at answer time to ground its response in current sources. Where real-time
  citations and referral traffic come from.
- **Citation** — when an answer links or attributes a specific source ("according to
  X…"). Drives referral clicks.
- **Mention** — when an answer names a brand without linking. Still valuable for
  awareness and entity salience; not a click.
- **Share of voice (SOV) / share of answer** — a brand's portion of all citations or
  mentions across a defined prompt set, versus competitors.
- **Prompt set** — the curated list of conversational questions a brand is optimizing and
  measuring against (see `aeo-foundation`, `prompt-research`).

## Authority and content

- **Entity** — a distinct, recognized thing (brand, person, place) in a knowledge graph.
  Being a recognized entity is what lets engines confidently name you.
- **Knowledge graph** — a structured network of entities and relationships (e.g. Google's
  Knowledge Graph, Wikidata) that engines draw on for facts.
- **Semantic consensus** — the degree to which the same claims about a brand appear
  consistently across many trusted, independent sources. A strong driver of citation.
- **E-E-A-T** — Experience, Expertise, Authoritativeness, Trustworthiness. A quality lens
  engines (and Google) use; signaled by named authors, credentials, sourcing, accuracy.
- **Answer-first / BLUF (Bottom Line Up Front)** — leading a section with a short, direct,
  self-contained answer before the supporting detail. Improves extractability.
- **Semantic chunking** — structuring content so each section is a self-contained,
  independently understandable passage an engine can lift cleanly.
- **Information gain** — the unique, original value a page adds beyond what already exists
  (data, firsthand experience, fresh perspective). Favored by engines.

## Technical

- **AI crawler / bot** — an automated agent that fetches pages for an AI system. May be
  for training, real-time retrieval, or on-demand user fetches (see
  [ai-crawlers.md](ai-crawlers.md)).
- **SSR / CSR** — Server-Side Rendering delivers full HTML from the server; Client-Side
  Rendering builds content in the browser with JavaScript. Most AI crawlers do not
  execute JavaScript, so SSR content is far more reliably read.
- **Structured data / schema (JSON-LD)** — machine-readable markup describing a page's
  entities and content, helping engines parse and trust it (see
  [schema-cookbook.md](schema-cookbook.md)).
- **llms.txt** — a proposed plain-Markdown file at a site's root meant to summarize key
  content for LLMs. Adoption is early and engines largely ignore it today; treat as a
  low-cost, low-impact best practice.
