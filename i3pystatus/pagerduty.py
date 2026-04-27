from i3pystatus import IntervalModule
from i3pystatus.core.util import internet, require, formatp

import pypd

__author__ = 'chestm007'


class PagerDuty(IntervalModule):
    """
    Module to get the current incidents in PD
    Requires `pypd`

    Formatters:

    * `{num_incidents}` - current number of incidents unresolved
    * `{num_acknowledged_incidents}` - as it sounds
    * `{num_triggered_incidents}` - number of unacknowledged incidents

    Example:

    .. code-block:: python

        status.register(
            'pagerduty',
            api_key='mah_api_key',
            user_id='LKJ19QW'
        )
    """

    settings = (
        'format',
        ('api_key', 'pagerduty api key'),
        ('color', 'module text color'),
        ('interval', 'refresh interval'),
        ('user_id', 'your pagerduty user id, shows up in the url when viewing your profile '
                    '`https://subdomain.pagerduty.com/users/<user_id>`')
    )

    required = ['api_key']

    format = '{num_triggered_incidents} triggered  {num_acknowledged_incidents} acknowledged'
    api_key = None
    color = '#AA0000'
    interval = 60
    user_id = None
    api_search_dict = dict(statuses=['triggered', 'acknowledged'])

    num_acknowledged_incidents = None
    num_triggered_incidents = None
    num_incidents = None

    def init(self):
        pass

    @require(internet)
    def run(self):
        pass
