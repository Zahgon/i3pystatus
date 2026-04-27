import json
import os.path
import requests
from subprocess import call
from urllib.parse import urljoin
import xml.etree.ElementTree as ET
from i3pystatus import IntervalModule
from i3pystatus.core.util import user_open


class Syncthing(IntervalModule):
    """
    Check Syncthing's online status and start/stop Syncthing via
    click events.

    Requires `requests`.
    """

    format_up = 'ST up'
    color_up = '#00ff00'
    format_down = 'ST down'
    color_down = '#ff0000'
    configfile = '~/.config/syncthing/config.xml'
    url = 'auto'
    apikey = 'auto'
    verify_ssl = True
    interval = 10
    on_leftclick = 'st_open'
    on_rightclick = 'st_toggle_systemd'

    settings = (
        ('format_up', 'Text to show when Syncthing is running'),
        ('format_down', 'Text to show when Syncthing is not running'),
        ('color_up', 'Color when Syncthing is running'),
        ('color_down', 'Color when Syncthing is not running'),
        ('configfile', 'Path to Syncthing config'),
        ('url', 'Syncthing GUI URL; "auto" reads from local config'),
        ('apikey', 'Syncthing APIKEY; "auto" reads from local config'),
        ('verify_ssl', 'Verify SSL certificate'),
    )

    def st_get(self, endpoint):
        # TODO: Maybe we can share a session across multiple GETs.
        pass

    def st_post(self, endpoint, data=None):
        pass

    def read_config(self):
        pass

    def ping(self):
        pass

    def run(self):
        pass

    # Callbacks
    def st_open(self):
        """Callback: Open Syncthing web UI"""
        pass

    def st_restart(self):
        """Callback: Restart Syncthing"""
        pass

    def st_stop(self):
        """Callback: Stop Syncthing"""
        pass

    def st_start_systemd(self):
        """Callback: systemctl --user start syncthing.service"""
        pass

    def st_restart_systemd(self):
        """Callback: systemctl --user restart syncthing.service"""
        pass

    def st_stop_systemd(self):
        """Callback: systemctl --user stop syncthing.service"""
        pass

    def st_toggle_systemd(self):
        """Callback: start Syncthing service if offline, or stop it when online"""
        pass
