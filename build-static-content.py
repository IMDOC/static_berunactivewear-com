#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
博客首页静态化脚本

功能：
1. 读取 assets/blogs-page-1.json 中的第一页博客数据
2. 生成静态博客卡片 HTML，注入到 blogs.html 的 blogGrid 容器
3. 修改 blogs.html 中的 JS，使其识别静态内容、跳过第一页的重复加载

使用方法：
    python3 build-static-content.py

Shipped by: /init-blog-framework (B2B site builder)
Site-agnostic — reads site's own assets/blogs-page-1.json and patches blogs.html
"""

import json
import os
import re
from typing import List


# ============ 工具函数 ============

def read_json(file_path: str) -> dict:
    """读取JSON文件"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"❌ 读取文件失败: {file_path}")
        print(f"   错误: {e}")
        exit(1)


def escape_html(text) -> str:
    """HTML转义"""
    if text is None:
        return ''
    return (str(text)
            .replace('&', '&amp;')
            .replace('<', '&lt;')
            .replace('>', '&gt;')
            .replace('"', '&quot;')
            .replace("'", '&#039;'))


# ============ 生成博客卡片 HTML ============

def generate_blog_cards_html(blogs_data: List[dict]) -> str:
    """生成博客第一页的静态卡片HTML"""
    DEFAULT_THUMBNAIL = 'https://docerp.s3.us-west-1.amazonaws.com/images/p_14/d_default/372f5478573476c5de199e50a54e8b4e.webp'

    def format_date(date_string):
        """格式化日期"""
        from datetime import datetime
        try:
            date = datetime.strptime(date_string, '%Y-%m-%d')
            return date.strftime('%b %d, %Y')
        except Exception:
            return date_string

    cards_html = []
    for blog in blogs_data:
        featured_class = 'featured' if blog.get('featured', False) else ''
        thumbnail = blog.get('thumbnail') or DEFAULT_THUMBNAIL

        card_html = f'''
            <article class="blog-card {featured_class}" data-static-blog>
                <a href="{blog.get('url', '#')}" class="blog-thumbnail-wrapper">
                    <img src="{thumbnail}"
                         alt="{escape_html(blog.get('title', ''))}"
                         class="blog-thumbnail"
                         loading="lazy"
                         onerror="this.src='{DEFAULT_THUMBNAIL}'">
                </a>
                <div class="blog-content">
                    <span class="blog-category">{escape_html(blog.get('category', ''))}</span>
                    <a href="{blog.get('url', '#')}" style="text-decoration: none;">
                        <h2 class="blog-title">{escape_html(blog.get('title', ''))}</h2>
                    </a>
                    <p class="blog-excerpt">{escape_html(blog.get('excerpt', ''))}</p>
                    <div class="blog-meta">
                        <div class="blog-meta-item">
                            <i class="bi bi-person-circle"></i>
                            <span>{escape_html(blog.get('author') or 'Unknown Author')}</span>
                        </div>
                        <div class="blog-meta-item">
                            <i class="bi bi-calendar3"></i>
                            <span>{format_date(blog.get('date', ''))}</span>
                        </div>
                        <div class="blog-meta-item">
                            <i class="bi bi-clock"></i>
                            <span>{blog.get('readTime', '5 min read')}</span>
                        </div>
                    </div>
                    <a href="{blog.get('url', '#')}" class="read-more">
                        Read More <i class="bi bi-arrow-right"></i>
                    </a>
                </div>
            </article>'''
        cards_html.append(card_html)

    return '\n'.join(cards_html)


# ============ 修改 blogs.html ============

