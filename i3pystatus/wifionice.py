from datetime import datetime, timedelta
from json import loads
from urllib.request import urlopen
from threading import Condition, Thread

from i3pystatus import Module
from i3pystatus.core.util import formatp, user_open


class WifiOnIceAPI(Module):
    """
    Displays information about your current trip on Deutsche Bahn trains.
    Allows you to open an url formatted using train information.

    Requires the PyPI package `basiciw` if you want to use automatic
    detection. See below on how to disable automatic detection based on
    wifi adapter names.

    .. rubric:: URL examples

    * `https://travelynx.de/s/{last_station_no}?train={train_type}%20{train_no}` - Open travelynx check in page
    * `https://bahn.expert/details/{train_type}%20{train_no}/{trip_date}/?station={next_station_no}` - Show bahn.expert view for next station

    .. rubric:: Available formatters

    * `{arrival_in}` - Time until arrival (in form "1h 12m" or "53m")
    * `{arrival_time}` - Arrival time of train at the station (actual, if available, otherwise scheduled)
    * `{delay}` - delay of train in minutes
    * `{gps_lat}` - Current GPS latitude
    * `{gps_lon}` - Current GPS longitude
    * `{last_station_no}` - EVA number of the previous stop
    * `{net_current}` - current state of network quality
    * `{net_duration}` - how long until the next network quality change
    * `{net_expected}` - next state of network quality
    * `{next_platform}` - Platform number or name
    * `{next_station_no}` - EVA number of the next stop
    * `{next_station}` - Station name
    * `{speed}` - Train speed in km/h
    * `{train_no}` - Train number
    * `{train_type}` - Train Type (probably always `ICE`)
    """

    final_destination = 'Endstation'
    format_offtrain = None
    format_ontrain = '{speed}km/h > {next_station} ({arrival_in}[ | {delay}])'
    ice_status = {}
    off_train_interval = 10
    on_leftclick = 'open_url'
    on_train_interval = 2
    trip_info = {}
    url_on_click = ''
    wifi_adapters = ['wlan0']
    wifi_names = ['WiFi@DB', 'WIFIonICE']

    settings = (
        ("final_destination", "Information text for 'final destination has been reached'"),
        ("format_offtrain", "Formatter for 'not on a train' (module hidden if `None` - no formatters available)"),
        ("format_ontrain", "Formatter for 'on a train'"),
        ("off_train_interval", "time between updates if no train is detected"),
        ("on_train_interval", "time between updates while on a train"),
        ("url_on_click", "URL to open when left-clicking the module"),
        ("wifi_adapters", "List of wifi adapters the module should consider "
                          "when detecting if you are in a train. Set to `None` "
                          "to disable that functionality."),
        ("wifi_names", "List of Wifi network names that should be considered 'on a train'."),
    )

    def _format_time(self, seconds):
        pass

    def _check_wifi(self):
        pass

    def _loop(self):
        pass

    @property
    def _format_vars(self):
        pass

    def init(self):
        pass

    def open_url(self):
        pass

    def update_bar(self):
        pass
