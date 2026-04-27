import docker
from i3pystatus import IntervalModule


class Docker(IntervalModule):
    """
    Display information about docker containers.

    Formatter accepts dict key's. e.g:

    containers[key_value] : containers[running]

    Requires: docker

    .. rubric:: Available formatters

    * `{containers}` â€” dictionary of information related to containers in docker
            `total` - total number of containers in docker e.g:
            status - total number of containers currently in the specified status e.g: `containers[running]`
    * `{volumes}` â€” dictionary of information related to volumes
            `count` - total count of volumes
            `volume_name` - specifies the volume_name to get information for e.g: `volumes[volume332]`
    * `{images}` â€” dictionary of information related to docker images
            `count` - total count of images in docker
    """

    settings = (
        "format",
        "color",
        ("interval", "Update interval (in seconds)"),
    )
    color = None
    interval = 5
    format = "containers: {containers[running]} running/{containers[total]} total"

    def run(self):
        pass
