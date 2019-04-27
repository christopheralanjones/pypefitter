"""
Contains the base-class Emitters.
"""
from pypefitter.api.emitter import BaseEmitter


class JenkinsEmitter(BaseEmitter):
    """
    A base class for all Jenkins-related emitters.
    """
    def __init__(self, entry_point):
        """
        Initializes the plugin.

        entry_point
            The entry point metadata that was used to instantiate this
            plugin. This allows the plugin to use its own metadata to mek
            decisions regarding its behavior.
        """
        super().__init__(entry_point)

    @classmethod
    def is_compatible_with(cls, plugin_id: str) -> bool:
        """
        Determines if this plugin is compatible with the specified plkugin ID.

        Parameters
        ----------
        plugin_id : str
            The ID of the plugin for which we're testing compatibility.

        Returns
        -------
        bool
            True if this plugin is compatible with the one identified by the
            plugin_id and False otherwise. By default we assume compatibility.
        """
        return plugin_id == 'jenkins'


class AwsEmitter(BaseEmitter):
    """
    A base class for all AWS-related emitters.
    """
    @classmethod
    def is_compatible_with(cls, plugin_id: str) -> bool:
        """
        Determines if this plugin is compatible with the specified plkugin ID.

        Parameters
        ----------
        plugin_id : str
            The ID of the plugin for which we're testing compatibility.

        Returns
        -------
        bool
            True if this plugin is compatible with the one identified by the
            plugin_id and False otherwise. By default we assume compatibility.
        """
        return plugin_id == 'aws'
