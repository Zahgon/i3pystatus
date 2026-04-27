# -*- coding: utf-8 -*-
from i3pystatus import Module
from threading import Thread
import i3ipc


class WindowTitle(Module):
    """
    Display the current window title with async update.
    Uses asynchronous update via i3 IPC events.
    Provides instant title update only when it required.

    fork from window_tile_async of py3status by Anon1234 https://github.com/Anon1234

    Requires the PyPI package `i3ipc`.

    .. rubric:: Available formaters

    * `{title}`      â€” title of current focused window
    * `{class_name}` - name of application class

    @author jok
    @license BSD
    """

    settings = (
        ("format", "format string."),
        ("always_show", "do not hide the title when it can be already visible"),
        ("empty_title", "string that will be shown instead of the title when the title is hidden"),
        ("max_width", "maximum width of title"),
        ("color", "text color"),
    )

    format = "{title}"
    always_show = False
    empty_title = ""
    max_width = 79
    color = "#FFFFFF"

    def init(self):
        pass

    def get_title(self, conn):
        pass

    def update_title(self, conn, e):
        # catch only focused window title updates
        pass

    def clear_title(self, *args):
        pass

    def update_display(self):
        pass

    def _loop(self):
        pass
