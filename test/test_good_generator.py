#!/usr/bin/env python
# -*- coding: utf-8 -*-

def test_markdown_features_and_readme_generation():
    with open('test/features/index.html') as index:
        index_data = index.read()
        assert index_data == """<!DOCTYPE html>
<head>
<meta charset="UTF-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
<meta name="viewport" content="width=device-width,initial-scale=1">

<title>Markdown Feature Test | Good Generator.py</title>
<link rel="canonical" href="https://ooz.github.io/ggpy/test/features/">
<link rel="shortcut icon" href="https://ooz.github.io/ggpy/static/gg.png">

<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto+Slab"> <!-- Vollkorn works, too -->
<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=PT+Sans">
<link rel="stylesheet" href="https://cdn.rawgit.com/necolas/normalize.css/master/normalize.css">
<link rel="stylesheet" href="https://cdn.rawgit.com/milligram/milligram/master/dist/milligram.min.css">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/9.11.0/styles/default.min.css" type="text/css">
<link rel="stylesheet" href="https://ooz.github.io/ggpy/static/ooz_blog.css">

<meta name="author" content="Good Gen" />
<meta name="description" content="Description" />
<meta name="keywords" content="" />

<meta name="twitter:author" content="@oozgo" />
<meta name="twitter:card" content="summary" />
<meta name="twitter:creator" content="@oozgo" />

<meta property="og:title" content="Markdown Feature Test" />
<meta property="og:type" content="article" />
<meta property="og:url" content="https://ooz.github.io/ggpy/test/features/" />
<meta property="og:description" content="Description" />
<meta property="og:image" content="https://ooz.github.io/ggpy/static/gg.png" />
<meta property="og:locale" content="en-US" />
<meta property="article:published_time" content="1337-06-06T13:37:42+01:00" />
</head>

<body class="milligram container">
<div style="text-align:center">
<a href="https://ooz.github.io/ggpy"><img src="https://ooz.github.io/ggpy/static/gg.png" class="avatar" /></a>
</div>
<div>
<h1 id="markdown-feature-test">Markdown Feature Test</h1>
<small style="float:right;"><a href="https://ooz.github.io/ggpy">Good Gen</a>, 1337-06-06</small>
</div>

<div style="padding-top:2.5rem;">
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
<ul class="task-list">
<li><del>Unordered list item, DELETED!</del></li>
<li>
<p><code>Unordered list item, inline coded</code></p>
</li>
<li class="task-list-item">
<p><input type="checkbox" disabled/> unchecked</p>
</li>
<li class="task-list-item"><input type="checkbox" disabled checked/> checked</li>
</ul>
<h2 id="code">Code</h2>
<pre class="highlight"><code># Code blocks work</code></pre>

<pre class="highlight"><code class="language-python">def python_code_blocks():
    return &quot;work, too!&quot;</code></pre>

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
<th align="right">just</th>
<th>fine</th>
</tr>
</thead>
<tbody>
<tr>
<td>for</td>
<td>real</td>
<td align="right">yep</td>
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
<p><img alt="Good Generator Logo" src="https://ooz.github.io/ggpy/static/gg.png" /></p>
<p>Horizontal rule...</p>
<hr />
<h2 id="other-markdown-extensions">Other Markdown Extensions</h2>
<h3 id="definition-lists-and-footnotes">Definition Lists and Footnotes</h3>
<dl>
<dt>Definition List</dt>
<dd>is defined here<sup id="fnref:1"><a class="footnote-ref" href="#fn:1" rel="footnote">1</a></sup>.</dd>
<dt>Other List</dt>
<dd>is defined here<sup id="fnref:here"><a class="footnote-ref" href="#fn:here" rel="footnote">2</a></sup>.</dd>
</dl>
<h3 id="abbreviations">Abbreviations</h3>
<p><abbr title="Hyper Text Markup Language">HTML</abbr></p>
<h2 id="leftovers">Leftovers</h2>
<p>Yep, now the footnotes are arriving!</p>
<div class="footnote">
<hr />
<ol>
<li id="fn:1">
<p>Numbered footnote&#160;<a class="footnote-backref" href="#fnref:1" rev="footnote" title="Jump back to footnote 1 in the text">&#8617;</a></p>
</li>
<li id="fn:here">
<p>Labeled footnote&#160;<a class="footnote-backref" href="#fnref:here" rev="footnote" title="Jump back to footnote 2 in the text">&#8617;</a></p>
</li>
</ol>
</div>
</div>
<div>
<a href="https://ooz.github.io/ggpy" class="nav-arrow"><strong>⬅</strong></a>
<a href="#" class="nav-arrow"><strong>⬆</strong></a>

<a href="https://twitter.com/oozgo" class="social-icon">twitter</a>
<a href="https://github.com/ooz/ggpy" class="social-icon">github</a>
<a href="https://ooz.github.io/ggpy/test/about" class="social-icon">about</a>
</div>
<script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/9.11.0/highlight.min.js"></script>
<script type="text/javascript">hljs.initHighlightingOnLoad();</script>
</body>
</html>
"""

