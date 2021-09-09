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
                  <br> <font size="6">ILS Doctoral Research Forum</font><br> <br>   
                  <br> <font size="5">Nov. 12, 2021</font>
                  <br>
                  <br> <font size="5">ILS, Luddy Hall</font>
                  <br>
                  <br>
                  <br> <font size="4">700 N. Woodlawn Ave</font>
                  <br> <font size="4">Bloomington, IN</font>
                  <br> <font size="4">USA</font>"""

SITELOGO = "/images/profile.png"
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
             )
GITHUB_URL = 'https://github.com/ils-drf/ils-drf.github.io-src'

ARTICLE_HIDE_TRANSLATION = False

DISPLAY_CATEGORIES_ON_MENU = False

LOAD_CONTENT_CACHE = False
FILENAME_METADATA = '(?P<title>.*)'
DELETE_OUTPUT_DIRECTORY = False

OUTPUT_PATH = 'output'
INDEX_SAVE_AS = 'index.html'

# # Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# LINKS = ((ILS, https://ils.indiana.edu/index.html)
#   )

