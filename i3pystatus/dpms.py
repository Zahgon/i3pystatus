from i3pystatus import IntervalModule
from i3pystatus.core.command import run_through_shell


class DPMS(IntervalModule):
    """
    Shows and toggles status of DPMS which prevents screen from blanking.

    .. rubric:: Available formatters

    * `{status}` â€” the current status of DPMS

    @author Georg Sieber <g.sieber AT gmail.com>
    """

    interval = 5

    settings = (
        "format",
        "format_disabled",
        "color",
        "color_disabled",
    )

    color_disabled = "#AAAAAA"
    color = "#FFFFFF"
    format = "DPMS: {status}"
    format_disabled = "DPMS: {status}"

    on_leftclick = "toggle_dpms"

    status = False

    def run(self):

        pass

    def toggle_dpms(self):
        pass
