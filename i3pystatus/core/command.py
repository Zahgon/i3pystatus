import logging
import shlex
import subprocess
from collections import namedtuple

CommandResult = namedtuple("Result", ['rc', 'out', 'err'])


def run_through_shell(command, enable_shell=False):
    """
    Retrieve output of a command.
    Returns a named tuple with three elements:

    * ``rc`` (integer) Return code of command.
    * ``out`` (string) Everything that was printed to stdout.
    * ``err`` (string) Everything that was printed to stderr.

    Don't use this function with programs that outputs lots of data since the
    output is saved in one variable.

    :param command: A string or a list of strings containing the name and
     arguments of the program.
    :param enable_shell: If set ot `True` users default shell will be invoked
     and given ``command`` to execute. The ``command`` should obviously be a
     string since shell does all the parsing.
    """
    pass


def execute(command, detach=False):
    """
    Runs a command in background. No output is retrieved. Useful for running GUI
    applications that would block click events.

    :param command: A string or a list of strings containing the name and
     arguments of the program.
    :param detach: If set to `True` the program will be executed using the
     `i3-msg` command. As a result the program is executed independent of
     i3pystatus as a child of i3 process. Because of how i3-msg parses its
     arguments the type of `command` is limited to string in this mode.
    """
    pass
