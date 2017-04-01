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

# https://github.com/getpelican/pelican-themes/tree/master/pelican-bootstrap3
THEME = ".//pelican-bootstrap3"
BOOTSTRAP_THEME = 'sandstone'  # This bootstrap3 theme serves as base
# Custonized CSS file for CastorisCausa
CUSTOM_CSS = 'theme//css//castoris.css'

# pelican-bootstrap3 EXTRAS
SHOW_ARTICLE_AUTHOR = False
USE_PAGER = False
# USER_PAGER
# TRUE = shows 'Older posts' and 'Newer post' buttons
# FALSE = shows arrows and numbers of pages <<, 1,2,3 >>
# SITELOGO = 'images/dr_pk.jpg'
# SITELOGO_SIZE = 50
HIDE_SITENAME = False
DISPLAY_BREADCRUMBS = True  # HOME > Something > something
BOOTSTRAP_NAVBAR_INVERSE = False  # Not use in Castoris Theme
# FAVICON = 'images/dr_pk.jpg.png'
DISPLAY_ARTICLE_INFO_ON_INDEX = True  # Shows Date and Tag in summaries
# BANNER = 'images/dr_pk.jpg'
# BANNER_ALL_PAGES = True
# SIDEBAR_IMAGES_HEADER = 'My Images'
SIDEBAR_IMAGES = ['../images/side_image_500.jpg']
# This path is accessible to index and for pages/posts

DISQUSURL = 'http://castoriscausa.com'
DISQUS_SITENAME = u"castoriscausa"
DISQUS_NO_ID = True
DISQUS_DISPLAY_COUNTS = True

TAG_CLOUD_MAX_ITEMS = 10


# Language and Timezone
TIMEZONE = 'America/Montreal'
DEFAULT_LANG = u'en'
DATE_FORMATS = '%a, %d %b %Y'


DELETE_OUTPUT_DIRECTORY = True
OUTPUT_RETENTION = ['.git', 'CNAME']

TYPOGRIFY = True
CC_LICENSE = "CC-BY-NC-SA"

'''
 CONTENT
Defines the Paths for different elements of content
'''
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

'''
 OUTPUT
Defines paths and filenames for Output files
'''
OUTPUT_PATH = 'output/'
# HTML files for Pages
PAGE_SAVE_AS = 'pages/{slug}.html'
# HTML files for Articles
ARTICLE_SAVE_AS = 'posts/{slug}.html'
# HTML files for Articles with translation
ARTICLE_LANG_SAVE_AS = 'posts/{slug}-{lang}.html'


'''
 URLS
Defines the URL for the elements in the website
www.site.com/+ ...
'''
# Pages
PAGE_URL = 'pages/{slug}'
# Articles
ARTICLE_URL = 'posts/{slug}'
# Articles with translation
ARTICLE_LANG_URL = 'posts/{slug}-{lang}'


'''
INDEX HTML LOOK
'''
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
#  Add the fiel Sortorder to the page MD documentm e.g. Sortorder: 2
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
