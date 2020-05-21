#!/usr/bin/env python
# -*- coding: utf-8 -*-

import gg

def test_post_template():
    canonical_url = 'https://ooz.github.io/ggpy/'
    body = '<h1>Hey!</h1>'
    markdown = gg.configure_markdown()
    post = gg.post_template(canonical_url, body, markdown, False)
    assert post == \
'''<!DOCTYPE html>
<html lang="en-US">
<head>
<meta charset="UTF-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
<meta name="viewport" content="width=device-width,initial-scale=1">

<title>Good Generator.py</title>
<link rel="canonical" href="https://ooz.github.io/ggpy/">
<link rel="shortcut icon" href="https://ooz.github.io/ggpy/static/gg.png">

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
}
.avatar { border-radius: 50%; box-shadow: 0px 1px 2px rgba(0, 0, 0, 0.2); max-width: 3rem; }
.nav { float: left; margin-right: 1rem; }
.social { float: right; margin-left: 1rem; }

.dark-mode { color: #FFF; background: #363636; }
.dark-mode a { color: #0A7; }
.dark-mode blockquote { background: #222; border-left: 0.3rem solid #0A7; }
.dark-mode code { background: #222; }
.dark-mode pre { border-left: 0.3rem solid #0A7; }
</style>
<script>
function toggleTheme() { document.body.classList.toggle("dark-mode") }
function initTheme() { let h=new Date().getHours(); if (h <= 8 || h >= 20) { toggleTheme() } }
</script>

<meta name="author" content="Good Gen" />
<meta name="description" content="" />
<meta name="keywords" content="" />
<meta name="twitter:author" content="@oozgo" />
<meta name="twitter:card" content="summary" />
<meta name="twitter:creator" content="@oozgo" />
<meta property="og:title" content="" />
<meta property="og:type" content="article" />
<meta property="og:url" content="https://ooz.github.io/ggpy/" />
<meta property="og:description" content="" />
<meta property="og:image" content="https://ooz.github.io/ggpy/static/gg.png" />
<meta property="og:locale" content="en-US" />
<meta property="article:published_time" content="" />
<script type="application/ld+json">
{"@context":"http://schema.org","@type":"WebSite","headline":"","url":"https://ooz.github.io/ggpy/","name":"Good Generator.py","description":""}</script>
</head>

<body onload="initTheme()">
<header>
<a href="https://ooz.github.io/ggpy"><img src="https://ooz.github.io/ggpy/static/gg.png" class="avatar" /></a>

</header>
<section>
<h1>Hey!</h1>
</section>
<footer>
<a href="https://ooz.github.io/ggpy" class="nav">back</a>
<a href="#" class="nav">top</a>
<a href="javascript:toggleTheme()" class="nav">🌚🌞</a>
<a href="mailto:example@example.com" class="social">email</a>
<a href="https://twitter.com/oozgo" class="social">twitter</a>
<a href="https://github.com/ooz/ggpy" class="social">github</a>
<a href="https://ooz.github.io/ggpy/test/about" class="social">about</a>
</footer>
</body>
</html>
'''

def test_index():
    posts = given_posts()
    index = gg.index(posts)
    assert index == \
'''<!DOCTYPE html>
<html lang="en-US">
<head>
<meta charset="UTF-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
<meta name="viewport" content="width=device-width,initial-scale=1">

<title>Index | Good Generator.py</title>
<link rel="canonical" href="https://ooz.github.io/ggpy">
<link rel="shortcut icon" href="https://ooz.github.io/ggpy/static/gg.png">

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
}
.avatar { border-radius: 50%; box-shadow: 0px 1px 2px rgba(0, 0, 0, 0.2); max-width: 3rem; }
.nav { float: left; margin-right: 1rem; }
.social { float: right; margin-left: 1rem; }

.dark-mode { color: #FFF; background: #363636; }
.dark-mode a { color: #0A7; }
.dark-mode blockquote { background: #222; border-left: 0.3rem solid #0A7; }
.dark-mode code { background: #222; }
.dark-mode pre { border-left: 0.3rem solid #0A7; }
</style>
<script>
function toggleTheme() { document.body.classList.toggle("dark-mode") }
function initTheme() { let h=new Date().getHours(); if (h <= 8 || h >= 20) { toggleTheme() } }
</script>

</head>

<body onload="initTheme()">
<header>
<a href="https://ooz.github.io/ggpy"><img src="https://ooz.github.io/ggpy/static/gg.png" class="avatar" /></a>
<h1>Index</h1>
</header>
<section>
<table><tbody>
<tr><td>2020-02-01</td><td><a href="https://example.com/blog">Blog</a></td></tr>
<tr><td>2020-01-31</td><td><a href="https://example.com/">Root</a></td></tr>
</tbody></table>
</section>
<footer>
<a href="#" class="nav">top</a>
<a href="javascript:toggleTheme()" class="nav">🌚🌞</a>
<a href="mailto:example@example.com" class="social">email</a>
<a href="https://twitter.com/oozgo" class="social">twitter</a>
<a href="https://github.com/ooz/ggpy" class="social">github</a>
<a href="https://ooz.github.io/ggpy/test/about" class="social">about</a>
</footer>
</body>
</html>
'''

def test_sitemap():
    posts = given_posts()
    sitemap = gg.sitemap(posts)
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