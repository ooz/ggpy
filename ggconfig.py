#!/usr/bin/env python
# -*- coding: utf-8 -*-

config = {
    'site': {
        'base_url': 'https://oliz.io/ggpy',          # Default: no base_url, then ggpy won't convert to absolute/canonical links
        'render_root_readme': True,                  # Deprecated, soon controlled via tags (__index) in the affected README.md's meta block, default: True
        'generate_sitemap': True,                    # Default: False, could also make git dependency optional (only needed for timestamp)
        'additional_sitemap_entries': [],            # Default: none / empty
        'title': 'Good Generator.py',                # Default: no common title will be rendered across all pages
        'logo': 'static/gg.png',                     # Default: no common logo will be rendered across all pages
        'about_url': 'https://oliz.io/ggpy/test/about', # Default: no about link
        'csp': '''<meta http-equiv="Content-Security-Policy" content="script-src 'unsafe-inline'">''', # Deprecated, see below
        'referrer': '''<meta name="referrer" content="no-referrer">''' # Deprecated, will prob. be replaced with general way to inject header tags
    },
    'author': {
        'name': 'Good Gen',
        'url': 'https://oliz.io/ggpy',
    },
    'social': {
        'email': 'example@example.com',
        'github_url': 'https://github.com/ooz/ggpy',
        'twitter_url': 'https://twitter.com/oozgo',
        'twitter_username': '@oozgo'
    }
}
