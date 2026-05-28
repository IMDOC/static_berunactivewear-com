---
slug: cycling-apparel-manufacturer
domain: berunactivewear.com
page_type: landing
primary_keyword: cycling apparel manufacturer
route: /cycling-apparel-manufacturer
---

# Cycling Apparel Manufacturer for DTC Brands and Amateur Race Teams

> Italian-source chamois. ΔE ≤1.5 within-batch sublimation. Full 6-SKU kit from one factory in one PO. Custom cycling jerseys, bib shorts with multi-density chamois, long-sleeve thermal, bib tights, wind vests, and warmer bundles cut-and-sewn under one project manager. MOQ 300 baseline per SKU, 220 cross-SKU one PO under the Cycling Team Pack.

## S1: Hero (C+D) [full-bleed hero]

**Eyebrow**: "CYCLING APPAREL · FULL SUBLIMATION · 6-SKU TEAM KIT"

**H1**: "Cycling Apparel Manufacturer for DTC Brands and Amateur Race Teams"

**Sub**: "Italian-source chamois. ΔE ≤1.5 within-batch sublimation. Full 6-SKU kit from one factory in one PO."

**Stats bar** (brand-red `|` divider, 4 items):
- Italian-source chamois · 3-density 80/60/40 kg/m³
- ΔE ≤ 1.5 within-batch sublimation
- 6-SKU full kit · one PM · one PO
- MOQ 300 baseline · 220 cross-SKU Team Pack

**CTA pair**:
- Primary (red solid): "Send Your Cycling Tech-Pack or Design Brief" → `#inquiry-form`
- Ghost outline: "Build Your Cycling Team Kit" → `#inquiry-form` (JS pre-fills message: "I'm organizing a team kit for [X] riders. I need pricing for jersey / bib / long-sleeve / tight / vest / warmers — circle all that apply. Our season starts [date].")

**Right inset card** (desktop only, hidden on mobile):

Heading: "Why cycling brands and teams choose Berun"

Bullets:
- Italian-source multi-density chamois — not Asian commodity foam
- ΔE ≤ 1.5 on every piece in the same PO, spectrophotometer-verified
- Dedicated sublimation line tuned for cycling polyester + UV-stable ink
- Single PM + single dye batch across all 6 SKUs
- Multi-season delivery: summer, shoulder, winter under one spec
- OEM, ODM, private label, Cycling Team Pack — four paths

**Image slot**: Full-bleed background, dark #1F2937 overlay at 60% opacity. Reuse `assets/images/hero-factory-bg.webp`. Right inset card has no image.

**Style**: 50-60vh min-height. Left 55% text column. Right 45% white card with 8px radius, 1px border. Mobile: full single column, right inset hidden via `display:none`, CTA stacks full-width. Stats bar uses brand-red `|` dividers.

---

## S2: Cycling Subcategory Cards (C+D) [card-grid image-top]

**H2**: "Custom Cycling Jerseys, Bib Shorts, Long-Sleeve Thermal, Tights, Vests and Warmers We Cut and Sew"

**Sub**: "Six cycling SKUs that build one annual kit. Race-fit cut, full-sublimation construction."

**Card 1: Cycling Jersey (Short-Sleeve, Race Fit)**
- Description: "Front zip, 3 rear cargo pockets, silicone gripper hem, full-sublimation panel construction."
- Tags: `race-fit aero-cut` · `full sublimation` · `110-140 GSM poly-elastane`
- Link: "Spec a jersey →" → `#inquiry-form`

**Card 2: Cycling Bib Shorts (Italian-Source Chamois)**
- Description: "Italian-source chamois, 3-density 80/60/40 kg/m³ zoning, 12-panel flatlock attachment."
- Tags: `Italian chamois` · `3-density 80/60/40` · `12-panel flatlock`
- Link: "Spec a bib short →" → `#inquiry-form`

**Card 3: Long-Sleeve / Thermal Jersey**
- Description: "Brushed-back fleece, windproof front panel, optional merino-blend body."
- Tags: `220-260 GSM brushed` · `windproof front` · `merino option`
- Link: "Spec a long-sleeve →" → `#inquiry-form`

