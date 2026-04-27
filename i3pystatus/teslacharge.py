import teslapy
from i3pystatus import IntervalModule


class TeslaCharge(IntervalModule):
    """
    Displays the current charge/range of your Tesla vehicle. There is a ton of
    data that could be displayed, so read this module to see the full list of
    datapoints that can be displayed.
    Requires: teslapy
    """

    settings = (
        ("email", "Email address used to login to your Tesla account."),
        ("password", "Password for accessing your Tesla account."),
        ("units", "Miles (default) or km"),
        ("interval", "Poll frequency. Polling too often can drain the battery"),
        ("format_with_charge", "Display format while car is charging"),
        ("format_without_charge", "Display format while car is not charging")
    )
    required = ("email", "password")
    units = "miles"
    conversion_factor = 0.62137119
    charge_complete = "#00FF00"  # green
    charging = "#FFFF00"         # yellow
    offline_color = "#FF0000"    # red
    interval = 900
    charging_icon = 'âš¡'
    disconnect_icon = ''
    format_with_charge = "{name}: {charge_state_icon}{charge_rate} {battery_level}%/{charge_limit_soc}% ({battery_range})"
    format_without_charge = "{name}: {battery_level}%/{charge_limit_soc}% ({battery_range})"

    def run(self):
        # Setup Tesla API client
        pass
