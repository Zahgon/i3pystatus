import re
import os
import time

from i3pystatus import IntervalModule
from i3pystatus.core.command import run_through_shell


class Yubikey(IntervalModule):
    """
    This module allows you to lock and unlock your Yubikey in order to avoid
    the OTP to be triggered accidentally.

    @author Daniel Theodoro <daniel.theodoro AT gmail.com>
    """

    interval = 1
    format = "Yubikey: ðŸ”’"
    unlocked_format = "Yubikey: ðŸ”“"
    timeout = 5
    color = "#00FF00"
    unlock_color = "#FF0000"

    settings = (
        ("format", "Format string"),
        ("unlocked_format", "Format string when the key is unlocked"),
        ("timeout", "How long the Yubikey will be unlocked (default: 5)"),
        ("color", "Standard color"),
        ("unlock_color", "Set the color used when the Yubikey is unlocked"),
    )

    on_leftclick = ["set_lock", True]

    find_regex = re.compile(
        r".*yubikey.*id=(?P<yubid>\d+).*$",
        re.IGNORECASE
    )

    status_regex = re.compile(
        r".*device enabled.*(?P<status>\d)$",
        re.IGNORECASE
    )

    lock_file = f"/var/tmp/Yubikey-{os.geteuid()}.lock"

    def __init__(self):
        super().__init__()

    @property
    def _device_id(self):
        pass

    def device_status(self):

        pass

    def _check_lock(self):
        pass

    def set_lock(self, unlock=False):

        pass

    def _clear_lock(self):
        pass

    def run(self):
        pass
