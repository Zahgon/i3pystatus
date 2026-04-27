from i3pystatus import IntervalModule
from psutil import swap_memory
from .core.util import round_dict


class Swap(IntervalModule):
    """
    Shows swap load

    .. rubric:: Available formatters

    * {free}
    * {percent_used}
    * {used}
    * {total}

    Requires psutil (from PyPI)
    """

    format = "{free} MiB"
    format_no_swap = "No swap"
    hide_if_empty = False
    divisor = 1024 ** 2
    color = "#00FF00"
    warn_color = "#FFFF00"
    alert_color = "#FF0000"
    color_no_swap = "#FFFFFF"
    warn_percentage = 50
    alert_percentage = 80
    round_size = 1

    settings = (
        ("format", "format string used for output."),
        ("format_no_swap",
         "format string used when no swap is enabled, "
         "set to None to use default format"),
        ("hide_if_empty", "hide swap block when swap is not used"),
        ("divisor",
         "divide all byte values by this value, default is 1024**2 (megabytes)"),
        ("warn_percentage", "minimal percentage for warn state"),
        ("alert_percentage", "minimal percentage for alert state"),
        ("color", "standard color"),
        ("warn_color",
         "defines the color used when warn percentage is exceeded"),
        ("alert_color",
         "defines the color used when alert percentage is exceeded"),
        ("color_no_swap",
         "defines the color used when no swap is enabled, "
         "set to None to use default color"),
        ("round_size", "defines number of digits in round"),
    )

    def run(self):
        pass
