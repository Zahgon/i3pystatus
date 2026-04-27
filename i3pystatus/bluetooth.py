from os.path import basename

import dbus

from i3pystatus import IntervalModule, formatp
from i3pystatus.core.util import TimeWrapper


def proxyobj(bus, path, interface):
    """ commodity to apply an interface to a proxy object """
    pass


def filter_by_interface(objects, interface_name):
    """ filters the objects based on their support
        for the specified interface """
    pass


def getprop(obj, prop, t):
    pass


def get_bluetooth_device_list(show_disconnected):
    # shamelessly stolen from https://stackoverflow.com/questions/14262315/list-nearby-discoverable-bluetooth-devices-including-already-paired-in-python/14267310#14267310
    pass


class Bluetooth(IntervalModule):
    """
    Shows currently connected bluetooth devices.

        * Requires ``python-dbus`` from your distro package manager, or \
``dbus-python`` from PyPI.

        Left click on the module to cycle forwards through devices, and right \
click to cycle backwards.

        .. rubric:: Available formatters (uses :ref:`formatp`)

        * `{name}` â€” (the name of the device)
        * `{dev_addr}` â€” (the bluetooth device address)

        .. rubric:: Available callbacks

        * ``next_device`` â€” iterate forward through devices
        * ``prev_device`` â€” iterate backwards through devices

        Example module registration with callbacks:

        ::
            status.register("now_playing",
                on_leftclick="next_device",
                on_rightclick="prev_device",
                on_upscroll="next_device",
                on_downscroll="prev_device")
    """

    interval = 1

    settings = (
        ("format", "formatp string"),
        ("color", "Text color"),
        ("connected_color", "Connected device color"),
        ("show_disconnected", "Show disconnected but paired devices")
    )

    format = "{name}: {dev_addr}"
    color = "#ffffff"
    connected_color = "#00ff00"

    on_leftclick = "next_device"
    on_rightclick = "prev_device"
    on_upscroll = 'next_device'
    on_downscroll = 'prev_device'

    num_devices = 0
    dev_index = 0
    devices = []
    show_disconnected = True

    def run(self):
        pass

    def next_device(self):
        pass

    def prev_device(self):
        pass
