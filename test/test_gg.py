#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

import gg
from ggconfig import config

DATE = r'''\d+-\d{2}-\d{2}'''
UTC_FORMATTED = DATE + r'''T\d{2}:\d{2}:\d{2}Z'''

def test_now_utc_formatted() -> None:
    assert re.match(UTC_FORMATTED, gg.now_utc_formatted())

def test_last_modified() -> None:
    assert re.match(DATE, gg.last_modified('README.md'))

def test_last_modified_for_unknown_file() -> None:
    assert gg.last_modified('does-not-exist.md') == ''

def test_convert_path() -> None:
    assert gg.convert_path('README.md') == 'index.html'
    assert gg.convert_path('test/README.md') == 'test/index.html'
    assert gg.convert_path('test/some-post.md') == 'test/some-post.html'

def test_convert_canonical() -> None:
    assert gg.convert_canonical('.', 'index.html', config) == 'https://oliz.io/ggpy/'
    assert gg.convert_canonical('.', 'test/features/index.html', config) == 'https://oliz.io/ggpy/test/features/'
    assert gg.convert_canonical('.', 'test/some-post.html', config) == 'https://oliz.io/ggpy/test/some-post.html'

    assert gg.convert_canonical('.', 'index.html') == 'index.html'
    assert gg.convert_canonical('.', 'test/features/index.html') == 'test/features/'
    assert gg.convert_canonical('.', 'test/some-post.html') == 'test/some-post.html'

def test_kebab_case() -> None:
    assert gg.kebab_case('New Post 2') == 'new-post-2'

def test_kebab_case_filter_special_characters() -> None:
    assert gg.kebab_case('New Post :)') == 'new-post-'

def test_read_post() -> None:
    post = gg.read_post('.', "README.md", config)
    assert post['filepath'] == 'index.html'
    assert len(post['html'])
    assert post['date'] == ''
    assert re.match(DATE, post['last_modified'])
    assert post['tags'] == ''
    assert post['title'] == ''
    assert post['url'] == 'https://oliz.io/ggpy/'
    assert post['is_index'] == False

    post = gg.read_post('.', "README.md")
    assert post['url'] == 'index.html'
    assert post['is_index'] == False

    post = gg.read_post('.', "test/features/README.md", config)
    assert post['url'] == 'https://oliz.io/ggpy/test/features/'
    assert post['is_index'] == False

    post = gg.read_post('.', "test/features/README.md")
    assert post['url'] == 'test/features/'
    assert post['is_index'] == False
