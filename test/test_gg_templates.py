#!/usr/bin/env python
# -*- coding: utf-8 -*-

import gg

def test_post_template():
    return f"""
    canonical_url = 'https://ooz.github.io/ggpy/'
    body = '<h1>Hey!</h1>'
    post = gg.post_template(canonical_url, body, None, False)
    assert post == \
'''
'''
"""

def test_sitemap():
    posts = [
        {
            'url': 'https://example.com/',
            'last_modified': '2020-02-20'
        },
        {
            'url': 'https://example.com/blog',
            'last_modified': '2020-02-21'
        }
    ]
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