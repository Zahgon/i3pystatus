from collections import defaultdict
from string import Formatter
import re

from i3pystatus import IntervalModule
from i3pystatus.core.color import ColorRangeModule

try:
    from natsort import natsorted as sorted
except ImportError:
    pass


class CpuUsage(IntervalModule, ColorRangeModule):
    """
    Shows CPU usage.
    The first output will be inacurate.

    Linux only
    Requires the PyPI package 'colour'.

    .. rubric:: Available formatters

    * `{usage}`      â€” usage average of all cores
    * `{usage_cpu*}` â€” usage of one specific core. replace "*" by core number starting at 0
    * `{usage_all}`  â€” usage of all cores separate. usess natsort when available(relevant for more than 10 cores)

    """

    format = "{usage:02}%"
    format_all = "{core}:{usage:02}%"
    exclude_average = False
    interval = 1
    color = '#FFFFFF'
    dynamic_color = False
    upper_limit = 100
    settings = (
        ("format", "format string."),
        ("format_all", ("format string used for {usage_all} per core. "
                        "Available formaters are {core} and {usage}. ")),
        ("exclude_average", ("If True usage average of all cores will "
                             "not be in format_all.")),
        ("color", "HTML color code #RRGGBB"),
        ("dynamic_color", "Set color dynamically based on CPU usage. Note: this overrides color_up"),
        ("start_color", "Hex or English name for start of color range, eg '#00FF00' or 'green'"),
        ("end_color", "Hex or English name for end of color range, eg '#FF0000' or 'red'")
    )

    def init(self):
        pass

    def get_cpu_timings(self):
        """
        reads and parses /proc/stat
        returns dictionary with all available cores including global average
        """
        pass

    def calculate_usage(self, cpu, total, busy):
        """
        calculates usage
        """
        pass

    def gen_format_all(self, usage):
        """
        generates string for format all
        """
        pass

    def get_usage(self):
        """
        parses /proc/stat and calcualtes total and busy time
        (more specific USER_HZ see man 5 proc for further informations )
        """
        pass

    def run(self):
        pass
