import argparse
import logging
from typing import List
import sys

logging.basicConfig(format='%(asctime)-15s  %(message)s')
logger = logging.getLogger('pypefitter')


def parse_cli_arguments(args_to_parse: List[str] = None) -> argparse.Namespace:
    """
    Define and parse all of the command-line arguments provided.
    :return: An argparser.Namespace that contains all of the parsed arguments.
    """

    parsed_args = None

    try:
        parser = argparse.ArgumentParser(description='Run pypefitter to generate a concrete pipeline from the abstract form.')
        parser.add_argument('-s', '--src', dest='src', action='store',
                           default='pipeline.pf',
                           help='The source file containing the pipeline declaration. Defaults to \'pipeline.pf\'.')
        parser.add_argument('-p', '--provider', dest='provider', action='store',
                           default='jenkins', choices=['jenkins', 'aws'],
                           help='The name of the provider for which the pipeline should be generated. Defaults to \'jenkins\'.')
        parser.add_argument('-v', dest='verbosity', action='count',
                           default=2,
                           help='The verbosity level of the logging.')
        parser.add_argument('-c', '--config', dest='config', action='store',
                           help='The file containing provider-specific configuration. This is used during the transformation of the abstract pipeline into its concrete form for the specified provider.')
        parsed_args = parser.parse_args(args_to_parse) if args_to_parse is not None else parser.parse_args()
    except SystemExit:
        pass

    return parsed_args


if __name__ == "__main__":
    args = parse_cli_arguments()
    if args is not None:
        print(args.src)
        print(args.provider)
        print(args.verbosity)
        print(args.config)
