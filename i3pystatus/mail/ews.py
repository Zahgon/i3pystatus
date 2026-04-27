import exchangelib
import contextlib
import time

from i3pystatus.mail import Backend


class ExchangeMailAccount(Backend):
    """
    Checks for mail on an Exchange account.

    Requires the python exchangelib library - https://github.com/ecederstrand/exchangelib.
    """

    settings = (
        ("host", 'The url to connect to. If unset, autodiscover is tried with the email address domain. If set, autodiscover is disabled.'),
        "username", "password", "email_address",
        ('keyring_backend', 'alternative keyring backend for retrieving credentials'),
    )
    required = ("username", "password", "email_address")
    keyring_backend = None

    host = None

    account = None
    last = 0

    @contextlib.contextmanager
    def ensure_connection(self):
        pass

    def count_new_mail(self):
        pass

    @property
    def unread(self):
        pass


Backend = ExchangeMailAccount
