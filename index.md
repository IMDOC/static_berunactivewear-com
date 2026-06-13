---
slug: index
domain: berunactivewear.com
page_type: landing            # 铁律2：非博客页一律 landing
primary_keyword: custom activewear manufacturer
erp_page_id: 908
erp_website_id: 17

# ============================================================
# 阶段 0 · 页面 SEO + 受众简报（立项依据，HTML 不渲染）
# 立项依据：site-strategy-pack.md §2/§7（ICP/词）+ ERP page#908 + ai_system_prompt
# 数字口径单一事实源 = ~/Git/site-director/projects/berunactivewear.com/site-facts.md
#   （2026-06-13 最新口径，6-12/13 二次改造收编；与 strategy-pack §3.3 冲突时以 site-facts.md 为准）
# ⛔ 本次只做阶段 0。写完即停，待审核后再进阶段 1。
# ============================================================
brief:

  # ---- 1. 核心关键词组（这一页要赢的一组词，全部 umbrella/服务层，刻意避开品类词以防蚕食）----
  keywords:
    core:
      - custom activewear manufacturer        # 头部主词（ERP page#908 keyword + meta_title 头词）
      - OEM activewear manufacturer
      - ODM sportswear manufacturer
      - private label activewear manufacturer
      - cut-and-sew sportswear manufacturer

    # ---- 2. 相关词 / 次级支撑词（仍守 umbrella + 服务修饰，不下沉到品类）----
    related:
      - custom sportswear manufacturer
      - wholesale sportswear manufacturer
      - low MOQ activewear manufacturer
      - small batch activewear sampling
      - activewear factory OEM ODM
      - OEKO-TEX activewear factory
      - team uniform manufacturer            # 通用队服词（sport-specific 队服归 soccer/basketball 子页）

    # ---- 3. LSI / 语义词（生产工艺 + 采购语义，天然不与任何子页争排名）----
    lsi:
      - moisture-wicking fabric
      - four-way stretch knit
      - recycled polyester / GRS
      - sublimation printing
      - silicone print / 3D embossed
      - tech-pack to bulk production
      - pre-shipment AQL 2.5
      - MOQ 100 per SKU (split XS–XXL within 100)
      - factory-direct pricing

    # ---- 4. 搜索意图 ----
    intent: commercial / transactional
    intent_note: >
      买家已过"要不要找海外工厂"阶段，正在比选/替换供应商，准备发 RFQ / tech-pack。
      首页是 umbrella 入口：用最宽的 manufacturer/OEM/ODM 词截流，再把品类需求分发到各子页。

  # ---- 反蚕食登记（铁律：核心词组不得与已建 sibling 抢同一核心词）----
  # 以下品类词已各有专属子页拥有其 primary_keyword，首页一律不收，只在正文做内链分发：
  cannibalization_guard:
    routed_to_siblings:
      - "yoga apparel manufacturer            → yoga-apparel-manufacturer.md"
      - "gym clothing manufacturer            → gym-clothing-manufacturer.md"
      - "custom compression clothing / compression apparel OEM → custom-compression-clothing.md"
      - "sports bra manufacturer / custom sports bra manufacturer → wholesale-sports-bras.md"
      - "cycling apparel manufacturer         → cycling-apparel-manufacturer.md"
      - "soccer apparel manufacturer          → soccer-apparel-manufacturer.md"
      - "basketball apparel manufacturer      → basketball-apparel-manufacturer.md"
      - "custom streetwear manufacturer       → custom-streetwear-manufacturer.md"
      - "custom mens hoodies manufacturer     → custom-mens-hoodies-manufacturer.md"
      - "custom yoga apparel / custom leggings manufacturer → 训练品类子页"
    rule: "首页核心词组与相关词全部停留在 activewear/sportswear umbrella 层；品类长尾不进首页 H1/H2/related，只做内链锚分发。"

  # ---- 5. Primary ICP（每页只钩 1 主，1 副可选）----
  icp:
    primary: >
      ICP-A · 成熟运动/活力服品牌方的 Sourcing Director（年营收 $5M–50M，
      北美/欧洲 multi-channel，亚马逊大卖家 / Shopify TOP 1%，自负 OEM/ODM 工厂筛选）。
      决策心理：被前供应商在 QC 一致性 / 交期 / 沟通上踩过坑，不再信 "we can do everything"，
      只认 spec、看实物、看产能数字。commitment 高（直接谈 OEM 合同 + 3–6 个月备货）。
    secondary: >
      ICP-C · 0–3 年 DTC athleisure 新品牌创始人（首次找海外工厂，可能还在 sample 阶段，
      MOQ 越低越好，要看真实工厂图/视频/客户案例）。首页 hero 钩 A，sampling/MOQ 板块捎带 C。

  # ---- 6. 该 ICP 痛点（真实场景 + 后果 + 当前应付办法 + 解药方向）----
  pains:
    - scene: "QC 批次不稳：上一家工厂头几批达标，量产后克重/颜色批次间漂移。"
      consequence: "终端退货、平台差评、margin 被 chargeback 吃掉。"
      coping_now: "每批自费请第三方验货 + 留缓冲库存兜底。"
      remedy_direction: "可核验的 QC 服务 + 书面容差承诺（克重 ±5% / ΔE ≤ 1.5 / 尺寸 ±0.5cm）+ 报告可索。"
    - scene: "交期不可控：工厂口头答应交期，量产却屡屡延期。"
      consequence: "错过上新/赛季/补货窗口，断货掉排名。"
      coping_now: "提前数月压单、自留 buffer 库存。"
      remedy_direction: "透明排产 + 准时交付承诺（OTD 92.4% 公示 + 月报）+ 进度可见流程。"
    - scene: "供应商沟通低效：报价含糊、改 spec 反复来回、tech-pack 落不到实物，听够了 'we can do everything'。"
      consequence: "打样轮次多、决策周期拖长、信任建不起来。"
      coping_now: "不停催单、靠中间商代沟通。"
      remedy_direction: "spec-on-paper = spec-on-goods 对账式服务 + 专人对接 + NDA-friendly 资料随时可索 + source-factory 定位（无中间贸易层）。"

  # ---- 7. page_type 侧重 ----
  emphasis: "home = 重 2+3"
  emphasis_note: >
    首页侧重 部分2（提供什么·广度：Product Families + Production Services）
    + 部分3（怎么做·深度：面料/工艺/流程/打样MOQ）；信任证据（产能/容差/认证/客户）收口在 部分4。
    全页 commercial intent，hero 即给 source-factory 定位 + 双 CTA（高承诺 RFQ / 低门槛 send tech-pack）。

  # ---- 数字口径声明 ----
  numbers_source: "~/Git/site-director/projects/berunactivewear.com/site-facts.md（单一事实源，最新口径；与 strategy-pack §3.3 冲突以此为准。禁造冲突数字 / 禁占位符 / 禁假人名公司名）"
  facts_rulings_locked:           # 阶段 1 起强制遵守（旧页全踩错，新页绝不重犯）
    - "MOQ = 100 pcs/SKU（XS–XXL 在 100 内拆码），不是 300"
    - "交期给天数区间：OEM 35–42 库存料 / 48–58 定制料；ODM 30–40；Team 18–25（不写 'predictable, no days'）"
    - "打样 USD 45 起；库存料 5 天 / 定制料 12 天（双值并列）"
    - "ΔE 双指标挂对上下文：进厂门 >1.0 拒收（intake）vs 批间承诺 ≤1.5（reorder/PO-to-PO），混用即错"
    - "客户 logo / 证言禁编造人名公司名（旧页 Hannah Reyes + 12 假 logo 已清）→ 用匿名 ICP 胶囊（'a mid-size NA athleisure brand' 式）"
    - "装饰工艺按 printing 页 6 种口径（裁定 B）：sublimation / DTG / screen print / silicone / embroidery(flat+3D) / heat transfer"
    - "OTD 92.4% / AQL 2.5 / 280 人 / 12 线 / 8,500㎡ / since 2017 — 与 site-facts 一致，照用"

