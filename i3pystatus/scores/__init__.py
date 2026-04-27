import copy
import json
import operator
import pytz
import re
import threading
import time
from datetime import datetime, timedelta
from urllib.request import urlopen
from urllib.error import HTTPError, URLError

from i3pystatus import SettingsBase, Module, formatp
from i3pystatus.core.util import user_open, internet, require


class ScoresBackend(SettingsBase):
    settings = ()
    favorite_teams = []
    all_games = True
    date = None
    games = {}
    scroll_order = []
    last_update = 0

    def init(self):
        # Merge the passed team colors with the global ones. A simple length
        # check is sufficient here because i3pystatus.scores.Scores instance
        # will already have checked to see if any invalid teams were specified
        # in team_colors.
        pass

    def api_request(self, url):
        pass

    @property
    def name(self):
        '''
        Return the backend name
        '''
        pass

    def get_api_date(self):
        '''
        Figure out the date to use for API requests. Assumes yesterday's date
        if between midnight and 10am Eastern time. Override this function in a
        subclass to change how the API date is calculated.
        '''
        pass

    @staticmethod
    def add_ordinal(number):
        pass

    @staticmethod
    def zero_fallback(value):
        pass

    def get_nested(self, data, expr, callback=None, default=''):
        pass

    def interpret_api_return(self, data, team_game_map):
        pass


