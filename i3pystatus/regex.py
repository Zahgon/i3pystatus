import re

from i3pystatus import IntervalModule


class Regex(IntervalModule):
    """
    Simple regex file watcher

    The groups of the regex are passed to the format string as positional arguments.
    """

    flags = 0
    format = "{0}"
    settings = (
        ("format", "format string used for output"),
        "regex",
        ("file", "file to search for regex matches"),
        ("flags", "Python.re flags"),
    )
    required = ("regex", "file")

    def init(self):
        pass

    def run(self):
        pass
