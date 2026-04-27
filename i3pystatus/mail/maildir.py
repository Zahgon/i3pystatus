import os
from i3pystatus.mail import Backend


class MaildirMail(Backend):
    """
    Checks for local mail in Maildir
    """

    settings = (
        "directory",
    )
    required = ("directory",)

    directory = ""

    @property
    def unread(self):
        pass


Backend = MaildirMail
