import json

from urllib.request import urlopen
from datetime import datetime

from i3pystatus import IntervalModule
from i3pystatus.core.util import internet, require


class SpaceAPI(IntervalModule):
    """
    Show if a hackerspace is open

    .. rubric:: Available formatters

    * {state}
    * {message}
    * {lastchange}
    """

    data = {}
    format = "S: {state}"
    color_open = "#00FF00"
    color_closed = "#FF0000"
    interval = 10

    settings = (
        ("url", "spaceapi endpoint"),
        ("format", "format string used for output."),
        ("color_open", "color if hackerspace is opened"),
        ("color_closed", "color if hackerspace is closed"),
        ("interval", "update interval")
    )

    required = ('url', )
    url = None

    @require(internet)
    def run(self):
        pass
