"""
Defines the Pypefitter command model.
"""
from abc import abstractmethod
from pathlib import Path
import pypefitter
from pypefitter.api import PypefitterPlugin
from pypefitter.api.builder import PypefitterPluginCLIRequestBuilder
from pypefitter.api.emitter import Emitter
from pypefitter.api.parser import PypefitterParserHelper
from pypefitter.api.provider import Provider
from pypefitter.api.request import PypefitterRequest, PypefitterResponse
from typing import List


class PypefitterActionCLIRequestBuilder(PypefitterPluginCLIRequestBuilder):
    """
    The builder is used to construct Pypefitter requests from other sources.

    The most common use of this pattern is build Pypefitter requests from
    the CLI.
    """
    @classmethod
    def assemble(cls, **kwargs) -> None:
        """
        Assemble the materials needed to perform the build. This allows the
        build to perform pre-processing or preparation before being asked to
        produce the finished request.
        """
        # get the arguments
        action: Action = kwargs['action']
        action_parser = kwargs['parser']
        action_parser.add_parser(action.get_plugin_id()).set_defaults(action=action.get_plugin_id())


class Action(PypefitterPlugin):
    """
    Represents an action that can be performed within Pypefitter. These
    actions are intended to encapsulate the logic that performs those
    actions and makes it possible to extend the capabilities of the various
    providers.
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
        return PypefitterActionCLIRequestBuilder()

    @abstractmethod
    def do_action(self, provider: Provider, request: PypefitterRequest) -> PypefitterResponse:
        """
        Performs the action.

        Parameters
        ----------
        provider : Provider
            The Provider on whose behalf the action is being taken.
        request : PypefitterRequest
            The request that encapsulates all of the information acquired
            when pypefitter was invoked.

        Returns
        -------
        PypefitterResponse
            The result of the request being performed.
        """
        pass


class CommonAction(Action):
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
        return 'pyperfitter.providers.actions'


class InitAction(CommonAction):
    """
    Performs an initialization to help bootstrap a new developer
    """
    @classmethod
    def get_plugin_id(cls) -> str:
        """
        Each action needs to have its own to help uniquely identify it
        within its entry point.

        Returns
        -------
        str
            The ID of the action that uniquely identifies it within its entry
            point.
        """
        return 'init'

    def do_action(self, provider: Provider, request: PypefitterRequest) -> PypefitterResponse:
        """
        Performs the action.

        Parameters
        ----------
        provider : Provider
            The Provider on whose behalf the action is being taken.
        request : PypefitterRequest
            The request that encapsulates all of the information acquired
            when pypefitter was invoked.

        Returns
        -------
        PypefitterResponse
            The result of the request being performed.
        """
        pypefitter.logger.info(f"Writing default pypefitter declaration")
        with open(f"{request.file}", 'w') as pf_file:
            pf_file.write('pypefitter pypeline { }')
            pf_file.close()
        pypefitter.logger.info(f"Default pypefitter declaration written")
        return PypefitterResponse()


class PypefitterGenerateActionCLIRequestBuilder(PypefitterActionCLIRequestBuilder):
    """
    The builder is used to construct Pypefitter requests from other sources.

    The most common use of this pattern is build Pypefitter requests from
    the CLI.
    """
    @classmethod
    def assemble(cls, **kwargs) -> None:
        """
        Assemble the materials needed to perform the build. This allows the
        build to perform pre-processing or preparation before being asked to
        produce the finished request.
        """
        provider: Provider = kwargs['provider']
        action: Action = kwargs['action']
        action_parser = kwargs['parser']

        # get the list of emitters for the provider
        emitters: List[Emitter] = provider.get_emitters()
        emitter_names = list(map(lambda emitter: emitter.get_plugin_id(), emitters))

        # finish defining the arguments
        generate_parser = action_parser.add_parser(action.get_plugin_id())
        generate_parser.set_defaults(action=action.get_plugin_id(), emitter=emitters[0].get_plugin_id())
        generate_parser.add_argument('emitter', choices=emitter_names, nargs='?', default=emitters[0].get_plugin_id(),
                                     help='The style of output to be produced')


class GenerateAction(CommonAction):
    """
    Performs an initialization to help bootstrap a new developer
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
        return PypefitterGenerateActionCLIRequestBuilder()

    @classmethod
    def get_plugin_id(cls) -> str:
        """
        Each action needs to have its own to help uniquely identify it
        within its entry point.

        Returns
        -------
        str
            The ID of the action that uniquely identifies it within its entry
            point.
        """
        return 'generate'

    def do_action(self, provider: Provider, request: PypefitterRequest) -> PypefitterResponse:
        """
        Performs the action.

        Parameters
        ----------
        provider : Provider
            The Provider on whose behalf the action is being taken.
        request : PypefitterRequest
            The request that encapsulates all of the information acquired
            when pypefitter was invoked.

        Returns
        -------
        PypefitterResponse
            The result of the request being performed.
        """
        return ValidateAction().do_action(provider, request)


class ValidateAction(CommonAction):
    """
    Performs an initialization to help bootstrap a new developer
    """
    @classmethod
    def get_plugin_id(cls) -> str:
        """
        Each action needs to have its own to help uniquely identify it
        within its entry point.

        Returns
        -------
        str
            The ID of the action that uniquely identifies it within its entry
            point.
        """
        return 'validate'

    def do_action(self, provider: Provider, request: PypefitterRequest) -> PypefitterResponse:
        """
        Performs the action.

        Parameters
        ----------
        provider : Provider
            The Provider on whose behalf the action is being taken.
        request : PypefitterRequest
            The request that encapsulates all of the information acquired
            when pypefitter was invoked.

        Returns
        -------
        PypefitterResponse
            The result of the request being performed.
        """
        pf_file_path = Path(request.file)
        pf_content = PypefitterParserHelper.read_pypefitter_file(pf_file_path)
        pypefitter.logger.info(f"Parse of pypefitter file started")
        PypefitterParserHelper.parse_pypefitter_definition(pf_content)
        pypefitter.logger.info(f"Parse of Pypefitter file complete")
        return PypefitterResponse()
