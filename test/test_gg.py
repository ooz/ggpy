#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

import gg

def test_is_root_readme():
    assert gg.is_root_readme('README.md')

def test_last_modified():
    assert re.match(r'''\d+-\d{2}-\d{2}''', gg.last_modified('README.md'))

def test_convert_path():
    assert gg.convert_path('README.md') == 'index.html'
    assert gg.convert_path('test/README.md') == 'test/index.html'
    assert gg.convert_path('test/some-post.md') == 'test/some-post.html'

def test_convert_canonical():
    assert gg.convert_canonical('.', 'index.html') == 'https://ooz.github.io/ggpy/'
    assert gg.convert_canonical('.', 'test/features/index.html') == 'https://ooz.github.io/ggpy/test/features/'
    assert gg.convert_canonical('.', 'test/some-post.html') == 'https://ooz.github.io/ggpy/test/some-post.html'