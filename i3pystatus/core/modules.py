import html
import inspect
import traceback

from i3pystatus.core.settings import SettingsBase
from i3pystatus.core.threading import Manager
from i3pystatus.core.util import (convert_position,
                                  MultiClickHandler)
from i3pystatus.core.command import execute


def is_method_of(method, object):
    """Decide whether ``method`` is contained within the MRO of ``object``."""
    pass


class Module(SettingsBase):
    position = 0

    settings = (
        ('on_leftclick', "Callback called on left click (see :ref:`callbacks`)"),
        ('on_middleclick', "Callback called on middle click (see :ref:`callbacks`)"),
        ('on_rightclick', "Callback called on right click (see :ref:`callbacks`)"),
        ('on_upscroll', "Callback called on scrolling up (see :ref:`callbacks`)"),
        ('on_downscroll', "Callback called on scrolling down (see :ref:`callbacks`)"),
        ('on_doubleleftclick', "Callback called on double left click (see :ref:`callbacks`)"),
        ('on_doubleleftclick', "Callback called on double left click (see :ref:`callbacks`)"),
        ('on_doublemiddleclick', "Callback called on double middle click (see :ref:`callbacks`)"),
        ('on_doublerightclick', "Callback called on double right click (see :ref:`callbacks`)"),
        ('on_doubleupscroll', "Callback called on double scroll up (see :ref:`callbacks`)"),
        ('on_doubledownscroll', "Callback called on double scroll down (see :ref:`callbacks`)"),
        ('on_otherclick', "Callback called on other click (see :ref:`callbacks`)"),
        ('on_doubleotherclick', "Callback called on double other click (see :ref:`callbacks`)"),
        ('on_change', "Callback called when output is changed (see :ref:`callbacks`)"),
        ('multi_click_timeout', "Time (in seconds) before a single click is executed."),
        ('hints', "Additional output blocks for module output (see :ref:`hints`)"),
    )

    on_leftclick = None
    on_middleclick = None
    on_rightclick = None
    on_upscroll = None
    on_downscroll = None
    on_doubleleftclick = None
    on_doublemiddleclick = None
    on_doublerightclick = None
    on_doubleupscroll = None
    on_doubledownscroll = None

    on_otherclick = None
    on_change = None
    on_doubleotherclick = None

    multi_click_timeout = 0.25

    hints = {"markup": "none"}

    def __init__(self, *args, **kwargs):
        self._output = None
        super(Module, self).__init__(*args, **kwargs)
        self.__multi_click = MultiClickHandler(self.__button_callback_handler,
                                               self.multi_click_timeout)

    @property
    def output(self):
        pass

    @output.setter
    def output(self, value):
        pass

    def registered(self, status_handler):
        """Called when this module is registered with a status handler"""
        pass

    def inject(self, json):
        pass

    def run(self):
        pass

    def send_output(self):
        """Send a status update with the current module output"""
        pass

    def __log_button_event(self, button, cb, args, action, **kwargs):
        pass

    def __button_callback_handler(self, button, cb, **kwargs):

        pass

    def on_click(self, button, **kwargs):
        """
        Maps a click event with its associated callback.

        Currently implemented events are:

        ============  ================  =========
        Event         Callback setting  Button ID
        ============  ================  =========
        Left click    on_leftclick      1
        Middle click  on_middleclick    2
        Right click   on_rightclick     3
        Scroll up     on_upscroll       4
        Scroll down   on_downscroll     5
        Others        on_otherclick     > 5
        ============  ================  =========

        The action is determined by the nature (type and value) of the callback
        setting in the following order:

        1. If null callback (``None``), no action is taken.
        2. If it's a `python function`, call it and pass any additional
           arguments.
        3. If it's name of a `member method` of current module (string), call
           it and pass any additional arguments.
        4. If the name does not match with `member method` name execute program
           with such name.

        .. seealso:: :ref:`callbacks` for more information about
         callback settings and examples.

        :param button: The ID of button event received from i3bar.
        :param kwargs: Further information received from i3bar like the
         positions of the mouse where the click occurred.
        :return: Returns ``True`` if a valid callback action was executed.
         ``False`` otherwise.
        """
        pass

    def move(self, position):
        pass

    def text_to_pango(self):
        """
        Replaces all ampersands in `full_text` and `short_text` attributes of
        `self.output` with `&amp;`.

        It is called internally when pango markup is used.

        Can be called multiple times (`&amp;` won't change to `&amp;amp;`).
        """
        pass


class IntervalModule(Module):
    settings = (
        ("interval", "interval in seconds between module updates"),
    )
    interval = 5  # seconds
    managers = {}

    def registered(self, status_handler):
        pass

    def __call__(self):
        self.run()

    def run(self):
        """Called approximately every self.interval seconds

        Do not rely on this being called from the same thread at all times.
        If you need to always have the same thread context, subclass AsyncModule."""
