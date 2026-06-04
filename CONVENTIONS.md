# 静态站点路径与命名规范

> **单一事实源**：本文档是 B2B 静态站点（kikimami ERP + Cloudflare Pages 栈）的路径/命名契约。
> 所有 skill、ERP 代码、人工编辑都**必须**遵守。违反会导致子目录页面 404、JS 数据拉取失败、导航坏掉。

版本: 1.0 · 更新: 2026-04-19

---

## 铁律一览（30 秒版）

1. **站内资源一律用绝对路径** `/xxx`，禁用相对路径 `../xxx` 和 `xxx`
2. **JSON 数据源字段固定**：文章数组叫 `blogs`，不是 `posts`
3. **URL 字段写绝对路径**：JSON 里 `"url": "/foo"` 而不是 `"foo"`
4. **作者列表固定路径**：`assets/authors.json`
5. **SEO 元数据用完整 URL**：canonical / og:image / JSON-LD `@id` 等写 `https://www.{domain}/...`

---

## 1. 路径规范

### 1.1 HTML `<link>` / `<script>` / `<img>` 引用

| 场景 | 正确 | 错误 |
|------|------|------|
| CSS | `<link href="/assets/css/global.css">` | `href="assets/css/..."` 或 `href="../assets/css/..."` |
| JS | `<script src="/assets/dynamic-menu.js">` | `src="assets/..."` 或 `src="../assets/..."` |
| 站点根资源 (logo) | 已迁 R2 站：`<img src="https://img.{domain}/assets/images/logo.svg">`；未迁站：`<img src="/assets/images/logo.svg">` | `src="logo.webp"`（相对/本地，已迁站不准） |
| 内容真实图 (`/assets/images/` 产品·工厂照) | 已迁 R2 站：`<img src="https://img.{domain}/assets/images/x.webp" onerror="this.onerror=null;this.src='/assets/images/x.webp'">`；未迁站：`<img src="/assets/images/x.webp">` | `src="assets/images/..."`（相对）/ 第三方随机图源 / grapesjs random-image |
| Favicon / apple-touch-icon / android / ms-icon | 已迁 R2 站：`<link rel="icon" href="https://img.{domain}/favicon-32x32.png">`；未迁站：`href="/favicon-32x32.png"` | `href="favicon-32x32.png"`（相对） |
| Manifest **链接本身** | `<link rel="manifest" href="/manifest.json">`（manifest.json 文件**始终本地服务**，但其内部 `icons[].src` 走 `img.`） | `href="manifest.json"` |

**原因**：CF Pages 的 clean URL（`/blog`, `/author/allen` — 无 `.html`）会让浏览器把页面 base 当成目录，相对路径会错位成 `/blog/assets/...` 或 `/author/assets/...`。绝对路径 `/assets/...` 一致解析。R2 自定义域名 URL（`https://img.{domain}/...`）是**完全限定 URL**，同样免疫 base 错位，与绝对路径规则不冲突。

> **图片 CDN 参数化（CEO image-pipeline B方案 · 每站一桶 + 同域 `img.{domain}` · 2026-06-03 起含根资源）**：
> - **所有图片 = 内容图 + 根资源**（`/assets/images/` 下的产品/工厂/设备照、`og:image`/`twitter:image`/JSON-LD `image` meta 内容图、以及 logo / favicon / apple-touch-icon / android-icon / ms-icon / manifest 内部 icons / browserconfig 图）→ 一律用站点 `image_cdn_base`（单一事实源 = `registry.json` 的 `sites[domain].image_cdn_base`）。有值 → `{image_cdn_base}/<原路径>`（`<img>` 加 `onerror` 回退本地；meta / `<link>` 图标 / manifest-icons / og 无 onerror，硬 URL）；留空（站未建桶）→ 本地绝对。
> - **唯一例外**：`<link rel="manifest" href="/manifest.json">` 链接本身保持本地（manifest.json 文件本地服务），但其内部 `icons[].src` 改 `img.`。
> - **范围（已迁站）**：`src` / `href` / og-content 里凡指向本站图片/图标的本地路径（`/assets/images/*`、`/favicon-*`、`/apple-icon-*`、`/android-icon-*`、`/ms-icon-*`）全部加 `image_cdn_base` 前缀。本地文件保留在仓库做 onerror 兜底，**不准删**。
> - **占位 inline SVG**（Photo TBD / monogram）无 host，完全不动。

