#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import re

from gg import read_file

SITE_TITLE = 'Good Generator.py'
LOGO_URL = 'https://oliz.io/ggpy/static/gg.png'
GENERATED_FEATURE_HTML = \
f'''<header>
<a href="https://oliz.io/ggpy"><img src="{LOGO_URL}" class="avatar" /></a>
<div style="text-align:right;">
<h1 id="markdown-feature-test-without-quotes-bug">Markdown Feature Test without &quot;quotes bug&quot;</h1>
<small><a href="https://oliz.io/ggpy">Good Gen</a>, 1996-06-06</small>
</div>
</header>
<section>
<h2 id="headline-2">Headline 2</h2>
<p>Paragraph
with
non-empty
lines.</p>
<h2 id="lists">Lists</h2>
<ol>
<li><strong>Ordered list item, bold</strong></li>
<li><em>Ordered list item, italic</em></li>
</ol>
<hr />
<ul>
<li>Normal unordered list item</li>
<li><del>Unordered list item, DELETED!</del></li>
<li><code>Unordered list item, inline coded</code></li>
</ul>
<hr />
<ul class="task-list">
<li class="task-list-item"><input type="checkbox" disabled/> unchecked</li>
<li class="task-list-item"><input type="checkbox" disabled checked/> checked</li>
</ul>
<h2 id="code">Code</h2>
<pre class="highlight"><code># Code blocks work</code></pre>
<pre class="highlight"><code class="language-python">def python_code_blocks():
    return "work, too!"</code></pre>
<p>Let there be...</p>
<pre><code>another
code
block
</code></pre>
<h2 id="tables">Tables</h2>
<table>
<thead>
<tr>
<th>Tables</th>
<th>work</th>
<th style="text-align: right;">just</th>
<th>fine</th>
</tr>
</thead>
<tbody>
<tr>
<td>for</td>
<td>real</td>
<td style="text-align: right;">yep</td>
<td>yeah.</td>
</tr>
</tbody>
</table>
<h2 id="quotes">Quotes</h2>
<blockquote>
<p>"So smart"</p>
<p>"So smart" - me, sometimes</p>
</blockquote>
<h2 id="image">Image</h2>
<p><img alt="Good Generator Logo" src="https://oliz.io/ggpy/static/gg.png" /></p>
<p>Horizontal rule...</p>
<hr />
<h2 id="other-markdown-extensions">Other Markdown Extensions</h2>
<h3 id="definition-lists-and-footnotes">Definition Lists and Footnotes</h3>
<dl>
<dt>Definition List</dt>
<dd>is defined here<sup id="fnref:1"><a class="footnote-ref" href="#fn:1">1</a></sup>.</dd>
<dt>Other List</dt>
<dd>is defined here<sup id="fnref:here"><a class="footnote-ref" href="#fn:here">2</a></sup>.</dd>
</dl>
<h3 id="abbreviations">Abbreviations</h3>
<p><abbr title="Hyper Text Markup Language">HTML</abbr></p>
<h2 id="leftovers">Leftovers</h2>
<p>Yep, now the footnotes are arriving!</p>
<div class="footnote">
<hr />
<ol>
<li id="fn:1">
<p>Numbered footnote&#160;<a class="footnote-backref" href="#fnref:1" title="Jump back to footnote 1 in the text">&#8617;</a></p>
</li>
<li id="fn:here">
<p>Labeled footnote&#160;<a class="footnote-backref" href="#fnref:here" title="Jump back to footnote 2 in the text">&#8617;</a></p>
</li>
</ol>
</div>
</section>
'''
GENERATED_POST_HTML = \
f'''<header>
<a href="https://oliz.io/ggpy"><img src="{LOGO_URL}" class="avatar" /></a>
<div style="text-align:right;">
<h1 id="some-post">Some Post</h1>
<small><a href="https://oliz.io/ggpy">Good Gen</a>, 2018-03-17</small>
</div>
</header>
<section>
<p>Yep! Intro text!</p>
<h2 id="headline">Headline</h2>
<p>More text!</p>
</section>
'''

