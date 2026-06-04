#!/usr/bin/env python3
"""
render_article.py — 站点侧文章渲染（Shopify 风格）

ERP 写 _posts/{slug}.json，本脚本读 JSON → 生成 {slug}.html。
被 build_site.py 在聚合页渲染之前 import 并调用。

JSON schema（见 _posts/README.md 或 rules/posts.md）:
{
  "slug": "...",
  "title": "...",
  "body_html": "<h2>...</h2>...",
  "publish_date": "YYYY-MM-DD",
  "publish_datetime": "ISO 8601",
  "reading_minutes": 15,
  "hero_image": "https://...",
  "author": {"slug": "allen", "name": "Allen", "title": "..."},
  "category": {"slug": "manufacturing", "name": "Manufacturing"},
  "target_keywords": ["kw1", "kw2", ...],
  "seo": {
    "title_tag": "...",
    "meta_description": "...",
    "canonical_url": "..."
  },
  "plan": {
    "toc_enabled": true,
    "cta_blocks": [{"heading": "...", "body": "...", "button_text": "...", "button_link": "..."}],
    "faq_items": [{"q": "...", "a": "..."}, ...]
  },
  "related_slugs": ["slug1", "slug2", ...]
}
"""
from __future__ import annotations

import json
import re
from datetime import datetime
from html import escape as html_escape
from pathlib import Path

try:
    from bs4 import BeautifulSoup
except ImportError:
    raise SystemExit('render_article.py 需要 beautifulsoup4: pip install beautifulsoup4 lxml')


SHELL_SKIP = {'blog.html', 'blogs.html', 'index.html', 'about-us.html', 'about.html',
              'contact-us.html', 'contact.html', 'faq.html', '404.html', '500.html',
              'privacy.html', 'terms.html'}


def load_shell_template(site_root: Path, exclude_paths=None) -> str | None:
    """Shell template 选取顺序：
    1. 优先用 `_shell.html`（如果存在）— 专用种子文件，永远不被渲染覆盖
    2. 否则挑一篇已存在的文章 HTML（有 .blog-hero + .article-content + #dynamic-menu-container）

    `_shell.html` 模式更稳定：避免"用 A 当 shell 又渲染 A"的循环依赖。
    """
    seed = site_root / '_shell.html'
    if seed.exists():
        return seed.read_text(encoding='utf-8')

    exclude = {str(Path(p).resolve()) for p in (exclude_paths or [])}
    for p in sorted(site_root.glob('*.html')):
        if p.name in SHELL_SKIP or '-test' in p.stem:
            continue
        if str(p.resolve()) in exclude:
            continue
        try:
            soup = BeautifulSoup(p.read_text(encoding='utf-8'), 'lxml')
        except Exception:
            continue
        if (soup.select_one('.blog-hero')
                and soup.select_one('.article-content')
                and soup.find(id='dynamic-menu-container')):
            return str(soup)
    return None


def _upsert_meta(soup, *, key: str, value: str, attr: str = 'name') -> None:
    if not value:
        return
    tag = soup.find('meta', attrs={attr: key})
    if tag:
        tag['content'] = value
        return
    new_tag = soup.new_tag('meta')
    new_tag[attr] = key
    new_tag['content'] = value
    if soup.head:
        soup.head.append(new_tag)


def _upsert_canonical(soup, href: str) -> None:
    if not href:
        return
    link = soup.find('link', attrs={'rel': 'canonical'})
    if link:
        link['href'] = href
        return
    new = soup.new_tag('link', rel='canonical', href=href)
    if soup.head:
        soup.head.append(new)


def _normalize_body(title: str, body_html: str) -> str:
    """从 body_html 删掉重复的 H1（如果 H1 文字就是标题）。"""
    soup = BeautifulSoup(f'<div>{body_html}</div>', 'lxml')
    wrapper = soup.find('div')
    if not wrapper:
        return ''
    norm = lambda s: re.sub(r'\s+', ' ', s or '').strip().lower()
    ntitle = norm(title)
    for h1 in wrapper.find_all('h1'):
        if norm(h1.get_text(' ', strip=True)) == ntitle:
            h1.decompose()
    return ''.join(str(c) for c in wrapper.contents).strip()


