from i3pystatus.core.util import require, internet

try:
    from imaplib2.imaplib2 import IMAP4, IMAP4_SSL
    use_idle = True
except ImportError:
    from imaplib import IMAP4, IMAP4_SSL
    use_idle = False
import contextlib
import time
import socket
from threading import Thread

from i3pystatus.mail import Backend


IMAP_EXCEPTIONS = (socket.error, socket.gaierror, IMAP4.abort, IMAP4.error)


class IMAP(Backend):
    """
    Checks for mail on a IMAP server
    """

    settings = (
        "host", "port",
        "username", "password",
        ('keyring_backend', 'alternative keyring backend for retrieving credentials'),
        "ssl",
        "mailbox",
    )
    required = ("host", "username", "password")
    keyring_backend = None

    port = 993
    ssl = True
    mailbox = "INBOX"

    imap_class = IMAP4
    connection = None
    last = 0

    def init(self):
        pass

    @contextlib.contextmanager
    def ensure_connection(self):
        pass

    def _idle_thread(self):
        # update mail count on startup
        pass

    def count_new_mail(self):
        pass

    @property
    @require(internet)
    def unread(self):
        pass

Backend = IMAP
