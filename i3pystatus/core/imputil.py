import inspect
import types
from importlib import import_module
from i3pystatus.core.exceptions import ConfigAmbigiousClassesError, ConfigInvalidModuleError


class ClassFinder:
    """Support class to find classes of specific bases in a module"""

    def __init__(self, baseclass):
        self.baseclass = baseclass

    def predicate_factory(self, module):
        pass

    def get_matching_classes(self, module):
        # Transpose [ (name, list), ... ] to ( [name, ...], [list, ...] )
        pass

    def get_class(self, module):
        pass

    def get_module(self, module):
        pass

    def instanciate_class_from_module(self, module, *args, **kwargs):
        pass
