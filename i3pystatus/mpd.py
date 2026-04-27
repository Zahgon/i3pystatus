from collections import defaultdict
import socket
from os.path import basename
from math import floor

from i3pystatus import IntervalModule, formatp
from i3pystatus.core.util import TimeWrapper


class MPD(IntervalModule):
    """
    Displays various information from MPD (the music player daemon)

    .. rubric:: Available formatters (uses :ref:`formatp`)

    * `{title}` â€” (the title of the current song)
    * `{album}` â€” (the album of the current song, can be an empty string \
(e.g. for online streams))
    * `{artist}` â€” (can be empty, too)
    * `{album_artist}` â€” (can be empty)
    * `{filename}` â€” (file name with out extension and path; empty unless \
title is empty)
    * `{song_elapsed}` â€” (Position in the currently playing song, uses \
:ref:`TimeWrapper`, default is `%m:%S`)
    * `{song_length}` â€” (Length of the current song, same as song_elapsed)
    * `{pos}` â€” (Position of current song in playlist, one-based)
    * `{len}` â€” (Songs in playlist)
    * `{status}` â€” (play, pause, stop mapped through the `status` dictionary)
    * `{bitrate}` â€” (Current bitrate in kilobit/s)
    * `{volume}` â€” (Volume set in MPD)

    .. rubric:: Available callbacks

    * ``switch_playpause`` â€” Plays if paused or stopped, otherwise pauses. \
Emulates ``mpc toggle``.
    * ``stop`` â€” Stops playback. Emulates ``mpc stop``.
    * ``next_song`` â€” Goes to next track in the playlist. Emulates ``mpc \
next``.
    * ``previous_song`` â€” Goes to previous track in the playlist. Emulates \
``mpc prev``.
    * ``mpd_command`` â€” Send a command directly to MPD's socket. The command \
is the second element of the list. Documentation for available commands can \
be found at https://www.musicpd.org/doc/protocol/command_reference.html

    Example module registration with callbacks:

    ::

        status.register("mpd",
            on_leftclick="switch_playpause",
            on_rightclick=["mpd_command", "stop"],
            on_middleclick=["mpd_command", "shuffle"],
            on_upscroll=["mpd_command", "seekcur -10"],
            on_downscroll=["mpd_command", "seekcur +10"])

    Note that ``next_song`` and ``previous_song``, and their ``mpd_command`` \
equivalents, are ignored while mpd is stopped.

    """

    interval = 1

    settings = (
        ("host"),
        ("port", "MPD port. If set to 0, host will we interpreted as a Unix \
socket."),
        ("format", "formatp string"),
        ("status", "Dictionary mapping pause, play and stop to output"),
        ("color", "The color of the text"),
        ("color_map", "The mapping from state to color of the text"),
        ("max_field_len", "Defines max length for in truncate_fields defined \
fields, if truncated, ellipsis are appended as indicator. It's applied \
*before* max_len. Value of 0 disables this."),
        ("max_len", "Defines max length for the hole string, if exceeding \
fields specefied in truncate_fields are truncated equaly. If truncated, \
ellipsis are appended as indicator. It's applied *after* max_field_len. Value \
of 0 disables this."),
        ("time_format", "format string for 'pos' and 'len' fields"),
        ("truncate_fields", "fields that will be truncated if exceeding \
max_field_len or max_len."),
        ("hide_inactive", "Hides status information when MPD is not running"),
        ("password", "A password for access to MPD. (This is sent in \
cleartext to the server.)"),
    )

    host = "localhost"
    port = 6600
    password = None
    s = None
    format = "{title} {status}"
    status = {
        "pause": "â–·",
        "play": "â–¶",
        "stop": "â—¾",
    }
    color = "#FFFFFF"
    color_map = {}
    max_field_len = 25
    max_len = 100
    time_format = "%m:%S"
    truncate_fields = ("title", "album", "artist", "album_artist")
    hide_inactive = False
    on_leftclick = "switch_playpause"
    on_rightclick = "next_song"
    on_upscroll = on_rightclick
    on_downscroll = "previous_song"

    def _mpd_command(self, sock, command):
        pass

    def run(self):
        pass

    def switch_playpause(self):
        pass

    def stop(self):
        pass

    def next_song(self):
        pass

    def previous_song(self):
        pass

    def mpd_command(self, command):
        pass
