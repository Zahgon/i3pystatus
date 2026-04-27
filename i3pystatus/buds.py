from enum import Enum, IntEnum
from json import JSONDecodeError, loads
from i3pystatus import IntervalModule
from i3pystatus.core.command import run_through_shell
from i3pystatus.core.color import ColorRangeModule
from i3pystatus.core.desktop import DesktopNotification


class BudsEqualizer(Enum):
    off = 0
    bass = 1
    soft = 2
    dynamic = 3
    clear = 4
    treble = 5


class BudsPlacementStatus(IntEnum):
    wearing = 1
    idle = 2
    case = 3


class Buds(IntervalModule, ColorRangeModule):
    earbuds_binary = "earbuds"

    """
    Displays information about Galaxy Buds devices

    Requires the earbuds tool from https://github.com/JojiiOfficial/LiveBudsCli

    .. rubric :: Available formatters
    * {amb} Displays the current ambient sound control status.
    * {anc} Displays the current active noise control status.
    * {battery} Displays combined battery level for left and right.
        If both are at the same level, it simply returns the battery level.
        If they have different levels and the drift threshold is enabled, provided
        they do not exceed the threshold, display the smaller level.
        If they have different battery levels, it returns both levels, if the threshold
        is exceeded.
    * `{left_battery}` Displays the left bud battery level.
    * `{right_battery}` Displays the right bud battery level.
    * `{battery_case} Displays the case battery level, if one of the buds is on the case.
    * `{device_model}` The model of the device.
    * `{equalizer} Displays current equalizer setting, only if the equalizer is on.
    * `{placement_left}` A placement indicator for the left bud, if it's on the (C)ase, (I)dle or being (W)ear.
    * `{placement_right}` A placement indicator for the right bud, if it's on the (C)ase, (I)dle or being (W)ear.
    * `{touchpad}` Displays if the touchpad is locked, and only if it is locked. A T(ouchpad)L(ocked) string indicates
        the touchpad is locked.
    """

    settings = (
        ("format", "Format string used for output"),
        ("interval", "Interval to run the module"),
        ("hide_no_device", "Hide the output if no device is connected"),
        ("battery_drift_threshold", "Drift threshold."),
        ("use_battery_drift_threshold", "Whether to display combined or separate levels, based on drift"),
        ("connected_color", "Output color for when the device is connected"),
        ("disconnected_color", "Output color for when the device is disconnected"),
        ("dynamic_color", "Output color based on battery level. Overrides connected_color"),
        ("start_color", "Hex or English name for start of color range, eg '#00FF00' or 'green'"),
        ("end_color", "Hex or English name for end of color range, eg '#FF0000' or 'red'"),
        ("wearing_symbol", "Symbol used to display when wearing the buds"),
        ("idle_symbol", "Symbol used to display for when the buds are in idle state"),
        ("case_symbol", "Symbol used to display when the buds are on the case"),
        ("battery_case_symbol", "Symbol used to indicate one of the buds is on the case"),
        ("enable_notifications", "Display notifications for certain battery levels events")
    )

    format = (
        "{device_model} "
        "L{placement_left}"
        "{battery}"
        "R{placement_right}"
        "{battery_case}"
        "{amb}"
        "{anc}"
        "{equalizer}"
        "{touchpad}"
    )
    hide_no_device = False
    battery_limit = 100
    battery_drift_threshold = 3
    use_battery_drift_threshold = True
    wearing_symbol = "W"
    idle_symbol = "I"
    case_symbol = "C"
    battery_case_symbol = "C"

    enable_notifications = True

    connected_color = "#00FF00"
    disconnected_color = "#FFFFFF"
    dynamic_color = True
    colors = []

    on_leftclick = 'toggle_anc'
    on_rightclick = 'toggle_amb'
    on_doubleleftclick = 'connect'
    on_doublerightclick = 'disconnect'
    on_middleclick = ['equalizer_set', BudsEqualizer.off]
    on_downscroll = ['equalizer_set', -1]
    on_upscroll = ['equalizer_set', +1]
    on_doublemiddleclick = 'restart_daemon'
    on_doubleupscroll = ['touchpad_set', 'true']
    on_doubledownscroll = ['touchpad_set', 'false']

    def init(self):
        pass

    def run(self):
        pass

    def battery_display_status(self, left_battery, right_battery, placement_left, placement_right):
        # determine battery level
        pass

    def battery_case_display(self, battery_case, left_battery, right_battery, placement_left, placement_right):
        # determine if the battery case should be displayed
        pass

    def connect(self):
        pass

    def disconnect(self):
        pass

    def equalizer_set(self, adjustment):
        pass

    def restart_daemon(self):
        pass

    def toggle_amb(self):
        pass

    def toggle_anc(self):
        pass

    @staticmethod
    def touchpad_lock_status(tab_lock_status):
        # determine touchpad lock status
        pass

    def touchpad_set(self, setting):
        pass

    def translate_placement(self, placement):
        pass