def test_generate() -> None:
    import gg
    from ggconfig import config
    gg.generate(['.'], config)

def test_sitemap_generation() -> None:
    sitemap_data = read_file('sitemap.xml')
    assert re.match(r'''<\?xml version="1.0" encoding="utf-8" standalone="yes" \?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://oliz.io/ggpy/</loc>
    <lastmod>[\d\-]{10}</lastmod>
  </url>
  <url>
    <loc>https://oliz.io/ggpy/CHANGELOG.html</loc>
    <lastmod>[\d\-]{10}</lastmod>
  </url>
  <url>
    <loc>https://oliz.io/ggpy/test/features/</loc>
    <lastmod>[\d\-]{10}</lastmod>
  </url>
  <url>
    <loc>https://oliz.io/ggpy/test/features/index-inline-posts/little-inline-content-no-description.html</loc>
    <lastmod>[\d\-]{10}</lastmod>
  </url>
  <url>
    <loc>https://oliz.io/ggpy/test/features/index-inline-posts/lots-of-content-no-description.html</loc>
    <lastmod>[\d\-]{10}</lastmod>
  </url>
  <url>
    <loc>https://oliz.io/ggpy/test/features/index-inline-posts/lots-of-content-with-description.html</loc>
    <lastmod>[\d\-]{10}</lastmod>
  </url>
  <url>
    <loc>https://oliz.io/ggpy/test/features/index-inline-posts/no-content-with-description.html</loc>
    <lastmod>[\d\-]{10}</lastmod>
  </url>
  <url>
    <loc>https://oliz.io/ggpy/test/features/meta.html</loc>
    <lastmod>[\d\-]{10}</lastmod>
  </url>
  <url>
    <loc>https://oliz.io/ggpy/test/some-post.html</loc>
    <lastmod>[\d\-]{10}</lastmod>
  </url>
</urlset>
''', sitemap_data)

def test_sitemap_does_not_include_drafts() -> None:
    sitemap_data = read_file('sitemap.xml')
    assert 'draft-not-included-in-sitemap' not in sitemap_data

def test_rss_generation() -> None:
    rss = read_file('rss.xml')
    assert rss.startswith('''<?xml version="1.0" encoding="utf-8" standalone="yes"?>
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">
  <channel>''')
    assert rss.endswith('''</rss>\n''')

def test_markdown_features_and_readme_generation() -> None:
    # given & when
    index_title = 'Markdown Feature Test without &quot;quotes bug&quot;'
    index_raw_title = 'Markdown Feature Test without "quotes bug"'
    canonical_url = 'https://oliz.io/ggpy/test/features/'
    index_data = read_file('test/features/index.html')

    # then
    index_data = then_is_framed_by_html_boilerplate(index_data)
    index_data = then_has_bottom_navigation_and_social_links(index_data)
    index_data = then_has_title_canonical_and_favicon(
        index_data,
        title=f'{index_title} | {SITE_TITLE}',
        canonical_url=canonical_url,
        favicon_url=LOGO_URL
    )
    index_data = then_has_style(index_data)
    index_data = then_head_ends_with_meta_tags(
        index_data,
        title=index_title,
        raw_title=index_raw_title,
        description=index_title,
        raw_description=index_raw_title,
        canonical_url=canonical_url,
        creation_time='1996-06-06T13:37:42Z'
    )
    index_data = then_has_body(index_data)
    assert GENERATED_FEATURE_HTML == index_data

def test_post_conversion() -> None:
    # given & when
    post_title = 'Some Post'
    description = 'Nice post!'
    canonical_url = 'https://oliz.io/ggpy/test/some-post.html'
    post_data = read_file('test/some-post.html')

    # then
    post_data = then_is_framed_by_html_boilerplate(post_data)
    post_data = then_has_bottom_navigation_and_social_links(post_data)
    post_data = then_has_title_canonical_and_favicon(
        post_data,
        title=f'{post_title} | {SITE_TITLE}',
        canonical_url=canonical_url,
        favicon_url=LOGO_URL
    )
    post_data = then_has_style(post_data)
    post_data = then_head_ends_with_meta_tags(
        post_data,
        title=post_title,
        raw_title=post_title,
        description=description,
        raw_description=description,
        canonical_url=canonical_url,
        creation_time='2018-03-17T13:37:42Z'
    )
    post_data = then_has_body(post_data)
    assert GENERATED_POST_HTML == post_data

