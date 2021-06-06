#!/usr/bin/env python
# -*- coding: utf-8 -*-

config = {
    'site': {
        'base_url': 'https://oliz.io/ggpy',          # Default: no base_url, then ggpy won't convert to absolute/canonical links
        'generate_sitemap': True,                    # Default: False, could also make git dependency optional (only needed for timestamp)
        'additional_sitemap_entries': [],            # Default: none / empty
        'title': 'Good Generator.py',                # Default: no common title will be rendered across all pages
        'logo': 'static/gg.png',                     # Default: no common logo will be rendered across all pages
        'head': [                                    # Additioal head tags, default: none / empty
            '''<meta http-equiv="Content-Security-Policy" content="script-src 'unsafe-inline'">''',
            '''<meta name="referrer" content="no-referrer">'''
        ]
    },
    'author': {
        'name': 'Good Gen',
        'url': 'https://oliz.io/ggpy'
    },
    'social': {
        'about_url': 'https://oliz.io/ggpy/test/about',
        'email': 'example@example.com',
        'github_url': 'https://github.com/ooz/ggpy',
        'twitter_url': 'https://twitter.com/oozgo',
        'twitter_username': '@oozgo'
    }
}
