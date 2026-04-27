from i3pystatus import IntervalModule
import soco


class Sonos(IntervalModule):
    """
    Controls and displays information from Sonos devices.

    A devices is found by IP, by name, or automatically if no IP or name is \
    supplied.

    .. rubric:: Available formatters

    * `{player_name}` â€” player name
    * `{volume}` â€” volume from 0 to 100
    * `{muted}` â€” "M" if muted, else ""
    * `{title}` â€” the title of the current song
    * `{artist}` â€” the artist of the current song
    * `{album}` â€” the album of the current song
    * `{duration}` â€” duration of the current song (%M:%S)
    * `{position}` â€” position in the current song (%M:%S)
    * `{state}` â€” Playing, Paused, Stopped

    Requires: soco (can be installed using pip)
    """

    ip = None
    name = None
    format = "{state}: {artist} - {title} [{muted}{volume:.0f}%]"
    color = "#FFFFFF"
    format_no_music = "No music"
    color_no_music = "#888888"
    format_no_connection = "No connection"
    color_no_connection = "#888888"
    hide_no_connection = False

    interval = 1

    settings = (
        ("ip", "Speaker IP address."),
        ("name", "Speaker name (used if no IP is given)."),
        ("format", "Format used when playing or paused."),
        ("color", "Color used when playing or paused."),
        ("format_no_music", "Format used when stopped."),
        ("color_no_music", "Color used when stopped."),
        ("format_no_connection", "Format used if no player is connected."),
        ("color_no_connection", "Color used if no player is connected."),
        ("hide_no_connection", "Hide output if no player is connected."),
    )

    state_text_map = {
        "PLAYING": "Playing",
        "TRANSITIONING": "Playing",
        "PAUSED_PLAYBACK": "Paused",
        "STOPPED": "Stopped",
    }

    on_leftclick = "play_pause"
    on_upscroll = "incr_vol"
    on_middleclick = "toggle_mute"
    on_downscroll = "decr_vol"
    on_doubleleftclick = "next_song"

    player = None

    def run(self):
        pass

    @property
    def output_no_connection(self):
        pass

    @property
    def group_coordinator(self):
        pass

    def play_pause(self):
        pass

    def incr_vol(self):
        pass

    def decr_vol(self):
        pass

    def toggle_mute(self):
        pass

    def next_song(self):
        pass
