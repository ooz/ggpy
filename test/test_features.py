#!/usr/bin/env python
# -*- coding: utf-8 -*-

from gg import read_file

def test_omit_machine_readable_meta_when_no_meta_tag_is_set():
    rendered = read_file('test/features/no-meta.html')

    assert '<meta name="author"' not in rendered
    assert '<meta name="description"' not in rendered
    assert '<meta name="keywords"' not in rendered
    assert '<meta name="twitter:author"' not in rendered
    assert '<meta name="twitter:card"' not in rendered
    assert '<meta name="twitter:creator"' not in rendered
    assert '<meta property="og:title"' not in rendered
    assert '<meta property="og:type"' not in rendered
    assert '<meta property="og:url"' not in rendered
    assert '<meta property="og:description"' not in rendered
    assert '<meta property="og:image"' not in rendered
    assert '<meta property="og:locale"' not in rendered
    assert '<script type="application/ld+json">' not in rendered

def test_omit_page_header_when_no_header_tag_is_set():
    rendered = read_file('test/features/no-header.html')

    assert '<header>' not in rendered
    assert '</header>' not in rendered
    assert '<a href="https://oliz.io/ggpy"><img src="https://oliz.io/ggpy/static/gg.png" class="avatar" /></a>' not in rendered
    assert '<div style="text-align:right;">' not in rendered
    assert '<h1' not in rendered
    assert '<small><a href=' not in rendered

    assert '<footer>' in rendered

def test_omit_page_footer_when_no_footer_tag_is_set():
    rendered = read_file('test/features/no-footer/index.html')

    assert '<header>' in rendered

    assert '<footer>' not in rendered
    assert '</footer>' not in rendered
    assert ' class="nav">' not in rendered
    assert ' class="social">' not in rendered
