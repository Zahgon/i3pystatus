import sys
from i3pystatus.mail import Backend
import subprocess


class MboxMail(Backend):
    """
    Checks for local mail in mbox
    """

    settings = ()
    required = ()

    @property
    def unread(self):
        pass


Backend = MboxMail