def _inject_article_body(soup, body_html: str) -> None:
    article = soup.select_one('.article-content')
    if not article:
        return
    article.clear()
    body_fragment = BeautifulSoup(body_html, 'lxml')
    src = body_fragment.body or body_fragment
    for child in list(src.contents):
        article.append(child)


def _update_hero(soup, title: str, hero_image: str = '') -> None:
    h1 = soup.select_one('.blog-hero h1')
    if h1:
        h1.string = title
    if hero_image:
        bg_re = re.compile(
            r"(\.blog-hero::before\s*\{[^}]*background:\s*url\()['\"][^'\"]+['\"](\)[^}]*\})",
            re.IGNORECASE | re.DOTALL,
        )
        for style in soup.find_all('style'):
            text = style.string or style.get_text()
            if '.blog-hero::before' not in text:
                continue
            updated = bg_re.sub(rf"\1'{hero_image}'\2", text, count=1)
            if updated != text:
                style.string = updated
                break


def _update_breadcrumb(soup, title: str, category: dict | None) -> None:
    """
    - 所有位置的活动项文字改成文章标题（.blog-hero 或 .article-meta-wrap 都处理）
    - 相对 href 改成绝对（/blog、/author/xx、/category/xx）
    - 在 active 前插入 category <li>（如果 category 提供）
    """
    for active in soup.select('.breadcrumb-item.active'):
        active.clear()
        active.append(title)

    for bc in soup.select('ol.breadcrumb, ul.breadcrumb'):
        for a in bc.select('a[href]'):
            h = a.get('href', '')
            if h == 'blog':
                a['href'] = '/blog'
            elif h.startswith('author/') and not h.startswith('/'):
                a['href'] = '/' + h
            elif h.startswith('category/') and not h.startswith('/'):
                a['href'] = '/' + h

        if not category or not category.get('slug') or not category.get('name'):
            continue
        active_li = bc.select_one('li.breadcrumb-item.active')
        if not active_li:
            continue
        if any((a.get('href') or '').startswith(f"/category/{category['slug']}")
               for a in bc.select('a[href]')):
            continue
        cat_li = soup.new_tag('li', attrs={'class': 'breadcrumb-item'})
        cat_a = soup.new_tag('a', href=f"/category/{category['slug']}")
        cat_a.string = category['name']
        cat_li.append(cat_a)
        active_li.insert_before(cat_li)


def _update_meta_info(soup, author: dict | None, publish_date: str, reading_minutes: int) -> None:
    spans = soup.select('.blog-meta-item span') or soup.select('.article-info span')
    if not spans:
        return
    if len(spans) >= 1 and author and author.get('name'):
        spans[0].clear()
        if author.get('slug'):
            a = soup.new_tag('a', href=f"/author/{author['slug']}", rel='author')
            a['style'] = 'color:inherit;text-decoration:none;border-bottom:1px dotted currentColor;'
            a.string = author['name']
            spans[0].append(a)
        else:
            spans[0].string = author['name']
    if len(spans) >= 2 and publish_date:
        # 保留图标子元素如果存在
        icon = spans[1].find('i')
        spans[1].clear()
        if icon:
            spans[1].append(icon)
            spans[1].append(' ')
        spans[1].append(_format_date(publish_date))
    if len(spans) >= 3 and reading_minutes:
        icon = spans[2].find('i')
        spans[2].clear()
        if icon:
            spans[2].append(icon)
            spans[2].append(' ')
        spans[2].append(f'{reading_minutes} min read')


def _format_date(iso_date: str) -> str:
    try:
        return datetime.strptime(iso_date[:10], '%Y-%m-%d').strftime('%B %d, %Y')
    except Exception:
        return iso_date


