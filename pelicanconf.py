#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# To deplot locally:
# 1. $ ./reserve.sh
# 2. Open http://localhost:8000/index.html in browser

# To deplot online:
# 0. Set to false RELATIVE_URLS
# 1. $ ./prepare_html_repo.sh
# 2. Commit and Push castoris-html

###########################
# General Pelican
###########################
# Language and Timezone
TIMEZONE = 'America/Montreal'
DEFAULT_LANG = u'en'
DEFAULT_DATE_FORMAT = '%Y/%m/%d'

# Site general information
AUTHOR = u'Raymundo Cassani'
SITENAME = u'CastorisCausa'
SITEURL = u'https://www.castoriscausa.com'

# Delete Output files everytime Pelican runs
DELETE_OUTPUT_DIRECTORY = True
# Keep these files from deleting output
OUTPUT_RETENTION = ['.git']

# True if you want document-relative URLs when developing
# False to deploy online
RELATIVE_URLS = True

###########################
# KIS theme
###########################
THEME = ".//theme//pelican-kis"
# Subtitle string
# SITESUBTITLE = u'Catchy phrase'

# Show elements in Menu bar
MENU_ELEMENTS = ['menu_links', 'categories', 'pages']
MENU_LINKS= (
                ('Home', SITEURL),
            ) # Menu items before Pages

# Show elements in Side bar
SIDEBAR_ELEMENTS = ['tipuesearch_input', 'links', 'categories', 'tags']
SIDEBAR_TITLE_TEXT = u'Hello'
SIDEBAR_TEXT = u'A brief text that will appear in de siderbar, this can be anything'

# Blogroll
LINKS = (
         ('Home', SITEURL),
         ('MuSAE Lab', 'http://musaelab.ca/')
        )

# Show Metadata in Indexes and Articles
SHOW_ARTICLE_TAGS = True
SHOW_ARTICLE_AUTHOR = False
SHOW_ARTICLE_CATEGORY = True
SHOW_ARTICLE_DATEMODIFIED = True

# Customized CSS file for CastorisCausa
CUSTOM_CSS = 'castoris.css'

###########################
# Others
###########################
# Social icons
# https://fontawesome.com/icons?d=gallery&m=free
SOCIAL = (
          ('GitHub', 'https://github.com/rcassani'),
          ('Twitter', 'https://twitter.com/r_cassani'),
          ('LinkedIn', 'https://www.linkedin.com/in/rcassani/'),
          ('user-graduate', 'https://scholar.google.com/citations?hl=en&user=3A9_Ww8AAAAJ'),
          ('envelope', 'mailto:raymundo.cassani@gmail.com'),
         )

# DISQUS
DISQUSURL = 'https://castoriscausa.com'
DISQUS_SITENAME = u"castoriscausa"
DISQUS_NO_ID = True
DISQUS_DISPLAY_COUNTS = True

# Pygments Style, see: http://pygments.org/demo/6353539/?style=native
PYGMENTS_STYLE = 'native'  # native, fruity, paraiso-dark

# Google Analytics Track-ID
GOOGLE_ANALYTICS = 'UA-86432394-1'

# CC License
CC_LICENSE = "CC-BY-NC-SA"

# Plugins directory
PLUGIN_PATHS = ['plugins/']
PLUGINS = ['tipue_search', 'sitemap','series']

SITEMAP = {'format': 'xml'}

JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.with_', 'jinja2.ext.do']}

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight', 'linenums':'True'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
        'markdown.extensions.toc': {'title': 'Contents:'},
    },
    'output_format': 'html5',
}

############################
#  Content
############################
PATH = 'content'            # Content root directory
ARTICLE_PATHS = ['posts']   # Article directories
PAGE_PATHS = ['pages']      # Page directories
IGNORE_FILES = ['drafts']   # Ignored files

# Directories to be copied to Output (paths relative to Content)
STATIC_PATHS = ['images', 'custom_css', 'extra/CNAME', 'extra/robots.txt', 'htmls']
# Paths rel to Content : {'path' : Path in Output}
EXTRA_PATH_METADATA = {
     'custom_css/castoris.css': {'path': 'castoris.css'},
     'extra/CNAME': {'path': 'CNAME'},
     'extra/robots.txt': {'path': 'robots.txt'},
}

DIRECT_TEMPLATES = ('index', 'categories', 'authors', 'archives', 'search')

############################
# Output
############################
OUTPUT_PATH = 'output/'     # Output root directory

ARTICLE_URL = 'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}/'  # article URL
PAGE_URL = 'pages/{slug}'                            # page URL
ARTICLE_LANG_URL = 'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}/{lang}/' # article lang URL
CATEGORY_URL = 'category/{slug}/'                    # category index URL
TAG_URL = 'tags/{slug}/'                             # tag index URL

ARTICLE_SAVE_AS = ARTICLE_URL + 'index.html'         # article filename
PAGE_SAVE_AS = PAGE_URL + '.html'                    # page filename
ARTICLE_LANG_SAVE_AS = ARTICLE_LANG_URL + 'index.html' # article lang filename
CATEGORY_SAVE_AS = CATEGORY_URL + 'index.html'       # category index filename
TAG_SAVE_AS = TAG_URL + 'index.html'                 # tag index filename


# Add the field Sortorder to the page MD documentm e.g. Sortorder: 2
PAGES_SORT_ATTRIBUTE = 'sortorder' # Sort pages by a 'sortorder' attribute
SUMMARY_MAX_LENGTH = 50            # Summary for Index (words)
DEFAULT_PAGINATION = 6             # Number of articles per page
NEWEST_FIRST_ARCHIVES = True       # Order of Articles

############################
# Feed
############################
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
