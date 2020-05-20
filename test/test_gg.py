#!/usr/bin/env python
# -*- coding: utf-8 -*-

import gg

def test_is_root_readme():
    assert gg.is_root_readme('README.md')