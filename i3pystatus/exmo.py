# -*- coding: utf-8 -*-

import requests

from i3pystatus import IntervalModule, formatp
from i3pystatus.core.util import internet, require, user_open


class Exmo(IntervalModule):
    """
    This module fetching and displays exchange rates with EXMO.
    Using API <https://exmo.me/en/api>.

    .. rubric:: Available formatters

    * {buy_price}
    * {status}
    * {pair}

    """

    settings = (
        ('format', 'Format string used for output'),
        ('pair', 'Currency pair for display on output'),
        ('color', 'Standard color'),
        ('colorize', 'Enable color change on price increase/decrease'),
        ('color_up', 'Color for price increases'),
        ('color_down', 'Color for price decreases'),
        ('interval', 'Update interval.'),
        'status'
    )
    format = '{buy_price}[ {status}] {pair}'
    pair = 'BTC_USD'
    color = '#FFFFFF'
    colorize = False
    color_up = '#00FF00'
    color_down = '#FF0000'
    interval = 60
    status = {
        'price_up': 'â–²',
        'price_down': 'â–¼',
    }

    _prev_price = 0
    _prev_status = ''
    _prev_color = '#FFFFFF'

    def __init__(self, *args, **kwargs):
        super(Exmo, self).__init__(*args, **kwargs)
        self.on_leftclick = [
            'open_something',
            'https://exmo.me/ru/trade#?pair={}'.format(self.pair)
        ]

    def fetch_data(self):
        pass

    @require(internet)
    def run(self):
        pass

    def open_something(self, url_or_command):
        """
        Wrapper function, to pass the arguments to user_open
        """
        pass
