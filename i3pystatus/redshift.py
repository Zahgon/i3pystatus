import os
import signal
import threading
from subprocess import Popen, PIPE

from i3pystatus import IntervalModule, formatp


class RedshiftController(threading.Thread):

    def __init__(self, args=[]):
        """Initialize controller and start child process

        The parameter args is a list of command line arguments to pass on to
        the child process. The "-v" argument is automatically added."""

        threading.Thread.__init__(self)

        # Initialize state variables
        self._inhibited = False
        self._temperature = 0
        self._period = 'Unknown'
        self._location = (0.0, 0.0)
        self._brightness = 0.0
        self._pid = None

        cmd = ["redshift"] + args
        if "-v" not in cmd:
            cmd += ["-v"]

        env = os.environ.copy()
        env['LANG'] = env['LANGUAGE'] = env['LC_ALL'] = env['LC_MESSAGES'] = 'C'

        self._params = {
            "args": cmd,
            "env": env,
            "bufsize": 1,
            "stdout": PIPE,
            "universal_newlines": True,
        }

    def parse_output(self, line):
        """Convert output to key value pairs"""
        pass

    def update_value(self, key, value):
        """Parse key value pairs to update their values"""
        pass

    @property
    def inhibited(self):
        """Current inhibition state"""
        pass

    @property
    def temperature(self):
        """Current screen temperature"""
        pass

    @property
    def period(self):
        """Current period of day"""
        pass

    @property
    def location(self):
        """Current location"""
        pass

    @property
    def brightness(self):
        """Current brightness"""
        pass

    def set_inhibit(self, inhibit):
        """Set inhibition state"""
        pass

    def run(self):
        pass


class Redshift(IntervalModule):
    """
    Show status and control redshift - http://jonls.dk/redshift/.

    This module runs an instance of redshift by itself, since it needs to parse
    its output, so you should remove redshift/redshift-gtk from your i3 config
    before using this module.

    Requires `redshift` installed.

    .. rubric:: Available formatters

    * `{inhibit}` â€” show if redshift is currently On or Off (using `toggle_inhibit` callback)
    * `{latitude}` â€” location latitude
    * `{longitude}` â€” location longitude
    * `{period}` â€” current period (Day or Night)
    * `{temperature}` â€” current screen temperature in Kelvin scale (K)

    """
    settings = (
        ("color", "Text color"),
        ("error_color", "Text color when an error occurs"),
        "format",
        ("format_inhibit",
            "List of 2 strings for `{inhibit}`, the first is shown when Redshift is On and the second is shown when Off"),
        ("redshift_parameters", "List of parameters to pass to redshift binary"),
    )

    color = "#ffffff"
    error_color = "#ff0000"
    format = "{inhibit} {temperature}K"
    format_inhibit = ["On", "Off"]
    on_leftclick = "toggle_inhibit"
    redshift_parameters = []

    def init(self):
        pass

    def update_values(self):
        pass

    def toggle_inhibit(self):
        """Enable/disable redshift"""
        pass

    def run(self):
        pass