### 1.2 HTML `<a href>` 内部跳转

| 场景 | 正确 | 错误 |
|------|------|------|
| 站内页面 | `<a href="/about-us">` | `<a href="about-us">` |
| 文章 | `<a href="/how-to-order-custom-fishing-shirts">` | `<a href="how-to-order-custom-fishing-shirts">` |
| 分类 | `<a href="/custom-fishing-shirts">` | `<a href="custom-fishing-shirts">` |
| 作者页 | `<a href="/author/allen">` | `<a href="author/allen">` 或 `<a href="../author/allen">` |
| 首页 | `<a href="/">` | `<a href="./">` |

### 1.3 JS `fetch()` / AJAX

```js
// ✓ 正确
fetch('/assets/blogs-index.json')
fetch('/assets/blogs-page-1.json')
fetch('/assets/authors.json')

// ✗ 错误
fetch('assets/blogs-index.json')     // /blog 页访问变成 /blog/assets/...
fetch('../assets/blogs-index.json')  // 作者页访问变成 /assets/assets/...（或类似错位）
```

### 1.4 Config JSON 里的链接

**menu-config.json**、**footer-config.json** 等 config 文件里所有 `link` / `url` / `href` 字段也必须绝对路径：

```json
{
  "menuItems": [
    { "text": "Blog", "link": "/blog" },
    { "text": "About", "link": "/about-us" },
    { "text": "Contact", "link": "/contact-us" }
  ],
  "ctaButton": { "text": "Get a Quote", "link": "/contact-us" }
}
```

### 1.5 SEO 元数据（canonical / OG / Schema）— 用完整 URL

```html
<!-- canonical 必须带 https:// -->
<link rel="canonical" href="https://www.runfishapparel.com/how-to-order-custom-fishing-shirts">

<!-- OG image / URL 必须带 https:// -->
<meta property="og:url" content="https://www.runfishapparel.com/how-to-order-custom-fishing-shirts">
<meta property="og:image" content="https://docerp.s3.us-west-1.amazonaws.com/.../hero.webp">

<!-- JSON-LD 的 @id / url / image 必须带 https:// -->
<script type="application/ld+json">
{
  "@type": "Article",
  "mainEntityOfPage": { "@id": "https://www.runfishapparel.com/..." },
  "author": { "@type": "Person", "url": "https://www.runfishapparel.com/author/allen" }
}
</script>
```

**例外**：`<link rel="author" href="https://..." >` 用绝对域名；但页内可见 byline 的 `<a rel="author" href="/author/allen">` 用站内绝对路径即可。

---

## 2. 文件命名规范

### 2.1 站点根目录

| 类型 | 文件名 | 访问 URL |
|------|--------|---------|
| 首页 | `index.html` | `/` |
| 落地页 / product_catalog / product | `{slug}.html`（扁平在根目录） | `/{slug}` |
| 博客列表页 | **`blog.html`**（单数，本栈默认） | `/blog` |
| 博客文章 | `{slug}.html`（扁平在根目录，**不**在 `blog/` 子目录） | `/{slug}` |
| 作者列表（可选） | `authors.html` | `/authors` |
| 作者档案 | `author/{slug}.html` | `/author/{slug}` |
| sitemap | `sitemap.xml` | `/sitemap.xml` |
| robots | `robots.txt` | `/robots.txt` |
| CF 重定向 | `_redirects` | — |

> **为什么文章不放 `blog/` 子目录**：便于 ERP `load_site_shell_template()` 扫描、相关文章匹配、sitemap 生成。所有 `<meta name="post_article" content="true">` 页面都在根目录。

### 2.2 assets/ 目录结构

