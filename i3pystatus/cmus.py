import os

from i3pystatus import formatp
from i3pystatus import IntervalModule
from i3pystatus.core.command import run_through_shell
from i3pystatus.core.util import TimeWrapper


def _extract_artist_title(input):
    pass


class Cmus(IntervalModule):
    """
    Gets the status and current song info using cmus-remote

    .. rubric:: Available formatters

    * `{status}` â€” current status icon (paused/playing/stopped)
    * `{song_elapsed}` â€” song elapsed time (mm:ss format)
    * `{song_length}` â€” total song duration (mm:ss format)
    * `{artist}` â€” artist
    * `{title}` â€” title
    * `{album}` â€” album
    * `{tracknumber}` â€” tracknumber
    * `{file}` â€” file or url name
    * `{stream}` â€” song name from stream
    * `{bitrate}` â€” bitrate
    """

    settings = (
        ('format', 'formatp string'),
        ('format_not_running', 'Text to show if cmus is not running'),
        ('color', 'The color of the text'),
        ('color_not_running', 'The color of the text, when cmus is not running'),
        ('status', 'Dictionary mapping status to output'),
    )

    color = '#ffffff'
    color_not_running = '#ffffff'
    format = '{status} {song_elapsed}/{song_length} {artist} - {title}'
    format_not_running = 'Not running'
    interval = 1
    status = {
        'paused': 'â–·',
        'playing': 'â–¶',
        'stopped': 'â—¾',
    }

    on_leftclick = 'playpause'
    on_rightclick = 'next_song'
    on_upscroll = 'next_song'
    on_downscroll = 'previous_song'

    def _cmus_command(self, command):
        pass

    def _query_cmus(self):
        pass

    def run(self):
        pass

    def playpause(self):
        pass

    def next_song(self):
        pass

    def previous_song(self):
        pass
