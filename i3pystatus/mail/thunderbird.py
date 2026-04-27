# This plugin listens for dbus signals emitted by the
# thunderbird-dbus-sender extension for TB:
# https://github.com/janoliver/thunderbird-dbus-sender
# The plugin must be active and thunderbird running for the module to work
# properly.

from functools import partial

import dbus
from dbus.mainloop.glib import DBusGMainLoop
from gi.repository import GObject

from i3pystatus.mail import Backend


class Thunderbird(Backend):
    """
    This class listens for dbus signals emitted by
    the dbus-sender extension for thunderbird.

    Requires python-dbus
    """

    _unread = set()

    def init(self):
        pass

    def new_msg(self, id, author, subject):
        pass

    def changed_msg(self, id, event):
        pass

    @property
    def unread(self):
        pass


Backend = Thunderbird
