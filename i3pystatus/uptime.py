
from i3pystatus import IntervalModule, formatp


class Uptime(IntervalModule):
    """
    Outputs Uptime

    .. rubric:: Available formatters

    * `{days}` - uptime in days
    * `{hours}` - rest of uptime in hours
    * `{mins}` - rest of uptime in minutes
    * `{secs}` - rest of uptime in seconds
    * `{uptime}` - deprecated: equals '`{hours}:{mins}`'
    """

    settings = (
        ("format", "Format string"),
        ("color", "String color"),
        ("alert", "If you want the string to change color"),
        ("seconds_alert", "How many seconds necessary to start the alert"),
        ("color_alert", "Alert color"),
    )

    file = "/proc/uptime"
    format = "up {hours}:{mins}"
    color = "#ffffff"
    alert = False
    seconds_alert = 60 * 60 * 24 * 30  # 30 days
    color_alert = "#ff0000"

    def run(self):
        pass
