# AI Crawlers Reference

The user-agent landscape for AI systems, and how to control access. This is the single
place to update crawler facts; other skills (notably `ai-crawler-access`) link here.

**Why three categories matter.** An AI bot fetches for one of three reasons, and the
reason changes what blocking it costs you:

- **Training crawlers** collect content to train future models. Blocking them keeps your
  content out of model weights but generates no referral traffic either way.
- **Retrieval / search crawlers** fetch in real time to ground answers (RAG). These are
  the ones that produce live citations and referral clicks — usually the most important
  to allow.
- **User-triggered fetchers** retrieve a page on demand when a user asks the assistant
  about it. Blocking them can prevent live citation of pages a user explicitly requests.

## Major user agents

Verify the current official string and behavior from each provider's documentation before
relying on it — these evolve. Categories below reflect each bot's primary purpose.

| Provider | Training | Retrieval / search | User-triggered |
|---|---|---|---|
| OpenAI | `GPTBot` | `OAI-SearchBot` | `ChatGPT-User` |
| Anthropic | `ClaudeBot` | `Claude-SearchBot` | `Claude-User` |
| Perplexity | (none declared) | `PerplexityBot` | `Perplexity-User` |
| Google | `Google-Extended` (a robots token, trains Gemini; not a separate crawler) | Googlebot powers AI Overviews | Googlebot |
| Apple | `Applebot-Extended` (training opt-out token) | `Applebot` | `Applebot` |
| Meta | `Meta-ExternalAgent` | — | — |
| ByteDance | `Bytespider` | — | — |
| Common Crawl | `CCBot` (open dataset reused by many LLMs) | — | — |

Notes:
- **Google-Extended** and **Applebot-Extended** are *robots.txt tokens* controlling
  training use, not distinct crawlers. Blocking them does not remove you from Search.
- **Googlebot is unusual**: it renders JavaScript. Most dedicated AI crawlers do **not**
  execute JavaScript (see `ai-retrievability`).
- Some crawlers have been reported to ignore robots.txt or rotate identities. Treat
  robots.txt as cooperative control, not enforcement; use server/WAF rules when you need
  hard blocking.

## Controlling access

**robots.txt** is the first lever. A common posture — allow retrieval and user-triggered
bots (you want citations) while deciding separately on training:

```
# Allow real-time retrieval / citation
User-agent: OAI-SearchBot
Allow: /
User-agent: Claude-SearchBot
Allow: /
User-agent: PerplexityBot
Allow: /

# Training: allow to feed future models, or disallow to opt out
User-agent: GPTBot
Allow: /
User-agent: Google-Extended
Allow: /
```

**WAF / CDN.** robots.txt is advisory. For bots that ignore it, or to enforce a policy,
use firewall/CDN rules (e.g. at the CDN edge). Note that some platforms now block AI bots
by default on new sites — if citations matter, confirm your CDN is not silently blocking
retrieval crawlers.

**Verification.** Bad actors spoof user-agent strings. Where a provider publishes official
IP ranges, verify a bot by confirming its IP belongs to the published range (and/or
reverse-DNS) before allowing it on the strength of its user-agent alone.

## Decision summary

| Goal | Training crawlers | Retrieval crawlers |
|---|---|---|
| Maximize AI citations & referrals | Allow | Allow |
| Want citations, avoid training use | Disallow | Allow |
| Keep content out of AI entirely | Disallow | Disallow (accepts zero AI visibility) |
