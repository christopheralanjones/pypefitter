import argparse
import logging
from typing import List

logging.basicConfig(format='%(asctime)-15s  %(message)s')
logger = logging.getLogger('pypefitter')


def parse_cli_arguments(args_to_parse: List[str] = None) -> argparse.Namespace:
    """
    Define and parse all of the command-line arguments provided.
    :return: An argparser.Namespace that contains all of the parsed arguments.
    """

    parsed_args = None

    try:
        parser = argparse.ArgumentParser(
            description='Run pypefitter to create a concrete pipeline.')
        parser.add_argument('-s', '--src', dest='src', action='store',
                            default='pipeline.pf',
                            help='The file containing the pypefitter definition.')
        parser.add_argument('-p', '--provider', dest='provider', action='store',
                            default='jenkins', choices=['jenkins', 'aws'],
                            help='The provider to be used to create the pipeline.')
        parser.add_argument('-v', dest='verbosity', action='count',
                            default=2,
                            help='The verbosity level of the logging.')
        parser.add_argument('-c', '--config', dest='config', action='store',
                            help='The provider-specific configuration file.')
        parsed_args = parser.parse_args(args_to_parse) \
            if args_to_parse is not None else parser.parse_args()
    except SystemExit:
        pass

    return parsed_args


if __name__ == "__main__":
    args = parse_cli_arguments()
    if args is not None:
        print(args)
