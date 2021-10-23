#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Author: Oliver Z., https://oliz.io
Description: Minimal static site generator easy to use with GitHub Pages o.s.
Website: https://oliz.io/ggpy/
Version: 2.0.1
License: Dual-licensed under GNU AGPLv3 or MIT License,
         see LICENSE.txt file for details.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

import argparse

import glob
from html import escape
import os
import sys
import time
import markdown

##############################################################################
# META TAGS WITH SPECIAL FUNCTION
##############################################################################

TAG_DRAFT = '__draft__'
TAG_INDEX = '__index__'
TAG_INLINE = '__inline__'
TAG_NO_FOOTER = '__no_footer__'
TAG_NO_HEADER = '__no_header__'
TAG_NO_META = '__no_meta__'
SPECIAL_TAGS = [
    TAG_DRAFT,
    TAG_INDEX,
    TAG_INLINE,
    TAG_NO_FOOTER,
    TAG_NO_HEADER,
    TAG_NO_META
]

##############################################################################
# MARKDOWN CONVERSION
##############################################################################
def configure_markdown():
    return markdown.Markdown(
        extensions = [
            'extra',
            'meta',
            'sane_lists',
            'toc',
            'pymdownx.magiclink',
            'pymdownx.betterem',
            'pymdownx.tilde',
            'pymdownx.emoji',
            'pymdownx.tasklist',
            'pymdownx.superfences'
        ]
    )

def markdown2post(content='', config=None):
    config = config or {}
    MD = configure_markdown()
    html_section = MD.reset().convert(content)
    date = convert_meta(MD, 'date')
    tags = convert_meta(MD, 'tags')
    title = convert_meta(MD, 'title')
    raw_title = convert_meta(MD, 'title', raw=True)
    description = convert_meta(MD, 'description', default=title)
    raw_description = convert_meta(MD, 'description', default=raw_title, raw=True)
    html_headline = MD.reset().convert('# ' + title) if len(title) else ''
    post = {
        'date': date,
        'title': title,
        'raw_title': raw_title,
        'description': description,
        'raw_description': raw_description,
        'tags': tags,
        'html_headline': html_headline,
        'html_section': html_section
    }
    return post

def convert_meta(md, field, default='', raw=False):
    field_value = md.Meta.get(field, '')
    if len(field_value):
        if raw:
            return ''.join(field_value)
        return escape(', '.join(field_value)) if field == 'tags' else escape(''.join(field_value))
    return default

##############################################################################
# CONTENT FORMATTERS AND SNIPPETS
##############################################################################
def logo_url(config=None):
    config = config or {}
    base_url = config.get('site', {}).get('base_url', '')
    logo_url = base_url + '/' + config.get('site', {}).get('logo', '')
    return logo_url if logo_url != '/' else ''

def header(logo_url, title_html, date='', config=None):
    config = config or {}
    author_url = config.get('author', {}).get('url', '')
    lines = []
    if len(author_url) and len(logo_url):
        lines.append(f'<a href="{author_url}"><img src="{logo_url}" class="avatar" /></a>')
    lines.append(post_header(title_html, date, config))
    return '\n'.join([line for line in lines if len(line)])

def pagetitle(title='', config=None):
    config = config or {}
    root_title = config.get('site', {}).get('title', '')
    if len(title):
        if len(root_title) and title != root_title:
            return f'{title} | {root_title}'
        return title
    return root_title

def post_header(title_html, date='', config=None):
    config = config or {}
    name = config.get('author', {}).get('name', '')
    author_url = config.get('author', {}).get('url', '')
    name_and_date = date[:10]
    if len(name) and len(name_and_date):
        maybe_linked_author = name
        if len(author_url):
            maybe_linked_author = f'<a href="{author_url}">{name}</a>'
        name_and_date = f'{maybe_linked_author}, {name_and_date}'
    if len(name_and_date):
        name_and_date = f'''<small>{name_and_date}</small>'''
    header = ''
    if len(title_html) or len(name_and_date):
        header = f'''<div style="text-align:right;">
{title_html}
{name_and_date}
</div>'''
    return header

def footer_navigation():
    return '\n'.join([
        '''<a href="#" class="nav">top</a>''',
        '''<a href="javascript:toggleTheme()" class="nav">🌓</a>''',
        '''<a href="javascript:toggleFontSize()" class="nav">aA</a>'''
    ])

