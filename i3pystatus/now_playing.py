from os.path import basename

import dbus

from i3pystatus import IntervalModule, formatp
from i3pystatus.core.util import TimeWrapper


class Dbus:
    obj_dbus = "org.freedesktop.DBus"
    path_dbus = "/org/freedesktop/DBus"
    obj_player = "org.mpris.MediaPlayer2"
    path_player = "/org/mpris/MediaPlayer2"
    intf_props = obj_dbus + ".Properties"
    intf_player = obj_player + ".Player"


class NoPlayerException(Exception):
    pass


class NowPlaying(IntervalModule):
    """
    Shows currently playing track information. Supports media players that \
conform to the Media Player Remote Interfacing Specification.

    * Requires ``python-dbus`` from your distro package manager, or \
``dbus-python`` from PyPI.

    Left click on the module to play/pause, and right click to go to the next \
track.

    .. rubric:: Available formatters (uses :ref:`formatp`)

    * `{title}` â€” (the title of the current song)
    * `{album}` â€” (the album of the current song, can be an empty string \
(e.g. for online streams))
    * `{artist}` â€” (can be empty, too)
    * `{filename}` â€” (file name with out extension and path; empty unless \
title is empty)
    * `{song_elapsed}` â€” (position in the currently playing song, uses \
:ref:`TimeWrapper`, default is `%m:%S`)
    * `{song_length}` â€” (length of the current song, same as song_elapsed)
    * `{status}` â€” (play, pause, stop mapped through the `status` dictionary)
    * `{volume}` â€” (volume)

    .. rubric:: Available callbacks

    * ``playpause`` â€” Plays if paused or stopped, otherwise pauses.
    * ``next_song`` â€” Goes to next track in the playlist.
    * ``player_command`` â€” Invoke a command with the `MediaPlayer2.Player` \
interface. The method name and its arguments are appended as list elements.
    * ``player_prop`` â€” Get or set a property of the `MediaPlayer2.Player` \
interface. Append the property name to get, or the name and a value to set.

    `MediaPlayer2.Player` methods and properties are documented at \
https://specifications.freedesktop.org/mpris-spec/latest/Player_Interface.html

    Your player may not support the full interface.

    Example module registration with callbacks:

    ::

        status.register("now_playing",
            on_leftclick=["player_command", "PlayPause"],
            on_rightclick=["player_command", "Stop"],
            on_middleclick=["player_prop", "Shuffle", True],
            on_upscroll=["player_command", "Seek", -10000000],
            on_downscroll=["player_command", "Seek", +10000000])

    """

    interval = 1

    settings = (
        ("player", "Player name. If not set, compatible players will be \
                    detected automatically."),
        ("status", "Dictionary mapping pause, play and stop to output text"),
        ("format", "formatp string"),
        ("color", "Text color"),
        ("format_no_player", "Text to show if no player is detected"),
        ("color_no_player", "Text color when no player is detected"),
        ("hide_no_player", "Hide output if no player is detected"),
    )

    hide_no_player = True
    format_no_player = "No Player"
    color_no_player = "#ffffff"

    format = "{title} {status}"
    color = "#ffffff"
    status = {
        "pause": "â–·",
        "play": "â–¶",
        "stop": "â—¾",
    }
    statusmap = {
        "Playing": "play",
        "Paused": "pause",
        "Stopped": "stop",
    }

    on_leftclick = "playpause"
    on_rightclick = "next_song"
    on_upscroll = 'volume_up'
    on_downscroll = 'volume_down'

    player = None
    old_player = None

    def find_player(self):
        pass

    def get_player(self):
        pass

    def run(self):
        pass

    def playpause(self):
        pass

    def next_song(self):
        pass

    def volume_up(self):
        pass

    def volume_down(self):
        pass

    @property
    def volume(self):
        pass

    def player_command(self, command, *args):
        pass

    def get_player_prop(self, name, default=None):
        pass

    def set_player_prop(self, name, value):
        pass

    def player_prop(self, name, value=None):
        pass
