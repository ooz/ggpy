#!/usr/bin/env python
# -*- coding: utf-8 -*-

def test_sitemap_generation():
    with open('sitemap.xml') as sitemap:
        sitemap_data = sitemap.read()
        assert sitemap_data == '''<?xml version="1.0" encoding="utf-8" standalone="yes" ?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://ooz.github.io/ggpy/</loc>
  </url>
  <url>
    <loc>https://ooz.github.io/ggpy/test/about/</loc>
  </url>
  <url>
    <loc>https://ooz.github.io/ggpy/test/features/</loc>
  </url>
  <url>
    <loc>https://ooz.github.io/ggpy/test/some-post.html</loc>
  </url>
</urlset>
'''