import requests
import json
from decimal import Decimal

from i3pystatus import IntervalModule
from i3pystatus.core.util import internet, require


class Coin(IntervalModule):
    """
    Fetches live data of all cryptocurrencies available at coinmarketcap <https://coinmarketcap.com/>.
    Coin setting should be equal to the 'id' field of your coin in <https://api.coinmarketcap.com/v1/ticker/>.

    Example coin settings: bitcoin, bitcoin-cash, ethereum, litecoin, dash, lisk.
    Example currency settings: usd, eur, huf.

    .. rubric:: Available formatters

    * {symbol}
    * {price}
    * {rank}
    * {24h_volume}
    * {market_cap}
    * {available_supply}
    * {total_supply}
    * {max_supply}
    * {percent_change_1h}
    * {percent_change_24h}
    * {percent_change_7d}
    * {last_updated} - time of last update on the API's part
    * {status}
    """

    settings = (
        ("format", "format string used for output."),
        ("color"),
        ("coin", "cryptocurrency to fetch"),
        ("decimal", "round coin price down to this decimal place"),
        ("currency", "fiat currency to show fiscal data"),
        ("symbol", "coin symbol"),
        ("interval", "update interval in seconds"),
        ("status_interval", "percent change status in the last: '1h' / '24h' / '7d'")
    )

    symbol = "Â¤"
    color = None
    format = "{symbol} {price}{status}"
    coin = "ethereum"
    currency = "USD"
    interval = 600
    status_interval = "24h"
    decimal = 2

    def fetch_data(self):
        pass

    def set_status(self, change):
        pass

    @require(internet)
    def run(self):
        pass