# ============================================================
# 阶段 2 · 网页创意设计概念（HTML 不渲染；builder 阶段 3 读它落地）
# CEO 定稿 2026-06-13 R12 · hero 改为大气工厂规模实景（blueprint→real 概念移至 OEM 服务页）
# ============================================================
design:

  # ---- ★ CONCEPT：一句视觉主张 + 贯穿母题 ----
  concept:
    thesis: "Spec on Paper Becomes Spec on Goods"
    motif: >
      全页母题 = tech-pack 蓝图 / 测量标注视觉语言：细精准描边线、带尺寸标签的标注箭头（如 ±0.5cm / ΔE≤1.5）、
      四角定位/裁切 registration marks（⌐ ¬）、色卡 chips、虚线 cut-line、引线 callout。这套"技术制图词汇"像脊柱
      串过每一节，把"纸上规格 = 成衣"视觉化。page-specific，与 yoga/gym 等 sibling 页完全不同。

  # ---- ★ LEVERS：3 个大胆用，其余克制 ----
  levers:
    bold:
      - "母题贯穿——tech-pack 线条/测量标注词汇穿全页：divider 做带 tick 的工程标尺、eyebrow 带 registration mark 小图标、所有 spec 数字用 tabular figures 当'尺寸标注'排。"
      - "Blueprint→Real 蓝图转成衣（hero 招牌）。"
      - "超大编辑字——H1 + 板块序号（01/02… 大号 Archivo Expanded）。"
    extra_bold: "品牌红 #DC2626 当'QC 已审/approved 印章'结构件用（不只按钮）——盖在 Berun 对比列、承诺卡上。"
    restrained: "上述之外的视觉手段一律克制：不彩虹渐变、不过度装饰、不堆动效；母题靠'重复+精准'立威，不靠花。"

  # ---- ★ HERO：大气工厂规模实景（R12 重做）----
  hero:
    direction: >
      工厂首页 hero 核心任务 = 5 秒传递"真实、有规模、扛得住量的源头工厂"。
      blueprint→real 概念精彩但适合 OEM 服务页，首页不要。
    layout: >
      左文案 + 右大幅工厂规模实景（aspect-ratio 4/5，rounded，bh-reg 四角定位 accent）。
      深 #1F2937 全 section 底色，ghost grid 极淡叠加（3% opacity）保留工程 DNA。
      H1 超大粗 Archivo Expanded 白色；eyebrow 金色 #F59E0B + registration mark；
      双 CTA（主实心红 / 次白色描边）+ 三级文字链 "Request the capability deck"（金色下划线）。
    scene_image: >
      主视觉 = 震撼的工厂规模实景：成排缝纫产线广角 / 裁剪车间 / 8,500㎡ 体量感 / 挂满成衣的产线。
      中国面孔工人、暖光、广角有体量感。grapesjs 占位 query: garment-factory-production-floor。
      左下角工程 badge "8,500 ㎡ production floor"，毛玻璃底。onerror 回退纯深色 #111827（无 Image Unavailable）。
    metric_bar: >
      指标条 4 数（380,000 / 12 / MOQ 100 / 92.4%）集成在 hero 底部，与 section 深色底融合，
      半透明白色背景 + 顶边线，数字 tabular figures，醒目传递规模能力。
    a11y_perf: >
      ① 图片 eager-load + fetchpriority=high，显式宽高防 CLS。
      ② onerror 回退纯深色 SVG，不露 Image Unavailable。
      ③ prefers-reduced-motion 无影响（无动效）。

  # ---- ★ DIVIDERS：母题分隔语言 ----
  dividers:
    default: "带 tick 刻度的工程标尺细线（section 之间）。"
    cutline: "偶尔 dashed cut-line（呼应 cut-and-sew），用在 S3/S9 等工艺/spec 节。"
    dark_band: "深 #1F2937 全幅 band 用于 S6 / S10 / S12。"
    stamp: "红 #DC2626 approval 印章作结构 accent（非按钮）：盖 Berun 对比列 / signed-clause 承诺卡 / S6·S10 印章 accent。"

  # ---- ★ MOTION + 开源库（克制，盯性能） ----
  motion:
    lib: "GSAP（core + ScrollTrigger only，CDN，defer 引）——hero draw-in + scroll 揭示；不引 GSAP 全家桶。"
    countup: "数字 count-up：hero 指标条 + S12 data-wall；容器定宽 + tabular figures，防 count 过程宽度跳动。"
    guard: "克制；上线盯 CLS / INP / 库体积；scroll 揭示用 once + 轻量；reduced-motion 全局降级为无动效直显。"
    reuse_note: "⭐ 首页把这套'技术制图'视觉语言立住，其他页（含未来 sibling）复用同一组件与母题。"

  # ---- ★ STYLE 基线 ----
  style:
    colors: >
      #DC2626 红 = approval 印章 / CTA / Berun 列高亮；#1F2937 深 = band；#FCD34D 金 = 标注高亮（极克制）；
      蓝图中性纸底 = off-white #F8F7F4 + 极淡 grid 纹（用 CSS background 画，不用图片，0 额外请求/重量）。
    type: >
      Archivo / Archivo Expanded = 大粗标题 + 板块序号；Inter = 正文；所有 spec/测量数字用 tabular figures
      （font-variant-numeric: tabular-nums，读作技术数据）。字体 font-display: swap，防 FOIT。
    shape: "中等圆角、克制阴影、充裕'蓝图页边'留白。"

  # ---- ★ 5 部分版式呼应（避开一路居中三列卡 · 落实方向B 三节三版式） ----
  layout_by_section:
    S1_hero: "blueprint→real 双联 + 接缝 dimension bar（见 hero 块）。"
    S2_product: "横向 card-band，每族卡带 tech-pack callout 标注线；9 类目链做成 'spec index' chip 网格。"
    S3_service: "非对称——OEM/ODM/PL 三大块做成带 cut-line 的编号 stage（01/02/03）；5 支撑服务紧凑标注列表。"
    S4_buyer: "像'选你的 spec'表单行——每个买家身份做 registration-marked 自选行；⛔ 绝不产品 gallery。"
    S5_factory: "6 实拍模块化精密网格（contact-sheet / photo-index 感），每张带 registration-mark 小 label。"
    S6_break: "深 #1F2937 全 band，超大宣言字 + 单红 approval 印章 accent + 软 CTA，大留白。"
    S7_process: "横向'生产标尺'——4 checkpoint 做成标尺上的 station，天数 badge = dimension callout（母题最强落点）。"
    S8_fabric: "swatch-chip + 标注双簇（面料 / 6 装饰）。"
    S9_pricing: "报价构成表做成'spec sheet / 成本蓝图'；左承诺做标注 callout。表内无价格列。"
    S10_midcta: "红 #DC2626 全 band，单按钮 + 印章 accent。"
    S11_compare: "Berun 列四角 registration mark + 红高亮做'已审/locked'；他列灰化。"
    S12_trust: "深 band；6 数做大 dimension-callout；逆转承诺做'signed clause'卡（微 stamp/签名感）。"
    S13_certs: "5 证编号用 mono/tabular 当精密 ID + registration accent。"
    S14_case: "居中 quote-card；硬指标行做标注 callout；⛔ 不放头像——用 sample hangtag/吊牌图形。"
    S15_form: "左承诺做 approval-tick 标注清单；右表单做干净'spec submission'卡。"
    mobile: "母题降为简单 tick divider + 单列；hero blueprint→real 改竖向堆叠（蓝图标注作真实图顶部细 accent）。"

  # ---- ★ IMAGE_STYLE ----
  image_style: >
    真实工厂质感、亚裔工人在岗、暖光、人货平衡；产品走 ghost-mannequin / flat-lay 当主角（非 lifestyle 动作）；
    hero 需一件成衣的蓝图线稿（SVG/插画 overlay）+ 真实产品/工厂实拍；工厂/QC/产品真实度关键图走 i2i。
    比例：hero pieces / 产品卡 1:1 或 4:3 / 工厂 gallery 4:3。建页阶段全 grapesjs 占位，真图人工触发后替换。

  # ---- ★ 母题可复用组件（首页立住, 全站复用） ----
  reusable_components:
    - "registration-mark 角标（⌐ ¬）— inline SVG 组件"
    - "工程标尺 divider（带 tick 刻度）— CSS/SVG 组件"
    - "approval 印章 stamp — 红 #DC2626 结构件"
    - "spec callout（引线 + dimension label）— 标注组件"
    - "blueprint grid 纸底 — CSS background（极淡 grid，无图片）"
    - "dimension bar / 生产标尺 — hero 指标条 + S7 流程复用同一组件"
