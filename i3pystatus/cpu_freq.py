from i3pystatus import IntervalModule


class CpuFreq(IntervalModule):
    """
    class uses by default `/proc/cpuinfo` to determine the current cpu frequency

    .. rubric:: Available formatters

    * `{avg}` - mean from all cores in MHz `4.3f`
    * `{avgg}` - mean from all cores in GHz `1.2f`
    * `{coreX}` - frequency of core number `X` in MHz (format `4.3f`), where 0 <= `X` <= number of cores - 1
    * `{coreXg}` - frequency of core number `X` in GHz (fromat `1.2f`), where 0 <= `X` <= number of cores - 1

    """
    format = "{avgg}"
    settings = (
        "format",
        ("color", "The text color"),
        ("file", "override default path"),
    )

    file = '/proc/cpuinfo'
    color = '#FFFFFF'

    def createvaluesdict(self):
        """
        function processes the /proc/cpuinfo file, use file=/sys to use kernel >=4.13 location
        :return: dictionary used as the full-text output for the module
        """
        pass

    def run(self):
        pass
