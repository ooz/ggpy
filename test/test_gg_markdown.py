#!/usr/bin/env python
# -*- coding: utf-8 -*-

import gg
from ggconfig import config

def test_markdown2post() -> None:
    no_meta_no_config = gg.markdown2post()
    assert no_meta_no_config['date'] == ''
    assert no_meta_no_config['title'] == ''
    assert no_meta_no_config['raw_title'] == ''
    assert no_meta_no_config['description'] == ''
    assert no_meta_no_config['raw_description'] == ''
    assert no_meta_no_config['tags'] == ''
    assert no_meta_no_config['html_headline'] == ''
    assert no_meta_no_config['html_section'] == ''

    no_meta_ggconfig = gg.markdown2post(config=config)
    assert no_meta_ggconfig['date'] == ''
    assert no_meta_ggconfig['title'] == ''
    assert no_meta_ggconfig['raw_title'] == ''
    assert no_meta_ggconfig['description'] == ''
    assert no_meta_ggconfig['raw_description'] == ''
    assert no_meta_ggconfig['tags'] == ''
    assert no_meta_ggconfig['html_headline'] == ''
    assert no_meta_ggconfig['html_section'] == ''

    content_no_meta_no_config = gg.markdown2post('# Headline!')
    assert content_no_meta_no_config['date'] == ''
    assert content_no_meta_no_config['title'] == ''
    assert content_no_meta_no_config['raw_title'] == ''
    assert content_no_meta_no_config['description'] == ''
    assert content_no_meta_no_config['raw_description'] == ''
    assert content_no_meta_no_config['tags'] == ''
    assert content_no_meta_no_config['html_headline'] == ''
    assert content_no_meta_no_config['html_section'] == '<h1 id="headline">Headline!</h1>'

    content_meta_ggconfig = gg.markdown2post(given_newpost(), config)
    assert content_meta_ggconfig['date'] == '2021-04-04T15:33:17Z'
    assert content_meta_ggconfig['title'] == 'New Post'
    assert content_meta_ggconfig['raw_title'] == 'New Post'
    assert content_meta_ggconfig['description'] == 'Description'
    assert content_meta_ggconfig['raw_description'] == 'Description'
    assert content_meta_ggconfig['tags'] == '__draft__, some-tag, some-other-tag'
    assert content_meta_ggconfig['html_headline'] == '<h1 id="new-post">New Post</h1>'
    assert content_meta_ggconfig['html_section'] == '<p>My new post!</p>'

def given_newpost() -> str:
    return \
'''---
title: New Post
description: Description
date: 2021-04-04T15:33:17Z
tags: __draft__, some-tag
tags: some-other-tag
---

My new post!
'''