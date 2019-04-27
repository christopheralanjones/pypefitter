"""
The API package contains the shareable elements of pypefitter that allow
the plugins to integrate with the main framework.
"""
from abc import ABC, abstractmethod


class PypefitterError(Exception):
    """
    A custom base exception for all Pypefitter-related problems.
    """
    def __init__(self, message):
        self.message = message


class PypefitterRequest(object):
    """
    A request provided to the Pypefitter API.
    """
    def __init__(self, command: str, provider: str, file: str, **kwargs):
        """
        Initializes the PypefitterRequest. The kwargs can contain arbitrary
        data, but it must be understood by the receiver of the request.

        Parameters
        ----------
        command : str
            The name of the command to be executed.
        provider :  str
            The name of the provider to be used.
        file : str
            The full path to the file to be used.
        """
        self.command = command
        self.file = file
        self.provider = provider
        self.__dict__.update(kwargs)


class PypefitterResponse(object):
    """
    A response provided by the Pypefitter API resulting from a
    PypefitterRequest.
    """
    def __init__(self, return_code: int = 200, reason: str = 'OK', **kwargs):
        """
        Initializes the PypefitterResponse

        Parameters
        ----------
        return_code : str
            The code representing the response. As much as possible we try to
            adhere to HTTP response codes, but this isn't mandatory.
        reason : str
            Any text that can help shed light on why the `return_code` is what
            it is.
        """
        self.return_code = return_code
        self.reason = reason
        self.__dict__.update(kwargs)


class PypefitterPlugin(ABC):
    """
    Defines a base class for all pluggable aspects of Pypefitter.
    """
    def __init__(self, entry_point):
        """
        Initializes the plugin.

        entry_point
            The entry point metadata that was used to instantiate this
            plugin. This allows the plugin to use its own metadata to mek
            decisions regarding its behavior.
        """
        self.entry_point = entry_point

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
