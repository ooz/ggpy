#!/usr/bin/env python
# -*- coding: utf-8 -*-

config = {
    'site': {
        'base_url': 'https://ooz.github.io/ggpy',
        'render_root_readme': True,
        'generate_sitemap': True,
        'additional_sitemap_entries': [],
        'title': 'Good Generator.py',
        'logo': 'static/gg.png',
        'about_url': 'https://ooz.github.io/ggpy/test/about',
        'csp': '''<meta http-equiv="Content-Security-Policy" content="script-src 'unsafe-inline'">''',
        'referrer': '''<meta name="referrer" content="no-referrer">'''
    },
    'author': {
        'name': 'Good Gen',
        'url': 'https://ooz.github.io/ggpy',
    },
    'social': {
        'email': 'example@example.com',
        'github_url': 'https://github.com/ooz/ggpy',
        'twitter_url': 'https://twitter.com/oozgo',
        'twitter_username': '@oozgo'
    }
}
