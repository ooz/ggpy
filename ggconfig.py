#!/usr/bin/env python
# -*- coding: utf-8 -*-

config = {
    'site': {
        'base_url': 'https://oliz.io/ggpy',          # Default: no base_url, then ggpy won't convert to absolute/canonical links. Must not end with a "/"
        'generate_sitemap': True,                    # Default: False
        'generate_rss': True,                        # Default: False
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
        'about': 'https://oliz.io/about.html',
        'github': 'https://github.com/ooz/ggpy',
        'twitter': 'https://nitter.net/',
        'email': 'mailto:example@example.com'
    }
}
