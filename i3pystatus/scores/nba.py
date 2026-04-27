from i3pystatus.core.util import internet, require
from i3pystatus.scores import ScoresBackend

import copy
import pytz
import re
import time
from datetime import datetime, timezone

LIVE_URL = 'https://www.nba.com/game/{id}'
API_URL = 'https://cdn.nba.com/static/json/liveData/scoreboard/todaysScoreboard_00.json'


class NBA(ScoresBackend):
    '''
    Backend to retrieve NBA scores. For usage examples, see :py:mod:`here
    <.scores>`.

    .. rubric:: Available formatters

    * `{home_team}` â€” Depending on the value of the ``team_format`` option,
      will contain either the home team's name, abbreviation, or city
    * `{home_score}` â€” Home team's current score
    * `{home_wins}` â€” Home team's number of wins
    * `{home_losses}` â€” Home team's number of losses
    * `{home_seed}` â€” During the playoffs, shows the home team's playoff seed.
      When not in the playoffs, this formatter will be blank.
    * `{home_favorite}` â€” Displays the value for the :py:mod:`.scores` module's
      ``favorite`` attribute, if the home team is one of the teams being
      followed. Otherwise, this formatter will be blank.
    * `{away_team}` â€” Depending on the value of the ``team_format`` option,
      will contain either the away team's name, abbreviation, or city
    * `{away_score}` â€” Away team's current score
    * `{away_wins}` â€” Away team's number of wins
    * `{away_losses}` â€” Away team's number of losses
    * `{away_seed}` â€” During the playoffs, shows the away team's playoff seed.
      When not in the playoffs, this formatter will be blank.
    * `{away_favorite}` â€” Displays the value for the :py:mod:`.scores` module's
      ``favorite`` attribute, if the away team is one of the teams being
      followed. Otherwise, this formatter will be blank.
    * `{time_remaining}` â€” Time remaining in the current quarter/OT period
    * `{quarter}` â€” Number of the current quarter
    * `{start_time}` â€” Start time of game in system's localtime (supports
      strftime formatting, e.g. `{start_time:%I:%M %p}`)
    * `{overtime}` â€” If the game ended in overtime, this formatter will show
      ``OT``. If the game ended in regulation, or has not yet completed, this
      formatter will be blank.

    .. rubric:: Team abbreviations

    * **ATL** â€” Atlanta Hawks
    * **BKN** â€” Brooklyn Nets
    * **BOS** â€” Boston Celtics
    * **CHA** â€” Charlotte Hornets
    * **CHI** â€” Chicago Bulls
    * **CLE** â€” Cleveland Cavaliers
    * **DAL** â€” Dallas Mavericks
    * **DEN** â€” Denver Nuggets
    * **DET** â€” Detroit Pistons
    * **GSW** â€” Golden State Warriors
    * **HOU** â€” Houston Rockets
    * **IND** â€” Indiana Pacers
    * **MIA** â€” Miami Heat
    * **MEM** â€” Memphis Grizzlies
    * **MIL** â€” Milwaukee Bucks
    * **LAC** â€” Los Angeles Clippers
    * **LAL** â€” Los Angeles Lakers
    * **MIN** â€” Minnesota Timberwolves
    * **NOP** â€” New Orleans Pelicans
    * **NYK** â€” New York Knicks
    * **OKC** â€” Oklahoma City Thunder
    * **ORL** â€” Orlando Magic
    * **PHI** â€” Philadelphia 76ers
    * **PHX** â€” Phoenix Suns
    * **POR** â€” Portland Trailblazers
    * **SAC** â€” Sacramento Kings
    * **SAS** â€” San Antonio Spurs
    * **TOR** â€” Toronto Raptors
    * **UTA** â€” Utah Jazz
    * **WAS** â€” Washington Wizards
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
        ('live_url', 'URL string to launch NBA Game Tracker. This value '
                     'should not need to be changed.'),
        ('api_url', 'Alternate URL string from which to retrieve score data. '
                    'Like, **live_url**, this value should not need to be '
                    'changed.'),
    )

    required = ()

    _default_colors = {
        'ATL': '#E2383F',
        'BKN': '#DADADA',
        'BOS': '#178D58',
        'CHA': '#00798D',
        'CHI': '#CD1041',
        'CLE': '#FDBA31',
        'DAL': '#006BB7',
        'DEN': '#5593C3',
        'DET': '#207EC0',
        'GSW': '#DEB934',
        'HOU': '#CD1042',
        'IND': '#FFBB33',
        'MIA': '#A72249',
        'MEM': '#628BBC',
        'MIL': '#4C7B4B',
        'LAC': '#ED174C',
        'LAL': '#FDB827',
        'MIN': '#35749F',
        'NOP': '#A78F59',
        'NYK': '#F68428',
        'OKC': '#F05033',
        'ORL': '#1980CB',
        'PHI': '#006BB7',
        'PHX': '#E76120',
        'POR': '#B03037',
        'SAC': '#7A58A1',
        'SAS': '#DADADA',
        'TOR': '#CD112C',
        'UTA': '#4B7059',
        'WAS': '#E51735',
    }

    _valid_teams = [x for x in _default_colors]
    _valid_display_order = ['in_progress', 'final', 'pregame', 'postponed']

    display_order = _valid_display_order
    format_no_games = 'NBA: No games'
    format = '[{scroll} ]NBA: [{away_favorite} ][{away_seed} ]{away_team} [{away_score} ]({away_wins}-{away_losses}) at [{home_favorite} ][{home_seed} ]{home_team} [{home_score} ]({home_wins}-{home_losses}) {game_status}'
    status_pregame = '{start_time:%H:%M %Z}'
    status_in_progress = '({time_remaining} {quarter})'
    status_final = '(Final[/{overtime}])'
    status_postponed = 'PPD'
    team_colors = _default_colors
    live_url = LIVE_URL
    api_url = API_URL

    # These will inherit from the Scores class if not overridden
    team_format = None

    def check_scores(self):
        pass

    def process_game(self, game):
        pass
