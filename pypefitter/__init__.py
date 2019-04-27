"""
Contains the core elements of Pypefitter. Additional plugins are provided via
the 'providers' directory.
"""
import argparse
import logging
from pypefitter.api import PypefitterError, PypefitterRequest, PypefitterResponse
from pypefitter.api.manager import EntryPointManager
from pypefitter.api.provider import Emitter
from pypefitter.api.provider import Provider
from typing import List

# do the basic logging configuration
logging.basicConfig(format='%(asctime)-15s  %(message)s')
logger = logging.getLogger('pypefitter')
logger.setLevel(logging.INFO)


# this is a constant
pf_default_file = 'pypefitter.pf'


def parse_cli_arguments(args_to_parse: List[str] = None) -> PypefitterResponse:
    """
    Define and parse all of the command-line arguments provided.

    Parameters
    ----------
    args_to_parse : List[str]
        The list of arguments to be parsed against the various argument
        parsing rules.

    Returns
    -------
    argparse.Namespace
        An `argparser.Namespace`_ that contains all of the parsed arguments.
    """
    try:
        # these are going to apply to everything
        parser = argparse.ArgumentParser(prog='pypefitter',
                                         description='Run pypefitter to create a concrete pipeline.')
        parser.add_argument('-v', '--verbose', dest='verbosity', action='count', default=0,
                            help='The verbosity level of the logging')
        parser.add_argument('-f', '--file', dest='file', action='store',
                            default=f"{pf_default_file}",
                            help='The file containing the pypefitter definition.')

        # these will be delegated to the providers to construct
        provider_parsers = parser.add_subparsers()
        for provider_name in EntryPointManager.get_plugin_names(Provider.get_entry_point()):
            provider_parser = provider_parsers.add_parser(provider_name)
            provider_parser.set_defaults(provider=provider_name)
            EntryPointManager.get_plugin(Provider.get_entry_point(), provider_name).decorate_cli(provider_parser)

        # set some defaults
        parser.set_defaults(provider='jenkins', command='generate', emitter='jenkinsfile')

        # now try to parse the arguments
        parsed_args = parser.parse_args(args_to_parse) \
            if args_to_parse is not None else parser.parse_args()

        # assuming we can, we then package everything up
        request: PypefitterRequest = \
            PypefitterRequest(parsed_args.command, parsed_args.provider, parsed_args.file,
                              **{'emitter': parsed_args.emitter, 'verbosity': parsed_args.verbosity})
        response = PypefitterResponse(200, 'OK', **{'request': request})
    except SystemExit:
        response = PypefitterResponse(400, 'Bad Request')

    # the payload of the response will be the request that will actually be
    # used to perform work
    return response


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
    EntryPointManager.load_entry_point(Provider.get_entry_point())
    EntryPointManager.load_entry_point(Emitter.get_entry_point())

    # parse the command-line arguments
    response: PypefitterResponse = parse_cli_arguments(argv)
    if response.return_code != 200:
        return 1
    request: PypefitterRequest = response.request
    logger.info('-' * 80)
    logger.info(f"Provider.......{request.provider}")
    logger.info(f"Emitter........{request.emitter}")
    logger.info(f"Command........{request.command}")
    logger.info(f"Definition.....{request.file}")
    logger.info('-' * 80)
    set_logging_level(request)

    # invoke the specific provider method
    try:
        provider: Provider = EntryPointManager.get_plugin(Provider.get_entry_point(), request.provider)
        response: PypefitterResponse = getattr(provider, request.command)(request)
    except PypefitterError:
        return 1
    finally:
        logger.info('-' * 80)
    return 0 if response.return_code == 200 else response.return_code
