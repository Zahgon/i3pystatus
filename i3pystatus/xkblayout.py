import subprocess
from itertools import zip_longest

from i3pystatus import IntervalModule
from xkbgroup import XKeyboard


class Xkblayout(IntervalModule):
    """Displays and changes current keyboard layout.

    ``change_layout`` callback finds the current layout in the
    ``layouts`` setting and enables the layout following it. If the
    current layout is not in the ``layouts`` setting the first layout
    is enabled.

    ``layouts`` can be stated with or without variants,
    e.g.: ``status.register("xkblayout", layouts=["de neo", "de"])``

    Requires xkbgroup (from PyPI)

    .. rubric:: Available formatters

    * `{num}` â€” current group number
    * `{name}` â€” current group name
    * `{symbol}` â€” current group symbol
    * `{variant}` â€” current group variant
    * `{count}` â€” number of all groups
    * `{names}` â€” names of all groups
    * `{symbols}` â€” symbols of all groups
    * `{variants}` â€” variants of all groups
    """

    interval = 1
    color = "#FFFFFF"
    format = "\u2328 {symbol}"
    layouts = []
    uppercase = True
    settings = (
        ("color", "RGB hexadecimal color code specifuer, defaults to #FFFFFF"),
        ("format", "Format string"),
        ("layouts", "List of layouts"),
        ("uppercase", "Flag for uppercase output"),
    )

    on_leftclick = ["change_layout", 1]
    on_upscroll = ["change_layout", 1]
    on_downscroll = ["change_layout", -1]

    def init(self):
        pass

    def set_layouts(self, layouts):
        pass

    def change_layout(self, increment=1):
        pass

    def run(self):
        pass
