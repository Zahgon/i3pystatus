class ConfigError(Exception):
    """ABC for configuration exceptions"""

    def __init__(self, module, *args, **kwargs):
        self.message = "Module '{0}': {1}".format(
            module, self.format(*args, **kwargs))

        super().__init__(self.message)

    def format(self, *args, **kwargs):
        pass


class ConfigKeyError(ConfigError, KeyError):
    def format(self, key):
        pass


class ConfigMissingError(ConfigError):
    def format(self, missing):
        pass


class ConfigAmbigiousClassesError(ConfigError):
    def format(self, ambigious_classes):
        pass


class ConfigInvalidModuleError(ConfigError):
    def format(self):
        pass
