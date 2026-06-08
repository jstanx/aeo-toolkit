---
name: answer-engineering
description: >-
  Structure content so answer engines can extract and cite it — answer-first / BLUF
  passages, 40-60 word direct-answer blocks, question-style headings, semantic chunking,
  and self-contained sections. Works for any business, B2B or B2C, product or service.
  Use when writing or rewriting content to get cited by AI, making a page "AI-readable",
  formatting answers for ChatGPT or Perplexity or Google AI Overviews, structuring FAQs,
  or fixing content that ranks but never gets quoted. For the evidence inside the answers
  use evidence-and-citations; for markup use structured-data; for rendering use
  ai-retrievability.
metadata:
  version: 0.1.0
---

# Answer Engineering

This skill structures content so answer engines can **find the answer, lift it cleanly,
and attribute it to you**. Engines do not read a page top to bottom and reward length;
they slice pages into passages and pull the one that best answers the query. If your
answer is buried, hedged, or tangled with three other ideas, it does not get used — no
matter how good the page is. Answer engineering is the craft of making each passage
extractable. It works for any business, B2B or B2C, product or service.

This is about *structure and clarity*. The *evidence* that makes an answer credible
(statistics, quotes, citations) is **evidence-and-citations**; the *markup* that helps
machines parse it is **structured-data**; whether a crawler can read the page at all is
**ai-retrievability**. Use them together.

## When to use this skill

- Writing new content intended to be cited by AI.
- Rewriting content that ranks in search but is never quoted in AI answers.
- Structuring FAQs, definitions, comparisons, and how-tos for extraction.
- Auditing a page's structure for "AI-readability."

## Before you write

Read `aeo-foundation.md` for the audience and the target prompts — you are writing answers
to *specific questions people ask AI*, so start from those. If it is missing, point to the
**aeo-foundation** skill. Confirm: the exact question this passage answers, and the one
fact or recommendation the reader (and the engine) should walk away with.

## Core principles

- **Answer first (BLUF).** Lead each section with the direct answer, then expand. Engines
  weight the opening of a passage heavily; the conclusion-first "inverted pyramid" beats
  the slow build-up.
- **One question, one section.** Each section answers a single question completely. Mixed
  ideas produce passages an engine cannot cleanly lift.
- **Self-contained passages.** Write each section so it makes full sense pulled out of the
  page with no surrounding context — because that is exactly how it will be used.
- **Avoid the middle "dead zone."** Models recall the start and end of long documents far
  better than the middle. Put key answers near the top of the page and near the top of
  each section, not buried mid-article.
- **Specific and verifiable beats padded.** A tight, concrete answer is extracted; filler
  and keyword repetition are ignored or penalized (see the shared
  [citation ranking factors](../../references/citation-ranking-factors.md)).
- **Match how people ask.** Phrase headings as the natural-language questions from the
  prompt set, not as keyword fragments.

## The answer-block pattern

The reusable unit of AEO content:

1. **Heading = the question**, phrased the way a person would ask an assistant
   ("How much does X cost?" not "Pricing").
2. **A 40–60 word direct answer** immediately after the heading. Self-contained, no
   "as mentioned above," no setup. This is the part engines lift, so make it complete and
   accurate on its own.
3. **Expansion** — 150–400 words of context, evidence, examples, and nuance for the human
   reader and for follow-up depth.
4. **A clean exit** — a takeaway or transition; do not let the next idea bleed in.

See [references/answer-patterns.md](references/answer-patterns.md) for worked before/after
examples, the BLUF rationale, the dead-zone effect, and FAQ formatting.

## Workflow

1. **List the questions.** From the foundation prompt set, gather the exact questions this
   page should answer. One page can answer several related questions, one per section.
2. **Outline as questions.** Turn each into a question-style heading; order them the way a
   reader's curiosity flows (often broad → specific).
3. **Write the answer block** for each: 40–60 word direct answer, then expansion.
4. **Make each passage self-contained.** Reread each section alone — does it stand without
   the rest of the page? Remove back-references.
5. **Front-load the page.** Put the most important answer (and a short summary) near the
   top; keep critical content out of the deep middle.
6. **Format for chunking.** Short paragraphs (2–4 sentences), lists for steps or sets,
   tables for comparisons, descriptive subheadings.
7. **Hand off.** Add evidence with **evidence-and-citations**, markup with
   **structured-data**, and verify crawlability with **ai-retrievability**.

Run the result against [templates/answer-block-checklist.md](templates/answer-block-checklist.md)
before publishing.

## Output format

- The restructured content, ready to publish, with question-style headings and answer
  blocks in place.
- For key sections, the **40–60 word answer block** called out so the user can see and
  refine the exact extractable passage.
- A short note on what changed and why (e.g., "moved the pricing answer above the fold;
  split the buried comparison into its own section").
- Any `(assumption)` about the audience question or claim flagged for confirmation.

## Common pitfalls

- Burying the answer under a long warm-up.
- Sections that answer three questions at once.
- Passages full of "as we saw above" that collapse when extracted.
- Important answers stranded in the middle of a long page.
- Question headings written as keyword stubs instead of real questions.
- Padding to hit a word count — it dilutes the passage and can hurt citation.

## Tool

Score a page (Markdown, HTML, or URL) for extractability — question headings plus 40-60 word answer blocks:

```bash
python scripts/score_answer_blocks.py page.md
python scripts/score_answer_blocks.py --url https://example.com/page
```

> Optional. The script only automates this step; it needs `python3` (standard library only, no install). No Python? Just follow the steps above manually.

## Related Skills

- **aeo-foundation** — the audience and the prompt set you are answering.
- **evidence-and-citations** — the statistics, quotes, and sources that make answers
  credible and cite-worthy.
- **structured-data** — schema (incl. FAQPage) that reinforces extraction.
- **ai-retrievability** — ensures crawlers can actually read the structured content.
- **ai-visibility-audit** — checks interpretability/extractability across the site.
