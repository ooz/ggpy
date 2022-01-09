#!/usr/bin/env python
# -*- coding: utf-8 -*-

import gg
from ggconfig import config

##############################################################################
# CONTENT SNIPPETS
##############################################################################
def test_logo_url() -> None:
    assert gg.logo_url(config) == 'https://oliz.io/ggpy/static/gg.png'
    assert gg.logo_url() == ''

def test_pagetitle() -> None:
    assert gg.pagetitle('Good Generator.py', config) == 'Good Generator.py'
    assert gg.pagetitle('Some Page', config) == 'Some Page | Good Generator.py'
    assert gg.pagetitle('Title with default config') == 'Title with default config'
    assert gg.pagetitle('') == ''
    assert gg.pagetitle() == ''
    assert gg.pagetitle('', config) == 'Good Generator.py'

def test_meta() -> None:
    meta = gg.meta('oz', 'Nice text!', '__draft__, foo, __inline__, bar, tags, __no_header__')
    assert meta == \
'''<meta name="author" content="oz">
<meta name="description" content="Nice text!">
<meta name="keywords" content="foo, bar, tags">'''

def test_meta_single_special_tag() -> None:
    meta = gg.meta('oz', 'Nice text!', '__draft__')
    assert meta == \
'''<meta name="author" content="oz">
<meta name="description" content="Nice text!">'''

def test_opengraph() -> None:
    opengraph = gg.opengraph('Title!', 'https://oliz.io/ggpy/', 'Nice text!', '2020-02-20', config)
    assert opengraph == \
'''<meta property="og:title" content="Title!">
<meta property="og:type" content="article">
<meta property="og:url" content="https://oliz.io/ggpy/">
<meta property="og:description" content="Nice text!">
<meta property="og:image" content="https://oliz.io/ggpy/static/gg.png">
<meta property="og:locale" content="en-US">
<meta property="article:published_time" content="2020-02-20">'''
    opengraph_default_config = gg.opengraph('Title!', 'https://oliz.io/ggpy/', 'Nice text!', '2020-02-20')
    assert opengraph_default_config == \
'''<meta property="og:title" content="Title!">
<meta property="og:type" content="article">
<meta property="og:url" content="https://oliz.io/ggpy/">
<meta property="og:description" content="Nice text!">
<meta property="og:locale" content="en-US">
<meta property="article:published_time" content="2020-02-20">'''

def test_json_ld() -> None:
    json_ld = gg.json_ld('Title! "BAM!"', 'https://oliz.io/ggpy/', 'It says "BAM!"', config)
    assert json_ld == \
'''<script type="application/ld+json">
{"@context":"http://schema.org","@type":"WebSite","headline":"Title! \\"BAM!\\"","url":"https://oliz.io/ggpy/","name":"Good Generator.py","description":"It says \\"BAM!\\""}</script>'''
    json_ld_default_config = gg.json_ld('Title! "BAM!"', 'https://oliz.io/ggpy/', 'It says "BAM!"')
    assert json_ld_default_config == \
'''<script type="application/ld+json">
{"@context":"http://schema.org","@type":"WebSite","headline":"Title! \\"BAM!\\"","url":"https://oliz.io/ggpy/","description":"It says \\"BAM!\\""}</script>'''

def test_header() -> None:
    header = gg.header('https://example.com/logo.png', '<h1>Title!</h1>', '2021-03-27', config)
    assert header == \
'''<a href="https://oliz.io/ggpy"><img src="https://example.com/logo.png" class="avatar" /></a>
<div style="text-align:right;">
<h1>Title!</h1>
<small><a href="https://oliz.io/ggpy">Good Gen</a>, 2021-03-27</small>
</div>'''
    header_default_config = gg.header('', '<h1>Title!</h1>', '2021-03-27')
    assert header_default_config == \
'''<div style="text-align:right;">
<h1>Title!</h1>
<small>2021-03-27</small>
</div>'''

def test_post_header() -> None:
    post_header = gg.post_header('<h1 id="title">Title!</h1>', '2020-02-20', config)
    assert post_header == \
'''<div style="text-align:right;">
<h1 id="title">Title!</h1>
<small><a href="https://oliz.io/ggpy">Good Gen</a>, 2020-02-20</small>
</div>'''
    post_header_default_config = gg.post_header('<h1 id="title">Title!</h1>', '2020-02-20')
    assert post_header_default_config == \
'''<div style="text-align:right;">
<h1 id="title">Title!</h1>
<small>2020-02-20</small>
</div>'''

def test_footer_navigation() -> None:
    footer_nav = gg.footer_navigation()
    assert footer_nav == \
'''<a href="#" class="nav">top</a>
<a href="javascript:toggleTheme()" class="nav">🌓</a>
<a href="javascript:toggleFontSize()" class="nav">aA</a>'''

