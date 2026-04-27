import collections
import functools
import re
import socket
import string
import inspect
from threading import Timer, RLock

import time


def lchop(string, prefix):
    """Removes a prefix from string

    :param string: String, possibly prefixed with prefix
    :param prefix: Prefix to remove from string
    :returns: string without the prefix
    """
    pass


def popwhile(predicate, iterable):
    """Generator function yielding items of iterable while predicate holds for each item

    :param predicate: function taking an item returning bool
    :param iterable: iterable
    :returns: iterable (generator function)
    """
    pass


def partition(iterable, limit, key=lambda x: x):
    pass


def round_dict(dic, places):
    """
    Rounds all values in a dict containing only numeric types to `places` decimal places.
    If places is None, round to INT.
    """
    pass


class ModuleList(collections.UserList):
    def __init__(self, status_handler, class_finder):
        self.status_handler = status_handler
        self.finder = class_finder
        super().__init__()

    def append(self, module, *args, **kwargs):
        pass

    def get(self, find_id):
        pass


class KeyConstraintDict(collections.UserDict):
    """
    A dict implementation with sets of valid and required keys

    :param valid_keys: Set of valid keys
    :param required_keys: Set of required keys, must be a subset of valid_keys
    """

    class MissingKeys(Exception):
        def __init__(self, keys):
            self.keys = keys

    def __init__(self, valid_keys, required_keys):
        super().__init__()

        self.valid_keys = valid_keys
        self.required_keys = set(required_keys)
        self.seen_keys = set()

    def __setitem__(self, key, value):
        """Trying to add an invalid key will raise KeyError
        """
        if key in self.valid_keys:
            self.seen_keys.add(key)
            self.data[key] = value
        else:
            raise KeyError(key)

    def __delitem__(self, key):
        self.seen_keys.remove(key)
        del self.data[key]

    def __iter__(self):
        """Iteration will raise a MissingKeys exception unless all required keys are set
        """
        if self.missing():
            raise self.MissingKeys(self.missing())

        return self.data.__iter__()

    def missing(self):
        """Returns a set of keys that are required but not set
        """
        pass


def convert_position(pos, json):
    pass


def bytes_info_dict(in_bytes):
    pass


def flatten(l):
    """
    Flattens a hierarchy of nested lists into a single list containing all elements in order

    :param l: list of arbitrary types and lists
    :returns: list of arbitrary types
    """
    pass


def formatp(string, **kwargs):
    """
    Function for advanced format strings with partial formatting

    This function consumes format strings with groups enclosed in brackets. A
    group enclosed in brackets will only become part of the result if all fields
    inside the group evaluate True in boolean contexts.

    Groups can be nested. The fields in a nested group do not count as fields in
    the enclosing group, i.e. the enclosing group will evaluate to an empty
    string even if a nested group would be eligible for formatting. Nesting is
    thus equivalent to a logical or of all enclosing groups with the enclosed
    group.

    Escaped brackets, i.e. \\\\[ and \\\\] are copied verbatim to output.

    :param string: Format string
    :param kwargs: keyword arguments providing data for the format string
    :returns: Formatted string
    """
    pass


class TimeWrapper:
    """
    A wrapper that implements __format__ and __bool__ for time differences and time spans.

    :param seconds: seconds (numeric)
    :param default_format: the default format to be used if no explicit format_spec is passed to __format__

    Format string syntax:

    * %h, %m and %s are the hours, minutes and seconds without leading zeros (i.e. 0 to 59 for minutes and seconds)
    * %H, %M and %S are padded with a leading zero to two digits, i.e. 00 to 59
    * %l and %L produce hours non-padded and padded but only if hours is not zero. If the hours are zero it produces an empty string.
    * %% produces a literal %
    * %E (only valid on beginning of the string) if the time is null, don't format anything but rather produce an empty string. If the time is non-null it is removed from the string.

    The formatted string is stripped, i.e. spaces on both ends of the result are removed
    """

    class TimeTemplate(string.Template):
        delimiter = "%"
        idpattern = r"[a-zA-Z]"

    def __init__(self, seconds, default_format="%m:%S"):
        self.seconds = int(seconds)
        self.default_format = default_format

    def __bool__(self):
        """:returns: `bool(seconds)`, i.e. False if seconds == 0 and True otherwise
        """
        return bool(self.seconds)

    def __format__(self, format_spec):
        """Formats the time span given the format_spec (or the default_format).
        """
        format_spec = format_spec or self.default_format
        h = self.seconds // 3600
        m, s = divmod(self.seconds % 3600, 60)
        l = h if h else ""
        L = "%02d" % h if h else ""

        if format_spec.startswith("%E"):
            format_spec = format_spec[2:]
            if not self.seconds:
                return ""
        return self.TimeTemplate(format_spec).substitute(
            h=h, m=m, s=s,
            H="%02d" % h, M="%02d" % m, S="%02d" % s,
            l=l, L=L,
        ).strip()


