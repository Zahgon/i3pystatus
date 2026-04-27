import bisect
import configparser
import os
import re

from i3pystatus import IntervalModule, formatp
from i3pystatus.core.command import run_through_shell
from i3pystatus.core.desktop import DesktopNotification
from i3pystatus.core.util import lchop, TimeWrapper, make_bar, make_glyph, make_vertical_bar


class UEventParser(configparser.ConfigParser):
    @staticmethod
    def parse_file(file):
        pass

    def __init__(self):
        super().__init__(default_section="id10t", strict=False)

    def optionxform(self, key):
        pass

    def read_string(self, string):
        pass


class Battery:
    @staticmethod
    def create(from_file):
        pass

    def __init__(self, battery_info):
        self.battery_info = battery_info
        self.normalize_micro()

    def normalize_micro(self):
        pass

    def percentage(self, design=False):
        pass

    def status(self):
        pass

    def consumption(self, val):
        pass


class BatteryCharge(Battery):
    def __init__(self, bi):
        bi["CHARGE_FULL"] = bi["CHARGE_FULL_DESIGN"] if bi["CHARGE_NOW"] > bi["CHARGE_FULL"] else bi["CHARGE_FULL"]
        super().__init__(bi)

    def consumption(self):
        pass

    def _percentage(self, design):
        pass

    def wh_remaining(self):
        pass

    def wh_total(self):
        pass

    def wh_depleted(self):
        pass

    def remaining(self):
        pass


class BatteryEnergy(Battery):
    def consumption(self):
        pass

    def _percentage(self, design):
        pass

    def wh_remaining(self):
        pass

    def wh_total(self):
        pass

    def wh_depleted(self):
        pass

    def remaining(self):
        pass


class BatteryChecker(IntervalModule):
    """
    This class uses the /sys/class/power_supply/â€¦/uevent interface to check for the
    battery status.

    Setting ``battery_ident`` to ``ALL`` will summarise all available batteries
    and aggregate the % as well as the time remaining on the charge. This is
    helpful when the machine has more than one battery available.

    .. rubric:: Available formatters

    * `{remaining}` â€” remaining time for charging or discharging, uses TimeWrapper formatting, default format is `%E%h:%M`
    * `{percentage}` â€” battery percentage relative to the last full value
    * `{percentage_design}` â€” absolute battery charge percentage
    * `{consumption (Watts)}` â€” current power flowing into/out of the battery
    * `{status}`
    * `{no_of_batteries}` â€” The number of batteries included
    * `{battery_ident}` â€” the same as the setting
    * `{bar}` â€”bar displaying the relative percentage graphically
    * `{bar_design}` â€”bar displaying the absolute percentage graphically
    * `{glyph}` â€” A single character or string (selected from 'glyphs') representing the current battery percentage

    This module supports the :ref:`formatp <formatp>` extended string format
    syntax. By setting the ``FULL`` status to an empty string, and including
    brackets around the ``{status}`` formatter, the text within the brackets
    will be hidden when the battery is full, as can be seen in the below
    example:

    .. code-block:: python

        from i3pystatus import Status

        status = Status()

        status.register(
            'battery',
            interval=5,
            format='{battery_ident}: [{status} ]{percentage_design:.2f}%',
            alert=True,
            alert_percentage=15,
            status={
                'DPL': 'DPL',
                'CHR': 'CHR',
                'DIS': 'DIS',
                'FULL': '',
            }
        )

        # status.register(
        #     'battery',
        #     format='{status} {percentage:.0f}%',
        #     levels={
        #         25: "<=25",
        #         50: "<=50",
        #         75: "<=75",
        #     },
        # )

        status.run()

    """

    settings = (
        ("battery_ident", "The name of your battery, usually BAT0 or BAT1"),
        "format",
        ("not_present_text", "Text displayed if the battery is not present. No formatters are available"),
        ("alert", "Display a libnotify-notification on low battery"),
        ("critical_level_command", "Runs a shell command in the case of a critical power state"),
        "critical_level_percentage",
        "alert_percentage",
        "alert_timeout",
        ("alert_format_title", "The title of the notification, all formatters can be used"),
        ("alert_format_body", "The body text of the notification, all formatters can be used"),
        ("path", "Override the default-generated path and specify the full path for a single battery"),
        ("base_path", "Override the default base path for searching for batteries"),
        ("battery_prefix", "Override the default battery prefix"),
        ("status", "A dictionary mapping ('DPL', 'DIS', 'CHR', 'FULL') to alternative names"),
        ("levels", "A dictionary mapping percentages of charge levels to corresponding names."),
        ("color", "The text color"),
        ("full_color", "The full color"),
        ("charging_color", "The charging color"),
        ("critical_color", "The critical color"),
        ("not_present_color", "The not present color."),
        ("not_present_text",
         "The text to display when the battery is not present. Provides {battery_ident} as formatting option"),
        ("no_text_full", "Don't display text when battery is full - 100%"),
        ("glyphs", "Arbitrarily long string of characters (or array of strings) to represent battery charge percentage"),
        ("use_design_percentage", "Use design percentage rather then absolute percentage for alerts")
    )

    battery_ident = "ALL"
    format = "{status} {remaining}"
    status = {
        "DPL": "DPL",
        "CHR": "CHR",
        "DIS": "DIS",
        "FULL": "FULL",
    }
    levels = None
    not_present_text = "Battery {battery_ident} not present"

    alert = False
    critical_level_command = ""
    critical_level_percentage = 1
    alert_percentage = 10
    alert_timeout = -1
    alert_format_title = "Low battery"
    alert_format_body = "Battery {battery_ident} has only {percentage:.2f}% ({remaining:%E%hh:%Mm}) remaining!"
    color = "#ffffff"
    full_color = "#00ff00"
    charging_color = "#00ff00"
    critical_color = "#ff0000"
    not_present_color = "#ffffff"
    no_text_full = False
    glyphs = "â–�â–‚â–ƒâ–„â–…â–†â–‡â–ˆ"
    use_design_percentage = False

    battery_prefix = 'BAT'
    base_path = '/sys/class/power_supply'
    path = None
    paths = []

    notification = None

    def percentage(self, batteries, design=False):
        pass

    def consumption(self, batteries):
        pass

    def abs_consumption(self, batteries):
        pass

    def battery_status(self, batteries):
        pass

    def remaining(self, batteries):
        pass

    def init(self):
        pass

    def run(self):
        pass

    def alert_if_low_battery(self, fdict):
        pass
