#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'rickhau'
SITENAME = u'\u96a8\u610f\u96dc\u8a18 (Casual Notes)'
SITEURL = 'https://rickhau.github.io'

PATH = 'content'
DATE_FORMATS = {
    'zh_TW': '%Y-%m-%d %H:%M:%S'
}

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
LINKS = (('Online Compiler', 'http://rextester.com/'),
         ('UEFI Resource', 'http://www.lab-z.com/'),
         ('Brendan Gregg', 'http://www.brendangregg.com/blog/'),
         ('Colin Ian King', 'http://smackerelofopinion.blogspot.tw/'),)

# Social widget
SOCIAL = (('github', 'https://github.com/rickhau'),
          ('twitter', 'https://twitter.com/rickhau0912'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = False

# Theme list
# https://github.com/getpelican/pelican-themes
# Visual Theme: http://www.pelicanthemes.com/
# Change theme name here and update the .travis.xml to the corresponding theme git repository

#THEME = "pelican-bootstrap3"
#THEME = "pelican-simplegrey"
#THEME = "pelican-sober"
#THEME = "pelican-octopress-theme" # like Github Flavored Markdown theme
THEME = "blue-penguin"

PLUGIN_PATHS = ['pelican-plugins']

# For pelican-bootstrap3 theme settings
# FAVICON= "images/favicon.ico"
# PLUGINS = ["disqus_static"]
# PLUGINS = ['assets', 'i18n-subsites']  # i18n-subtitles: this is for pelican-bootstrap3 theme
#JINJA_ENVIRONMENT = {
#    'extensions': ['jinja2.ext.i18n'], #this is for pelican-bootstrap3 theme
#} 

# Specify pygments-css style: monokai.css
PYGMENTS_STYLE = 'monokai'
# Enable CodeHilite extension
# http://pythonhosted.org/Markdown/extensions/code_hilite.html#syntax
# https://pythonhosted.org/Markdown/extensions/index.html
# http://docs.getpelican.com/en/3.6.3/faq.html
MARKDOWN = {
    'extension_configs': {
        # 'markdown.extensions.codehilite': {'linenums': True}, # Doesn't support inline linue nums
        'markdown.extensions.codehilite': {'linenums': True, 'css_class': 'highlight'},
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
#PELICAN_SOBER_ABOUT = 'rickhau'
#PELICAN_SOBER_STICKY_SIDEBAR = True

# THEME: octopress
SEARCH_BOX = True

# THEME: blue-penguin
# https://github.com/jody-frankowski/blue-penguin
# all defaults to True.
DISPLAY_HEADER = True
DISPLAY_FOOTER = True
DISPLAY_HOME   = True
DISPLAY_MENU   = True
# provided as examples, they make ‘clean’ urls. used by MENU_INTERNAL_PAGES.
HOME_URL = 'index'
HOME_SAVE_AS = 'index.html'

# use those if you want pelican standard pages to appear in your menu
MENU_INTERNAL_PAGES = (
    ('HOME', HOME_URL, HOME_SAVE_AS),
    ('Archives', ARTICLE_URL, ARTICLE_SAVE_AS)
)
