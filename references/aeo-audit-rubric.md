# AEO Audit Rubric

A shared, five-dimension scoring model for assessing how ready a brand is to be cited by
answer engines. The `ai-visibility-audit` skill applies it; `ai-visibility-tracking` reuses
its metrics. Score each dimension 0–3 and combine into a maturity picture.

## The five dimensions

### 1. Discoverability — can engines reach the content?
- AI crawlers (retrieval + user-triggered) are allowed; CDN/WAF is not silently blocking.
- Important pages return clean 200s; sitemap present; reasonable page speed.
- Content is server-rendered or otherwise readable without executing JavaScript.

### 2. Interpretability — can engines understand it?
- Clear semantic structure: one H1, logical H2/H3, lists and tables where useful.
- Answer-first passages; self-contained chunks.
- Valid structured data (Organization, Article, Person, FAQ as relevant).
- Consistent, recognizable entity (name, category, facts).

### 3. Attribution — will engines cite it?
- Named authors with credentials and bylines.
- Clear sourcing: statistics, quotes, and links to authoritative references.
- Original data or genuine information gain.
- Organization and contact/credibility signals present.

### 4. Authority & trust — will engines trust it?
- Third-party corroboration: earned media, mentions, analyst/press coverage.
- Review-platform presence appropriate to the category.
- Community/forum presence where the category lives.
- Content freshness: substantively updated, not cosmetically re-dated.

### 5. Governance & risk — is it safe to cite?
- Accurate, non-misleading claims; corrections process for misrepresentation.
- Compliance for sensitive (YMYL) topics: health, finance, legal.
- Consistent entity facts across the web (no contradictions for engines to trip on).

## Scoring

For each dimension:

| Score | Meaning |
|---|---|
| 0 | Absent — major blocker |
| 1 | Partial — significant gaps |
| 2 | Solid — minor gaps |
| 3 | Strong — best practice |

Total out of 15. Pair the score with a prioritized fix list (impact vs. effort) rather
than treating the number as the deliverable.

## Maturity stages

Map the picture to a stage to set expectations and a roadmap:

- **Invisible** — rarely or never cited; no baseline presence.
- **Emerging** — occasional citations; entity and content foundations forming.
- **Established** — consistent citations across engines; recognized entity; real topical
  authority.
- **Authority** — the default entity for the category; cited across engines; shapes how AI
  describes the space.

## Companion metrics (for tracking over time)

- **Citation rate** — share of the prompt set where the brand appears with a link.
- **Mention rate** — share where the brand is named without a link.
- **Share of voice** — brand's share of all named entities across the prompt set vs.
  competitors.
- **Sentiment** — positive / neutral / negative framing of mentions.
- **AI referral traffic** — visits attributed to answer engines (see `ai-referral-analytics`).
