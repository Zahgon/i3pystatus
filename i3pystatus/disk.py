import os

from i3pystatus import IntervalModule
from .core.util import round_dict


class Disk(IntervalModule):
    """
    Gets ``{used}``, ``{free}``, ``{avail}`` and ``{total}`` amount of bytes on the given mounted filesystem.

    These values can also be expressed as percentages with the ``{percentage_used}``, ``{percentage_free}``
    and ``{percentage_avail}`` formats.
    """

    settings = (
        "format",
        "path",
        ("divisor", "divide all byte values by this value, default is 1024**3 (gigabyte)"),
        ("display_limit", "if more space is available than this limit the module is hidden"),
        ("critical_limit", "critical space limit (see critical_color)"),
        ("critical_color", "the critical color"),
        ("color", "the common color"),
        ("round_size", "precision, None for INT"),
        ("mounted_only", "display only if path is a valid mountpoint"),
        "format_not_mounted",
        "color_not_mounted"
    )
    required = ("path",)
    color = "#FFFFFF"
    color_not_mounted = "#FFFFFF"
    critical_color = "#FF0000"
    format = "{free}/{avail}"
    format_not_mounted = None
    divisor = 1024 ** 3
    display_limit = float('Inf')
    critical_limit = 0
    round_size = 2
    mounted_only = False

    def not_mounted(self):
        pass

    def run(self):
        pass