def about_and_social_icons(config=None):
    config = config or {}
    social_config = config.get('social', {})

    social = []
    for key in social_config.keys():
        val = social_config[key]
        social.append(_social_link(key, val))

    return '\n'.join(reversed(social))

def _social_link(label, link):
    return f'<a href="{link}" class="social">{label}</a>' if len(link) else ''

def posts_index(posts):
    posts = [post for post in posts if TAG_DRAFT not in post['tags'] and TAG_INDEX not in post['tags']]
    posts_html = []
    for post in reversed(sorted(posts, key=lambda post: post['date'])):
        day = post['date'][:10]
        title = post['title']
        url = post['url']
        if (day != '' and title != ''):
            is_inlined = TAG_INLINE in post['tags']
            if is_inlined:
                content = post.get('html_section', '')
                description = post.get('description', '')
                content_chars_count = len(content)
                content_lines_count = content.count('\n') + 1
                posts_html.append(f'''<div class="card"><small class="social">{day}</small>''')
                if content_chars_count > 500 or content_lines_count > 10:
                    if description == title:
                        posts_html.append(f'''<details><summary><a href="{url}"><b>{title}</b></a></summary>''')
                    else:
                        posts_html.append(f'''<a href="{url}"><b>{title}</b></a>''')
                        posts_html.append(f'''<details><summary>{description}</summary>''')
                    posts_html.append(f'''{content}''')
                    posts_html.append(f'''</details>''')
                else:
                    posts_html.append(f'''<a href="{url}"><b>{title}</b></a>''')
                    if description != title and content_chars_count == 0:
                        posts_html.append(html_tag_block('div', f'{description}'))
                    else:
                        posts_html.append(html_tag_block('div', f'{content}'))
                posts_html.append(f'''</div>''')
            else:
                posts_html.append(f'''<div class="card"><small class="social">{day}</small><a href="{url}"><b>{title}</b></a></div>''')
    posts_html = '\n'.join(posts_html)
    return html_tag_block('div', posts_html)

## META, SOCIAL AND MACHINE-READABLES
def meta(author, description, tags):
    meta_names = []
    keywords = _sanitize_special_tags(tags)
    if len(author):
        meta_names.append(('author', author))
    if len(description):
        meta_names.append(('description', description))
    if len(keywords):
        meta_names.append(('keywords', keywords))
    return '\n'.join([_meta_tag('name', name[0], name[1]) for name in meta_names])

def _sanitize_special_tags(tags):
    '''Refactor to use regex
    '''
    sanitized = tags
    for tag in SPECIAL_TAGS:
        tag_in_center_or_at_end = f', {tag}'
        tag_at_beginning = f'{tag}, '
        if tag_in_center_or_at_end in sanitized:
            sanitized = sanitized.replace(tag_in_center_or_at_end, '')
        elif tag_at_beginning in sanitized:
            sanitized = sanitized.replace(tag_at_beginning, '')
        elif tag == sanitized:
            sanitized = ''
    return sanitized

def opengraph(title, url, description, date, config=None):
    '''url parameter should end with "/" to denote a directory!
    '''
    config = config or {}
    image = config.get('site', {}).get('base_url', '') + '/' + config.get('site', {}).get('logo', '')
    optional_image_tag = f'''\n<meta property="og:image" content="{image}" />''' if image != '/' else ''
    meta_properties = [
        ('og:title', title),
        ('og:type', 'article'),
        ('og:url', url),
        ('og:description', description)
    ]
    if image != '/':
        meta_properties.append(('og:image', image))
    meta_properties.append(('og:locale', 'en-US'))
    if len(date):
        meta_properties.append(('article:published_time', date))
    return '\n'.join([_meta_tag('property', prop[0], prop[1]) for prop in meta_properties])

def _meta_tag(type, type_value, content):
    return html_tag_empty('meta', [(type, type_value), ('content', content)])

def json_ld(title, url, description, config=None):
    config = config or {}
    root_title = config.get('site', {}).get('title', '')
    json_escaped_root_title = root_title.replace('"', '\\"')
    json_escaped_title = title.replace('"', '\\"')
    json_escaped_description = description.replace('"', '\\"')
    name_block = f',"name":"{json_escaped_root_title}"' if len(root_title) else ''
    return \
f'''<script type="application/ld+json">
{{"@context":"http://schema.org","@type":"WebSite","headline":"{json_escaped_title}","url":"{url}"{name_block},"description":"{json_escaped_description}"}}</script>'''

