import subprocess

from i3pystatus import IntervalModule


class Keyboard_locks(IntervalModule):
    """
    Shows the status of CAPS LOCK, NUM LOCK and SCROLL LOCK

    .. rubric:: Available formatters

    * `{caps}` â€” the current status of CAPS LOCK
    * `{num}` â€” the current status of NUM LOCK
    * `{scroll}` â€” the current status of SCROLL LOCK
    """

    interval = 1

    settings = (
        ("format", "Format string"),
        ("caps_on", "String to show in {caps} when CAPS LOCK is on"),
        ("caps_off", "String to show in {caps} when CAPS LOCK is off"),
        ("num_on", "String to show in {num} when NUM LOCK is on"),
        ("num_off", "String to show in {num} when NUM LOCK is off"),
        ("scroll_on", "String to show in {scroll} when SCROLL LOCK is on"),
        ("scroll_off", "String to show in {scroll} when SCROLL LOCK is off"),
        "color"
    )

    format = "{caps} {num} {scroll}"
    caps_on = "CAP"
    caps_off = "___"
    num_on = "NUM"
    num_off = "___"
    scroll_on = "SCR"
    scroll_off = "___"
    color = "#FFFFFF"
    data = {}

    def get_status(self):
        pass

    def run(self):
        pass
