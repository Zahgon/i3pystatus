from i3pystatus import IntervalModule
from i3pystatus.core.command import run_through_shell


class Shell(IntervalModule):
    """
    Shows output of shell command

    .. rubric:: Available formatters

    * `{output}` â€” just the striped command output without newlines
    """

    color = "#FFFFFF"
    error_color = "#FF0000"
    ignore_empty_stdout = False

    settings = (
        ("command", "command to be executed"),
        ("ignore_empty_stdout", "Let the block be empty"),
        ("color", "standard color"),
        ("error_color", "color to use when non zero exit code is returned"),
        "format"
    )

    required = ("command",)
    format = "{output}"

    def run(self):
        pass
