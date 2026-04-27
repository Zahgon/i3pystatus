from i3pystatus import IntervalModule
from requests import get, post
import json
import subprocess


class HassioMulti(IntervalModule):
    """
    Displays multiple Homeassistant.io entities with a single API call.
    Requires the PyPI package `requests`

    This is more efficient than multiple Hassio instances when monitoring
    several entities, as it fetches all states in one bulk API call.

    Left click cycles to the next entity.
    Right click toggles the current entity.
    Middle click refreshes all entities.
    Scroll up/down cycles through entities.

    .. rubric:: Available formatters

    * ``{friendly_name}`` â€” friendly name of current entity
    * ``{entity_id}`` â€” entity ID
    * ``{state}`` â€” current state
    * ``{last_change}`` â€” last state change time
    * ``{last_update}`` â€” last update time
    * ``{entity_index}`` â€” current entity index (1-based)
    * ``{entity_count}`` â€” total number of entities
    * Any entity attribute (e.g., ``{current_temperature}``, ``{brightness}``)

    .. rubric:: Example usage

    ::

        status.register("hassio_multi",
            entity_ids=["light.living_room", "switch.fan", "sensor.temperature"],
            hassio_url="http://homeassistant.local:8123",
            hassio_token="your_token_here",
            format="{friendly_name}: {state} [{entity_index}/{entity_count}]",
        )
    """

    settings = (
        ("entity_ids", "List of entity IDs to track."),
        ("hassio_url", "URL to your hassio install."),
        ("hassio_token", "HomeAssistant API token."),
        ("interval", "Update interval."),
        ("desired_state", "The desired or \"good\" state of entities."),
        ("good_color", "Color of text while entity is in desired state"),
        ("bad_color", "Color of text while entity is not in desired state"),
        "format",
        ("hide_state", "State value used to hide an entity from display"),
        ("browser_cmd", "Command to open browser (default: xdg-open)"),
    )
    required = ("hassio_url", "hassio_token", "entity_ids")
    desired_state = "on"
    good_color = "#00FF00"
    bad_color = "#FF0000"
    interval = 15
    hide_state = None
    format = "{friendly_name}: {state}"
    browser_cmd = "xdg-open"

    on_leftclick = "next_entity"
    on_rightclick = "toggle"
    on_middleclick = "refresh"
    on_upscroll = "prev_entity"
    on_downscroll = "next_entity"

    _entity_index = 0
    _entities_data = []

    def _get_headers(self):
        pass

    def _fetch_all_states(self):
        """Fetch all entity states in one API call"""
        pass

    def run(self):
        pass

    def _get_current_entity_id(self):
        """Get the entity_id of the currently displayed entity"""
        pass

    def next_entity(self):
        """Cycle to next entity"""
        pass

    def prev_entity(self):
        """Cycle to previous entity"""
        pass

    def toggle(self):
        """Toggle the current entity state"""
        pass

    def refresh(self):
        """Force refresh all entities"""
        pass

    def open_dashboard(self):
        """Open the Home Assistant dashboard in a browser"""
        pass

