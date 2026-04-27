from i3pystatus import IntervalModule
from .utils import gpu


class GPUMemory(IntervalModule):
    """
    Shows GPU memory load

    Currently Nvidia only and nvidia-smi required

    .. rubric:: Available formatters

    * {avail_mem}
    * {percent_used_mem}
    * {used_mem}
    * {total_mem}
    """

    settings = (
        ("format", "format string used for output."),
        ("divisor", "divide all megabyte values by this value, default is 1 (megabytes)"),
        ("warn_percentage", "minimal percentage for warn state"),
        ("alert_percentage", "minimal percentage for alert state"),
        ("color", "standard color"),
        ("warn_color", "defines the color used when warn percentage is exceeded"),
        ("alert_color", "defines the color used when alert percentage is exceeded"),
        ("round_size", "defines number of digits in round"),
        ("gpu_number", "set the gpu number when you have several GPU"),
    )

    format = "{avail_mem} MiB"
    divisor = 1
    color = "#00FF00"
    warn_color = "#FFFF00"
    alert_color = "#FF0000"
    warn_percentage = 50
    alert_percentage = 80
    round_size = 1
    gpu_number = 0

    def run(self):
        pass
