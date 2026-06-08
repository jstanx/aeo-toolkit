# AEO Readiness Checklist

A concrete, testable checklist spanning the whole discipline. Use it for a fast readiness
pass or as the backbone of an audit. Each item maps to the skill that owns it; several can
be auto-checked with the tools noted. Aim for "yes" on the criticals first, then work down.

How to read it: **[critical]** items block citation outright; the rest raise the ceiling.

## 1. Crawler access — can engines reach you? (`ai-crawler-access`)
- [ ] **[critical]** robots.txt does not block retrieval bots (OAI-SearchBot, Claude-SearchBot, PerplexityBot). _Tool: `check_ai_crawlers.py`_
- [ ] **[critical]** CDN/WAF (e.g. Cloudflare) is not silently blocking AI crawlers. _Tool: `check_ai_crawlers.py --live`_
- [ ] A deliberate policy is set per bot category (training vs. retrieval vs. user-triggered).
- [ ] Important AI bots are verified by published IP ranges, not just user-agent.
- [ ] Logs confirm retrieval bots actually visit key pages. _Tool: `parse_crawler_logs.py`_

## 2. Retrievability — can engines read you? (`ai-retrievability`)
- [ ] **[critical]** Main content is in the server-rendered HTML (visible with JavaScript off).
- [ ] HTML is clean and semantic (one H1, logical H2/H3, real lists/tables).
- [ ] Pages load fast and return stable 200s (no timeouts/errors for bots).
- [ ] Internal linking connects pillars and clusters; no orphan pages.

## 3. Extractability — can engines lift an answer? (`answer-engineering`)
- [ ] Key sections lead with a 40-60 word, self-contained direct answer. _Tool: `score_answer_blocks.py`_
- [ ] Headings are phrased as the questions people actually ask.
- [ ] One question per section; passages make sense out of context.
- [ ] The most important answer sits near the top of the page (not the dead middle).
- [ ] Lists and tables are used for steps, sets, and comparisons.

## 4. Evidence — are claims cite-worthy? (`evidence-and-citations`, `claim-accuracy`)
- [ ] Specific, sourced statistics appear where claims are made.
- [ ] Original data or firsthand insight is present where possible.
- [ ] Expert quotes are attributed; claims link to authoritative sources.
- [ ] No unsupported superlatives or invented numbers (they backfire).
- [ ] Every checkable claim is verified; facts are consistent across pages.

## 5. Structured data — is it machine-parseable? (`structured-data`)
- [ ] Organization schema with `sameAs` on the home/about page. _Tool: `generate_schema.py`_
- [ ] Article + linked Person (author) schema on content.
- [ ] FAQPage schema where genuine Q&A appears on the page.
- [ ] Honest `dateModified` reflecting real updates.
- [ ] All schema validates and matches visible content.

## 6. Entity — does AI know who you are? (`entity-optimization`, `author-authority`)
- [ ] A crawlable entity home (About page) states the canonical facts.
- [ ] A complete, referenced Wikidata item exists (Wikipedia if genuinely notable).
- [ ] Core facts (name, founding, HQ, category) are identical across the web. _Tool: `check_entity_consistency.py`_
- [ ] Generic brand names are disambiguated (name + category).
- [ ] Content has named, credentialed authors (real bylines, author pages).

## 7. Authority & corroboration — do engines trust you? (`digital-pr`, `community-and-reviews`, `comparison-content`)
- [ ] The brand is mentioned across multiple independent, trusted sources (consensus).
- [ ] Presence on the review platforms engines cite for the category.
- [ ] Authentic presence in the communities engines pull from (e.g. Reddit/forums).
- [ ] Included accurately in third-party "best of"/alternatives/comparison content.
- [ ] Original data exists that others cite.

## 8. Freshness — is it current? (`content-freshness`)
- [ ] High-value pages are refreshed substantively on a cadence (not cosmetic re-dates).
- [ ] Time-sensitive facts (pricing, stats) are current.
- [ ] Pages that lost citations have been diagnosed and refreshed.

## 9. Per-engine tuning (the `*-optimization` skills)
- [ ] Priorities reflect the target engine (e.g. freshness/community for Perplexity;
      entity/encyclopedic for ChatGPT; organic+structure for Google AI Overviews;
      entity+YouTube for Gemini; accuracy+authority for Claude).

## 10. Forward-looking signals (`ai-capability-signaling`, `multimodal-aeo`)
- [ ] `llms.txt` published (low-cost). _Tool: `generate_llms_txt.py`_
- [ ] Markdown twins / copy-for-AI on priority pages.
- [ ] Transcripts and captions on all video/audio; VideoObject schema on video.

## 11. Measurement — can you prove it? (`ai-visibility-tracking`, `ai-referral-analytics`)
- [ ] A fixed prompt set is tracked across engines on a cadence. _Tool: `test_prompts.py`_
- [ ] Citation rate, mention rate, and share of voice are recorded over time.
- [ ] AI-referral traffic is captured in analytics (not lost in "Direct").
- [ ] Readiness is scored and mapped to a maturity stage. _Tool: `score_audit.py`_

---

**Success looks like:** the brand is cited (not just mentioned) for its high-value prompts
across multiple engines, share of voice trends up versus competitors, AI-referral traffic
grows, and what engines say about the brand is accurate. Track those outcomes, not the
checkbox count.