def _inject_head_meta(soup, post: dict) -> None:
    seo = post.get('seo') or {}
    title_tag = seo.get('title_tag') or post.get('title', '')
    meta_desc = seo.get('meta_description') or ''
    canonical = seo.get('canonical_url') or ''
    author = post.get('author') or {}
    category = post.get('category') or {}
    hero = post.get('hero_image') or ''
    pub_dt = post.get('publish_datetime') or datetime.now().astimezone().isoformat(timespec='seconds')
    keywords = post.get('target_keywords') or []

    if soup.title and title_tag:
        soup.title.string = title_tag
    _upsert_meta(soup, key='description', value=meta_desc)
    _upsert_meta(soup, key='keywords', value=', '.join(keywords))
    _upsert_meta(soup, key='author', value=author.get('name', ''))
    _upsert_meta(soup, key='og:title', value=title_tag, attr='property')
    _upsert_meta(soup, key='og:description', value=meta_desc, attr='property')
    _upsert_meta(soup, key='og:image', value=hero, attr='property')
    _upsert_meta(soup, key='og:url', value=canonical, attr='property')
    _upsert_meta(soup, key='og:type', value='article', attr='property')
    _upsert_meta(soup, key='article:author', value=author.get('name', ''), attr='property')
    _upsert_meta(soup, key='article:section', value=category.get('name', ''), attr='property')
    _upsert_meta(soup, key='article:published_time', value=pub_dt, attr='property')
    _upsert_meta(soup, key='article:modified_time', value=pub_dt, attr='property')
    _upsert_canonical(soup, canonical)

    # 每个 target_keyword 一条 <meta property="article:tag">
    if soup.head:
        for t in soup.head.find_all('meta', attrs={'property': 'article:tag'}):
            t.decompose()
        for kw in keywords:
            kw = (kw or '').strip()
            if not kw:
                continue
            m = soup.new_tag('meta')
            m['property'] = 'article:tag'
            m['content'] = kw
            soup.head.append(m)


def _render_cta_banner(soup, block: dict):
    h = html_escape(block.get('heading', ''))
    b = html_escape(block.get('body', ''))
    bt = html_escape(block.get('button_text', 'Get in touch'))
    bl = html_escape(block.get('button_link', '/contact-us'))
    return BeautifulSoup(
        f'<section class="cta-banner-section"><div class="cta-banner">'
        f'<h2>{h}</h2><p>{b}</p>'
        f'<a href="{bl}" class="cta-button">{bt} →</a>'
        f'</div></section>', 'lxml'
    ).body.contents[0]


def _render_faq(soup, items: list):
    html = '<section class="faq-section"><h2>FAQ</h2><div class="faq-list">'
    for it in items or []:
        q = html_escape(it.get('q', ''))
        a = html_escape(it.get('a', ''))
        html += f'<details class="faq-item"><summary>{q}</summary><div class="faq-answer"><p>{a}</p></div></details>'
    html += '</div></section>'
    return BeautifulSoup(html, 'lxml').body.contents[0]


def _slugify_heading(text: str) -> str:
    slug = re.sub(r'[^a-z0-9]+', '-', (text or '').strip().lower()).strip('-')
    return slug[:60] or 'section'


def _regenerate_toc(soup):
    """扫描 .article-content 里的 H2/H3 重建 sidebar TOC（避免 shell 里有陈旧条目）。
    TOC 容器 id=toc-nav-container，列表 id=toc-list-content（若无则用 .toc-list）。
    给每个 heading 自动补 id，让 TOC 链接能锚点跳转。"""
    article = soup.select_one('.article-content')
    toc = soup.select_one('#toc-nav-container, .toc-nav, .article-toc')
    if not article or not toc:
        return 0
    items = []
    for h in article.select('h2, h3'):
        text = h.get_text(' ', strip=True)
        if not text:
            continue
        hid = h.get('id') or _slugify_heading(text)
        # 确保 heading 有 id（被锚点跳转需要）
        h['id'] = hid
        level = 2 if h.name == 'h2' else 3
        items.append((level, hid, text))
    if not items:
        return 0

    # 找列表容器：优先 id 锁定，否则第一个 <ul>/<ol>
    list_container = toc.select_one('#toc-list-content, .toc-list, ul, ol')
    if list_container is None:
        list_container = soup.new_tag('ul')
        list_container['class'] = 'toc-list'
        toc.append(list_container)
    list_container.clear()
    # 扁平渲染：H3 缩进两空格显示即可
    idx = 0
    for level, hid, text in items:
        if level == 2:
            idx += 1
            label = f'{idx}. {text}'
        else:
            label = f'    {text}'
        li = soup.new_tag('li')
        a = soup.new_tag('a', href=f'#{hid}')
        a.string = label
        li.append(a)
        list_container.append(li)
    return len(items)


