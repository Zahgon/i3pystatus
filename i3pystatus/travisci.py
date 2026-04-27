import os

import dateutil.parser

from travispy import TravisPy

from i3pystatus import IntervalModule
from i3pystatus.core.util import TimeWrapper, formatp, internet, require

__author__ = 'chestm007'


class TravisCI(IntervalModule):
    """
    Get current status of travis builds
    Requires `travispy` `dateutil.parser`

    Formatters:

    * `{repo_slug}`  - repository owner/repository name
    * `{repo_status}` - repository status
    * `{repo_name}` - repository name
    * `{repo_owner}` - repository owner
    * `{last_build_finished}` - date of the last finished build
    * `{last_build_duration}` - duration of the last build


    Examples

    .. code-block:: python

        status_color_map = {
            'passed': '#00FF00',
            'failed': '#FF0000',
            'errored': '#FFAA00',
            'cancelled': '#EEEEEE',
            'started': '#0000AA',

        }

    .. code-block:: python

        repo_status_map={
            'passed': '<span color="#00af00">passed</span>',
            'started': '<span color="#0000af">started</span>',
            'failed': '<span color="#af0000">failed</span>',
        }

    """

    settings = (
        'format',
        ('github_token', 'github personal access token'),
        ('repo_slug', 'repository identifier eg. "enkore/i3pystatus"'),
        ('time_format', 'passed directly to .strftime() for `last_build_finished`'),
        ('repo_status_map', 'map representing how to display status'),
        ('duration_format', '`last_build_duration` format string'),
        ('status_color_map', 'color for all text based on status'),
        ('color', 'color for all text not otherwise colored'))

    required = ('github_token', 'repo_slug')

    format = '{repo_owner}/{repo_name}-{repo_status} [({last_build_finished}({last_build_duration}))]'
    short_format = '{repo_name}-{repo_status}'
    time_format = '%m/%d'
    duration_format = '%m:%S'
    status_color_map = None
    repo_status_map = None
    color = '#DDDDDD'
    travis = None

    on_leftclick = 'open_build_webpage'

    def init(self):
        pass

    def _format_time(self, time):
        pass

    @require(internet)
    def run(self):
        pass

    def open_build_webpage(self):
        pass
