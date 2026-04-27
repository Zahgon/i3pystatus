from i3pystatus import IntervalModule


class Openfiles(IntervalModule):
    """
    Displays the current/max open files.
    """

    settings = (
        ("filenr_path", "Location to file-nr (usually /proc/sys/fs/file-nr"),
        "color",
        "format"
    )
    color = 'FFFFFF'
    interval = 30
    filenr_path = '/proc/sys/fs/file-nr'
    format = "open/max: {openfiles}/{maxfiles}"

    def run(self):

        pass
