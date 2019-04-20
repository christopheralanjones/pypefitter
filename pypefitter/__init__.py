"""
Contains the core elements of Pypefitter. Additional plugins are provided via
the 'providers' directory.
"""
import argparse
import logging
from pypefitter.api import PypefitterError
from pypefitter.api.provider import EmitterManager, Provider, ProviderManager
from typing import List

# do the basic logging configuration
logging.basicConfig(format='%(asctime)-15s  %(message)s')
logger = logging.getLogger('pypefitter')
logger.setLevel(logging.INFO)


# this is a constant
pf_default_file = 'pypefitter.pf'


def parse_cli_arguments(args_to_parse: List[str] = None) -> argparse.Namespace:
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
    parsed_args = None

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
        for provider_name in ProviderManager.get_loaded_provider_names():
            provider_parser = provider_parsers.add_parser(provider_name)
            provider_parser.set_defaults(provider=provider_name)
            ProviderManager.get_provider(provider_name).decorate_cli(provider_parser)

        # set some defaults
        parser.set_defaults(provider='jenkins', command='generate', emitter='jenkinsfile')

        # now try to parse the arguments
        parsed_args = parser.parse_args(args_to_parse) \
            if args_to_parse is not None else parser.parse_args()
    except SystemExit:
        pass
    return parsed_args


def set_logging_level(args: argparse.Namespace) -> None:
    """
    Sets the logging level based on the arguments provided.

    Parameters
    ----------
    args : argsparse.Namespace
        The arguments provided to the Pypefitter CLI.
    """
    # first things first -- set the logging level. we do this by
    # starting at 'error' and working down. we never allow it go
    # below 'debug' though since that would disable all logging
    # and that would be bad.
    log_level = (4 - args.verbosity) * 10 if args.verbosity < 4 else 10
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
    ProviderManager.load_providers()

    # parse the command-line arguments
    args = parse_cli_arguments(argv)
    if not args:
        return 1
    logger.info('--------------------------------------------')
    logger.info(f"Provider.......{args.provider}")
    logger.info(f"Emitter........{args.emitter}")
    logger.info(f"Command........{args.command}")
    logger.info(f"Definition.....{args.file}")
    logger.info('--------------------------------------------')
    set_logging_level(args)

    # invoke the specific provider method
    try:
        provider: Provider = ProviderManager.get_provider(args.provider)
        getattr(provider, args.command)(args)
    except PypefitterError:
        return 1
    return 0
