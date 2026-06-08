# Answer Patterns: Worked Examples

Deep reference for `answer-engineering`. Shows the patterns in practice.

## Why answer-first (BLUF) works

Answer engines retrieve *passages*, not pages, and they weight the beginning of a passage
heavily. A reader — and a model — should get the answer in the first sentence or two,
before the supporting detail. This is the journalist's inverted pyramid and the military's
"bottom line up front." The build-up-to-a-conclusion essay structure is the wrong shape
for extraction: the engine often never reaches your conclusion.

## The dead-zone effect

Long documents have a recall curve: the **start** is recalled best, the **end** moderately,
and the **middle** much less reliably. Two consequences:

- Put the most important answer near the **top of the page**, with a short summary.
- Put each section's answer near the **top of the section**.
- Do not strand a critical, citable fact in the deep middle of a 3,000-word article.

## Before / after

### Before (buried, mixed, context-dependent)

> ### Pricing
> When we started the company, we believed pricing should be simple. Over the years
> we've experimented with many models, and after a lot of customer feedback we landed on
> an approach we're proud of. As mentioned above, our philosophy is value-based, and so
> the way we've structured things reflects that — there are a few tiers, and they scale
> with usage in a way most teams find fair once they get going.

Problem: the heading is a keyword stub; the answer is hedged and never actually stated; it
references "above"; an engine has nothing to lift.

### After (answer-first, self-contained)

> ### How much does Acme cost?
> Acme costs $0 to start and scales by tracked users: the Free plan covers up to 1,000
> monthly tracked users, Pro is $99/month up to 10,000, and Enterprise is custom-priced.
> All plans include the full analytics feature set; tiers differ only by volume and
> support.
>
> Most teams begin on Free to validate the data, then move to Pro once they pass 1,000
> tracked users… [expansion continues]

The 40–60 word block answers the exact question, stands alone, and is liftable verbatim.

## Writing the 40–60 word answer block

- State the answer in the **first sentence**.
- Make it **complete without the page** — no "as above," no undefined pronouns.
- Keep it **40–60 words**: long enough to be a full answer, short enough to be quoted whole.
- Be **specific** — names, numbers, conditions — not "it depends" or "fast and easy."
- Keep claims **accurate and defensible**; an engine that detects an overclaim deprioritizes
  the source.

## Formatting that chunks well

- **Paragraphs:** 2–4 sentences. Long blocks are harder to chunk and read.
- **Lists:** use for steps, criteria, or sets of items — easy for engines to enumerate.
- **Tables:** use for comparisons and specs — frequently pulled into AI answers.
- **Headings:** descriptive and question-shaped; never skip levels (H2 → H4).
- **One idea per section:** if a section needs the word "also" twice, it is two sections.

## FAQ formatting

FAQs are a high-extraction format because each item is already a self-contained Q&A.

- Phrase questions exactly as users ask AI (pull from the foundation prompt set).
- Answer each in 40–60 self-contained words; expand below only if needed.
- Reinforce with FAQPage schema (see the shared schema cookbook) — but only when the FAQ
  genuinely appears on the page.
- Do not pad the list with questions no one asks; relevance beats volume.

## Quick rewrite procedure

1. Find the question the section answers; make it the heading.
2. Write the answer in one or two sentences, 40–60 words, no back-references.
3. Move supporting detail below the answer.
4. Read the section in isolation; fix anything that only makes sense in context.
5. Check the page: is the top answer near the top? Are key facts out of the dead middle?
