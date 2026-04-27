from i3pystatus.core.color import ColorRangeModule
from i3pystatus.cpu_usage import CpuUsage
from i3pystatus.core.util import make_graph


class CpuUsageGraph(CpuUsage, ColorRangeModule):
    """
     Shows CPU usage as a Unicode graph.
     The first output will be inacurate.

     Depends on the PyPI colour module - https://pypi.python.org/pypi/colour/0.0.5

     Linux only

     .. rubric:: Available formatters

     * `{cpu_graph}`  â€” graph of cpu usage.
     * `{usage}`      â€” usage average of all cores
     * `{usage_cpu*}` â€” usage of one specific core. replace "*" by core number starting at 0
     * `{usage_all}`  â€” usage of all cores separate. usess natsort when available(relevant for more than 10 cores)
     """

    settings = (
        ("cpu", "cpu to monitor, choices are 'usage_cpu' for all or 'usage_cpu*'. R"
                "eplace '*' by core number starting at 0."),
        ("start_color", "Hex or English name for start of color range, eg '#00FF00' or 'green'"),
        ("end_color", "Hex or English name for end of color range, eg '#FF0000' or 'red'"),
        ("graph_width", "Width of the cpu usage graph"),
        ("graph_style", "Graph style ('blocks', 'braille-fill', 'braille-peak', or 'braille-snake')"),
        ("direction", "Graph running direction ('left-to-right', 'right-to-left')"),
    )

    graph_width = 15
    graph_style = 'blocks'
    format = '{cpu_graph}'
    cpu = 'usage_cpu'
    direction = 'left-to-right'

    def init(self):
        pass

    def run(self):
        pass
