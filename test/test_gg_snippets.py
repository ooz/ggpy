#!/usr/bin/env python
# -*- coding: utf-8 -*-

import gg
from ggconfig import config

##############################################################################
# CONTENT SNIPPETS
##############################################################################
def test_logo_url():
    assert gg.logo_url(config) == 'https://oliz.io/ggpy/static/gg.png'
    assert gg.logo_url() == ''

def test_pagetitle():
    assert gg.pagetitle('Good Generator.py', config) == 'Good Generator.py'
    assert gg.pagetitle('Some Page', config) == 'Some Page | Good Generator.py'
    assert gg.pagetitle('Title with default config') == 'Title with default config'
    assert gg.pagetitle('') == ''
    assert gg.pagetitle() == ''
    assert gg.pagetitle('', config) == 'Good Generator.py'

def test_meta():
    meta = gg.meta('oz', 'Nice text!', 'foo, bar, tags')
    assert meta == \
'''<meta name="author" content="oz">
<meta name="description" content="Nice text!">
<meta name="keywords" content="foo, bar, tags">'''

def test_twitter():
    twitter = gg.twitter(config)
    assert twitter == \
'''<meta name="twitter:author" content="@oozgo">
<meta name="twitter:card" content="summary">
<meta name="twitter:creator" content="@oozgo">'''
    twitter_not_configured = gg.twitter()
    assert twitter_not_configured == ''

def test_opengraph():
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

def test_json_ld():
    json_ld = gg.json_ld('Title! "BAM!"', 'https://oliz.io/ggpy/', 'It says "BAM!"', config)
    assert json_ld == \
'''<script type="application/ld+json">
{"@context":"http://schema.org","@type":"WebSite","headline":"Title! \\"BAM!\\"","url":"https://oliz.io/ggpy/","name":"Good Generator.py","description":"It says \\"BAM!\\""}</script>'''
    json_ld_default_config = gg.json_ld('Title! "BAM!"', 'https://oliz.io/ggpy/', 'It says "BAM!"')
    assert json_ld_default_config == \
'''<script type="application/ld+json">
{"@context":"http://schema.org","@type":"WebSite","headline":"Title! \\"BAM!\\"","url":"https://oliz.io/ggpy/","description":"It says \\"BAM!\\""}</script>'''

def test_header():
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

def test_post_header():
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

def test_footer_navigation():
    footer_nav = gg.footer_navigation('https://example.com', False)
    assert footer_nav == \
'''<a href="https://example.com" class="nav">back</a>
<a href="#" class="nav">top</a>
<a href="javascript:toggleTheme()" class="nav">🌓</a>'''

def test_about_and_social_icons():
    about_and_social = gg.about_and_social_icons(config)
    assert about_and_social == \
'''<a href="mailto:example@example.com" class="social">email</a>
<a href="https://twitter.com/oozgo" class="social">twitter</a>
<a href="https://github.com/ooz/ggpy" class="social">github</a>
<a href="https://oliz.io/ggpy/test/about" class="social">about</a>'''
    about_and_social_default_config = gg.about_and_social_icons()
    assert about_and_social_default_config == ''

def test_posts_index():
    posts = gg.scan_posts(['.'])
    assert len(posts) == 6
    posts_index = gg.posts_index(posts)
    assert posts_index == \
'''<table>
<tbody>
<tr><td>2021-04-04</td><td><a href="test/features/meta.html">Markdown Meta Data</a></td></tr>
<tr><td>2018-05-06</td><td><a href="test/about/">About / Impress / Privacy / Legal</a></td></tr>
<tr><td>2018-03-17</td><td><a href="test/features/draft-not-included-in-sitemap.html">Draft</a></td></tr>
<tr><td>2018-03-17</td><td><a href="test/some-post.html">Some Post</a></td></tr>
<tr><td>1337-06-06</td><td><a href="test/features/">Markdown Feature Test without &quot;quotes bug&quot;</a></td></tr>
</tbody>
</table>'''

##############################################################################
# HTML SNIPPETS
##############################################################################
def test_html_opening_boilerplate():
    assert gg.html_opening_boilerplate() == \
'''<!DOCTYPE html>
<html lang="en-US">
<head>
<meta charset="UTF-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
<meta name="viewport" content="width=device-width,initial-scale=1">'''

def test_html_head_body_boilerplate():
    assert gg.html_head_body_boilerplate() == \
'''</head>

<body onload="initTheme()">'''

def test_html_tag_line():
    assert gg.html_tag_line('title', 'Nice!') == '<title>Nice!</title>'

def test_html_tag_block():
    assert gg.html_tag_block('footer', '<p>in closing</p>') == \
'''<footer>
<p>in closing</p>
</footer>'''

def test_html_tag_empty():
    link_tag = gg.html_tag_empty('link', [('rel', 'canonical'), ('href','https://example.com')])
    assert link_tag == '<link rel="canonical" href="https://example.com">'
    omit_empty_tag = gg.html_tag_empty('link', [])
    assert omit_empty_tag == ''

def test_html_closing_boilerplate():
    assert gg.html_closing_boilerplate() == \
'''</body>
</html>
'''

def test_inline_style():
    style = gg.inline_style()
    assert 'body {' in style
    assert '.dark-mode' in style
    assert '.avatar' in style
    assert '.nav' in style
    assert '.social' in style

def test_inline_javascript():
    js = gg.inline_javascript()
    assert 'function toggleTheme' in js
    assert 'function initTheme' in js