```
assets/
├── css/                        # 所有样式
│   ├── article-shell.css       # ERP REQUIRED_ASSETS
│   ├── article-components.css  # ERP REQUIRED_ASSETS
│   ├── article-toc.css         # ERP REQUIRED_ASSETS
│   ├── article-sidebar.css     # ERP REQUIRED_ASSETS
│   ├── article-embeds.css      # ERP REQUIRED_ASSETS
│   ├── related-posts.css       # ERP REQUIRED_ASSETS
│   ├── post-page.css           # init-blog-framework 专属
│   ├── global.css
│   ├── dynamic-menu.css
│   ├── bootstrap.min.css
│   └── bootstrap-icons.min.css
├── js/                         # 所有脚本
│   ├── article-shell.js        # ERP REQUIRED_ASSETS
│   ├── related-posts.js        # ERP REQUIRED_ASSETS
│   ├── article-toc.js          # init-blog-framework 专属
│   └── bootstrap.bundle.min.js
├── images/
│   └── authors/                # 作者头像
│       ├── allen.webp
│       └── jake-morrison.webp
├── includes/
│   └── article-sidebar.html
├── menu-config.json            # 顶部导航配置
├── footer-config.json          # 页脚配置
├── topbar-config.json          # 顶栏联系方式配置
├── authors.json                # ★ 作者清单（固定路径）
├── blogs-index.json            # 博客索引（totalBlogs / categories / totalPages）
└── blogs-page-{N}.json         # 分页数据，每页 20 篇
```

### 2.3 slug 命名

- kebab-case：`how-to-order-custom-fishing-shirts`
- 只含 `[a-z0-9-]`，无下划线、无大写、无中文
- 结尾不带 `-test`、`-test1`、`-test2` 等后缀（ERP shell detector 会跳过带 `-test` 的文件）
- 长度 ≤ 70 字符

### 2.4 作者 slug

- 纯英文名：`allen`、`sarah-johnson`、`michael-chen`
- 名字有空格 → 用连字符：`Sarah Johnson` → `sarah-johnson`
- **禁止** `editorial`、`admin`、`team`、`staff`、`content`、`writer`、`author`、品牌名、纯数字

---

## 3. JSON Schema 约定

### 3.1 `assets/blogs-page-{N}.json`

```json
{
  "pageNumber": 1,
  "blogs": [                        ← 数组字段名是 "blogs"（不是 "posts"）
    {
      "title": "...",
      "slug": "how-to-order-...",   ← 不带 /
      "url": "/how-to-order-...",   ← 带前导 /
      "excerpt": "...",
      "author": "Allen",            ← 真人名
      "authorTitle": "Content Director & Fishing Apparel Specialist",
      "date": "2026-04-18",
      "category": "Manufacturing",
      "categorySlug": "manufacturing",
      "thumbnail": "https://...webp",  ← OG image 完整 URL
      "readTime": "15 min read",
      "tags": ["...", "..."],
      "featured": true,
      "id": 1
    }
  ]
}
```

### 3.2 `assets/blogs-index.json`

```json
{
  "totalBlogs": 1,
  "totalPages": 1,
  "postsPerPage": 20,
  "categories": [
    { "name": "Manufacturing", "slug": "manufacturing", "count": 1 }
  ],
  "latestUpdate": "2026-04-18"
}
```

### 3.4 `assets/categories.json`（⭐ ERP 分类归属单一事实源）

```json
{
  "version": "1.0",
  "domain": "runfishapparel.com",
  "default_category_slug": "manufacturing",
  "categories": [
    {
      "slug": "manufacturing",
      "name": "Manufacturing",
      "description": "...",
      "icon": "bi-gear-wide-connected",
      "featured": true,
      "parent_topic_ids": [],                   ← ERP topic.id 精确锁定（优先级最高）
      "parent_topic_keywords": ["manufacturing", "oem", "odm"],   ← 英文关键词
      "parent_topic_keywords_zh": ["制造", "生产", "工厂"]         ← 中文关键词（ERP topic 可能是中文）
    }
  ]
}
```

**ERP 匹配优先级**（`batch_blog_auto_optimized_deploy` Step 2.5）：
1. post 关联 topic 的 parent.id 在 `parent_topic_ids[]` 里 → 精确命中
2. parent.keyword 英文含 `parent_topic_keywords` 任一 → 命中
3. parent.keyword 中文含 `parent_topic_keywords_zh` 任一 → 命中
4. 都不命中 → 用 `default_category_slug` + **发钉钉通知**建议编辑 manifest

### 3.3 `assets/authors.json`（⭐ ERP 作者单一事实源）

```json
{
  "version": "1.0",
  "domain": "runfishapparel.com",
  "default_author_slug": "allen",
  "picking_strategy": "expertise_match",
  "authors": [
    {
      "slug": "allen",                   ← 唯一键，匹配 author/{slug}.html
      "name": "Allen",                   ← 真人名（过 E-E-A-T 黑名单）
      "title": "Content Director & Fishing Apparel Specialist",
      "bio_short": "...",
      "expertise_tags": ["oem-manufacturing", "fabric-technology", ...],
      "email": "sales@runfishapparel.com",
      "avatar_url": "/assets/images/authors/allen.webp",
      "page_url": "/author/allen",
      "featured": true
    }
  ]
}
```