def _ensure_inquiry_form(soup, brand_name: str = '', domain: str = ''):
    """侧边栏注入询盘表单（form.lianf.com 规范）。已存在则跳过。"""
    aside = soup.select_one('aside.article-sidebar, .blog-sidebar, aside.blog-sidebar')
    if not aside:
        return False
    if aside.select_one('form'):
        return False  # 已有表单

    form_html = f'''
<div class="sidebar-widget sidebar-inquiry" style="background:#fff;border-radius:12px;padding:24px;box-shadow:0 2px 12px rgba(0,0,0,0.06);margin-top:16px;">
  <h3 style="font-size:1.05rem;font-weight:700;color:#1F2937;margin-bottom:8px;">Quick Inquiry</h3>
  <p style="font-size:0.85rem;color:#666;margin-bottom:14px;">Send your specs — we&#39;ll reply with a factory-direct quote in 24 hours.</p>
  <form id="articleInquiryForm" class="inquiry-form" style="display:flex;flex-direction:column;gap:10px;">
    <input type="text" name="website" style="display:none" tabindex="-1" autocomplete="off">
    <input type="text" name="name" placeholder="Your Name *" required class="form-control" style="padding:8px 12px;border:1px solid #dee2e6;border-radius:6px;font-size:0.9rem;">
    <input type="email" name="email" placeholder="Email *" required class="form-control" style="padding:8px 12px;border:1px solid #dee2e6;border-radius:6px;font-size:0.9rem;">
    <input type="text" name="company" placeholder="Company / Brand" class="form-control" style="padding:8px 12px;border:1px solid #dee2e6;border-radius:6px;font-size:0.9rem;">
    <textarea name="message" placeholder="What are you looking to produce? (fabric, MOQ, delivery)" rows="3" class="form-control" style="padding:8px 12px;border:1px solid #dee2e6;border-radius:6px;font-size:0.9rem;resize:vertical;"></textarea>
    <button type="submit" style="background:#1F2937;color:#fff;border:none;border-radius:6px;padding:10px;font-weight:600;cursor:pointer;">Request Quote</button>
  </form>
  <script>
  (function(){{
    var f = document.getElementById('articleInquiryForm');
    if (!f || f.dataset.bound) return;
    f.dataset.bound = '1';
    var loaded = Date.now();
    f.addEventListener('submit', async function(e){{
      e.preventDefault();
      var btn = f.querySelector('button[type=submit]');
      var orig = btn.textContent;
      btn.disabled = true; btn.textContent = 'Sending...';
      try {{
        var r = await fetch('https://form.lianf.com/', {{
          method:'POST', headers:{{'Content-Type':'application/json'}},
          body: JSON.stringify({{
            domain: '{domain or "example.com"}',
            form_type: 'inquiry',
            form_data: {{ name: f.name.value, email: f.email.value, company: f.company.value, message: f.message.value }},
            honeypot: f.website.value,
            submission_time: Math.floor((Date.now() - loaded)/1000),
            page_url: location.href,
          }})
        }});
        var d = await r.json();
        if (d.success) {{ alert('Thanks! We&#39;ll reply within 24 hours.'); f.reset(); }}
        else alert('Submission failed: ' + (d.msg || 'unknown error'));
      }} catch(err) {{ alert('Network error. Please try again.'); }}
      finally {{ btn.disabled = false; btn.textContent = orig; }}
    }});
  }})();
  </script>
</div>
'''.strip()
    aside.append(BeautifulSoup(form_html, 'lxml').body.contents[0])
    return True


