#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

import gg

def test_is_root_readme():
    assert gg.is_root_readme('README.md')

def test_last_modified():
    assert re.match(r'''\d+-\d{2}-\d{2}''', gg.last_modified('README.md'))