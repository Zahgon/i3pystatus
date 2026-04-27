# -*- coding: utf-8 -*-
from threading import Thread
from i3pystatus import Module
import i3ipc


class Scratchpad(Module):
    """
    Display the amount of windows and indicate urgency hints on scratchpad (async).

    fork from scratchpad_async of py3status by cornerman

    Requires the PyPI package `i3ipc`.

    .. rubric:: Available formaters

    * `{number}`      â€” amount of windows on scratchpad

    @author jok
    @license BSD
    """

    settings = (
        ("format", "format string."),
        ("always_show", "whether the indicator should be shown if there are"
         " no scratchpad windows"),
        ("color_urgent", "color of urgent"),
        ("color", "text color"),
    )

    format = u"{number} âŒ«"
    always_show = True
    color_urgent = "#900000"
    color = "#FFFFFF"

    def init(self):
        pass

    def update_scratchpad_counter(self, conn, *args):
        pass

    def _listen(self):
        pass
