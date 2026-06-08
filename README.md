# AEO Toolkit — Answer Engine Optimization skills, agents & tools

A professional, end-to-end **Answer Engine Optimization** toolkit — skills, agents, and runnable tools.

Search is changing. Instead of scrolling a page of blue links, people increasingly ask an
AI assistant — ChatGPT, Claude, Gemini, Perplexity, Google AI Overviews — and act on the
single answer it gives. **AEO is the practice of getting your brand surfaced, cited, and
recommended inside those answers.** This library turns that practice into skills an agent
can run: diagnose where you stand, research the prompts that matter, engineer content that
gets quoted, build the authority engines trust, fix the technical foundations, and measure
the results.

It works for any business — B2B or B2C, product or service — and assumes no prior AEO
background; the skills explain the concepts as they go.

Built by [Jason Stanley](https://github.com/jstanx).

> **Compatible with any agent that supports the open `SKILL.md` standard** — Claude Code,
> Claude.ai, Cursor, Codex, Gemini CLI, and more.

## Install

Pick whichever fits your setup.

```bash
# Claude Code — add this repo as a plugin marketplace, then install
/plugin marketplace add jstanx/aeo-toolkit
/plugin install aeo-toolkit

# Any SKILL.md agent (Cursor, Codex, Gemini CLI, …) via the npx installer
npx skills add https://github.com/jstanx/aeo-toolkit            # all skills
npx skills add https://github.com/jstanx/aeo-toolkit --skill ai-visibility-audit

# Or clone and copy the skills you want into your agent's skills folder
git clone https://github.com/jstanx/aeo-toolkit.git
cp -r aeo-toolkit/skills/ai-visibility-audit ~/.claude/skills/
```

Skills are plain folders, so you can also just drop any `skills/<name>/` directory into
your project and your agent will pick it up.

## Use it

Once installed, your agent loads the right skill automatically when your request matches —
or you can call one directly.

```text
You:  "Set up our AEO context."
      → aeo-foundation builds the source-of-truth context file

You:  "Audit my site and tell me why I'm not getting cited by AI."
      → ai-visibility-audit baselines every engine and returns a prioritized roadmap

You:  "Rewrite this page so ChatGPT and Perplexity will quote it."
      → answer-engineering restructures it into extractable, answer-first passages

Direct call:  /ai-visibility-audit      /entity-optimization      /prompt-research
```

## How the skills fit together

```text
                       ┌──────────────────────────┐
                       │      aeo-foundation      │   the context file every skill reads
                       └─────────────┬────────────┘
                                     │
     ┌───────────────┬───────────────┼───────────────┬────────────────┐
     ▼               ▼               ▼               ▼                ▼
  STRATEGY &      CONTENT        AUTHORITY        TECHNICAL        PLATFORM
  RESEARCH                       & OFF-SITE                        (per engine)
     │               │               │               │                │
     └───────────────┴──────► MEASUREMENT ◄──────────┴────────────────┘
                     tracks results and feeds learnings back into the foundation
```

Build the foundation once; every other skill reads it, and the measurement skills feed what
they learn back in. Skills also cross-link each other and a shared
[`references/`](references/) library, so the set works as a connected system — not a pile of
tips.

## Start here

1. **[aeo-foundation](skills/aeo-foundation/)** — build the context file every other skill
   reads first (brand entity, prompt set, competitors, baseline).
2. **[ai-visibility-audit](skills/ai-visibility-audit/)** — see where you stand today and
   get a prioritized roadmap.
3. Then work the roadmap with the content, authority, technical, platform, and measurement
   skills below.

## The skills

**Foundation**
| Skill | What it does |
|---|---|
| [aeo-foundation](skills/aeo-foundation/) | The source-of-truth context file the others read |

**Strategy & research**
| Skill | What it does |
|---|---|
| [prompt-research](skills/prompt-research/) | Find and prioritize the prompts buyers ask AI |
| [ai-visibility-audit](skills/ai-visibility-audit/) | Baseline + score readiness, produce a roadmap |
| [competitor-ai-analysis](skills/competitor-ai-analysis/) | Share of voice and citation gaps vs competitors |

**Content**
| Skill | What it does |
|---|---|
| [answer-engineering](skills/answer-engineering/) | Structure content so engines extract and cite it |
| [evidence-and-citations](skills/evidence-and-citations/) | Add the statistics, data, quotes, and sources engines reward |
| [content-freshness](skills/content-freshness/) | Keep content current with substantive refreshes |
| [comparison-content](skills/comparison-content/) | Win "best of", alternatives, and "X vs Y" prompts |
| [multimodal-aeo](skills/multimodal-aeo/) | Optimize video, images, and audio for AI answers |
| [claim-accuracy](skills/claim-accuracy/) | Accuracy + consistency as a citation/trust signal |

**Authority & off-site**
| Skill | What it does |
|---|---|
| [entity-optimization](skills/entity-optimization/) | Become a recognized entity in knowledge graphs |
| [author-authority](skills/author-authority/) | Build named-author E-E-A-T signals |
| [digital-pr](skills/digital-pr/) | Earn the third-party corroboration that drives citations |
| [community-and-reviews](skills/community-and-reviews/) | Presence on Reddit, forums, and review platforms |

**Technical**
| Skill | What it does |
|---|---|
| [ai-crawler-access](skills/ai-crawler-access/) | Let the right AI bots crawl; set a deliberate policy |
| [structured-data](skills/structured-data/) | JSON-LD schema for parsing and entities |
| [ai-retrievability](skills/ai-retrievability/) | Server-rendered, readable, fast, well-linked pages |
| [llms-txt](skills/llms-txt/) | Implement `llms.txt` with honest expectations |
| [ai-capability-signaling](skills/ai-capability-signaling/) | Markdown twins, copy-for-AI, machine metadata (forward edge) |
| [crawler-log-analysis](skills/crawler-log-analysis/) | Analyze access logs for real AI-bot behavior |

**Platform-specific**
| Skill | What it does |
|---|---|
| [perplexity-optimization](skills/perplexity-optimization/) | Tune for Perplexity (freshness, community) |
| [chatgpt-optimization](skills/chatgpt-optimization/) | Tune for ChatGPT (entity, mentions, authority) |
| [google-ai-overviews-optimization](skills/google-ai-overviews-optimization/) | Tune for Google AI Overviews (organic + structure) |
| [gemini-optimization](skills/gemini-optimization/) | Tune for Gemini (Google ecosystem, YouTube) |
| [claude-optimization](skills/claude-optimization/) | Tune for Claude (accuracy, author authority, original data) |

**Measurement**
| Skill | What it does |
|---|---|
| [ai-visibility-tracking](skills/ai-visibility-tracking/) | Track citations, share of voice, sentiment over time |
| [ai-referral-analytics](skills/ai-referral-analytics/) | Attribute AI-assistant traffic in analytics |

<details>
<summary><strong>All skills, A–Z</strong></summary>

[aeo-foundation](skills/aeo-foundation/) ·
[ai-capability-signaling](skills/ai-capability-signaling/) ·
[ai-crawler-access](skills/ai-crawler-access/) ·
[ai-referral-analytics](skills/ai-referral-analytics/) ·
[ai-retrievability](skills/ai-retrievability/) ·
[ai-visibility-audit](skills/ai-visibility-audit/) ·
[ai-visibility-tracking](skills/ai-visibility-tracking/) ·
[answer-engineering](skills/answer-engineering/) ·
[author-authority](skills/author-authority/) ·
[chatgpt-optimization](skills/chatgpt-optimization/) ·
[claim-accuracy](skills/claim-accuracy/) ·
[claude-optimization](skills/claude-optimization/) ·
[community-and-reviews](skills/community-and-reviews/) ·
[comparison-content](skills/comparison-content/) ·
[competitor-ai-analysis](skills/competitor-ai-analysis/) ·
[content-freshness](skills/content-freshness/) ·
[crawler-log-analysis](skills/crawler-log-analysis/) ·
[digital-pr](skills/digital-pr/) ·
[entity-optimization](skills/entity-optimization/) ·
[evidence-and-citations](skills/evidence-and-citations/) ·
[gemini-optimization](skills/gemini-optimization/) ·
[google-ai-overviews-optimization](skills/google-ai-overviews-optimization/) ·
[llms-txt](skills/llms-txt/) ·
[multimodal-aeo](skills/multimodal-aeo/) ·
[perplexity-optimization](skills/perplexity-optimization/) ·
[prompt-research](skills/prompt-research/) ·
[structured-data](skills/structured-data/)

</details>

## Agents

Seven sub-agents orchestrate the skills as a loop — **diagnose → plan → execute → measure**
(in [`agents/`](agents/)):

- [aeo-auditor](agents/aeo-auditor.md) — **diagnose**: a full audit and prioritized roadmap.
- [aeo-strategist](agents/aeo-strategist.md) — **plan**: turn findings into a sequenced, skill-mapped plan.
- [aeo-implementer](agents/aeo-implementer.md) — **execute**: carry out the whole roadmap across domains.
- [content-optimizer](agents/content-optimizer.md) — execute (content): structure, evidence, freshness, accuracy, media.
- [authority-builder](agents/authority-builder.md) — execute (authority): entity, authors, digital PR, community, comparisons.
- [technical-fixer](agents/technical-fixer.md) — execute (technical): crawler access, readability, schema, llms.txt, logs.
- [prompt-tester](agents/prompt-tester.md) — **measure**: citations and share of voice across engines over time.

## Tools

Many skills ship small, **dependency-free** scripts you can run directly — an AI-crawler
access checker, an access-log parser, an answer-block extractability scorer, a JSON-LD
generator, an `llms.txt` generator, an entity-consistency checker, an audit scorer, and a
prompt/citation tester. Each skill's **Tool** section documents how to run its script.

## Requirements

- **Using the skills:** nothing to install — they're instructions any compatible agent reads.
- **Running the optional tool scripts:** Python 3 (standard library only — no `pip install`).
  Don't have Python? Each skill's steps work fine by hand; the scripts just automate them.

## Repository layout

Every skill lives in its own folder under [`skills/`](skills/), defined by a `SKILL.md`
file, with deeper material in `references/`, reusable `templates/`, and runnable `scripts/`:

```text
skills/<skill-name>/
  SKILL.md          # when to use it + how to do the work
  references/       # deep guides, tables, worked examples (loaded on demand)
  templates/        # checklists, audit sheets, trackers
  scripts/          # optional runnable tools (pure standard library)
agents/             # sub-agents that orchestrate the skills
references/         # shared, cross-skill library (see below)
```

A `SKILL.md` front matter tells an agent **when** to reach for the skill; the body tells it
**how** to do the work and **what** to produce. The shared
[`references/`](references/) library holds cross-cutting material:

- [glossary.md](references/glossary.md) — AEO/GEO/LLMO terms
- [ai-crawlers.md](references/ai-crawlers.md) — AI bot user-agent landscape and access control
- [citation-ranking-factors.md](references/citation-ranking-factors.md) — what drives AI citations
- [schema-cookbook.md](references/schema-cookbook.md) — reusable JSON-LD recipes
- [aeo-audit-rubric.md](references/aeo-audit-rubric.md) — the shared scoring model
- [aeo-readiness-checklist.md](references/aeo-readiness-checklist.md) — a concrete, testable readiness checklist

## Versioning

Semantic versioning. See [CHANGELOG.md](CHANGELOG.md) for the version of every skill, agent, and tool, plus release notes and change history.

## Contributing

This library is meant to grow as answer engines evolve. See
[CONTRIBUTING.md](CONTRIBUTING.md) for the structure and quality bar. Keep content original,
practical, and vendor-neutral, and cross-link related skills so the set stays connected.

## License

[MIT](LICENSE) © [Jason Stanley](https://github.com/jstanx)
