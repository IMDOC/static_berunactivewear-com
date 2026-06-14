---
slug: about
domain: berunactivewear.com
page_type: landing            # 铁律2：非博客页一律 landing
primary_keyword: about berun active wear
erp_page_id: 917
erp_website_id: 17

# ============================================================
# 阶段 0 · 页面 SEO + 受众简报（立项依据，HTML 不渲染）
# 立项依据：site-strategy-pack.md §2/§7（ICP/词）+ ERP page#917 + site-facts.md
# 数字口径单一事实源 = ~/Git/site-director/projects/berunactivewear.com/site-facts.md
# ⛔ 本次只做阶段 0。写完即停，待审核后再进阶段 1。
# ============================================================
brief:

  # ---- 1. 核心关键词组（品牌可信度 / 公司背景 / EEAT 词；刻意不抢首页商业词）----
  keywords:
    core:
      - about berun active wear               # 品牌词（who-are-you 搜索）
      - berun activewear factory              # 工厂身份确认词
      - activewear factory company profile    # 买家调研类词（是谁/规模/背景）
      - who we are activewear manufacturer    # EEAT 品牌可信度词
      - custom activewear factory background  # 工厂资质/历程词

    related:
      - activewear manufacturer since 2017    # 成立年份时间线（历程类）
      - certified activewear factory          # 认证背书词（WRAP/GRS/Higg/BSCI/OEKO-TEX）
      - ethical activewear manufacturing      # 合规/文化类词（买家 ESG 审核入口）
      - activewear OEM factory team           # 团队/人员词
      - B2B activewear production partner     # 长期合作关系词

    lsi:
      - factory tour
      - company profile deck
      - WRAP Gold certified factory
      - Higg FEM 82 score
      - 280 workers single-payroll            # 规模佐证（防贸易商怀疑）
      - 8500 sqm single-facility              # 单一工厂无分包
      - 12 production lines
      - pattern makers in-house               # 团队能力（16 名打版师）
      - AQL 2.5 in-house QC lab

    # ---- 2. 搜索意图 ----
    intent: informational / trust
    intent_note: >
      买家已知道 Berun（从首页/子页进入），或正在 due-diligence（背景调查）阶段。
      搜索动机：确认对方是真工厂还是贸易商 / 了解规模/历史/团队 / 看有无合规认证。
      不是来比价、不是来查 MOQ——是来判断"这家工厂值不值得深入谈"。
      因此 about 的转化目标 = 建立信任纵深 → 引导预约工厂参观 / 索取公司 Profile Deck。

  # ---- 反蚕食登记（about 禁止抢首页/子页已占的商业词）----
  cannibalization_guard:
    no_steal_from:
      - "custom activewear manufacturer         → 首页 index.md 主词"
      - "OEM/ODM activewear manufacturer        → 首页主词组"
      - "MOQ 100 / lead time 35-42d             → 首页/服务页已深度讲，about 只一句话+内链"
      - "5 product families（training/athleisure/team/outdoor/accessories）
                                               → 首页/品类子页已展开，about 不展开"
      - "printing techniques (sublimation/DTG…) → 印花页/服务页，about 不展开"
      - "certifications 5 item list             → 首页已列，about 只一句话+资质背景故事"
    rule: >
      about 核心词全部停留在"这家公司是谁 / 规模 / 历程 / 团队 / 文化 / 合规" 层；
      商业 transaction 词（quote/get started/OEM/ODM/MOQ）不进 H1/H2/meta title，
      只在 CTA 和 footer 微量出现。

  # ---- 3. ICP（4 类共享，信任纵深对所有买家同等有效）----
  icp:
    all_four: true
    icp_note: >
      about 页不收敛 ICP，四类买家都会查"谁在做"：
      · ICP-A（成熟品牌 Sourcing Director）：做 due-diligence，需要工厂背景/认证/规模数字。
      · ICP-B（健身房连锁采购）：需确认对方是真工厂还是中间商。
      · ICP-C（DTC 新品牌创始人）：第一次找工厂，want to know "who is behind the factory"。
      · ICP-D（运动队/俱乐部）：确认工厂有团队服定制能力 + 交期可靠。
    shared_pain: >
      最大公约数痛点 = "怕找错工厂"：
      - 怕是贸易商（分包、无实际产能、质量无管控）
      - 怕没实力（规模小/人手少/设备老/无认证）
      - 怕没有合规（无 WRAP/BSCI/GRS 等买家方 ESG 硬要求）
      - 怕数据说不清楚（工厂自我描述含糊、没有真实数字/照片）
      about 页用"谁在运营、做了多久、什么规模、什么认证、什么文化"来正面回答。

  # ---- 4. 核心痛点（真实场景 + 后果 + 解药方向）----
  pains:
    - scene: "不知道对面是工厂还是贸易商——网站看起来都一样，报价也差不多。"
      consequence: "打了样才发现对方分包、一致性无法控制，白费打样费和时间。"
      coping_now: "要求工厂视频、问有没有营业执照、看 Alibaba/Made-in-China 评级。"
      remedy_direction: >
        about 展示：单一工厂 8,500 ㎡（无分包）、280 名员工 single-payroll、
        12 条自有产线——用具体数字而非口号证明实力。
    - scene: "合规要求越来越严（ESG/碳足迹/认证），不知道工厂有没有达标。"
      consequence: "品牌被采购审核打回、付了定金工厂却无法提供 BSCI/GRS 证书。"
      coping_now: "要索证书（常遇'证书更新中'推辞）。"
      remedy_direction: >
        about 把 5 项认证（WRAP Gold / GRS / Higg FEM 82 / BSCI / OEKO-TEX）
        放在工厂文化/合规文化叙事语境下讲，不只是 logo 堆列——说明为什么做、审核频次、审核机构。
    - scene: "看不到工厂真实状态——只有精修图，不知道实际产能和团队水准。"
      consequence: "合作后发现与预期差距大，换供应商成本极高。"
      coping_now: "要求视频、亲自去中国工厂看厂（成本高、时间长）。"
      remedy_direction: >
        about 提供"虚拟工厂参观"CTA（视频/照片）+ 团队人物简介，
        让买家不出门就能完成初步工厂尽调。

  # ---- 5. about 独占内容区块（首页/子页禁止出现）----
  exclusive_content:
    - 工厂历程时间线（2017 年创立 → 关键里程碑 → 今天）
    - 团队人物介绍（Anna 销售团队 / QC 团队 / 打版师团队 —— 真名 Anna 之外其余匿名）
    - 工厂文化/运营理念（每日 7:45 白板排程、面料到厂 4 小时验布等运营细节）
    - 合规文化叙事（5 项认证的"为什么做"而非"我们有"）
    - 工厂参观 CTA（Book a virtual factory tour）
    - 公司 Profile Deck 下载入口（Request company profile deck）

  # ---- 去重声明（首页已讲，about 只一句话+链接）----
  already_covered_by_homepage:
    - "5 服务线（OEM/ODM/Private Label/Sampling/Team Custom）→ 一句话+/services 内链"
    - "4+1 产品族展开清单 → 一句话+/products 内链"
    - "5 认证 logo 列表 → about 只讲认证背景故事，logo 一行即止"
    - "MOQ 100 / 交期 / 打样费 → 只在 FAQ-style 句子里带过+/faq 内链"
    - "月产 380K pcs / 产线 12 条 → about 可引用但要放在工厂规模叙事语境，不再展开成信息板块"

  # ---- 6. CTA 方向（关系型，不是交易型）----
  cta:
    primary:   "Book a Virtual Factory Tour"          # 最低门槛：视频参观，无需出行
    secondary: "Request Company Profile Deck"         # 中间承诺：索取 PDF 资料
    tertiary:  "Talk to Anna"                          # 高承诺：直接联系销售
    forbidden_cta:
      - "Get a Quote"      # 首页已用
      - "Send Tech-Pack"   # 首页已用
      - "Start Your Order" # 交易型

  # ---- 7. page_type 侧重 ----
  emphasis: "about = 重 3+4"
  emphasis_note: >
    重3（细节深度）：工厂历程/团队人物/运营细节/合规文化——让买家看到"这家工厂怎么运作的"。
    重4（信任集中）：5 项认证背书故事 + OTD 92.4% 公开数字 + 真实工厂规模数字——买家 due-diligence 核心诉求。
    重1/重2（产品/服务广度）在 about 只做分发，不展开——已有首页+子页覆盖。

  # ---- 数字口径声明 ----
  numbers_source: "~/Git/site-director/projects/berunactivewear.com/site-facts.md（单一事实源）"
  facts_rulings_locked:
    - "MOQ = 100 pcs/SKU（XS–XXL 在 100 内拆码），不是 300"
    - "工厂面积 8,500 m²，单一工厂无分包"
    - "280 人 single-payroll：180 缝纫工 / 36 裁剪 / 24 印花刺绣 / 32 QC / 8 实验室技工；16 名打版师"
    - "12 条产线：5 cut-and-sew / 4 sublimation / 3 team-set"
    - "月产 380K pcs；准时交付率 92.4%（rolling 12 个月）"
    - "成立 2017 年（8 年）"
    - "5 认证：WRAP Gold（WRAP-GLD-156823）/ GRS（CU 1014387 GRS-2024）/ Higg FEM（82/100）/ BSCI / OEKO-TEX Standard 100（23.HCN.74521）"
    - "ΔE 双指标：进厂门 >1.0 拒收（intake）vs 批间承诺 ≤1.5（reorder）"
    - "联系人：Anna / sales@berunactivewear.com / +86-159-0277-8636"
    - "客户 logo / 证言禁编造人名公司名 → 用匿名 ICP 胶囊"
    - "正文禁出现 China / Guangzhou / 中国 / 广州（只在 footer/Schema）"