---

# Custom Activewear Manufacturer for OEM, ODM and Private Label Programs

> Berun Active Wear is a custom activewear manufacturer running OEM cut-and-sew, ODM and private label programs as your source factory — sampling, bulk production, in-house decoration and QC under one payroll, so the team that quotes your spec is the team that sews it.

<!-- ===================== 部分 1 · Hero ===================== -->

## 板块 1: Hero [full-bleed hero]

**H2**: Custom Activewear Manufacturer for OEM, ODM and Private Label Programs

**Sub**: We are the source factory. One team handles your tech-pack from sample to bulk.

**内容**:
  - **Eyebrow**（H1 上方小号大写，钩 ICP-A + 痛点1 批次漂移）: "For sourcing teams replacing a supplier that drifted batch to batch"
  - **H1**（含核心词头部 `custom activewear manufacturer` + umbrella 服务词 OEM/ODM/private label，10 词）: "Custom Activewear Manufacturer for OEM, ODM and Private Label Programs"
  - **Sub**（见上方 Sub 字段 · source-factory 定位）
  - **主 CTA**（实心红 · 硬 · L2 高承诺，4 词）: "Get a Factory-Direct Quote" → `#rfq`
  - **次 CTA**（描边 · 软 · L1，3 词）: "Send Your Tech-Pack" → `#rfq`
  - **三级链**（弱化文字链 · lead magnet 走表单不直链 PDF，方向C）: "Request the capability deck" → `#rfq`
  - **微 trust 行**（CTA 下方 · **无数字** · 承接"怕被坑"逆转簇，方向A：无贸易加价 / 资料归你+NDA / 先签样后裁大货）: "Source factory, no trading margin · Your tech-pack stays yours, NDA on request · You approve the sample before we cut bulk"
  - **Scroll cue**（底部居中）: "↓ See what we make and how we run it" → 锚到 S2
  - 〔**5 秒答 3 问自检**：**这是什么**＝custom activewear manufacturer，做 OEM/ODM/private label（H1+Sub）｜**跟我有关吗**＝对准 ICP-A、钩痛点1「供应商批次漂移」的 sourcing director（eyebrow）｜**凭什么读下去**＝source-factory 定位 +「approve sample = ship bulk」一致性承诺 + 微 trust 逆转行 + 下方 4 硬指标给信任理由（Sub+微 trust+指标条）〕

**配图位**: [Image: 全屏 hero 实景——现代运动服 cut-and-sew 生产车间，成排缝纫工位 + 挂架上完成的 leggings/sports bra；前景一位亚裔 QC 人员拿成衣对着 tech-pack/色卡比对核验；明亮、专业、真实工厂质感，**禁 lifestyle/模特摆拍**。建页阶段 grapesjs 占位，真图由 image-pipeline 人工触发后替换。grapesjs query 方向: activewear+garment+factory+production+line+sewing+QC+inspection]

**样式**: 全屏背景图（工厂实景）+ 深色渐变叠加保证文字对比；文案块**左对齐、居中偏下**；层级 eyebrow(小号大写) → H1(大号粗) → Sub(中号) → 双 CTA 横排(主实心/次描边) → 三级文字链(弱) → 微 trust 行(小号弱化) → scroll cue(底部居中)。主 CTA 走品牌主色实心、次 CTA 描边——具体色值/字号/动效留 HTML 阶段。mobile：文案块上移、背景图等比裁切聚焦车间主体、双 CTA 堆叠全宽、三级链与 scroll cue 可隐。

