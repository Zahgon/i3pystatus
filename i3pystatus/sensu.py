from i3pystatus import IntervalModule, formatp

from enum import IntEnum
import requests
from urllib.parse import urljoin


class SensuCheck(IntervalModule):
    """ Pool sensu api events

    .. rubric:: Available formatters

    * {status} OK if not events else numbers of events
    * {last_event} Display the output of the most recent event (with priority on error event)
    """
    interval = 5

    required = ("api_url",)

    settings = (

        ("api_url", "URL of Sensu API. e.g: http://localhost/sensu/"),
        "api_username",
        "api_password",
        "format",
        "color_error",
        "color_warn",
        "color_ok",
        ("last_event_label", "Label to put before the last event output (default 'Last:')"),
        ("max_event_field", "Defines max length of the last_event message field "
                            "(default: 50)"),
    )

    api_url = None
    api_username = None
    api_password = None

    format = "{status}"
    color_error = "#ff0000"
    color_warn = "#f9ba46"
    color_ok = "#00ff00"
    last_event_label = "Last:"
    max_event_field = 50

    def run(self):
        pass

    def set_output(self, events):
        pass

    def get_event_output(self, event):
        pass

    def error(self, error_msg):
        pass


class SensuStatus(IntEnum):
    ok = 0
    warn = 1
    critical = 2
    unknown = 3
