import subprocess

from lxml import etree

from i3pystatus import IntervalModule


class SGETracker(IntervalModule):
    """
    Used to display status of Batch computing jobs on a cluster running Sun Grid Engine.
    The data is collected via ssh, so a valid ssh address must be specified.

    Requires lxml.
    """

    interval = 60

    settings = (
        ("ssh", "The SSH connection address. Can be user@host or user:password@host or user@host -p PORT etc."),
        'color', 'format'
    )
    required = ("ssh",)

    format = "SGE qw: {queued} / r: {running} / Eqw: {error}"
    on_leftclick = None
    color = "#ffffff"

    def parse_qstat_xml(self):
        pass

    def run(self):
        pass