- `picking_strategy`:
  - `"default"` → 永远用 `default_author_slug` 对应作者
  - `"expertise_match"` → 文章关键词 × 作者 `expertise_tags` 交集最大者胜

---

## 4. ERP 契约

### 4.1 Shell template 探测条件

ERP `batch_blog_auto_optimized_deploy` 会从站点挑一篇文章做 shell。必须同时满足：

```python
soup.select_one(".blog-hero")
soup.select_one(".article-content")
soup.find(id="dynamic-menu-container")
"-test" not in filename.stem
```

首篇 seed 文章**必须**符合，并且**永远不要删**。

### 4.2 REQUIRED_ASSETS 8 个文件

ERP `shared_assets.py` 会校验以下文件存在，缺一个 Step 8 就发 warning：

```
assets/css/article-shell.css
assets/css/article-components.css
assets/css/article-toc.css
assets/css/article-sidebar.css
assets/css/article-embeds.css
assets/css/related-posts.css
assets/js/article-shell.js
assets/js/related-posts.js
```

### 4.3 作者链接自动注入（Step 6.5）

ERP 发稿时：
1. 从 `assets/authors.json` 按 `picking_strategy` 挑作者
2. 把该作者 `name` 注入 byline
3. 自动把 byline 包成 `<a href="/author/{slug}" rel="author">`
4. JSON-LD `Article.author.url` 填 `https://{domain}/author/{slug}`
5. `<head>` 加 `<link rel="author" href="https://{domain}/author/{slug}">`

### 4.4 本地构建脚本调用（Step 9.5）

ERP push 前会执行：

```bash
python3 generate_blog_pages.py      # 刷新 blogs-page-{N}.json + blogs-index.json
python3 build-static-content.py     # 把 dm-nav / ft-footer 预渲染进 HTML
```

脚本缺失 → warning + 跳过，不阻断部署。

---

## 5. 常见坑与自检

### 5.1 新页面上线前自检

```bash
# 无相对资源引用
grep -E '(href|src)="[a-z][^"/:#]' YOUR_PAGE.html

# 无空菜单容器（build-static-content.py 没跑）
grep '<div id="dynamic-menu-container"></div>' YOUR_PAGE.html
# 若存在 → 跑 python3 build-static-content.py

# canonical 用完整 URL
grep -E '<link rel="canonical" href="https?://' YOUR_PAGE.html
```

### 5.2 作者页专项自检

```bash
# 所有资源绝对路径
grep -cE '(href|src)="\.\./|href="[a-z][^"/:#]' author/*.html
# 期望: 0
```

### 5.3 博客列表自检

```bash
# fetch 用绝对路径
grep -E "fetch\('assets/|fetch\(\"assets/" blog.html
# 期望: 无匹配

# JS 读字段名
grep -E "data\.(blogs|posts)" blog.html
# 应有 data.blogs 优先，data.posts 回退
```

---

## 6. SEO 命名规范

### 6.1 `<title>` 标签

| 页面类型 | 格式 | 示例 | 长度 |
|---------|------|------|------|
| 首页 | `{H1 核心词}｜{brand}` | `Professional Fishing Apparel Manufacturer \| Runfish Apparel` | ≤ 60 |
| 落地页 (product_catalog) | `{product keyword}：{value prop} \| {brand}` | `Custom Fishing Shirts: OEM & ODM from MOQ 50 \| Runfish Apparel` | ≤ 60 |
| 产品页 | `{product slug}：{price/MOQ hook} \| {brand}` | `Custom Fishing Hoodies: Wholesale from $12 \| Runfish Apparel` | ≤ 60 |
| 博客文章 | `{Article title, can match H1} \| {brand}` | `How to Order Custom Fishing Shirts \| Runfish Apparel` | ≤ 65 |
| 博客列表 | `{Category} Blog: {Niche} Insights \| {brand}` | `Fishing Apparel Blog: Manufacturing Insights \| Runfish Apparel` | ≤ 65 |
| 作者页 | `{Name} — {title} \| {brand}` | `Allen — Content Director \| Runfish Apparel` | ≤ 65 |
| 404 | `Page Not Found \| {brand}` | — | — |