def require(predicate):
    """Decorator factory for methods requiring a predicate. If the
    predicate is not fulfilled during a method call, the method call
    is skipped and None is returned.

    :param predicate: A callable returning a truth value
    :returns: Method decorator

    .. seealso::

        :py:class:`internet`

    """

    def decorator(method):
        pass

    return decorator


class internet:
    """
    Checks for internet connection by connecting to a server.

    This class exposes two configuration variables:
        * address - a tuple containing (host,port) of the server to connect to
        * check_frequency - the frequency in seconds for checking the connection

    :rtype: bool

    .. seealso::

        :py:func:`require`

    """
    address = ('google.com', 80)
    check_frequency = 1

    dns_cache = []
    last_checked = time.perf_counter() - check_frequency

    connected = False

    def __new__(cls):
        if not internet.connected:
            internet.dns_cache = internet.resolve()

        now = time.perf_counter()
        elapsed = now - internet.last_checked
        if not internet.connected or elapsed > internet.check_frequency:
            internet.last_checked = now
            internet.connected = internet.check_connection()
        return internet.connected

    @staticmethod
    def check_connection():
        pass

    @staticmethod
    def check(res):
        pass

    @staticmethod
    def resolve():
        pass


def make_graph(values, lower_limit=0.0, upper_limit=100.0, style="blocks"):
    """
    Draws a graph made of unicode characters.

    :param values: An array of values to graph.
    :param lower_limit: Minimum value for the y axis (or None for dynamic).
    :param upper_limit: Maximum value for the y axis (or None for dynamic).
    :param style: Drawing style ('blocks', 'braille-fill', 'braille-peak', or 'braille-snake').
    :returns: Bar as a string
    """
    pass


def make_vertical_bar(percentage, width=1, glyphs=None):
    """
    Draws a vertical bar made of unicode characters.

    :param percentage: A value between 0 and 100
    :param width: How many characters wide the bar should be.
    :returns: Bar as a String
    """
    pass


def make_bar(percentage):
    """
    Draws a bar made of unicode box characters.

    :param percentage: A value between 0 and 100
    :returns: Bar as a string
    """
    pass


def make_glyph(number, glyphs=" _â–�â–‚â–ƒâ–„â–…â–†â–‡â–ˆ", lower_bound=0, upper_bound=100, enable_boundary_glyphs=False):
    """
    Returns a single glyph from the list of glyphs provided relative to where
    the number is in the range (by default a percentage value is expected).

    This can be used to create an icon based representation of a value with an
    arbitrary number of glyphs (e.g. 4 different battery status glyphs for
    battery percentage level).

    :param number: The number being represented.  By default a percentage value\
    between 0 and 100 (but any range can be defined with lower_bound and\
    upper_bound).
    :param glyphs: Either a string of glyphs, or an array of strings.  Using an array\
    of strings allows for additional pango formatting to be applied such that\
    different colors could be shown for each glyph).
    :param lower_bound:  A custom lower bound value for the range.
    :param upper_bound:  A custom upper bound value for the range.
    :param enable_boundary_glyphs: Whether the first and last glyphs should be used\
    for the special case of the number being <= lower_bound or >= upper_bound\
    respectively.
    :returns: The glyph found to represent the number
    """
    pass


def user_open(url_or_command):
    """Open the specified paramater in the web browser if a URL is detected,
    othewrise pass the paramater to the shell as a subprocess. This function
    is inteded to bu used in on_leftclick/on_rightclick callbacks.

    :param url_or_command: String containing URL or command
    """
    pass


class MultiClickHandler(object):
    def __init__(self, callback_handler, timeout):
        self.callback_handler = callback_handler
        self.timeout = timeout

        self.lock = RLock()

        self._timer_id = 0
        self.timer = None
        self.button = None
        self.cb = None
        self.kwargs = None

    def set_timer(self, button, cb, **kwargs):
        pass

    def clear_timer(self):
        pass

    def _timer_function(self, timer_id):
        pass

    def check_double(self, button):
        pass


def get_module(function):
    """Function decorator for retrieving the ``self`` argument from the stack.

    Intended for use with callbacks that need access to a modules variables, for example:

    .. code:: python

        from i3pystatus import Status, get_module
        from i3pystatus.core.command import execute
        status = Status(...)
        # other modules etc.
        @get_module
        def display_ip_verbose(module):
            execute('sh -c "ip addr show dev {dev} | xmessage -file -"'.format(dev=module.interface))
        status.register("network", interface="wlan1", on_leftclick=display_ip_verbose)
    """
    pass
