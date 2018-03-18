#!/usr/bin/env python
# -*- coding: utf-8 -*-

import glob
from html import escape
import os
import sys
import markdown

import ggconfig as gg

MD = markdown.Markdown(
        extensions = [
            'markdown.extensions.extra',
            'markdown.extensions.headerid',
            'markdown.extensions.meta',
            'markdown.extensions.sane_lists',
            'markdown.extensions.tables',
            'pymdownx.magiclink',
            'pymdownx.betterem',
            'pymdownx.tilde',
            'pymdownx.emoji',
            'pymdownx.tasklist',
            'pymdownx.superfences'
        ]
    )

def render_template(title, canonical_url, description, tags, date, body, root=False):
    base_url = gg.config.get('site', {}).get('base_url', '')
    logo_url = base_url + '/' + gg.config.get('site', {}).get('logo', '')
    style_url = base_url + '/' + gg.config.get('site', {}).get('style', '')
    author_name = gg.config.get('author', {}).get('name', '')
    author_url = gg.config.get('author', {}).get('url', '')
    return """<!DOCTYPE html>
  <head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
    <meta name="viewport" content="width=device-width,initial-scale=1">
    <title>%s</title>
    <link rel="canonical" href="%s">

%s
%s
%s
  <link rel="shortcut icon" href="%s">
%s
  <link rel="stylesheet" href="%s">
  </head>
  <body class="milligram container">
  <div style="text-align:center">
    <a href="%s"><img src="%s" class="avatar" /></a>
  </div>
  %s
  <div style="padding-top:2.5rem;">
  %s
  </div>
  <div>
  %s
%s
  </div>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/9.11.0/highlight.min.js"></script>
  <script type="text/javascript">hljs.initHighlightingOnLoad();</script>
  </body>
</html>
""" % (convert_title2pagetitle(title),
canonical_url,
meta(author_name, description, tags),
twitter(gg.config.get('social', {}).get('twitter_username', '')),
opengraph(title, canonical_url, description, date),
logo_url,
external_stylesheets(True),
style_url,
author_url,
logo_url,
post_header(title, date),
body,
'' if root else render_footer_navigation(base_url),
render_social_icons(),
)

def render_social_icons():
    github = gg.config.get('social', {}).get('github_url', ''),
    twitter = gg.config.get('social', {}).get('twitter_url', ''),
    email = gg.config.get('author', {}).get('email', '')
    icons = []
    if len(github):
        icons.append('<a href="%s" class="social-icon"><i class="fab fa-github"></i></a>' % github)
    if len(twitter):
        icons.append('<a href="%s" class="social-icon"><i class="fab fa-twitter"></i></a>' % twitter)
    if len(email):
        icons.append('<a href="mailto:%s" class="social-icon"><i class="far fa-envelope"></i></a>' % email)
    return '\n'.join(icons)

def render_footer_navigation(root_url):
    return """<a href="%s" style="float:left;"><strong style="font-size:2.5rem">⬅</strong></a>
<a href="#" style="float:left;"><strong style="font-size:2.5rem">⬆</strong></a>
""" % root_url

def meta(author, description, tags):
    return """<meta name="author" content="%s" />
<meta name="description" content="%s" />
<meta name="keywords" content="%s" />
""" % (author,
description,
tags
)

def twitter(twitter_username):
    return """<meta name="twitter:author" content="%s" />
<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:creator" content="%s" />
""" % (twitter_username,
twitter_username
)

# URL should end with "/" for a directory!
def opengraph(title, url, description, date,
              image=gg.config.get('site', {}).get('base_url', '') + '/' + gg.config.get('site', {}).get('logo', '')):
    return """<meta property="og:title" content="%s" />
<meta property="og:type" content="article" />
<meta property="og:url" content="%s" />
<meta property="og:description" content="%s" />
<meta property="og:image" content="%s" />
<meta property="og:locale" content="en-US" />
<meta property="article:published_time" content="%s" />
""" % (title,
url,
description,
image,
date
)

def post_header(title, date):
    return """<div>
%s
<small style="float:right;">%s</small>
</div>
""" % (MD.reset().convert('# ' + title),
date[:10]
)

