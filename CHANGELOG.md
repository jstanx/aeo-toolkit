# Changelog & Versions

The central record of what's in this toolkit, at what version, and what changed in each
release. Versions follow **semantic versioning** (MAJOR.MINOR.PATCH). Each release section
gets its date when it is published.

## Versioning policy

- **MAJOR** — breaking changes: structural/format changes, or removing/renaming a skill,
  agent, or tool.
- **MINOR** — new skills, agents, tools, or material content additions (backwards-compatible).
- **PATCH** — fixes, clarifications, and small edits.

Each skill also carries its own version in its `SKILL.md` frontmatter (`metadata.version`);
the tables below mirror those. When you change a component, bump it here **and** in its
frontmatter, and add a line to the relevant release below.

## Component versions

### Skills (27)

| Skill | Version |
|---|---|
| aeo-foundation | 0.1.0 |
| ai-capability-signaling | 0.1.0 |
| ai-crawler-access | 0.1.0 |
| ai-referral-analytics | 0.1.0 |
| ai-retrievability | 0.1.0 |
| ai-visibility-audit | 0.1.0 |
| ai-visibility-tracking | 0.1.0 |
| answer-engineering | 0.1.0 |
| author-authority | 0.1.0 |
| chatgpt-optimization | 0.1.0 |
| claim-accuracy | 0.1.0 |
| claude-optimization | 0.1.0 |
| community-and-reviews | 0.1.0 |
| comparison-content | 0.1.0 |
| competitor-ai-analysis | 0.1.0 |
| content-freshness | 0.1.0 |
| crawler-log-analysis | 0.1.0 |
| digital-pr | 0.1.0 |
| entity-optimization | 0.1.0 |
| evidence-and-citations | 0.1.0 |
| gemini-optimization | 0.1.0 |
| google-ai-overviews-optimization | 0.1.0 |
| llms-txt | 0.1.0 |
| multimodal-aeo | 0.1.0 |
| perplexity-optimization | 0.1.0 |
| prompt-research | 0.1.0 |
| structured-data | 0.1.0 |

### Agents (7)

| Agent | Version |
|---|---|
| aeo-auditor | 0.1.0 |
| aeo-implementer | 0.1.0 |
| aeo-strategist | 0.1.0 |
| authority-builder | 0.1.0 |
| content-optimizer | 0.1.0 |
| prompt-tester | 0.1.0 |
| technical-fixer | 0.1.0 |

### Tools (8)

| Tool | Skill | Version |
|---|---|---|
| check_ai_crawlers.py | ai-crawler-access | 0.1.0 |
| score_audit.py | ai-visibility-audit | 0.1.0 |
| test_prompts.py | ai-visibility-tracking | 0.1.0 |
| score_answer_blocks.py | answer-engineering | 0.1.0 |
| parse_crawler_logs.py | crawler-log-analysis | 0.1.0 |
| check_entity_consistency.py | entity-optimization | 0.1.0 |
| generate_llms_txt.py | llms-txt | 0.1.0 |
| generate_schema.py | structured-data | 0.1.0 |

### Repo tooling & infra

| File | Version |
|---|---|
| .claude-plugin/marketplace.json | 0.1.0 |

Reference docs in `references/` are unversioned living documents, kept current with the
toolkit as engine behavior and best practices change.

## Releases

### 0.1.0 — Initial release

The first public release: a complete, dedicated Answer Engine Optimization toolkit.

**Highlights**

- **27 skills** across foundation, strategy & research, content, authority,
  technical, per-engine (all five major engines), and measurement.
- **7 sub-agents** orchestrating the skills as a loop — diagnose, plan, execute
  (overall plus content / authority / technical specialists), and measure.
- **8 dependency-free tools** — crawler-access check, log parser, answer-block
  scorer, JSON-LD generator, llms.txt generator, entity-consistency checker, audit scorer,
  and prompt/citation tester.
- Shared reference library and a concrete **AEO readiness checklist**.
- Installable `marketplace.json`.
