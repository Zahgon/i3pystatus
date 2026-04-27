from i3pystatus import IntervalModule


class Tlp(IntervalModule):
    """
    Shows the current mode of TLP (Linux power management tool), either
    battery, AC or unknown.

    .. rubric:: Available formatters

    * `{output}` - one of the strings configured through the `*_text` settings
    """
    last_pwr_file = "/run/tlp/last_pwr"
    bat_color = "#00FF00"
    ac_color = "#FFAA00"
    na_color = "#FF0000"
    bat_text = "BAT"
    ac_text = "AC"
    na_text = "N/A"

    settings = (
        ("last_pwr_file", "path to the TLP 'last pwr' file, default is `/run/tlp/last_pwr`"),
        ("bat_color", "color of text when TLP is in battery mode"),
        ("ac_color", "color of text when TLP is in AC mode"),
        ("na_color", "color of text when TLP is in unknown mode"),
        ("bat_text", "text to show when TLP is in battery mode"),
        ("ac_text", "text to show when TLP is in AC mode"),
        ("na_text", "text to show when TLP is in unknown mode"),
        "format",
    )

    format = "{output}"

    def run(self):
        pass
