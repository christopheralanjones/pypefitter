"""
Contains the various managers used within the API.
"""
import pkg_resources
import pypefitter
from pypefitter.api import PypefitterError, PypefitterPlugin
from typing import List


# class PypefitterProviderError(PypefitterError):
#     """
#     A custom base exception for all Provider-related problems.
#     """
#     def __init__(self, message):
#         super().__init__(message)
#
#
# class PypefitterProviderNotFoundError(PypefitterProviderError):
#     """
#     Represents an exception where a provider is requested but cannot
#     be found in the list of previously discovered Providers.
#     """
#     def __init__(self, provider_name: str):
#         self.provider_name = provider_name
#         super().__init__(
#             f"Provider [{provider_name}] is not in the list of discovered providers"
#         )
#
#
# class PypefitterEmitterError(PypefitterError):
#     """
#     A custom base exception for all Emitter-related problems.
#     """
#     def __init__(self, message):
#         super().__init__(message)
#
#
# class PypefitterEmitterNotFoundError(PypefitterEmitterError):
#     """
#     Represents an exception where an emitter is requested but cannot
#     be found in the list of previously discovered Emitters.
#     """
#     def __init__(self, emitter_name: str):
#         self.emitter_name = emitter_name
#         super().__init__(
#             f"Emitter [{emitter_name}] is not in the list of discovered emitters"
#         )

class PypefitterPluginError(PypefitterError):
    """
    A custom base exception for all Provider-related problems.
    """
    def __init__(self, message):
        super().__init__(message)


class PypefitterPluginNotFoundError(PypefitterPluginError):
    """
    Represents an exception where a plugin is requested from an entry point
    but cannot be found in the list of previously discovered plugins.
    """
    def __init__(self, entry_point: str, plugin_id: str):
        """
        Initializes the error.

        Parameters
        ----------
        entry_point : str
            The name of the entry point that was being used.
        plugin_id : str
            The ID of the plugin that was being requested.
        """
        self.entry_point = entry_point
        self.plugin_id = plugin_id
        super().__init__(
            f"Plugin [{plugin_id}] was not found in entry point [{entry_point}]"
        )


class EntryPointManager(object):
    """
    A helper class to manage the various Pypefitter plugins.
    """

    __plugin_cache = {}
    """
    A dictionary of entry points and the plugins that have been loaded for
    each of them. There will be an entry for each entry point registered
    using the register_entry_point method. Each such entry will then have
    another map of plugin IDs to actual plugin instances.
    """

    @classmethod
    def load_plugins(cls, entry_point: str) -> None:
        """
        Finds and loads the plugins for the specified entry_point.

        If the entry point has already been loaded, it will be re-loaded,
        which could result in other side-effects.

        Parameters
        ----------
        entry_point : str
            The name of the entry point for which we want to load the plugins.
        """
        pypefitter.logger.debug(f"Preparing plugin cache for entry point [{entry_point}]")
        pypefitter.logger.info(f"Loading plugins for [{entry_point}] entry point")
        for plugin in pkg_resources.iter_entry_points(entry_point):
            if entry_point not in cls.__plugin_cache:
                cls.__plugin_cache[entry_point] = {}
            cls.__plugin_cache[entry_point][plugin.name] = (plugin.load())(None)
            pypefitter.logger.info(f"Loaded [{plugin.name}] as [{cls.__plugin_cache[entry_point][plugin.name].__class__.__name__}]")
        pypefitter.logger.info(f"Plugins from [{entry_point}] entry point loaded")

    @classmethod
    def get_plugin(cls, entry_point: str, plugin_id: str) -> object:
        """
        Returns the plugin from the specified entry_point with the specified
        plugin id.

        Parameters
        ----------
        entry_point : str
            The name of the entry point for which we want the plugin.
        plugin_id : str
            The ID of the plugin that we wish to return. The value of this
            parameter must match to the key used in the entry point.

        Returns
        -------
        object
            The plugin associated with the plugin_id within the specified
            entry point or None if there are no such plugins.

        Raises
        ------
        PypefitterPluginNotFoundError
            If no plugin with the specified ID exists within the specified
            entry point.
        """
        if entry_point not in cls.__plugin_cache.keys():
            cls.load_plugins(entry_point)
        if entry_point not in cls.__plugin_cache.keys():
            return None
        if plugin_id not in cls.__plugin_cache[entry_point].keys():
            raise PypefitterPluginNotFoundError(entry_point, plugin_id)
        return cls.__plugin_cache[entry_point][plugin_id]

    @classmethod
    def get_plugins(cls, entry_point: str) -> List[PypefitterPlugin]:
        """
        Returns a list of the names of the plugins that have been loaded
        for the specified entry point.

        Parameters
        ----------
        entry_point : str
            The name of the entry point for which we want to load the plugins.

        Returns
        -------
        List[PypefitterPlugin]
            The list of the plugins that have been loaded for the specified
            entry point or None if the entry point does not exist.
        """
        if entry_point not in cls.__plugin_cache.keys():
            cls.load_plugins(entry_point)
        return list(cls.__plugin_cache[entry_point].values()) if entry_point in cls.__plugin_cache.keys() else None

    @classmethod
    def get_plugin_names(cls, entry_point: str) -> List[str]:
        """
        Returns a list of the names of the plugins that have been loaded
        for the specified plugin type.

        Parameters
        ----------
        entry_point : str
            The name of the entry point for which we want to load the plugins.

        Returns
        -------
        List[str]
            The list of the names of the plugins that have been loaded for
            the specified plugin type or None if no such plugins exist.
        """
        if entry_point not in cls.__plugin_cache.keys():
            cls.load_plugins(entry_point)
        return list(cls.__plugin_cache[entry_point].keys()) if entry_point in cls.__plugin_cache.keys() else None
