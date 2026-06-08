---
name: author-authority
description: >-
  Build the author and expertise signals answer engines reward — named, credentialed
  authors, real bylines, author pages and Person schema, and demonstrated firsthand
  experience (E-E-A-T). Works for any business, B2B or B2C, product or service. Use when
  the request is to add author credibility, strengthen E-E-A-T, set up author bios or
  bylines, signal expertise to AI, or fix anonymous content that does not get cited. Pairs
  with structured-data (Person schema) and evidence-and-citations.
metadata:
  version: 0.1.0
---

# Author Authority

This skill builds the **expertise and trust signals** attached to *people*. Answer engines
weigh who is behind the content: named authors with real credentials and demonstrated
experience are cited far more than anonymous pages. This is the E-E-A-T lens — Experience,
Expertise, Authoritativeness, Trustworthiness — applied to make a brand's voices
recognizable and credible. It works for any business, B2B or B2C.

## When to use this skill

- Adding or strengthening author bylines, bios, and author pages.
- Signaling expertise and firsthand experience to AI.
- Setting up Person schema and author entities.
- Fixing anonymous or "staff"-bylined content that fails to earn citations.

## Before you start

Read `aeo-foundation.md` for the brand's real experts and authors, their credentials, and
any compliance needs (especially for YMYL topics — health, finance, legal). If it is
missing, point to the **aeo-foundation** skill.

## The signals

- **Real, named authors** — actual people, not "Admin" or "Team." A named author is the
  baseline E-E-A-T signal.
- **Demonstrated experience** — firsthand evidence: "we tested," "in our deployment,"
  original data, lessons from real work. Experience is hard to fake and disproportionately
  valued.
- **Credentials and relevance** — the author's qualifications and why they are credible on
  *this* topic, shown in the byline and bio.
- **Author pages** — a real page per author with bio, credentials, links to their work and
  professional profiles, marked up with Person schema and connected to the Organization.
- **Consistency** — the same author identity across the site and the web (profile links,
  `sameAs`), so the person is recognizable as an entity too.

## Workflow

1. **Assign real authors.** Replace generic bylines with named experts who actually have
   standing on the topic.
2. **Write credible bios.** For each author, a bio stating credentials, relevant
   experience, and topic authority; link their professional profiles.
3. **Build author pages + Person schema.** One page per author, marked up with Person
   schema (name, jobTitle, credentials, `sameAs`), linked from their articles and to the
   Organization (see **structured-data**).
4. **Surface experience in the content.** Add firsthand detail, original data, and
   "how we know this" so expertise is demonstrated, not just claimed.
5. **Handle YMYL carefully.** For health, finance, and legal topics, foreground qualified
   authors, review/medical-reviewer notes, and accurate sourcing — trust requirements are
   higher and so are the stakes.
6. **Keep identities consistent** across the site and external profiles.

## Output format

- **Author bylines and bios** ready to publish, with credentials and links.
- **Author-page** content and **Person schema** for each author.
- Notes on where to **add firsthand experience** to existing content.
- For YMYL: a note on required reviewer/credential signals.
- `(assumption)` tags on any credential to confirm.

## Common pitfalls

- "Staff" or anonymous bylines on content meant to be authoritative.
- Bios that list a name but no credentials or relevant experience.
- Claiming expertise without demonstrating experience (engines reward the shown work).
- Inconsistent author identities, so the person never becomes a recognized entity.
- Under-investing in author trust on exactly the YMYL topics that need it most.

## Related Skills

- **structured-data** — Person schema and author-to-Organization links.
- **entity-optimization** — authors as people-entities connected to the brand.
- **evidence-and-citations** — the data and quotes that demonstrate expertise.
- **digital-pr** — external coverage that builds an author's outside authority.
