from i3pystatus.core.util import KeyConstraintDict
from i3pystatus.core.exceptions import ConfigKeyError, ConfigMissingError
import inspect
import logging
import getpass


class SettingsBaseMeta(type):
    """Add interval setting to `settings` attribute if it does not exist."""

    def __init__(cls, name, bases, namespace):
        super().__init__(name, bases, namespace)

        cls.settings, cls.required = SettingsBaseMeta.get_merged_settings(cls)

    @staticmethod
    def get_merged_settings(cls):
        pass


class SettingsBase(metaclass=SettingsBaseMeta):
    """
    Support class for providing a nice and flexible settings interface

    Classes inherit from this class and define what settings they provide and
    which are required.

    The constructor is either passed a dictionary containing these settings, or
    keyword arguments specifying the same.

    Settings are stored as attributes of self.
    """

    __PROTECTED_SETTINGS = ["password", "email", "username"]

    settings = (
        ("log_level", "Set to true to log error to .i3pystatus-<pid> file."),
    )

    """settings should be tuple containing two types of elements:

    * bare strings, which must be valid Python identifiers.
    * two-tuples, the first element being a identifier (as above) and the second a docstring for the particular setting

    """

    required = tuple()
    """required can list settings which are required"""

    log_level = logging.WARNING
    logger = None

    def __init__(self, *args, **kwargs):
        def get_argument_dict(args, kwargs):
            pass

        self.__name__ = "{}.{}".format(self.__module__, self.__class__.__name__)

        settings = self.flatten_settings(self.settings)

        sm = KeyConstraintDict(settings, self.required)
        settings_source = get_argument_dict(args, kwargs)

        protected = self.get_protected_settings(settings_source)
        settings_source.update(protected)

        try:
            sm.update(settings_source)
        except KeyError as exc:
            raise ConfigKeyError(type(self).__name__, key=exc.args[0]) from exc

        try:
            self.__dict__.update(sm)
        except KeyConstraintDict.MissingKeys as exc:
            raise ConfigMissingError(
                type(self).__name__, missing=exc.keys) from exc

        if self.__name__.startswith("i3pystatus"):
            self.logger = logging.getLogger(self.__name__)
        else:
            self.logger = logging.getLogger("i3pystatus." + self.__name__)
        self.logger.setLevel(self.log_level)
        self.init()

    def get_protected_settings(self, settings_source):
        """
        Attempt to retrieve protected settings from keyring if they are not already set.
        """
        pass

    def get_setting_from_keyring(self, setting_identifier, keyring_backend=None):
        """
        Retrieves a protected setting from keyring
        :param setting_identifier: must be in the format package.module.Class.setting
        """
        pass

    def init(self):
        """Convenience method which is called after all settings are set

        In case you don't want to type that super()â€¦blabla :-)"""

    @staticmethod
    def flatten_settings(settings):
        pass
