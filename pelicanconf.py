#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

#Note: the output directly needs to added seperately

AUTHOR = 'The Atlas Project'
SITENAME = 'The Atlas Project'
SITEURL = 'https://theatlasproject.org'

PATH = 'content'

OUTPUT_PATH ='output/theatlusproject.github.io/'
TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
         ('Got Questions?', 'https://www.gotquestions.org/'),
         ('Desiring God', 'https://www.desiringgod.org/'),
         ('The Bible Project', 'https://thebibleproject.com/'),
         )

# Social widget
SOCIAL ='' 
#(('You can add links in your config file', '#')          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

#File Paths
THEME = 'themes/attila2'
HOME_COVER = 'img/home-bg2.jpg'
HEADER_COVER = 'img/home-bg2.jpg' #HEADER_COVER offically deprecated
ARTICLES_PATHS = ['content/articles']
STATIC_PATHS = ['img']
PAGE_PATHS = ['pages']


# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

DEFAULT_DATE_FORMAT = ''

#Content Lisenscing: CC-BY
CC_LICENSE = 'CC-BY'
SHOW_ARTICLE_AUTHOR = True

SHOW_CREDITS = True

#logos
SITELOGO = 'img/atlas_filler_logo.png'
SITELOGO_SIZE = '32'
FAVICON = '/favico.png'

#Cache Settings
CACHE_CONTENT = False
LOAD_CONTENT_CACHE = False