**禁忌**：
- ❌ 标题不含核心关键词
- ❌ 品牌放最前（除首页外）
- ❌ 关键词堆砌：`Buy Cheap Best Top Custom Fishing Shirts...`
- ❌ 全部大写 `CUSTOM FISHING SHIRTS`

### 6.2 `<meta name="description">`

| 页面类型 | 字数 | 必含 |
|---------|------|------|
| 全部 | 150–160 字符（不能 < 140，不能 > 160） | 核心关键词 + 价值主张 + CTA |
| 博客文章 | 150–160 | 核心关键词首次出现在前 100 字符 |
| 落地页 | 150–160 | 含 MOQ / 价格区间 / 定制能力等 B2B 决策点 |

**验证**：
```bash
# 检查所有页面 meta description 长度
grep -oE '<meta name="description" content="[^"]+"' *.html | \
  awk -F'"' '{print length($4), FILENAME ":" $4}' | sort -n | head -20
# 期望所有都在 150-160 之间
```

### 6.3 `<meta name="keywords">`

- 逗号分隔，5–10 个关键词
- 第一个必须是**主关键词**（与 title + H1 + URL 一致）
- 全小写
- 不堆叠同义词

```html
<meta name="keywords" content="custom fishing shirts, fishing apparel manufacturer, OEM fishing clothing, wholesale fishing shirts, sublimation fishing shirts">
```

### 6.4 URL Slug

- **kebab-case 纯英文**：`custom-fishing-shirts`
- **≤ 70 字符**（含 domain 则 ≤ 90）
- **含主关键词**：`how-to-order-custom-fishing-shirts`
- **停用词可酌情保留**：`how-to` / `for` / `with` 可保留（提升语义），但 `a / an / the / of` 省略
- **产品页与分类页区分**：
  - 分类：`/custom-fishing-shirts`（catalog）
  - 单品：`/products/runfish-pro-bass-shirt`（未来 SKU 级）
- **禁止**：
  - ❌ `/产品中文名` 中文 slug
  - ❌ `/post_123` 下划线 / ID 式
  - ❌ `/how_to_order_custom_fishing_shirts` 下划线
  - ❌ 结尾带 `.html`（href 统一不带，让 CF Pages routing 处理）

### 6.5 Heading 层级

| 页面 | H1 数量 | 层级 |
|------|--------|------|
| 所有页面 | **恰好 1 个 H1** | — |
| 落地页 | 1 H1 + 2-4 H2（对应 section） + H3 支撑论点 | H1 → H2 → H3（不跳级） |
| 博客文章 | 1 H1（= title 去站点名）+ 5-10 H2 + H3 展开 | 同上 |
| 作者页 | 1 H1（= author name）+ H2 分区（Expertise / Bio / Articles） | 同上 |

**H1 必须**：
- 含主关键词
- 位于 Hero 区块（视觉最大文字）
- 与 `<title>` 语义一致但**不完全相同**（title 含 brand，H1 可以不含）

### 6.6 图片 `alt` 文本

| 场景 | 规则 |
|------|------|
| Hero / OG 图 | 描述图片 + 含主关键词："Custom fishing shirts production line — Runfish factory Guangzhou" |
| 正文插图 | 描述 + 上下文：`"UPF50+ sublimation print on polyester jersey fabric"` |
| 装饰性图 | `alt=""`（空字符串）— 告诉屏幕阅读器跳过 |
| Logo | `alt="{Brand name}"` 固定 |
| 作者头像 | `alt="{Name} — {Title} at {Brand}"` |

**禁忌**：
- ❌ `alt="image"` / `alt="picture"` / `alt="photo"`
- ❌ `alt="Custom Fishing Shirts Custom Fishing Shirts Wholesale..."` 关键词塞
- ❌ 无 alt 属性（a11y 严重违规）

### 6.7 JSON-LD Schema

每个页面至少要有**两层 schema**：页面类型 + 面包屑。

| 页面类型 | Schema @type |
|---------|------------|
| 首页 | `WebSite` + `Organization`（publisher） |
| 落地页 (product_catalog) | `CollectionPage` 或 `ItemList` |
| 产品页 | `Product` + `Offer`（含 priceRange） |
| 博客文章 | `Article` + `BreadcrumbList` |
| 博客列表 | `Blog` + `BreadcrumbList` |
| 作者页 | `ProfilePage` + `Person` |
| About | `AboutPage` + `Organization` |
| Contact | `ContactPage` + `Organization` |

