from datetime import date, timedelta

import khal
import khal.cli
import khal.settings
from i3pystatus.calendar import CalendarBackend, CalendarEvent, formatter


class KhalEvent(CalendarEvent):
    def __init__(self, khal_event):
        self.id = khal_event.uid
        self.start = khal_event.start_local
        self.end = khal_event.end_local
        self.title = khal_event.summary
        self.recurring = khal_event.recurring
        self._calendar = khal_event.calendar

    @formatter
    def calendar(self):
        pass


class Khal(CalendarBackend):
    """
    Backend for Khal. Requires `khal` to be installed.

    .. rubric:: Available formatters
        * `{calendar}` â€” Calendar event is from.
    """

    settings = (
        ('config_path', 'Path to your khal.conf'),
        ('calendars', 'Restrict to these calendars pass as a list)'),
        ('days', 'Check for the next X days'),
    )

    days = 7

    config_path = None
    calendars = None

    def init(self):
        pass

    def open_connection(self):
        pass

    def update(self):
        pass
