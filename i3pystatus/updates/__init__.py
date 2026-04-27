import threading

from i3pystatus import SettingsBase, Module, formatp
from i3pystatus.core.util import internet, require
from i3pystatus.core.desktop import DesktopNotification


class Backend(SettingsBase):
    settings = ()
    updates = 0


class Updates(Module):
    """
    Generic update checker.
    To use select appropriate backend(s) for your system.
    For list of all available backends see :ref:`updatebackends`.

    Left clicking on the module will refresh the count of upgradeable packages.
    This may be used to dismiss the notification after updating your system.

    Right clicking shows a desktop notification with a summary count and a list
    of available updates.

    .. rubric:: Available formatters

    * `{count}` â€” Sum of all available updates from all backends.
    * For each backend registered there is one formatter named after the
      backend, multiple identical backends do not accumulate, but overwrite
      each other.
    * For example, `{Cower}` (note capital C) is the number of updates
      reported by the cower backend, assuming it has been registered.

    .. rubric:: Usage example

    ::

        from i3pystatus import Status
        from i3pystatus.updates import pacman, cower

        status = Status()

        status.register("updates",
                        format = "Updates: {count}",
                        format_no_updates = "No updates",
                        backends = [pacman.Pacman(), cower.Cower()])

        status.run()

    """

    interval = 3600

    settings = (
        ("backends", "Required list of backends used to check for updates."),
        ("format", "Format used when updates are available. "
         "May contain formatters."),
        ("format_no_updates", "String that is shown if no updates are "
            "available. If not set the module will be hidden if no updates "
            "are available."),
        ("format_working", "Format used while update queries are run. By "
            "default the same as ``format``."),
        ("format_summary", "Format for the summary line of notifications. By "
            "default the same as ``format``."),
        ("notification_icon", "Icon shown when reporting the list of updates. "
            "Default is ``software-update-available``, and can be "
            "None for no icon."),
        "color",
        "color_no_updates",
        "color_working",
        ("interval", "Default interval is set to one hour."),
    )
    required = ("backends",)

    backends = None
    format = "Updates: {count}"
    format_no_updates = None
    format_working = None
    format_summary = None
    notification_icon = "software-update-available"
    color = "#00DD00"
    color_no_updates = None
    color_working = None

    on_leftclick = "run"
    on_rightclick = "report"

    def init(self):
        pass

    def update_thread(self):
        pass

    @require(internet)
    def check_updates(self):
        pass

    def run(self):
        pass

    def report(self):
        pass
