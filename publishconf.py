#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'https://rickhau.github.io'
RELATIVE_URLS = False

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing
# https://github.com/DandyDev/pelican-bootstrap3/issues/219
# http://leafwind.tw/20141111-using-pelican-to-build-blog.html
#   Admin -> Settings ->Your website's shortname is XXX 
#   DISQUS_SITENAME = 'shortname'

DISQUS_SITENAME = "rickhau-github-io"
# GOOGLE_UNIVERSAL_ANALYTICS = "UA-96861038-1"
GOOGLE_ANALYTICS = "UA-96861038-1" # Refer to analytics.html
