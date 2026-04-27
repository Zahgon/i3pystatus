import os

from i3pystatus import Module


class Uname(Module):
    """
    uname(1) like module.

    .. rubric:: Available formatters

    * `{sysname}` â€” operating system name
    * `{nodename}` â€” name of machine on network (implementation-defined)
    * `{release}` â€” operating system release
    * `{version}` â€” operating system version
    * `{machine}` â€” hardware identifier
    """

    format = "{sysname} {release}"
    settings = (
        ("format", "format string used for output"),
    )

    def init(self):
        pass
