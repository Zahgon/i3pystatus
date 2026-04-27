from i3pystatus import Module

import random
import string
import subprocess


class RandomPassword(Module):
    """
    Generates a random password and copies it to the clipboard. Useful if you use any password manager and you want to generate a password in the moment and save it later in you manager's database.

    Uses `SystemRandom` class as a cryptographically secure pseudo-number generator - <https://docs.python.org/3/library/random.html#random.SystemRandom>

    - Requires `xsel` or `xclip` for copying to the clipboard.
    - Generates a new password with a left click by default.
    - Generates a password with a default length of 12 and with lowercase, uppercase,  digits and special symbols.

    .. rubric:: Available formatters

    * `{length}` â€” length of generated password
    """

    settings = (
        ("format", "Format string to be displayed in the status bar"),
        ("length", "Length of the generated password"),
        ("charset", "Dictionary containing character types to be included in the password"),
        ("cliptool", "Currently supports xsel and xclip"),
        ("color", "HTML color hex code #RRGGBB"),
    )

    format = 'ï‚„'
    length = 12
    charset = ['lowercase', 'uppercase', 'digits', 'special']
    cliptool = None
    color = None

    on_doubleleftclick = 'generate_password'

    def init(self):
        # Finds out if either xsel or xclip exist
        pass

    def _find_cliptool(self):
        pass

    def generate_password(self):
        # If a blank list is provided for the charset, it will generate an empty password
        pass
