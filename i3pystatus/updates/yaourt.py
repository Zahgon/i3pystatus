from i3pystatus.core.command import run_through_shell
from i3pystatus.updates import Backend


class Yaourt(Backend):
    """
    This module counts the available updates using yaourt.
    By default it will only count aur packages. Thus it can be used with the
    pacman backend like this:

    .. code-block:: python

        from i3pystatus.updates import pacman, yaourt
        status.register("updates", backends = \
[pacman.Pacman(), yaourt.Yaourt()])

    To count both pacman and aur packages, pass False in the constructor:

    .. code-block:: python

        from i3pystatus.updates import yaourt
        status.register("updates", backends = [yaourt.Yaourt(False)])
    """

    def __init__(self, aur_only=True):
        self.aur_only = aur_only

    @property
    def updates(self):
        pass

Backend = Yaourt

if __name__ == "__main__":
    """
    Call this module directly; Print the update count and notification body.
    """
    print("Updates: {}\n\n{}".format(*Backend().updates))
