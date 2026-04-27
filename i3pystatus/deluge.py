import time

from deluge_client import DelugeRPCClient, FailedToReconnectException

from i3pystatus import IntervalModule, logger
from i3pystatus.core.util import bytes_info_dict


class Deluge(IntervalModule):
    """
    Deluge torrent module
    Requires `deluge-client`

    .. rubric:: Formatters:

    * `{num_torrents}`       - number of torrents in deluge
    * `{free_space_bytes}`   - bytes free in path
    * `{used_space_bytes}`   - bytes used in path
    * `{upload_rate}` - bytes sent per second
    * `{download_rate}` - bytes received per second
    * `{total_uploaded}`     - bytes sent total
    * `{total_downloaded}`     - bytes received total

    """

    settings = (
        'format',
        'color',
        ('rounding', 'number of decimal places to round numbers too'),
        ('host', 'address of deluge server (default: 127.0.0.1)'),
        ('port', 'port of deluge server (default: 58846)'),
        ('username', 'username to authenticate with deluge'),
        ('password', 'password to authenticate to deluge'),
        ('path', 'override "download path" server-side when checking space used/free'),
        ('offline_string', 'string to output while unable to connect to deluge daemon')
    )
    required = ('username', 'password')

    host = '127.0.0.1'
    port = 58846
    path = None
    color = None
    libtorrent_stats = False
    rounding = 2
    offline_string = 'offline'

    format = 'â›†{num_torrents} âœ‡{free_space_bytes}'

    id = int(time.time())  # something random

    def init(self):
        pass

    def run(self):
        pass

    def parse_values(self, values):
        pass

    def get_path_size(self, path=None):
        """
        get used space of path in bytes (default: download location)
        """
        pass

    def get_free_space(self, path=None):
        """
        get free space of path in bytes (default: download location)
        """
        pass

    def get_torrents_status(self, torrent_id=None, keys=None):
        pass

    def get_session_statistics(self):
        pass