def _inject_plan_blocks(soup, post: dict, all_posts_by_slug: dict):
    plan = post.get('plan') or {}
    article = soup.select_one('.article-content')
    if not article:
        return

    # CTA banners (appended to article content tail)
    for block in (plan.get('cta_blocks') or []):
        article.append(_render_cta_banner(soup, block))

    # FAQ (appended after CTAs)
    if plan.get('faq_items'):
        article.append(_render_faq(soup, plan['faq_items']))

    # Related posts — slugs → minimal card list
    related = post.get('related_slugs') or []
    if related and all_posts_by_slug:
        rel_html = '<section class="related-posts-section"><h2>Related Articles</h2><div class="related-posts-list">'
        for slug in related[:4]:
            rp = all_posts_by_slug.get(slug)
            if not rp:
                continue
            title = html_escape(rp.get('title', ''))
            thumb = html_escape(rp.get('hero_image', ''))
            rel_html += (
                f'<a href="/{slug}" class="related-posts-card">'
                f'<img src="{thumb}" alt="{title}" loading="lazy">'
                f'<div class="related-posts-card-body"><h3>{title}</h3></div></a>'
            )
        rel_html += '</div></section>'
        article.append(BeautifulSoup(rel_html, 'lxml').body.contents[0])


def render_article_from_json(post: dict, shell_html: str, all_posts_by_slug: dict | None = None) -> str:
    """一篇文章的完整渲染：shell template + JSON data → HTML"""
    soup = BeautifulSoup(shell_html, 'lxml')

    title = post.get('title', '').strip()
    body = _normalize_body(title, post.get('body_html', ''))

    _inject_article_body(soup, body)
    _update_hero(soup, title, post.get('hero_image', ''))
    _update_breadcrumb(soup, title, post.get('category'))
    _update_meta_info(
        soup,
        author=post.get('author'),
        publish_date=post.get('publish_date', ''),
        reading_minutes=int(post.get('reading_minutes') or 0),
    )
    _inject_head_meta(soup, post)
    _inject_plan_blocks(soup, post, all_posts_by_slug or {})

    # 侧边栏重建：TOC 从正文 H2/H3 再生 + 询盘表单注入
    _regenerate_toc(soup)
    _site_domain = ''
    canonical = (post.get('seo') or {}).get('canonical_url', '')
    if canonical:
        import urllib.parse as _up
        _site_domain = _up.urlparse(canonical).hostname or ''
        _site_domain = _site_domain.replace('www.', '')
    _ensure_inquiry_form(soup, brand_name='', domain=_site_domain)

    return str(soup)


def build_articles_from_posts(site_root: Path) -> int:
    """扫 _posts/*.json → 渲染每篇到 {slug}.html。返回生成篇数。"""
    posts_dir = site_root / '_posts'
    if not posts_dir.is_dir():
        return 0

    post_jsons = sorted(posts_dir.glob('*.json'))
    if not post_jsons:
        return 0

    all_posts = {}
    for p in post_jsons:
        try:
            data = json.loads(p.read_text(encoding='utf-8'))
            json_slug = data.get('slug')
            if not json_slug:
                print(f'   ⚠ SKIP {p.name}: JSON 缺 "slug" 字段或为空', flush=True)
                continue
            if json_slug != p.stem:
                print(
                    f'   ⚠ SLUG MISMATCH {p.name}: filename stem="{p.stem}" vs JSON.slug="{json_slug}". '
                    f'build_site.py 会按文件名检查 HTML，可能报 "未生成 HTML"。'
                    f'修法：让 ERP 端把 JSON.slug 改成与文件名一致。',
                    flush=True,
                )
            all_posts[json_slug] = data
        except Exception as e:
            print(f'   ⚠ 解析 {p.name} 失败: {e}', flush=True)
            continue

    shell = load_shell_template(site_root)
    if not shell:
        print('   ⚠ 未找到合格的 shell template（需要 .blog-hero + .article-content + #dynamic-menu-container）', flush=True)
        return 0

    count = 0
    for slug, post in all_posts.items():
        try:
            html = render_article_from_json(post, shell, all_posts)
            (site_root / f'{slug}.html').write_text(html, encoding='utf-8')
            count += 1
        except Exception as e:
            import traceback
            print(f'   ⚠ 渲染 {slug} 失败: {type(e).__name__}: {e}', flush=True)
            print(f'      trace: {traceback.format_exc().splitlines()[-3:]}', flush=True)
    return count


if __name__ == '__main__':
    import sys
    root = Path(sys.argv[1] if len(sys.argv) > 1 else '.').resolve()
    print(f'渲染 {root} 下 _posts/*.json...')
    n = build_articles_from_posts(root)
    print(f'✓ 渲染了 {n} 篇文章')
