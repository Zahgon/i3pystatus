import sqlite3
from datetime import datetime

import pytz
from dateutil.tz import tzlocal
from i3pystatus.calendar import CalendarEvent, CalendarBackend, formatter


class Flag:
    PRIVATE = 1
    HAS_ATTENDEES = 2
    HAS_PROPERTIES = 4
    EVENT_ALLDAY = 8
    HAS_RECURRENCE = 16
    HAS_EXCEPTIONS = 32
    HAS_ATTACHMENTS = 64
    HAS_RELATIONS = 128
    HAS_ALARMS = 256
    RECURRENCE_ID_ALLDAY = 512


class LightningCalendarEvent(CalendarEvent):
    def __init__(self, row):
        self.id = row['id']
        self.title = row['title']
        self._event_start = row['event_start']
        self._event_start_tz = row['event_start_tz']
        self._event_end = row['event_end']
        self._event_end_tz = row['event_end_tz']
        self._flags = row['flags']
        self._location = row['location'] or ''

    @property
    def recurring(self):
        pass

    @property
    def end(self):
        pass

    @property
    def start(self):
        pass

    @formatter
    def location(self):
        pass

    def _convert_date(self, microseconds_from_epoch, timezone):
        pass


class Lightning(CalendarBackend):
    """
    Backend for querying the Thunderbird's Lightning database. Requires `pytz` and `dateutil`.

    .. rubric:: Available formatters

    * `{location}` â€” Where the event occurs
    """

    settings = (
        ('database_path', 'Path to local.sqlite.'),
        ('days', 'Only show events between now and this many days in the future'),
    )

    required = ('database_path',)

    days = 7

    database_path = None

    def update(self):
        pass
