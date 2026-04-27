import urllib.request
import json
from datetime import datetime

from i3pystatus import IntervalModule
from i3pystatus.core.util import internet, require, user_open

import locale
import threading
from contextlib import contextmanager

LOCALE_LOCK = threading.Lock()


@contextmanager
def setlocale(name):
    # To deal with locales only in this module and keep it thread save
    pass


class Bitcoin(IntervalModule):

    """
    This module fetches and displays current Bitcoin market prices and
    optionally monitors transactions to and from a list of user-specified
    wallet addresses. Market data is pulled from the Bitaps Market
    API <https://bitaps.com> and it is possible to specify
    the exchange to be monitored.
    Transaction data is pulled from blockchain.info
    <https://blockchain.info/api/blockchain_api>.

    .. rubric:: Available formatters

    * {last_price}
    * {ask_price}
    * {bid_price}
    * {open_price}
    * {volume}
    * {volume_thousand}
    * {volume_percent}
    * {age}
    * {status}
    * {last_tx_type}
    * {last_tx_addr}
    * {last_tx_value}
    * {balance_btc}
    * {balance_fiat}
    * {symbol}

    """

    settings = (
        ("format", "Format string used for output."),
        ("currency", "Base fiat currency used for pricing."),
        ("wallet_addresses", "List of wallet address(es) to monitor."),
        ("color", "Standard color"),
        ("exchange", "Get ticker from a custom exchange instead"),
        ("colorize", "Enable color change on price increase/decrease"),
        ("color_up", "Color for price increases"),
        ("color_down", "Color for price decreases"),
        ("interval", "Update interval."),
        ("symbol", "Symbol for bitcoin sign"),
        "status"
    )
    format = "{symbol} {status}{last_price}"
    currency = "USD"
    exchange = "bitstamp"
    symbol = "\uF15A"
    wallet_addresses = ""
    color = "#FFFFFF"
    colorize = False
    color_up = "#00FF00"
    color_down = "#FF0000"
    interval = 600
    status = {
        "price_up": "â–²",
        "price_down": "â–¼",
    }

    on_leftclick = "electrum"
    on_rightclick = ["open_something", "https://bitaps.com/"]

    _price_prev = 0

    def _get_age(self, bitcoinaverage_timestamp):
        pass

    def _query_api(self, api_url):
        pass

    def _fetch_price_data(self):
        pass

    def _fetch_blockchain_data(self):
        pass

    @require(internet)
    def run(self):
        pass

    def open_something(self, url_or_command):
        """
        Wrapper function, to pass the arguments to user_open
        """
        pass
