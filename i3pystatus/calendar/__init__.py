import inspect
import re
import threading
from abc import abstractmethod
from datetime import datetime, timedelta

from i3pystatus import IntervalModule, formatp, SettingsBase
from i3pystatus.core.color import ColorRangeModule
from i3pystatus.core.desktop import DesktopNotification

humanize_imported = False
try:
    import humanize
    humanize_imported = True
except ImportError:
    pass


def strip_microseconds(delta):
    pass


def formatter(func):
    """ Decorator to mark a CalendarEvent method as a formatter. """
    pass


class CalendarEvent:
    """
    Simple class representing an Event. The attributes title, start, end and recurring are required as
    these will be used for the formatters. The id attribute is used to uniquely identify the event.

    If a backend wishes to provide extra formatters to the user, this can be done by adding additional
    methods and decorating them with the @formatter decorator. See the LightningCalendarEvent from the
    lightning module for an example of this.
    """

    # Unique identifier for this event
    id = None

    # The title of this event
    title = None

    # Datetime object representing when this event begins
    start = None

    # Datetime object representing when this event ends
    end = None

    # Whether or not this event is a recurring event
    recurring = False

    def formatters(self):
        """
        Build a dictionary containing all those key/value pairs that will be exposed to the user via formatters.
        """
        pass

    @property
    def time_remaining(self):
        pass

    @property
    def humanize_time_remaining(self):
        pass

    def __str__(self):
        return "{}(title='{}', start={}, end={}, recurring={})" \
            .format(type(self).__name__,
                    self.title,
                    repr(self.start),
                    repr(self.end),
                    self.recurring)


class CalendarBackend(SettingsBase):
    """
    Base class for calendar backend. Subclasses should implement update and populate the events list.

    Optionally, subclasses can override on_click to perform actions on the current event when clicked.
    """

    def init(self):
        pass

    @abstractmethod
    def update(self):
        """ Subclasses should implement this method and populate the events list with CalendarEvents."""

    def on_click(self, event):
        """ Override this method to do more interesting things with the event. """
        pass

    def __iter__(self):
        return iter(self.events)

    def __len__(self):
        return len(self.events)


class Calendar(IntervalModule, ColorRangeModule):
    """
    Generic calendar module. Requires the PyPI package ``colour``.

    .. rubric:: Available formatters

    * {title} - the title or summary of the event
    * {remaining_time} - how long until this event is due
    * {humanize_remaining} - how long until this event is due in human readable format

    Additional formatters may be provided by the backend, consult their documentation for details.

    .. note:: Optionally requires `humanize` to display time in human readable format.
    """

    settings = (
        ('format', 'Format string to display in the bar'),
        ('backend', 'Backend to use for collecting calendar events'),
        ('skip_recurring', 'Whether or not to skip recurring events'),
        ('skip_all_day', 'Whether or not to skip all day events'),
        ('skip_regex', 'Skip events with titles that match this regex'),
        ('update_interval', "How often in seconds to call the backend's update method"),
        ('urgent_seconds', "When within this many seconds of the event, set the urgent flag"),
        ('urgent_blink', 'Whether or not to blink when within urgent_seconds of the event'),
        ('dynamic_color', 'Whether or not to change color as the event approaches'),
        'color'
    )

    required = ('backend',)

    skip_recurring = False
    skip_all_day = False
    skip_regex = None
    interval = 1
    backend = None
    update_interval = 600
    dynamic_color = True
    urgent_seconds = 300
    urgent_blink = False
    color = None

    current_event = None
    urgent_acknowledged = False

    format = "{title} - {remaining}"

    on_rightclick = 'handle_click'
    on_leftclick = 'acknowledge'

    def init(self):
        pass

    def update_thread(self):
        pass

    def refresh_events(self):
        pass

    def run(self):
        pass

    def handle_click(self):
        pass

    def get_color(self):
        pass

    def is_urgent(self):
        """
        Determine whether or not to set the urgent flag. If urgent_blink is set, toggles urgent flag
        on and off every second.
        """
        pass

    def acknowledge(self):
        pass
