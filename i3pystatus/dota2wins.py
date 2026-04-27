from dota2py import api
from i3pystatus import IntervalModule


class Dota2wins(IntervalModule):
    """
    Displays the win/loss ratio of a given Dota account.
    Requires: dota2py
    """

    settings = (
        ("matches", "Number of recent matches to calculate"),
        ("steamid", "Steam ID or username to track"),
        ("steam_api_key", "Steam API key "
            "(http://steamcommunity.com/dev/apikey)"),
        ("good_threshold", "Win percentage (or higher) which you are happy "
            "with"),
        ("bad_threshold", "Win percentage you want to be alerted (difference "
            "between good_threshold and bad_threshold is cautious_threshold)"),
        ("interval", "Update interval (games usually last at least 20 min)."),
        ("good_color", "Color of text while win percentage is above "
            "good_threshold"),
        ("bad_color", "Color of text while win percentage is below "
            "bad_threshold"),
        ("caution_color", "Color of text while win precentage is between good "
            "and bad thresholds"),
        ("screenname", "If set to 'retrieve', requests for the users's "
            "screenname via API calls. Else, use the supplied string as the "
            "user's screename"),
        "format"
    )
    required = ("steamid", "steam_api_key")
    good_color = "#00FF00"     # green
    caution_color = "#FFFF00"  # yellow
    bad_color = "#FF0000"      # red
    good_threshold = 50
    bad_threshold = 45
    matches = 25
    interval = 1800
    screenname = 'retrieve'
    format = "{screenname} {wins}W:{losses}L {win_percent:.2f}%"

    def run(self):
        pass
