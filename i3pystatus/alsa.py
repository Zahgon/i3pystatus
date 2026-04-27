from alsaaudio import Mixer, ALSAAudioError
from math import exp, log, log10, ceil, floor

from i3pystatus import IntervalModule


class ALSA(IntervalModule):
    """
    Shows volume of ALSA mixer. You can also use this for inputs, btw.

    Requires pyalsaaudio

    .. rubric:: Available formatters

    * `{volume}` â€” the current volume in percent
    * `{muted}` â€” the value of one of the `muted` or `unmuted` settings
    * `{card}` â€” the associated soundcard
    * `{mixer}` â€” the associated ALSA mixer
    """

    interval = 1

    settings = (
        "format",
        ("format_muted", "optional format string to use when muted"),
        ("mixer", "ALSA mixer"),
        ("mixer_id", "ALSA mixer id"),
        ("card", "ALSA sound card"),
        ("increment", "integer percentage of max volume to in/decrement volume on mousewheel"),
        "muted", "unmuted",
        "color_muted", "color",
        "channel",
        ("map_volume", "volume display/setting as in AlsaMixer. increment option is ignored then.")
    )

    muted = "M"
    unmuted = ""
    color_muted = "#AAAAAA"
    color = "#FFFFFF"
    format = "â™ª: {volume}"
    format_muted = None
    mixer = "Master"
    mixer_id = 0
    card = -1
    channel = 0
    increment = 5

    map_volume = False

    alsamixer = None
    has_mute = True

    on_upscroll = "increase_volume"
    on_downscroll = "decrease_volume"
    on_leftclick = "switch_mute"
    on_rightclick = on_leftclick

    def init(self):
        pass

    def create_mixer(self):
        pass

    def run(self):
        pass

    def switch_mute(self):
        pass

    def get_cur_volume(self):
        pass

    def get_new_volume(self, direction):
        pass

    def increase_volume(self, delta=None):
        pass

    def decrease_volume(self, delta=None):
        pass

    def get_db(self):
        pass

    def map_db(self, value, dbMin, dbMax, volMin, volMax):
        pass

    def exp10(self, x):
        pass
