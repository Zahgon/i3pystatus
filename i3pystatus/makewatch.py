from i3pystatus import IntervalModule
import psutil
import getpass


class MakeWatch(IntervalModule):
    """
    Watches for make jobs and notifies when they are completed.
    requires: psutil
    """

    settings = (
        ("name", "Listen for a job other than 'make' jobs"),
        ("running_color", "Text color while the job is running"),
        ("idle_color", "Text color while the job is not running"),
        "format",
    )
    running_color = "#FF0000"  # red
    idle_color = "#00FF00"   # green
    name = 'make'
    format = "{name}: {status}"

    def run(self):
        pass
