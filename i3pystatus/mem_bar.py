from i3pystatus import IntervalModule
from psutil import virtual_memory
from i3pystatus.core.color import ColorRangeModule
from i3pystatus.core.util import make_bar, make_glyph


class MemBar(IntervalModule, ColorRangeModule):
    """
    Shows memory load as a bar.

    .. rubric:: Available formatters

    * {used_mem_bar}

    Requires psutil and colour (from PyPI)
    """

    format = "{used_mem_bar}"
    color = "#00FF00"
    warn_color = "#FFFF00"
    alert_color = "#FF0000"
    warn_percentage = 50
    alert_percentage = 80
    multi_colors = False

    bar_type = "bar"

    def init(self):
        pass

    settings = (
        ("format", "format string used for output."),
        ("warn_percentage", "minimal percentage for warn state"),
        ("alert_percentage", "minimal percentage for alert state"),
        ("color", "standard color"),
        ("warn_color",
         "defines the color used when warn percentage is exceeded"),
        ("alert_color",
         "defines the color used when alert percentage is exceeded"),
        ("multi_colors", "whether to use range of colors from 'color' to 'alert_color' based on memory usage."),
        ("bar_type", "choose from 'glyph' or 'bar'")
    )

    def run(self):
        pass
