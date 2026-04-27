import os

import dateutil.parser

from circleci.api import Api

from i3pystatus import IntervalModule
from i3pystatus.core.util import TimeWrapper, formatp, internet, require

__author__ = 'chestm007'


class CircleCI(IntervalModule):
    """
    Get current status of circleci builds
    Requires `circleci` `dateutil.parser`

    Formatters:

    * `{repo_slug}`  - repository owner/repository name
    * `{repo_status}` - repository status
    * `{repo_name}` - repository name
    * `{repo_owner}` - repository owner
    * `{last_build_started}` - date of the last finished started
    * `{last_build_duration}` - duration of the last build, not populated with workflows(yet)


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
            'success': '<span color="#00af00">success</span>',
            'running': '<span color="#0000af">running</span>',
            'failed': '<span color="#af0000">failed</span>',
        }

    """

    settings = (
        'format',
        ('circleci_token', 'circleci access token'),
        ('repo_slug', 'repository identifier eg. "enkore/i3pystatus"'),
        ('time_format', 'passed directly to .strftime() for `last_build_started`'),
        ('repo_status_map', 'map representing how to display status'),
        ('duration_format', '`last_build_duration` format string'),
        ('status_color_map', 'color for all text based on status'),
        ('color', 'color for all text not otherwise colored'),
        ('workflow_name', '[WORKFLOWS_ONLY] if specified, monitor this workflows status. if not specified this module '
                          'will default to reporting the status of your last build'),
        ('workflow_branch', '[WORKFLOWS_ONLY] if specified, monitor the workflows in this branch'))

    required = ('circleci_token', 'repo_slug')

    format = '{repo_owner}/{repo_name}-{repo_status} [({last_build_started}({last_build_duration}))]'
    short_format = '{repo_name}-{repo_status}'
    time_format = '%m/%d'
    duration_format = '%m:%S'
    status_color_map = None
    repo_slug = None
    circleci_token = None
    repo_status_map = None
    color = '#DDDDDD'
    workflow_name = None
    workflow_branch = None

    circleci = None

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
