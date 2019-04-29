"""
Contains the various default builders
"""
from abc import ABC, abstractmethod
from typing import List


class PypefitterRequestBuilder(ABC):
    """
    The builder is used to construct Pypefitter requests from other sources.

    The most common use of this pattern is build Pypefitter requests from
    the CLI.
    """
    @classmethod
    @abstractmethod
    def assemble(cls, **kwargs) -> None:
        """
        Assemble the materials needed to perform the build. This allows the
        build to perform pre-processing or preparation before being asked to
        produce the finished request.
        """
        pass


class PypefitterPluginCLIRequestBuilder(PypefitterRequestBuilder):
    """
    Build a request from the CLI using the argparse package.
    """
    pass


class PypefitterProviderCLIRequestBuilder(PypefitterPluginCLIRequestBuilder):
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
        provider = kwargs['provider']
        provider_parser = kwargs['parser']

        # get the commands for the provider -- begin with the commands common
        # to all providers
        actions: List = provider.get_actions()
        action_names = list(map(lambda action: action.get_plugin_id(), actions))

        # now setup some commands and whatever sub-arguments they require
        action_parser = provider_parser.add_subparsers(title='action')
        for action in actions:
            action.get_cli_builder().assemble(**{'action': action, 'parser': action_parser, 'provider': provider})

        # get the list of emitters for the provider and set the final defaults
        # on the arguments
        emitters: List = provider.get_emitters()
        provider_parser.set_defaults(provider=provider.get_plugin_id(), action=action_names[0], emitter=emitters[0].get_plugin_id())