# ============================================================

# ============================================================
# 阶段 2 · 创意设计概念（HTML 不渲染；阶段 3 builder 读它落地）
# CEO 定稿 2026-06-13
# ============================================================
design:

  concept:
    name: "On the Record"
    tagline: "一家被记录、被审计、看得见的真工厂"
    rationale: >
      About 页的买家任务 = due-diligence（这家是不是真工厂 / 有没有实力合规）。
      视觉母题 = 凭证 / 档案 / 审计语言：verified/approved 审计印章 accent、
      年份时间戳、ID 卡式团队卡、证书封印式 cert 块、"on file / documented" 调性。
      一切都有记录、被审计、是真的 —— 视觉化打消"怕找错工厂"。
      区分首页"spec=goods 蓝图"母题，about 走档案感，两页视觉语言完全不同。

  # ---- Hero 设计（S1）----
  hero:
    concept: "公司档案封面 / 可信记录"
    rationale: >
      不是销售 hero，不是工厂规模截流 hero。
      呈现方式 = 一份被核验的公司记录：真实工厂实景或团队合照作为 hero 背景，
      公司身份信息（Since 2017 / 单一工厂 / 280 人）像档案封面上的字段一样呈现，
      不是 marketing slogan。
    bg: "深色 overlay 工厂或团队实景图（暖光、纪实感，非广告精修）"
    layout: "左侧文字 + 右侧图片（或全宽图 + 深 overlay 文字居左）"
    stat_badges:
      style: "'verified facts' 徽章感 —— 带红 ✓ 印章 accent，tabular-nums 字体"
      items: ["8 Years Operating ✓", "280 Workers, Single Payroll ✓"]
    cta_style: "关系型，非交易型；primary 红底白字，secondary 白边透明"
    image_notes: >
      工厂实景（车间、产线、面料检测）或团队合影。
      中国/亚洲面孔，暖光，纪实感，不塑料。
      i2i 风格（有真实参考时优先）；grapesjs 占位待真图。

  # ---- 设计 Levers（3 个大胆用）----
  levers:
    - id: lever_1
      name: "审计印章母题"
      usage: >
        红色 ✓ 印章 accent 贯穿全页：
        · Hero stat badges 带 ✓（verified facts 感）
        · S6 cert 块每项认证带印章封印式边框 + cert number 等宽字体打印样式
        · S7 信任数字每个 stat card 右上角小 ✓ 印章
        · 颜色：#DC2626 红 = 审计 ✓ 印章；#FCD34D 金 = 标注/批注
      avoid: "不要做成真实法律印章（太庄重），保持设计化 accent 即可"

    - id: lever_2
      name: "时间线做成有记录的年表"
      usage: >
        S3 时间线：
        · 每个节点左侧大字年份（tabular-nums，#DC2626 红色强调）
        · 节点圆形做成档案骑缝印 / 时间戳感
        · 滚动进入时节点 reveal 动效（贴合"年表翻页"感）
        · 右侧穿插工厂实景图（小尺寸，纪实风）
      layout: "居中垂直时间线，左年份 + 右文字，图片穿插在偶数节点右侧"

    - id: lever_3
      name: "ID 卡式团队卡 + 证书封印式 cert 块"
      usage: >
        S4 团队卡：
        · 每张卡做成 ID badge 感：头像圆形（passport 比例）/ 姓名 + 职位像工牌字段
        · 背景用轻网格纹或浅灰；右下角小印章图标（工厂内部"授权"感）
        S6 cert 块：
        · 每项认证：logo + cert number 用等宽字体（像官方文件编号）
          + 叙事文字 + 右侧"文件封印"边框装饰
        · 整体像一份摊开的合规文件夹

  # ---- 背景图 Band 规划（满版图 + 深 overlay）----
  image_bands:
    - section: "S1 Hero"
      bg: "工厂车间全景或团队大合影，深 overlay（opacity 0.55–0.65），文字在 overlay 上"
      image_ratio: "16:9 or full-viewport-height"

    - section: "S5 Operations"
      bg: "车间深色暗调底图（生产线/缝纫工序），overlay #1F2937，白字"
      image_ratio: "16:7 banner"

    - section: "S7 虚拟参观邀约 band（可选）"
      bg: "工厂入口或展示区实景图，overlay 深红 #7F1D1D，白字邀约语 + CTA"
      image_ratio: "16:5 slim banner"

    rule: "flat 与图 band 交替出现，图 band 不超过 3 处，保持阅读节奏"

  # ---- Shape Divider 过渡 ----
  shape_dividers:
    count: "2–4 处，不铺满全页"
    variants:
      - "Hero → S2: wave（白浪入灰）"
      - "S3/S4 → S5: slant（白斜切入深色）"
      - "S6 → S7: arc（白弧入浅灰）"
    avoid: "连续多个 divider 堆叠；divider 颜色与相邻 section 对比度不足"

  # ---- 克制动效 ----
  animations:
    - target: "Hero stat badges（8 Years / 280 Workers）"
      type: "数字滚动计数（countUp）from 0"
      trigger: "进入视口时触发一次"
      duration: "1.2s ease-out"

    - target: "S7 trust stat cards（92.4% / 280 / 8,500 / 8 Years）"
      type: "数字滚动计数（countUp）"
      trigger: "进入视口时触发一次"
      duration: "1.5s ease-out"

    - target: "S3 时间线节点"
      type: "滚动 reveal —— 每个节点 fade-in + slide-up，从下到上依次触发"
      trigger: "IntersectionObserver，每节点独立触发"
      duration: "0.5s per node, 0.2s stagger"

    - target: "S6 cert 块"
      type: "微 stamp 动效 —— 每个 cert card 进入视口时印章 ✓ icon scale 1.0→1.15→1.0（弹一下）"
      trigger: "IntersectionObserver"
      duration: "0.3s bounce"

    rule: "只这 4 处动效，其余静态；禁 parallax / 禁自动轮播 / 禁 hover 文字消失"

  # ---- 图片调性 & 来源 ----
  image_style:
    tone: "真实纪实工厂/团队风格 —— 暖光、非广告精修、真实感"
    subject_notes:
      - "工厂工序图：缝纫工、裁床、面料检测、产线白板 —— 中国/亚洲面孔"
      - "团队头像：ID 卡式（圆形裁切，passport 比例，中性背景或工厂环境）"
      - "证书 logo：官方真实 logo（WRAP / GRS / Higg / BSCI / OEKO-TEX）"
    process: "走 i2i（有真实参考图优先）；无参考时 t2i + 详细 prompt"
    placeholder: "阶段 3 建站时 grapesjs 占位（[TODO: image of ...]），阶段 4 通过后换真图"
    ratios:
      hero: "3:2 or 16:9"
      team_headshot: "1:1（圆形裁切）"
      timeline_node: "4:3"
      ops_banner: "16:7"

  # ---- Design Token（复用站点已有）----
  tokens:
    colors:
      red:  "#DC2626  → 审计 ✓ 印章 / CTA primary / 年份强调"
      dark: "#1F2937  → 深色 band / overlay / 正文深色"
      gold: "#FCD34D  → 标注 / 批注 accent / 时间线节点圆心"
    typography:
      heading:      "Archivo（站点已有）"
      body:         "Inter"
      numbers:      "tabular-nums —— 所有年份/数字/cert 编号/事实数据强制使用"
      cert_numbers: "monospace（Courier New fallback）—— 模拟官方文件编号感"
    spacing: "Bootstrap 5 spacing scale；section padding-y: 80–100px"

  # ---- Section 布局快速索引（2026-06-14 扩充版）----
  layout_map:
    S1_hero:      "full-width dark-overlay-image / left-text right-image"
    S2_products:  "light-gray bg / centered 2-col cards / no image"
    S3_timeline:  "white bg / centered vertical timeline / 4 nodes / image at even nodes"
    S4_team:      "paper bg / 4-col ID-card grid / circular headshots"
    S4b_team_grp: "white bg / 2-col dept group cards (Sewing/QC/Pattern/Sales) / 4 main photos + 6 mini thumbs"
    S4c_values:   "paper bg / 2-col 4-value cards / icon-grid / left red-stripe accent"
    S5_ops:       "dark-image-band / 2-col icon list / 6 items + 3-photo factory strip"
    S6_certs:     "white bg / left logo col + right narrative col"
    S7_stats:     "paper bg / 4 stat cards + invite para + 2-row gallery (7 images total)"
    S7c_feedback: "dark bg / 3-col testimonial cards / archive-style buyer quotes + metrics"
    S7b_invite:   "deep-red-overlay-image slim band / tour invite + CTA"
    S8_contact:   "dark bg / 3 option cards + form / Anna avatar left"

