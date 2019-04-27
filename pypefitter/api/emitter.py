"""
Contains API-related elements related to emitters.
"""
from pypefitter.api import PypefitterPlugin


class Emitter(PypefitterPlugin):
    """
    Each emitter understands how to emit code. Each emitter works on behalf of
    a single Provider, which means that each provider can support more than one
    Emitter.
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


class BaseEmitter(Emitter):
    """
    Each emitter understands how to emit code. Each emitter works on behalf of
    a single Provider, which means that each provider can support more than one
    Emitter.
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
