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


class Provider(ABC):
    """
    Defines the Provider API, which is used to declare concrete Provider
    implementations for platforms like Jenkins or AWS.
    """
    @classmethod
    @abstractmethod
    def get_provider_id(cls) -> str:
        """
        Returns the unique id of the provider.

        Returns
        -------
        str
            The unique id of the provider.
        """
        pass

    @classmethod
    def decorate_cli(cls, provider_parser):
        """
        Adds provider-specific options to the CLI.

        Parameters
        ----------
        provider_parser
            The argparse parser that will represent this provider
        """
        pass

    def generate(self, request: PypefitterRequest) -> PypefitterResponse:
        """
        Performs the actual code generation process.

        Parameters
        ----------
        request : PypefitterRequest
            The request to Pypefitter, which will contain the appropriate
            request data.

        Returns
        -------
        PypefitterResponse
            The response object that provides information about the request.
        """
        pass

    def init(self, request: PypefitterRequest) -> PypefitterResponse:
        """
        Used to produce a default pypefitter file to help teams bootstrap
        the process. This might be affected by the type of the Provider
        so we allow them the ability to override.

        Parameters
        ----------
        request : PypefitterRequest
            The request to Pypefitter, which will contain the appropriate
            request data.

        Returns
        -------
        PypefitterResponse
            The response object that provides information about the request.
        """
        pass

    def validate(self, request: PypefitterRequest) -> PypefitterResponse:
        """
        Performs a validation step to ensure that there is enough information
        provided that a subsequent code generation request will succeed.

        Parameters
        ----------
        request : PypefitterRequest
            The request to Pypefitter, which will contain the appropriate
            request data.

        Returns
        -------
        PypefitterResponse
            The response object that provides information about the request.
        """
        pass


class Emitter(ABC):
    """
    Each emitter understands how to emit code. Each emitter works on behalf of
    a single Provider, which means that each provider can support more than one
    Emitter.
    """
    @classmethod
    @abstractmethod
    def get_emitter_id(cls) -> str:
        """
        Returns the ID of the Emitter.

        Returns
        -------
        str
            The ID of the Emitter. This value will be unique across all
            emitters loaded by the emitter entry point.
        """
        pass

    @classmethod
    @abstractmethod
    def get_provider_id(cls) -> str:
        """
        Returns the ID of the Provider to which this Emitter is associated.

        Returns
        -------
        str
            The unique ID of the Provider for which this Emitter will emit.
        """
        pass

    @classmethod
    def emits_for_provider(cls, provider_name: str) -> bool:
        """
        Indicates whether or not this Emitter can emit on behalf of the
        specified Provider.

        Parameters
        ----------
        provider_name : str
            The name of the provider as defined in the pypefitter_providers
            entry point.

        Returns
        -------
        bool
            True if the Emitter will emit for the Provider with `provider_name`
            and False otherwise.
        """
        return provider_name.lower() == cls.get_provider_id()
