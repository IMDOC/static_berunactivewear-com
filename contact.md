---
slug: contact
domain: berunactivewear.com
page_type: landing
primary_keyword: custom activewear inquiry
route: A
---

# Contact Berun Active Wear — Get a Quote Within 1 Business Day

> Step 4 complete — 5 sections, all rhythm + content filled.

## 板块 1: Hero — Start Your Custom Activewear Project
- **AIDA**: A (Attention)
- **Trust 维度**: —（contact Hero 不承载 trust 证据，仅导航信号）
- **rhythm**: full-bleed hero
- **高度**: 50vh
- **背景**: hero-factory-bg.webp with dark overlay (rgba(0,0,0,0.55))
- **bg_alternation**: dark
- **process**: Compact hero — exists only to confirm intent and push visitor to form below. No product shots, no trust badges. Sub names Anna + SLA. No CTA buttons (form is S2 immediately below).
- **内容**:
  - **eyebrow**: CONTACT US
  - **H1**: Start Your Custom Activewear Project
  - **Sub**: Send your tech-pack, request a sample, or describe what you need. Anna from our sourcing team replies within one business day.
  - **CTA**: none (form is right below)

## 板块 2: Inquiry Form + Contact Info — Submit Your Inquiry
- **AIDA**: A (Action — page 核心转化板块)
- **Trust 维度**: 专业 + 流程（named person + SLA + multi-channel）
- **rhythm**: standard
- **高度**: 100vh
- **bg_alternation**: white (#FFFFFF)
- **process**: Split layout 60/40 — left = form, right = 4 contact cards. Form uses form.lianf.com API with honeypot spam protection. Submit button "Send Your Inquiry" red full-width. Below button: privacy note. Right-side cards each have icon + channel name + value + micro-copy.
- **内容**:
  - **H2**: Submit Your Inquiry
  - **layout**: split 60/40 (desktop), stacked form-first (mobile)
  - **form_id**: inquiry-form
  - **form_api**: https://form.lianf.com
  - **form_domain**: berunactivewear.com
  - **honeypot**: `<input type="text" name="website" style="display:none" tabindex="-1">`
  - **tracking_js**: pageLoadTime (window load timestamp) + submission_time (submit click timestamp) + page_url (window.location.href)
  - **fields**:
    - Full Name | text | required | placeholder: "Your full name"
    - Email Address | email | required | placeholder: "you@company.com"
    - Company Name | text | required | placeholder: "Your company or brand name"
    - Order Type | select | required | options: "Select order type..." (disabled default) / OEM Cut-and-Sew / ODM / Private Label / Small-Batch Sampling / Team Customization / Other
    - Message | textarea | required | placeholder: "Describe your project — quantities, styles, timeline, or attach a tech-pack below." | rows: 5
    - File Upload | file | optional | label: "Attach tech-pack or reference files (PDF, AI, ZIP — max 10 MB)" | accept: .pdf,.ai,.zip,.png,.jpg
  - **submit_button**: "Send Your Inquiry" | style: red (#DC2626), full-width, rounded
  - **below_button**: "Your information is kept confidential. We never share your data with third parties."
  - **contact_cards** (right side, 4 cards):
    - **Email**: sales@berunactivewear.com | link: mailto:sales@berunactivewear.com | micro: "For spec sheets, tech-packs, and formal inquiries."
    - **Phone**: +86-159-0277-8636 | link: tel:+8615902778636 | micro: "Mon–Fri, 9 AM – 6 PM (GMT+8)."
    - **WhatsApp**: Chat with Anna, Sales Manager | link: https://wa.me/8615902778636 | micro: "Fastest channel for quick questions."
    - **Response SLA**: Within 1 business day | micro: "Urgent? Call or WhatsApp directly."

## 板块 3: What Happens After You Inquire — Inquiry-to-Production Timeline
- **AIDA**: I + T (Interest + Trust — sets expectations, reduces anxiety)
- **Trust 维度**: 流程（transparent 4-step timeline with real numbers）
- **rhythm**: standard
- **高度**: auto, padding 5rem top/bottom
- **bg_alternation**: #FAF7F2 (warm tint)
- **process**: Horizontal 4-step timeline — each step is icon + name + one-line description + duration badge. No paragraphs, no branching flowcharts. All numbers from §3.3.
- **内容**:
  - **H2**: What Happens Next
  - **Sub**: From inquiry to production in four steps.
  - **timeline** (4 steps, horizontal):
    - **Step 1**: Spec Review | "We review your requirements and confirm feasibility." | badge: "1 business day"
    - **Step 2**: MOQ Split + FOB Quote | "Per-size quantity breakdown and landed cost estimate." | badge: "2–3 days"
    - **Step 3**: Sample Production | "One piece per sample, fabric-on-stock styles." | badge: "5–12 working days"
    - **Step 4**: Bulk Production | "Cut-and-sew to your approved sample and spec." | badge: "35–42 days"

## 板块 4: Quick Reference — Key Facts
- **AIDA**: T (Trust — last-second reassurance)
- **Trust 维度**: 专业 + 认证（hard numbers + cert count）
- **rhythm**: data-wall
- **高度**: auto, compact strip (80px desktop)
- **bg_alternation**: white (#FFFFFF)
- **process**: 4 stat cards in a single horizontal row. Large number top, label below. No expanding cards, no "learn more" links. All numbers from §3.3.
- **内容**:
  - **H2**: none (compact strip, no title)
  - **stats** (4 cards, horizontal):
    - "300" | "MOQ per SKU" | note: "split XS–XXL"
    - "USD 45" | "Sample fee" | note: "1 piece"
    - "35–42" | "Days to bulk" | note: "OEM standard"
    - "5" | "Certifications on file" | note: ""

## 板块 5: CTA Banner — Prefer to Talk First?
- **AIDA**: A (Action — catches bottom-of-page non-submitters)
- **Trust 维度**: —（pure action, no proof）
- **rhythm**: mid-cta
- **高度**: 30vh
- **bg_alternation**: dark (#1F2937)
- **process**: Dark background banner. Catches visitors who scrolled past form without submitting. CTA links to Anna's WhatsApp with pre-filled message. Phone number as secondary plaintext.
- **内容**:
  - **H2**: Prefer to Talk First?
  - **Sub**: Book a 30-minute sourcing call with our engineering lead.
  - **CTA**: "Book a Call" | link: https://wa.me/8615902778636?text=Hi%20Anna%2C%20I%27d%20like%20to%20book%20a%20sourcing%20call. | style: red (#DC2626) button
  - **secondary**: Anna, Sales Manager · +86-159-0277-8636