**`author` 字段必须是 `Person` 不是 `Organization`**（E-E-A-T）：

```json
"author": {
  "@type": "Person",
  "name": "Allen",
  "url": "https://www.runfishapparel.com/author/allen",
  "jobTitle": "Content Director & Fishing Apparel Specialist",
  "worksFor": { "@type": "Organization", "name": "Runfish Apparel" }
}
```

### 6.8 Open Graph / Twitter Card

| 字段 | 格式 | 必填 |
|------|------|------|
| `og:title` | = `<title>` 去站点名（或稍短版） | ✓ |
| `og:description` | = meta description 或更短版本 | ✓ |
| `og:url` | 完整 URL `https://www.{domain}/{slug}` | ✓ |
| `og:type` | `website` / `article` / `profile` | ✓ |
| `og:image` | 完整 URL，**1200×630 px**（1.91:1） | ✓ |
| `og:image:alt` | 描述性 alt | 推荐 |
| `og:site_name` | = brand name | ✓ |
| `og:locale` | `en_US`（默认英文站） | ✓ |
| `twitter:card` | `summary_large_image` | ✓ |
| `twitter:image` | 同 `og:image` | ✓ |

### 6.9 内链锚文本

- **含主关键词**：链到"custom fishing shirts"时，锚文本用 `custom fishing shirts` 或 `fishing shirt manufacturer`，不要 `click here` / `this page`
- **同一关键词 → 同一目标**：全站"OEM fishing apparel" 锚文本都指向 `/oem-odm-services`
- **自然多样**：不要 100% 精确匹配，30% 精确 + 30% 部分匹配 + 30% 品牌/裸 URL + 10% 通用
- **每个文章 ≥ 3 条内链**（指向 product catalog / pillar page / 相关文章）
- **首次出现原则**：关键词第一次出现时做锚文本，后续提及不重复链

### 6.10 robots & canonical

| 页面 | robots | canonical |
|------|--------|-----------|
| 所有对外页面 | `index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1` | 完整 URL，指向自己 |
| 分页 `?page=2` | `index, follow` + `<link rel="prev/next">` | 指向不带 `?page` 的基础 URL |
| 搜索结果 | `noindex, follow` | — |
| 404 / 500 | `noindex, nofollow` | — |
| 作者页 | `index, follow` | 完整 URL |
| test 页（`-test` 后缀） | `noindex, nofollow` | — |

---

## 8. 代码注释规范

> **铁律**：HTML/CSS/JS/Python 生产文件**不保留装饰性注释**。

### 8.1 要删除的注释类型

| 类型 | 示例 | 为什么删 |
|------|------|---------|
| 区块分隔 | `/* ============ 工具函数 ============ */` | 靠 function 名和空行分隔足够 |
| 装饰符号 | `/* ========== Hero Section ========== */` | 噪音 |
| 翻译说明 | `// 提取标题（优先使用 og:title...）` | 代码本身应可读 |
| 版本注释 | `/* v1.0 - 2026-04-19 */` | 用 git 管 |
| 占位说明 | `<!-- Main Content -->`, `<!-- Footer -->`, `<!-- Dynamic Menu Container -->` | 语义化 tag 已经清楚 |
| TODO 清单 | `/* TODO: 添加 xxx */` | 用 issue tracker |
| 作者名 | `/* 作者：XXX */` | 用 git log |
| Copy-paste 遗留 | `<!-- Copied from runfishapparel -->` | 无意义 |

### 8.2 可保留的注释

| 类型 | 示例 |
|------|------|
| 合同契约性注释 | `// ERP contract: this class name is hard-coded in post_optimizer/toc.py` |
| 解释不明显的**原因** | `// leading / required — CF Pages clean URL resolves relative paths wrong` |
| 关键字段标记 | `<!-- BLOG_GRID_START -->` / `<!-- BLOG_GRID_END -->`（构建脚本依赖） |
| 许可证头 | `/* Bootstrap 5 MIT License ... */`（第三方） |

### 8.3 落实到各类文件

