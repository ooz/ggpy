#!/usr/bin/env python
# -*- coding: utf-8 -*-

def test_readme_conversion():
    with open('test/index.html', 'r') as index:
        index_data = index.read()
        assert index_data == """<!DOCTYPE html>
  <head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
    <meta name="viewport" content="width=device-width,initial-scale=1">
    <title>Good Generator.py</title>
    <link rel="canonical" href="https://ooz.github.io/ggpy/test/">

<meta name="author" content="ooz" />
<meta name="description" content="" />
<meta name="keywords" content="" />

<meta name="twitter:author" content="@oozgo" />
<meta name="twitter:card" content="" />
<meta name="twitter:creator" content="@oozgo" />

<meta property="og:title" content="" />
<meta property="og:type" content="article" />
<meta property="og:url" content="https://ooz.github.io/ggpy/test/" />
<meta property="og:description" content="" />
<meta property="og:image" content="https://ooz.github.io/ggpy/static/gg.png" />
<meta property="og:locale" content="en-US" />
<meta property="article:published_time" content="" />

  <link rel="shortcut icon" href="https://ooz.github.io/ggpy/static/gg.png">
  <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto+Slab"> <!-- Vollkorn works, too -->
  <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=PT+Sans">
  <link rel="stylesheet" href="https://cdn.rawgit.com/necolas/normalize.css/master/normalize.css">
  <link rel="stylesheet" href="https://cdn.rawgit.com/milligram/milligram/master/dist/milligram.min.css">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/9.11.0/styles/default.min.css" type="text/css">
  <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.0.8/css/regular.css" integrity="sha384-A/oR8MwZKeyJS+Y0tLZ16QIyje/AmPduwrvjeH6NLiLsp4cdE4uRJl8zobWXBm4u" crossorigin="anonymous">
  <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.0.8/css/brands.css" integrity="sha384-IiIL1/ODJBRTrDTFk/pW8j0DUI5/z9m1KYsTm/RjZTNV8RHLGZXkUDwgRRbbQ+Jh" crossorigin="anonymous">
  <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.0.8/css/fontawesome.css" integrity="sha384-q3jl8XQu1OpdLgGFvNRnPdj5VIlCvgsDQTQB6owSOHWlAurxul7f+JpUOVdAiJ5P" crossorigin="anonymous">
  <link rel="stylesheet" href="https://ooz.github.io/ggpy/static/ooz_blog.css">
  </head>
  <body class="milligram container">
  <div style="text-align:center">
    <a href="https://ooz.github.io"><img src="https://ooz.github.io/ggpy/static/gg.png" class="avatar" /></a>
  </div>
  <div>
<h1 id="_1"></h1>
<small style="float:right;"></small>
</div>

  <div style="padding-top:2.5rem;">
  <h1 id="test-readme">Test README</h1>
<p>Lots of stuff</p>
<ul>
<li>A</li>
<li>2</li>
<li>and more</li>
</ul>
<h2 id="headline">Headline</h2>
<p>More text!</p>
<p>See <a href="another-post.html">other post</a>, too!</p>
  </div>
  <div>
  <a href="https://ooz.github.io/ggpy" style="float:left;"><strong style="font-size:2.5rem">⬅</strong></a>
<a href="#" style="float:left;"><strong style="font-size:2.5rem">⬆</strong></a>

    <a href="https://github.com/ooz" class="social-icon"><i class="fab fa-github"></i></a>
    <a href="https://twitter.com/oozgo" class="social-icon"><i class="fab fa-twitter"></i></a>
    <a href="mailto:oliverzeit@gmail.com" class="social-icon"><i class="far fa-envelope"></i></a></li>
    <!--
        <li style=""><a href="#">rss</a></li>
    -->
  </div>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/9.11.0/highlight.min.js"></script>
  <script type="text/javascript">hljs.initHighlightingOnLoad();</script>
  </body>
</html>
"""

def test_post_conversion():
    with open('test/another-post.html', 'r') as post:
        post_data = post.read()
        assert post_data == """<!DOCTYPE html>
  <head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
    <meta name="viewport" content="width=device-width,initial-scale=1">
    <title>Another Post | Good Generator.py</title>
    <link rel="canonical" href="https://ooz.github.io/ggpy/test/another-post.html">

<meta name="author" content="ooz" />
<meta name="description" content="Nice post!" />
<meta name="keywords" content="" />

<meta name="twitter:author" content="@oozgo" />
<meta name="twitter:card" content="Nice post!" />
<meta name="twitter:creator" content="@oozgo" />

<meta property="og:title" content="Another Post" />
<meta property="og:type" content="article" />
<meta property="og:url" content="https://ooz.github.io/ggpy/test/another-post.html" />
<meta property="og:description" content="Nice post!" />
<meta property="og:image" content="https://ooz.github.io/ggpy/static/gg.png" />
<meta property="og:locale" content="en-US" />
<meta property="article:published_time" content="2018-03-17T13:37:42Z" />

  <link rel="shortcut icon" href="https://ooz.github.io/ggpy/static/gg.png">
  <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto+Slab"> <!-- Vollkorn works, too -->
  <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=PT+Sans">
  <link rel="stylesheet" href="https://cdn.rawgit.com/necolas/normalize.css/master/normalize.css">
  <link rel="stylesheet" href="https://cdn.rawgit.com/milligram/milligram/master/dist/milligram.min.css">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/9.11.0/styles/default.min.css" type="text/css">
  <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.0.8/css/regular.css" integrity="sha384-A/oR8MwZKeyJS+Y0tLZ16QIyje/AmPduwrvjeH6NLiLsp4cdE4uRJl8zobWXBm4u" crossorigin="anonymous">
  <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.0.8/css/brands.css" integrity="sha384-IiIL1/ODJBRTrDTFk/pW8j0DUI5/z9m1KYsTm/RjZTNV8RHLGZXkUDwgRRbbQ+Jh" crossorigin="anonymous">
  <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.0.8/css/fontawesome.css" integrity="sha384-q3jl8XQu1OpdLgGFvNRnPdj5VIlCvgsDQTQB6owSOHWlAurxul7f+JpUOVdAiJ5P" crossorigin="anonymous">
  <link rel="stylesheet" href="https://ooz.github.io/ggpy/static/ooz_blog.css">
  </head>
  <body class="milligram container">
  <div style="text-align:center">
    <a href="https://ooz.github.io"><img src="https://ooz.github.io/ggpy/static/gg.png" class="avatar" /></a>
  </div>
  <div>
<h1 id="another-post">Another Post</h1>
<small style="float:right;">2018-03-17</small>
</div>

  <div style="padding-top:2.5rem;">
  <p>Yep! Intro text!</p>
<h2 id="headline">Headline</h2>
<p>More text!</p>
  </div>
  <div>
  <a href="https://ooz.github.io/ggpy" style="float:left;"><strong style="font-size:2.5rem">⬅</strong></a>
<a href="#" style="float:left;"><strong style="font-size:2.5rem">⬆</strong></a>

    <a href="https://github.com/ooz" class="social-icon"><i class="fab fa-github"></i></a>
    <a href="https://twitter.com/oozgo" class="social-icon"><i class="fab fa-twitter"></i></a>
    <a href="mailto:oliverzeit@gmail.com" class="social-icon"><i class="far fa-envelope"></i></a></li>
    <!--
        <li style=""><a href="#">rss</a></li>
    -->
  </div>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/9.11.0/highlight.min.js"></script>
  <script type="text/javascript">hljs.initHighlightingOnLoad();</script>
  </body>
</html>
"""
