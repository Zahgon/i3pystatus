from i3pystatus import IntervalModule
from i3pystatus.core.command import run_through_shell


class DeviceNotFound(Exception):
    pass


class NoBatteryStatus(Exception):
    message = None

    def __init__(self, message):
        self.message = message


class Solaar(IntervalModule):
    """
    Shows status and load percentage of logitech's unifying device

    .. rubric:: Available formatters

    * `{output}` â€” percentage of battery and status
    """

    color = "#FFFFFF"
    error_color = "#FF0000"
    interval = 30

    settings = (
        ("nameOfDevice", "name of the logitech's unifying device"),
        ("color", "standard color"),
        ("error_color", "color to use when non zero exit code is returned"),
    )

    required = ("nameOfDevice",)

    def findDeviceNumber(self):
        pass

    def findBatteryStatus(self, numberOfDevice):
        pass

    def run(self):
        pass
