#!/usr/bin/env python
# -*- coding: utf-8 -*-

import gg

def test_pagetitle():
    assert gg.pagetitle('Good Generator.py', gg.CONFIG) == 'Good Generator.py'
    assert gg.pagetitle('Some Page', gg.CONFIG) == 'Some Page | Good Generator.py'
    assert gg.pagetitle('Title with default config') == 'Title with default config'
    assert gg.pagetitle('') == ''
    assert gg.pagetitle() == ''

def test_style():
    style = gg.style()
    # CSS
    assert '<style>' in style
    assert 'body {' in style
    assert '.avatar' in style
    assert '.nav' in style
    assert '.social' in style
    assert '.dark-mode' in style
    assert '</style>' in style
    # JS for dark-mode switch
    assert '<script>' in style
    assert 'function toggleTheme' in style
    assert 'function initTheme' in style
    assert '</script>' in style

def test_meta():
    meta = gg.meta('oz', 'Nice text!', 'foo, bar, tags')
    assert meta == \
'''<meta name="author" content="oz" />
<meta name="description" content="Nice text!" />
<meta name="keywords" content="foo, bar, tags" />'''

def test_twitter():
    twitter = gg.twitter('@oozgo')
    assert twitter == \
'''<meta name="twitter:author" content="@oozgo" />
<meta name="twitter:card" content="summary" />
<meta name="twitter:creator" content="@oozgo" />'''

def test_opengraph():
    opengraph = gg.opengraph('Title!', 'https://ooz.github.io/ggpy/', 'Nice text!', '2020-02-20', gg.CONFIG)
    assert opengraph == \
'''<meta property="og:title" content="Title!" />
<meta property="og:type" content="article" />
<meta property="og:url" content="https://ooz.github.io/ggpy/" />
<meta property="og:description" content="Nice text!" />
<meta property="og:image" content="https://ooz.github.io/ggpy/static/gg.png" />
<meta property="og:locale" content="en-US" />
<meta property="article:published_time" content="2020-02-20" />'''
    opengraph_default_config = gg.opengraph('Title!', 'https://ooz.github.io/ggpy/', 'Nice text!', '2020-02-20')
    assert opengraph_default_config == \
'''<meta property="og:title" content="Title!" />
<meta property="og:type" content="article" />
<meta property="og:url" content="https://ooz.github.io/ggpy/" />
<meta property="og:description" content="Nice text!" />
<meta property="og:locale" content="en-US" />
<meta property="article:published_time" content="2020-02-20" />'''

def test_json_ld():
    json_ld = gg.json_ld('Title! "BAM!"', 'https://ooz.github.io/ggpy/', 'It says "BAM!"', gg.CONFIG)
    assert json_ld == \
'''<script type="application/ld+json">
{"@context":"http://schema.org","@type":"WebSite","headline":"Title! \\"BAM!\\"","url":"https://ooz.github.io/ggpy/","name":"Good Generator.py","description":"It says \\"BAM!\\""}</script>'''
    json_ld_default_config = gg.json_ld('Title! "BAM!"', 'https://ooz.github.io/ggpy/', 'It says "BAM!"')
    assert json_ld_default_config == \
'''<script type="application/ld+json">
{"@context":"http://schema.org","@type":"WebSite","headline":"Title! \\"BAM!\\"","url":"https://ooz.github.io/ggpy/","description":"It says \\"BAM!\\""}</script>'''

def test_post_header():
    post_header = gg.post_header('<h1 id="title">Title!</h1>', '2020-02-20', gg.CONFIG)
    assert post_header == \
'''<div style="text-align:right;">
<h1 id="title">Title!</h1>
<small><a href="https://ooz.github.io/ggpy">Good Gen</a>, 2020-02-20</small>
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
    about_and_social = gg.about_and_social_icons(gg.CONFIG)
    assert about_and_social == \
'''<a href="mailto:example@example.com" class="social">email</a>
<a href="https://twitter.com/oozgo" class="social">twitter</a>
<a href="https://github.com/ooz/ggpy" class="social">github</a>
<a href="https://ooz.github.io/ggpy/test/about" class="social">about</a>'''
    about_and_social_default_config = gg.about_and_social_icons()
    assert about_and_social_default_config == ''
