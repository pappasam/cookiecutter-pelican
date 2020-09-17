"""Pelican production configuration file."""

# pylint: disable=wildcard-import,unused-wildcard-import,wrong-import-position
# isort: off

import os
import sys

sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = "https://mydomain.com"
RELATIVE_URLS = False
FEED_ALL_ATOM = "feeds/all.atom.xml"
CATEGORY_FEED_ATOM = "feeds/{slug}.atom.xml"
DELETE_OUTPUT_DIRECTORY = False
DISQUS_SITENAME = "mydisqussitename"
GOOGLE_ANALYTICS = "MYGOOGLEANALYTICSID"
