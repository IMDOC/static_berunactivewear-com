# Tag Entity — Creation & Editing Rules

> **Use as AI prompt scaffold** when ERP generates/edits entries in `assets/tags.json`.

---

## What a "Tag" is

A **tag** is a short, keyword-level content label that sits below category in granularity. It:
- Appears at `/tag/{slug}` as an auto-generated aggregation page
- Gets rendered as a pill on blog cards + article pages
- Matches article meta keywords via `aliases` (handles writing variations)
- Stays short and reusable across many articles

Tags are **many** (10-40 per site). Different from categories (few, structural). Different from keywords (SEO-only, not a page).

---

## Output Contract

Every entry in `tags.json.tags[]`:

### Required fields

| Field | Type | Rule |
|-------|------|------|
| `slug` | string | kebab-case, 2-12 chars, `[a-z0-9-]`, unique. **Short**: `oem`, `upf50`, `moq` |
| `name` | string | 1-2 words, display form, can have `+` or `&` (e.g. `UPF50+`, `OEM & ODM`) |
| `description` | string | 1 sentence, 100-150 chars, used on tag page + og:description |
| `aliases` | array<string> | 3-6 variations the article meta might use, lowercase, include synonyms and acronym/phrase pairs |

### Optional

| Field | Type | Rule |
|-------|------|------|
| `featured` | boolean | true = show in sidebar tag cloud |
| `related_tags` | array<string> | sibling tag slugs shown on tag page |

---

## Naming Rules

- **Short**: ≤ 12 chars for slug, ≤ 15 chars for name. Long = it's probably a keyword phrase, not a tag.
- **No stop words**: `the-fishing-guide` → `fishing-guide` (drop `the`)
- **No category overlap**: if `Manufacturing` is a category, don't also have a `manufacturing` tag
- **Abbreviate industry terms**: `oem` / `odm` / `moq` / `qc` / `upf50`
- **One per concept**: not both `upf` and `upf-protection` — merge via `aliases`

---

## Alias Strategy

Aliases are the **fuzzy match layer** between article meta and registered tags. Each alias is lowercase, no punctuation (other than `+`), reflects how writers/AI might naturally write the concept.

For tag `oem`, good aliases:
```json
["oem manufacturing", "fishing apparel oem", "oem fishing clothing", "oem fishing shirts"]
```

For tag `upf50`:
```json
["upf50+", "upf 50", "upf50 protection", "sun protection", "upf 50+"]
```

---

## Good Example

```json
{
  "slug": "private-label",
  "name": "Private Label",
  "description": "Private-label branding, custom tagging, and label compliance articles.",
  "aliases": ["private label fishing clothing", "private label fishing apparel", "custom label"]
}
```

---

## After Editing

Run `python3 build_site.py` — regenerates all `/tag/{slug}.html`.

## ERP AI-Assist Workflow

Same pattern as categories.md: inject this file + current `tags.json` → ask AI to return new tag entry → append → rebuild.
