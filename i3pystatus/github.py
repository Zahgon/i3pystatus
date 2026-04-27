import copy
import json
import re
import threading
import time
from urllib.request import urlopen

from i3pystatus import IntervalModule, formatp
from i3pystatus.core import ConfigError
from i3pystatus.core.desktop import DesktopNotification
from i3pystatus.core.util import user_open, internet, require

try:
    import requests
    HAS_REQUESTS = True
except ImportError:
    HAS_REQUESTS = False

API_METHODS_URL = 'https://www.githubstatus.com/api/v2/summary.json'
STATUS_URL = 'https://www.githubstatus.com'
NOTIFICATIONS_URL = 'https://github.com/notifications'
AUTH_URL = 'https://api.github.com/notifications'


class Github(IntervalModule):
    '''
    This module checks the GitHub system status, and optionally the number of
    unread notifications.

    .. versionchanged:: 3.36
        Module now checks system status in addition to unread notifications.

    .. note::
        For notification checking, the following is required:

        - The requests_ module must be installed.
        - Either ``access_token`` (recommended) or ``username`` and
          ``password`` must be used to authenticate to GitHub.

        Using an access token is the recommended authentication method. Click
        here__ to generate a new access token. Fill in the **Token
        description** box, and enable the **notifications** scope by checking
        the appropriate checkbox. Then, click the **Generate token** button.

        .. important::
            An access token is the only supported means of authentication for
            this module, if `2-factor authentication`_ is enabled.

        .. _requests: https://pypi.python.org/pypi/requests
        .. __: https://github.com/settings/tokens/new
        .. _`2-factor authentication`: https://help.github.com/articles/about-two-factor-authentication/

        See here__ for more information on GitHub's authentication API.

        .. __: https://developer.github.com/v3/#authentication

        If you would rather use a username and password pair, you can either
        pass them as arguments when registering the module, or use i3pystatus'
        :ref:`credential management <credentials>` support to store them in a
        keyring. Keep in mind that if you do not pass a ``username`` or
        ``password`` parameter when registering the module, i3pystatus will
        still attempt to retrieve these values from a keyring if the keyring_
        Python module is installed. This could result in i3pystatus aborting
        during startup if it cannot find a usable keyring backend. If you do
        not plan to use credential management at all in i3pystatus, then you
        should either ensure that A) keyring_ is not installed, or B) both
        keyring_ and keyrings.alt_ are installed, to avoid this error.

        .. _keyring: https://pypi.python.org/pypi/keyring
        .. _keyrings.alt: https://pypi.python.org/pypi/keyrings.alt


    .. rubric:: Available formatters

    * `{status}` â€” Current GitHub status. This formatter can be different
      depending on the current outage status (``none``, ``minor``, ``major``,
      or ``critical``). The content displayed for each of these statuses is
      defined in the **status** config option.
    * `{unread}` â€” When there are unread notifications, this formatter will
      contain the value of the **unread_marker** marker config option.
      there are no unread notifications, it formatter will be an empty string.
    * `{unread_count}` â€” The number of unread notifications
      notifications, it will be an empty string.
    * `{update_error}` â€” When an error is encountered updating this module,
      this formatter will be set to the value of the **update_error**
      config option.

    .. rubric:: Click events

    This module responds to 4 different click events:

    - **Left-click** â€” Forces an update of the module.
    - **Right-click** â€” Triggers a desktop notification showing the most recent
      update to the GitHub status. This is useful when the status changes when
      you are away from your computer, so that the updated status can be seen
      without visiting the `GitHub Status Dashboard`_. This click event
      requires **notify_status** to be set to ``True``.
    - **Double left-click** â€” Opens the GitHub `notifications page`_ in your web
      browser.
    - **Double right-click** â€” Opens the `GitHub Status Dashboard`_ in your web
      browser.

    .. rubric:: Desktop notifications

    .. versionadded:: 3.36

    If **notify_status** is set to ``True``, a notification will be displayed
    when the status reported by the `GitHub Status API`_ changes.

    If **notify_unread** is set to ``True``, a notification will be displayed
    when new unread notifications are found. Double-clicking the module will
    launch the GitHub notifications dashboard in your browser.

    .. note::
        A notification will be displayed if there was a problem querying the
        `GitHub Status API`_, irrespective of whether or not **notify_status**
        or **notify_unread** is set to ``True``.

    .. rubric:: Example configuration

    The below example enables desktop notifications, enables Pango hinting for
    differently-colored **update_error** and **refresh_icon** text, and alters
    the both the status text and the colors used to visually denote the current
    status level. It also sets the log level to debug, for troubleshooting
    purposes.

    .. code-block:: python

        status.register(
            'github',
            log_level=logging.DEBUG,
            notify_status=True,
            notify_unread=True,
            access_token='0123456789abcdef0123456789abcdef01234567',
            hints={'markup': 'pango'},
            update_error='<span color="#af0000">!</span>',
            refresh_icon='<span color="#ff5f00">âŸ³</span>',
            status={
                'none': 'âœ“',
                'minor': '!',
                'major': '!!',
                'critical': '!!!',
            },
            colors={
                'none': '#008700',
                'minor': '#d7ff00',
                'major': '#af0000',
                'critical': '#640000',
            },
        )

    .. note::
        Setting debug logging and authenticating with an access token will
        include the access token in the log file, as the notification URL is
        logged at this level.

    .. _`GitHub Status API`: https://www.githubstatus.com/api
    .. _`GitHub Status Dashboard`: https://www.githubstatus.com/
    .. _`notifications page`: https://github.com/notifications

    .. rubric:: Extended string formatting

    .. versionadded:: 3.36

    This module supports the :ref:`formatp <formatp>` extended string format
    syntax. This allows for values to be hidden when they evaluate as False.
    The default ``format`` string value for this module makes use of this
    syntax to conditionally show the value of the ``update_error`` config value
    when the backend encounters an error during an update, but this can also
    be used to only show the number of unread notifications when that number is
    not **0**. The below example would show the unread count as **(3)** when
    there are 3 unread notifications, but would show nothing when there are no
    unread notifications.

    .. code-block:: python

        status.register(
            'github',
            notify_status=True,
            notify_unread=True,
            access_token='0123456789abcdef0123456789abcdef01234567',
            format='{status}[ ({unread_count})][ {update_error}]'
        )
    '''
    settings = (
        ('format', 'format string'),
        ('status', 'Dictionary mapping statuses to the text which represents '
                   'that status type. This defaults to ``GitHub`` for all '
                   'status types.'),
        ('colors', 'Dictionary mapping statuses to the color used to display '
                   'the status text'),
        ('refresh_icon', 'Text to display (in addition to any text currently '
                         'shown by the module) when refreshing the GitHub '
                         'status. **NOTE:** Depending on how quickly the '
                         'update is performed, the icon may not be displayed.'),
        ('update_error', 'Value for the ``{update_error}`` formatter when an '
                         'error is encountered while checking GitHub status'),
        ('keyring_backend', 'alternative keyring backend for retrieving '
                            'credentials'),
        ('username', ''),
        ('password', ''),
        ('access_token', ''),
        ('unread_marker', 'Defines the string that the ``{unread}`` formatter '
                          'shows when there are pending notifications'),
        ('notify_status', 'Set to ``True`` to display a desktop notification '
                          'on status changes'),
        ('notify_unread', 'Set to ``True`` to display a desktop notification '
                          'when new notifications are detected'),
        ('unread_notification_template',
            'String with no more than one ``%d``, which will be replaced by '
            'the number of new unread notifications. Useful for those with '
            'non-English locales who would like the notification to be in '
            'their native language. The ``%d`` can be omitted if desired.'),
        ('api_methods_url', 'URL from which to retrieve the API endpoint URL '
                            'which this module will use to check the GitHub '
                            'Status'),
        ('status_url', 'The URL to the status page (opened when the module is '
                       'double-clicked with the right mouse button'),
        ('notifications_url', 'The URL to the GitHub notifications page '
                              '(opened when the module is double-clicked with '
                              'the left mouse button'),
    )

    # Defaults for module configurables
    _default_colors = {
        'none': '#28a745',
        'maintenance': '#4f8cc9',
        'minor': '#dbab09',
        'major': '#e36209',
        'critical': '#dc3545',
    }

    # Module configurables
    format = '{status}[ {unread}][ {update_error}]'
    status = {}
    colors = _default_colors
    refresh_icon = 'âŸ³'
    update_error = '!'
    username = ''
    password = ''
    access_token = ''
    unread_marker = 'â€¢'
    notify_status = False
    notify_unread = False
    unread_notification_template = 'You have %d new notification(s)'
    api_methods_url = API_METHODS_URL
    status_url = STATUS_URL
    notifications_url = NOTIFICATIONS_URL

    # Global configurables
    interval = 600
    max_error_len = 50
    keyring_backend = None

    # Other
    unread = ''
    unknown_color = None
    unknown_status = '?'
    failed_update = False
    __previous_json = None
    __current_json = None
    new_unread = None
    previous_unread = None
    current_unread = None
    config_error = None
    data = {'status': '',
            'unread': 0,
            'unread_count': '',
            'update_error': ''}
    output = {'full_text': '', 'color': None}

    # Click events
    on_leftclick = ['perform_update']
    on_rightclick = ['show_status_notification']
    on_doubleleftclick = ['launch_notifications_url']
    on_doublerightclick = ['launch_status_url']

    @require(internet)
    def launch_status_url(self):
        pass

    @require(internet)
    def launch_notifications_url(self):
        pass

    def init(self):
        pass

    def update_loop(self):
        pass

    @require(internet)
    def status_api_request(self, url):
        pass

    def detect_status_change(self, response=None):
        pass

    @staticmethod
    def notify(message):
        pass

    def skip_notify(self, message):
        pass

    def show_status_notification(self):
        pass

    def show_unread_notification(self):
        pass

    @require(internet)
    def perform_update(self):
        pass

    @property
    def current_incidents(self):
        pass

    @property
    def previous_incidents(self):
        pass

    @property
    def current_status(self):
        pass

    @property
    def previous_status(self):
        pass

    @property
    def current_status_description(self):
        pass

    @require(internet)
    def update_status(self):
        pass

    @require(internet)
    def update_unread(self):
        # Reset the new_unread attribute to prevent spurious notifications
        pass

    def refresh_display(self):
        pass

    def run(self):
        pass
