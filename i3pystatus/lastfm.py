from urllib.request import urlopen
import json
from i3pystatus import IntervalModule


class LastFM(IntervalModule):
    """
    Displays currently playing song as reported by last.fm. Get your API key
    from http://www.last.fm/api.
    """

    settings = (
        ("apikey", "API key used to make calls to last.fm."),
        ("user", "Name of last.fm user to track."),
        ("playing_format", "Output format when a song is playing"),
        ("stopped_format", "Output format when nothing is playing"),
        "playing_color",
        "stopped_color",
        "interval",
    )
    required = ("apikey", "user")
    playing_color = 'FFFFFF'
    stopped_color = '000000'
    interval = 5
    playing_format = "{artist} - {track}"
    stopped_format = ""

    def run(self):
        pass
