from i3pystatus import IntervalModule, formatp
from i3pystatus.core.util import internet, require

import GeoIP
import urllib.request


class ExternalIP(IntervalModule):
    """
    Shows the external IP with the country code/name.

    Requires the PyPI package `GeoIP`.

    .. rubric:: Available formatters

    * {country_name} the full name of the country from the IP (eg. 'United States')
    * {country_code} the country code of the country from the IP (eg. 'US')
    * {ip} the ip
    """
    interval = 15

    settings = (
        "format",
        "color",
        ("color_down", "color when the http request failed"),
        ("color_hide", "color when the user has decide to switch to the hide format"),
        ("format_down", "format when the http request failed"),
        ("format_hide", "format when the user has decide to switch to the hide format"),
        ("ip_website", "http website where the IP is directly available as raw"),
        ("timeout", "timeout in seconds when the http request is taking too much time"),
    )

    format = "{country_name} {country_code} {ip}"
    format_hide = "{country_code}"
    format_down = "Timeout"

    ip_website = "https://api.ipify.org"
    timeout = 5
    color = "#FFFFFF"
    color_hide = "#FFFF00"
    color_down = "#FF0000"

    on_leftclick = "switch_hide"
    on_rightclick = "run"

    @require(internet)
    def get_external_ip(self):
        pass

    def run(self):
        pass

    def disable(self):
        pass

    def switch_hide(self):
        pass
