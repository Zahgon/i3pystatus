import xml.etree.ElementTree as ET
from i3pystatus import IntervalModule
from urllib.request import urlopen


class Plexstatus(IntervalModule):
    """
    Displays what is currently being streamed from your Plex Media Server.

    If you dont have an apikey you will need to follow this
        https://support.plex.tv/hc/en-us/articles/204059436-Finding-your-account-token-X-Plex-Token

    .. rubric:: Formatters

    * `{title}`       - title currently being streamed
    * `{platform}`    - plex recognised platform of the streamer
    * `{product}`     - plex product name on the streamer (Plex Web, Plex Media Player)
    * `{address}`     - address of the streamer
    * `{streamer_os}` - operating system on the streaming device
    """

    settings = (
        "format",
        "color",
        ("apikey", "Your Plex API authentication key"),
        ("address", "Hostname or IP address of the Plex Media Server"),
        ("port", "Port which Plex Media Server is running on"),
        ("interval", "Update interval"),
        ("stream_divider", "divider between stream info when multiple streams are active"),
        ("format_no_streams", "String that is shown if nothing is being streamed"),
    )
    required = ("apikey", "address")
    color = "#00FF00"  # green
    no_stream_color = "#FF0000"  # red
    port = 32400
    interval = 120
    format_no_streams = None
    format = "{platform}: {title}"
    stream_divider = '-'

    def run(self):
        pass
