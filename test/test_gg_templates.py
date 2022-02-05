#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
from typing import Any, Dict, List

import gg
from ggconfig import config

def test_newpost() -> None:
    assert re.match(r'''---
title: Title
description: -
date: \d+-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z
tags: __draft__
---
''', gg.template_newpost())

def test_template_page() -> None:
    post = {
        'url': 'https://oliz.io/ggpy/',
        'html_section': '<h1>Hey!</h1>'
    }
    rendered_post = gg.template_page(post, config)
    assert rendered_post == \
'''<!DOCTYPE html>
<html lang="en-US">
<head>
<meta charset="UTF-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta http-equiv="Content-Security-Policy" content="script-src 'unsafe-inline'">
<meta name="referrer" content="no-referrer">
<title>Good Generator.py</title>
<link rel="canonical" href="https://oliz.io/ggpy/">
<link rel="shortcut icon" href="https://oliz.io/ggpy/static/gg.png">
<style>
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
<meta name="author" content="Good Gen">
<meta property="og:title" content="">
<meta property="og:type" content="article">
<meta property="og:url" content="https://oliz.io/ggpy/">
<meta property="og:description" content="">
<meta property="og:image" content="https://oliz.io/ggpy/static/gg.png">
<meta property="og:locale" content="en-US">
<script type="application/ld+json">{"@context":"http://schema.org","@type":"WebSite","headline":"","url":"https://oliz.io/ggpy/","name":"Good Generator.py","description":""}</script>
</head>

<body onload="initTheme()">
<header>
<a href="https://oliz.io/ggpy"><img src="https://oliz.io/ggpy/static/gg.png" class="avatar" /></a>
</header>
<section>
<h1>Hey!</h1>
</section>
<footer>
<a href="#" class="nav">top</a>
<a href="javascript:toggleTheme()" class="nav">🌓</a>
<a href="javascript:toggleFontSize()" class="nav">aA</a>
<a href="https://oliz.io/about.html" class="social">about</a>
<a href="https://github.com/ooz/ggpy" class="social">github</a>
<a href="https://nitter.net/" class="social">twitter</a>
<a href="mailto:example@example.com" class="social">email</a>
</footer>
</body>
</html>
'''

def test_template_page_without_config() -> None:
    post = {
        'url': 'index.html',
        'html_section': '<h1>Hey!</h1>'
    }
    rendered_post = gg.template_page(post)
    assert rendered_post == \
'''<!DOCTYPE html>
<html lang="en-US">
<head>
<meta charset="UTF-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
<meta name="viewport" content="width=device-width,initial-scale=1">

<title></title>
<link rel="canonical" href="index.html">

<style>
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

<meta property="og:title" content="">
<meta property="og:type" content="article">
<meta property="og:url" content="index.html">
<meta property="og:description" content="">
<meta property="og:locale" content="en-US">
<script type="application/ld+json">{"@context":"http://schema.org","@type":"WebSite","headline":"","url":"index.html","description":""}</script>
</head>

<body onload="initTheme()">
<section>
<h1>Hey!</h1>
</section>
<footer>
<a href="#" class="nav">top</a>
<a href="javascript:toggleTheme()" class="nav">🌓</a>
<a href="javascript:toggleFontSize()" class="nav">aA</a>
</footer>
</body>
</html>
'''

def test_template_page_as_index() -> None:
    index:Dict[str, Any] = {}
    index['url'] = 'https://oliz.io/ggpy'
    index['is_index'] = True
    index['html_section'] = gg.posts_index(given_posts())
    rendered_index = gg.template_page(index, config)
    assert rendered_index == \
