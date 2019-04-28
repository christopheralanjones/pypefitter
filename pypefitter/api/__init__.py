"""
The API package contains the shareable elements of pypefitter that allow
the plugins to integrate with the main framework.
"""
from abc import ABC, abstractmethod
from pypefitter.api.builder import PypefitterPluginCLIRequestBuilder


class PypefitterError(Exception):
    """
    A custom base exception for all Pypefitter-related problems.
    """
    def __init__(self, message):
        self.message = message


class PypefitterPlugin(ABC):
    """
    Defines a base class for all pluggable aspects of Pypefitter.
    """
    @classmethod
    @abstractmethod
    def get_cli_builder(cls) -> PypefitterPluginCLIRequestBuilder:
        """
        The request builder that will be used to augment the CLI.

        Returns
        -------
        PypefitterRequestBuilder
            The request builder for the plugin.
        """
        pass

    @classmethod
    @abstractmethod
    def get_entry_point(cls) -> str:
        """
        Each class of plugin corresponds to an entry point. the plugin class
        can define its own entry_point, but it has to have one.

        Returns
        -------
        str
            The name of the entry point associated with the plugin.
        """
        pass

    @classmethod
    @abstractmethod
    def get_plugin_id(cls) -> str:
        """
        Each class of plugin needs to have its own to help uniquely identify it
        within its entry point.

        Returns
        -------
        str
            The ID of the plugin that uniquely identifies it within its entry
            point.
        """
        pass
