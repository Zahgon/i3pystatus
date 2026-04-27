from i3pystatus import IntervalModule
from json import loads
from dateutil.parser import parse
from dateutil.relativedelta import relativedelta
from datetime import datetime, timezone
import subprocess


class Timewarrior(IntervalModule):
    """
    Show current Timewarrior tracking
    Requires `json` `dateutil`

    Formaters:

    * `{tags}`  â€” contains tags of current track
    * `{start}` - contains start of track
    * `{duration}` â€” contains time of current track
    """

    format = '{duration}'
    duration_format = '{years}y{months}m{days}d{hours}h{minutes}m{seconds}s'
    enable_stop = True
    enable_continue = True
    color_running = '#00FF00'
    color_stopped = '#F00000'
    on_rightclick = 'stop_or_continue'
    track = None

    settings = (
        ('format', 'format string'),
        ('duration_format', 'duration format string'),
        ('enable_stop', 'Allow right click to stop tracking'),
        ('enable_continue', 'ALlow right click to continue tracking'),
        ('color_running', '#00FF00'),
        ('color_stopped', '#F00000'),
    )

    def loadTrack(self):
        pass

    def stop_or_continue(self):
        pass

    def run(self):
        pass
