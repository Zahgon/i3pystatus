from i3pystatus import IntervalModule, formatp

import datetime
import math

import decimal
import os

from i3pystatus.core.util import TimeWrapper

dec = decimal.Decimal


class MoonPhase(IntervalModule):
    """
    Available Formatters

    status: Allows for mapping of current moon phase
    - New Moon:
    - Waxing Crescent:
    - First Quarter:
    - Waxing Gibbous:
    - Full Moon:
    - Waning Gibbous:
    - Last Quarter:
    - Waning Crescent:

    """

    settings = (
        "format",
        ("status", "Current moon phase"),
        ("illum", "Percentage that is illuminated"),
        ("color", "Set color"),
        ("moonicon", 'Set icon')
    )

    format = "{illum} {status} {moonicon}"

    interval = 60 * 60 * 2  # every 2 hours

    status = {
        "New Moon": "NM",
        "Waxing Crescent": "WaxCres",
        "First Quarter": "FQ",
        "Waxing Gibbous": "WaxGib",
        "Full Moon": "FM",
        "Waning Gibbous": "WanGib",
        "Last Quarter": "LQ",
        "Waning Crescent": "WanCres",
    }

    color = {
        "New Moon": "#00BDE5",
        "Waxing Crescent": "#138DD8",
        "First Quarter": "#265ECC",
        "Waxing Gibbous": "#392FBF",
        "Full Moon": "#4C00B3",
        "Waning Gibbous": "#871181",
        "Last Quarter": "#C32250",
        "Waning Crescent": "#FF341F",
    }

    moonicon = {
        "New Moon": b'\xf0\x9f\x8c\x91'.decode(),
        "Waxing Crescent": b'\xf0\x9f\x8c\x92'.decode(),
        "First Quarter": b'\xf0\x9f\x8c\x93'.decode(),
        "Waxing Gibbous": b'\xf0\x9f\x8c\x94'.decode(),
        "Full Moon": b'\xf0\x9f\x8c\x95'.decode(),
        "Waning Gibbous": b'\xf0\x9f\x8c\x96'.decode(),
        "Last Quarter": b'\xf0\x9f\x8c\x97'.decode(),
        "Waning Crescent": b'\xf0\x9f\x8c\x98'.decode()
    }

    def pos(now=None):
        pass

    def current_phase(self):

        pass

    def illum(self):
        pass

    def run(self):
        pass
