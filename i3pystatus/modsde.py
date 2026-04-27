#!/usr/bin/env python

import urllib.request
import urllib.parse
import urllib.error
import re
import http.cookiejar
import xml.etree.ElementTree as ET
import webbrowser

from i3pystatus import IntervalModule


class ModsDeChecker(IntervalModule):
    """
    This class returns i3status parsable output of the number of
    unread posts in any bookmark in the mods.de forums.
    """

    settings = (
        ("format",
         """Use {unread} as the formatter for number of unread posts"""),
        ('keyring_backend', 'alternative keyring backend for retrieving credentials'),
        ("offset", """subtract number of posts before output"""),
        "color", "username", "password"
    )
    required = ("username", "password")
    keyring_backend = None

    color = "#7181fe"
    offset = 0
    format = "{unread} new posts in bookmarks"

    login_url = "http://login.mods.de/"
    bookmark_url = "http://forum.mods.de/bb/xml/bookmarks.php"
    opener = None
    cj = None
    logged_in = False

    on_leftclick = "open_browser"

    def init(self):
        pass

    def run(self):
        pass

    def get_unread_count(self):
        pass

    def login(self):
        pass

    def open_browser(self):
        pass
