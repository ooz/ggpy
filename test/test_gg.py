#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

import gg

DATE = r'''\d+-\d{2}-\d{2}'''

def test_is_root_readme():
    assert gg.is_root_readme('README.md')

def test_last_modified():
    assert re.match(DATE, gg.last_modified('README.md'))

def test_last_modified_for_unknown_file():
    assert gg.last_modified('does-not-exist.md') == ''

def test_convert_path():
    assert gg.convert_path('README.md') == 'index.html'
    assert gg.convert_path('test/README.md') == 'test/index.html'
    assert gg.convert_path('test/some-post.md') == 'test/some-post.html'

def test_convert_canonical():
    assert gg.convert_canonical('.', 'index.html') == 'https://ooz.github.io/ggpy/'
    assert gg.convert_canonical('.', 'test/features/index.html') == 'https://ooz.github.io/ggpy/test/features/'
    assert gg.convert_canonical('.', 'test/some-post.html') == 'https://ooz.github.io/ggpy/test/some-post.html'

def test_read_post():
    post = gg.read_post('.', "README.md")
    assert post['filepath'] == 'index.html'
    assert len(post['html'])
    assert post['date'] == ''
    assert re.match(DATE, post['last_modified'])
    assert post['tags'] == ''
    assert post['title'] == ''
    assert post['url'] == 'https://ooz.github.io/ggpy/'