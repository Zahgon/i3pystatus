from i3pystatus.core.util import internet, require
from i3pystatus.scores import ScoresBackend

import copy
import json
import pytz
import re
import time
from datetime import datetime
from urllib.request import urlopen

LIVE_URL = 'https://www.mlb.com/gameday/{id}'
SCOREBOARD_URL = 'http://m.mlb.com/scoreboard'
API_URL = 'https://statsapi.mlb.com/api/v1/schedule?sportId=1,51&date={date:%Y-%m-%d}&gameTypes=E,S,R,A,F,D,L,W&hydrate=team(),linescore(matchup,runners),stats,game(content(media(featured,epg),summary),tickets),seriesStatus(useOverride=true)&useLatestGames=false&language=en&leagueId=103,104,420'


class MLB(ScoresBackend):
    '''
    Backend to retrieve MLB scores. For usage examples, see :py:mod:`here
    <.scores>`.

    .. rubric:: Available formatters

    * `{home_team}` â€” Depending on the value of the ``team_format`` option,
      will contain either the home team's name, abbreviation, or city
    * `{home_score}` â€” Home team's current score
    * `{home_wins}` â€” Home team's number of wins
    * `{home_losses}` â€” Home team's number of losses
    * `{home_favorite}` â€” Displays the value for the :py:mod:`.scores` module's
      ``favorite`` attribute, if the home team is one of the teams being
      followed. Otherwise, this formatter will be blank.
    * `{away_team}` â€” Depending on the value of the ``team_format`` option,
      will contain either the away team's name, abbreviation, or city
    * `{away_score}` â€” Away team's current score
    * `{away_wins}` â€” Away team's number of wins
    * `{away_losses}` â€” Away team's number of losses
    * `{away_favorite}` â€” Displays the value for the :py:mod:`.scores` module's
      ``favorite`` attribute, if the away team is one of the teams being
      followed. Otherwise, this formatter will be blank.
    * `{top_bottom}` â€” Displays the value of either ``inning_top`` or
      ``inning_bottom`` based on whether the game is in the top or bottom of an
      inning.
    * `{inning}` â€” Current inning
    * `{outs}` â€” Number of outs in current inning
    * `{venue}` â€” Name of ballpark where game is being played
    * `{start_time}` â€” Start time of game in system's localtime (supports
      strftime formatting, e.g. `{start_time:%I:%M %p}`)
    * `{delay}` â€” Reason for delay, if game is currently delayed. Otherwise,
      this formatter will be blank.
    * `{postponed}` â€” Reason for postponement, if game has been postponed.
      Otherwise, this formatter will be blank.
    * `{suspended}` â€” Reason for suspension, if game has been suspended.
      Otherwise, this formatter will be blank.
    * `{extra_innings}` â€” When a game lasts longer than 9 innings, this
      formatter will show that number of innings. Otherwise, it will blank.

    .. rubric:: Team abbreviations

    * **ARI** â€” Arizona Diamondbacks
    * **ATL** â€” Atlanta Braves
    * **BAL** â€” Baltimore Orioles
    * **BOS** â€” Boston Red Sox
    * **CHC** â€” Chicago Cubs
    * **CIN** â€” Cincinnati Reds
    * **CLE** â€” Cleveland Guardians
    * **COL** â€” Colorado Rockies
    * **CWS** â€” Chicago White Sox
    * **DET** â€” Detroit Tigers
    * **HOU** â€” Houston Astros
    * **KC** â€” Kansas City Royals
    * **LAA** â€” Los Angeles Angels of Anaheim
    * **LAD** â€” Los Angeles Dodgers
    * **MIA** â€” Miami Marlins
    * **MIL** â€” Milwaukee Brewers
    * **MIN** â€” Minnesota Twins
    * **NYY** â€” New York Yankees
    * **NYM** â€” New York Mets
    * **OAK** â€” Oakland Athletics
    * **PHI** â€” Philadelphia Phillies
    * **PIT** â€” Pittsburgh Pirates
    * **SD** â€” San Diego Padres
    * **SEA** â€” Seattle Mariners
    * **SF** â€” San Francisco Giants
    * **STL** â€” St. Louis Cardinals
    * **TB** â€” Tampa Bay Rays
    * **TEX** â€” Texas Rangers
    * **TOR** â€” Toronto Blue Jays
    * **WSH** â€” Washington Nationals
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
        ('status_suspended', 'Format string used for the ``{game_status}`` '
                             'formatter when the game has been suspended'),
        ('inning_top', 'Value for the ``{top_bottom}`` formatter when game '
                       'is in the top half of an inning'),
        ('inning_bottom', 'Value for the ``{top_bottom}`` formatter when game '
                          'is in the bottom half of an inning'),
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
        ('live_url', 'Alternate URL string to launch MLB Gameday. This value '
                     'should not need to be changed'),
        ('scoreboard_url', 'Link to the MLB.com scoreboard page. Like '
                           '**live_url**, this value should not need to be '
                           'changed.'),
        ('api_url', 'Alternate URL string from which to retrieve score data. '
                    'Like **live_url*** this value should not need to be '
                    'changed.'),
    )

    required = ()

    _default_colors = {
        'AZ': '#A71930',
        'ATL': '#CE1141',
        'BAL': '#DF4601',
        'BOS': '#BD3039',
        'CHC': '#004EC1',
        'CIN': '#C6011F',
        'CLE': '#E31937',
        'COL': '#5E5EB6',
        'CWS': '#DADADA',
        'DET': '#FF6600',
        'HOU': '#EB6E1F',
        'KC': '#0046DD',
        'LAA': '#BA0021',
        'LAD': '#005A9C',
        'MIA': '#00A3E0',
        'MIL': '#0747CC',
        'MIN': '#D31145',
        'NYY': '#0747CC',
        'NYM': '#FF5910',
        'OAK': '#006659',
        'PHI': '#E81828',
        'PIT': '#FFCC01',
        'SD': '#FFC425',
        'SEA': '#2E8B90',
        'SF': '#FD5A1E',
        'STL': '#B53B30',
        'TB': '#8FBCE6',
        'TEX': '#C0111F',
        'TOR': '#0046DD',
        'WSH': '#C70003',
    }

    _valid_teams = [x for x in _default_colors]
    _valid_display_order = ['in_progress', 'suspended', 'final', 'pregame', 'postponed']

    display_order = _valid_display_order
    format_no_games = 'MLB: No games'
    format = '[{scroll} ]MLB: [{away_favorite} ]{away_team} [{away_score} ]({away_wins}-{away_losses}) at [{home_favorite} ]{home_team} [{home_score} ]({home_wins}-{home_losses}) {game_status}'
    status_pregame = '{start_time:%H:%M %Z}[ ({delay} Delay)]'
    status_in_progress = '({top_bottom} {inning}, {outs} Out)[ ({delay} Delay)]'
    status_final = '(Final[/{extra_innings}])'
    status_postponed = '(PPD: {postponed})'
    status_suspended = '(Suspended: {suspended})'
    inning_top = 'Top'
    inning_bottom = 'Bot'
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
