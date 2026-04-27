import json
import time
import urllib.error
import urllib.parse
import urllib.request

from i3pystatus import IntervalModule
from i3pystatus.core.util import internet, require


class ElementCall(IntervalModule):
    """
    Displays the number of active participants in an Element Call room on a
    Matrix homeserver. Uses the Matrix Client-Server API to read
    ``org.matrix.msc3401.call.member`` state events and counts members whose
    session has not yet expired.

    Requires a Matrix access token with read access to the target room.

    .. rubric:: Available formatters

    * ``{participants}`` â€” number of active call participants
    * ``{room_id}`` â€” the Matrix room ID being monitored
    * ``{room_alias}`` â€” the room_alias setting value

    .. rubric:: Example configuration

    .. code-block:: python

        status.register(
            "element_call",
            homeserver="https://matrix.example.com",
            access_token="syt_...",
            room_id="!abc123:example.com",
            format_active="\U0001F4DE {participants}",
            format_empty="\U0001F4DE",
            interval=15,
        )
    """

    settings = (
        ("homeserver", "Base URL of your Matrix homeserver (e.g. https://matrix.example.com)"),
        ("access_token", "Matrix access token with read access to the room"),
        ("room_id", "Matrix room ID to monitor (e.g. !abc123:example.com)"),
        ("room_alias", "Human-readable label used in {room_alias} formatter"),
        ("format_active", "Format string when participants > 0"),
        ("format_empty", "Format string when no one is in the call"),
        ("format_error", "Format string on API error"),
        ("color_active", "Color when participants > 0"),
        ("color_empty", "Color when call is empty"),
        ("color_error", "Color on API error"),
        ("interval", "Polling interval in seconds"),
    )

    homeserver = ""
    access_token = ""
    room_id = ""
    room_alias = ""
    format_active = "\U0001F4DE {participants}"
    format_empty = ""
    format_error = "\U0001F4DE ?"
    color_active = "#00FF00"
    color_empty = "#888888"
    color_error = "#FF0000"
    interval = 15

    # MSC3401 state event type used by Element Call
    _CALL_MEMBER_TYPE = "org.matrix.msc3401.call.member"

    @require(internet)
    def run(self):
        pass

    def _resolve_room_id(self, room_id_or_alias):
        """Resolve a room alias (#name:server) to a room ID (!id:server) if needed."""
        pass

    def _count_participants(self):
        """Return the number of active call participants in the room."""
        pass

    def _membership_active(self, membership, now_ms, origin_ts=0):
        """Return True if this membership entry has not yet expired."""
        pass
