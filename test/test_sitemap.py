#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

def test_sitemap_generation():
    sitemap_data = readfile('sitemap.xml')
    assert re.match(r'''<\?xml version="1.0" encoding="utf-8" standalone="yes" \?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://ooz.github.io/ggpy/</loc>
    <lastmod>[\d\-]{10}</lastmod>
  </url>
  <url>
    <loc>https://ooz.github.io/ggpy/test/about/</loc>
    <lastmod>[\d\-]{10}</lastmod>
  </url>
  <url>
    <loc>https://ooz.github.io/ggpy/test/features/</loc>
    <lastmod>[\d\-]{10}</lastmod>
  </url>
  <url>
    <loc>https://ooz.github.io/ggpy/test/some-post.html</loc>
    <lastmod>[\d\-]{10}</lastmod>
  </url>
</urlset>
''', sitemap_data)

def test_sitemap_does_not_include_drafts():
    sitemap_data = readfile('sitemap.xml')
    assert 'draft-not-included-in-sitemap' not in sitemap_data

def readfile(path):
    with open(path, 'r') as f:
        return f.read()