##############################################################################
# HTML SNIPPETS
##############################################################################
def additional_head_tags(config=None):
    config = config or {}
    return '\n'.join(config.get('site', {}).get('head', [])).strip()

def html_opening_boilerplate():
    return \
'''<!DOCTYPE html>
<html lang="en-US">
<head>
<meta charset="UTF-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
<meta name="viewport" content="width=device-width,initial-scale=1">'''

def html_head_body_boilerplate():
    return \
'''</head>

<body onload="initTheme()">'''

def html_tag_line(tag, content):
    return \
f'''<{tag}>{content}</{tag}>'''

def html_tag_block(tag, content):
    return \
f'''<{tag}>
{content}
</{tag}>'''

def html_tag_empty(tag, attributes):
    html_attributes = ' '.join([f'{attr[0]}="{attr[1]}"' for attr in attributes])
    if len(html_attributes):
        return f'<{tag} {html_attributes}>'
    return ''

def html_closing_boilerplate():
    return \
'''</body>
</html>
'''

## INLINE CSS AND JAVASCRIPT
## From: https://raw.githubusercontent.com/ooz/templates/master/html/oz.css
def inline_style():
    return '''body {
    font-family: sans-serif;
    line-height: 1.5;
    color: #363636;
    background: #FFF;
    margin: 1rem auto;
    padding: 0 .6rem;
    max-width: 44em;
    scroll-behavior: smooth;
}
a { color: #07A; text-decoration: none; }
blockquote {
    background: #EAEAEA;
    border-left: .3rem solid #07A;
    border-radius: .3rem;
    margin: 0 .2rem;
    padding: 0 .5rem;
}
code {
    font-size: .9rem;
    background: #EAEAEA;
    padding: .2rem .5rem;
    white-space: nowrap;
}
footer { margin-top: 1rem; }
h1 { text-align: center; margin: 0 auto; }
h1, h2, h3, h4, h5, h6 { font-family: serif; font-weight: bold; }
header { text-align:center; }
img { max-width: 100%; }
ul.task-list, ul.task-list li.task-list-item {
    list-style-type: none;
    list-style-image: none;
}
pre { border-left: .3rem solid #07A; }
pre > code {
    font-size: .9rem;
    background: #EAEAEA;
    box-sizing: inherit;
    display: block;
    overflow-x: auto;
    margin: 0 .2rem;
    white-space: pre;
}
table {
    border-spacing: 0;
    width: 100%;
}
td, th {
    border-bottom: .1rem solid;
    padding: .8rem 1rem;
    text-align: left;
    vertical-align: top;
}

.dark-mode { color: #CACACA; background: #363636; }
.dark-mode a { color: #0A7; }
.dark-mode blockquote { background: #222; border-left: .3rem solid #0A7; }
.dark-mode code { background: #222; }
.dark-mode pre { border-left: .3rem solid #0A7; }
.large-font { font-size: 1.2em; }

.avatar { border-radius: 50%; box-shadow: 0px 1px 2px rgba(0, 0, 0, 0.2); max-width: 3rem; }
.nav { float: left; margin-right: 1rem; }
.card { background: rgba(0, 0, 0, 0.1); box-shadow: 1px 3px 6px 0 rgba(0, 0, 0, 0.2); border-radius: 5px; padding: .8rem; margin-top: .8rem; }
.social { float: right; margin-left: 1rem; }'''
# From: https://raw.githubusercontent.com/ooz/templates/master/html/oz-accessibility.js
def inline_javascript():
    return '''function toggleTheme() { document.body.classList.toggle("dark-mode") }
function initTheme() { let h=new Date().getHours(); if (h <= 8 || h >= 20) { toggleTheme() } }
function toggleFontSize() { document.body.classList.toggle("large-font") }'''

##############################################################################
# TEMPLATES
#
# * New markdown file
# * Rendering markdown file as HTML
# * Rendering sitemap
##############################################################################
def template_newpost(title='Title', description='-'):
    return \
f'''---
title: {title}
description: {description}
date: {now_utc_formatted()}
tags: {TAG_DRAFT}
---
'''

