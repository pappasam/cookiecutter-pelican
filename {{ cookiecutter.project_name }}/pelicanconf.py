"""Pelican base configuration file."""

# core
#   https://docs.getpelican.com/en/stable/settings.html#basic-settings
#######################################################################
AUTHOR = "PELICAN AUTHOR"
SITENAME = "PELICAN SITENAME"
SITEURL = "http://localhost:8000"
PATH = "content"
TIMEZONE = "EST"
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
DEFAULT_PAGINATION = 10
FILENAME_METADATA = "(?P<slug>.*)"
LOAD_CONTENT_CACHE = False
TYPOGRIFY = True
EXTRA_PATH_METADATA = {
    "extra/custom.css": {
        "path": "static/custom.css",
    },
    "images/favicon.ico": {
        "path": "favicon.ico",
    },
}
STATIC_PATHS = ["images", "extra"]
MARKDOWN = {
    "extension_configs": {
        "markdown.extensions.codehilite": {
            "css_class": "highlight",
        },
        "markdown.extensions.extra": {},
        "markdown.extensions.meta": {},
        "markdown.extensions.toc": {
            "permalink": True,
            "title": "Table of Contents",
            "marker": "[TOC]",
            "toc_depth": 3,
        },
        "mdx_include": {"base_path": "./content/articles"},
    },
    "output_format": "html5",
}

# theme: https://github.com/pappasam/pelican-alchemy
#######################################################################
THEME = "pelican-themes/pelican-theme/alchemy"
SITESUBTITLE = "MY THEME SUBTITLE"
DESCRIPTION = "MY THEME DESCRIPTION"
SITEIMAGE = "/images/little-penguin-152-27563.png"
HIDE_AUTHORS = True
THEME_CSS_OVERRIDES = ["static/custom.css"]
PYGMENTS_STYLE = "default"
# fmt: off
ICONS = (
    ("fab fa-github", "https://github.com/pappasam"),
    ("fab fa-linkedin", "https://www.linkedin.com/in/samuel-roeca-23010735"),
    ("fab fa-facebook", "https://www.facebook.com/sam.roeca"),
    ("fab fa-twitter", "https://twitter.com/SamRoeca"),
    ("fab fa-youtube", "https://www.youtube.com/channel/UCjORdFKiDlqzzW7bWYqXuKA"),  # pylint: disable=line-too-long
    ("far fa-envelope", "mailto:samuel.roeca@gmail.com"),
)
# fmt: on

# plugins
#   https://github.com/pelican-plugins/sitemap#usage
#   https://github.com/pelican-plugins/neighbors#basic-usage
#######################################################################
PLUGINS = ["sitemap", "neighbors"]
SITEMAP = {
    "format": "xml",
    "priorities": {
        "articles": 1,
        "pages": 1,
        "indexes": 1,
    },
    "changefreqs": {
        "articles": "always",
        "pages": "always",
        "indexes": "always",
    },
}
