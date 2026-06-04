# Author Entity — Creation & Editing Rules

> **Use as AI prompt scaffold** when ERP generates/edits entries in `assets/authors.json`.

---

## What an "Author" is

An **author** is a real-person byline for blog articles. It:
- Appears at `/author/{slug}` as a profile page (bio + articles + expertise)
- Is linked from every article byline (`<a rel="author" href="/author/{slug}">`)
- Is matched to articles via `name` + ERP's `picking_strategy`
- Represents **editorial authority** for Google E-E-A-T

Authors are **1-3 per site** (not more — dilutes authority). Each author must be a **real human name**.

---

## Output Contract

### Required fields

| Field | Type | Rule |
|-------|------|------|
| `slug` | string | kebab-case of name, unique, 3-20 chars |
| `name` | string | Real person name (first only OR first + last), no titles/prefixes |
| `title` | string | Job title, 30-60 chars, specific: `Content Director & Fishing Apparel Specialist` |
| `bio_short` | string | 1 sentence, 120-180 chars, used in hero + og:description |
| `bio_long` | string | 2-3 paragraphs, real first-person tone, specific projects/years/places |
| `expertise_tags` | array<string> | 4-8 slugs matching the category expertise_match system |
| `email` | string | Contact email (can be shared sales@) |
| `avatar_url` | string | `/assets/images/authors/{slug}.webp` (AI headshot 1:1) |
| `page_url` | string | `/author/{slug}` |
| `featured` | boolean | `true` for the default/founder author |

---

## Author Naming — HARD RULES (E-E-A-T)

**REJECT**:
- ❌ `Editorial Team` / `{Brand} Team` / `Admin`
- ❌ Brand name as author (`Runfish Apparel`)
- ❌ Phone numbers, email handles, generic labels
- ❌ Non-human entities (`AI Writer`, `Bot`)

**ACCEPT**:
- ✓ Real first name: `Allen`, `Michael`, `Sarah`
- ✓ First + last: `Sarah Johnson`, `Michael Chen`, `Jake Morrison`
- ✓ For Chinese brands going global: English names (buyers respond better)

---

## bio_long Quality Bar

Must **feel like a real person wrote it**:
- Specific years of experience (`15+ years offshore fishing`)
- Specific places (`Gulf Coast to Alaska`, `Guangzhou factory floor`)
- Specific accomplishments (`60+ pro guides interviewed`, `500+ brands served`)
- Written in first-person or editorial voice, not corporate speak
- No clichés: avoid `passionate`, `dedicated`, `leveraging synergies`

---

## expertise_tags — Match to categories

Pull from category keywords or tags. Used by `batch_blog_auto_optimized_deploy` Step 2 (`picking_strategy: expertise_match`) to auto-assign the right author to new articles.

Example for a factory-side author: `["oem", "odm", "manufacturing", "fabric-technology", "quality-control", "moq"]`
Example for a field-test author: `["fishing-tips", "tournament", "field-testing", "saltwater-durability"]`

Make expertise_tags **non-overlapping across authors** — so ERP can unambiguously route articles.

---

## Good Example

See current `authors.json.authors[]` in this site (Allen, Jake Morrison) — canonical two-author B2B-angler setup.

---

## After Editing

1. Run `python3 build_site.py` — regenerates `/author/{slug}` article list
2. Ensure `/assets/images/authors/{slug}.webp` exists (use `/ai-image-gen` if not)

## ERP AI-Assist Workflow

Inject this file + current authors.json → ask AI for new author entry (matching an uncovered expertise angle) → ensure name passes E-E-A-T rules → merge → rebuild.