def template_page(post, config=None):
    config = config or {}
    canonical_url = post.get('url', '')
    title = post.get('title', '')
    date = post.get('date', '')
    tags = post.get('tags', '')
    description = post.get('description', '')
    raw_title = ''.join(post.get('raw_title', ''))
    raw_description = ''.join(post.get('raw_description', ''))
    logo = logo_url(config)
    author_name = config.get('author', {}).get('name', '')
    header_content = header(logo, post.get('html_headline', ''), date, config) if TAG_NO_HEADER not in tags else ''
    footer_content = ''
    if TAG_NO_FOOTER not in tags:
        footer_content = [
            footer_navigation(),
            about_and_social_icons(config)
        ]
        footer_content = '\n'.join([content for content in footer_content if len(content)])
    blocks = [_template_common_start(title, canonical_url, config)]
    if (not post.get('is_index', False)) and TAG_NO_META not in tags:
        blocks.extend([
            meta(author_name, description, tags),
            opengraph(title, canonical_url, description, date, config),
            json_ld(raw_title, canonical_url, raw_description, config)
        ])
    blocks.append(_template_common_body_and_end(header_content, post.get('html_section', ''), footer_content))
    return '\n'.join(blocks)

def _template_common_start(title, canonical_url, config):
    logo = logo_url(config)
    return '\n'.join([
        html_opening_boilerplate(),
        additional_head_tags(config),
        html_tag_line('title', pagetitle(title, config)),
        html_tag_empty('link', [('rel', 'canonical'), ('href', canonical_url)]),
        html_tag_empty('link', [('rel', 'shortcut icon'), ('href', logo)]) if len(logo) else '',
        html_tag_block('style', inline_style()),
        html_tag_block('script', inline_javascript()),
    ])

def _template_common_body_and_end(header, section, footer):
    blocks = [
        html_head_body_boilerplate(),
        html_tag_block('header', header) if len(header) else '',
        html_tag_block('section', section),
        html_tag_block('footer', footer) if len(footer) else '',
        html_closing_boilerplate()
    ]
    return '\n'.join([block for block in blocks if len(block)])

def template_sitemap(posts, config=None):
    config = config or {}
    posts = [post for post in posts if TAG_DRAFT not in post.get('tags', []) and TAG_INDEX not in post.get('tags', [])]
    sitemap_xml = []
    sitemap_xml.append('<?xml version="1.0" encoding="utf-8" standalone="yes" ?>')
    sitemap_xml.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')
    additional_entries = config.get('site', {}).get('additional_sitemap_entries', [])
    all_entries = [(post['url'], post['last_modified']) for post in posts]
    all_entries = all_entries + [(entry, '') for entry in additional_entries]
    all_entries = sorted(all_entries, key=lambda entry: entry[0])
    for entry in all_entries:
        sitemap_xml.append('  <url>')
        sitemap_xml.append('    <loc>%s</loc>' % escape(entry[0]))
        if len(entry[1]):
            sitemap_xml.append('    <lastmod>%s</lastmod>' % entry[1])
        sitemap_xml.append('  </url>')
    sitemap_xml.append('</urlset>\n')
    return '\n'.join(sitemap_xml)

def template_rss(posts, config=None):
    config = config or {}
    posts = [post for post in posts if TAG_DRAFT not in post.get('tags', []) and TAG_INDEX not in post.get('tags', [])]
    title = config.get('site', {}).get('title', '')
    base_url = config.get('site', {}).get('base_url', '')
    if title == '' and base_url != '':
        title = base_url
    rss_xml = []
    rss_xml.append('''<?xml version="1.0" encoding="utf-8" standalone="yes"?>
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">
  <channel>''')
    rss_xml.append(f'''    <title>{escape(title)}</title>''')
    rss_xml.append(f'''    <link>{escape(base_url)}</link>''')
    rss_xml.append(f'''    <description></description>''')
    rss_xml.append(f'''    <generator>Good Generator.py -- ggpy -- https://oliz.io/ggpy/</generator>''')
    rss_xml.append(f'''    <lastBuildDate>{now_utc_formatted()}</lastBuildDate>''')
    for post in posts:
        escaped_url = escape(post.get('url', ''))
        rss_xml.append(f'''    <item>''')
        rss_xml.append(f'''      <title>{escape(post.get('title', ''))}</title>''')
        rss_xml.append(f'''      <link>{escaped_url}</link>''')
        rss_xml.append(f'''      <pubDate>{escape(post.get('last_modified', ''))}</pubDate>''')
        rss_xml.append(f'''      <guid>{escaped_url}</guid>''')
        rss_xml.append(f'''      <description>{escape(post.get('html_section', ''))}</description>''')
        rss_xml.append(f'''    </item>''')
    rss_xml.append('''  </channel>
</rss>\n''')
    return '\n'.join(rss_xml)

