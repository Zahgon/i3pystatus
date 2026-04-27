import os

from i3pystatus.core.command import run_through_shell
from i3pystatus.updates import Backend


class AptGet(Backend):
    """
    Gets update count for Debian based distributions.

    This mimics the Arch Linux `checkupdates` script
    but with apt-get and written in python.
    """

    @property
    def updates(self):
        pass

Backend = AptGet

if __name__ == "__main__":
    """
    Call this module directly; Print the update count and notification body.
    """
    print("Updates: {}\n\n{}".format(*Backend().updates))
