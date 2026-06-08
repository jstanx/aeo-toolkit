---
name: ai-visibility-audit
description: >-
  Audit how ready a brand is to be cited by answer engines and produce a prioritized fix
  list — baseline what ChatGPT, Perplexity, Gemini, and Google AI Overviews say today,
  then score discoverability, interpretability, attribution, authority, and governance.
  Works for any business, B2B or B2C, product or service. Use when the request is to run
  an AEO or GEO audit, check AI visibility, find out why a brand is not cited by AI,
  baseline AI search presence, or assess answer-engine readiness. For competitor share of
  voice use competitor-ai-analysis; for ongoing tracking use ai-visibility-tracking.
metadata:
  version: 0.1.0
---

# AI Visibility Audit

This skill answers two questions: **where does the brand stand in AI answers today, and
what is holding it back?** It baselines real engine responses, scores readiness across
five dimensions, and returns a prioritized roadmap. It is the diagnostic that points every
other AEO skill at the right work. It applies to any business, B2B or B2C.

## When to use this skill

- Running an initial AEO/GEO audit for a brand or client.
- Diagnosing why a brand is absent or misrepresented in AI answers.
- Producing a prioritized AEO roadmap.
- Re-auditing after major content, technical, or authority changes.

## Before you start

Read `aeo-foundation.md` for the brand, the prompt set, and competitors. If the prompt set
is thin, run **prompt-research** first — you cannot baseline without prompts. If the
foundation is missing, point to the **aeo-foundation** skill.

## Step 1 — Baseline the current state

Run the prompt set across the major engines and record, per prompt and per engine:

- Is the brand **cited** (linked), **mentioned** (named, no link), or **absent**?
- Who is cited instead, and in what order?
- What is the **sentiment** and is anything **factually wrong**?

This snapshot is both the diagnosis input and the measurement starting line.

## Step 2 — Score the five dimensions

Apply the shared rubric in
[../../references/aeo-audit-rubric.md](../../references/aeo-audit-rubric.md), scoring each
0–3:

1. **Discoverability** — can engines reach the content? (crawler access, rendering,
   speed, indexable pages)
2. **Interpretability** — can they understand it? (structure, answer-first, schema,
   entity clarity)
3. **Attribution** — will they cite it? (named authors, sourcing, original data)
4. **Authority & trust** — will they trust it? (third-party corroboration, reviews,
   freshness)
5. **Governance & risk** — is it safe to cite? (accuracy, compliance, consistent facts)

## Step 3 — Diagnose

For each prompt the brand loses, trace the cause to a dimension and a lever:

- Absent everywhere → usually **discoverability** or **entity** problems.
- Ranks/known but not quoted → **interpretability** (structure/extractability).
- Quoted less than competitors → **authority** (corroboration, freshness, reviews).
- Misrepresented → **governance/entity** consistency.

## Step 4 — Prioritize and deliver

Sort fixes by impact vs. effort into **critical** (blockers), **high-impact**, and
**long-term**, and map each to the skill that executes it. Use
[templates/audit-worksheet.md](templates/audit-worksheet.md) to capture scores and the fix
list, and map the result to a maturity stage (Invisible → Emerging → Established →
Authority).

## Output format

- **Baseline table** — presence, competitors, sentiment per top prompt and engine.
- **Dimension scores** — 0–3 each, /15 total, with evidence.
- **Prioritized fixes** — issue, why it matters, the fix, the owning skill, rough effort.
- **Maturity stage** and the few moves that advance it.
- `(assumption)` tags where access or data was limited.

## Common pitfalls

- Scoring structure without first baselining real answers.
- A 200-item checklist no one will action — prioritize.
- Auditing one engine and generalizing; they differ (see the platform skills).
- Treating the score as the deliverable instead of the roadmap.

## Tool

Score the five-dimension rubric and get a maturity stage:

```bash
python scripts/score_audit.py --template          # blank input to fill in
python scripts/score_audit.py --input scores.json # total /15 + stage + weakest dimensions
```

For a fast manual pass, use the shared [AEO readiness checklist](../../references/aeo-readiness-checklist.md).

> Optional. The script only automates this step; it needs `python3` (standard library only, no install). No Python? Just follow the steps above manually.

## Related Skills

- **aeo-foundation** / **prompt-research** — supply the prompts to baseline against.
- **competitor-ai-analysis** — quantifies share of voice vs. rivals.
- **ai-visibility-tracking** — turns this baseline into ongoing measurement.
- Content, authority, technical, and platform skills — execute the prioritized fixes.
