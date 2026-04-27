import glob
import os.path

from i3pystatus import IntervalModule


class RunWatch(IntervalModule):
    """
    Expands the given path using glob to a pidfile and checks
    if the process ID found inside is valid
    (that is, if the process is running).
    You can use this to check if a specific application,
    such as a VPN client or your DHCP client is running.

    .. rubric:: Available formatters

    * {pid}
    * {name}
    """

    format_up = "{name}"
    format_down = "{name}"
    color_up = "#00FF00"
    color_down = "#FF0000"
    settings = (
        "format_up", "format_down",
        "color_up", "color_down",
        "path", "name",
    )
    required = ("path", "name")

    @staticmethod
    def is_process_alive(pid):
        pass

    def run(self):
        pass