**Card 4: Bib Tights / Winter Tights**
- Description: "Roubaix thermal fabric, windproof front, ankle zipper + reflective tab, chamois integrated."
- Tags: `Roubaix thermal` · `windproof front` · `ankle zip + reflective`
- Link: "Spec a winter tight →" → `#inquiry-form`

**Card 5: Cycling Vest / Wind Gilet**
- Description: "Windproof front + mesh back, packable into rear pocket, drop-tail cut for riding position."
- Tags: `windproof front + mesh back` · `pack-down` · `drop-tail cut`
- Link: "View wind-shell construction →" → `/products/outdoor-running#fabric`

**Card 6: Arm + Leg Warmers + Skull Cap (Cyclist Add-Ons)**
- Description: "Thermal Roubaix arm + leg warmers + skull cap, silicone gripper bands, team-kit add-on bundle."
- Tags: `thermal Roubaix` · `silicone gripper` · `3-piece bundle`
- Link: "View cycling socks →" → `/products/accessories#subcategories`

**Image slot**: 6 grapesjs `random-image` per build-rules §5 with onerror three-tier fallback:
- Card 1: `query=cycling-jersey&w=640&h=400`
- Card 2: `query=cycling-bib-shorts&w=640&h=400`
- Card 3: `query=cycling-long-sleeve-jersey&w=640&h=400`
- Card 4: `query=cycling-tights&w=640&h=400`
- Card 5: `query=cycling-wind-vest&w=640&h=400`
- Card 6: `query=cycling-arm-warmers&w=640&h=400`

**Style**: White bg #FFFFFF. Cards: white bg, 8px radius, 1px border #E5E7EB, hover translateY(-3px) + shadow. Image on top ~60% of card height. 3-column desktop / 2-column tablet / 1-column mobile. Section padding `clamp(60px, 8vw, 100px)`.

---

## S3: Cycling Discipline Matrix (C+D) [card-list image-side alternating]

**H2**: "Custom Cycling Apparel Spec'd to Your Discipline: Road, Gravel, MTB, Triathlon, Indoor, and Endurance Gran Fondo"

**Sub**: "Gravel grit. Road aero. MTB abrasion. Triathlon hydrodynamics. We spec the fabric to the discipline."

**Card 1: Road Racing** (image left, text right)
- Profile: "High-speed aero, group ride pelotons."
- SKU mix: "Race-fit jersey + bib shorts + arm warmers."
- Fabric: "110 GSM aero-knit polyester, race-cut, low-pad chamois for short-effort."

**Card 2: Gravel / Adventure** (image right, text left)
- Profile: "Endurance-bias, mixed surface, longer rides."
- SKU mix: "Relaxed-fit jersey + bib short (higher chamois density) + vest."
- Fabric: "140 GSM textured polyester, added side pocket on jersey, reflective accent at lower back."

**Card 3: Mountain Biking (MTB / Enduro)** (image left, text right)
- Profile: "Trail abrasion, baggy fit over chamois liner."
- SKU mix: "Loose-fit jersey + technical baggy short (separate chamois liner) + arm warmers."
- Fabric: "160 GSM ripstop polyester, 30,000+ Martindale abrasion cycles, ventilation panels."

**Card 4: Triathlon** (image right, text left)
- Profile: "Swim-to-bike-to-run hydrodynamic, fast transitions."
- SKU mix: "Tri suit (one-piece) + sleeveless jersey + minimal-pad chamois."
- Fabric: "90 GSM compression poly-elastane, quick-dry surface, sub-1cm-thickness chamois."

**Card 5: Indoor Cycling (Zwift / Smart Trainer / Spin Class)** (image left, text right)
- Profile: "High-sweat sustained effort, no wind."
- SKU mix: "Ultra-light sleeveless jersey + minimal-pad bib + sweatband."
- Fabric: "90 GSM mesh polyester, sweat-wicking, grip-pattern bib hem stays put on trainer."

