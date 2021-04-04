#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

import gg
from ggconfig import config

def test_newpost():
    assert re.match(r'''---
title: Title
description: -
date: \d+-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z
tags: __draft__
---
''', gg.template_newpost())

def test_template_post():
    post = {
        'url': 'https://oliz.io/ggpy/',
        'html_section': '<h1>Hey!</h1>'
    }
    post = gg.template_post(post, config)
    assert post == \
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
    font-size: 18px;
    font-family: sans-serif;
    line-height: 1.6;
    color: #363636;
    background: #FFF;
    margin: 1rem auto;
    padding: 0 10px;
    max-width: 700px;
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
    font-size: 80%;
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
pre { border-left: 0.3rem solid #07A; }
pre > code {
    font-size: 14px;
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
.dark-mode blockquote { background: #222; border-left: 0.3rem solid #0A7; }
.dark-mode code { background: #222; }
.dark-mode pre { border-left: 0.3rem solid #0A7; }

.avatar { border-radius: 50%; box-shadow: 0px 1px 2px rgba(0, 0, 0, 0.2); max-width: 3rem; }
.nav { float: left; margin-right: 1rem; }
.social { float: right; margin-left: 1rem; }
</style>
<script>
function toggleTheme() { document.body.classList.toggle("dark-mode") }
function initTheme() { let h=new Date().getHours(); if (h <= 8 || h >= 20) { toggleTheme() } }
</script>
<meta name="author" content="Good Gen">
<meta name="twitter:author" content="@oozgo">
<meta name="twitter:card" content="summary">
<meta name="twitter:creator" content="@oozgo">
<meta property="og:title" content="">
<meta property="og:type" content="article">
<meta property="og:url" content="https://oliz.io/ggpy/">
<meta property="og:description" content="">
<meta property="og:image" content="https://oliz.io/ggpy/static/gg.png">
<meta property="og:locale" content="en-US">
<script type="application/ld+json">
{"@context":"http://schema.org","@type":"WebSite","headline":"","url":"https://oliz.io/ggpy/","name":"Good Generator.py","description":""}</script>
</head>

<body onload="initTheme()">
<header>
<a href="https://oliz.io/ggpy"><img src="https://oliz.io/ggpy/static/gg.png" class="avatar" /></a>
</header>
<section>
<h1>Hey!</h1>
</section>
<footer>
<a href="https://oliz.io/ggpy" class="nav">back</a>
<a href="#" class="nav">top</a>
<a href="javascript:toggleTheme()" class="nav">🌓</a>
<a href="mailto:example@example.com" class="social">email</a>
<a href="https://twitter.com/oozgo" class="social">twitter</a>
<a href="https://github.com/ooz/ggpy" class="social">github</a>
<a href="https://oliz.io/ggpy/test/about" class="social">about</a>
</footer>
</body>
</html>
'''

def test_template_post_without_config():
    post = {
        'url': 'index.html',
        'is_root_index': True,
        'html_section': '<h1>Hey!</h1>'
    }
    post = gg.template_post(post)
    assert post == \
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
    font-size: 18px;
    font-family: sans-serif;
    line-height: 1.6;
    color: #363636;
    background: #FFF;
    margin: 1rem auto;
    padding: 0 10px;
    max-width: 700px;
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
    font-size: 80%;
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
pre { border-left: 0.3rem solid #07A; }
pre > code {
    font-size: 14px;
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
.dark-mode blockquote { background: #222; border-left: 0.3rem solid #0A7; }
.dark-mode code { background: #222; }
.dark-mode pre { border-left: 0.3rem solid #0A7; }

.avatar { border-radius: 50%; box-shadow: 0px 1px 2px rgba(0, 0, 0, 0.2); max-width: 3rem; }
.nav { float: left; margin-right: 1rem; }
.social { float: right; margin-left: 1rem; }
</style>
<script>
function toggleTheme() { document.body.classList.toggle("dark-mode") }
function initTheme() { let h=new Date().getHours(); if (h <= 8 || h >= 20) { toggleTheme() } }
</script>


<meta property="og:title" content="">
<meta property="og:type" content="article">
<meta property="og:url" content="index.html">
<meta property="og:description" content="">
<meta property="og:locale" content="en-US">
<script type="application/ld+json">
{"@context":"http://schema.org","@type":"WebSite","headline":"","url":"index.html","description":""}</script>
</head>

<body onload="initTheme()">
<header>

</header>
<section>
<h1>Hey!</h1>
</section>
<footer>
<a href="#" class="nav">top</a>
<a href="javascript:toggleTheme()" class="nav">🌓</a>
</footer>
</body>
</html>
'''

def test_template_index():
    posts = given_posts()
    index = gg.template_index({}, posts, config)
    assert index == \
'''<!DOCTYPE html>
<html lang="en-US">
<head>
<meta charset="UTF-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta http-equiv="Content-Security-Policy" content="script-src 'unsafe-inline'">
<meta name="referrer" content="no-referrer">
<title>Index | Good Generator.py</title>
<link rel="canonical" href="https://oliz.io/ggpy">
<link rel="shortcut icon" href="https://oliz.io/ggpy/static/gg.png">
<style>
body {
    font-size: 18px;
    font-family: sans-serif;
    line-height: 1.6;
    color: #363636;
    background: #FFF;
    margin: 1rem auto;
    padding: 0 10px;
    max-width: 700px;
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
    font-size: 80%;
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
pre { border-left: 0.3rem solid #07A; }
pre > code {
    font-size: 14px;
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
.dark-mode blockquote { background: #222; border-left: 0.3rem solid #0A7; }
.dark-mode code { background: #222; }
.dark-mode pre { border-left: 0.3rem solid #0A7; }

.avatar { border-radius: 50%; box-shadow: 0px 1px 2px rgba(0, 0, 0, 0.2); max-width: 3rem; }
.nav { float: left; margin-right: 1rem; }
.social { float: right; margin-left: 1rem; }
</style>
<script>
function toggleTheme() { document.body.classList.toggle("dark-mode") }
function initTheme() { let h=new Date().getHours(); if (h <= 8 || h >= 20) { toggleTheme() } }
</script>
</head>

<body onload="initTheme()">
<header>
<a href="https://oliz.io/ggpy"><img src="https://oliz.io/ggpy/static/gg.png" class="avatar" /></a>
<h1>Index</h1>
</header>
<section>
<table>
<tbody>
<tr><td>2020-02-01</td><td><a href="https://example.com/blog">Blog</a></td></tr>
<tr><td>2020-01-31</td><td><a href="https://example.com/">Root</a></td></tr>
</tbody>
</table>
</section>
<footer>
<a href="#" class="nav">top</a>
<a href="javascript:toggleTheme()" class="nav">🌓</a>
<a href="mailto:example@example.com" class="social">email</a>
<a href="https://twitter.com/oozgo" class="social">twitter</a>
<a href="https://github.com/ooz/ggpy" class="social">github</a>
<a href="https://oliz.io/ggpy/test/about" class="social">about</a>
</footer>
</body>
</html>
'''

def test_template_index_with_custom_title():
    posts = given_posts()
    index = gg.template_index({'title': 'Blog'}, posts, config)
    assert '<title>Blog | Good Generator.py</title>' in index
    assert '<h1>Blog</h1>' in index

def test_template_sitemap():
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

def test_template_sitemap_with_additional_entries():
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

def given_posts():
    return [
        {
            'url': 'https://example.com/',
            'title': 'Root',
            'date': '2020-01-31',
            'last_modified': '2020-02-20'
        },
        {
            'url': 'https://example.com/blog',
            'title': 'Blog',
            'date': '2020-02-01',
            'last_modified': '2020-02-21'
        }
    ]