def then_is_framed_by_html_boilerplate(result:str) -> str:
    html_start = \
'''<!DOCTYPE html>
<html lang="en-US">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta http-equiv="Content-Security-Policy" content="script-src 'unsafe-inline'">
<meta name="referrer" content="no-referrer">
'''
    html_end = \
'''</body>
</html>
'''
    assert result.startswith(html_start)
    assert result.endswith(html_end)
    return result.replace(html_start, '').replace(html_end, '')

def then_has_bottom_navigation_and_social_links(result:str) -> str:
    navigation_and_social_links = \
'''<footer>
<a href="#" class="nav">top</a>
<a href="javascript:toggleTheme()" class="nav">🌓</a>
<a href="javascript:toggleFontSize()" class="nav">aA</a>
<a href="https://oliz.io/about.html" class="social">about</a>
<a href="https://github.com/ooz/ggpy" class="social">github</a>
<a href="https://nitter.net/" class="social">twitter</a>
<a href="mailto:example@example.com" class="social">email</a>
</footer>
'''
    assert result.endswith(navigation_and_social_links)
    return result.replace(navigation_and_social_links, '')

def then_has_title_canonical_and_favicon(result:str, title:str='', canonical_url:str='', favicon_url:str='') -> str:
    title_and_links = \
f'''<title>{title}</title>
<link rel="canonical" href="{canonical_url}">
<link rel="shortcut icon" href="{favicon_url}">
'''
    assert result.startswith(title_and_links)
    return result.replace(title_and_links, '')

def then_has_style(result:str) -> str:
    style = \
'''<style>
body {
    font-family: sans-serif;
    line-height: 1.5;
    color: #363636;
    background: #FFF;
    margin: 1rem auto;
    padding: 0 .6rem 1rem .6rem;
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

.avatar { border-radius: 50%; max-width: 5rem; }
.nav { float: left; margin-right: 1rem; }
.card { background: rgba(0, 0, 0, 0.1); border-radius: 5px; padding: .8rem; margin-top: .8rem; }
.social { float: right; margin-left: 1rem; }
</style>
<script>
function toggleTheme() { document.body.classList.toggle("dark-mode") }
function initTheme() { let h=new Date().getHours(); if (h <= 8 || h >= 20) { toggleTheme() } }
function toggleFontSize() { document.body.classList.toggle("large-font") }
</script>
'''
    assert result.startswith(style)
    return result.replace(style, '')

def then_head_ends_with_meta_tags(result:str, title:str='', raw_title:str='', description:str='', raw_description:str='', canonical_url:str='', creation_time:str='') -> str:
    json_escaped_raw_title = raw_title.replace('"', '\\"')
    json_escaped_raw_description = raw_description.replace('"', '\\"')
    meta = \
f'''<meta name="author" content="Good Gen">
<meta name="description" content="{description}">
<meta property="og:title" content="{title}">
<meta property="og:type" content="article">
<meta property="og:url" content="{canonical_url}">
<meta property="og:description" content="{description}">
<meta property="og:image" content="{LOGO_URL}">
<meta property="og:locale" content="en-US">
<meta property="article:published_time" content="{creation_time}">
<script type="application/ld+json">{{"@context":"http://schema.org","@type":"WebSite","headline":"{json_escaped_raw_title}","url":"{canonical_url}","name":"Good Generator.py","description":"{json_escaped_raw_description}"}}</script>
</head>

'''
    print(result)
    print(meta)
    assert result.startswith(meta)
    return result.replace(meta, '')

def then_has_body(result:str) -> str:
    body = \
'''<body onload="initTheme()">
'''
    assert result.startswith(body)
    return result.replace(body, '')
