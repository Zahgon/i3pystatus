from i3pystatus import IntervalModule
from urllib.request import urlopen
from urllib.error import HTTPError, URLError

import json
import webbrowser


class sabnzbd(IntervalModule):
    """
    Displays the current status of SABnzbd.

    A leftclick pauses/resumes downloading.
    A rightclick opens SABnzbd inside a browser.

    .. rubric:: Available formatters

    * All the first-level parameters from
      https://sabnzbd.org/wiki/advanced/api#queue
      (e.g. status, speed, timeleft, spaceleft, eta ...)
    """

    format = "{speed} - {timeleft}"
    format_paused = "{status}"
    host = "127.0.0.1"
    port = 8080
    api_key = ""
    url = "http://{host}:{port}/sabnzbd/api?output=json&apikey={api_key}"
    color = "#FFFFFF"
    color_paused = "#FF0000"
    color_downloading = "#00FF00"

    settings = (
        ("format", "format string used for output"),
        ("format_paused", "format string used if SABnzbd is paused"),
        ("host", "address of the server running SABnzbd"),
        ("port", "port that SABnzbd is running on"),
        ("api_key", "api key of SABnzbd"),
        ("color", "default color"),
        ("color_paused", "color if SABnzbd is paused"),
        ("color_downloading", "color if downloading"),
    )

    on_leftclick = "pause_resume"
    on_rightclick = "open_browser"

    def init(self):
        """Initialize the URL used to connect to SABnzbd."""
        pass

    def run(self):
        """Connect to SABnzbd and get the data."""
        pass

    def pause_resume(self):
        """Toggle between pausing or resuming downloading."""
        pass

    def is_paused(self):
        """Return True if downloads are currently paused."""
        pass

    def is_downloading(self):
        """Return True if downloads are running."""
        pass

    def open_browser(self):
        """Open the URL of SABnzbd inside a browser."""
        pass