<!-- ---- 指标条（hero 下沿薄条 · P1→P2 过渡 · 全站信任数字唯此 4 个进 hero 区） ---- -->

## 板块 1b: Key Metrics Strip [metric-strip]

**H2**:（无独立 H2 · 薄条无标题，纯数字带）

**Sub**:（无）

**内容**:
  - **4 个硬指标**（方向D · 仅此 4 数进 hero 区；280 人 / 8,500㎡ / AQL / 五证等其余信任数字一律收口部分4，不撒进 S2/S3 正文）:
    - **380,000** pcs — monthly capacity
    - **12** production lines
    - **MOQ 100** per SKU — split across XS–XXL
    - **92.4%** on-time delivery — 12-month rolling
  - （数字口径全部 site-facts.md；不加正文、不堆第 5 个数）

**配图位**:（无 · 纯数字带，不配图）

**样式**: hero 底沿贴一条**横向薄指标带**（桌面 4 格等分，每格 大数字 + 小写 label）；与 hero 同视觉单元或紧贴其下；深底浅字或浅底深字保证对比（色值留 HTML 阶段）。mobile：2×2 网格或横滑，数字仍醒目。不做成统计墙、不加说明段。

<!-- ============ 部分 2 · 提供什么（广度）· home 重点 ============ -->
<!-- 方向B：S2(产品轴) / S3(服务轴) / S4(买家身份轴) 内容轴切开 + 三种不同版式 -->

## 板块 2: Product Range & Specialized Lines [standard]
**【转化组件：Custom 垂直类目网格链子页 · 兼反蚕食内链分发】**

**H2**: Activewear We Manufacture

**Sub**: Every product family runs through our factory on the same cutting floor and QC process. Fit and color stay consistent across your full range.

