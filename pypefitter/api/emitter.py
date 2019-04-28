"""
Contains API-related elements related to emitters.
"""
from pypefitter.api import PypefitterPlugin
from pypefitter.api.builder import PypefitterPluginCLIRequestBuilder


class PypefitterEmitterCLIRequestBuilder(PypefitterPluginCLIRequestBuilder):
    """
    The builder is used to construct Pypefitter requests from other sources.

    The most common use of this pattern is build Pypefitter requests from
    the CLI.
    """
    @classmethod
    def assemble(cls, **kwargs) -> None:
        pass


class Emitter(PypefitterPlugin):
    """
    The abstract base class for all emitters. New Emitters should extend the
    BaseEmitter class instead.
    """
    @classmethod
    def get_cli_builder(cls) -> PypefitterPluginCLIRequestBuilder:
        """
        The request builder that will be used to augment the CLI.

        Returns
        -------
        PypefitterRequestBuilder
            The request builder for the plugin.
        """
        return None

    @classmethod
    def get_entry_point(cls) -> str:
        """
        Each class of plugin corresponds to an entry point. the plugin class
        can define its own entry_point, but it has to have one.

        Returns
        -------
        str
            The name of the entry point associated with the plugin.
        """
        return 'pypefitter.emitters'
