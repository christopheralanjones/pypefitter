"""
Contains API-related elements related to emitters.
"""
from pypefitter.api import Emitter
from pypefitter.api.manager import ProviderManager


class BaseEmitter(Emitter):
    """
    Each emitter understands how to emit code. Each emitter works on behalf of
    a single Provider, which means that each provider can support more than one
    Emitter.
    """
    def __init__(self):
        """
        Constructs the Emitter. Each emitter is bound to the Provider that it
        supports.
        """
        self.provider = ProviderManager.get_provider(self.get_provider_id())
