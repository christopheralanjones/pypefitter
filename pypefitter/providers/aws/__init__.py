"""
Defines the AwsProvider provider.
"""
from pypefitter.api.provider import Provider


class AwsProvider(Provider):
    """
    Provides services related to the AWS platform.
    """
    @classmethod
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
        return 'aws'
