"""
Contains the core elements of Pypefitter. Additional plugins are provided via
the 'providers' directory.
"""
import argparse
import logging
from pypefitter.api import PypefitterError
from pypefitter.api.request import PypefitterRequest, PypefitterResponse
from pypefitter.api.builder import PypefitterRequestBuilder
from pypefitter.api.provider import Provider
from typing import List

# do the basic logging configuration
logging.basicConfig(format='%(asctime)-15s  %(message)s')
logger = logging.getLogger('pypefitter')
logger.setLevel(logging.INFO)

# this is a constant
pf_default_file = 'pypefitter.pf'


class PypefitterCLIRequestBuilder(PypefitterRequestBuilder):
    """
    Build a request from the CLI using the argparse package. This request
    builder is invoked by Pypefitter itself and acts as the coordinator
    across all CLI builders. Each plugin should implement the
    PypefitterPluginCLIBuilder instead.
    """
    @classmethod
    def assemble(cls, **kwargs) -> None:
        """
        Assemble the materials needed to perform the build. In this case this
        means that we call upon each provider to contribute it's own content
        to the CLI.
        """
        parser = kwargs['parser']
        parser.add_argument('-v', '--verbose', dest='verbosity', action='count', default=0,
                            help='The verbosity level of the logging')
        parser.add_argument('-f', '--file', dest='file', action='store',
                            default=f"{pf_default_file}",
                            help='The file containing the pypefitter definition.')

        # these will be delegated to the providers to construct
        provider_parsers = parser.add_subparsers()
        for provider in Provider.get_providers():
            provider_parser = provider_parsers.add_parser(provider.get_plugin_id())
            provider_parser.set_defaults(provider=provider.get_plugin_id())
            provider.get_cli_builder().assemble(**{'provider': provider, 'parser': provider_parser})

        # set some defaults
        parser.set_defaults(provider='jenkins', action='generate', emitter='jenkinsfile')

    @classmethod
    def build(cls, **kwargs) -> PypefitterRequest:
        """
        Build the PypefitterRequest from argparse.

        Returns
        -------
        PypefitterRequest
            The request that was prepared from argparse.
        """
        try:
            # allocate the parser and then assemble it
            parser = argparse.ArgumentParser(prog='pypefitter',
                                             description='Run pypefitter to create a concrete pipeline.')
            cls.assemble(parser=parser)

            # now that assembly is complete, attempt to parse
            parsed_args = parser.parse_args(kwargs['args']) \
                if 'args' in kwargs.keys() else parser.parse_args()

            # assuming we can, we then package everything up
            request: PypefitterRequest = \
                PypefitterRequest(parsed_args.action, parsed_args.provider, parsed_args.file,
                                  **{'emitter': parsed_args.emitter, 'verbosity': parsed_args.verbosity})
        except SystemExit:
            request: PypefitterRequest = None
        return request


def set_logging_level(request: PypefitterRequest) -> None:
    """
    Sets the logging level based on the arguments provided.

    Parameters
    ----------
    request : PypefitterRequest
        The request containing all of the arguments provided via the CLI.
    """
    # first things first -- set the logging level. we do this by
    # starting at 'error' and working down. we never allow it go
    # below 'debug' though since that would disable all logging
    # and that would be bad.
    log_level = (4 - request.verbosity) * 10 if request.verbosity < 4 else 10
    logger.setLevel(log_level)


def main(argv: List[str] = None) -> int:
    """
    The Pypefitter driver. This method will parse the arguments provided
    and then perform the specified command.

    Parameters
    ----------
    argv : List[str]
        Any command-line arguments to be provided.
    """
    # find all of the providers installed as plugins
    logger.info('-' * 80)

    # parse the command-line arguments
    builder: PypefitterCLIRequestBuilder = PypefitterCLIRequestBuilder()
    request: PypefitterRequest = builder.build(args=argv)
    if request is None:
        return 400
    logger.info('-' * 80)
    logger.info(f"Provider.......{request.provider}")
    logger.info(f"Emitter........{request.emitter}")
    logger.info(f"Action.........{request.action}")
    logger.info(f"Definition.....{request.file}")
    logger.info('-' * 80)
    set_logging_level(request)

    # invoke the specific provider method
    provider: Provider = Provider.get_provider(request.provider)
    response: PypefitterResponse = provider.do_action(request)
    logger.info('-' * 80)
    logger.error(f"[{response.return_code}] {response.reason}")
    return 0 if response.return_code == 200 else response.return_code