**Card 6: Endurance / Gran Fondo / Charity Ride** (image right, text left)
- Profile: "4-8 hour rides, mixed weather, sponsor visibility, group identity."
- SKU mix: "Full 6-SKU kit with sponsor logos across every piece."
- Fabric: "140 GSM all-weather polyester + Ultra-Endurance 3-density chamois + reflective accents."

**Image slot**: 6 grapesjs images alternating left/right:
- Card 1: `query=road-cycling-peloton&w=480&h=360`
- Card 2: `query=gravel-cycling-adventure&w=480&h=360`
- Card 3: `query=mountain-bike-trail&w=480&h=360`
- Card 4: `query=triathlon-cycling&w=480&h=360`
- Card 5: `query=indoor-cycling-trainer&w=480&h=360`
- Card 6: `query=gran-fondo-charity-ride&w=480&h=360`

**Style**: Tint bg #FAF7F2. Horizontal card 100% width per card, image 40% one side / text 60% other, alternating direction (1=image-left, 2=image-right, 3=image-left, 4=image-right, 5=image-left, 6=image-right). Mobile: image always on top, text below, full-width stack. 32px gap between cards. Subtle shadow on each card. Section padding `clamp(60px, 8vw, 100px)`.

---

## S4: Chamois Pad Engineering (C+D) [split table+diagram, page-unique anchor]

**H2**: "Italian-Source Chamois Engineering for Cycling Bib Shorts Manufacturing"

**Sub**: "The make-or-break component. We source the chamois grades Italian and Portuguese factories use."

**Content (left 55% — chamois spec comparison table)**:

| Chamois Spec | Berun Cycling Standard | Industry Commodity |
|---|---|---|
| Supplier source | Italian-source (Cytech / Elastic-Interface affiliated, Tier-1 European supplier) | Generic Asian commodity ($4-6/pad) |
| Density zoning | 3-density gradient: 80 kg/m³ sit-bone / 60 kg/m³ perineum / 40 kg/m³ edge | Single-density ~50 kg/m³ throughout |
| Gender mold | Separate male / female / unisex molds, anatomically distinct | One-pad-fits-all unisex |
| Cover fabric | 80-denier suede-coated polyester, anti-bacterial, 30,000+ Martindale cycles | 40-denier commodity polyester |
| Attachment method | 12-panel flatlock seam, full perimeter sewn-in to bib body | Perimeter glue + chain-stitch at 4 points |
| Endurance test | 6-hour continuous-ride simulation, zero pressure-point fail criterion | None (no in-house testing) |
| Sit-bone landing | Anatomical sit-bone pocket molded into pad | Flat foam, no landing pocket |

**Below table**: "Available in 3 chamois series for different ride durations:"
- **Sprint chamois** — ≤2 hr rides (crit racing, indoor cycling) — thinner, low-profile
- **Endurance chamois** — 2-5 hr rides (road racing, gravel rides) — standard 3-density
- **Ultra-Endurance chamois** — 5-12 hr rides (Gran Fondo, multi-day tours) — thicker sit-bone density + extended sit-bone landing

**Content (right 45%)**: Chamois cross-section technical illustration. Caption: "Chamois cross-section showing 3-density zones (80 / 60 / 40 kg/m³) with 80-denier suede-coated cover and 12-panel flatlock perimeter attachment."

**Image slot**: 1 technical illustration SVG right side (chamois cross-section). Fallback: grapesjs `query=cycling-chamois-pad&w=720&h=560`, then `.img-ph` placeholder per build-rules §5.

**Style**: White bg. Split 55/45 desktop, stack mobile (table first, diagram second). Table: striped rows, header in #1F2937 with white text, body alternating white / #FAF7F2; "Berun Cycling Standard" column subtly tinted brand-red light wash. Below 480px viewport: table horizontal scroll fallback. Diagram: 8px radius, subtle border, brand-yellow #FCD34D accent labels for the 3 density numbers. Section padding `clamp(80px, 10vw, 120px)`.

---

## S5: Three Cycling Failure Modes → Three Engineered Fixes (C+D) [zigzag]

**H2**: "Three Cycling Apparel Failure Modes We Engineer Out"

**Sub**: "Three things our new customers showed us after their last vendor burned them."

