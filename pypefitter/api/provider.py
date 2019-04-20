"""
Defines the classes that are used to implement providers for the various
platforms.
"""
from abc import ABC, abstractmethod
from antlr4 import CommonTokenStream, InputStream
import argparse
import errno
import os
from pathlib import Path
import pkg_resources
import pypefitter
from pypefitter.api import PypefitterError
from pypefitter.dsl.parser.PypefitterLexer import PypefitterLexer
from pypefitter.dsl.parser.PypefitterParser import PypefitterParser
from pypefitter.dsl.visitor import PypefitterErrorListener, PypefitterVisitor
from typing import List


class PypefitterProviderError(PypefitterError):
    """
    A custom base exception for all Provider-related problems.
    """
    pass


class PypefitterProviderNotFoundError(PypefitterProviderError):
    """
    Represents an exception where a provider is requested but cannot
    be found in the list of previously discovered Providers.
    """
    def __init__(self, provider_name: str):
        self.provider_name = provider_name
        self.message = f"Provider [{provider_name}] is not in the list of discovered providers"


class PypefitterEmitterError(PypefitterError):
    """
    A custom base exception for all Emitter-related problems.
    """
    pass


class PypefitterEmitterNotFoundError(PypefitterEmitterError):
    """
    Represents an exception where an emitter is requested but cannot
    be found in the list of previously discovered Emitters.
    """
    def __init__(self, emitter_name: str):
        self.emitter_name = emitter_name
        self.message = f"Emitter [{emitter_name}] is not in the list of discovered emitters"


class ProviderHelper:
    """
    This class provides some simple helper functions to keep the main Provider
    classes comparatively clean.
    """
    @classmethod
    def parse_pypefitter_definition(cls, pf_content: str) -> None:
        """
        Parses a Pypefitter definition in the pf_content argument.

        Parameters
        ----------
        pf_content : str
            A Pypefitter definition that we want to parse.
        """
        pypefitter.logger.debug(f"Attaching lexer to input stream")
        lexer = PypefitterLexer(InputStream(pf_content))
        pypefitter.logger.debug(f"Attaching token stream to lexer")
        stream = CommonTokenStream(lexer)
        pypefitter.logger.debug(f"Attaching parser to token stream")
        parser = PypefitterParser(stream)
        parser._listeners = [PypefitterErrorListener()]
        pypefitter.logger.debug(f"Attaching visitor to parser")
        visitor = PypefitterVisitor()
        pypefitter.logger.debug(f"Starting parse")
        visitor.visitPypefitter(parser.pypefitter())

    @classmethod
    def read_pypefitter_file(cls, pf_file_path: Path) -> str:
        """
        Reads the content of a Pypefitter file.

        Parameters
        ----------
        pf_file_path : Path
            The path to the file containing a Pypefitter definition.

        Returns
        -------
        str
            The content of 'pf_file_path'.
        """
        pypefitter.logger.info(f"Using Pypefitter file [{pf_file_path}]")
        if not pf_file_path.is_file():
            pypefitter.logger.error(f"Pypefitter file [{pf_file_path}] does not exist")
            raise PypefitterError from FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), pf_file_path)

        pypefitter.logger.info(f"Reading Pypefitter file")
        with pf_file_path.open('r') as pf_file:
            pf_content = pf_file.read()
        return pf_content


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
    def decorate_cli(cls, provider_parser) -> None:
        """
        Adds provider-specific options to the CLI.

        Parameters
        ----------
        provider_parser
            An argsparse parser that the `Provider`_ can decorate with its
            own options.
        """
        # get the list of emitters for the provider
        emitters: List[str] = \
            EmitterManager.get_loaded_emitters_names_for_provider(cls.get_provider_id())

        # now setup some commands and whatever subarguments they require
        command_parser = provider_parser.add_subparsers(title='command')
        command_parser.add_parser('init').set_defaults(command='init')
        command_parser.add_parser('validate').set_defaults(command='validate')
        generate_parser = command_parser.add_parser('generate')
        generate_parser.set_defaults(command='generate', emitter=emitters[0])
        generate_parser.add_argument('emitter', choices=emitters, nargs='?', default=emitters[0],
                                     help='The style of output to be produced')

        # assign some global defaults to make it easier to have a fast cli
        provider_parser.set_defaults(provider=cls.get_provider_id(), command='generate', emitter=emitters[0])

    def generate(self, args: argparse.Namespace) -> None:
        """
        Performs the actual code generation process.
        :return:
        """
        self.validate(args)

    def init(self, args: argparse.Namespace) -> None:
        """
        Used to produce a default pypefitter file to help teams bootstrap
        the process. This might be affected by the type of the Provider
        so we allow them the ability to override.
        :return:
        """
        pass

    def validate(self, args: argparse.Namespace) -> None:
        """
        Performs a validation step to ensure that there is enough information
        provided that a subsequent code generation request will succeed.
        :return:
        """
        pf_file_path = Path(args.file)
        pf_content = ProviderHelper.read_pypefitter_file(pf_file_path)
        pypefitter.logger.info(f"Parse of pypefitter file started")
        ProviderHelper.parse_pypefitter_definition(pf_content)
        pypefitter.logger.info(f"Parse of Pypefitter file complete")


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
        :param provider_name: The name of the provider that we wish to return.
        The value of this parameter must match to the key used in the entry
        point used to define pypefitter providers.
        :return: The Provider associated with the provider_name or None if
        there are no Providers associated with the provider_name.
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
        :return: The list of the names of the providers that have been loaded
        by Pypefitter.
        """
        return list(cls.providers.keys())


class Emitter(ABC):
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

    @classmethod
    @abstractmethod
    def get_emitter_id(cls) -> str:
        pass

    @classmethod
    @abstractmethod
    def get_provider_id(cls) -> str:
        pass

    @classmethod
    def emits_for_provider(cls, provider_name: str) -> bool:
        """
        Indicates whether or not this Emitter can emit on behalf of the
        specified Provider.
        :param provider_name: The name of the provider as defined in the
        pypefitter_providers entry point.
        :return: True if the provider is for 'jenkins' and false otherwise.
        """
        return provider_name.lower() == cls.get_provider_id()


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

        pypefitter.logger.error(f"Loading emitters from [{emitter_entry_point}] entry point")
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
        :param emitter_name: The name of the Emitter that we wish to return.
        The value of this parameter must match to the key used in the entry
        point used to define pypefitter emitters.
        :return: The Emitter associated with the emitter_name or None if
        there are no Emitters associated with the emitter_name.
        """
        if emitter_name not in cls.emitters.keys():
            raise PypefitterEmitterNotFoundError(emitter_name)
        return cls.emitters[emitter_name]

    @classmethod
    def get_loaded_emitter_names(cls) -> List[str]:
        """
        Returns a list of the names of the emitters that have been loaded
        by Pypefitter.
        :return: The list of the names of the providers that have been loaded
        by Pypefitter.
        """
        return list(cls.emitters.keys())

    @classmethod
    def get_loaded_emitters_names_for_provider(cls, provider_name: str) -> List[str]:
        """
        Returns a list of the names of the emitters that have been loaded
        by Pypefitter.
        :param provider_name: The name of the Provider for which we want the
        list of supported Emitter names.
        :return: The list of the names of the emitters that have been loaded
        by Pypefitter that can support the specified provider.
        """
        provider_emitters: List[str] = []
        for emitter_name, emitter_class in cls.emitters.items():
            if getattr(emitter_class, 'emits_for_provider')(provider_name):
                provider_emitters.append(emitter_name)
        return provider_emitters
