from i3pystatus import IntervalModule
from requests import get, post
import json
import subprocess
import time


# Global cache for sharing state data between multiple Hassio instances
_hassio_cache = {}
_hassio_cache_time = {}


class Hassio(IntervalModule):
    """
    Displays the state of a Homeassistant.io entity
    Requires the PyPI package `requests`

    Left click toggles the entity state (for switches, lights, etc.)
    Middle click forces a refresh of the current state.
    Right click opens the Home Assistant dashboard in a browser.

    For monitoring multiple entities efficiently, see :py:mod:`hassio_multi`.

    .. rubric:: Available formatters

    * ``{friendly_name}`` â€” friendly name of the entity
    * ``{entity_id}`` â€” entity ID
    * ``{state}`` â€” current state
    * ``{last_change}`` â€” last state change time
    * ``{last_update}`` â€” last update time
    * Any entity attribute (e.g., ``{current_temperature}``, ``{brightness}``)

    .. rubric:: Example with entity attributes

    ::

        # Display thermostat current temperature
        status.register("hassio",
            entity_id="climate.garage_thermostat_2",
            hassio_url="http://homeassistant.local:8123",
            hassio_token="your_token",
            format="Garage: {current_temperature}Â°F",
        )
    """

    settings = (
        ("entity_id", "Entity ID to track."),
        ("hassio_url", "URL to your hassio install. (default: "
            "https://localhost:8123)"),
        ("hassio_token", "HomeAssistant API token "
            "(https://developers.home-assistant.io/docs/auth_api/#long-lived-access-token)"),
        ("interval", "Update interval."),
        ("desired_state", "The desired or \"good\" state of the entity."),
        ("good_color", "Color of text while entity is in desired state"),
        ("bad_color", "Color of text while entity is not in desired state"),
        "format",
        ("hide_state", "State value used to determine if the results should be hidden"),
        ("browser_cmd", "Command to open browser (default: xdg-open)"),
        ("use_cache", "Share state cache with other Hassio instances (reduces API calls)"),
        ("cache_timeout", "How long to use cached data in seconds (default: same as interval)"),
    )
    required = ("hassio_url", "hassio_token", "entity_id")
    desired_state = "on"
    good_color = "#00FF00"     # green
    bad_color = "#FF0000"      # red
    interval = 15
    hide_state = None
    format = "{friendly_name}: {state}"
    browser_cmd = "xdg-open"
    use_cache = False
    cache_timeout = None

    on_leftclick = "toggle"
    on_middleclick = "refresh"
    on_rightclick = "open_dashboard"

    def _get_headers(self):
        pass

    def _fetch_entity(self, entity_id):
        """Fetch a single entity state, optionally using cache"""
        pass

    def run(self):
        pass

    def toggle(self):
        """Toggle the entity state (for switches, lights, input_booleans, etc.)"""
        pass

    def refresh(self):
        """Force a refresh of the current state"""
        pass

    def open_dashboard(self):
        """Open the Home Assistant dashboard in a browser"""
        pass