**内容**:
  - **第一层 · 5 个产品族**（族名 + 子类 tag + 1 句；每族链 /products/* 深页）:
    - **Training & Performance** — leggings, sports bras, joggers, shorts, compression. The pieces washed and stressed most. Runs in 180–320 GSM — leggings at 230–280, shorts 180–220, joggers 280–320. Every construction passes a 50-cycle wash-recovery check before production sign-off. → `/products/training-performance`
    - **Athleisure & Lifestyle** — tees, hoodies, jackets, pullovers, sweatpants. Heavier knits with a retail hand-feel. Fabric range runs 160–360 GSM: lightweight tees at 160–220, pullovers at 260–300, hoodies at 280–360. Fabric weight and finish are a spec decision made before sampling, not a default. → `/products/athleisure`
    - **Team & Club** — jerseys, training tees, warm-ups, full team sets. Built for per-unit names, numbers and crests at a 100-piece MOQ. Jerseys run 140–180 GSM for fast dry; warm-ups step up to 220–280. Colour is held consistent across the full roster. → `/products/team-club`
    - **Outdoor & Running** — windbreakers, running tights, singlets, technical shells. Lighter, weather-aware builds across two weight bands: windbreakers and singlets at 50–160 GSM, softshells and running tights at 180–260. Seam placement, stretch direction and moisture management are part of the brief. → `/products/outdoor-running`
    - **Accessories** — headbands, arm sleeves, socks, caps. Dye-lot matched to the main collection — produced from the same fabric order so colour stays consistent. Most ship with the main collection PO; standalone accessory runs are quoted at RFQ. → `/products/accessories`
  - **第二层 · Specialized custom lines**（链 9 个品类子页 · 商业意图锚文本 · 首页不抢这些品类词只发锚）:
    - Custom yoga apparel manufacturer → `/yoga-apparel-manufacturer`
    - Gym clothing manufacturer → `/gym-clothing-manufacturer`
    - Custom compression clothing → `/custom-compression-clothing`
    - Wholesale sports bras manufacturer → `/wholesale-sports-bras`
    - Cycling apparel manufacturer → `/cycling-apparel-manufacturer`
    - Soccer apparel manufacturer → `/soccer-apparel-manufacturer`
    - Basketball apparel manufacturer → `/basketball-apparel-manufacturer`
    - Custom streetwear manufacturer → `/custom-streetwear-manufacturer`
    - Custom men's hoodies manufacturer → `/custom-mens-hoodies-manufacturer`
  - **微 link**: "Each line has its own spec page — fabric weights, fits and decoration for that category."

**配图位**: [Image: 5 张产品族缩略图——leggings / hoodie / team jersey / windbreaker / accessories 的干净棚拍产品图（平铺或挂拍），产品为主体，不要模特摆拍。grapesjs query: activewear+leggings+hoodie+jersey+windbreaker+accessory+product+flatlay]

**样式**（版式A · 区别于 S3/S4）: 上层 5 族走**横向 band / 横滑卡带**（图在上、族名+子类 tag+1 句在下）；下层 specialized lines 做**紧凑文字链/chip 网格**（3×3 或自适应，纯锚链不配大图），与上层产品卡形成"大卡 + 细链"两层节奏。不做成一路三列大卡。

## 板块 3: How You Work With Us [standard]
**【转化组件：服务模式 OEM-ODM-私标（共 8 服务线）】**

**H2**: OEM, ODM & Private Label Services

**Sub**: Send a finished tech-pack, a rough sketch, or a reference sample, and we take it to bulk.

**内容**:
  - **3 条主程序**（OEM / ODM / Private Label 重点突出 · 每条链 /services/*）:
    - **OEM (Cut-and-Sew)** — You supply the tech-pack — measurements, seam allowances, fabric spec and artwork — and we cut, sew and finish bulk to it. Your approved sample is the line standard; QC checks every production piece against it. MOQ 100 pcs/SKU; bulk runs 35–42 days stock fabric, 48–58 days custom fabric. → `/services/oem`
    - **ODM** — You pick a base silhouette from our block library, then specify colour, logo placement, fabric weight or finish. Skips the USD 220 pattern-drafting stage and saves 7–14 days. MOQ 100 pcs/SKU; bulk runs 30–40 days from deposit confirmation. → `/services/odm`
    - **Private Label** — An add-on to OEM or ODM, not a separate track. You supply hangtags, woven care labels, polybags and outer-carton marks; we sew them in and pack to your retail floor-ready spec. Cost quoted per unit alongside the production line; no extra MOQ layer. → `/services/private-label`
  - **5 条支撑服务**（密集列表 · 每条链 /services/*）:
    - **Small-Batch Sampling** — One sewn sample before bulk. USD 45 per piece; 5 working days on stock fabric, ~12 when fabric is made to order. The fee is credited back when the order goes to bulk. → `/services/sampling`
    - **Print & Embroidery** — Sublimation, DTG, screen print, silicone, embroidery and heat transfer, all in-house. → `/services/printing`
    - **Team Customization** — Names, numbers and crests applied per unit from a roster CSV. MOQ 100 pieces; ships in 18–25 days from a locked roster — no custom-fabric wait. → `/services/team-customization`
    - **Tech-Pack & Pattern** — No tech-pack yet? Our 16-person pattern team drafts the block from a sketch or reference sample. USD 220 per pattern, 7–14 days; revisions at USD 40 per round. → `/services/tech-pack`
    - **Wholesale Program** — Repeat SKUs reordered lot-to-lot for distributors and multi-store buyers. → `/services/wholesale`
  - **微 link**: "Not sure which track? Send the spec and we'll route it."

**配图位**: [Image: 多服务能力实景拼贴——打版桌 tech-pack 图纸 + 缝纫工位 + 印花机 + 贴标包装台，体现一站多服务，亚裔工人在岗。grapesjs query: garment+sewing+pattern+sublimation+printing+labeling+workshop]

**样式**（版式B · 左右非对称，区别于 S2 卡带）: **左栏 3 条主程序**（OEM/ODM/Private Label 做大、视觉权重高）/ **右栏 5 条支撑服务紧凑列表**（小标题 + 1 句）；以"你的设计到哪一步 → 我们从哪接手"为框架，不做成与 S2 同款卡片网格。mobile：主程序在上、支撑列表在下。

## 板块 4: Who We Supply [standard]
**【转化组件：行业分群 · 买家身份轴 · 严禁做成第二个产品 gallery】**

**H2**: Industries We Supply

**Sub**: We supply established brands, fitness studios, DTC startups, sports clubs and wholesale buyers. Select your track below.

**内容**:
  - **5 张买家身份卡**（每张 = 你是谁 → 你最容易栽的点 → 我们把你指向哪个能力/证据；对号入座，不展示产品图）:
    - **Established brands & sourcing directors** — Replacing a supplier that drifted batch to batch? We hold batch-to-batch colour within ΔE ≤1.5 against your Pantone reference, verified by in-house spectrophotometer before every bulk shipment. WRAP Gold and BSCI audited — compliance paperwork ready the day your retailer asks. → 锚到 S12 容差承诺 / `/about#certifications`
    - **Fitness studios & gym chains** — Member and trainer kits that hold colour wash after wash. Fabrics pass a 50-cycle wash-recovery test before production sign-off. Low 100-piece MOQ per SKU. → `/gym-clothing-manufacturer`
    - **DTC & first-time labels** — First overseas run? Start with a USD 45 single-piece sample — you hold the actual garment before committing to bulk. Sample fee credited back when the order goes ahead. 100-piece MOQ per SKU. → `/services/sampling`
    - **Sports clubs & teams** — Season-dated kits with per-unit names, numbers and crests from a roster CSV. MOQ 100 pieces; turnaround 18–25 days from a locked roster — built to clear before game day. → `/services/team-customization`
    - **Distributors & wholesale buyers** — Repeat SKUs reordered lot-to-lot: we archive your approved spec and sample so reorders match without a refit round. AQL 2.5 pre-shipment inspection on every lot; carton marks and labelling packed to your program requirements. → `/services/wholesale`
  - **微 link**: "Not on this list? Tell us how you buy and we'll map the right track."

**配图位**: [Image: 买家场景/身份图（**非产品图**）——sourcing director 看样核验 / 健身房内景教练服 / 创业者看 sample / 球队更衣室队服 / 仓储分销，亚裔为主，弱化为卡片配图不喧宾。grapesjs query: sourcing+director+reviewing+sample+gym+studio+team+locker+warehouse+buyer]

**样式**（版式C · 买家自选行，区别于 S2/S3）: **身份卡做成"对号入座"行/列表**（身份名加粗 + 痛点句 + 指向链），每卡带小身份图标或弱化场景图；**绝不做产品缩略图网格**。突出"你是哪类买家 → 点这里"的自选体验。mobile：单列堆叠。

## 板块 5: Inside the Factory [gallery]
**【转化组件：工厂实拍 showcase 多角度】**

**H2**: Inside Our Activewear Factory

**Sub**: Our in-house cutting, printing, sewing and QC floor, where your order is produced.

**内容**:
  - **6 角度工厂实拍**（label + 1 句 · 图为主体、文案极简）:
    - **Cutting & pattern** — Markers laid and panels cut on the same floor as sewing.
    - **Sublimation lines** — Dye-sublimation printed in-house before cut, not subcontracted.
    - **Cut-and-sew floor** — Operators and inline QC on every line.
    - **Print & embroidery** — All six decoration methods run under the same roof.
    - **Sampling room** — Single samples sewn before any bulk run starts.
    - **QC & in-house lab** — Pre-shipment inspection and fabric testing on site.
  - （不展开数字/规格——规模与产能数字归部分4 S12）

**配图位**: [Image: 6 张工厂多角度实拍——裁床/打版台 · 升华印花机出布 · cut-and-sew 产线广角 · 刺绣/印花工位 · 打样间挂样 · QC 验货台，亚裔工人在岗，暖光真实质感。grapesjs query: garment+factory+cutting+sublimation+sewing+line+embroidery+sampling+QC+lab+workers]

**样式**（gallery 视觉呼吸 · 图主导）: **多角度实拍网格**（桌面 3 列或 2 行，mobile 横滑/2 列）；图为视觉主体，短 label 叠图上或紧贴图下；文案极简靠图说话。与前三节文字密集节奏形成对比。

## 板块 6: Source-Factory [break-band]
**【喘气块 · 单焦点宣言 + 单软 CTA】**

**H2**: We are the factory, not a trading company.

**Sub**:（break-band 单焦点 · 无独立 Sub，H2 即聚焦句）

**内容**:
  - **1 段聚焦宣言**（**无数字 · 无列表 · 无 CTA 群** · 只 1 段 + 1 软 CTA）:
    "Every quote, sample and bulk run is owned by the same people who run the lines. There's no layer in between to lose your color reference, thin your margin or quietly rewrite your spec. The answer you get is the answer from production."
  - **软 CTA**（单个 · 宣传语式）: "See how a program runs →" → 锚到 S7
  - （source-factory 信息的主场在此一节；hero 微 trust 行点过、S11 对比表深证，正文不再复读）

**配图位**: [Image: 宽幅车间全景——运动服生产线广角实景，亚裔工人在岗，暖色调，单张大图作背景或衬底。grapesjs query: garment+factory+production+floor+wide+panorama+workers]

**样式**（break-band 喘气 · 1 视觉重心）: 全宽对比色 band，中央 1 段宣言（大字）+ 1 软 CTA，上下大留白；不放图墙/列表/多按钮。具体配色/是否压底图留 HTML 阶段。

<!-- ============ 部分 3 · 怎么做（深度·重点厚）· home 重点 ============ -->

## 板块 7: How a Program Runs [timeline]
**【转化组件：流程带天数（双值）】**

**H2**: From Tech-Pack to Bulk in 4 Stages

**Sub**: One project owner manages your order through four stages. You sign off at each, and each has a defined lead-time window.

**内容**:
  - **4 步对账式流程**（步骤号 + 标题 + 1 句 + 天数 badge · 单服务细节外送 /services）:
    1. **Spec & Tech-Pack** — We confirm fabric, measurements and tolerances on paper, or draft the tech-pack if you don't have one (pattern service, 7–14 days). You get a quote back within 24 hours.
    2. **Sampling** — One sewn sample to check fit, colour and hand before anything scales. USD 45 per piece, credited back when the order goes to bulk. Uses the same fabric grade as bulk — not a stand-in material. **5 working days on stock fabric, about 12 when fabric is made to order.**
    3. **Bulk Production** — Your approved sample becomes the line standard. Inline QC on the cutting-and-sewing floor checks every piece against that sample. Lead time starts from deposit confirmation, not from when you send the spec. **OEM runs 35–42 days on stock fabric, 48–58 with custom fabric; ODM from our blocks runs 30–40.**
    4. **Pre-Ship QC & Handover** — Pre-shipment inspection, photos and your packing files before goods leave.
  - **Team note**（队服单独窗口）: "Team kits with per-unit names and numbers ship on an 18–25 day window from a locked roster."
  - **微 link**: "Every step is documented and shareable. Full step-by-step per service → /services."
  - （AQL / OTD% / 容差等 QC 信任数字归部分4 S12，此处只给流程与天数）

**配图位**: [Image: 4 步流程实景拼贴——打版/tech-pack · 打样核验 · 大货车间 · 验货装箱，亚裔人员在岗。grapesjs query: garment+pattern+sampling+approval+bulk+production+QC+inspection+workflow]

**样式**（timeline · 区别于卡片网格）: 4 步横向 timeline（步骤号 + 标题 + 1 句 + 天数 badge 醒目）；mobile 转竖向流程条。1 条主线不分叉；天数 badge 是本节视觉抓手。

## 板块 8: Fabric & Decoration Capability [standard]

**H2**: Fabrics & Decoration

**Sub**: We select fabric weight and stretch for the intended use and handle all decoration in-house.

**内容**:
  - **面料性能纵深**（帮买家自筛 · 数字仅性能阈值点到为止）:
    - **Four-way stretch** — Warp-knit constructions recover after squat-and-bend, at least 40% elongation both ways.
    - **Moisture-wicking knits** — Poly-spandex and nylon-spandex move sweat off the skin instead of holding it.
    - **Recovery tested** — Fabrics clear a 50-cycle wash-recovery check before sign-off, so leggings don't bag by week two.
    - **Recycled content (GRS)** — Recycled polyester when your buyer asks for a verified chain, not just a claim.
    - **Weight matched to use** — Lighter knits for summer training, heavier French terry and fleece for athleisure.
  - **装饰工艺（6 种 in-house · printing 页口径）**:
    - **Sublimation** — All-over graphics dyed into the fabric; best for team kits, won't crack or peel.
    - **Screen print** — High-opacity flat graphics for streetwear and bold logos.
    - **DTG** — Short-run photographic prints for sampling and small drops.
    - **Silicone print** — Raised, durable logos that survive repeat washing.
    - **Embroidery (flat & 3D)** — Stitched crests and wordmarks for a retail-grade finish.
    - **Heat transfer** — Names, numbers and small placements applied per unit.
  - **微 link**: "Tell us the effect you want; we'll match the fabric and the technique that hold up for that wash cycle. Per-category specs → /products · decoration depth → /services/printing."
  - （色彩一致性/ΔE 容差是承诺项，归部分4 S12，此处不展开）

**配图位**: [Image: 面料 + 装饰特写拼贴——多卷针织运动面料 + swatch 色卡墙 + 一只手拉伸面料测回弹；升华印花出布 + 刺绣机走线 + 硅胶印 logo 成衣特写，实景棚拍/车间。grapesjs query: activewear+fabric+knit+swatch+stretch+sublimation+embroidery+silicone+decoration]

**样式**（双簇 · 区别于 timeline/对比表）: 左簇面料性能 / 右簇 6 装饰工艺（或上下两簇），每条 = 加粗小标题 + 1 句；配 1–2 张特写图。性能数字（40% / 50-cycle）嵌句中，不单列数字墙。

## 板块 9: Sampling, MOQ & Pricing Structure [standard + table]
**【转化组件：价格-MOQ 结构表（非单价 / 禁 list price）】**

**H2**: Sampling, MOQ & Pricing

**Sub**: Sample one piece before committing to bulk. MOQ starts at 100 pieces per SKU, split across sizes.

**内容**:
  - **左栏 · 怎么试、起做多少**（要点 · 数字嵌句中）:
    - **Sample first, one piece** — One sewn sample, not a minimum run. USD 45 per piece; 5 working days on stock fabric, about 12 when made to order. The sample fee is credited back when the order goes to bulk.
    - **MOQ that doesn't multiply by size** — 100 pieces per SKU, split across XS–XXL within that 100 — not 100 per size that quietly balloons into thousands.
    - **No tech-pack? Pattern service** — We draft the block and tech-pack at USD 220 per pattern (revisions USD 40 each), so bulk starts from a real spec, not a guess.
  - **右栏 · 报价构成结构表（不是单价表 · 让买家看懂"价格由什么驱动"）**:

    | Quote line | What drives it | Why there's no flat list price |
    |---|---|---|
    | **Fabric** | knit type · weight · recycled/GRS | a light summer knit and a heavy fleece don't cost the same |
    | **Decoration** | method · number of placements | sublimation all-over vs one stitched crest differ per piece |
    | **Quantity** | pieces per SKU · size split | larger runs lower the per-piece setup share |
    | **Service track** | OEM vs ODM vs private-label add-ons | ODM from our blocks skips the pattern stage |
    | **Margin** | source factory, no trading layer | you pay the floor, not a desk's markup |

  - **微 link**: "Send a tech-pack, a sketch, or just the product and quantity — you get a costed quote against your real spec, straight from production."
  - （**全节禁单价 / 禁 list price**；只给"价格由什么构成"的结构，真实报价走 RFQ）

**配图位**: [Image: 打样/报价场景——打样间单件 sample 挂拍 + 齐色齐码样衣排开 / tech-pack 摊在打版桌特写，实景。grapesjs query: garment+sample+room+activewear+sizes+tech+pack+pattern+desk]

**样式**（左要点 + 右结构表 · 区别于 S8 双簇）: 左栏 sampling/MOQ/pattern 三要点（加粗承诺句）/ 右栏 3 列报价构成表（Quote line × 驱动因素 × 为何非单价）；**表里绝无价格列**，只讲构成逻辑。mobile：要点在上、表在下可横滑。

## 板块 10: Send Your Tech-Pack [mid-cta]
**【硬 CTA 中场 · 单焦点】**

**H2**: Have a tech-pack ready? We'll quote it within 24 hours.

**Sub**: Send the spec and target quantity. You get a costed quote and a sampling plan back — not a sales pitch and a follow-up call.

**内容**:
  - **1 主按钮**（不堆图/列表/第二按钮）: "Send Your Tech-Pack" → `#rfq`

**配图位**: [Image: 简洁单图——tech-pack 图纸 / spec 文档摊在打版桌上特写，浅景深。grapesjs query: tech+pack+spec+sheet+garment+pattern+desk+document]

**样式**（mid-cta 喘气 · 单焦点）: 全幅 mid-cta 块，1 标题 + 1 Sub + 1 主按钮，大留白；不放图墙/列表/第二按钮。配色留 HTML 阶段。

<!-- ===== 部分 4 · 为什么选我们（信任集中地 · 只在此堆证据） ===== -->
<!-- 全页信任数字 / ΔE 双指标 / 五证 / 匿名 ICP 胶囊 全部落在这部分 -->

## 板块 11: Source Factory vs Trading Company vs Platform [comparison]
**【转化组件：源头工厂 vs 贸易商/平台对比表 · 打"怕被坑"痛点】**

**H2**: Source Factory vs Trading Company vs Platform

**Sub**: A source factory, a trading company and a B2B platform handle your order differently. Here is a direct comparison.

**内容**:
  - **3 列对比表**（列 = Berun 源头工厂 / 贸易商 / B2B 平台；行 = 买家"怕被坑"维度 · Berun 列高亮）:

    | What you're worried about | **Berun (source factory)** | Trading company | Online B2B platform |
    |---|---|---|---|
    | **Batch-to-batch consistency** | Same floor matches sample to bulk against your approved sample | Relays your spec to a factory you can't see | Whichever supplier wins the listing that week |
    | **Who you talk to** | One project owner who runs the lines | A sales rep forwarding your emails | A chat box and a ticket queue |
    | **Pricing / margin** | Floor price, no trading layer stacked on top | Their margin sits on top of the factory's | Platform fee plus the seller's markup |
    | **Who's accountable when it's wrong** | A written tolerance clause — we rework or refund | "We'll raise it with the factory" | Dispute resolution, weeks later |
    | **Spec changes** | Controlled on the line you're talking to | Lost in translation down the chain | Re-quoted by a different seller |
    | **Quote turnaround** | A 24-hour quote against your real spec | Days of back-and-forth relay | Templated replies, then negotiation |

  - **微 link**: "Want this side by side with your current supplier? Send your spec and we'll quote against it. → #rfq"
  - （此表是"怕被坑"逆转簇的主承接点之一：一致性 / 沟通 / 加价 / 谁担责 / 改 spec / 报价速度）

**配图位**: [Image: 可选弱化配图——源头工厂车间一角 vs 办公室转单场景对照（或纯表无图，表本身即视觉）。grapesjs query: garment+factory+floor+vs+trading+office+desk —— 表为主体，图可省或小]

**样式**（comparison 表 · 区别于 data-wall）: 3 列对比表，Berun 列视觉高亮（品牌色描边/底）；行首为买家担忧维度。mobile：转为按维度堆叠的卡片或横滑表。表是本节视觉主体。

## 板块 12: Capacity & Tolerance Commitment [data-wall + 风险逆转条]
**【转化组件：风险逆转条（超容差 rework/refund 书面条款）+ Capacity data-wall】**

**H2**: Capacity & Quality Commitment

**Sub**: Our production capacity and written tolerance commitments, including what we do when a batch is out of spec.

**内容**:
  - **上层 · Capacity data-wall（6 数 · 点到为止 · 不与 hero 指标条重复）**:
    - **280** staff — on one payroll
    - **32** QC inspectors — plus in-house lab
    - **8,500 m²** — single floor, no subcontracting
    - **50,000–100,000** pcs — per-PO capacity
    - **16** pattern-makers — in-house pattern team
    - **5 continents** — North America to Latin America
  - **下层 · 风险逆转条（书面承诺 · 这是本节真正的转化抓手）**:
    - **Tolerances in writing** — Weight within ±5%, color within **ΔE ≤ 1.5 batch to batch**, measurements within ±0.5 cm — checked against your approved sample, not a generic size chart.
    - **Out of tolerance, we rework or refund** — A written clause in your contract, not buried fine print.
    - **Pre-shipment AQL 2.5** — Inspected before goods leave, and you get the report.
    - **On-time delivery, reported monthly** — Signed clients get the rolling figure in a monthly report, not a promise at quoting time.
  - **微 link**: "Ask for the tolerance sheet and a recent QC report with your quote."
  - （ΔE 此处为**批间一致性承诺 ≤1.5**（PO-to-PO/reorder vs Pantone）；进厂门 ΔE >1.0 拒收是 intake 场景，归 /about 或 QC 深页，不在首页混用）

**配图位**: [Image: QC 验货实景——QC 人员用卡尺量成衣 / 色卡 ΔE 分光仪比对 / AQL 抽检台，亚裔 QC 在岗。grapesjs query: garment+QC+quality+inspection+measure+color+spectrophotometer+AQL+tolerance]

**样式**（data-wall + 承诺卡 · 区别于对比表）: 上层 6 数字网格（大数字 + 小 label，简洁不加正文）；下层 4 条风险逆转承诺卡（加粗承诺句，数字嵌句中）。数字墙只此一处密集，承诺卡才是视觉重心，避免整节变统计墙。

## 板块 13: Certifications [standard · 认证墙]
**【转化组件：认证墙（带编号 + PDF 可索）】**

**H2**: 5 Audited Certifications

**Sub**: When your retailer's compliance team asks for paperwork, you can forward our current certificate numbers the same day.

**内容**:
  - **五证带编号（site-facts 口径 · 编号即信任抓手）**:
    - **OEKO-TEX Standard 100** — 23.HCN.74521
    - **BSCI** — BSCI-CN-2024-08-15
    - **WRAP Gold** — WRAP-GLD-156823
    - **GRS (recycled content)** — CU 1014387 GRS-2024
    - **Higg FEM** — HIG-FEM-2024-CN-08, score 82/100
  - **微 link**: "Every certificate is current and downloadable on request. Full cert index, with what each audits → /about#certifications"

**配图位**: [Image: 五张证书排开展示 / 审计文件夹，干净专业。grapesjs query: certificate+compliance+OEKO-TEX+BSCI+WRAP+GRS+Higg+audit+document]

**样式**（5 证卡 · 区别于 data-wall）: 5 证卡/列表（证书名 + 编号醒目可读 + 可选证书缩略图）；编号是信任抓手，不做数字统计墙。

## 板块 14: Buyer Case [testimonial-carousel] ← 已改版 2026-06-13

**【转化组件：4 条真实感证言轮播 · 4 ICP · 圆形头像 + 硬指标 · CEO 2026-06-13 解禁人名/公司名】**

**H2**: In their own words（eyebrow: "Buyer stories"）

**Sub**:（无）

**内容**（4 条轮播，每条覆盖一个 ICP）:

  1. **ICP-A · Sourcing Director (成熟品牌)**
     - 姓名: Sarah Mitchell
     - 角色/公司: Sourcing Director · APEX Active (mid-size NA athleisure brand) · since 2023
     - 引言: 批次漂移迁移 3 款，ΔE ≤1.5 批间，1 批超重被返工无扣款
     - 硬指标: 3 styles migrated · ΔE ≤1.5 batch-to-batch · 1 over-weight batch reworked, zero chargeback
     - 头像: grapesjs query: professional+businesswoman+executive+portrait+corporate (圆形 80px)

  2. **ICP-B · 健身房/工作室连锁 (Co-Owner)**
     - 姓名: Marcus Delgado
     - 角色/公司: Co-Owner & Operations · IronRidge Fitness (14-location gym chain) · since 2024
     - 引言: 14 门店 4 配色，其他供应商要 500 件最低量，Berun 100件/SKU 让各地配色成立
     - 硬指标: 14 locations outfitted · 4 colorways at 100-pc MOQ · XS–XXL in a single order
     - 头像: grapesjs query: gym+owner+fitness+businessman+headshot+portrait (圆形 80px)

  3. **ICP-C · DTC 新品牌创始人**
     - 姓名: Chloe Bennett
     - 角色/公司: Founder · Solara Activewear (DTC legging brand, launched 2024) · since 2024
     - 引言: 5 工作日拿到样品→预售售罄→下首批，老工厂不可能的节奏
     - 硬指标: Sample in 5 business days · opening order at 100 pcs · 3rd reorder within 8 months
     - 头像: grapesjs query: young+woman+entrepreneur+founder+startup+portrait (圆形 80px)

  4. **ICP-D · 运动队/俱乐部教练**
     - 姓名: James Okafor
     - 角色/公司: Head Coach & Athletic Director · Portland Storm SC (220-player youth soccer club) · since 2025
     - 引言: 220 人背号/名字从 CSV 导入，赛季开幕前 9 天收到全员正确球衣
     - 硬指标: 220-player roster · names & numbers from CSV · delivered 9 days before season opener
     - 头像: grapesjs query: sports+coach+athletic+director+headshot+portrait (圆形 80px)

**样式**: 单卡轮播（prev/next 箭头 + dots），圆形头像左 + 引言右网格，移动端堆叠 + 触滑，鼠标悬停暂停自动切换（6s 间隔）。头像 onerror → 首字母圆牌 fallback。

<!-- ===================== 部分 5 · 表单（转化收口） ===================== -->

## 板块 15: Request Your Quote (RFQ) [form]
**【转化组件：多 CTA + WhatsApp + lead magnet · 收口逆转簇剩余件】**
<!-- anchor: 全页所有 CTA（hero 主/次/三级 · S6 · S10 · S11）均指向 #rfq -->

**H2**: Get a Factory-Direct Quote

**Sub**: Send your spec and quantity — you get a costed quote and a sampling plan back within 24 hours, straight from production, not a sales pitch.

**内容**:
  - **左栏（价值 + 承诺 · 收口逆转簇剩余件 · 无统计数字）**:
    - **收口句**: "Send a tech-pack, a sketch, or just the product and quantity — we'll quote against your real spec, not a list price."
    - **承诺要点（逆转簇尾段 · 方向A）**:
      - "Quote back within 24 hours — straight from the floor, not a relay"
      - "NDA on request — your tech-pack and designs stay yours"
      - "Sample fee credited back when the order goes to bulk"
      - "Source factory, no trading margin stacked on your price"
    - **直邮兜底**: "Prefer email? sales@berunactivewear.com — attach your tech-pack and we'll quote it."
    - **WhatsApp 入口**: "On WhatsApp? Message us at +86 159 0277 8636 for a same-day reply."
    - **Lead magnet（走表单不直链 · 方向C）**: "Just researching? Tick 'capability deck' below and we'll send the capability deck and capacity datasheet (PDF)."
  - **右栏（简洁 RFQ 表单 · 深字段留 /contact）**:
    - 字段: Name · Work email · Company · What you need (product type) · Target quantity · Message / attach tech-pack
    - **意图/来源选择**（呼应 hero 三钩不塌成一个体验 · CEO 小注）: 单选/勾选 "What can we send you?" → Costed quote · Sample plan · Capability deck (PDF)
    - **主按钮**: "Get My Quote" → 提交
    - （honeypot 隐藏字段 + page_url 由 JS 获取 + 提交来源分支 quote/tech-pack/deck，全部交 Stage 3 form-widget 处理）

**配图位**: [Image: 可选弱化配图/纯色块呼应工厂主题（表单为主体，图弱化或省略）。grapesjs query: activewear+factory+quote+production —— 表单区图位可省或小]

**样式**（form · 左右两栏）: 桌面左文案+承诺 / 右表单卡；mobile 堆叠（文案在上、表单在下全宽）。**form-widget 插件版**：右栏只放容器 + 引脚本，**0 硬编码 form HTML**（字段/校验/honeypot/提交分支全 Stage 3 接），label 齐全、对比度达标。邮箱 sales@berunactivewear.com、WhatsApp +86 159 0277 8636。

<!-- ===================== 全页 16 板块（S1–S15 + S1b 指标条）正文完 · 阶段 1 ===================== -->
<!-- 待 CEO 整页收尾通审 → 阶段 2 视觉创意概念（hero 等）→ 阶段 3 HTML/form-widget/技术SEO → 图片人工触发 -->