**Row 1: Chamois Bunching and Saddle Sores** (image left, text right)
- **Pain h3**: "Chamois bunched, cover ripped, three riders got saddle sores"
- **Pain body**: "Pelotonia 80-rider charity team. Chamois bunched at the inseam on the first training ride. One cover ripped at hour two. Three riders developed saddle sores by day one of the 200-mile event. Coordinator refunded $4,800."
- **Solution h3**: "Our fix"
- **Solution body**: "Italian-source chamois (Cytech / Elastic-Interface affiliated). 3-density 80/60/40 kg/m³. Gender-specific molds. 12-panel flatlock seam — no glue, no perimeter-only stitching. 80-denier suede-coated cover. 6-hour endurance test on every pre-bulk sample."

**Row 2: Within-Batch Sublimation Color Drift** (image right, text left)
- **Pain h3**: "Twelve teammates ordered, three came back the wrong shade"
- **Pain body**: "Road racing club ordered 12 jerseys + 12 bibs in team navy with sponsor logos. Season-opener photo: 9 true navy, 2 grey-navy, 1 lavender. Sponsor logo drifted 2-3mm on 4 jerseys. Energy-drink sponsor cancelled the $1,200 contribution citing brand-standards failure."
- **Solution h3**: "Our fix"
- **Solution body**: "ΔE ≤ 1.5 within-batch — spectrophotometer-verified on every piece pre-shipment (different from cross-PO drift on knit-stretch sister pages). ±1mm registration tolerance on sponsor logos crossing panel seams. Dedicated sublimation line tuned for cycling polyester. UV-stable disperse-dye ink. Pre-bulk batch sample (1 jersey + 1 bib + 1 warmer) shipped for sign-off before bulk runs."

**Row 3: Four-Vendor Patchwork for One Team Kit** (image left, text right)
- **Pain h3**: "Four vendors, $8,500, six months, sixty percent unhappy"
- **Pain body**: "Amateur club organizer assembled the 2024 kit via 4 vendors: Vietnam jerseys + bibs, Yiwu vest + warmers, local screen-printer for sponsor logos (peeled after 4 washes), drop-ship winter tights (different navy, different stretch). Four navy shades in the group photo. $8,500 spent, six months sourcing, 60% of riders unhappy."
- **Solution h3**: "Our fix"
- **Solution body**: "Single PM, single PO across all 6 SKUs. Same dye batch + same fabric mill for matching-color SKUs. Cycling Team Pack MOQ: 50 jerseys + 50 bibs + 30 long-sleeve + 30 tights + 30 vests + 30 warmer bundles = 220 cross-SKU one PO. Summer Q1, shoulder Q2, winter Q3 — same color story across all three deliveries."

**Image slot**: 3 grapesjs images:
- Row 1: `query=cycling-chamois-pad-cutaway&w=560&h=400`
- Row 2: `query=cycling-jersey-team-lineup&w=560&h=400`
- Row 3: `query=cycling-team-kit-flatlay&w=560&h=400`

**Style**: Tint bg #FAF7F2. Zigzag image-text alternating. Each row 50/50 split desktop, stacked mobile (image always on top). Pain block: red accent border-left 3px. Solution block: green accent border-left 3px. 96px vertical gap between rows desktop (64px mobile). Section padding `clamp(80px, 10vw, 120px)`.

---

## S6: Mid CTA (C+D) [full-width red strip]

**H2**: "Get a Cycling Kit Spec Match in 24 Hours"

**Sub**: "Send your design brief or tech-pack. Name your discipline and kit composition. We confirm fabric, MOQ split, and lead time within one business day."

**CTA**: "Request 24-Hour Cycling Kit Spec Match" → `#inquiry-form` with smooth-scroll JS per build-rules §9.

**Image slot**: None — solid color background only.

**Style**: Full-width brand-red strip #DC2626 background. White H2 and sub, centered. Single white-outlined button with red text on hover-invert. 25-30vh min-height. Padding `clamp(64px, 7vh, 88px)`.

---

## S7: OEM, ODM, Private Label, Cycling Team Pack (C+D) [card-grid icon-top, 4 cards]

