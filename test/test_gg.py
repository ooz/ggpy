#!/usr/bin/env python
# -*- coding: utf-8 -*-

import gg

def test_about_and_social_icons():
    about_and_social = gg.about_and_social_icons()

    assert about_and_social == \
'''<a href="https://twitter.com/oozgo" class="social">twitter</a>
<a href="https://github.com/ooz/ggpy" class="social">github</a>
<a href="https://ooz.github.io/ggpy/test/about" class="social">about</a>'''

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