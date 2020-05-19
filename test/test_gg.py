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