**H2**: "Cycling Apparel OEM, ODM, Private Label, and the Cycling Team Pack"

**Sub**: "Four production models for four commitment levels. The Cycling Team Pack is our cycling-only program."

**Card 1: OEM (Cut-and-Sew)**
- Positioning: "Your tech-pack, our cut-and-sew lines, full custom control."
- Spec bullets:
  - MOQ 300 baseline / SKU
  - 35-42 day lead time
  - 1-piece sample USD 45 (waived after first PO)
  - AQL 2.5 pre-shipment
- Best for: "DTC cycling brands with finished tech-packs and a defined capsule launch plan."
- Link: "View full OEM process →" → `/services/oem`

**Card 2: ODM (Cycling-Cut Block Patterns)**
- Positioning: "40+ cycling-cut block patterns. You customize color, sublimation art, sponsor logos."
- Spec bullets:
  - MOQ 200 / SKU
  - 30-35 day lead time
  - 1-piece sample USD 45
  - Pattern royalty waived
- Best for: "New cycling brands without a tech-pack, or teams adapting an existing pattern."
- Link: "View ODM block patterns →" → `/services/odm`

**Card 3: Private Label**
- Positioning: "Our cycling blanks (jerseys, bibs, vests), your hangtag, care label, sponsor placement."
- Spec bullets:
  - MOQ 100 / style
  - 14-21 day lead time
  - Existing blank library
  - Fastest market entry
- Best for: "Founders racing to first PO or club captains testing a one-season trial kit fast."
- Link: "View private label process →" → `/services/private-label`

