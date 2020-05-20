#!/usr/bin/env python
# -*- coding: utf-8 -*-

import gg

def test_style():
    style = gg.style()

    assert '<style>' in style
    assert 'body {' in style
    assert '.avatar' in style
    assert '.nav' in style
    assert '.social' in style
    assert '.dark-mode' in style
    assert '</style>' in style

    assert '<script>' in style
    assert 'function toggleTheme' in style
    assert 'function initTheme' in style
    assert '</script>' in style

def test_footer_navigation():
    footer_nav = gg.footer_navigation('https://example.com', False)

    assert footer_nav == \
'''<a href="https://example.com" class="nav">back</a>
<a href="#" class="nav">top</a>
<a href="javascript:toggleTheme()" class="nav">🌚🌞</a>'''

def test_about_and_social_icons():
    about_and_social = gg.about_and_social_icons()

    assert about_and_social == \
'''<a href="https://twitter.com/oozgo" class="social">twitter</a>
<a href="https://github.com/ooz/ggpy" class="social">github</a>
<a href="https://ooz.github.io/ggpy/test/about" class="social">about</a>'''
