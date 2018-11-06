#!/usr/bin/env python
# -*- coding: utf-8 -*-

SITE_TITLE = 'Good Generator.py'
LOGO_URL = 'https://ooz.github.io/ggpy/static/gg.png'
GENERATED_FEATURE_HTML = \
f'''<div style="text-align:center">
<a href="https://ooz.github.io/ggpy"><img src="{LOGO_URL}" class="avatar" /></a>
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
'''
GENERATED_POST_HTML = \
f'''<div style="text-align:center">
<a href="https://ooz.github.io/ggpy"><img src="{LOGO_URL}" class="avatar" /></a>
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
'''

def test_markdown_features_and_readme_generation():
    # given & when
    index_title = 'Markdown Feature Test'
    canonical_url = 'https://ooz.github.io/ggpy/test/features/'
    index_data = readfile('test/features/index.html')

    # then
    index_data = then_is_framed_by_html_boilerplate(index_data)
    index_data = then_has_bottom_navigation_and_social_links(index_data)
    index_data = then_has_title_canonical_and_favicon(
        index_data,
        title=f'{index_title} | {SITE_TITLE}',
        canonical_url=canonical_url,
        favicon_url=LOGO_URL
    )
    index_data = then_has_stylesheets(index_data)
    index_data = then_head_ends_with_meta_tags(
        index_data,
        title=index_title,
        description='Description',
        canonical_url=canonical_url,
        creation_time='1337-06-06T13:37:42+01:00'
    )
    index_data = then_has_body(index_data)
    assert GENERATED_FEATURE_HTML == index_data

def test_post_conversion():
    # given & when
    post_title = 'Some Post'
    canonical_url = 'https://ooz.github.io/ggpy/test/some-post.html'
    post_data = readfile('test/some-post.html')

    # then
    post_data = then_is_framed_by_html_boilerplate(post_data)
    post_data = then_has_bottom_navigation_and_social_links(post_data)
    post_data = then_has_title_canonical_and_favicon(
        post_data,
        title=f'{post_title} | {SITE_TITLE}',
        canonical_url=canonical_url,
        favicon_url=LOGO_URL
    )
    post_data = then_has_stylesheets(post_data)
    post_data = then_head_ends_with_meta_tags(
        post_data,
        title=post_title,
        description='Nice post!',
        canonical_url=canonical_url,
        creation_time='2018-03-17T13:37:42Z'
    )
    post_data = then_has_body(post_data)
    assert GENERATED_POST_HTML == post_data

def then_is_framed_by_html_boilerplate(result):
    html_start = \
'''<!DOCTYPE html>
<head>
<meta charset="UTF-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
<meta name="viewport" content="width=device-width,initial-scale=1">

'''
    html_end = \
'''<script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/9.11.0/highlight.min.js"></script>
<script type="text/javascript">hljs.initHighlightingOnLoad();</script>
</body>
</html>
'''
    assert result.startswith(html_start)
    assert result.endswith(html_end)
    return result.replace(html_start, '').replace(html_end, '')

def then_has_bottom_navigation_and_social_links(result):
    navigation_and_social_links = \
'''<div>
<a href="https://ooz.github.io/ggpy" class="nav-arrow">🔙</a>
<a href="#" class="nav-arrow">🔝</a>
<a href="https://twitter.com/oozgo" class="social-icon">twitter</a>
<a href="https://github.com/ooz/ggpy" class="social-icon">github</a>
<a href="https://ooz.github.io/ggpy/test/about" class="social-icon">about</a>
</div>
'''
    assert result.endswith(navigation_and_social_links)
    return result.replace(navigation_and_social_links, '')

def then_has_title_canonical_and_favicon(result, title='', canonical_url='', favicon_url=''):
    title_and_links = \
f'''<title>{title}</title>
<link rel="canonical" href="{canonical_url}">
<link rel="shortcut icon" href="{favicon_url}">

'''
    assert result.startswith(title_and_links)
    return result.replace(title_and_links, '')

def then_has_stylesheets(result):
    stylesheets = \
'''<link rel="stylesheet" href="https://cdn.rawgit.com/necolas/normalize.css/master/normalize.css">
<link rel="stylesheet" href="https://cdn.rawgit.com/milligram/milligram/master/dist/milligram.min.css">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/9.11.0/styles/default.min.css">
<link rel="stylesheet" href="https://ooz.github.io/ggpy/static/ooz_blog.css">

'''
    assert result.startswith(stylesheets)
    return result.replace(stylesheets, '')

def then_head_ends_with_meta_tags(result, title='', description='', canonical_url='', creation_time=''):
    meta = \
f'''<meta name="author" content="Good Gen" />
<meta name="description" content="{description}" />
<meta name="keywords" content="" />
<meta name="twitter:author" content="@oozgo" />
<meta name="twitter:card" content="summary" />
<meta name="twitter:creator" content="@oozgo" />
<meta property="og:title" content="{title}" />
<meta property="og:type" content="article" />
<meta property="og:url" content="{canonical_url}" />
<meta property="og:description" content="{description}" />
<meta property="og:image" content="{LOGO_URL}" />
<meta property="og:locale" content="en-US" />
<meta property="article:published_time" content="{creation_time}" />
</head>

'''
    assert result.startswith(meta)
    return result.replace(meta, '')

def then_has_body(result):
    body = \
'''<body class="container">
'''
    assert result.startswith(body)
    return result.replace(body, '')

def readfile(path):
    with open(path, 'r') as f:
        return f.read()
