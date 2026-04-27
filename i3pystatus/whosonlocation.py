from i3pystatus import IntervalModule
import requests
from collections import OrderedDict
from bs4 import BeautifulSoup


class WhosOnLocation():
    email = None
    password = None
    session = None

    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.session = requests.Session()

    def login(self):
        pass

    def get_status(self):
        pass

    def on_site(self):
        pass

    def off_site(self):
        pass

    def __change_status(self, status):
        pass

    # _type can be org or location
    def search(self, keyword, _type='location'):
        pass

    @staticmethod
    def __parse_results(page):
        pass


class WOL(IntervalModule):
    """
    Change your whosonlocation.com status.

    Requires the PyPi module `beautifulsoup4`
    """
    location = None
    email = None
    password = None

    settings = (
        ('keyring_backend', 'alternative keyring backend for retrieving credentials'),
        'email',
        'password'
    )
    keyring_backend = None

    color_on_site = '#00FF00'
    color_off_site = '#ff0000'
    format = 'Status: {status}'
    status = None

    on_leftclick = 'change_status'

    def init(self):
        pass

    def change_status(self):
        pass

    def run(self):
        pass
