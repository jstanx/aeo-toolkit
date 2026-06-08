# Schema Cookbook for AEO

Reusable JSON-LD recipes that help answer engines parse content, understand entities, and
extract answers. The `structured-data` skill drives strategy; this file holds the
copy-adaptable markup. Use JSON-LD (not microdata/RDFa); validate before shipping.

## Principles

- **JSON-LD in a script tag**, placed in the page head or body.
- **Mark up what is true and visible** on the page — schema describes content, it does not
  replace it.
- **Connect entities**: an article references its author (Person), who is affiliated with
  the Organization. These links help engines verify credibility.
- **Validate** with a schema validator and a rich-results test before publishing.

## Priority types for AEO

1. **Organization** — anchors the brand entity (pair with `entity-optimization`).
2. **Article / BlogPosting** — content type, author, dates.
3. **Person** — author identity and credentials (E-E-A-T).
4. **FAQPage** — question/answer pairs engines can lift directly.
5. **Product**, **Review/AggregateRating**, **HowTo**, **BreadcrumbList** — as relevant.

## Recipes

### Organization (brand entity anchor)

```json
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "Acme Analytics",
  "url": "https://example.com",
  "logo": "https://example.com/logo.png",
  "description": "Self-serve product analytics for B2B SaaS teams.",
  "foundingDate": "2019",
  "sameAs": [
    "https://en.wikipedia.org/wiki/Acme_Analytics",
    "https://www.wikidata.org/wiki/Q000000",
    "https://www.linkedin.com/company/acme-analytics",
    "https://www.crunchbase.com/organization/acme-analytics"
  ]
}
```

`sameAs` is how you tell engines that all these profiles are the same entity — important
for recognition and disambiguation.

### Article with linked author and publisher

```json
{
  "@context": "https://schema.org",
  "@type": "BlogPosting",
  "headline": "How answer engines choose sources",
  "datePublished": "2026-01-15",
  "dateModified": "2026-06-01",
  "author": {
    "@type": "Person",
    "name": "Jordan Lee",
    "jobTitle": "Head of Research",
    "url": "https://example.com/team/jordan-lee",
    "sameAs": ["https://www.linkedin.com/in/jordanlee"]
  },
  "publisher": {
    "@type": "Organization",
    "name": "Acme Analytics",
    "logo": { "@type": "ImageObject", "url": "https://example.com/logo.png" }
  }
}
```

`dateModified` signals freshness; keep it honest and tied to substantive updates.

### FAQPage (directly extractable Q&A)

```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What is answer engine optimization?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Answer engine optimization is the practice of getting a brand cited and recommended inside AI-generated answers from assistants like ChatGPT and Perplexity."
      }
    }
  ]
}
```

Phrase questions the way people actually ask them; keep each answer a self-contained
40–60 words so it can be lifted whole.

### Nesting for a compound signal

You can nest an FAQPage inside an Article so the page reads as "an article that also
contains Q&A," which strengthens extraction confidence. Only do this when the FAQ content
genuinely appears on the page.

## Validation checklist

- [ ] Valid JSON-LD (no syntax errors), in a `script type="application/ld+json"` tag.
- [ ] Every marked-up fact appears in the visible page content.
- [ ] Organization has `name`, `url`, `logo`, `sameAs`.
- [ ] Articles link `author` (Person) and `publisher` (Organization).
- [ ] Dates are accurate; `dateModified` reflects real updates.
- [ ] Passes a schema validator and a rich-results test.
