from i3pystatus.core.command import run_through_shell
from i3pystatus.updates import Backend


class Cower(Backend):
    """
    Checks for updates in Arch User Repositories using the `cower` AUR helper.

    Depends on cower AUR agent - https://github.com/falconindy/cower
    """

    @property
    def updates(self):
        pass

Backend = Cower

if __name__ == "__main__":
    """
    Call this module directly; Print the update count and notification body.
    """
    print("Updates: {}\n\n{}".format(*Backend().updates))