def patch_blogs_html(blogs_data: List[dict]) -> bool:
    """注入静态博客卡片，并修改 JS 跳过重复加载"""
    file_path = 'blogs.html'

    if not os.path.exists(file_path):
        print(f"❌ 找不到文件: {file_path}")
        return False

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    changes = []

    # ---------- 1. 生成静态卡片 HTML ----------
    static_blogs_html = generate_blog_cards_html(blogs_data)

    # ---------- 2. 移除旧的静态博客卡片（保证幂等） ----------
    existing_static_blog_pattern = r'\s*<article\s+class="blog-card[^"]*"\s+data-static-blog>[\s\S]*?</article>'
    content = re.sub(existing_static_blog_pattern, '', content)

    # ---------- 3. 替换 blogGrid 内部的 loading div，注入静态卡片 ----------
    # 先移除 loading div
    loading_div_pattern = r'\s*<!--\s*Loading state\s*-->\s*<div class="loading">[\s\S]*?</div>'
    content = re.sub(loading_div_pattern, '', content)

    # 在 blogGrid 开始标签后插入静态卡片
    blog_grid_start_pattern = r'(<div\s+id="blogGrid"\s+class="blog-grid">)\s*'
    if re.search(blog_grid_start_pattern, content):
        replacement = rf'\1\n{static_blogs_html}\n        '
        content = re.sub(blog_grid_start_pattern, replacement, content, count=1)
        changes.append('博客第一页静态化')
    else:
        print("  ⚠️  找不到 blogGrid 容器，跳过静态化")
        return False

    # ---------- 4. 修改 renderBlogs()：第一页有静态内容时跳过渲染 ----------
    render_blogs_check = (
        'function renderBlogs() {\n'
        '        const blogGrid = document.getElementById(\'blogGrid\');\n'
    )
    render_blogs_patched = (
        'function renderBlogs() {\n'
        '        const blogGrid = document.getElementById(\'blogGrid\');\n'
        '        // 第一页已有静态内容时跳过重新渲染（SEO静态化）\n'
        '        if (currentPage === 1 && document.querySelectorAll(\'[data-static-blog]\').length > 0) {\n'
        '            return;\n'
        '        }\n'
    )
    if render_blogs_check in content and render_blogs_patched not in content:
        content = content.replace(render_blogs_check, render_blogs_patched, 1)
        changes.append('renderBlogs() 静态内容跳过逻辑')

    # ---------- 5. 修改 loadBlogsIndex()：有静态内容时跳过第1页数据加载 ----------
    load_page_1_old = (
        '            // 初始化加载第 1 页\n'
        '            await loadPageData(1);\n'
        '            renderBlogs();\n'
        '            renderPagination();'
    )
    load_page_1_new = (
        '            // 初始化加载第 1 页（如果已有静态内容则跳过数据加载）\n'
        '            const hasStaticContent = document.querySelectorAll(\'[data-static-blog]\').length > 0;\n'
        '            if (hasStaticContent) {\n'
        '                currentPage = 1;\n'
        '                renderPagination();\n'
        '            } else {\n'
        '                await loadPageData(1);\n'
        '                renderBlogs();\n'
        '                renderPagination();\n'
        '            }'
    )
    if load_page_1_old in content and load_page_1_new not in content:
        content = content.replace(load_page_1_old, load_page_1_new, 1)
        changes.append('loadBlogsIndex() 静态内容跳过逻辑')

    # ---------- 6. 写入文件 ----------
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"✅ {file_path} - 已更新 ({', '.join(changes)})")
    return True


# ============ 主函数 ============

def main():
    print('\n' + '=' * 40)
    print('🚀 博客首页静态化处理')
    print('=' * 40 + '\n')

    # 1. 读取第一页博客数据
    blogs_page_1_file = 'assets/blogs-page-1.json'
    print(f'📖 读取 {blogs_page_1_file}...')

    if not os.path.exists(blogs_page_1_file):
        print(f"❌ 找不到文件: {blogs_page_1_file}")
        exit(1)

    blogs_data_raw = read_json(blogs_page_1_file)
    blogs_list = blogs_data_raw.get('blogs', [])

    if not blogs_list:
        print("❌ blogs-page-1.json 中没有博客数据")
        exit(1)

    print(f'✅ 读取到 {len(blogs_list)} 篇文章\n')

    # 2. 处理 blogs.html
    print('⚙️  处理 blogs.html...')
    success = patch_blogs_html(blogs_list)

    # 3. 输出统计
    print('\n' + '=' * 40)
    if success:
        print('✨ 博客首页静态化完成！')
        print('💡 blogs.html 现在包含静态文章内容')
        print('💡 搜索引擎爬虫可直接看到第一页文章')
        print('💡 JS 分页加载其他页面仍正常工作')
    else:
        print('❌ 静态化失败，请检查错误信息')
    print('=' * 40 + '\n')


# ============ 执行 ============

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\n\n⚠️  用户中断操作')
        exit(0)
    except Exception as e:
        print(f'\n❌ 发生错误: {e}')
        import traceback
        traceback.print_exc()
        exit(1)
