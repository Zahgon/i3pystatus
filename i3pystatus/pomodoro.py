import subprocess
from datetime import datetime, timedelta
from i3pystatus import IntervalModule
from i3pystatus.core.desktop import DesktopNotification


STOPPED = 0
RUNNING = 1
BREAK = 2


class Pomodoro(IntervalModule):

    """
    This plugin shows Pomodoro timer.

    Left click starts/restarts timer.
    Right click stops it.

    Example color settings.

    .. code-block:: python

        color_map = {
            'stopped': '#2ECCFA',
            'running': '#FFFF00',
            'break': '#37FF00'
        }
    """

    settings = (
        ('sound',
         'Path to sound file to play as alarm. Played by "aplay" utility'),
        ('pomodoro_duration',
         'Working (pomodoro) interval duration in seconds'),
        ('break_duration', 'Short break duration in seconds'),
        ('long_break_duration', 'Long break duration in seconds'),
        ('short_break_count', 'Short break count before first long break'),
        ('format', 'format string, available formatters: current_pomodoro, '
                   'total_pomodoro, time'),
        ('inactive_format', 'format string to display when no timer is running'),
        ('color', 'dictionary containing a mapping of statuses to colours')
    )

    inactive_format = 'Start Pomodoro'

    color_map = {
        'stopped': '#2ECCFA',
        'running': '#FFFF00',
        'break': '#37FF00'
    }

    color = None
    sound = None

    interval = 1
    short_break_count = 3
    format = 'â˜¯ {current_pomodoro}/{total_pomodoro} {time}'

    pomodoro_duration = 25 * 60
    break_duration = 5 * 60
    long_break_duration = 15 * 60

    on_rightclick = "stop"
    on_leftclick = "start"

    def init(self):
        # state could be either running/break or stopped
        pass

    def run(self):
        pass

    def start(self):
        pass

    def stop(self):
        pass

    def _alarm(self, text):
        pass
