import subprocess

from i3pystatus import IntervalModule


class Ping(IntervalModule):
    """
    This module display the ping value between your computer and a host.

    ``switch_state`` callback can disable the Ping when desired.
    ``host`` property can be changed for set a specific host.

    .. rubric:: Available formatters

    * {ping} the ping value in milliseconds.
    """

    interval = 5

    settings = (
        "color",
        "format",
        ("color_disabled", "color when disabled"),
        ("color", "color when latency is below threshold"),
        ("color_bad", "color when latency is above threshold"),
        ("color_down", "color when ping fail"),
        ("format_disabled", "format string when disabled"),
        ("format_down", "format string when ping fail"),
        ("latency_threshold", "latency threshold in ms"),
        ("host", "host to ping")
    )

    color = "#FFFFFF"
    color_bad = "#FFFF00"
    color_down = "#FF0000"
    color_disabled = None

    disabled = False

    format = "{ping} ms"
    format_down = "down"
    format_disabled = None

    latency_threshold = 120
    host = "8.8.8.8"

    on_leftclick = "switch_state"

    def init(self):
        pass

    def switch_state(self):
        pass

    def ping_host(self):
        pass

    def run(self):
        pass
