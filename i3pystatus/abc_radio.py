import logging
import shutil
import threading
import os
import xml.etree.ElementTree as etree
from datetime import datetime

import requests
import vlc
from dateutil import parser
from dateutil.tz import tzutc
from i3pystatus import IntervalModule
from i3pystatus.core.desktop import DesktopNotification
from i3pystatus.core.util import internet, require


class State:
    PLAYING = 1
    PAUSED = 2
    STOPPED = 3


class ABCRadio(IntervalModule):
    """
    Streams ABC Australia radio - https://radio.abc.net.au/. Currently uses VLC to do the
    actual streaming.

    Requires the PyPI packages `python-vlc`, `python-dateutil` and `requests`. Also requires VLC
    - https://www.videolan.org/vlc/index.html

    .. rubric:: Available formatters

    * `{station}` â€” Current station
    * `{title}` â€” Title of current show
    * `{url}` â€” Show's URL
    * `{remaining}` â€” Time left for current show
    * `{player_state}` â€” Unicode icons representing play, pause and stop
    """

    settings = (
        ("format", "format string for when the player is inactive"),
        ("format_playing", "format string for when the player is playing"),
        ("target_stations", "list of station ids to select from. Station ids can be obtained "
                            "from the following XML - http://www.abc.net.au/radio/data/stations_apps_v3.xml. "
                            "If the list is empty, all stations will be accessible."),
    )

    format = "{station} {title} {player_state}"
    format_playing = "{station} {title} {remaining} {player_state}"

    on_leftclick = 'toggle_play'
    on_upscroll = ['cycle_stations', 1]
    on_downscroll = ['cycle_stations', -1]
    on_doubleleftclick = 'display_notification'
    interval = 1

    # Destroy the player after this many seconds of inactivity
    PLAYER_LIFETIME = 5

    # Do not suspend the player when i3bar is hidden.
    keep_alive = True
    show_info = {}
    player = None
    station_info = None
    station_id = None
    stations = None
    prev_title = None
    prev_station = None
    target_stations = []

    end = None
    start = None
    destroy_timer = None
    cycle_lock = threading.Lock()

    player_icons = {
        State.PAUSED: "â–·",
        State.PLAYING: "â–¶",
        State.STOPPED: "â—¾",
    }

    def init(self):
        pass

    @require(internet)
    def run(self):
        pass

    def update_show_info(self):
        pass

    def get_player_state(self):
        pass

    def get_remaining(self):
        pass

    def cycle_stations(self, increment=1):
        pass

    def display_notification(self):
        pass

    def toggle_play(self):
        pass

    def init_player(self):
        pass

    def destroy(self):
        pass


class ABCStationInfo:
    PLAYING_URL = "https://program.abcradio.net.au/api/v1/programitems/{}/live.json?include=now"

    def currently_playing(self, station_id):
        pass

    def get_stations(self):
        pass

    def _get(self, url):
        pass


log = logging.getLogger(__name__)


class VLCPlayer(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.idle = threading.Event()
        self.die = threading.Event()
        self.instance = vlc.Instance()
        self.player_state = State.STOPPED
        self.player = self.instance.media_player_new()

    def run(self):
        pass

    def load_stream(self, url):
        pass

    def stream_loaded(self):
        pass

    def play(self):
        pass

    def pause(self):
        pass

    def stop(self):
        pass

    def destroy(self):
        pass

    def set_state(self, state):
        pass

    def is_playing(self):
        pass