def external_stylesheets(highlightjs=False):
    return """<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto+Slab"> <!-- Vollkorn works, too -->
<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=PT+Sans">
<link rel="stylesheet" href="https://cdn.rawgit.com/necolas/normalize.css/master/normalize.css">
<link rel="stylesheet" href="https://cdn.rawgit.com/milligram/milligram/master/dist/milligram.min.css">
<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.0.8/css/all.css" integrity="sha384-3AB7yXWz4OeoZcPbieVW64vVXEwADiYyAEhwilzWsLw+9FgqpyjjStpPnpBO8o8S" crossorigin="anonymous">
%s
""" % ('<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/9.11.0/styles/default.min.css" type="text/css">' if highlightjs else '')

def convert(directory, filepath, root=False):
    with open(filepath, 'r') as infile:
        markdown_post = infile.read()
        html_post = MD.reset().convert(markdown_post)
        targetpath = convert_path(filepath)
        with open(targetpath, 'w') as outfile:
            canonical_url = convert_canonical(directory, targetpath)
            date = convert_meta(MD, 'date')
            tags = convert_meta(MD, 'tags')
            title = convert_meta(MD, 'title')
            html = render_template(title,
                canonical_url,
                convert_meta(MD, 'description', default=title),
                tags,
                date,
                html_post,
                root
            )
            outfile.write(html)
            return {
                'date': date,
                'url': canonical_url,
                'title': title,
                'tags': tags
            }

def convert_meta(md, field, default=''):
    field_value = MD.Meta.get(field, '')
    if len(field_value) > 0:
        return escape(', '.join(field_value))
    return default

def convert_path(filepath):
    targetpath = filepath[:-3]
    if targetpath.endswith('README'):
        targetpath = targetpath[:-6] + 'index'
    targetpath += '.html'
    return targetpath

def convert_canonical(directory, targetpath):
    base_url = gg.config.get('site', {}).get('base_url', '')
    targetpath = os.path.relpath(targetpath, directory)
    if targetpath.endswith('index.html'):
        return base_url + '/' + targetpath[:-10]
    return base_url + '/' + targetpath

def convert_title2pagetitle(title):
    root_title = gg.config.get('site', {}).get('title', '')
    if len(title) and title != root_title:
        return title + ' | ' + root_title
    return root_title

def make_index(posts):
    base_url = gg.config.get('site', {}).get('base_url', '')
    root_title = gg.config.get('site', {}).get('title', '')
    logo_url = base_url + '/' + gg.config.get('site', {}).get('logo', '')
    style_url = base_url + '/' + gg.config.get('site', {}).get('style', '')
    author_url = gg.config.get('author', {}).get('url', '')
    posts_html = []
    for post in reversed(sorted(posts, key=lambda post: post['date'])):
        day = post['date'][:10]
        title = post['title']
        url = post['url']
        if (day != '' and title != ''):
            posts_html.append('<tr><td>%s</td><td><a href="%s">%s</a></td></tr>' % (day, url, title))
    posts_html = "\n".join(posts_html)

    index_html = """<!DOCTYPE html>
  <head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
    <meta name="viewport" content="width=device-width,initial-scale=1">
    <title>%s</title>
    <link rel="canonical" href="%s">
  <link rel="shortcut icon" href="%s">
%s
  <link rel="stylesheet" href="%s">
  </head>
  <body class="milligram container">
  <div style="text-align:center">
    <a href="%s"><img src="%s" class="avatar" /></a>
  </div>
  %s
  <div style="padding-top:2.5rem;">
  %s
  </div>
  <div>
%s
  </div>
  </body>
</html>
""" % ("Blog Index | " + root_title,
base_url,
logo_url,
external_stylesheets(),
style_url,
author_url,
logo_url,
'<h1>Blog</h1>',
"""<table><tbody>
%s
</tbody></table>""" % posts_html,
render_social_icons()
)

    with open('index.html', 'w') as index_file:
        index_file.write(index_html)

def is_root_readme(path):
    return os.path.relpath(path) == 'README.md'

def main(directories):
    render_root_readme = gg.config.get('site', {}).get('render_root_readme', True)
    posts = []
    for directory in directories:
        paths = glob.glob(directory + '/**/*.md', recursive=True)
        for path in paths:
            root_readme = is_root_readme(path)
            if not root_readme or render_root_readme:
                posts.append(convert(directory, path, root=root_readme))

    if not render_root_readme:
        make_index(posts)

if __name__ == "__main__":
    main(sys.argv[1:])