class Scores(Module):
    '''
    This is a generic score checker, which must use at least one configured
    :ref:`score backend <scorebackends>`.

    Followed games can be scrolled through with the mouse/trackpad.
    Left-clicking on the module will refresh the scores, while right-clicking
    it will cycle through the configured backends. Double-clicking the module
    with the left button will launch the league-specific (MLB Gameday / NHL
    GameCenter / etc.) URL for the game. If there is not an active game,
    double-clicking will launch the league-specific scoreboard URL containing
    all games for the current day.

    Double-clicking with the right button will reset the current backend to the
    first game in the scroll list. This is useful for quickly switching back to
    a followed team's game after looking at other game scores.

    Scores for the previous day's games will be shown until 10am Eastern Time
    (US), after which time the current day's games will be shown.

    .. rubric:: Available formatters

    Formatters are set in the backend instances, see the :ref:`scorebackends`
    for more information.

    This module supports the :ref:`formatp <formatp>` extended string format
    syntax. This allows for values to be hidden when they evaluate as False
    (e.g. when a formatter is blank (an empty string). The default values for
    the format strings set in the :ref:`score backends <scorebackends>`
    (``format_pregame``, ``format_in_progress``, etc.) make heavy use of
    formatp, hiding many formatters when they are blank.

    .. rubric:: Usage example

    .. code-block:: python

        from i3pystatus import Status
        from i3pystatus.scores import mlb, nhl, nba

        status = Status()

        status.register(
            'scores',
            hints={'markup': 'pango'},
            colorize_teams=True,
            favorite_icon='<span size="small" color="#F5FF00">â˜…</span>',
            team_format='abbreviation',
            backends=[
                mlb.MLB(
                    teams=['CWS', 'SF'],
                    team_format='name',
                    format_no_games='No games today :(',
                    inning_top='â¬†',
                    inning_bottom='â¬‡',
                ),
                nhl.NHL(teams=['CHI']),
                nba.NBA(
                    teams=['GSW'],
                    all_games=False,
                ),
            ],
        )

        status.run()

    To enable colorized team name/city/abbbreviation, ``colorize_teams`` must
    be set to ``True``. This also requires that i3bar is configured to use
    Pango, and that the :ref:`hints <hints>` param is set for the module and
    includes a ``markup`` key, as in the example above. To ensure that i3bar is
    configured to use Pango, the `font param`__ in your i3 config file must
    start with ``pango:``.

    .. __: http://i3wm.org/docs/userguide.html#fonts

    .. _scores-game-order:

    If a ``teams`` param is not specified for the backend, then all games for
    the current day will be tracked, and will be ordered by the start time of
    the game. Otherwise, only games from explicitly-followed teams will be
    tracked, and will be in the same order as listed. If ``ALL`` is part of the
    list, then games from followed teams will be first in the scroll list,
    followed by all remaining games in order of start time.

    Therefore, in the above example, only White Sox and Giants games would be
    tracked, while in the below example all games would be tracked, with
    White Sox and Giants games appearing first in the scroll list and the
    remaining games appearing after them, in order of start time.

    .. code-block:: python

        from i3pystatus import Status
        from i3pystatus.scores import mlb

        status = Status()

        status.register(
            'scores',
            hints={'markup': 'pango'},
            colorize_teams=True,
            favorite_icon='<span size="small" color="#F5FF00">â˜…</span>',
            backends=[
                mlb.MLB(
                    teams=['CWS', 'SF', 'ALL'],
                    team_colors={
                        'NYM': '#1D78CA',
                    },
                ),
            ],
        )

        status.run()

    .. rubric:: Troubleshooting

    If the module gets stuck during an update (i.e. the ``refresh_icon`` does
    not go away), then the update thread probably encountered a traceback. This
    traceback will (by default) be logged to ``~/.i3pystatus-<pid>`` where
    ``<pid>`` is the PID of the thread. However, it may be more convenient to
    manually set the logfile to make the location of the log data reliable and
    avoid clutter in your home directory. For example:

    .. code-block:: python

        import logging
        from i3pystatus import Status
        from i3pystatus.scores import mlb, nhl

        status = Status(
            logfile='/home/username/var/i3pystatus.log',
        )

        status.register(
            'scores',
            log_level=logging.DEBUG,
            backends=[
                mlb.MLB(
                    teams=['CWS', 'SF'],
                    log_level=logging.DEBUG,
                ),
                nhl.NHL(
                    teams=['CHI'],
                    log_level=logging.DEBUG,
                ),
                nba.NBA(
                    teams=['CHI'],
                    log_level=logging.DEBUG,
                ),
            ],
        )

        status.run()

    .. note::
        The ``log_level`` must be set separately in both the module and the
        backend instances (as shown above), otherwise the backends will
        still use the default log level.
    '''
    interval = 300

    settings = (
        ('backends', 'List of backend instances'),
        ('interval', 'Update interval (in seconds)'),
        ('favorite_icon', 'Value for the ``{away_favorite}`` and '
                          '``{home_favorite}`` formatter when the displayed game '
                          'is being played by a followed team'),
        ('color', 'Color to be used for non-colorized text (defaults to the '
                  'i3bar color)'),
        ('color_no_games', 'Color to use when no games are scheduled for the '
                           'currently-displayed backend (defaults to the '
                           'i3bar color)'),
        ('colorize_teams', 'Dislay team city, name, and abbreviation in the '
                           'team\'s color (as defined in the '
                           ':ref:`backend <scorebackends>`\'s ``team_colors`` '
                           'attribute)'),
        ('scroll_arrow', 'Value used for the ``{scroll}`` formatter to '
                         'indicate that more than one game is being tracked '
                         'for the currently-displayed backend'),
        ('refresh_icon', 'Text to display (in addition to any text currently '
                         'shown by the module) when refreshing scores. '
                         '**NOTE:** Depending on how quickly the update is '
                         'performed, the icon may not be displayed.'),
        ('team_format', 'One of ``name``, ``abbreviation``, or ``city``'),
    )

    backends = []
    favorite_icon = 'â˜…'
    color = None
    color_no_games = None
    colorize_teams = False
    scroll_arrow = 'â¬�'
    refresh_icon = 'âŸ³'
    team_format = 'name'

    output = {'full_text': ''}
    game_map = {}
    backend_id = 0

    on_upscroll = ['scroll_game', 1]
    on_downscroll = ['scroll_game', -1]
    on_leftclick = ['check_scores', 'click event']
    on_rightclick = ['cycle_backend', 1]
    on_doubleleftclick = ['launch_web']
    on_doublerightclick = ['reset_backend']

    def init(self):
        pass

    def update_thread(self):
        pass

    @property
    def current_backend(self):
        pass

    @property
    def current_scroll_index(self):
        pass

    @property
    def current_game_id(self):
        pass

    @property
    def current_game(self):
        pass

    def scroll_game(self, step=1):
        pass

    def cycle_backend(self, step=1):
        pass

    def reset_backend(self):
        pass

    def launch_web(self):
        pass

    @require(internet)
    def check_scores(self, force=False):
        pass

    def show_refresh_icon(self):
        pass

    def refresh_display(self):
        pass

    def run(self):
        pass
