---
slug: basketball-apparel-manufacturer
domain: berunactivewear.com
page_type: landing
primary_keyword: basketball apparel manufacturer
route: /basketball-apparel-manufacturer
---

# Basketball Apparel Manufacturer for Amateur Teams, AAU Programs, and High-School Conferences

> Single-pass double-side reversible practice jerseys without bleed-through after a 60-cycle wash test. Tear-away 22-snap YKK-grade warm-up pants double-tested at every snap before shipment. ±2mm chest 12-16cm and back 25-30cm two-panel simultaneous number registration verified by overhead-camera template QC. Squad-flex re-order rule for the 3-5 mid-AAU-circuit replacement pieces your last basketball uniform manufacturer wouldn't ship under 300 MOQ. Custom basketball jerseys, game shorts, reversible practice jerseys, tear-away warm-up pants, shooting shirts + warm-up jackets, and mid-calf basketball socks + shooting arm sleeves cut-and-sewn under one project manager. MOQ 300 baseline per SKU; Basketball Squad Pack carve-out at 220 cross-SKU pieces (game jersey + game shorts ≥80 each, other SKUs flexible) for single-team AAU + HS conference + Park&Rec multi-team consolidated orders.

## S1: Hero (D1+D2+D3+D4) [white-bg centered reversible jersey diptych — structurally distinct from yoga/gym/cycling/soccer dark-overlay-with-right-inset-card pattern]

**Top eyebrow ribbon** (thin centered horizontal strip): "BASKETBALL SQUAD · REVERSIBLE · ±2MM · 14-DAY"

**Central Product Diptych** (centered, ~50% of hero height, max-width 880px):

- **Left jersey** — outer face: white body + navy chest number `#14` (chest centered, 14cm visual reference) + small player name above, navy collar trim, sleeveless tank silhouette, soft drop-shadow
- **Center flip-arrow column** (between jerseys, ~80px gap on each side):
  - SVG `↔` horizontal double-headed arrow, brand-red `#DC2626`, ~64×40px
  - Label beneath: "Single-pass double-side sublimation" (12px bold, brand-yellow `#FCD34D` underline)
  - Dashed vertical separator behind (1px dashed, brand-yellow 40% opacity, 60% of jersey height) — signals dye-blocked dual-layer construction
- **Right jersey** — inner face: navy body + white chest number `#14` (SAME number by construction — signals reversible same-number commitment) + small player name above in white, white collar trim, mirrored sleeveless tank silhouette, soft drop-shadow

Both jerseys at equal scale (~400×500px desktop, aspect ratio 4:5).

**H1** (centered below diptych, ~32px font-size, max-width 920px):

"Basketball Apparel Manufacturer for Amateur Teams, AAU Programs, and High-School Conferences"

