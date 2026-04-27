from i3pystatus import IntervalModule
try:
    from os import cpu_count
except ImportError:
    from multiprocessing import cpu_count


class Load(IntervalModule):
    """
    Shows system load

    .. rubric:: Available formatters

    * `{avg1}` â€” the load average of the last minute
    * `{avg5}` â€” the load average of the last five minutes
    * `{avg15}` â€” the load average of the last fifteen minutes
    * `{tasks}` â€” the number of tasks (e.g. 1/285, which indiciates that one out of 285 total tasks is runnable)
    """

    format = "{avg1} {avg5}"
    settings = (
        "format",
        ("color", "The text color"),
        ("critical_limit", "Limit above which the load is considered critical, defaults to amount of cores."),
        ("critical_color", "The critical color"),
    )

    file = "/proc/loadavg"
    color = "#ffffff"
    critical_limit = cpu_count()
    critical_color = "#ff0000"

    def run(self):
        pass