'''<!DOCTYPE html>
<html lang="en-US">
<head>
<meta charset="UTF-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta http-equiv="Content-Security-Policy" content="script-src 'unsafe-inline'">
<meta name="referrer" content="no-referrer">
<title>Good Generator.py</title>
<link rel="canonical" href="https://oliz.io/ggpy">
<link rel="shortcut icon" href="https://oliz.io/ggpy/static/gg.png">
<style>
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
</head>

<body onload="initTheme()">
<header>
<a href="https://oliz.io/ggpy"><img src="https://oliz.io/ggpy/static/gg.png" class="avatar" /></a>
</header>
<section>
<div>
<div class="card"><small class="social">2020-02-01</small><a href="https://example.com/blog"><b>Blog</b></a></div>
<div class="card"><small class="social">2020-01-31</small><a href="https://example.com/"><b>Root</b></a></div>
</div>
</section>
<footer>
<a href="#" class="nav">top</a>
<a href="javascript:toggleTheme()" class="nav">🌓</a>
<a href="javascript:toggleFontSize()" class="nav">aA</a>
<a href="https://oliz.io/about.html" class="social">about</a>
<a href="https://github.com/ooz/ggpy" class="social">github</a>
<a href="https://nitter.net/" class="social">twitter</a>
<a href="mailto:example@example.com" class="social">email</a>
</footer>
</body>
</html>
'''

def test_template_page_with_custom_title() -> None:
    index = {}
    index['title'] = 'Blog'
    index['html_headline'] = '<h1>Blog</h1>'
    index['html_section'] = gg.posts_index(given_posts())
    rendered_index = gg.template_page(index, config)
    assert '<title>Blog | Good Generator.py</title>' in rendered_index
    assert '<h1>Blog</h1>' in rendered_index

def test_template_sitemap() -> None:
    posts = given_posts()
    sitemap = gg.template_sitemap(posts)
    assert sitemap == \
'''<?xml version="1.0" encoding="utf-8" standalone="yes" ?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://example.com/</loc>
    <lastmod>2020-02-20</lastmod>
  </url>
  <url>
    <loc>https://example.com/blog</loc>
    <lastmod>2020-02-21</lastmod>
  </url>
</urlset>
'''

def test_template_sitemap_with_additional_entries() -> None:
    posts = given_posts()
    config = {
        'site': {
            'additional_sitemap_entries': ['https://example.com/hallo']
        }
    }
    sitemap = gg.template_sitemap(posts, config)
    assert sitemap == \
'''<?xml version="1.0" encoding="utf-8" standalone="yes" ?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://example.com/</loc>
    <lastmod>2020-02-20</lastmod>
  </url>
  <url>
    <loc>https://example.com/blog</loc>
    <lastmod>2020-02-21</lastmod>
  </url>
  <url>
    <loc>https://example.com/hallo</loc>
  </url>
</urlset>
'''

def test_template_rss() -> None:
    posts = given_posts()
    rss = gg.template_rss(posts)
    assert rss.startswith('''<?xml version="1.0" encoding="utf-8" standalone="yes"?>
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">
  <channel>
    <title></title>
    <link></link>
    <description></description>
    <generator>Good Generator.py -- ggpy -- https://oliz.io/ggpy</generator>
    <lastBuildDate>''')
    assert rss.endswith('''</lastBuildDate>
    <atom:link href="rss.xml" rel="self" type="application/rss+xml" />
    <item>
      <title>Root</title>
      <link>https://example.com/</link>
      <pubDate>Fri, 31 Jan 2020 00:00:00 -0000</pubDate>
      <guid>https://example.com/</guid>
      <description></description>
    </item>
    <item>
      <title>Blog</title>
      <link>https://example.com/blog</link>
      <pubDate>Sat, 01 Feb 2020 00:00:00 -0000</pubDate>
      <guid>https://example.com/blog</guid>
      <description></description>
    </item>
  </channel>
</rss>
''')

def given_posts() -> List[dict]:
    return [
        {
            'url': 'https://example.com/',
            'title': 'Root',
            'date': '2020-01-31',
            'last_modified': '2020-02-20',
            'tags': []
        },
        {
            'url': 'https://example.com/blog',
            'title': 'Blog',
            'date': '2020-02-01',
            'last_modified': '2020-02-21',
            'tags': []
        }
    ]