**HTML**
- 删除 `<!-- Blog Listing Section -->`、`<!-- Main Content -->`、`<!-- Pagination -->` 这类 "什么是什么" 的注释
- 保留构建标记 `<!-- BLOG_GRID_START -->` / `<!-- BLOG_GRID_END -->`
- 保留 Schema 区分注释 `<!-- Schema: Article -->` / `<!-- Schema: BreadcrumbList -->`（两个 JSON-LD 并排时有区分价值）

**CSS**
- 删除 `/* ========== Hero Section ========== */` 等分隔条
- 删除 `/* 样式 */`、`/* 按钮样式 */` 等描述
- 保留 `/* ERP contract: #toc-nav-container id is required by post_optimizer */` 这类契约注释

**JS**
- 删除 `// Load blog index info`、`// Render a single blog card` 这类动词短语
- 保留 `// leading / required — CF Pages clean URL...` 这类解释原因的
- JSDoc（`@param` `@returns`）只在导出函数用

**Python**
- 删除中文 `# 扫描目录中所有包含 <article> 标签的 HTML 文件`（函数名已说明）
- 删除 `# 核心必需参数`、`# 自动生成的参数` 等区块标题
- 保留模块 docstring 一句话介绍 + 必要的契约说明

**JSON/YAML 配置**
- 本身不支持注释（JSON）或不鼓励（YAML）
- 不用 `"_comment"` 字段假装注释

### 8.4 清理工具

```bash
# HTML 注释清理（保留构建标记和 Schema 标注）
# 保留白名单：BLOG_GRID_START|BLOG_GRID_END|Schema:|post-optimizer
python3 << 'EOF'
import re
from pathlib import Path
KEEP = re.compile(r'BLOG_GRID_START|BLOG_GRID_END|Schema:|post-optimizer|contract', re.I)
for f in Path('.').glob('*.html'):
    txt = f.read_text(encoding='utf-8')
    # 逐个替换 <!-- ... --> 注释，白名单命中就保留
    new = re.sub(r'<!--([\s\S]*?)-->',
                 lambda m: m.group(0) if KEEP.search(m.group(1)) else '', txt)
    # 清空连续空行
    new = re.sub(r'\n\s*\n\s*\n+', '\n\n', new)
    if new != txt:
        f.write_text(new, encoding='utf-8')
        print(f'cleaned {f.name}')
EOF
```

---

## 7. 统一术语表（避免不同 skill 用不同叫法）

| 标准词 | 禁用别名 | 说明 |
|--------|---------|------|
| `slug` | `uri`, `path_segment`, `url_key` | URL 里的 kebab-case 标识 |
| `blog article` | `post`, `content`, `journal entry` | 博客文章 |
| `landing page` | `product page`, `category page`（在 catalog 场景下） | 落地页 |
| `product_catalog` | `products`, `products-list`, `collection` | 产品聚合页 page_type |
| `author manifest` | `author list`, `writers.json`, `editors.json` | 始终叫 `assets/authors.json` |
| `shell template` | `skeleton`, `wrapper`, `frame` | ERP 挑选的 layout 模板文章 |
| `default_author_slug` | `main_author`, `primary_author`, `editor_in_chief` | authors.json 里的默认作者键 |
| `expertise_tags` | `topics`, `specialties`, `categories`（易和分类混淆） | 作者擅长领域（与文章 keywords 匹配） |
| `post_article` | `blog_post`, `article_page` | `<meta name="post_article" content="true">` 是识别博客文章的统一 marker |
| `blog-hero` class | `article-hero`, `post-hero`, `hero-section` | 博客/文章页 hero 区块统一 class（ERP shell detector 硬编码） |
| `article-content` class | `article-body`, `post-body`, `content-wrap` | 文章正文容器统一 class |
| `dynamic-menu-container` id | `site-nav`, `header-menu`, `main-nav` | 导航挂载点统一 id |

---

## 6. 升级与演进

- 本规范升级时 bump 顶部 `版本` 号
- 改动需同步更新以下所有引用方：
  - skill `init-website` / `init-blog-framework` / `init-site-framework`
  - skill `post-from-erp` / `landing-from-md` / `landing-page-optimizer`
  - ERP `kikimami_server/static_web/api/batch_blog_api.py`
  - ERP `kikimami_server/static_web/post_optimizer/` 全模块
- 违反此规范造成的线上 bug 修复后，**必须**把预防规则加进本文档
