# Category Entity — Creation & Editing Rules

> **Use this file as a system-prompt scaffold** when ERP calls an AI model to generate or edit an entry in `assets/categories.json`. Feed this entire file to the LLM before its JSON-generation turn.

---

## What a "Category" is

A **category** is a high-level content bucket for blog articles on a B2B static site. It:
- Appears at `/category/{slug}` as a landing page (hero + article grid + FAQ + CTA)
- Appears in the main nav and blog-list sidebar
- Maps to one or more ERP CMS parent-topics (so posts auto-route to it on deploy)
- Represents an **editorial expertise pillar**, not a product line

Categories are **few and stable** (4-6 per site). They're different from tags (many, granular, per-article). Different from product categories (future `assets/product-categories.json`).

---

## Output Contract

Every entry in `categories.json.categories[]` **must** satisfy this shape. AI generators MUST return valid JSON conforming to this.

### Required fields

| Field | Type | Rule |
|-------|------|------|
| `slug` | string | kebab-case, 3-20 chars, `[a-z0-9-]`, unique per site, no trailing `-` |
| `name` | string | 1-3 words, Title Case, no punctuation, e.g. `Manufacturing`, `Fabric Technology` |
| `description` | string | 1 sentence, 150-200 chars, used as fallback og:description |
| `icon` | string | Bootstrap Icons class (`bi-*`), e.g. `bi-gear-wide-connected` |
| `featured` | boolean | `true` for 2-3 flagship categories (shown on homepage), `false` otherwise |
| `parent_topic_keywords` | array<string> | 8-12 English keywords, lowercase, for ERP topic→category matching |
| `parent_topic_keywords_zh` | array<string> | 5-8 Chinese keywords (ERP CMS may have Chinese topics) |

### Optional — recommended for featured categories

| Field | Type | Rule |
|-------|------|------|
| `parent_topic_ids` | array<int> | ERP topic.id exact lock (highest priority when resolving) |
| `seo.title` | string | ≤ 60 chars, format `{Category} — {angle} \| {brand}`, primary keyword in first 30 chars |
| `seo.description` | string | 150-160 chars, primary keyword + B2B value prop + CTA verb |
| `seo.keywords` | string | 5-10 comma-separated, primary first, all lowercase |
| `seo.og_image` | string | absolute URL to 1200×630 image |
| `hero.badge` | string | optional uppercase pill text above H1 (e.g. `B2B MANUFACTURING`) |
| `hero.h1` | string | page H1, must contain primary keyword, 30-60 chars |
| `hero.subtitle` | string | 1-2 sentences supporting H1, 100-180 chars |
| `hero.cta_text` | string | button label, e.g. `Request a Quote` |
| `hero.cta_link` | string | relative path, e.g. `/contact-us` |
| `sections` | array<block> | ordered content blocks (see below) |

### Supported section block types

| `type` | Fields | When to use |
|--------|--------|-------------|
| `feature_grid` | `title`, `subtitle?`, `items[{icon, title, body}]` (3-6 items) | Explain what the category covers |
| `faq` | `title?` (default "FAQ"), `items[{q, a}]` (3-5 Q&A) | Pre-empt buyer questions |
| `cta_banner` | `heading`, `body`, `button_text`, `button_link` | Mid-page conversion prompt |
| `stat_row` | `items[{value, label}]` (3-4 stats) | Credibility numbers |
| `custom_html` | `html` (raw HTML string) | Escape hatch, use sparingly |

---

## Naming Rules

- **Don't**: `blog`, `articles`, `posts`, `content` (too generic — these are page types, not editorial topics)
- **Don't**: Product-line names (`Shirts`, `Hoodies`) — those belong in product-categories.json
- **Don't**: Time-bound names (`2024-trends`) — categories are evergreen
- **Do**: Editorial angle names: `Manufacturing` / `Fabric Technology` / `Industry Trends` / `Fishing Tips`
- **Do**: Audience angle names: `For Wholesalers` / `For Private Labels` (B2B segmentation)

---

## SEO Title Templates (for `seo.title`)

| Pattern | Example |
|---------|---------|
| `{Category} — {keyword angle} \| {brand}` | `Manufacturing — OEM & ODM Fishing Apparel Factory \| Runfish Apparel` |
| `{Category} Insights for {audience} \| {brand}` | `Fabric Technology Insights for Brand Owners \| Runfish Apparel` |
| `{Keyword question} — {Category} \| {brand}` | `How to Source UPF50+ Fabric — Fabric Technology \| Runfish Apparel` |

Never just `{Category} \| {brand}` — add the angle/keyword.

---

## Keyword Strategy

`parent_topic_keywords` drives ERP auto-routing. Coverage checklist:
- ✓ The 2-3 main English synonyms of the category theme
- ✓ Industry jargon the CMS writers actually use (`OEM`, `ODM`, `MOQ`, `sublimation`)
- ✓ B2B-intent verbs (`sourcing`, `wholesale`, `private label`)
- ✗ Generic words like `article` / `guide` / `post`
- ✗ Brand name (it's implied)

`parent_topic_keywords_zh` mirrors in Chinese for topics authored in 中文。Use industry-standard Chinese terminology (e.g. `制造` not `做`, `面料` not `布`).

---

## Good Minimal Example (slim entry, for non-featured category)

```json
{
  "slug": "industry-trends",
  "name": "Industry Trends",
  "description": "Market intelligence on fishing apparel demand, tournament sponsorships, and B2B retail shifts.",
  "icon": "bi-graph-up-arrow",
  "featured": false,
  "parent_topic_ids": [],
  "parent_topic_keywords": ["industry", "trends", "market", "business", "news", "report", "analysis", "icast", "expo"],
  "parent_topic_keywords_zh": ["行业", "趋势", "市场", "商业", "资讯", "报告"]
}
```

## Good Full Example (featured category with hero + sections)

See `categories.json.categories[0]` (`manufacturing`) in this site — canonical reference.

---

## After Editing — Build Step

Anyone (human or ERP AI) who edits `categories.json` must immediately run:

```bash
python3 build_site.py
```

This regenerates `/category/{slug}.html` from the manifest. Do NOT hand-edit category HTML — it gets overwritten on next build.

---

## ERP AI-Assist Workflow

When ERP wants to add/edit a category:

1. Read `rules/categories.md` (this file) into prompt
2. Read existing `assets/categories.json` so AI knows what's already defined
3. Ask AI to return JSON for the new/updated entry
4. Validate against required fields
5. Merge into `categories.json`
6. `git commit` + trigger `build_site.py`
7. Deploy
