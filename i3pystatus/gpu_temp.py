from i3pystatus import IntervalModule
from .utils import gpu


class GPUTemperature(IntervalModule):
    """
    Shows GPU temperature

    Currently Nvidia only and nvidia-smi required

    .. rubric:: Available formatters

    * `{temp}`       â€” the temperature in integer degrees celsius
    """

    settings = (
        ("format", "format string used for output. {temp} is the temperature in integer degrees celsius"),
        ("display_if", "snippet that gets evaluated. if true, displays the module output"),
        ("gpu_number", "set the gpu number when you have several GPU"),
        "color",
        "alert_temp",
        "alert_color",
    )
    format = "{temp} Â°C"
    color = "#FFFFFF"
    alert_temp = 90
    alert_color = "#FF0000"
    display_if = 'True'
    gpu_number = 0

    def run(self):
        pass
