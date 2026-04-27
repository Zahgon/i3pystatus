from fnmatch import fnmatch

import netifaces

from i3pystatus import IntervalModule, formatp
from i3pystatus.core.color import ColorRangeModule
from i3pystatus.core.util import make_graph, round_dict, make_bar, bytes_info_dict


def count_bits(integer):
    pass


def cidr6(addr, bits):
    pass


def v4_to_int(v4):
    pass


def prefix4(mask):
    pass


def cidr4(addr, mask):
    pass


def get_bonded_slaves():
    pass


def sysfs_interface_up(interface, unknown_up=False):
    pass


def detect_active_interface(ignore_ifaces, default_interface):
    pass


class NetworkInfo:
    """
    Retrieve network information.
    """

    def __init__(self, interface, ignore_interfaces, detached_down, unknown_up, freq_divisor, get_wifi_info=False):
        if interface not in netifaces.interfaces() and not detached_down:
            raise RuntimeError(
                "Unknown interface {iface}!".format(iface=interface))

        self.ignore_interfaces = ignore_interfaces
        self.detached_down = detached_down
        self.unknown_up = unknown_up
        self.get_wifi_info = get_wifi_info

        if freq_divisor == 0:
            raise RuntimeError("Frequency divider cannot be 0!")
        else:
            self.freq_divisor = freq_divisor

    def get_info(self, interface):
        pass

    @staticmethod
    def extract_network_info(network_info):
        pass

    def extract_wireless_info(self, interface):
        pass


class NetworkTraffic:
    """
    Retrieve network traffic information
    """

    pnic = None
    pnic_before = None

    def __init__(self, unknown_up):
        self.unknown_up = unknown_up

    def update_counters(self, interface):
        pass

    def clear_counters(self):
        pass

    def get_bytes_sent(self):
        pass

    def get_bytes_received(self):
        pass

    def get_packets_sent(self):
        pass

    def get_packets_received(self):
        pass

    def get_rx_total(self, interface):
        pass

    def get_tx_total(self, interface):
        pass

    def get_usage(self, interface):
        pass


