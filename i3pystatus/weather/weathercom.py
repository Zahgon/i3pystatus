import json
import re
from datetime import datetime
from html.parser import HTMLParser
from urllib.request import Request, urlopen

from i3pystatus.core.util import internet, require
from i3pystatus.weather import WeatherBackend


class WeathercomHTMLParser(HTMLParser):
    '''
    Obtain data points required by the Weather.com API which are obtained
    through some other source at runtime and added as <script> elements to the
    page source.
    '''
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'

    def __init__(self, logger):
        self.logger = logger
        super(WeathercomHTMLParser, self).__init__()

    def get_weather_data(self, url):
        pass

    def load_json(self, json_input):
        pass

    def handle_data(self, content):
        '''
        Sometimes the weather data is set under an attribute of the "window"
        DOM object. Sometimes it appears as part of a javascript function.
        Catch either possibility.
        '''
        pass


class Weathercom(WeatherBackend):
    '''
    This module gets the weather from weather.com. The ``location_code``
    parameter should be set to the location code from weather.com. To obtain
    this code, search for your location on weather.com, and when you go to the
    forecast page, the code you need will be everything after the last slash in
    the URL (e.g. ``94107:4:US``, or
    ``8b7867695971473a260df2c5d49ff92dc9079dcb673c545f5f107f5c4ab30732``).

    .. _weather-usage-weathercom:

    .. rubric:: Usage example

    .. code-block:: python

        from i3pystatus import Status
        from i3pystatus.weather import weathercom

        status = Status(logfile='/home/username/var/i3pystatus.log')

        status.register(
            'weather',
            format='{condition} {current_temp}{temp_unit}[ {icon}][ Hi: {high_temp}][ Lo: {low_temp}][ {update_error}]',
            interval=900,
            colorize=True,
            hints={'markup': 'pango'},
            backend=weathercom.Weathercom(
                location_code='94107:4:US',
                units='imperial',
                update_error='<span color="#ff0000">!</span>',
            ),
        )

        status.run()

    See :ref:`here <weather-formatters>` for a list of formatters which can be
    used.
    '''
    settings = (
        ('location_code', 'Location code from www.weather.com'),
        ('units', '\'metric\' or \'imperial\''),
        ('update_error', 'Value for the ``{update_error}`` formatter when an '
                         'error is encountered while checking weather data'),
    )
    required = ('location_code',)

    location_code = None
    units = 'metric'
    update_error = '!'

    url_template = 'https://weather.com/{locale}/weather/today/l/{location_code}'

    # This will be set in the init based on the passed location code
    conditions_url = None

    def init(self):
        pass

    @require(internet)
    def check_weather(self):
        '''
        Fetches the current weather from wxdata.weather.com service.
        '''
        pass
