#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# To deplot locally:
# 1. $ fab build
# 2. $ fab serve, alternatively, $ fab reserve, does build and serve
# 3. Open http://localhost:8000/index.html in browser

# Site general information
AUTHOR = u'Ray Cassani'
SITENAME = u'CastorisCausa'
# SITEURL = 'wwww.castoriscausa.com'

###########################
# ######## THEME ######## #
###########################

# https://github.com/getpelican/pelican-themes/tree/master/pelican-bootstrap3
THEME = ".//pelican-bootstrap3"
BOOTSTRAP_THEME = 'sandstone'  # This bootstrap3 theme serves as base

###########################
# #### EXTRAS BS3 ####### #
###########################
# Author info for each article
SHOW_ARTICLE_AUTHOR = False

# Category for each article
SHOW_ARTICLE_CATEGORY = False

# Modified date besides publishing date for each article
SHOW_DATE_MODIFIED = False

# Custonized CSS file for CastorisCausa
CUSTOM_CSS = 'theme//css//castoris.css'

# Pygments Style, see: http://pygments.org/demo/6353539/?style=native
PYGMENTS_STYLE = 'native'

# Pagination
USE_PAGER = False
# TRUE = shows 'Older posts' and 'Newer post' buttons
# FALSE = shows arrows and numbers of pages <<, 1,2,3 >>

# Sitelogo and size
# SITELOGO = 'images/dr_pk.jpg'
# SITELOGO_SIZE = 50

HIDE_SITENAME = False

# Breadcrumbs: HOME > Something > something
DISPLAY_BREADCRUMBS = True

# Inverse Navigation bar color
BOOTSTRAP_NAVBAR_INVERSE = False  # Leave as FALSE, and edit in castoris.css

# FAVICON = 'images/dr_pk.jpg.png'

DISPLAY_ARTICLE_INFO_ON_INDEX = True  # Shows Date and Tag in summaries

# BANNER = 'images/dr_pk.jpg'
# BANNER_ALL_PAGES = True

# SIDEBAR_IMAGES_HEADER = 'My Images'
SIDEBAR_IMAGES = ['../images/side_image_500.jpg']  # Path relative to index.html in output


# DISQUS
DISQUSURL = 'http://castoriscausa.com'
DISQUS_SITENAME = u"castoriscausa"
DISQUS_NO_ID = True
DISQUS_DISPLAY_COUNTS = True

# Tag Cloud
TAG_CLOUD_MAX_ITEMS = 10

# Language and Timezone
TIMEZONE = 'America/Montreal'
DEFAULT_LANG = u'en'
DATE_FORMATS = '%a, %d %b %Y'

# Delete Output files everytime SSG runs
DELETE_OUTPUT_DIRECTORY = True
# Keep these files from deleting output
OUTPUT_RETENTION = ['.git', 'CNAME']

# Makes style improvements in fonts
TYPOGRIFY = True
CC_LICENSE = "CC-BY-NC-SA"

############################
# ####### CONTENT ######## #
# Defines the Paths for different elements of content
############################
# Content root directory
PATH = 'content'
# Page directories
PAGE_PATHS = ['pages']
# Article directories
ARTICLE_PATHS = ['articles']
# Ignored files
IGNORE_FILES = ['drafts', 'main.md', 'software.md']
# Directories to be copied to OUTPUT (paths relative to Content)
STATIC_PATHS = ['images', 'custom_css']
# Pelican to change castoris.css path from './custom_css/' to `./themes/css/
EXTRA_PATH_METADATA = {
    'custom_css/castoris.css': {'path': './theme/css/castoris.css'}
}
# Plugins directory
PLUGIN_PATHS = ['plugins']
PLUGINS = ['tipue_search']
DIRECT_TEMPLATES = ('index', 'categories', 'authors', 'archives', 'search')

############################
# ####### OUTPUT ######### #
# Defines paths and filenames for Output files
############################
# Output directory
OUTPUT_PATH = 'output/'
# HTML files for Pages
PAGE_SAVE_AS = 'pages/{slug}.html'
# HTML files for Articles
ARTICLE_SAVE_AS = 'posts/{slug}.html'
# HTML files for Articles with translation
ARTICLE_LANG_SAVE_AS = 'posts/{slug}-{lang}.html'

############################
# ######## PAGES ######### #
# Defines the URL for the elements in the website
# www.site.com/+ ...
############################
# Pages
PAGE_URL = 'pages/{slug}'
# Articles
ARTICLE_URL = 'posts/{slug}'
# Articles with translation
ARTICLE_LANG_URL = 'posts/{slug}-{lang}'

###########################
# #### INDEX HTML LOOK ####### #
###########################
# Display pages list on the top menu
DISPLAY_PAGES_ON_MENU = True
# Display categories list on the top menu
DISPLAY_CATEGORIES_ON_MENU = False
# Display categories list as a submenu of the top menu
DISPLAY_CATEGORIES_ON_SUBMENU = True
# Display the category in the article's info
DISPLAY_CATEGORIES_ON_POSTINFO = False
# Display the author in the article's info
DISPLAY_AUTHOR_ON_POSTINFO = False
# Display the search form
DISPLAY_SEARCH_FORM = True
# Sort pages list by a given attribute
# Add the field Sortorder to the page MD documentm e.g. Sortorder: 2
PAGES_SORT_ATTRIBUTE = 'sortorder'
# Measured in Words
SUMMARY_MAX_LENGTH = 50
# Google Analytics Track-ID
GOOGLE_ANALYTICS = 'UA-86432394-1'
# Number of articles per page
DEFAULT_PAGINATION = 6
# Order of Articles
NEWEST_FIRST_ARCHIVES = True

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
         ('Home', 'http://www.castoriscausa.com'),
         ('#', '#')
        )

# Social widget
SOCIAL = (
          ('GitHub', 'https://github.com/rcassani'),
          ('#', '#')
         )


# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

JINJA_EXTENSIONS = []
