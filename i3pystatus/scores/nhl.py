from i3pystatus.core.util import internet, require
from i3pystatus.scores import ScoresBackend

import copy
import json
import pytz
import re
import time
from datetime import datetime
from urllib.request import urlopen

LIVE_URL = 'https://www.nhl.com/gamecenter/{id}'
SCOREBOARD_URL = 'https://www.nhl.com/scores'
API_URL = 'https://statsapi.web.nhl.com/api/v1/schedule?startDate={date:%Y-%m-%d}&endDate={date:%Y-%m-%d}&expand=schedule.teams,schedule.linescore,schedule.broadcasts.all&site=en_nhl&teamId='


class NHL(ScoresBackend):
    '''
    Backend to retrieve NHL scores. For usage examples, see :py:mod:`here
    <.scores>`.

    .. rubric:: Available formatters

    * `{home_team}` â€” Depending on the value of the ``team_format`` option,
      will contain either the home team's name, abbreviation, or city
    * `{home_score}` â€” Home team's current score
    * `{home_wins}` â€” Home team's number of wins
    * `{home_losses}` â€” Home team's number of losses
    * `{home_otl}` â€” Home team's number of overtime losses
    * `{home_favorite}` â€” Displays the value for the :py:mod:`.scores` module's
      ``favorite`` attribute, if the home team is one of the teams being
      followed. Otherwise, this formatter will be blank.
    * `{home_empty_net}` â€” Shows the value from the ``empty_net`` parameter
      when the home team's net is empty.
    * `{away_team}` â€” Depending on the value of the ``team_format`` option,
      will contain either the away team's name, abbreviation, or city
    * `{away_score}` â€” Away team's current score
    * `{away_wins}` â€” Away team's number of wins
    * `{away_losses}` â€” Away team's number of losses
    * `{away_otl}` â€” Away team's number of overtime losses
    * `{away_favorite}` â€” Displays the value for the :py:mod:`.scores` module's
      ``favorite`` attribute, if the away team is one of the teams being
      followed. Otherwise, this formatter will be blank.
    * `{away_empty_net}` â€” Shows the value from the ``empty_net`` parameter
      when the away team's net is empty.
    * `{period}` â€” Current period
    * `{venue}` â€” Name of arena where game is being played
    * `{start_time}` â€” Start time of game in system's localtime (supports
      strftime formatting, e.g. `{start_time:%I:%M %p}`)
    * `{overtime}` â€” If the game ended in overtime or a shootout, this
      formatter will show ``OT`` kor ``SO``. If the game ended in regulation,
      or has not yet completed, this formatter will be blank.

    .. rubric:: Playoffs

    In the playoffs, losses are not important (as the losses will be equal to
    the other team's wins). Therefore, it is a good idea during the playoffs to
    manually set format strings to exclude information on team losses. For
    example:

    .. code-block:: python

        from i3pystatus import Status
        from i3pystatus.scores import nhl

        status = Status()
        status.register(
            'scores',
            hints={'markup': 'pango'},
            colorize_teams=True,
            favorite_icon='<span size="small" color="#F5FF00">â˜…</span>',
            backends=[
                nhl.NHL(
                    favorite_teams=['CHI'],
                    format='[{scroll} ]NHL: [{away_favorite} ]{away_team} ({away_wins}) at [{home_favorite} ]{home_team} ({home_wins}) {game_status}'
                ),
            ],
        )

    .. rubric:: Team abbreviations

    * **ANA** â€” Anaheim Ducks
    * **ARI** â€” Arizona Coyotes
    * **BOS** â€” Boston Bruins
    * **BUF** â€” Buffalo Sabres
    * **CAR** â€” Carolina Hurricanes
    * **CBJ** â€” Columbus Blue Jackets
    * **CGY** â€” Calgary Flames
    * **CHI** â€” Chicago Blackhawks
    * **COL** â€” Colorado Avalanche
    * **DAL** â€” Dallas Stars
    * **DET** â€” Detroit Red Wings
    * **EDM** â€” Edmonton Oilers
    * **FLA** â€” Florida Panthers
    * **LAK** â€” Los Angeles Kings
    * **MIN** â€” Minnesota Wild
    * **MTL** â€” Montreal Canadiens
    * **NJD** â€” New Jersey Devils
    * **NSH** â€” Nashville Predators
    * **NYI** â€” New York Islanders
    * **NYR** â€” New York Rangers
    * **OTT** â€” Ottawa Senators
    * **PHI** â€” Philadelphia Flyers
    * **PIT** â€” Pittsburgh Penguins
    * **SEA** â€” Seattle Kraken
    * **SJS** â€” San Jose Sharks
    * **STL** â€” St. Louis Blues
    * **TBL** â€” Tampa Bay Lightning
    * **TOR** â€” Toronto Maple Leafs
    * **VAN** â€” Vancouver Canucks
    * **VGK** â€” Vegas Golden Knights
    * **WPG** â€” Winnipeg Jets
    * **WSH** â€” Washington Capitals
    '''
    interval = 300

    settings = (
        ('favorite_teams', 'List of abbreviations of favorite teams. Games '
                           'for these teams will appear first in the scroll '
                           'list. A detailed description of how games are '
                           'ordered can be found '
                           ':ref:`here <scores-game-order>`.'),
        ('all_games', 'If set to ``True``, all games will be present in '
                      'the scroll list. If set to ``False``, then only '
                      'games from **favorite_teams** will be present in '
                      'the scroll list.'),
        ('display_order', 'When **all_games** is set to ``True``, this '
                          'option will dictate the order in which games from '
                          'teams not in **favorite_teams** are displayed'),
        ('format_no_games', 'Format used when no tracked games are scheduled '
                            'for the current day (does not support formatter '
                            'placeholders)'),
        ('format', 'Format used to display game information'),
        ('status_pregame', 'Format string used for the ``{game_status}`` '
                           'formatter when the game has not started '),
        ('status_in_progress', 'Format string used for the ``{game_status}`` '
                               'formatter when the game is in progress'),
        ('status_final', 'Format string used for the ``{game_status}`` '
                         'formatter when the game has finished'),
        ('status_postponed', 'Format string used for the ``{game_status}`` '
                             'formatter when the game has been postponed'),
        ('empty_net', 'Value for the ``{away_empty_net}`` or '
                      '``{home_empty_net}`` formatter when the net is empty. '
                      'When the net is not empty, these formatters will be '
                      'empty strings.'),
        ('team_colors', 'Dictionary mapping team abbreviations to hex color '
                        'codes. If overridden, the passed values will be '
                        'merged with the defaults, so it is not necessary to '
                        'define all teams if specifying this value.'),
        ('team_format', 'One of ``name``, ``abbreviation``, or ``city``. If '
                        'not specified, takes the value from the ``scores`` '
                        'module.'),
        ('date', 'Date for which to display game scores, in **YYYY-MM-DD** '
                 'format. If unspecified, the current day\'s games will be '
                 'displayed starting at 10am Eastern time, with last '
                 'evening\'s scores being shown before then. This option '
                 'exists primarily for troubleshooting purposes.'),
        ('live_url', 'URL string to launch NHL GameCenter. This value should '
                     'not need to be changed.'),
        ('scoreboard_url', 'Link to the NHL.com scoreboard page. Like '
                           '**live_url**, this value should not need to be '
                           'changed.'),
        ('api_url', 'Alternate URL string from which to retrieve score data. '
                    'Like **live_url**, this value should not need to be '
                    'changed.'),
    )

    required = ()

    _default_colors = {
        'ANA': '#B4A277',
        'ARI': '#AC313A',
        'BOS': '#F6BD27',
        'BUF': '#1568C5',
        'CAR': '#FA272E',
        'CBJ': '#1568C5',
        'CGY': '#D23429',
        'CHI': '#CD0E24',
        'COL': '#9F415B',
        'DAL': '#058158',
        'DET': '#E51937',
        'EDM': '#2F6093',
        'FLA': '#E51837',
        'LAK': '#DADADA',
        'MIN': '#176B49',
        'MTL': '#C8011D',
        'NJD': '#CC0000',
        'NSH': '#FDB71A',
        'NYI': '#F8630D',
        'NYR': '#1576CA',
        'OTT': '#C50B2F',
        'PHI': '#FF690B',
        'PIT': '#FFB81C',
        'SEA': '#96D8D8',
        'SJS': '#007888',
        'STL': '#1764AD',
        'TBL': '#296AD5',
        'TOR': '#296AD5',
        'VAN': '#0454FA',
        'VGK': '#B4975A',
        'WPG': '#1568C5',
        'WSH': '#E51937',
    }

    _valid_teams = [x for x in _default_colors]
    _valid_display_order = ['in_progress', 'final', 'pregame', 'postponed']

    display_order = _valid_display_order
    format_no_games = 'NHL: No games'
    format = '[{scroll} ]NHL: [{away_favorite} ]{away_team} [{away_score} ]({away_wins}-{away_losses}-{away_otl}) at [{home_favorite} ]{home_team} [{home_score} ]({home_wins}-{home_losses}-{home_otl}) {game_status}'
    status_pregame = '{start_time:%H:%M %Z}'
    status_in_progress = '({time_remaining} {period})'
    status_final = '(Final[/{overtime}])'
    status_postponed = 'PPD'
    empty_net = 'EN'
    team_colors = _default_colors
    live_url = LIVE_URL
    scoreboard_url = SCOREBOARD_URL
    api_url = API_URL

    # These will inherit from the Scores class if not overridden
    team_format = None

    @require(internet)
    def check_scores(self):
        pass

    def process_game(self, game):
        pass