**Card 4: Cycling Team Pack — CYCLING-ONLY** (visually distinguished: brand-yellow #FCD34D 3px top border + "CYCLING-ONLY" ribbon)
- Positioning: "One factory, one PM, one PO across the full 6-SKU annual kit. Single dye batch, single sublimation pass, single QC sign-off across summer / shoulder / winter."
- Spec bullets:
  - **MOQ split (cross-SKU)**: 50 jerseys + 50 bibs + 30 long-sleeve + 30 tights + 30 vests + 30 warmer bundles = **220 pieces cross-SKU one PO** (vs 300 baseline single-SKU)
  - **Multi-season delivery**: summer kit Q1 (jersey + bib + warmers) / shoulder kit Q2 (long-sleeve + vest) / winter kit Q3 (tights)
  - Single PM + single account + single invoice
  - Same dye batch + same fabric mill for matching-color SKUs
  - Cross-SKU sample pull: 1 of each SKU (6 pieces) shipped together for color-match sign-off before bulk
  - Sponsor-logo registration ±1mm verified across every SKU in the kit
- Best for: "Amateur cycling clubs, charity-ride teams, Gran Fondo organizers, corporate / college cycling clubs. DTC brands launching a complete multi-SKU cycling capsule."
- Link: "Build your cycling team kit →" → `#inquiry-form` (JS pre-fills team-kit context message)

**Image slot**: 4 SVG icons (no photos for this section). Icons brand-red #DC2626 at top center of each card. Cycling Team Pack icon = composite of 6 mini-SKU silhouettes inside one icon frame.

**Style**: Tint bg #FAF7F2 (per Step 3 Decision_1). 4-column grid desktop, 2-column tablet, 1-column stack mobile. Cards: white bg, 8px radius, 1px border, hover lift. Icon 48-64px at top center. Link button at bottom (ghost outline for cards 1-3, brand-red solid for Cycling Team Pack to visually distinguish the page-unique card). Cycling Team Pack card: brand-yellow #FCD34D 3px top border + subtle hover border-glow pulse. Section padding `clamp(60px, 8vw, 100px)`.

---

## S8: Cycling Kit Sourcing Process (C+D) [horizontal stepper, 5 steps with 2 cycling-only]

**H2**: "Cycling Apparel Manufacturing Process: From Design Brief to Full Team Kit Shipment"

**Sub**: "Five steps. Two are cycling-specific. None are negotiable."

**Step 1: Design brief or tech-pack intake** (1-2 days)
Submit design brief, sketch, or tech-pack + sponsor logo files (vector preferred: .ai, .eps, .svg) + Pantone references. We confirm chamois availability, sublimation line capacity, fabric in stock, and quote per-SKU MOQ split. For team kits we ask about discipline, rider headcount, sponsor brand standards, and season opener date.

**Step 2: Chamois fit try-on** (3-5 days) **[CYCLING-SPECIFIC]**
Pre-bulk: 1 bib short sample produced with chamois in spec. Shipped to your captain or lead rider for an actual ride try-on (≥2 hr). Pass criterion: zero sit-bone pressure complaint, zero cover-fabric pilling, zero perimeter shift. Most factories skip rider try-on entirely.

**Step 3: Lab dip + first sample + sublimation registration test** (5-7 days)
Pantone match to within-batch ΔE ≤ 1.5. 1 jersey + 1 bib + (if applicable) 1 warmer sample printed in production-line conditions. Sponsor-logo placement measured at ±1mm tolerance, especially on logos crossing panel seams. Sample shipped via DHL / FedEx (3-5 day transit). USD 45 sample fee waived after first PO.

**Step 4: Pre-bulk sublimation batch sample (cross-SKU color match)** (5-7 days) **[CYCLING-SPECIFIC]**
Before bulk runs: factory prints 1 of each SKU in the kit (up to 6 pieces for full Cycling Team Pack) in actual production print-run conditions, photographs them together under controlled studio lighting, and ships the multi-SKU sample pull to you for cross-SKU color-match and brand-standards sign-off. Catches the "navy on bib ≠ navy on jersey" failure before bulk.

**Step 5: Bulk cut-sew + AQL 2.5 pre-shipment + ship** (35-42 days OEM, 30-35 ODM, 14-21 Private Label)
Cut-and-sew across dedicated lines (sublimation + chamois integration + cut-sew) under one PM. Per-piece sublimation ΔE check at sublimation station. Pre-shipment AQL 2.5 inspection. Bureau Veritas / SGS third-party inspection on request. FOB your designated port.

**Total end-to-end**: Single SKU 50-60 days. Multi-season Cycling Team Pack 90-120 days summer-to-winter delivery window — same factory, same color story, same QC across all seasons.

**Image slot**: Optional 1 wide image at top: grapesjs `query=cycling-factory-sublimation-print&w=1080&h=400`. 5 step icons inside numbered circles.

**Style**: White bg. Horizontal stepper desktop (5 nodes connected by line), vertical stepper mobile. Numbered circles 56px brand-red #DC2626 fill, white number. Steps 2 and 4 visually marked with brand-yellow #FCD34D "CYCLING-SPECIFIC" ribbon overlay on the circle + subtle 4s scale-pulse animation. Section padding `clamp(60px, 8vw, 100px)`. Total-days callout at bottom in tinted strip.

---

## S9: Cycling Apparel Manufacturer FAQ (C+D) [accordion + FAQ Schema, 8 items split C 4 + D 4]

**H2**: "Cycling Apparel Manufacturer FAQ"

**Sub**: "Eight questions cycling buyers ask before sending a tech-pack or team brief. Four for DTC brands, four for amateur teams."

**Group A: For DTC cycling brands (ICP-C)**

**Q1: What's the MOQ for a single cycling SKU like a flagship jersey or bib short?**
A: 300 pieces per SKU baseline (split across XS-XXL from that 300, not multiplied per size). 200/SKU on ODM block patterns. 100/style on Private Label. For a full multi-SKU capsule, ask about the Cycling Team Pack rule — 220 pieces cross-SKU one PO.

**Q2: Can I order 1 sample to test before committing to a 300-piece bulk?**
A: Yes. 1-piece sample, USD 45 fee, 5 working days when fabric is in stock. Sample fee waived after first bulk PO. You can sample any of the 6 cycling SKUs before deciding (jersey, bib, long-sleeve, tight, vest, warmers).

**Q3: How do I verify the chamois is actually Italian-source and not generic Asian foam relabeled?**
A: We disclose the chamois supplier name on request (Cytech-affiliated or Elastic-Interface-affiliated Tier-1 European supplier). We also ship a chamois cross-section cutaway sample (one bib cut open) so you can verify the 3-density zoning and 12-panel flatlock attachment yourself before committing.

**Q4: My capsule depends on a color story across 6 SKUs. How do you prevent cross-SKU drift?**
A: Same dye batch + same fabric mill across matching-color SKUs. Before bulk we produce 1 of each SKU in production print-run conditions, photograph them together under controlled studio lighting, and ship the 6-piece pull for sign-off. ΔE ≤ 1.5 within-batch tolerance, spectrophotometer-verified on every piece.

**Group B: For amateur teams and clubs (ICP-D)**

**Q5: I don't have a tech-pack — I have a team design brief, sponsor logo files, and a rider headcount. Can you still produce my team kit?**
A: Yes. ODM is the entry path: 40+ cycling-cut block patterns (race-fit jersey, gravel-fit jersey, bib short with Italian-source chamois, bib tight, vest, warmers). You provide color, sublimation art, sponsor logos, rider sizes. We cut-sew and sublimate against the block pattern. No formal tech-pack required.

**Q6: How does the Cycling Team Pack work — what's the actual MOQ split?**
A: Cycling Team Pack is our cycling-only program for full team kits. MOQ split: 50 jerseys + 50 bibs + 30 long-sleeve + 30 tights + 30 vests + 30 warmer bundles = 220 cross-SKU one PO (vs 300 baseline single-SKU). One PM, one PO number, one invoice, same dye batch across matching-color SKUs. Multi-season delivery: summer Q1, shoulder Q2, winter Q3 — all under one master spec.

**Q7: My team has sponsor logos with brand-standards tolerance. What's your registration accuracy?**
A: ±1mm tolerance on sponsor-logo placement, verified per piece pre-shipment. Before bulk we measure registration on the 6-piece cross-SKU sample pull and confirm sign-off against your sponsor's brand-standards file (if you can share it). Sponsor cancellations from logo drift are a specific failure mode we engineer out.

**Q8: Our season opens in 3 months. Can you deliver a full team kit in time?**
A: Yes, with planning. Cycling Team Pack lead time from brief intake → chamois try-on → lab dip → sublimation batch sample → bulk ≈ 70-90 days for the summer kit (jersey + bib + warmers). Long-sleeve + vest add 30 days. Winter tights add another 30 days. For a 3-month window: prioritize summer kit, ship shoulder + winter under the same Cycling Team Pack PO.

**Image slot**: None (accordion typography only). Chevron icon for accordion toggle.

**Style**: Tint bg #FAF7F2. Accordion list max-width 960px centered. Each FAQ row: Q in bold, A in body text. Click expands, chevron rotates 180°. Schema JSON-LD `FAQPage` injected in `<head>` with all 8 Q&A. Group A and Group B separated by subtle horizontal rule + group label. Section padding `clamp(60px, 8vw, 100px)`.

---

## S10: Certifications + Logo Wall + Inline Quote (C+D) [badge-row + logo-wall + quote-card hybrid]

**H2**: "Certified Cycling Apparel Factory: OEKO-TEX, BSCI, WRAP, GRS, and Higg"

**Sub**: "Five certifications. Each matters for a cycling-specific reason. Twelve brands and clubs ship with us today."

**Zone 1: 5 cert badges row**
1. OEKO-TEX Standard 100 (`23.HCN.74521`) — "Skin-contact safety for chamois cover in direct-saddle contact, 4-8 hours per ride."
2. BSCI (`BSCI-CN-2024-08-15`) — "Social compliance, cycling brand procurement + sponsorship audit-ready."
3. WRAP Gold (`WRAP-GLD-156823`) — "Ethical manufacturing standard for amateur-club brand integrity."
4. GRS (`CU 1014387 GRS-2024`) — "Recycled-polyester chain-of-custody for eco cycling capsules (rPET jerseys, bibs)."
5. Higg FEM (`HIG-FEM-2024-CN-08`, score 82/100) — "Dye-house traceability for within-batch sublimation color consistency."

**Zone 2: Inline customer quote (single quote-card)**

> "We tried four vendors in 2024 — jerseys from one, vest and warmers from another, sponsor logos heat-pressed locally, winter tights drop-shipped. $8,500, six months, and the navy didn't match across pieces. For 2025 Berun ran the full kit through one Cycling Team Pack PO. Same dye batch across all six SKUs. The sponsor signed for another season."
>
> — Marcus, Team Captain, Berlin Mile Club

<!-- PLACEHOLDER NOTE: Berlin Mile Club is in the §3.5 12-customer list (verbatim). The persona name "Marcus, Team Captain" is representative — replace with real captain name once business team confirms. Quote text 58 words, anchors pain_3 multi-vendor patchwork → Cycling Team Pack switch narrative. -->

**Zone 3: 12-brand logo wall** (4×3 grid)

Akarra Active · Aspen Athletic Co. · Berlin Mile Club · Capella Sport · Coastline Performance · Forge Lab Athletics · Granite Run · Kindred Strength · Meridian Move · Northcrest Outdoor · Sequoia Sweat · Verdant Athletics

<!-- PLACEHOLDER NOTE: 12-brand list verbatim from site-strategy-pack §3.5. Real brand logos to be uploaded by business team; grayscale placeholder SVG with brand name in the meantime per build-rules §5. -->

Caption: "12 active partners across cycling clubs, DTC cycling brands, athleisure, yoga, training, and outdoor."

**Image slot**:
- Zone 1: 5 existing certificate-*-preview.webp images per build-rules §5.
- Zone 2: 1 monogram SVG ("M" in brand-red #DC2626 circle).
- Zone 3: 12 brand logo placeholder SVGs (grayscale, brand name in cell).

**Style**: White bg. Zone 1 = horizontal row, 5 cert badges + caption below each (5 cols desktop, 2-3 cols mobile). Zone 2 = max-width 720px centered quote-card, tinted #FAF7F2 bg, large quote mark, monogram icon left of attribution. Zone 3 = 4×3 grid logo wall (2-col on mobile = 6 rows of 2), 1px gray border per cell, hover grayscale → color. Section padding `clamp(80px, 10vw, 120px)`.

---

## S11: Final CTA + Inquiry Form (C+D) [dark final-cta with form]

**H2**: "Start Your Cycling Apparel Production"

**Sub**: "Send your design brief or tech-pack. Share your discipline and kit composition. We reply within one business day."

**Form fields** (4 fields per build-rules §9):
- `Full Name` (required, text input)
- `Email` (required, email input)
- `Phone / WhatsApp` (optional, tel input)
- `Message` (required, textarea) — placeholder: "What cycling apparel do you need? Drop a design brief or tech-pack link, describe your kit composition (single jersey, full team kit, multi-season program), share sponsor logo files, or paste a reference photo URL. Mention your discipline (Road / Gravel / MTB / Triathlon / Indoor / Gran Fondo) and rider headcount if it's a team kit."
- Honeypot: hidden `name="website"` field with `display:none`
- Submit button: "Send Your Inquiry" (red solid)
- Form action: `https://form.lianf.com/`
- JS auto-inject: `submission_time`, `page_url` per build-rules §9

**Trust line below form**: "Replies within 1 business day · NDA on request · Sample fee waived after first PO · Cycling Team Pack samples available across the full 6-SKU kit"

**Contact alternates below trust line**: "Or email sales@berunactivewear.com directly · WhatsApp +86-159-0277-8636 · Anna, Sales Manager"

**Image slot**: Solid #1F2937 bg, optional grapesjs `query=cycling-bib-chamois-pad&w=1920&h=720` at 15% opacity background.

**Style**: Dark bg #1F2937, white text. H2 + sub centered. Form max-width 600px centered. Form fields: white bg, dark text, 8px radius, 1px border. Required-field asterisks in brand-accent #FCD34D. Submit button: brand-red #DC2626 fill, white text, full-width form bottom. ID `inquiry-form` on the form element. Smooth-scroll JS focuses first form field on anchor scroll-in per build-rules §9. Section padding `clamp(80px, 10vw, 120px)`.
