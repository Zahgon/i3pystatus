import re
from datetime import datetime
from urllib.request import Request, urlopen

from i3pystatus.core.util import internet, require
from i3pystatus.weather import WeatherBackend


class Wunderground(WeatherBackend):
    '''
    This module retrieves weather data from Weather Underground.

    .. note::
        Previous versions of this module required an API key to work. Weather
        Underground has since discontinued their API, and this module has been
        rewritten to reflect that.

    .. rubric:: Finding your weather station

    To use this module, you must provide a weather station code (as the
    ``location_code`` option). To find your weather station, first search for
    your city and click to view the current conditions. Below the city name you
    will see the station name, and to the right of that a ``CHANGE`` link.
    Clicking that link will display a map, where you can find the station
    closest to you. Clicking on that station will take you back to the current
    conditions page. The weather station code will now be the last part of the
    URL. For example:

    .. code-block:: text

        https://www.wunderground.com/weather/us/ma/cambridge/KMACAMBR4

    In this case, the weather station code would be ``KMACAMBR4``.

    .. _weather-usage-wunderground:

    .. rubric:: Usage example

    .. code-block:: python

        from i3pystatus import Status
        from i3pystatus.weather import wunderground

        status = Status(logfile='/home/username/var/i3pystatus.log')

        status.register(
            'weather',
            format='{condition} {current_temp}{temp_unit}[ {icon}][ Hi: {high_temp}][ Lo: {low_temp}][ {update_error}]',
            colorize=True,
            hints={'markup': 'pango'},
            backend=wunderground.Wunderground(
                location_code='KMACAMBR4',
                units='imperial',
                update_error='<span color="#ff0000">!</span>',
            ),
        )

        status.run()

    See :ref:`here <weather-formatters>` for a list of formatters which can be
    used.
    '''
    settings = (
        ('location_code', 'Location code from wunderground.com'),
        ('units', '\'metric\' or \'imperial\''),
        ('update_error', 'Value for the ``{update_error}`` formatter when an '
                         'error is encountered while checking weather data'),
    )

    required = ('location_code',)

    location_code = None
    units = 'metric'
    update_error = '!'

    # Will be set in the init func
    conditions_url = None

    forecast_url = 'https://api.weather.com/v3/wx/forecast/daily/7day?apiKey={api_key}&geocode={lat:.2f}%2C{lon:.2f}&language=en-US&units={units_type}&format=json'
    observation_url = 'https://api.weather.com/v2/pws/observations/current?apiKey={api_key}&stationId={location_code}&format=json&units={units_type}'
    overview_url = 'https://api.weather.com/v3/aggcommon/v3alertsHeadlines;v3-wx-observations-current;v3-location-point?apiKey={api_key}&geocodes={lat:.2f}%2C{lon:.2f}&language=en-US&units={units_type}&format=json'

    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:88.0) Gecko/20100101 Firefox/88.0',
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Connection': 'keep-alive',
    }

    def init(self):
        pass

    @require(internet)
    def get_api_key(self):
        '''
        Grab the API key out of the page source from the home page
        '''
        pass

    @require(internet)
    def api_request(self, url, headers=None):
        pass

    @require(internet)
    def check_weather(self):
        '''
        Query the desired station and return the weather data
        '''
        pass
