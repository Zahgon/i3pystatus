from i3pystatus.file import File
from i3pystatus import Module
from i3pystatus.core.command import run_through_shell
import glob
import shutil


class Backlight(File):
    """
    Screen backlight info

    - (Optional) requires `xbacklight` to change the backlight brightness with the scollwheel.

    .. rubric:: Available formatters

    * `{brightness}` â€” current brightness relative to max_brightness
    * `{max_brightness}` â€” maximum brightness value
    * `{percentage}` â€” current brightness in percent
    """

    settings = (
        ("format", "format string, formatters: brightness, max_brightness, percentage"),
        ("format_no_backlight", "format string when no backlight file available"),
        ("backlight",
            "backlight, see `/sys/class/backlight/`. Supports glob expansion, i.e. `*` matches anything. "
            "If it matches more than one filename, selects the first one in alphabetical order"),
        "color",
    )
    required = ()

    backlight = "*"
    format = "{brightness}/{max_brightness}"
    format_no_backlight = "No backlight"

    base_path = "/sys/class/backlight/{backlight}/"
    components = {
        "brightness": (int, "brightness"),
        "max_brightness": (int, "max_brightness"),
    }
    transforms = {
        "percentage": lambda cdict: round((cdict["brightness"] / cdict["max_brightness"]) * 100),
    }
    on_upscroll = "lighter"
    on_downscroll = "darker"

    def init(self):
        pass

    def run_no_backlight(self):
        pass

    def lighter(self):
        pass

    def darker(self):
        pass