# ============================================================
# 阶段 1 · 五部分正文（9 sections）
# CEO 定稿骨架 2026-06-13；正文一次性写完
# ============================================================
sections:

  # ----------------------------------------------------------
  # 部分 1 · Hero（S1）
  # ----------------------------------------------------------
  - id: s1_hero
    part: 1
    label: "Company Identity Hero"
    bg: dark
    layout: "full-width, left-text right-image (factory floor / team photo), 2 stat badges bottom"

    meta_title: "About Berun Active Wear — Activewear Factory Since 2017"
    meta_description: "8-year single-facility activewear factory. 280 workers, 12 production lines, 380K pcs/month. WRAP Gold, GRS, Higg FEM 82, BSCI, OEKO-TEX certified."

    h1: "Berun Active Wear — Activewear Factory Since 2017"
    sub: >
      Single 8,500 m² facility, 280 workers on one payroll, 12 production lines.
      Serving sportswear brands, gym chains, and DTC startups across North America, Europe, and ANZ.

    bullets:
      - "Single factory, 8,500 m², no subcontracting at any stage. All 12 production lines are on-site and owner-operated under one roof."
      - "280 workers on a single payroll — 180 machinists, 36 cutting and pattern staff (including 16 pattern makers), 24 print and embroidery workers, 32 QC, and 8 lab technicians."
      - "OEM and ODM clients across North America (42%), Europe (28%), ANZ (14%), and other markets — repeat orders from sportswear brands, gym chains, and DTC labels."

    stat_badges:
      - "8 Years Operating"
      - "280 Workers, Single Payroll"

    cta_primary:   "Book a Virtual Factory Tour"
    cta_secondary: "Request Company Profile Deck"

  # ----------------------------------------------------------
  # 部分 2 · 提供什么，简·分发（S2）
  # ----------------------------------------------------------
  - id: s2_what_we_make
    part: 2
    label: "What We Make — one-liner + internal links"
    bg: light-gray
    layout: "centered 2-column cards (Products / Services), internal links below each"

    h2: "What Berun Produces and Offers"

    card_products:
      heading: "Product Families"
      body: >
        Berun manufactures across four main categories — training and performance
        (leggings, sports bras, joggers, compression), athleisure (tees, hoodies,
        jackets), team and club (jerseys, warm-ups, team sets), and outdoor and
        running (windbreakers, tights, singlets) — plus accessories produced in
        matching fabric and colorways.
      cta_text: "View All Products"
      cta_href: "/products"

    card_services:
      heading: "Production Services"
      body: >
        Core services: OEM cut-and-sew, ODM style development from Berun's library,
        private label (branded hangtags, care labels, polybag, carton), sampling,
        in-house print and embroidery (six techniques), team customization with
        roster-driven numbering, tech-pack and pattern work, and wholesale programs.
      cta_text: "View All Services"
      cta_href: "/services"

  # ----------------------------------------------------------
  # 部分 3 · 细节深度（S3 · S4 · S5）
  # ----------------------------------------------------------
  - id: s3_timeline
    part: 3
    label: "Factory History Timeline"
    bg: white
    layout: "centered vertical timeline, 4 nodes, alternating text and image"

    h2: "Berun Factory History: 2017 to Now"

    nodes:
      - year: "2017"
        title: "Founded"
        body: >
          Berun opened with three cut-and-sew lines focused on performance leggings
          and sports bras for North American wholesale buyers. The founding team came
          from sportswear manufacturing backgrounds. Output in the first year was
          under 50,000 pcs per month, with a single customer segment and a tight
          product scope.

      - year: "2020"
        title: "12-Line Expansion"
        body: >
          Production expanded to 12 lines — five cut-and-sew, four sublimation,
          and three team-set — with all lines housed in the current 8,500 m² facility.
          The sublimation department was added in-house, eliminating reliance on
          outside print vendors. Monthly capacity crossed 200,000 pcs.
          OEKO-TEX Standard 100 first certification obtained this year.

      - year: "2023"
        title: "QC Lab Upgrade + OEKO-TEX Renewal"
        body: >
          The in-house QC lab added spectrophotometric colorimetric testing, allowing
          incoming fabric measurement against approved lab dips at ΔE accuracy.
          OEKO-TEX Standard 100 renewed under certificate 23.HCN.74521, covering
          both fabric and finished garment harmful-substance testing.
          BSCI social compliance audit (BSCI-CN-2024-08-15) passed with no major findings.

      - year: "2024"
        title: "WRAP Gold + GRS + Higg FEM — Full Compliance Stack"
        body: >
          WRAP Gold certification (WRAP-GLD-156823), GRS (CU 1014387 GRS-2024),
          and Higg FEM (HIG-FEM-2024-CN-08, score 82/100) were all completed in
          2024, giving clients a full compliance documentation set for ESG
          supplier qualification. Monthly output reached 380,000 pcs across all
          12 lines, with on-time delivery holding at 92.4% rolling 12-month average.

  - id: s4_team
    part: 3
    label: "Team"
    bg: white
    layout: "4-person card grid, photo placeholder + name + role + 2-sentence bio"

    h2: "The Team Running Berun"

    members:
      - name: "Anna"
        role: "Sales Manager"
        photo: "[TODO: image of Anna, Sales Manager, professional headshot]"
        bio: >
          Anna handles all inbound B2B inquiries from RFQ to bulk shipment confirmation.
          She responds to quote requests within 24 hours with confirmed service track,
          MOQ applicability, lead time range, and initial pricing direction.
          Clients with active orders reach her directly via WhatsApp or email
          for sample tracking, spec questions, and shipment status.
        contact_email: "sales@berunactivewear.com"
        contact_phone: "+86-159-0277-8636"

      - name: "Marcus Lin"
        role: "Head of Production"
        photo: "[TODO: image of Marcus Lin, Head of Production, factory floor or office]"
        bio: >
          Marcus has managed activewear production scheduling for 15 years.
          He runs the 7:45 AM daily production board, allocating each of the 12
          lines by ship-date priority and adjusting for material availability in
          real time. He coordinates the cutting, sewing, and finishing sequence to
          hold the 92.4% on-time delivery rate across all order types.

      - name: "Jenny Zhao"
        role: "QC Manager"
        photo: "[TODO: image of Jenny Zhao, QC Manager, lab or inspection area]"
        bio: >
          Jenny leads the 32-person QC team covering inline inspection on every
          production line and AQL 2.5 pre-shipment sampling on every order.
          She manages the colorimetric records for each batch — incoming fabric
          measured against approved lab dips (ΔE >1.0 rejected), and batch-to-batch
          reorder consistency tracked at ΔE ≤1.5 — and holds sign-off authority
          on all outbound shipments.

      - name: "David Tang"
        role: "Head Pattern Maker"
        photo: "[TODO: image of David Tang, pattern maker at work, table with patterns]"
        bio: >
          David leads the 16-person pattern and grading team. He converts client
          tech-packs into production-ready patterns, grades from XS to 5XL, and
          manages revision cycles at USD 40 per round with a 2–5 working-day
          turnaround per revision. New style patterns are typically completed
          in 7–14 working days from confirmed tech-pack.

  # ----------------------------------------------------------
  # 部分 3b · Team Groups — 280 人群像（S4b）2026-06-14 新增
  # ----------------------------------------------------------
  - id: s4b_team_groups
    part: 3
    label: "The 280-Person Team — Department Groups"
    bg: white
    layout: "2-col 4-card grid / main dept photo + optional mini thumbnail strip"
    h2: "The 280 People Behind Every Order"
    sub: "Four department leads run the operation. Behind them: 280 direct employees in one building, no subcontracting at any production stage."

    groups:
      - dept: "Sewing Production"
        headcount: "180 machinists"
        lines: "5 cut-and-sew + 4 sublimation + 3 team-set"
        desc: >
          Every machinist is assigned to a single line for their full shift. Each line of
          22–24 operators runs under one line supervisor feeding Marcus's 7:45 AM board.
          No sewing or sublimation work goes outside the facility.
        photo: "[TODO: group photo of sewing production floor, multiple machinists at machines]"
        mini:
          - "[TODO: close shot of machinist sewing activewear leggings]"
          - "[TODO: sewing line running at capacity]"
          - "[TODO: sublimation press in operation]"

      - dept: "Quality Control Team"
        headcount: "32 QC workers + 8 lab technicians"
        desc: >
          Jenny's QC team runs at two levels: inline workers per production line
          checking every 30-piece interval, and lab technicians running AQL 2.5
          pre-shipment sampling and colorimetric sign-off before every outbound order.
        photo: "[TODO: QC team conducting inline check, garments at inspection station]"
        mini:
          - "[TODO: inline QC measurement check during production run]"
          - "[TODO: lab tech using spectrophotometer for color testing]"
          - "[TODO: pre-shipment AQL 2.5 random sampling table]"

      - dept: "Cutting & Pattern"
        headcount: "36 cutting workers + 16 pattern makers"
        desc: >
          David leads 16 pattern makers converting tech-packs to production-ready patterns
          (XS–5XL), while 36 cutting workers process 15,000 panels per shift. All grading
          and revision cycles stay in-house.
        photo: "[TODO: cutting room floor with fabric panels and cutting tables]"

      - dept: "Sales & Client Support"
        headcount: "Anna-led team"
        desc: >
          All inbound B2B inquiries — from first RFQ through sample sign-off, bulk
          production tracking, and shipment confirmation. Every active client has a
          named contact. New RFQ response: 24 business hours, reviewed.
        photo: "[TODO: sales team reviewing order specs at desk, professional environment]"

    image_note: "All photos: real factory workers, Asian faces, warm documentary light. No stock."

  # ----------------------------------------------------------
  # 部分 3c · Values — 经营理念（S4c）2026-06-14 新增
  # ----------------------------------------------------------
  - id: s4c_values
    part: 3
    label: "Operating Principles / What We Stand For"
    bg: paper
    layout: "2-col 4-value icon-cards, left red-stripe border accent"
    h2: "Four Principles Running Every Order"
    sub: "Not a mission statement. Four things buyers asked us to prove — and that we have built the operation around."

    values:
      - title: "Spec on Paper = Spec on Goods"
        icon: "bi-file-earmark-check"
        body: >
          What the approved tech-pack and sealed sample say is what ships.
          Incoming fabric is checked within 4 hours (ΔE >1.0 rejected), AQL 2.5
          pre-shipment sampling before every shipment. Not close to spec — exactly on it.

      - title: "One Factory, Full Transparency"
        icon: "bi-eye"
        body: >
          All 280 workers on one payroll. No subcontracting at any stage — not for
          overflow, not for embroidery, not for finishing. Book a visit; there is no
          second location to schedule around.

      - title: "Verified, Not Claimed"
        icon: "bi-patch-check-fill"
        body: >
          Five third-party-audited certifications with certificate numbers on file:
          WRAP Gold, GRS, Higg FEM 82/100, BSCI, OEKO-TEX Standard 100.
          Audit reports available to clients under NDA. Certificate numbers, not claims.

      - title: "On-Time, On the Record"
        icon: "bi-clock-history"
        body: >
          92.4% on-time delivery rate, rolling 12-month average, measured against
          committed ship dates — not revised dates. Monthly delivery reports available
          to active clients. We do not revise the committed date retroactively.

  - id: s5_operations
    part: 3
    label: "Operations Detail"
    bg: dark-stripe
    layout: "2-column icon list, 6 items, each with icon + title + 2-sentence body"

    h2: "How Berun Runs Day-to-Day"

    items:
      - icon: "bi-clipboard-check"
        title: "7:45 AM Production Board"
        body: >
          Each morning, line supervisors update the floor whiteboard with that
          day's line allocation, prioritized by confirmed ship date.
          Every active order has a named line and a date on the board — no
          order sits in a queue without a scheduled production slot.

      - icon: "bi-droplet-half"
        title: "Fabric Checked Within 4 Hours of Arrival"
        body: >
          Every incoming fabric roll is tested for GSM, color (ΔE vs. approved
          lab dip using spectrophotometer), and shrinkage before it moves to
          the cutting floor. Rolls measuring ΔE >1.0 against the approved
          lab dip are rejected and returned to the supplier.

      - icon: "bi-search"
        title: "Inline QC on Every Production Line"
        body: >
          Each of the 12 lines has 2–3 dedicated inline QC workers checking
          seam integrity, print registration, and garment measurements
          at 30-piece intervals throughout the production run.
          Defects are flagged and corrected at the point of production,
          not caught at final inspection.

      - icon: "bi-patch-check"
        title: "AQL 2.5 Pre-Shipment on Every Order"
        body: >
          Before any order is released for shipping, Jenny's team runs
          AQL 2.5 full-batch random sampling per ANSI/ASQ Z1.4.
          Defect findings and pass/fail records are documented and
          available to clients on request.

      - icon: "bi-pencil-square"
        title: "Pattern Revisions at USD 40 per Round"
        body: >
          Pattern changes are quoted before each revision cycle begins.
          David's team completes revisions in 2–5 working days and
          produces a fit sample for client confirmation before the
          order returns to bulk production.

      - icon: "bi-reply-all"
        title: "24-Hour Quote Response"
        body: >
          Anna's team responds within 24 business hours confirming
          service track, MOQ applicability (100 pcs/SKU with XS–XXL
          size splits within the 100), lead time range, and initial
          pricing direction.
          This is a reviewed response, not an automated reply.

  # ----------------------------------------------------------
  # 部分 4 · 为什么选我们，信任纵深（S6 · S7）
  # ----------------------------------------------------------
  - id: s6_certifications
    part: 4
    label: "Certifications Story"
    bg: white
    layout: "left column: 5 cert logos stacked; right column: 5 narrative blocks"

    h2: "Berun's Certifications — What Each One Covers"

    certs:
      - name: "WRAP Gold"
        cert_number: "WRAP-GLD-156823"
        logo: "[TODO: WRAP Gold logo]"
        body: >
          WRAP (Worldwide Responsible Accredited Production) is a third-party
          labor and environmental compliance program with annual on-site audits
          conducted by independent WRAP-approved monitors.
          Gold status covers worker welfare, compensation and working hours,
          health and safety, and environmental management.
          Audit reports are available to clients under NDA for supplier
          qualification purposes.

      - name: "GRS"
        cert_number: "CU 1014387 GRS-2024"
        logo: "[TODO: GRS logo]"
        body: >
          The Global Recycled Standard traces recycled content through the
          supply chain from raw fiber to finished product.
          Berun's GRS certification means clients sourcing recycled polyester
          or nylon orders receive transaction certificates (TCs) linking their
          specific order to verified recycled fiber sources.
          This documentation is required by many EU and North American brands
          for ESG supplier reporting and scope 3 emissions disclosure.

      - name: "Higg FEM 82/100"
        cert_number: "HIG-FEM-2024-CN-08"
        logo: "[TODO: Higg Index logo]"
        body: >
          The Higg Facility Environmental Module scores factory environmental
          performance across energy use, water consumption, waste management,
          and emissions.
          Berun scored 82 out of 100 in the most recent verified assessment.
          Clients using the Higg Index for supplier qualification can request
          the verified FEM score report directly for their internal ESG records.

      - name: "BSCI"
        cert_number: "BSCI-CN-2024-08-15"
        logo: "[TODO: BSCI logo]"
        body: >
          The Business Social Compliance Initiative audit covers labor rights,
          occupational health and safety, and business ethics across the
          production facility.
          It is the standard used by most European retailers and brands for
          supplier onboarding and annual supplier reviews.
          Berun completed its most recent BSCI audit in August 2024
          with no major non-conformances.

      - name: "OEKO-TEX Standard 100"
        cert_number: "23.HCN.74521"
        logo: "[TODO: OEKO-TEX Standard 100 logo]"
        body: >
          OEKO-TEX Standard 100 tests garments for over 100 harmful substances
          including restricted dyes, heavy metals, formaldehyde, and pesticides.
          Berun's certification (23.HCN.74521) covers both fabric and finished
          product testing, satisfying chemical safety requirements for brands
          selling in EU, North American, and ANZ markets with strict
          restricted substance list (RSL) compliance requirements.

  - id: s7_trust_numbers
    part: 4
    label: "Trust Numbers + Factory Tour Invitation"
    bg: light-gray
    layout: "4 large stat cards, numbered; 1 paragraph invitation below"

    h2: "Berun Factory Scale and Delivery Record"

    stats:
      - number: "92.4%"
        label: "On-Time Delivery Rate"
        body: >
          Rolling 12-month average, measured against confirmed ship dates
          set at order placement. Monthly delivery reports are available
          to clients with active orders on request.

      - number: "280"
        label: "Workers, Single Payroll"
        body: >
          No subcontracting at any production stage. All machinists, QC
          staff, pattern makers, and print and embroidery workers are direct
          Berun employees working in the same facility.

      - number: "8,500 m²"
        label: "Single Facility, No Split Locations"
        body: >
          All 12 production lines, the in-house QC lab, cutting tables,
          sublimation equipment, and finishing are under one roof.
          No order is split across separate production sites.

      - number: "8 Years"
        label: "Operating Since 2017"
        body: >
          Certification histories, audit records, and order documentation
          going back to 2017 are maintained and available to clients
          conducting supplier due diligence.

    invitation: >
      Buyers considering a first order or switching suppliers can request
      a virtual factory walkthrough via video call. Anna schedules these
      on weekdays at a time that works across time zones.
      A 45-minute session covers the production floor, QC lab, and
      print department.

  # ----------------------------------------------------------
  # 部分 4c · 客户反馈（S7c）2026-06-14 新增
  # ----------------------------------------------------------
  - id: s7c_testimonials
    part: 4
    label: "Client Feedback — Buyer Testimonials"
    bg: dark
    layout: "3-col archive-style testimonial cards / quote + person + hard metric"
    h2: "What Buyers Say After the First Order"
    sub: "Three buyers. Three different starting points. All on the record."

    testimonials:
      - quote: >
          "We moved to Berun after two bad runs elsewhere — wrong GSM on arrival,
          color shifted 2–3 ΔE from the approved sample. Berun's first bulk landed
          exactly matched the sealed sample. The colorimetric records they sent with
          the shipment documentation were exactly what our QC team needed for the
          supplier audit file."
        role: "Head of Sourcing"
        buyer_type: "Activewear Brand"
        region: "North America"
        service: "OEM Cut-&-Sew"
        photo: "[TODO: professional headshot, Western/European buyer, neutral background]"
        metric: "3 consecutive POs — 0 color variance rejections"

      - quote: >
          "We run a private-label uniform program for 14 gym locations — coaches need
          fresh gear each quarter. Berun worked with our 100 pcs/SKU without pushing
          us to inflate the order, hit the 35-day lead time on all three runs, and
          the team jerseys with roster numbering came out clean every time."
        role: "Operations Manager"
        buyer_type: "Gym Chain"
        region: "Australia"
        service: "Private Label + Team Sets"
        photo: "[TODO: professional headshot, Australian/Western buyer, office setting]"
        metric: "14 locations · 100 pcs/SKU held across 3 runs"

      - quote: >
          "As a DTC brand launching our first collection, we needed a factory willing
          to work at 100-piece minimums and not treat us like a nuisance. Anna answered
          every question within a day. Our first order — 400 pcs across four SKUs —
          arrived on time and matched the approved samples. That was enough to place
          the second order."
        role: "Founder"
        buyer_type: "DTC Activewear Brand"
        region: "Europe"
        service: "OEM First Order"
        photo: "[TODO: professional headshot, European founder, clean background]"
        metric: "4 SKUs, 400 pcs total — on-time, no rework"

    note: >
      Per site-facts.md: 禁编造具体公司名/人名。用匿名 ICP 胶囊（role + buyer_type + region）。
      Fake testimonial names like "Akarra Active" 严禁。avatars = 用 AI 头像（欧美面孔，买家端）。

  # ----------------------------------------------------------
  # 部分 5 · 表单 / CTA（S8）
  # ----------------------------------------------------------
  - id: s8_contact
    part: 5
    label: "Contact / CTA"
    bg: dark
    layout: "left: text + Anna avatar; right: 3 option cards; below: contact form"

    h2: "Contact Berun or Schedule a Factory Tour"

    intro: >
      Three ways to move forward, depending on where you are in your
      supplier evaluation.

    options:
      - icon: "bi-camera-video"
        title: "Book a Virtual Factory Tour"
        body: >
          45-minute video walkthrough of the production floor, QC lab,
          and print department. Anna hosts. Available weekdays —
          request a time via email or WhatsApp.
        cta: "Book via Email"
        cta_href: "mailto:sales@berunactivewear.com?subject=Virtual Factory Tour Request"

      - icon: "bi-file-earmark-pdf"
        title: "Request Company Profile Deck"
        body: >
          Full PDF covering production capacity by line type, all five
          certifications, product categories, quality protocols,
          and pricing structure. Sent within 24 hours of request.
        cta: "Request Profile Deck"
        cta_href: "mailto:sales@berunactivewear.com?subject=Company Profile Deck Request"

      - icon: "bi-whatsapp"
        title: "Talk to Anna Directly"
        body: >
          WhatsApp or email. Anna responds within 24 business hours.
          For urgent RFQs or sample status inquiries,
          WhatsApp is faster.
        cta: "WhatsApp Anna"
        cta_href: "https://wa.me/8615902778636"

    form:
      heading: "Or send a message"
      fields:
        - name: "name"
          label: "Your Name"
          type: text
          required: true
        - name: "company"
          label: "Company"
          type: text
          required: true
        - name: "email"
          label: "Email"
          type: email
          required: true
        - name: "message"
          label: "What would you like to discuss?"
          type: textarea
          required: true
      submit_label: "Send Message"

    anna_note: >
      Anna reads every submission. If your inquiry falls outside her scope
      (production scheduling, QC questions, tech-pack specifics), she routes
      it to the right team member within the same business day.
