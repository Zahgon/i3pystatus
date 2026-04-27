import errno
import os
import locale
from datetime import datetime

try:
    import pytz
    HAS_PYTZ = True
except ImportError:
    HAS_PYTZ = False

from i3pystatus import IntervalModule


class Clock(IntervalModule):
    """
    This class shows a clock.

    .. note:: Optionally requires `pytz` for time zone data when using time
        zones other than local time.

    Format can be passed in four different ways:

    - single string, no timezone, just the strftime-format
    - one two-tuple, first is the format, second the timezone
    - list of strings - no timezones
    - list of two tuples, first is the format, second is timezone

    Use mousewheel to cycle between formats.

    For complete time format specification see:

    ::

        man strftime

    All available timezones are located in directory:

    ::

        /usr/share/zoneinfo/

    .. rubric:: Format examples

    ::

        # one format, local timezone
        format = '%a %b %-d %b %X'
        # multiple formats, local timezone
        format = [ '%a %b %-d %b %X', '%X' ]
        # one format, specified timezone
        format = ('%a %b %-d %b %X', 'Europe/Bratislava')
        # multiple formats, specified timezones
        format = [ ('%a %b %-d %b %X', 'America/New_York'), ('%X', 'Etc/GMT+9') ]

    """

    settings = (
        ("format", "`None` means to use the default, locale-dependent format."),
        ("color", "RGB hexadecimal code color specifier, default to #ffffff"),
    )
    format = None
    color = "#ffffff"
    interval = 1
    on_upscroll = ["scroll_format", 1]
    on_downscroll = ["scroll_format", -1]

    def init(self):
        pass

    def _expand_format(self, fmt):
        pass

    def _get_system_tz(self):
        '''
        Get the system timezone for use when no timezone is explicitly provided

        Requires pytz, if not available then no timezone will be set when not
        explicitly provided.
        '''
        pass

    def run(self):
        pass

    def scroll_format(self, step=1):
        pass
