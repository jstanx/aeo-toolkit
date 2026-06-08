---
name: multimodal-aeo
description: >-
  Optimize video, images, and audio so AI assistants and answer engines surface and cite
  them — transcripts and captions, VideoObject schema, YouTube presence (which Google and
  Gemini draw on heavily), descriptive image context, and podcast transcripts. Works for
  any business, B2B or B2C, product or service. Use when the request is to optimize video
  or YouTube or images or podcasts for AI answers, get multimedia cited by AI, make media
  AI-readable, or do multimodal AEO. Pairs with structured-data, answer-engineering, and
  gemini-optimization.
metadata:
  version: 0.1.0
---

# Multimodal AEO

AI answers increasingly include and cite **video, images, and audio** — and the engines
"understand" that media largely through its **text**: transcripts, captions, alt text, and
structured data. This skill makes a brand's multimedia surfaceable and citable by answer
engines. It works for any business, B2B or B2C. The honest core principle: engines mostly
read the *text around and inside* media, so the highest-leverage move is almost always to
give them clean, accurate text.

## When to use this skill

- Optimizing video or YouTube content to be cited in AI answers.
- Making images and diagrams understandable to multimodal models.
- Getting podcasts/audio surfaced via transcripts.
- Planning media that AI answer surfaces will pull from.

## Before you start

Read `aeo-foundation.md` for the audience, prompts, and which media the brand has or can
make. If it is missing, point to the **aeo-foundation** skill.

## The levers

1. **Transcripts and captions — non-negotiable.** Provide accurate, full transcripts and
   closed captions for every video and audio asset. Text is how engines parse, quote, and
   cite audiovisual content; without it, the asset is largely invisible to them.
2. **YouTube presence.** YouTube is a Google-owned surface that Google AI Overviews and
   Gemini draw on heavily. Use clear, question-shaped titles, thorough descriptions,
   chapters, and uploaded transcripts. Pairs with **gemini-optimization** and
   **google-ai-overviews-optimization**.
3. **VideoObject schema.** Mark up videos (name, description, thumbnail, uploadDate,
   transcript/caption URL) so machines understand them — see **structured-data** and the
   schema cookbook.
4. **Answer-first in the media itself.** State the answer early (the first lines of a video
   or its first chapter), and name chapters as the questions people ask — the same
   extractability logic as **answer-engineering**, applied to time-based media.
5. **Images and diagrams.** Use descriptive alt text, real captions, surrounding context,
   and meaningful filenames. Make the image genuinely answer a visual question; multimodal
   models read both the pixels and the text around them.
6. **Audio and podcasts.** Publish full transcripts and detailed show notes; that text is
   what gets indexed and cited, not the audio.
7. **Text twins.** Pair each major media asset with a written version (article, summary,
   or transcript page). Engines cite clean text most readily — see
   **ai-capability-signaling**.

## Workflow

1. **Inventory media** tied to high-value prompts (videos, key images/diagrams, podcasts).
2. **Add or fix transcripts/captions** for every audiovisual asset — accurate and complete.
3. **Optimize YouTube** items: question-shaped titles, full descriptions, chapters,
   uploaded transcripts.
4. **Mark up** videos with VideoObject and images with descriptive context.
5. **Apply answer-first** structure inside the media (early answers, question chapters).
6. **Publish text twins** for the assets that matter.
7. **Verify** the text is reachable and readable (see **ai-retrievability**).

## Output format

- A **media optimization plan**: which assets, what to add (transcripts, schema, twins).
- **Transcript/caption** status and gaps per asset.
- **YouTube** and **image** optimizations to apply.
- `(assumption)` tags where media inventory or platforms were unknown.

## Common pitfalls

- Audiovisual content with **no transcript** — effectively invisible to engines.
- Assuming engines "watch" or "look" rather than reading the surrounding text.
- Ignoring YouTube when targeting Google/Gemini answers.
- Thin alt text and missing captions on images that answer visual queries.
- No text twin, so clean media never becomes quotable text.

## Related Skills

- **structured-data** — VideoObject and image markup.
- **answer-engineering** — answer-first structure, applied to media.
- **gemini-optimization** / **google-ai-overviews-optimization** — the engines that lean on
  YouTube and visual results.
- **ai-capability-signaling** — text twins of media for clean ingestion.
