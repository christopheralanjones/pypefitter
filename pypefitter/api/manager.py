"""
Contains the various managers used within the API.
"""
import pkg_resources
import pypefitter
from pypefitter.api import Emitter, Provider, PypefitterError
from typing import List


class PypefitterProviderError(PypefitterError):
    """
    A custom base exception for all Provider-related problems.
    """
    def __init__(self, message):
        super().__init__(message)


class PypefitterProviderNotFoundError(PypefitterProviderError):
    """
    Represents an exception where a provider is requested but cannot
    be found in the list of previously discovered Providers.
    """
    def __init__(self, provider_name: str):
        self.provider_name = provider_name
        super().__init__(
            f"Provider [{provider_name}] is not in the list of discovered providers"
        )


class PypefitterEmitterError(PypefitterError):
    """
    A custom base exception for all Emitter-related problems.
    """
    def __init__(self, message):
        super().__init__(message)


class PypefitterEmitterNotFoundError(PypefitterEmitterError):
    """
    Represents an exception where an emitter is requested but cannot
    be found in the list of previously discovered Emitters.
    """
    def __init__(self, emitter_name: str):
        self.emitter_name = emitter_name
        super().__init__(
            f"Emitter [{emitter_name}] is not in the list of discovered emitters"
        )


class ProviderManager(object):
    """
    A helper class to manage the various Provider plugins.
    """
    providers = None

    @classmethod
    def load_providers(cls) -> None:
        """
        Finds and loads the various providers that are available to Pypefitter.
        """
        provider_entry_point: str = 'pypefitter_providers'

        pypefitter.logger.info(f"Loading providers from [{provider_entry_point}] entry point")
        cls.providers = {}
        for entry_point in pkg_resources.iter_entry_points(provider_entry_point):
            cls.providers[entry_point.name] = (entry_point.load())()
            pypefitter.logger.info(f"Loaded [{entry_point.name}] as [{cls.providers[entry_point.name].__class__.__name__}]")
        pypefitter.logger.info(f"Providers from [{provider_entry_point}] entry point loaded")

        # find all of the emitters installed as plugins and force them to load as well
        EmitterManager.load_emitters()

    @classmethod
    def get_provider(cls, provider_name: str) -> Provider:
        """
        Returns the Provider associated with the specified name. If multiple
        Providers have been loaded for the same name, then the first one loaded
        will be returned.

        Parameters
        ----------
        provider_name : str
            The name of the provider that we wish to return. The value of this
            parameter must match to the key used in the entry point used to
            define pypefitter providers.

        Returns
        -------
        Provider
            The Provider associated with the provider_name or None if there
            are no Providers associated with the provider_name.
        """
        # if we don't know what the provider is, that's a problem. if we do,
        # and if this is the first time we've been asked for it, then
        if provider_name not in cls.providers.keys():
            raise PypefitterProviderNotFoundError(provider_name)
        return cls.providers[provider_name]

    @classmethod
    def get_loaded_provider_names(cls) -> List[str]:
        """
        Returns a list of the names of the providers that have been loaded
        by Pypefitter.

        Returns
        -------
        List[str]
            The list of the names of the providers that have been loaded by
            Pypefitter.
        """
        return list(cls.providers.keys())


class EmitterManager(object):
    """
    A helper class to manage the various Emitter plugins.
    """
    emitters = None

    @classmethod
    def load_emitters(cls) -> None:
        """
        Finds and loads the various emitters that are available to Pypefitter.
        """
        emitter_entry_point: str = 'pypefitter_emitters'

        pypefitter.logger.info(f"Loading emitters from [{emitter_entry_point}] entry point")
        cls.emitters = {}
        for entry_point in pkg_resources.iter_entry_points(emitter_entry_point):
            cls.emitters[entry_point.name] = (entry_point.load())()
            pypefitter.logger.info(f"Loaded [{entry_point.name}] as [{cls.emitters[entry_point.name].__class__.__name__}]")
        pypefitter.logger.info(f"Emitters from [{emitter_entry_point}] entry point loaded")

    @classmethod
    def get_emitter(cls, emitter_name: str) -> Emitter:
        """
        Returns the Emitter associated with the specified name. If multiple
        Emitters have been loaded for the same name, then the first one loaded
        will be returned.

        Parameters
        ----------
        emitter_name : str
            The name of the Emitter that we wish to return. The value of this
            parameter must match to the key used in the entry point used to
            define pypefitter emitters.

        Returns
        -------
        Emitter
            The Emitter associated with the `emitter_name` or None if there
            are no Emitters associated with `emitter_name`.
        """
        if emitter_name not in cls.emitters.keys():
            raise PypefitterEmitterNotFoundError(emitter_name)
        return cls.emitters[emitter_name]

    @classmethod
    def get_loaded_emitter_names(cls) -> List[str]:
        """
        Returns a list of the names of the emitters that have been loaded
        by Pypefitter.

        Returns
        -------
        List[str]
            The list of the names of the providers that have been loaded by
            Pypefitter.
        """
        return list(cls.emitters.keys())

    @classmethod
    def get_loaded_emitters_names_for_provider(cls, provider_name: str) -> List[str]:
        """
        Returns a list of the names of the emitters that have been loaded
        by Pypefitter.

        Parameters
        ----------
        provider_name : str
            The name of the Provider for which we want the list of supported
            Emitter names.

        Returns
        -------
        List[str]
            The list of the names of the emitters that have been loaded by
            Pypefitter that can support the specified provider.
        """
        provider_emitters: List[str] = []
        for emitter_name, emitter_class in cls.emitters.items():
            if getattr(emitter_class, 'emits_for_provider')(provider_name):
                provider_emitters.append(emitter_name)
        return provider_emitters
