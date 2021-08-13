#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import datetime
import os

AUTHOR = 'ILS Doctoral Research Forum Organizers'
SITENAME = 'ILS Doctoral Research Forum'
SITEURL = 'https://ils-drf.github.io'
SITESUBTITLE = """<br>
                  <br>
                  <br><font size="5">ILS Doctoral Research Forum</font><br> <br>   
                  <br> <font size="4">**TIME TBD**, 2021</font>
                  <br>
                  <br> <font size="4">ILS, Luddy Hall</font>
                  <br>
                  <br>
                  <br> 700 N. Woodlawn Ave
                  <br> Bloomington, IN, USA"""

SITELOGO = "/images/profile_3.png"
# FAVICON = "/images/favicon.ico"
BROWSER_COLOR = '#333333'

USE_GOOGLE_FONTS = True
HOME_HIDE_TAGS = True
DISABLE_URL_HASH = True

MAIN_MENU = True
DISPLAY_PAGES_ON_MENU = False

PATH = 'content'
STATIC_PATHS = ['images']

TIMEZONE = 'America/Indiana/Indianapolis'
DATE_FORMATS = {"en": "%b %d, %Y"}

# License
COPYRIGHT_YEAR = datetime.now().year
COPYRIGHT_NAME = 'MIT'

DEFAULT_LANG = 'en'

THEME = "../../repo/pelican-themes/Flex"

CUSTOM_CSS = "static/custom.css"
EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'},  # and this
    "extra/custom.css": {"path": "static/custom.css"},
}

THEME_COLOR_AUTO_DETECT_BROWSER_PREFERENCE = True

LINKS_IN_NEW_TAB = 'external'

# SOCIAL = (('You can add links in your config file', '#'),
#           ('Another social link', '#'),)

DEFAULT_PAGINATION = 5


RELATIVE_URLS = True

MENUITEMS = (
            ('KEYNOTE SPEAKER', '/keynote'),
            ('CALL FOR PAPERS', "/cfp"),
            ('DATES', "/dates"),
             # ('CONFERENCE SCHEDULE', "/schedule")
            # ('Blog', '/blog/')
             )
GITHUB_URL = 'https://github.com/ils-drf/ils-drf.github.io-src'

ARTICLE_HIDE_TRANSLATION = False

DISPLAY_CATEGORIES_ON_MENU = False

LOAD_CONTENT_CACHE = False
FILENAME_METADATA = '(?P<title>.*)'
DELETE_OUTPUT_DIRECTORY = False

OUTPUT_PATH = 'output/blog'
INDEX_SAVE_AS = 'blog/index.html'
INDEX_URL = 'blog/'
# # Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


# Blogroll
# LINKS = (('Pelican', 'https://getpelican.com/'),
#          ('Python.org', 'https://www.python.org/'),
#          ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
#          ('You can modify those links in your config file', '#'),)

# Social widget


# Uncomment following line if you want document-relative URLs when developing
