"""
Defines the classes that are used to implement providers for the various
platforms.
"""
from antlr4 import CommonTokenStream, InputStream
import errno
import os
from pathlib import Path
import pypefitter
from pypefitter.api import PypefitterError, PypefitterPlugin, PypefitterRequest, PypefitterResponse
from pypefitter.api.manager import EntryPointManager
from pypefitter.api.emitter import Emitter
from pypefitter.dsl.parser.PypefitterLexer import PypefitterLexer
from pypefitter.dsl.parser.PypefitterParser import PypefitterParser
from pypefitter.dsl.visitor import PypefitterErrorListener, PypefitterVisitor
from typing import List


class ProviderHelper:
    """
    This class provides some simple helper functions to keep the main Provider
    classes comparatively clean.
    """
    @classmethod
    def parse_pypefitter_definition(cls, pf_content: str):
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
            raise PypefitterError(f"Pypefitter file [{pf_file_path}] does not exist") \
                from FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), pf_file_path)

        pypefitter.logger.info(f"Reading Pypefitter file")
        with pf_file_path.open('r') as pf_file:
            pf_content = pf_file.read()
        return pf_content


class Provider(PypefitterPlugin):
    """
    Defines the Provider API, which is used to declare concrete Provider
    implementations for platforms like Jenkins or AWS.
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
        return 'pypefitter.providers'

    @classmethod
    def get_emitters(cls) -> List[Emitter]:
        """
        Gets the Emitters that have been registered for this Provider.

        Returns
        -------
        List[Emitter]
            The Emitters that have been registered via the provider's emitter
            entry point.
        """
        emitters: List[PypefitterPlugin] = \
            EntryPointManager.get_plugins(f"{cls.get_entry_point()}.{cls.get_plugin_id()}.emitters")
        return emitters

    @classmethod
    def get_providers(cls) -> List:
        """
        Gets the Emitters that have been registered for this Provider.

        Returns
        -------
        List[Provider]
            The Providers that have been registered with Pypefitter's provider
            entry point
        """
        providers: List[PypefitterPlugin] = \
            EntryPointManager.get_plugins(cls.get_entry_point())
        return providers

    @classmethod
    def get_provider(cls, plugin_id: str):
        """
        Gets the Emitters that have been registered for this Provider.

        Parameters
        ----------
        plugin_id : str
            The ID of the provider that we want.

        Returns
        -------
        Provider
            The Provider with the specified plugin_id.

        Raises
        ------
        PypefitterPluginNotFoundError
            If no provider with the specified ID exists.
        """
        return EntryPointManager.get_plugin(cls.get_entry_point(), plugin_id)

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


class BaseProvider(Provider):
    """
    The base class for all concrete Providers.
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
    def decorate_cli(cls, provider_parser) -> None:
        """
        Adds provider-specific options to the CLI.

        Parameters
        ----------
        provider_parser
            The argparse parser that will represent this provider
        """
        # get the list of emitters for the provider
        emitters: List[Emitter] = cls.get_emitters()
        emitter_names = list(map(lambda emitter: emitter.get_plugin_id(), emitters))

        # now setup some commands and whatever sub-arguments they require
        command_parser = provider_parser.add_subparsers(title='command')
        command_parser.add_parser('init').set_defaults(command='init')
        command_parser.add_parser('validate').set_defaults(command='validate')
        generate_parser = command_parser.add_parser('generate')
        generate_parser.set_defaults(command='generate', emitter=emitters[0].get_plugin_id())
        generate_parser.add_argument('emitter', choices=emitter_names, nargs='?', default=emitters[0].get_plugin_id(),
                                     help='The style of output to be produced')

        # assign some global defaults to make it easier to have a fast cli
        provider_parser.set_defaults(provider=cls.get_plugin_id(), command='generate', emitter=emitters[0].get_plugin_id())

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
        return self.validate(request)

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
        pypefitter.logger.info(f"Writing default pypefitter declaration")
        with open(f"{request.file}", 'w') as pf_file:
            pf_file.write('pypefitter pypeline { }')
            pf_file.close()
        pypefitter.logger.info(f"Default pypefitter declaration written")
        return PypefitterResponse()

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
        pf_file_path = Path(request.file)
        pf_content = ProviderHelper.read_pypefitter_file(pf_file_path)
        pypefitter.logger.info(f"Parse of pypefitter file started")
        ProviderHelper.parse_pypefitter_definition(pf_content)
        pypefitter.logger.info(f"Parse of Pypefitter file complete")
        return PypefitterResponse()
