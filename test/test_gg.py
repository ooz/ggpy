#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

import gg
from ggconfig import config

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
    assert gg.convert_canonical('.', 'index.html', config) == 'https://oliz.io/ggpy/'
    assert gg.convert_canonical('.', 'test/features/index.html', config) == 'https://oliz.io/ggpy/test/features/'
    assert gg.convert_canonical('.', 'test/some-post.html', config) == 'https://oliz.io/ggpy/test/some-post.html'

    assert gg.convert_canonical('.', 'index.html') == 'index.html'
    assert gg.convert_canonical('.', 'test/features/index.html') == 'test/features/'
    assert gg.convert_canonical('.', 'test/some-post.html') == 'test/some-post.html'

def test_kebab_case():
    assert gg.kebab_case('New Post 2') == 'new-post-2'

def test_kebab_case_filter_special_characters():
    assert gg.kebab_case('New Post :)') == 'new-post-'

def test_read_post():
    post = gg.read_post('.', "README.md", False, config)
    assert post['filepath'] == 'index.html'
    assert len(post['html'])
    assert post['date'] == ''
    assert re.match(DATE, post['last_modified'])
    assert post['tags'] == ''
    assert post['title'] == ''
    assert post['url'] == 'https://oliz.io/ggpy/'

    post = gg.read_post('.', "README.md")
    assert post['url'] == 'index.html'