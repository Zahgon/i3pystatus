import json
import re
import threading
import time
from urllib.request import Request, urlopen

from i3pystatus import SettingsBase, IntervalModule, formatp
from i3pystatus.core.util import user_open, internet, require


class WeatherBackend(SettingsBase):
    settings = ()

    @require(internet)
    def http_request(self, url, headers=None):
        pass

    @require(internet)
    def api_request(self, url, headers=None):
        pass

    def check_response(self, response):
        pass


class Weather(IntervalModule):
    '''
    This is a generic weather-checker which must use a configured weather
    backend. For list of all available backends see :ref:`weatherbackends`.

    Double-clicking on the module will launch the forecast page for the
    location being checked, and single-clicking will trigger an update.

    .. _weather-formatters:

    .. rubric:: Available formatters

    * `{city}` â€” Location of weather observation
    * `{condition}` â€” Current weather condition (Rain, Snow, Overcast, etc.)
    * `{icon}` â€” Icon representing the current weather condition
    * `{observation_time}` â€” Time of weather observation (supports strftime format flags)
    * `{current_temp}` â€” Current temperature, excluding unit
    * `{low_temp}` â€” Forecasted low temperature, excluding unit
    * `{high_temp}` â€” Forecasted high temperature, excluding unit (may be
      empty in the late afternoon)
    * `{temp_unit}` â€” Either ``Â°C`` or ``Â°F``, depending on whether metric or
    * `{feelslike}` â€” "Feels Like" temperature, excluding unit
    * `{dewpoint}` â€” Dewpoint temperature, excluding unit
      imperial units are being used
    * `{wind_speed}` â€” Wind speed, excluding unit
    * `{wind_unit}` â€” Either ``kph`` or ``mph``, depending on whether metric or
      imperial units are being used
    * `{wind_direction}` â€” Wind direction
    * `{wind_gust}` â€” Speed of wind gusts in mph/kph, excluding unit
    * `{pressure}` â€” Barometric pressure, excluding unit
    * `{pressure_unit}` â€” ``mb`` or ``in``, depending on whether metric or
      imperial units are being used
    * `{pressure_trend}` â€” ``+`` if rising, ``-`` if falling, or an empty
      string if the pressure is steady (neither rising nor falling)
    * `{visibility}` â€” Visibility distance, excluding unit
    * `{visibility_unit}` â€” Either ``km`` or ``mi``, depending on whether
      metric or imperial units are being used
    * `{humidity}` â€” Current humidity, excluding percentage symbol
    * `{uv_index}` â€” UV Index
    * `{update_error}` â€” When the configured weather backend encounters an
      error during an update, this formatter will be set to the value of the
      backend's **update_error** config value. Otherwise, this formatter will
      be an empty string.

    This module supports the :ref:`formatp <formatp>` extended string format
    syntax. This allows for values to be hidden when they evaluate as False.
    The default **format** string value for this module makes use of this
    syntax to conditionally show the value of the **update_error** config value
    when the backend encounters an error during an update.

    See the following links for usage examples for the available weather
    backends:

    - :ref:`Weather.com <weather-usage-weathercom>`
    - :ref:`Weather Underground <weather-usage-wunderground>`

    .. rubric:: Troubleshooting

    If an error is encountered while updating, the ``{update_error}`` formatter
    will be set, and (provided it is in your ``format`` string) will show up
    next to the forecast to alert you to the error. The error message will (by
    default be logged to ``~/.i3pystatus-<pid>`` where ``<pid>`` is the PID of
    the update thread. However, it may be more convenient to manually set the
    logfile to make the location of the log data predictable and avoid clutter
    in your home directory. Additionally, using the ``DEBUG`` log level can
    be helpful in revealing why the module is not working as expected. For
    example:

    .. code-block:: python

        import logging
        from i3pystatus import Status
        from i3pystatus.weather import weathercom

        status = Status(logfile='/home/username/var/i3pystatus.log')

        status.register(
            'weather',
            format='{condition} {current_temp}{temp_unit}[ {icon}][ Hi: {high_temp}][ Lo: {low_temp}][ {update_error}]',
            colorize=True,
            hints={'markup': 'pango'},
            update_error='<span color="#ff0000">!</span>',
            log_level=logging.DEBUG,
            backend=weathercom.Weathercom(
                location_code='94107:4:US',
                units='imperial',
                log_level=logging.DEBUG,
            ),
        )

    .. note::
        The log level must be set separately in both the module and backend
        contexts.
    '''

    settings = (
        ('colorize', 'Vary the color depending on the current conditions.'),
        ('color_icons', 'Dictionary mapping weather conditions to tuples '
                        'containing a UTF-8 code for the icon, and the color '
                        'to be used.'),
        ('color', 'Display color (or fallback color if ``colorize`` is True). '
                  'If not specified, falls back to default i3bar color.'),
        ('backend', 'Weather backend instance'),
        ('refresh_icon', 'Text to display (in addition to any text currently '
                         'shown by the module) when refreshing weather data. '
                         '**NOTE:** Depending on how quickly the update is '
                         'performed, the icon may not be displayed.'),
        ('online_interval', 'seconds between updates when online (defaults to interval)'),
        ('offline_interval', 'seconds between updates when offline (default: 300)'),
        'format',
    )
    required = ('backend',)

    colorize = False
    color_icons = {
        'Fair': (u'\u263c', '#ffcc00'),
        'Fog': (u'', '#949494'),
        'Cloudy': (u'\u2601', '#f8f8ff'),
        'Partly Cloudy': (u'\u2601', '#f8f8ff'),  # \u26c5 is not in many fonts
        'Rainy': (u'\u26c8', '#cbd2c0'),
        'Thunderstorm': (u'\u26a1', '#cbd2c0'),
        'Sunny': (u'\u2600', '#ffff00'),
        'Snow': (u'\u2603', '#ffffff'),
        'default': ('', None),
    }

    color = None
    backend = None
    interval = 1800
    offline_interval = 300
    online_interval = None
    refresh_icon = 'âŸ³'
    format = '{current_temp}{temp_unit}[ {update_error}]'

    output = {'full_text': ''}

    on_doubleleftclick = ['launch_web']
    on_leftclick = ['check_weather']

    def launch_web(self):
        pass

    def init(self):
        pass

    def update_thread(self):
        pass

    def check_weather(self):
        '''
        Check the weather using the configured backend
        '''
        pass

    def get_color_data(self, condition):
        '''
        Disambiguate similarly-named weather conditions, and return the icon
        and color that match.
        '''
        pass

    def refresh_display(self):
        pass

    def run(self):
        pass