##############################################################################
# PURE LIBRARY FUNCTIONS, UTILITIES AND HELPERS
##############################################################################
_KEBAB_ALPHABET = '0123456789abcdefghijklmnopqrstuvwxyz-'
def kebab_case(word):
    return ''.join(c for c in word.lower().replace(' ', '-') if c in _KEBAB_ALPHABET)

def convert_path(filepath):
    targetpath = filepath[:-3]
    if targetpath.endswith('README'):
        targetpath = targetpath[:-6] + 'index'
    targetpath += '.html'
    return targetpath

##############################################################################
# SIDE-EFFECTS, interacting with filesystem
##############################################################################
def read_file(path):
    with open(path, 'r') as f:
        return f.read()

def write_file(path, content=''):
    with open(path, 'w') as f:
        f.write(content)

def scan_posts(directories, config=None):
    config = config or {}
    posts = []
    for directory in directories:
        paths = glob.glob(directory + '/**/*.md', recursive=True)
        for path in paths:
            post = read_post(directory, path, config=config)
            posts.append(post)
    return posts

def generate(directories, config=None):
    config = config or {}
    posts = scan_posts(directories, config)
    indices = [post for post in posts if TAG_INDEX in post['tags']]
    for index in indices:
        index['html_section'] = posts_index(posts)
        index['html'] = template_page(index, config)
    sitemap_and_rss_files = []
    if config.get('site', {}).get('generate_sitemap', False):
        sitemap_and_rss_files.append({
            'filepath': 'sitemap.xml',
            'html': template_sitemap(posts, config)
        })
    if config.get('site', {}).get('generate_rss', False):
        sitemap_and_rss_files.append({
            'filepath': 'rss.xml',
            'html': template_rss(posts, config)
        })
    posts.extend(sitemap_and_rss_files)
    for post in posts:
        write_file(post['filepath'], post['html'])

def convert_canonical(directory, targetpath, config=None):
    config = config or {}
    base_url = config.get('site', {}).get('base_url', '')
    targetpath = os.path.relpath(targetpath, directory)
    if len(base_url):
        if targetpath.endswith('index.html'):
            return f'{base_url}/{targetpath[:-10]}'
        return f'{base_url}/{targetpath}'
    else:
        if targetpath.endswith('index.html') and targetpath != 'index.html':
            return f'{targetpath[:-10]}'
    return targetpath

def read_post(directory, filepath, config=None):
    markdown_content = read_file(filepath)
    post = markdown2post(markdown_content, config)
    targetpath = convert_path(filepath)
    canonical_url = convert_canonical(directory, targetpath, config)
    post['filepath'] = targetpath
    post['url'] = canonical_url
    post['last_modified'] = last_modified(filepath)
    post['is_index'] = TAG_INDEX in post['tags']
    post['html'] = template_page(post, config)
    return post

REPO = None
try:
    import git
    REPO = git.Repo()
except ImportError: # pragma: no cover because git package is normally present, last_modified tested without
    print('No gitpython package found, degrading functionality (no last_modified support)!', file=sys.stderr)

def last_modified(filepath):
    if REPO:
        for commit in REPO.iter_commits(paths=filepath, max_count=1):
            return time.strftime('%Y-%m-%d', time.gmtime(commit.authored_date))
    return ''

def now_utc_formatted():
    now = time.localtime()
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', now)

##############################################################################
# MAIN PROGRAM
##############################################################################
if __name__ == '__main__': # pragma: no cover because main wrapper
    parser = argparse.ArgumentParser(description='The Good Generator for static websites and blogs.')
    parser.add_argument('-n', '--newpost', metavar='TITLE', type=str, nargs='?',
                        const='New Post',
                        default=argparse.SUPPRESS,
                        help='Creates a new post with TITLE.')
    parser.add_argument('directories', metavar='DIR', type=str, nargs='*',
                        help='Directory to convert recursively.')
    args = vars(parser.parse_args())

    config = {}
    try:
        import ggconfig
        config = ggconfig.config
    except ImportError:
        print('No ggconfig.py found, assuming defaults!', file=sys.stderr)

    if args.get('newpost', None):
        title = args.get('newpost')
        write_file(kebab_case(title) + '.md', template_newpost(title))
    if len(args.get('directories')):
        generate(args.get('directories'), config)