def test_post_conversion():
    with open('test/some-post.html', 'r') as post:
        post_data = post.read()
        assert post_data == \
"""<!DOCTYPE html>
<head>
<meta charset="UTF-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
<meta name="viewport" content="width=device-width,initial-scale=1">

<title>Some Post | Good Generator.py</title>
<link rel="canonical" href="https://ooz.github.io/ggpy/test/some-post.html">
<link rel="shortcut icon" href="https://ooz.github.io/ggpy/static/gg.png">

<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto+Slab"> <!-- Vollkorn works, too -->
<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=PT+Sans">
<link rel="stylesheet" href="https://cdn.rawgit.com/necolas/normalize.css/master/normalize.css">
<link rel="stylesheet" href="https://cdn.rawgit.com/milligram/milligram/master/dist/milligram.min.css">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/9.11.0/styles/default.min.css" type="text/css">
<link rel="stylesheet" href="https://ooz.github.io/ggpy/static/ooz_blog.css">

<meta name="author" content="Good Gen" />
<meta name="description" content="Nice post!" />
<meta name="keywords" content="" />

<meta name="twitter:author" content="@oozgo" />
<meta name="twitter:card" content="summary" />
<meta name="twitter:creator" content="@oozgo" />

<meta property="og:title" content="Some Post" />
<meta property="og:type" content="article" />
<meta property="og:url" content="https://ooz.github.io/ggpy/test/some-post.html" />
<meta property="og:description" content="Nice post!" />
<meta property="og:image" content="https://ooz.github.io/ggpy/static/gg.png" />
<meta property="og:locale" content="en-US" />
<meta property="article:published_time" content="2018-03-17T13:37:42Z" />
</head>

<body class="milligram container">
<div style="text-align:center">
<a href="https://ooz.github.io/ggpy"><img src="https://ooz.github.io/ggpy/static/gg.png" class="avatar" /></a>
</div>
<div>
<h1 id="some-post">Some Post</h1>
<small style="float:right;"><a href="https://ooz.github.io/ggpy">Good Gen</a>, 2018-03-17</small>
</div>

<div style="padding-top:2.5rem;">
<p>Yep! Intro text!</p>
<h2 id="headline">Headline</h2>
<p>More text!</p>
</div>
<div>
<a href="https://ooz.github.io/ggpy" class="nav-arrow"><strong>⬅</strong></a>
<a href="#" class="nav-arrow"><strong>⬆</strong></a>

<a href="https://twitter.com/oozgo" class="social-icon">twitter</a>
<a href="https://github.com/ooz/ggpy" class="social-icon">github</a>
<a href="https://ooz.github.io/ggpy/test/about" class="social-icon">about</a>
</div>
<script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/9.11.0/highlight.min.js"></script>
<script type="text/javascript">hljs.initHighlightingOnLoad();</script>
</body>
</html>
"""
