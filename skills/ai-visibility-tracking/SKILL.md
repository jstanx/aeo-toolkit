---
name: ai-visibility-tracking
description: >-
  Measure AI visibility over time — citation rate, mention rate, share of voice vs
  competitors, sentiment, and position — across ChatGPT, Perplexity, Gemini, and Google AI
  Overviews, with a repeatable cadence. Works for any business, B2B or B2C, product or
  service. Use when the request is to track or monitor AI visibility, measure share of
  voice in AI answers, set up AEO or GEO reporting, benchmark citations over time, or prove
  AEO ROI. Vendor-neutral. Pairs with ai-visibility-audit and ai-referral-analytics.
metadata:
  version: 0.1.0
---

# AI Visibility Tracking

This skill measures whether AEO work is actually moving the needle. It defines the metrics,
the method, and the cadence to track **citations, mentions, share of voice, sentiment, and
position** across engines over time. The audit is a snapshot; this is the ongoing
instrument. It is vendor-neutral — the metrics and method matter more than any one tool,
and the market of tools changes constantly. It works for any business, B2B or B2C.

## When to use this skill

- Standing up AEO/GEO measurement and reporting.
- Tracking citation and share-of-voice trends over time.
- Demonstrating the impact (ROI) of AEO work.
- Watching for new gaps, losses, or misrepresentations.

## Before you start

Read `aeo-foundation.md` for the prompt set, competitors, and the baseline. If there is no
prompt set or baseline, run **prompt-research** and **ai-visibility-audit** first — you
cannot track without them.

## The metrics

- **Citation rate** — share of the prompt set where the brand appears *with a link*.
- **Mention rate** — share where the brand is *named without a link* (still valuable for
  salience).
- **Share of voice** — the brand's share of all named entities across the prompt set,
  versus competitors. The core competitive metric.
- **Position** — whether the brand is cited early or late in the answer.
- **Sentiment** — positive / neutral / negative framing of mentions.
- **Accuracy** — whether what engines say about the brand is correct (track corrections).
- **AI referral traffic** — visits from answer engines (set up via **ai-referral-analytics**).

## Method (vendor-neutral)

You can run this manually for a focused prompt set, or with a dedicated tool for scale; the
measurement definitions are the same either way.

1. **Fix the inputs.** Lock the prompt set, the engines to track, and the competitor list so
   results are comparable over time.
2. **Run the set on a cadence.** Query each prompt on each engine; record citation, mention,
   position, sources, and sentiment. Keep conditions consistent (note that personalization
   and location can vary results).
3. **Compute the metrics** per engine and overall; calculate share of voice vs. competitors.
4. **Log to a tracker.** Use [templates/tracking-sheet.md](templates/tracking-sheet.md) so
   each pass is a dated, comparable row.
5. **Review trends and act.** Flag wins to reinforce, losses to investigate (often a
   freshness or competitor move), and inaccuracies to correct.

## Cadence

- **Weekly/biweekly:** citation, mention, sentiment on the core prompt set.
- **Monthly:** share of voice vs. competitors; trend review.
- **Quarterly:** full re-audit (with **ai-visibility-audit**) and prompt-set refresh.

## Output format

- A **dated metrics snapshot** per engine: citation rate, mention rate, SOV, position,
  sentiment.
- A **trend read**: what improved, what slipped, and the likely cause.
- An **action list**: reinforce, fix, or correct, mapped to the owning skills.
- `(assumption)` tags where measurement conditions limited confidence.

## Common pitfalls

- Changing the prompt set or competitors mid-stream, breaking comparability.
- Tracking opens/impressions vanity metrics instead of citation, SOV, and referral traffic.
- Measuring one engine and generalizing.
- Ignoring that personalization/location shift results — hold conditions steady and note
  them.
- Tracking without acting on the trends.

## Tool

Run your prompt set across AI engines and log brand/competitor mentions plus share of voice (engines enabled by API key; runs gracefully with none):

```bash
python scripts/test_prompts.py --selftest             # verify detection logic, no keys
python scripts/test_prompts.py --sample               # example prompts config
python scripts/test_prompts.py --input prompts.json --csv results.csv
```

Set OPENAI_API_KEY / ANTHROPIC_API_KEY / PERPLEXITY_API_KEY for the engines you want.

> Optional. The script only automates this step; it needs `python3` (standard library only, no install). No Python? Just follow the steps above manually.

## Related Skills

- **ai-visibility-audit** — the baseline and periodic deep dive this extends.
- **competitor-ai-analysis** — the share-of-voice method this operationalizes over time.
- **ai-referral-analytics** — the traffic side of measurement.
- **content-freshness** — often the response when tracked citations slip.
