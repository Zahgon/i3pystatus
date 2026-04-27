from i3pystatus import IntervalModule
import speedtest
import requests
import time
import os
from urllib.parse import urlparse
import contextlib
import sys
from io import StringIO


class NetSpeed(IntervalModule):
    """
    Attempts to provide an estimation of internet speeds.
    Requires: speedtest-cli/modularize-2
    speedtest-cli/modularize-2 can be installed using pip:
    `pip install git+https://github.com/sivel/speedtest-cli.git@modularize-2`
    """

    settings = (
        ("units", "Valid values are B, b, bytes, or bits"),
        "format",
        'color'
    )
    color = "#FFFFFF"
    interval = 300
    units = 'bits'
    format = "â†“{speed_down:.1f}{down_units} â†‘{speed_up:.1f}{up_units} ({hosting_provider})"

    def form_b(self, n: float) -> tuple:
        """
        formats a bps as bps/kbps/mbps/gbps etc
        handles whether its meant to be in bytes
        :param n: input float
        :rtype tuple:
        :return: tuple of float-number of mbps etc, str-units
        """
        pass

    def run(self):
        # since speedtest_cli likes to print crap, we need to squelch it
        pass
