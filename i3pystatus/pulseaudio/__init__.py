import re
import subprocess

from i3pystatus import Module
from i3pystatus.core.color import ColorRangeModule
from i3pystatus.core.util import make_vertical_bar, make_bar
from .pulse import *


class PulseAudio(Module, ColorRangeModule):
    """
    Shows volume of default PulseAudio sink (output).

    - Requires amixer for toggling mute and incrementing/decrementing volume on scroll.
    - Depends on the PyPI colour module - https://pypi.python.org/pypi/colour/0.0.5

    .. rubric:: Example configuration

    The example configuration below uses only unicode to display the volume (tested with otf-font-awesome)

    .. code-block:: python

        status.register(
            "pulseaudio",
            color_unmuted='#aa3300,
            color_muted='#aa0500',
            format_muted='\uf6a9',
            format='{volume_bar}',
            vertical_bar_width=1,
            vertical_bar_glyphs=['\uf026  ', '\uf027 ', '\uf028']
        )

    .. rubric:: Available formatters

    * `{volume}` â€” volume in percent (0...100)
    * `{db}` â€” volume in decibels relative to 100 %, i.e. 100 % = 0 dB, 50 % = -18 dB, 0 % = -infinity dB
      (the literal value for -infinity is `-âˆž`)
    * `{muted}` â€” the value of one of the `muted` or `unmuted` settings
    * `{volume_bar}` â€” unicode bar showing volume
    * `{selected}` â€” show the format_selected string if selected sink is the configured one
    """

    settings = (
        "format",
        ("format_muted", "optional format string to use when muted"),
        ("format_selected", "string used to mark this sink if selected"),
        "muted", "unmuted",
        "color_error", "color_muted", "color_unmuted",
        ("step", "percentage to increment volume on scroll"),
        ("sink", "sink name to use, None means pulseaudio default"),
        ("move_sink_inputs", "Move all sink inputs when we change the default sink"),
        ("bar_type", "type of volume bar. Allowed values are 'vertical' or 'horizontal'"),
        ("multi_colors", "whether or not to change the color from "
                         "'color_muted' to 'color_unmuted' based on volume percentage"),
        ("vertical_bar_width", "how many characters wide the vertical volume_bar should be"),
        ('vertical_bar_glyphs', 'custom array output as vertical bar instead of unicode bars')
    )

    muted = "M"
    unmuted = ""
    format = "â™ª: {volume}"
    format_muted = None
    format_selected = " ðŸ—¸"
    currently_muted = False
    has_amixer = False
    color_error = "#FF0000"
    color_muted = "#FF0000"
    color_unmuted = "#FFFFFF"
    vertical_bar_glyphs = None

    sink = None
    move_sink_inputs = True

    step = 5
    multi_colors = False
    bar_type = 'vertical'
    vertical_bar_width = 2

    on_rightclick = "switch_mute"
    on_doubleleftclick = "change_sink"
    on_leftclick = "pavucontrol"
    on_upscroll = "increase_volume"
    on_downscroll = "decrease_volume"

    def init(self):
        """Creates context, when context is ready context_notify_cb is called"""
        pass

    def request_update(self, context):
        """Requests a sink info update (sink_info_cb is called)"""
        pass

    def success_cb(self, context, success, userdata):
        pass

    @property
    def current_sink(self):
        pass

    def server_info_cb(self, context, server_info_p, userdata):
        """Retrieves the default sink and calls request_update"""
        pass

    def context_notify_cb(self, context, _):
        """Checks wether the context is ready

        -Queries server information (server_info_cb is called)
        -Subscribes to property changes on all sinks (update_cb is called)
        """
        pass

    def update_cb(self, context, t, idx, userdata):
        """A sink property changed, calls request_update"""
        pass

    def sink_info_cb(self, context, sink_info_p, eol, _):
        """Updates self.output"""
        pass

    def change_sink(self):
        pass

    def _call_pactl(self, pactl_arguments):
        pass

    def switch_mute(self):
        pass

    def increase_volume(self):
        pass

    def decrease_volume(self):
        pass
