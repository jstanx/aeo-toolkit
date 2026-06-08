---
name: claim-accuracy
description: >-
  Make content factually accurate and internally consistent so answer engines trust and
  cite it — verify claims, source them, keep facts consistent across pages and the web,
  cut overclaims, and correct what AI gets wrong about a brand. Works for any business,
  B2B or B2C, product or service. Use when the request is to fact-check content for AI,
  fix inaccuracies or overclaims, ensure factual consistency for AEO, improve
  trustworthiness, or correct AI misrepresentations of a brand. Pairs with
  evidence-and-citations and entity-optimization.
metadata:
  version: 0.1.0
---

# Claim Accuracy

Answer engines behave like **accuracy and consensus machines**: they favor claims they can
verify and corroborate, and they deprioritize unsupported or overstated assertions.
Accuracy is therefore not just ethics — it is an AEO signal. This skill makes a brand's
content verifiable, internally consistent, and free of overclaims, and fixes the cases
where engines repeat something false about the brand. It works for any business, B2B or
B2C, and pairs tightly with **evidence-and-citations** (adding proof) and
**entity-optimization** (consistent facts).

## When to use this skill

- Fact-checking content meant to be cited by AI.
- Removing overclaims and unsupported assertions that engines discount.
- Reconciling facts that differ across a brand's pages or profiles.
- Correcting inaccurate or outdated things AI assistants say about the brand.

## Before you start

Read `aeo-foundation.md` for the canonical facts, claims, and any compliance constraints
(especially YMYL — health, finance, legal). If it is missing, point to the
**aeo-foundation** skill.

## Principles

- **Accuracy is a trust signal.** Verifiable, correct content is favored; a detectable
  error or overclaim erodes how readily engines cite the source.
- **Support every strong claim.** Unsupported confidence backfires — pair claims with a
  source, a statistic, or a clear basis (see **evidence-and-citations**), or soften them.
- **Be consistent everywhere.** The same fact should read the same across your pages and
  your off-site profiles; contradictions inject doubt and weaken entity recognition.
- **No hype inflation.** "Best," "leading," "guaranteed," and invented numbers without
  backing are liabilities, not assets.
- **Correct, transparently.** When something changes or was wrong, fix it and date it.

## Workflow

1. **Inventory claims.** Pull every checkable assertion — numbers, superlatives,
   comparative statements, dates, capabilities, guarantees.
2. **Verify each.** Confirm against a primary or authoritative source. Cite it, correct it,
   or soften it. Anything you cannot support gets reworded or removed.
3. **Check internal consistency.** Ensure the same facts (pricing, dates, capabilities,
   results) match across all of the brand's own pages.
4. **Check external consistency.** Reconcile against the brand's other profiles and
   listings — hand the cross-web check to **entity-optimization** (and its consistency
   tool).
5. **Strip overclaims.** Replace unbacked superlatives and vague boasts with specific,
   supported statements — or cut them.
6. **Detect and fix AI misrepresentations.** Test what the major engines currently say
   about the brand (see **ai-visibility-audit**); for each error, fix the upstream source
   the engine is likely drawing on (your page, a profile, a third-party listing) and, where
   possible, the authoritative record.
7. **Keep a source of truth.** Maintain the canonical facts in `aeo-foundation.md` so future
   content stays consistent.

## Output format

- A **claims audit**: each checkable claim marked verified / needs-source / overclaim, with
  the fix.
- **Inconsistencies** found across pages or profiles, and how to reconcile them.
- **AI misrepresentations** observed, with the upstream source to correct for each.
- `(assumption)` tags where a fact could not be verified.

## Common pitfalls

- Superlatives and invented numbers with no backing — discounted by engines.
- Stale statistics or dates that make a page demonstrably wrong.
- The same fact stated differently on different pages.
- Ignoring what AI already says incorrectly about the brand.
- "Fixing" content while leaving the third-party source of the error untouched.

## Related Skills

- **evidence-and-citations** — the sources and data that turn a claim into a supported one.
- **entity-optimization** — consistent canonical facts across the web.
- **ai-visibility-audit** — surfaces what engines currently say (and get wrong).
- **aeo-foundation** — the source of truth for the brand's facts and claims.
