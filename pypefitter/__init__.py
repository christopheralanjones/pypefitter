"""
Contains the core elements of Pypefitter. Additional plugins are provided via
the 'providers' directory.
"""

from antlr4 import CommonTokenStream, InputStream
import argparse
import logging
from pathlib import Path
from pypefitter.dsl.parser.PypefitterLexer import PypefitterLexer
from pypefitter.dsl.parser.PypefitterParser import PypefitterParser
from pypefitter.dsl.visitor import PypefitterVisitor
from typing import List
logging.basicConfig(format='%(asctime)-15s  %(message)s')
logger = logging.getLogger('pypefitter')


pf_default_file = 'pypefitter.pf'


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
                            default=f"{pf_default_file}",
                            help='The file containing the pypefitter definition.')
        parser.add_argument('-p', '--provider', dest='provider', action='store',
                            default='jenkins', choices=['jenkins', 'aws'],
                            help='The provider to be used to create the pipeline.')
        parser.add_argument('-v', dest='verbosity', action='count',
                            default=2,
                            help='The verbosity level of the logging.')
        parser.add_argument('-c', '--config', dest='config', action='store',
                            help='The provider-specific configuration file.')
        if args_to_parse is None:
            args_to_parse = []
        parsed_args = parser.parse_args(args_to_parse)
    except SystemExit:
        pass
    return parsed_args


def main(argv: List[str] = None) -> int:
    """
    The Pypefitter driver.
    :param argv: Any command-line arguments to be provided.
    """

    # parse the command-line arguments
    args = parse_cli_arguments(argv)
    if args is None:
        return 1

    # verify that the source file exists -- if not, there's not much
    # point in proceeding.
    pf_decl_path = Path(args.src)
    if not pf_decl_path.is_file():
        logger.error(f"Pypefitter file [{args.src}] does not exist")
        return 2

    logger.info(f"Using Pypefitter file [{args.src}]")
    lexer = PypefitterLexer(InputStream(args.src))
    stream = CommonTokenStream(lexer)
    parser = PypefitterParser(stream)
    visitor = PypefitterVisitor()
    visitor.visitPypefitter(parser.pypefitter())
    return 0
