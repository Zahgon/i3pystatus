from i3pystatus.core.color import ColorRangeModule
from i3pystatus.cpu_usage import CpuUsage
from i3pystatus.core.util import make_bar, make_vertical_bar


class CpuUsageBar(CpuUsage, ColorRangeModule):
    """
    Shows CPU usage as a bar (made with unicode box characters).
    The first output will be inacurate.

    Linux only

    Requires the PyPI package `colour`.

    .. rubric:: Available formatters

    * `{usage_bar}`      â€” usage average of all cores
    * `{usage_bar_cpu*}` â€” usage of one specific core. replace "*" by core number starting at 0
    """

    format = "{usage_bar}"
    bar_type = 'horizontal'
    cpu = 'usage_cpu'

    settings = (
        ("format", "format string"),
        ("bar_type", "whether the bar should be vertical or horizontal. "
                     "Allowed values: `vertical` or `horizontal`"),
        ("cpu", "cpu to base the colors on. Choices are 'usage_cpu' for all or 'usage_cpu*'."
                " Replace '*' by core number starting at 0."),
        ("start_color", "Hex or English name for start of color range, eg '#00FF00' or 'green'"),
        ("end_color", "Hex or English name for end of color range, eg '#FF0000' or 'red'"),
        ("dynamic_color", "Use dynamic color"),
    )

    def init(self):
        pass

    def run(self):
        pass
