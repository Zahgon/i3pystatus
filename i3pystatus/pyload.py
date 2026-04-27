import urllib.request
import urllib.parse
import urllib.error
import http.cookiejar
import webbrowser
import json

from i3pystatus import IntervalModule


class pyLoad(IntervalModule):
    """
    Shows pyLoad status

    .. rubric:: Available formatters

    * `{captcha}` â€” see captcha_true and captcha_false, which are the values filled in for this formatter
    * `{progress}` â€” average over all running downloads
    * `{progress_all}` â€” percentage of completed files/links in queue
    * `{speed}` â€” kilobytes/s
    * `{download}` â€” downloads enabled, also see download_true and download_false
    * `{total}` â€” number of downloads
    * `{free_space}` â€” free space in download directory in gigabytes
    """
    interval = 5

    settings = (
        ("address", "Address of pyLoad webinterface"),
        "format",
        "captcha_true", "captcha_false",
        "download_true", "download_false",
        "username", "password",
        ('keyring_backend', 'alternative keyring backend for retrieving credentials'),
    )
    required = ("username", "password")
    keyring_backend = None

    address = "http://127.0.0.1:8000"
    format = "{captcha} {progress_all:.1f}% {speed:.1f} kb/s"
    captcha_true = "Captcha waiting"
    captcha_false = ""
    download_true = "Downloads enabled"
    download_false = "Downloads disabled"
    on_leftclick = "open_webbrowser"

    def _rpc_call(self, method, data=None):
        pass

    def init(self):
        pass

    def login(self):
        pass

    def run(self):
        pass

    def open_webbrowser(self):
        pass
