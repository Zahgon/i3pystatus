import time

from i3pystatus import IntervalModule
from i3pystatus.core.command import execute
from i3pystatus.core.util import TimeWrapper


class TimerState:
    stopped = 0
    running = 1
    overflow = 2


class Timer(IntervalModule):
    """
    Timer module to remind yourself that there probably is something else you
    should be doing right now.

    Main features include:

    - Set custom time interval with click events.
    - Different output formats triggered when remaining time is less than `x`
      seconds.
    - Execute custom python function or external command when timer overflows
      (or reaches zero depending on how you look at it).

    .. rubric:: Available formatters

    Time formatters are available to show the remaining time.
    These include ``%h``, ``%m``, ``%s``, ``%H``, ``%M``, ``%S``.
    See :py:class:`.TimeWrapper` for detailed description.

    The ``format_custom`` setting allows you to display different formats when
    certain amount of seconds is remaining.
    This setting accepts list of tuples which contain time in seconds,
    format string and color string each.
    See the default settings for an example:

    - ``(0, "+%M:%S", "#ffffff")`` - Use this format after overflow. White text
      with red background set by the urgent flag.
    - ``(60, "-%M:%S", "#ffa500")`` - Change color to orange in last minute.
    - ``(3600, "-%M:%S", "#00ff00")`` - Hide hour digits when remaining time is
      less than one hour.

    Only first matching rule is applied (if any).

    .. rubric:: Callbacks

    Module contains three mouse event callback methods:

    - :py:meth:`.start` - Default: Left click starts (or adds) 5 minute
      countdown.
    - :py:meth:`.increase` - Default: Upscroll/downscroll increase/decrease time
      by 1 minute.
    - :py:meth:`.reset` - Default: Right click resets timer.

    Two new event settings were added:

    - ``on_overflow`` - Executed when remaining time reaches zero.
    - ``on_reset`` - Executed when timer is reset but only if overflow occurred.

    These settings accept either a python callable object or a string with shell
    command.
    Python callbacks should be non-blocking and without any arguments.

    Here is an example that plays a short sound file in 'loop' every 60 seconds
    until timer is reset.
    (``play`` is part of ``SoX`` - the Swiss Army knife of audio manipulation)

    ::

        on_overflow = "play -q /path/to/sound.mp3 pad 0 60 repeat -"
        on_reset = "pkill -SIGTERM -f 'play -q /path/to/sound.mp3 pad 0 60 repeat -'"

    """

    interval = 1

    on_leftclick = ["start", 300]
    on_rightclick = "reset"
    on_upscroll = ["increase", 60]
    on_downscroll = ["increase", -60]

    settings = (
        ("format", "Default format that is showed if no ``format_custom`` "
         "rules are matched."),
        ("format_stopped", "Format showed when timer is inactive."),
        "color",
        "color_stopped",
        "format_custom",
        ("overflow_urgent", "Set urgent flag on overflow."),
        "on_overflow",
        "on_reset",
    )

    format = '-%h:%M:%S'
    format_stopped = "T"
    color = "#00ff00"
    color_stopped = "#ffffff"
    format_custom = [
        (0, "+%M:%S", "#ffffff"),
        (60, "-%M:%S", "#ffa500"),
        (3600, "-%M:%S", "#00ff00"),
    ]
    overflow_urgent = True
    on_overflow = None
    on_reset = None

    def init(self):
        pass

    def run(self):
        pass

    def start(self, seconds=300):
        """
        Starts timer.
        If timer is already running it will increase remaining time instead.

        :param int seconds: Initial time.
        """
        pass

    def increase(self, seconds):
        """
        Change remaining time value.

        :param int seconds: Seconds to add. Negative value subtracts from
         remaining time.
        """
        pass

    def reset(self):
        """
        Stop timer and execute ``on_reset`` if overflow occurred.
        """
        pass
