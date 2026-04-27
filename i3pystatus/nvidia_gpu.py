from i3pystatus import IntervalModule
from .utils import gpu


class NvidiaGPU(IntervalModule):
    """
    Shows Nvidia GPU information

    Nvidia-smi required

    .. rubric:: Available formatters

    * {usage} gpu usage in percent
    * {avail_mem} available memory
    * {used_mem} used memory
    * {total_mem} total memory
    * {percent_used_mem} used_mem / total_mem
    * {temp} the temperature in degrees celsius
    """

    settings = (
        ("format", "format string used for output."),
        ("format_no_gpu_found", "Text to display when no GPUs are found. In such a case no formatters are available."),
        ("divisor", "All memory values are divided by this. Default is 1 which outputs megabytes."),
        ("coloring_based_on", "What data to base the coloring on. Allowed values are 'usage', 'mem', 'temp'"),
        ("warn_value", "minimal value for warn state (value of the data type chosen with 'coloring_based_on' setting)"),
        ("alert_value", "minimal value for alert state (value of the data type chosen with 'coloring_based_on' setting)"),
        ("color", "standard color"),
        ("warn_color", "Defines the color used when warn value is exceeded."),
        ("alert_color", "Defines the color used when alert value is exceeded."),
        ("color_no_gpu_found", "Color to use for text when no GPUs are found."),
        ("round_size", "Defines number of digits in round. Applied to all values."),
        ("gpu_number", "GPU number, in case of multiple GPUs"),
    )

    format = "{usage}% {temp}Â°C"
    format_no_gpu_found = "No GPUs found"
    divisor = 1
    coloring_based_on = "usage"
    color = "#00FF00"
    warn_color = "#FFFF00"
    alert_color = "#FF0000"
    warn_value = 50
    alert_value = 80
    color_no_gpu_found = "#FF0000"
    round_size = 1
    gpu_number = 0

    def run(self):
        pass
