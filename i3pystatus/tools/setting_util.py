#!/usr/bin/env python
import glob
import inspect
import os
import getpass
import sys
import signal
import pkgutil
from collections import defaultdict, OrderedDict

import keyring

import i3pystatus
from i3pystatus import Module, SettingsBase
from i3pystatus.core import ClassFinder
from i3pystatus.core.exceptions import ConfigInvalidModuleError


def signal_handler(signal, frame):
    pass


def get_int_in_range(prompt, _range):
    pass


def enumerate_choices(choices):
    pass


def get_modules():
    pass


def get_credential_modules():
    pass


def main():
    pass

if __name__ == "__main__":
    main()