**Sub** (centered single line, ~18px font-size, color #4B5563, max-width 820px):

"Single-pass reversible. Tear-away 22-snap. ±2mm chest+back registration. 14-day AAU between-event turn. Four things your last vendor probably did not do."

**CTA pair** (centered horizontal):
- Primary (brand-red `#DC2626` solid, white text): "Send Your Squad Kit Brief" → `#inquiry-form`
- Ghost outline (brand-red border + brand-red text, hover invert): "Coordinate AAU League Order" → `#inquiry-form` (JS pre-fills message: "I'm coordinating [X] AAU teams / HS conference schools / Park&Rec teams for the [season name] season. Each squad is [Y] players. We have [Z] sponsor logos to apply across [team count] team designs. We need pricing for game jersey + game shorts + reversible practice jersey + warm-up jacket + warm-up pants + socks. Season opens [date].")

**Bottom 4 spec pills** (centered horizontal row, no separator characters between pills):

1. `single-pass × 60-cycle`
2. `22-snap YKK`
3. `±2mm chest+back`
4. `14-day AAU turn`

Each pill: 8px border-radius, 1px border #E5E7EB, white bg, padding 6px 14px, hover translateY(-2px) + border-color brand-red.

**Structurally removed from yoga/gym/cycling/soccer Hero pattern**:
- No full-bleed factory-floor background image (white background instead)
- No 60% dark overlay
- No 55/45 left-text + right-inset-card split (centered single-column instead)
- No 6-bullet inset card (4 spec pills replace at bottom, 67% visual footprint)
- No stats bar with `|` divider (4 self-contained pills replace, no separator characters)

**Image slots** (NOT a background image — two product slots):
- Left jersey: primary `query=basketball-reversible-jersey-white-side&w=400&h=500`
  - Fallback tier 2: `query=basketball-jersey-mockup&w=400&h=500`
  - Fallback tier 3: `query=basketball-jersey-tank&w=400&h=500`
  - Fallback tier 4: CSS `.img-ph` placeholder (camera icon + "Photo pending", 4:5 aspect preserved)
- Right jersey: primary `query=basketball-reversible-jersey-navy-side&w=400&h=500`
  - Fallback tier 2-4: same chain as left (different seed where applicable)
- Central flip-arrow + label: pure inline SVG (no grapesjs dependency)

**Animation hooks** (Step 3 codifies):
- On-load: diptych fade-in 0.4s ease-out (jerseys + flip-arrow simultaneously); H1 fade-in delay 0.6s; Sub + CTA + spec pills cascade-fade delay 0.8s-1.0s
- On-loop: central `↔` flip-arrow horizontal rotation 180° loop every 4s ease-in-out (subtle, 0.5 opacity at midpoint, signals reversible flip) — pauses on `prefers-reduced-motion: reduce`
- On-hover: jersey scale 1.03 + cast-shadow lift (0.25s ease-out)
- On-pill hover: border-color shift to brand-red + translateY(-2px) (0.2s ease-out)

**Mobile fallback (≤768px)**:
- Diptych stacks vertically (left jersey on top, central arrow rotates to `↕`, right jersey below)
- Each jersey scales to ~280×350px
- H1 → 26px, Sub → 16px
- Dual CTA stacks full-width vertically (primary top, ghost bottom)
- 4 spec pills wrap to 2×2 grid

**Tablet fallback (769-1024px)**:
- Diptych stays horizontal but jerseys scale to ~320×400px, 60px gap on each side of flip-arrow column

## S2: Basketball Subcategory Cards (D1+D2+D3+D4) [card-grid image-top]

**H2**: "Custom Basketball Jerseys, Reversible Practice Jerseys, Tear-Away Warm-Up Pants, Shooting Shirts, Shorts, and Socks We Cut and Sew"

**Sub**: "Six basketball SKUs that build one squad kit. Game-day construction, practice-day reversible color flip, sub-line tear-away mechanics, and the shooting + socks accessories you re-order every season."

**6 cards** (3+3 grid desktop / 2+2+2 tablet / 1-col mobile):

### Card 1 — Game Jersey (Home, Away, Alternate Sleeveless Tank)
- Image: `query=basketball-game-jersey&w=640&h=400`
- Positioning: Sleeveless tank match-day jersey with player number on chest 12-16cm + back 25-30cm, sponsor placement on chest opposite number, conference patch or team crest.
- Pills: `140-160 GSM lightweight poly` · `chest+back two-panel ±2mm` · `home / away / alternate rotation`
- Link: "Spec a game jersey →" → `#inquiry-form`

### Card 2 — Game Shorts (Knee-Length Baggy Cut)
- Image: `query=basketball-game-shorts&w=640&h=400`
- Positioning: Knee-length baggy-cut basketball game shorts with side panel sublimation, optional secondary sponsor on left thigh, side-hem inside-pocket for mouthguard storage.
- Pills: `knee-length baggy cut` · `side-panel sublimation` · `mouthguard inside-pocket`
- Link: "Spec game shorts →" → `#inquiry-form`

### Card 3 — Reversible Practice Jersey (Single-Pass Double-Side Sublimation)
- Image: `query=reversible-basketball-jersey&w=640&h=400`
- Positioning: Reversible sleeveless practice jersey with outer face one color + inner face contrasting color, per-side player numbers on chest + back, single-pass double-side sublimation transfer prevents bleed-through.
- Pills: `single-pass double-side` · `60-cycle wash tested` · `per-side ±2mm number registration`
- Link: "Spec a reversible practice jersey →" → `#inquiry-form`

### Card 4 — Tear-Away Warm-Up Pants (22-Snap YKK-Grade Side Closure)
- Image: `query=basketball-warmup-pants&w=640&h=400`
- Positioning: Tear-away snap-side warm-up pants with 22-snap YKK-grade fastener row down each outer leg, releases cleanly when a player is called to sub on, 100% pre-shipment snap-cycle test on every pant.
- Pills: `22-snap YKK-grade` · `100% pre-ship cycle test` · `50-cycle pull-release durability`
- Link: "Spec tear-away pants →" → `#inquiry-form`

### Card 5 — Shooting Shirt + Warm-Up Jacket
- Image: `query=basketball-shooting-shirt&w=640&h=400`
- Positioning: Long-sleeve shooting shirt for pre-game shootaround + snap-front warm-up jacket or pullover hoodie for bench rotation, matching team color and chest sponsor placement.
- Pills: `long-sleeve shooting shirt` · `snap-front or pullover` · `bench rotation durable`
- Link: "Spec shooting + warm-up →" → `#inquiry-form`

### Card 6 — Basketball Socks + Shooting Arm Sleeve Combo
- Image: `query=basketball-socks&w=640&h=400`
- Positioning: Mid-calf cushioned basketball sock with arch + Achilles support + shooting arm sleeve with 4-way stretch and internal grip stripe, left/right asymmetric spec per shooting hand.
- Pills: `mid-calf cushion` · `shooting sleeve L/R asymmetric` · `internal grip stripe`
- Link: "Spec socks + sleeve →" → `/products/accessories`

## S3: Basketball Competition Tier Matrix (D1+D2+D3+D4) [3-column attribute-grid panels]

**H2**: "Basketball Team Uniform Manufacturing Spec'd to Your Competition Tier"

**Sub**: "Adult amateur 5-a-side. Youth U10-U18 grassroots. High-school JV and varsity. NCAA DII-DIII and NIRSA campus club. AAU travel team and summer circuit. Corporate, church, and Park & Rec adult-rec. Each tier has its own SKU mix, rule library, and sizing curve."

**6 tier panels** (full-width row, image-left 40% + 3-col attribute grid right 60%):

### Panel 1 — Adult Amateur 5-a-side
- Image: `query=amateur-basketball-game&w=480&h=360`
- **SKU Mix**: home + away game jersey, game shorts, reversible practice jersey, mid-calf basketball socks, optional shooting shirt + warm-up jacket
- **Rule Library**: amateur-rec default standard, no state-tier compliance, basic NFHS-compatible number sizing 12-14cm chest + 25-28cm back for visual readability
- **Sizing Curve + Fabric Tier**: adult M-XXL primary distribution, sample 10-12 player roster, indoor-gym mesh tier (28-32°C + 65% humidity heat-resistance)

### Panel 2 — Youth U10-U18 Grassroots
- Image: `query=youth-basketball-team&w=480&h=360`
- **SKU Mix**: same 6 SKUs but with youth-sizing curves (U10=YS-YM, U12=YM-YL, U14-U18=YL-AM-AL); reversible practice jersey volume disproportionately high
- **Rule Library**: youth-league brand-standards restrictions (no alcohol / no gambling on U18-and-under); number sizing typically 12-14cm chest + 25-28cm back (youth jersey panel area smaller)
- **Sizing Curve + Fabric Tier**: 3 separate sizing buckets per age tier, growth-allowance recommended (1 size up on jersey for U10-U14); youth-skin-contact safety fabric tier

### Panel 3 — High-School JV + Varsity (Boys + Girls)
- Image: `query=high-school-basketball&w=480&h=360`
- **SKU Mix**: home + away + alternate game jersey, game shorts, reversible practice jersey, tear-away warm-up pants (varsity-tier required), warm-up jacket, mid-calf socks
- **Rule Library**: **NFHS Rules Book + state-tier athletic association rule library** (Texas UIL / California CIF / Florida FHSAA / New York NYSPHSAA / Illinois IHSA explicitly maintained; other 45 states adopt NFHS default), chest number ≥10cm + back number ≥15cm (most default 14cm chest + 28cm back)
- **Sizing Curve + Fabric Tier**: adult M-XL primary, 12-15 player roster per JV + 12-15 per varsity, state-tournament-eligibility re-order cycle; gym-grade indoor mesh tier

### Panel 4 — NCAA DII-DIII + NAIA + NJCAA + NIRSA Campus Club Basketball
- Image: `query=ncaa-college-basketball&w=480&h=360`
- **SKU Mix**: home + away game jersey, game shorts, reversible practice jersey, tear-away warm-up pants, shooting shirt + warm-up jacket, socks
- **Rule Library**: NCAA Rules Book Section 14 (uniform-number spec), amateur-tier compliance; NIRSA campus club operates outside NCAA varsity with university brand-standards (university name + athletics department logo + optional regional sponsor)
- **Sizing Curve + Fabric Tier**: adult M-XL primary, 12-15 player roster, season cycle per academic-year fall-to-spring (NCAA Nov-Mar; NIRSA Sept-May with regional tournament Feb-Mar)

### Panel 5 — AAU Travel Team + Summer Circuit (Adidas Gauntlet, Nike EYBL, Under Armour Association)
- Image: `query=aau-basketball-tournament&w=480&h=360`
- **SKU Mix**: home + away game jersey with AAU national-sponsor placement, game shorts, reversible practice jersey (custom per coaching staff for summer-camp drill rotation), tear-away warm-up pants, warm-up jacket, mid-calf socks
- **Rule Library**: **AAU national-sponsor brand-standards (Adidas Gauntlet / Nike EYBL / Under Armour Association)** — each AAU sponsor has its own sponsor-logo placement rule on chest + sleeve + chest-clear-space-from-number; per-tournament rule book covers number sizing at 14cm chest + 28cm back baseline
- **Sizing Curve + Fabric Tier**: 3 separate buckets per age division (U13-U14, U15-U16, U17), 6-15 teams per program per circuit season, mid-circuit transfer common (squad-flex re-order applies heavily); travel-pack durable indoor-gym fabric tier

### Panel 6 — Corporate + Church League + Park & Rec Adult Rec
- Image: `query=corporate-basketball-league&w=480&h=360`
- **SKU Mix**: simplified — single game jersey design (no home/away), game shorts, socks; often skip reversible + tear-away (recreational tier, no sub-line discipline)
- **Rule Library**: company logo on chest (employer-funded), department name on back instead of player names, single-sponsor; no state-tier compliance; basic 14cm chest + 28cm back default
- **Sizing Curve + Fabric Tier**: adult-only S-XL, 12-15 piece total kit, single-season or once-every-2-years refresh; standard indoor-gym mesh tier

## S4: Reversible Print, Tear-Away Construction & Per-Number Registration (D1+D2+D3+D4) [SVG composite + spec table + 3 callouts, page-unique anchor]

**H2**: "Reversible Print, Tear-Away Construction, and Per-Number Registration for Custom Basketball Uniform Manufacturers"

**Sub**: "Single-pass double-side sublimation transfer with no bleed-through after 60-cycle wash. Tear-away 22-snap YKK-grade fastener tested at every snap before shipment. ±2mm two-panel simultaneous registration on chest 12-16cm and back 25-30cm large-format numbers."

**SVG Composite Annotated Diagram (top-center 60% width)** — 3 sub-diagrams horizontal:
1. **Reversible jersey outer+inner side-by-side** with per-side number callouts (outer-face white-w-navy-trim with chest #14 + back #14 / inner-face navy-w-white-trim with chest #14 + back #14 — identical per-side number by construction), single-pass double-side sublimation transfer indicator arrow
2. **Tear-away warm-up pant side-view** with 22-snap YKK fastener row callouts down outer leg: `22 snaps · YKK-grade · 100% pre-shipment cycle test · 50-cycle pull-release durability tested`
3. **Chest + back number registration tolerance arrows** — front jersey chest with 14cm number + ±2mm tolerance arrow + back jersey with 28cm number + ±2mm tolerance arrow + NFHS / state-tier / AAU rule-library legend

**Spec Table (full-width below SVG)** — Berun Basketball Standard vs Industry Commodity:

| Construction / Spec | Berun Basketball Standard | Industry Commodity |
|---|---|---|
| Reversible practice jersey | Single-pass double-side sublimation transfer, dye-blocked dual-layer fabric, 60-cycle wash bleed-through test at 60°C | 2-pass sequential sublimation (bleed-through + per-side drift root cause), single-layer fabric, no wash test |
| Per-side number registration | Per-side independent registration template (outer + inner each have own ±2mm template), roster CSV per-side double-keyed mapping | Assumed-mirror template (drift root cause), single-pass operator entry from CSV (off-by-one root cause) |
| Tear-away warm-up pant | 22-snap YKK-grade fastener, 100% pre-shipment snap-cycle test, 50-cycle pull-release durability test | 18/20-snap commodity fastener, no per-pant snap test, no pull-release test |
| Number registration tolerance | ±2mm on chest 12-16cm AND ±2mm on back 25-30cm SIMULTANEOUSLY per garment | ±5-8mm typical drift on chest, separate ±5-8mm drift on back, no two-panel simultaneous QC |
| Number sizing rule library | NFHS + Texas UIL / California CIF / Florida FHSAA / New York NYSPHSAA / Illinois IHSA + Adidas Gauntlet / Nike EYBL / Under Armour Association + NCAA varsity + amateur-rec (6 rule libraries) | "We print whatever size you specify" — no rule-library check pre-bulk |
| Per-PO registration QC | Overhead-camera registration template QC per jersey at sublimation station; out-of-tolerance pulled and re-printed | Spot-check on first 10 pieces of bulk, no per-jersey overhead-camera QC |
| Number-and-name entry | Double-keyed verification (two operators independently from roster CSV) on every number + name field | Single-operator entry from CSV (typo failure mode root cause) |
| Pre-bulk reversible sample | 1 complete reversible practice jersey with all 12 players' numbers on BOTH faces, photographed on grid background with measurement tape overlay both-side | Single-side sample, no per-side grid photo |
| Indoor court mesh fabric tier | 28-32°C + 65% humidity indoor-gym heat-resistance + non-curling bottom hem after 4-cycle wash | Generic activewear mesh, no indoor-gym climate spec, hem-curl after 4 cycles common |
| Sublimation panel + roster CSV retention | 12 calendar months on factory server (panel + per-side spec + roster CSV + sponsor logo file) | Discarded after PO ships |
| Squad-flex re-order rule | ≤20% of original PO at zero added MOQ + 14-day turn + same panel reused + AAU between-event cadence | MOQ 300 + 6 weeks for any re-order regardless of quantity |

**3 micro-deep-dive callout boxes (below table, 3-col grid)**:

1. **Single-pass double-side sublimation construction** — Reversible practice jerseys are produced in a single press cycle with outer-face and inner-face dyes simultaneously transferred onto dye-blocked dual-layer fabric. The opaque blocking layer prevents dye-bleed migration through wash cycles. Industry-commodity 2-pass sequential process is the root cause for both bleed-through (no blocking layer) and per-side number drift (operator entry error on second pass).
2. **Tear-away 22-snap YKK-grade pre-shipment test** — Every tear-away warm-up pant has 22 YKK-grade snaps down each outer leg, double-tested at pre-shipment QC (every snap engaged + released twice per pant), plus production batch sample passes 50-cycle pull-release durability test. Industry-commodity 18/20-snap with no per-pant test produces the game-day failure: 1-or-2-of-22 snaps not releasing at the sub line.
3. **±2mm two-panel simultaneous registration + basketball-format number sizing rule library** — Every basketball jersey carries chest ±2mm AND back ±2mm SIMULTANEOUSLY (both panels measured against per-PO template via overhead-camera). Basketball numbers (chest 12-16cm + back 25-30cm) are 1.5-2x soccer back-only numbers (8-10cm), making drift more visible. Rule library covers NFHS / top-5 state-tier / AAU national-sponsor / NCAA varsity — PM configures registration template per selected standard.

## S5: 3 Pain → Solution Zigzag (D1+D2+D3+D4) [standard zigzag]

**H2**: "Three Basketball Squad Supply Failure Modes We Engineer Out"

**Sub**: "Three things our new customers showed us after their last factory wouldn't ship a mid-AAU-circuit replacement, mis-printed inner-face numbers on their reversible practice jerseys, or drifted the chest-and-back numbers enough that a parent's WhatsApp game-day photo flagged it within sixty seconds."

### Row 1 — Mid-AAU-Circuit Replacement Blocked by 300 MOQ (image-left text-right)
- Image: `query=aau-basketball-team-photo&w=560&h=400` (fallback `query=youth-basketball-coach`)
- **Pain H3**: "Three players grew, lost, or shredded their AAU jerseys between Tournament 1 and Tournament 3. The factory quoted 300 MOQ for 4 replacement pieces."
- **Pain body**: AAU travel-team program director, $16,500 pre-spring-circuit PO across 8 AAU teams (boys + girls U14-U17, 112 pieces). Six weeks into the Adidas Gauntlet Spring Circuit: one U15 girls player grew 4cm Feb-to-April, one U16 boys jersey forgotten at the Indianapolis hotel laundromat, one U17 girls jersey torn at the right armpit from a rebound-battle collision. Factory quote for 4 replacement pieces: MOQ 300 + 6 weeks. Options: $1,800 waste, mismatched street kit in front of college scouts at the Spring League showcase, or generic blanks without the regional auto-dealer-chain sponsor logo. Regional sponsor's marketing manager calls Monday morning, threatens to pull next-season's $3,200 sponsorship payout.
- **Solution H3**: "Our fix"
- **Solution body**: Squad-flex re-order rule: ≤20% of original PO at zero added MOQ + 14-day turn. AAU between-event cadence: Sunday submit after Tournament 1 → Friday ship before Tournament 3, fits the standard 7-day between-tournament gap with margin. Original sublimation panel + sponsor logo file + roster CSV retained 12 months on our server. Per-size specification (1 U15 girls Medium / 1 U16 boys Large / 1 U17 girls Small / 1 spare). Single PM continuity. Multi-team programs consolidate ALL teams' mid-circuit re-orders into one quarterly re-order PO.

### Row 2 — Reversible Jersey Bleed-Through + Per-Side Number Drift (image-right text-left)
- Image: `query=reversible-basketball-practice&w=560&h=400` (fallback `query=basketball-practice-scrimmage`)
- **Pain H3**: "Twenty-four reversible practice jerseys shipped. After three washes the inner-face navy bleeds through to the outer-face white. On six jerseys the inner-face number is one digit off from the outer-face number."
- **Pain body**: NIRSA campus club basketball head coach. Ordered 24 reversible practice jerseys for 12-vs-12 scrimmage (outer-face white-w-navy-trim, inner-face navy-w-white-trim, identical per-side numbers). First 3 washes at 60°C industrial campus washer reveal two failure modes: outer-face white bleeds gray-blue from inner-face navy on 18 of 24 jerseys (light-vs-dark 5v5 scrimmage now impossible from 30ft); inner-face number is off by one from outer-face on 6 of 24 jerseys (operator at original factory referenced wrong CSV column on the 2-pass second-side print job). Coach calls "white side numbers 0, 3, 11, 14, 22 — half-court" and 3 players don't know which side they belong to. Coach throws out the $2,400 reversible jersey set and re-orders from another factory.
- **Solution H3**: "Our fix"
- **Solution body**: Single-pass double-side sublimation transfer: outer-face and inner-face dyes simultaneously transferred onto dye-blocked dual-layer fabric in one press cycle — no 2-pass operator-entry error, no bleed-through migration through wash cycles. 60-cycle wash bleed-through test at 60°C industrial wash, zero detectable bleed-through through cycle 60. Per-side independent registration template (outer + inner each have own ±2mm template). Roster CSV per-side double-keyed mapping: outer-face and inner-face share the same player-number by construction. Pre-bulk reversible-jersey double-side photographed sample: 1 complete reversible with all 12 players' numbers on BOTH faces, photographed on grid background with measurement tape overlay both-side, shipped for sign-off before bulk PO.

### Row 3 — Chest + Back Number Registration Drift Visible in Game-Day Photos (image-left text-right)
- Image: `query=basketball-jersey-back-numbers&w=560&h=400` (fallback `query=basketball-game-jersey`)
- **Pain H3**: "Chest number 5mm off on four jerseys. Back number 4mm low on three jerseys. Parents on the sideline filmed every play. WhatsApp group flagged it within sixty seconds of tip-off."
- **Pain body**: High-school athletic-conference equipment buyer, 12 member schools' varsity boys basketball uniforms (168 home jerseys, chest 14cm + back 28cm per state-tier athletic association). Friday-night home opener inspection: chest number 5mm off-center on 4 of 14 jerseys, back number 4mm low on 3 of 14 jerseys. Parents in the bleachers film every basket, post to the team's WhatsApp parent group within 60 seconds of tip-off. By 2nd-quarter buzzer, 3 parents texted the AD, conference brand-standards manager flagged 7 of 14 home jerseys as out of spec, state athletic association compliance requires ≤±5mm tolerance for state-tournament eligibility. AD's call: re-print by Tuesday or forfeit Friday's home game. Options: $1,200 rush rebuild fee at her current vendor (8% of season equipment budget), forfeit home game, or swap player-jersey assignments mid-week putting drifted jerseys on bench-warmers (3 bench-warmer parents complain, 3 bench-warmer players quit mid-season).
- **Solution H3**: "Our fix"
- **Solution body**: ±2mm tolerance on chest 12-16cm number AND ±2mm on back 25-30cm number SIMULTANEOUSLY per jersey — overhead-camera registration template QC per jersey at sublimation station against per-PO basketball-format template configured per applicable rule library (NFHS / state-tier UIL/CIF/FHSAA/NYSPHSAA/IHSA / AAU national sponsor / NCAA varsity). Out-of-tolerance jerseys pulled off line and re-printed before packing. Number-and-name double-key verification: two operators enter independently from roster CSV. Pre-bulk single-jersey registration sample with chest + back number measurement tape overlay shipped for sign-off before bulk PO. Per-PO conference / sponsor / standard rule-library check by PM before bulk runs flags any conflict.

## S6: Mid CTA (D1+D2+D3+D4) [mid-cta full-width red strip]

**H2**: "Get a Basketball Squad Kit Spec Match in 24 Hours"

**Sub**: "Send your design brief, roster size, and sponsor logo files. Tell us your competition tier (Adult amateur 5-a-side / Youth U10-U18 / HS JV+Varsity / NCAA DII-DIII+NAIA+NIRSA campus club / AAU travel team + Summer circuit / Corporate + Church + Park&Rec) and squad composition. We match against our basketball panel library, single-pass double-side sublimation press capacity, tear-away 22-snap construction line, and 12 production lines, and confirm fabric, MOQ split, two-panel number registration tolerance, reversible bleed-through resistance, and 14-day re-order availability within one business day."

**CTA**: "Request a 24-Hour Basketball Squad Spec Match" → `#inquiry-form`

## S7: OEM, ODM, Private Label, Basketball Squad Pack (D1+D2+D3+D4) [card-grid icon-top, 4 cards with 4th elevated]

**H2**: "Basketball Apparel OEM, ODM, Private Label, and the Basketball Squad Pack"

**Sub**: "Four production models for four commitment levels. The Basketball Squad Pack is our basketball-only program — pick it if you need a squad kit with reversible single-pass double-side sublimation, tear-away 22-snap warm-up pants, squad-flex AAU between-event re-order, and the state-tier athletic association rule-library compliance baked in."

### Card 1 — OEM (Cut-and-Sew)
- Icon: factory cutting SVG, brand-red
- Positioning: "Your tech-pack, our cut-and-sew lines, full custom control on every chest+back number, sponsor placement, and snap fastener row."
- Spec bullets:
  - MOQ 300 baseline / SKU
  - 35-42 day lead time
  - 1-piece sample USD 45 (waived after first PO)
  - AQL 2.5 pre-shipment
- Best for: "Multi-team AAU + HS conference programs with tech-pack-ready designs (D2/D4) and adult amateur clubs with formalized team graphic standards."
- Link: "View full OEM process →" → `/services/oem`

### Card 2 — ODM (Basketball-Cut Block Patterns)
- Icon: pattern-block SVG, brand-red
- Positioning: "30+ basketball-cut block patterns. You customize color, sublimation art, number placement, sponsor logos."
- Spec bullets:
  - MOQ 200 / SKU
  - 30-35 day lead time
  - 1-piece sample USD 45
  - Pattern royalty waived
- Best for: "First-time amateur clubs and NIRSA campus club programs without a tech-pack, or HS programs adapting an existing pattern to a new season design."
- Link: "View ODM block patterns →" → `/services/odm`

### Card 3 — Private Label
- Icon: hangtag SVG, brand-red
- Positioning: "Our existing basketball game-jersey, reversible-practice, and tear-away-pant blanks. Your hangtag, sponsor placement, team crest."
- Spec bullets:
  - MOQ 100 / style
  - 14-21 day lead time
  - Existing basketball blank library
  - Fastest market entry
- Best for: "Corporate Sunday-rec captains racing to a season opener, or regional basketball-specific kit brands testing a new AAU-club design fast."
- Link: "View private label process →" → `/services/private-label`

### Card 4 — Basketball Squad Pack (basketball-only program, elevated)
- Icon: 6-SKU basketball kit silhouette SVG composite, brand-red
- Visual: brand-yellow #FCD34D top border + "BASKETBALL-ONLY" ribbon overlay
- Positioning: "One factory, one PM, one PO across the full basketball squad kit. Reversible single-pass double-side sublimation, tear-away 22-snap YKK-grade warm-up pants, squad-flex re-order on 20% of original PO, 14-day mid-season turn that fits AAU between-event cadence, and the NFHS + state-tier + AAU national-sponsor + NCAA varsity number sizing rule library ingested before bulk."
- Spec bullets:
  - **Cross-SKU MOQ floor**: 100 game jerseys + 100 game shorts + 50 reversibles + 30 warm-up jackets + 22 tear-away pants + 30 socks+sleeve combos = **332 pieces cross-SKU one PO** (example valid PO); mandatory floor is game jersey + game shorts ≥80 each, other SKUs flexible 30-50 each, cross-SKU total ≥220 pieces
  - **Squad-flex re-order rule**: ≤20% of original PO at zero added MOQ + 14-day turn
  - **AAU summer-circuit cadence adaptation**: 14-day turn fits standard 7-day between-tournament gap with margin (Sunday submit after Tournament 1 → Friday ship before Tournament 3)
  - **12-month panel + roster CSV + sponsor file retention**
  - **Single-pass double-side reversible sublimation** with 60-cycle wash bleed-through test
  - **Tear-away 22-snap YKK-grade fastener** with 100% pre-shipment snap-cycle test + 50-cycle pull-release durability test
  - **±2mm chest+back two-panel simultaneous registration** with overhead-camera per-jersey QC
  - **Basketball-format number sizing rule library**: NFHS / Texas UIL / California CIF / Florida FHSAA / New York NYSPHSAA / Illinois IHSA / Adidas Gauntlet / Nike EYBL / Under Armour Association / NCAA varsity / amateur-rec
  - **Multi-team consolidation**: AAU + HS conference + Park&Rec multi-team programs consolidate 6-20 team designs in one PO
  - **Per-side independent registration template + roster CSV per-side double-keyed mapping**
- Best for: "AAU travel-team program directors, HS athletic-conference equipment buyers, Park&Rec multi-team coordinators, regional basketball-specific kit brands, NIRSA campus club programs needing reversible + tear-away + tournament-cadence delivery, and adult amateur clubs that want the squad-flex re-order safety net from day one."
- Link: "Build your basketball squad kit →" → `#inquiry-form`

## S8: Basketball Kit Manufacturing Process (D1+D2+D3+D4) [horizontal stepper, 5 steps with 2 basketball-only]

**H2**: "Basketball Kit Manufacturing Process: From Squad Brief to Tip-Off Delivery"

**Sub**: "Five steps. Two are basketball-specific (reversible double-face pre-bulk sample + roster CSV per-side double-keyed + state-tier rule library check / per-jersey two-panel registration template QC + 100% snap-cycle test on tear-away pants + number-and-name double-key). None are negotiable."

Optional wide image at top: `query=basketball-factory-sublimation&w=1080&h=400` (fallback `query=garment-factory-floor`)

### Step 1 — Squad brief or tech-pack intake (1-2 days)
Submit squad design brief, sketch, or tech-pack + roster CSV (per-player size + name + number + position) + sponsor logo files (vector preferred: .ai, .eps, .svg) + Pantone references + applicable rule library (NFHS / state-tier athletic association / AAU national-sponsor brand-standards / NCAA varsity / amateur-rec). PM confirms panel availability, sublimation press capacity, tear-away pant production-line capacity, fabric in stock, and quotes per-SKU MOQ split. For multi-team AAU + HS conference + Park&Rec programs we confirm consolidated PO scope.

### Step 2 — Reversible double-face pre-bulk sample + roster CSV per-side double-keyed + state-tier rule library check (5-7 days) [BASKETBALL-SPECIFIC]
PM ingests roster CSV at order entry, double-keys per-side number mapping (outer + inner share same player-number by construction, eliminating inner-face off-by-one root cause). For reversible practice jerseys: factory produces 1 complete reversible with all 12 players' numbers on BOTH faces in production-line conditions, photographs on grid background with measurement tape overlay both-side, ships double-side photographed sample for sign-off. PM checks applicable rule library for number sizing + chest+back placement compliance, flags any conflict with customer-specified design before bulk PO.

### Step 3 — Lab dip + first sample + chest+back ±2mm registration test (5-7 days)
Pantone match. 1 sublimated basketball game jersey sample printed in production-line conditions with chest 14cm + back 28cm numbers measured at ±2mm tolerance two-panel simultaneous against tech-pack-specified positions. Plus 1 tear-away warm-up pant sample with 22-snap fastener row tested at 100% snap cycle. Samples shipped via DHL / FedEx (3-5 day transit). USD 45 sample fee waived after first PO.

### Step 4 — Per-jersey two-panel registration template QC + 100% snap-cycle test + name-and-number double-key (during bulk production, integrated checkpoint) [BASKETBALL-SPECIFIC]
Factory uses per-PO basketball-format registration template (transparency overlay showing chest 12-16cm + back 25-30cm number positions per applicable rule library). Overhead-camera-checks every jersey at sublimation station against the template; out-of-tolerance jerseys (chest >±2mm OR back >±2mm) are pulled off the line and re-printed before packing. Every tear-away warm-up pant gets 100% snap-cycle test (every snap engaged + released twice per pant) at pre-shipment QC. Number-and-name double-key verification: two operators enter independently from roster CSV; system flags any discrepancy for arbitration before printing.

### Step 5 — Bulk cut-sew + AQL 2.5 pre-shipment + ship (35-42 days OEM, 30-35 ODM, 14-21 Private Label, 14-day Squad-Flex re-order with AAU between-event cadence)
Cut-and-sew across dedicated lines (sublimation line + cut-sew line + basketball team kit assembly under one PM). Per-piece QC at sublimation station against registration template. Pre-shipment AQL 2.5 inspection. Bureau Veritas / SGS third-party inspection on request. FOB your designated port. Multi-team Basketball Squad Pack: consolidated shipment per delivery window (AAU spring-summer circuit tournament weekend / HS conference season opener / Park&Rec season cycle).

**Total end-to-end**: Single squad single PO 50-60 days. Multi-team Basketball Squad Pack 60-75 days for the consolidated multi-team launch order; squad-flex re-orders deliver in 14 days each within the 12-month panel-retention window.

## S9: Basketball Apparel Manufacturer FAQ (D1+D2+D3+D4) [accordion + FAQ Schema, 8 items split 4+4]

**H2**: "Basketball Apparel Manufacturer FAQ"

**Sub**: "Eight questions basketball buyers ask before sending a squad brief. Four for first-time squad organizers, four for returning customers and AAU + HS conference + Park&Rec multi-team coordinators."

### Group A: First-time squad organizer

**Q1: What's the MOQ for a single basketball SKU like a game jersey or reversible practice jersey, and how does the Basketball Squad Pack MOQ split work?**
A: Single SKU MOQ is 300 pieces (split across sizes XS-XXL from that 300, not multiplied per size). 200/SKU on ODM block patterns. 100/style on Private Label. For a full multi-SKU squad kit, ask about the Basketball Squad Pack — it allows 220 pieces cross-SKU one PO with game jersey + game shorts ≥80 each as the mandatory floor, other SKUs (reversible / tear-away / shooting+warm-up / socks+sleeve) flexible 30-50 each.

**Q2: Can I order 1 sample to test the reversible double-side sublimation or tear-away 22-snap construction before committing to a 300-piece bulk?**
A: Yes. 1-piece sample, USD 45 fee, 5 working days when fabric is in stock. Sample fee waived after first bulk PO. You can sample any of the 6 basketball SKUs. For reversible practice jersey samples we ship with both faces photographed on grid background with measurement tape overlay so you can verify per-side number registration + zero bleed-through pre-tendency before bulk.

**Q3: Do you produce reversible practice jerseys with single-pass double-side sublimation and dye-blocked dual-layer fabric construction?**
A: Yes — single-pass double-side sublimation transfer is mandatory on every reversible practice jersey we produce (not 2-pass sequential, which is the industry-commodity bleed-through + per-side number drift root cause). Dye-blocked dual-layer reversible-fabric construction with opaque blocking layer between faces prevents dye-bleed migration. We test production batches at 60 industrial wash cycles at 60°C for outer-face bleed-through detection at 30-ft viewing distance — zero detectable bleed-through through cycle 60 is the production protocol.

**Q4: What basketball-format number sizing standard library do you maintain for chest and back number placement?**
A: We maintain 6 rule-library standards: NFHS federal-tier (default for all 50 US states, ≥10cm chest + ≥15cm back minimum), top-5 high-school-volume state-tier (Texas UIL / California CIF / Florida FHSAA / New York NYSPHSAA / Illinois IHSA, typically 14cm chest + 28cm back default), AAU national-sponsor (Adidas Gauntlet / Nike EYBL / Under Armour Association — each with sponsor-logo-vs-number clear-space rule), NCAA varsity (12-16cm chest + 25-30cm back), and amateur-rec. You select the applicable standard at order entry; our PM configures the per-PO registration template per standard and overhead-camera-checks every jersey at sublimation station for ±2mm tolerance compliance.

### Group B: Returning customer / AAU + HS conference + Park&Rec multi-team coordinator

**Q5: How does the squad-flex re-order rule work for AAU summer-circuit replacement jerseys between tournament weekends?**
A: Squad-flex re-order allows up to 20% of your original PO volume at zero added MOQ + 14-day turn. The 14-day turn fits the standard AAU between-event cadence: Sunday submit after Tournament 1 → Friday ship before Tournament 3 (7-day between-tournament gap with margin). Example: your original PO was 100 pieces across 8 AAU teams → you can re-order up to 20 pieces (lost / grown-out / contact-rebound tear) within 12 months at zero added MOQ. Per-size specification supported. Original sublimation panel + roster CSV + sponsor logo file retained 12 months on our server. For an emergency on-tournament-week replacement (<14-day turn), send us an inquiry-form note and we'll quote case-by-case Express Replacement pricing.

**Q6: My AAU national sponsor (Adidas Gauntlet / Nike EYBL / Under Armour Association) rebranded mid-circuit. How long does a sponsor-logo-only re-batch take?**
A: 14 calendar days for sponsor-logo-only update on the original PO panel — base design + player chest+back numbers + crest + secondary sponsors stay untouched. We retain the original sublimation panel + per-sponsor logo file for 12 months, and our sublimation line is configured so the sponsor layer is independently re-printable without re-running the base print. Send us your new AAU national sponsor brand-standards file on day 1; we produce a sponsor-comp sample on day 5-7 for sign-off, then bulk re-print on day 9-12, ship on day 13-14.

**Q7: What's your per-jersey number registration tolerance and how is it verified at the sublimation station?**
A: ±2mm on chest 12-16cm number AND ±2mm on back 25-30cm number SIMULTANEOUSLY per jersey, verified by overhead-camera registration template QC at sublimation station against the per-PO basketball-format template (configured per your selected rule-library standard). Out-of-tolerance jerseys (chest >±2mm OR back >±2mm) are pulled off the line and re-printed before packing. Number-and-name entry uses double-key verification (two operators enter independently from your roster CSV, system flags discrepancies before printing) to eliminate single-operator typo failures.

**Q8: I'm coordinating 8 AAU teams + 12 HS conference schools + 8 Park&Rec teams. Can you consolidate across all three program types into one PO with per-program sponsor + crest preservation?**
A: Yes — multi-team consolidation is the core of the Basketball Squad Pack. One PM, one PO number, one invoice across all teams + schools + recreational programs. Each program's sponsor + crest + player roster is preserved as a separate spec layer in the master order. Mid-season sponsor re-batches consolidate across all affected teams into one re-batch PO with one sponsor-comp sample sign-off cycle. Delivery typically structured per program calendar (AAU spring-summer circuit tournament weekend / HS conference season opener / Park&Rec season cycle), all consolidated in the same shipment window or split per delivery preference.

## S10: Certifications + Logo Wall + Inline Quote (D1+D2+D3+D4) [badge-row + logo-wall + quote-card hybrid]

**H2**: "Certified Basketball Apparel Factory: OEKO-TEX, BSCI, WRAP, GRS, and Higg"

**Sub**: "Five certifications. Each matters for a basketball-specific reason. Twelve brands, AAU programs, and HS conferences ship with us today."

### 5-Cert Badge Row (top)
- **OEKO-TEX Standard 100** — `23.HCN.74521` — Skin-contact safety for youth-age sublimation ink across U10-U17 AAU + youth-grassroots player base (youth-league textile safety rules).
- **BSCI** — `BSCI-CN-2024-08-15` — Procurement audit for AAU national-sponsor (Adidas Gauntlet / Nike EYBL / Under Armour Association) brand compliance and youth-tier sponsor-funded program transparency.
- **WRAP Gold** — `WRAP-GLD-156823` — Ethical sourcing for amateur-tier rec-league community brand integrity and state-tier athletic association brand-standards trust.
- **GRS** — `CU 1014387 GRS-2024` — Recycled-polyester basketball kits for state-tier athletic-association sustainability programs (increasingly required for NCAA DII-DIII + NIRSA campus club compliance).
- **Higg FEM** — `HIG-FEM-2024-CN-08` — Dye-house traceability for cross-school color consistency across HS conference multi-team orders (12 member schools' jerseys all match within ΔE ≤1.5).

### 12-Brand Logo Wall (middle)
Caption: "Trusted by AAU travel-team programs, NIRSA campus club basketball programs, HS athletic-conference equipment buyers, and Park & Rec multi-team coordinators across 4 continents — North America 42% / Europe 28% / Oceania 14% / Middle East 10% / Latin America 6%"

12-brand grid (3+3+3+3) using existing logo wall assets.

### Inline Quote (bottom)
> "We coordinated 8 AAU teams + 12 reversible practice jersey sets for the Adidas Gauntlet Spring Circuit, then needed 4 mid-circuit replacement jerseys between Tournament 1 in Indianapolis and Tournament 3 in Atlanta. They had our roster CSV + sponsor file on the server from the original PO. Sunday submit → Friday ship. We did not lose a single tournament weekend."
>
> — Marcus Reed · AAU Director of Operations, Carolina Basketball Academy · 8-team multi-circuit Basketball Squad Pack

Avatar: `query=basketball-coach-portrait&w=80&h=80` rounded (fallback to initial circle)

## S11: Final CTA + Inquiry Form (D1+D2+D3+D4) [dark final-CTA + embedded form]

**H2**: "Start Your Basketball Squad Kit Production"

**Sub**: "Replies within one business day. Original panel + roster CSV + sponsor logo file retained 12 months for re-orders, AAU between-event replacement, and mid-season sponsor re-batch."

### 4-Field Inquiry Form
- **Full Name** (text, required) — placeholder: "Your name"
- **Email** (email, required) — placeholder: "you@yourdomain.com"
- **Phone / WhatsApp** (tel, optional) — placeholder: "+1 555 000 0000"
- **Message** (textarea, required) — placeholder: "What basketball apparel do you need? Drop your squad design brief, roster CSV link, sponsor brand-standards file, or paste a reference jersey photo URL. Tell us your competition tier (Adult amateur 5-a-side / Youth U10-U18 / HS JV+Varsity / NCAA DII-DIII+NAIA+NIRSA campus club / AAU travel team + Summer circuit / Corporate + Church + Park&Rec), AAU age division if applicable (U13-U14 / U15-U16 / U17), state-tier athletic association if applicable (UIL / CIF / FHSAA / NYSPHSAA / IHSA / other), squad size, team count, and main sponsor names. Mention if you need reversible practice jerseys with per-side number printing, tear-away warm-up pants with 22-snap construction, or shooting sleeves as part of the kit. Season opener date or first tournament weekend date if you have one."

Honeypot: `name="website"` (hidden, anti-bot)
Hidden fields: `submission_time` + `page_url` (auto-injected by JS)
Submit button: "Send Your Inquiry" (full-width, brand-red solid)
Form action: `https://form.lianf.com/`

### Trust Line (below form)
"Replies within 1 business day · NDA on request · Sample fee waived after first PO · Original panel + roster CSV + sponsor logo file retained 12 months for re-orders and AAU between-event replacement · sales@berunactivewear.com"