def test_about_and_social_icons() -> None:
    about_and_social = gg.about_and_social_icons(config)
    assert about_and_social == \
'''<a href="mailto:example@example.com" class="social">email</a>
<a href="https://nitter.net/" class="social">twitter</a>
<a href="https://github.com/ooz/ggpy" class="social">github</a>
<a href="https://oliz.io/about.html" class="social">about</a>'''
    about_and_social_default_config = gg.about_and_social_icons()
    assert about_and_social_default_config == ''

def test_posts_index() -> None:
    '''Generate index without inlined posts.
    '''
    posts = gg.scan_posts(['.'])
    posts = [post for post in posts if gg.TAG_INLINE not in post['tags']]
    posts_index = gg.posts_index(posts)
    assert posts_index == \
'''<div>
<div class="card"><small class="social">2021-04-04</small><a href="test/features/meta.html"><b>Markdown Meta Data</b></a></div>
<div class="card"><small class="social">2018-03-17</small><a href="test/some-post.html"><b>Some Post</b></a></div>
<div class="card"><small class="social">1996-06-06</small><a href="test/features/"><b>Markdown Feature Test without &quot;quotes bug&quot;</b></a></div>
</div>'''

def test_posts_index_inline() -> None:
    '''Generate index with inlined posts.

    Four cases:
    1. Lots of content but not description -> details block with title as summary
    2. Lots of content with description    -> details block with description as summary
    3. Has description but no content      -> only show description
    4. Else                                -> show content directly
    '''
    posts = gg.scan_posts(['test/features/index-inline-posts/'])
    posts_index = gg.posts_index(posts)
    assert posts_index == \
'''<div>
<div class="card"><small class="social">2021-07-17</small>
<a href="little-inline-content-no-description.html"><b>Little inline content, no description</b></a>
<div>
<p>This shows directly on the card, without details+summary blocks.</p>
</div>
</div>
<div class="card"><small class="social">2021-07-17</small>
<a href="no-content-with-description.html"><b>No content, but with description</b></a>
<div>
Just some more minor text from the description
</div>
</div>
<div class="card"><small class="social">2021-07-17</small>
<a href="lots-of-content-with-description.html"><b>Lots of content, with description</b></a>
<details><summary>Click here to expand...</summary>
<ul>
<li>One</li>
<li>Two</li>
<li>Three</li>
<li>Four</li>
<li>Five</li>
<li>Six</li>
<li>Seven</li>
<li>Eight</li>
<li>Nine</li>
<li>Ten</li>
</ul>
<p>... and some more lines.</p>
</details>
</div>
<div class="card"><small class="social">2021-07-17</small>
<details><summary><a href="lots-of-content-no-description.html"><b>Lots of content, no description</b></a></summary>
<ul>
<li>One</li>
<li>Two</li>
<li>Three</li>
<li>Four</li>
<li>Five</li>
<li>Six</li>
<li>Seven</li>
<li>Eight</li>
<li>Nine</li>
<li>Ten</li>
</ul>
<p>... and some more lines.</p>
</details>
</div>
</div>'''

##############################################################################
# HTML SNIPPETS
##############################################################################
def test_html_opening_boilerplate() -> None:
    assert gg.html_opening_boilerplate() == \
'''<!DOCTYPE html>
<html lang="en-US">
<head>
<meta charset="UTF-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
<meta name="viewport" content="width=device-width,initial-scale=1">'''

def test_html_head_body_boilerplate() -> None:
    assert gg.html_head_body_boilerplate() == \
'''</head>

<body onload="initTheme()">'''

def test_html_tag_line() -> None:
    assert gg.html_tag_line('title', 'Nice!') == '<title>Nice!</title>'

def test_html_tag_block() -> None:
    assert gg.html_tag_block('footer', '<p>in closing</p>') == \
'''<footer>
<p>in closing</p>
</footer>'''

def test_html_tag_empty() -> None:
    link_tag = gg.html_tag_empty('link', [('rel', 'canonical'), ('href','https://example.com')])
    assert link_tag == '<link rel="canonical" href="https://example.com">'
    omit_empty_tag = gg.html_tag_empty('link', [])
    assert omit_empty_tag == ''

def test_html_closing_boilerplate() -> None:
    assert gg.html_closing_boilerplate() == \
'''</body>
</html>
'''

def test_inline_style() -> None:
    style = gg.inline_style()
    assert 'body {' in style
    assert '.dark-mode' in style
    assert '.avatar' in style
    assert '.nav' in style
    assert '.social' in style

def test_inline_javascript() -> None:
    js = gg.inline_javascript()
    assert 'function toggleTheme' in js
    assert 'function initTheme' in js
