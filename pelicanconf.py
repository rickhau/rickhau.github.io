#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'rickhau'
SITENAME = u'\u96a8\u610f\u96dc\u8a18 (Casual Notes)'
SITEURL = 'http://rickhau.github.io'

PATH = 'content'

TIMEZONE = 'Asia/Taipei'

DEFAULT_LANG = u'zh'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

FEED_ALL_RSS = None
CATEGORY_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),)

# Social widget
SOCIAL = (('github', 'https://github.com/rickhau'),
          ('twitter', 'https://twitter.com/rickhau0912'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Theme list
# https://github.com/getpelican/pelican-themes
# Change theme name here and update the .travis.xml to the corresponding theme git repository

#THEME = "pelican-bootstrap3"
#THEME = "octopress" # like Github Flavored Markdown theme
#THEME = "pelican-simplegrey"
THEME = "pelican-sober"

PLUGIN_PATHS = ['pelican-plugins']

# For pelican-bootstrap3 theme settings
# FAVICON= "images/favicon.ico"
PLUGINS = ['assets']
# PLUGINS = ['assets', 'i18n-subsites']  # i18n-subtitles: this is for pelican-bootstrap3 theme
#JINJA_ENVIRONMENT = {
#    'extensions': ['jinja2.ext.i18n'], #this is for pelican-bootstrap3 theme
#} 

# Specify pygments-css style: monokai.css
PYGMENTS_STYLE = 'monokai'
# Enable CodeHilite extension
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
    },
    'output_format': 'html5',
}

# Enable Typogirfy
TYPOGRIFY = True

ARTICLE_URL = 'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
#PAGE_URL = 'pages/{slug}/'
#PAGE_SAVE_AS = 'pages/{slug}/index.html'

#YEAR_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/index.html'
#MONTH_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/index.html'

# THEME: pelican-sober
PELICAN_SOBER_ABOUT = 'rickhau'
PELICAN_SOBER_STICKY_SIDEBAR = True