class Network(IntervalModule, ColorRangeModule):
    """
    Displays network information for an interface.
    formatp support
    if u wanna display recv/send speed separate in dynamic color mode, please enable pango hint.

    Requires the PyPI packages `colour`, `netifaces`, `psutil` (optional, see below)
    and `basiciw` (optional, see below).

    .. rubric:: Available formatters

    Network Information Formatters:

    * `{interface}` â€” same as setting
    * `{v4}` â€” IPv4 address
    * `{v4mask}` â€” subnet mask
    * `{v4cidr}` â€” IPv4 address in cidr notation (i.e. 192.168.2.204/24)
    * `{v6}` â€” IPv6 address
    * `{v6mask}` â€” subnet mask
    * `{v6cidr}` â€” IPv6 address in cidr notation
    * `{mac}` â€” MAC of interface

    Wireless Information Formatters (requires PyPI package `basiciw`):

    * `{essid}` â€” ESSID of currently connected wifi
    * `{freq}` â€” Current frequency
    * `{freq_divisor}` â€” Frequency divisor
    * `{quality}` â€” Link quality in percent
    * `{quality_bar}` â€”Bar graphically representing link quality

    Network Traffic Formatters (requires PyPI package `psutil`):

    * `{interface}` â€” the configured network interface
    * `{network_graph_recv}` â€“ Unicode graph representing incoming network traffic
    * `{network_graph_sent}` â€“ Unicode graph representing outgoing network traffic
    * `{bytes_sent}` â€” bytes sent per second (divided by divisor | auto calculated if auto_units == True)
    * `{bytes_recv}` â€” bytes received per second (divided by divisor | auto calculated if auto_units == True)
    * `{packets_sent}` â€” packets sent per second
    * `{packets_recv}` â€” packets received per second
    * `{rx_tot_Mbytes}` â€” total Mbytes received
    * `{tx_tot_Mbytes}` â€” total Mbytes sent
    * `{rx_tot}` â€” total traffic recieved (rounded to nearest unit: KB, MB, GB)
    * `{tx_tot}` â€” total traffic sent (rounded to nearest unit: KB, MB, GB)
    """

    settings = (
        ("format_up", "format string"),
        ("format_active_up", "Dictionary containing format strings for auto-detected interfaces. "
                             "Each key can be either a full interface name, or a pattern matching "
                             "a interface, eg 'e*' for ethernet interfaces. "
                             "Fallback to format_up if no pattern could be matched."),
        ("format_down", "format string"),
        "color_up",
        "color_down",
        ("interface", "Interface to watch, eg 'eth0'"),
        ("dynamic_color", "Set color dynamically based on network traffic. Note: this overrides color_up"),
        ("start_color", "Hex or English name for start of color range, eg '#00FF00' or 'green'"),
        ("end_color", "Hex or English name for end of color range, eg '#FF0000' or 'red'"),
        ("graph_width", "Width of the network traffic graph"),
        ("graph_style", "Graph style ('blocks', 'braille-fill', 'braille-peak', or 'braille-snake')"),
        ("graph_direction", 'left-to-right/right-to-left'),
        ("separate_color", "display recv/send color separate in dynamic color mode."
                           "Note: only network speed formatters will display with range color "),
        ("coloring_type", "Whether to use the sent or received kb/s for dynamic coloring with non-separate colors. "
                          "Allowed values 'recv' or 'sent'"),
        ("divisor", "divide all byte values by this value"),
        ("recv_limit", "Expected max KiB/s. This value controls the drawing color of receive speed"),
        ("sent_limit", "Expected max KiB/s. similar with receive_limit"),
        ("freq_divisor", "divide Wifi frequency by this value"),
        ("ignore_interfaces", "Array of interfaces to ignore when cycling through "
                              "on click, eg, ['lo']"),
        ("round_size", "defines number of digits in round"),
        ("detached_down", "If the interface doesn't exist, display it as if it were down"),
        ("unknown_up", "If the interface is in unknown state, display it as if it were up"),
        ("next_if_down", "Change to next interface if current one is down"),
        ("detect_active", "Attempt to detect the active interface"),
        ("auto_units", "if true, unit of measurement is switched automatically (KB/MB/GB/...)"),
    )

    # Continue processing statistics when i3bar is hidden.
    keep_alive = True
    interval = 1
    interface = 'eth0'

    format_up = "{interface} {network_graph_recv}{bytes_recv}KB/s"
    format_active_up = {}
    format_down = "{interface}: DOWN"
    color_up = "#00FF00"
    color_down = "#FF0000"
    dynamic_color = True
    coloring_type = 'recv'
    graph_width = 15
    graph_style = 'blocks'
    graph_direction = 'left-to-right'
    recv_limit = 2048
    sent_limit = 1024
    separate_color = False
    next_if_down = False
    detect_active = False

    # Network traffic settings
    divisor = 1024
    round_size = 0
    auto_units = False

    # Network info settings
    detached_down = True
    unknown_up = False
    ignore_interfaces = ["lo"]
    freq_divisor = 1

    on_leftclick = "nm-connection-editor"
    on_rightclick = "cycle_interface"
    on_upscroll = ['cycle_interface', 1]
    on_downscroll = ['cycle_interface', -1]

    def init(self):
        # Don't require importing basiciw unless using the functionality it offers.
        pass

    def cycle_interface(self, increment=1):
        """Cycle through available interfaces in `increment` steps. Sign indicates direction."""
        pass

    def get_network_graph_recv(self, kbs, limit):
        # Cycle array by inserting at the start and chopping off the last element
        pass

    def get_network_graph_sent(self, kbs, limit):
        # Cycle array by inserting at the start and chopping off the last element
        pass

    def run(self):
        pass
