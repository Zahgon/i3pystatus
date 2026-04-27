from calendar import Calendar
from datetime import date, timedelta

from i3pystatus import IntervalModule


class WeekCal(IntervalModule):
    """
    Displays the days of the current week as they would be represented on a calendar sheet,
    with the current day highlighted.
    By default, the current day of week is displayed in the front, and the month and year are
    displayed in the back.

    Example: ``Sat  16 17 18 19 20[21]22  May 2016``
    """

    settings = (
        ("startofweek", "First day of the week (0 = Monday, 6 = Sunday), defaults to 0."),
        ("prefixformat", "Prefix in strftime-format"),
        ("suffixformat", "Suffix in strftime-format"),
        ("todayhighlight", "Characters to highlight today's date"),
    )
    startofweek = 0
    interval = 30
    prefixformat = "%a"
    suffixformat = "%b %Y"
    todayhighlight = ("[", "]")

    def __init__(self, *args, **kwargs):
        IntervalModule.__init__(self, *args, **kwargs)
        self.cal = Calendar(self.startofweek)

    def run(self):
        pass
