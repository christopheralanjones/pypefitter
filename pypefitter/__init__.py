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

# do the basic logging configuration
logging.basicConfig(format='%(asctime)-15s  %(message)s')
logger = logging.getLogger('pypefitter')

# this is a constant
pf_default_file = 'pypefitter.pf'


def parse_cli_arguments(args_to_parse: List[str] = None) -> argparse.Namespace:
    """
    Define and parse all of the command-line arguments provided.
    :return: An argparser.Namespace that contains all of the parsed arguments.
    """

    parsed_args = None

    try:
        parser = argparse.ArgumentParser(prog='pypefitter',
                                         description='Run pypefitter to create a concrete pipeline.')
        parser.add_argument('-v', '--verbose', dest='verbosity', action='count', default=0,
                            help='The verbosity level of the logging.')
        parser.add_argument('-f', '--file', dest='file', action='store',
                            default=f"{pf_default_file}",
                            help='The file containing the pypefitter definition.')
        parser.add_argument('-p', '--provider', dest='provider', action='store',
                            help='The name of the provider to be used to perform the pypefitter command.')
        command_parsers = parser.add_subparsers()
        command_parsers.add_parser('validate')
        command_parsers.add_parser('generate')

        parsed_args = parser.parse_args(args_to_parse) \
            if args_to_parse is not None else parser.parse_args()
    except SystemExit:
        pass
    return parsed_args


def parse_pypefitter_definition(args: argparse.Namespace, pf_content: str):
    """
    Parses a Pypefitter definition in the pf_content argument.
    :param args: The arguments provided to the Pypefitter CLI.
    :param pf_content: A Pypefitter definition that we want to parse.
    """
    logger.info(f"Parse of Pypefitter file [{args.file}] started")
    logger.debug(f"Attaching lexer to input stream")
    lexer = PypefitterLexer(InputStream(pf_content))
    logger.debug(f"Attaching token stream to lexer")
    stream = CommonTokenStream(lexer)
    logger.debug(f"Attaching parser to token stream")
    parser = PypefitterParser(stream)
    logger.debug(f"Attaching visitor to parser")
    visitor = PypefitterVisitor()
    logger.debug(f"Starting parse")
    visitor.visitPypefitter(parser.pypefitter())
    logger.info(f"Parse of Pypefitter file [{args.file}] complete")


def read_pypefitter_file(args: argparse.Namespace, pf_file_path: Path) -> str:
    """
    Reads the content of a Pypefitter file.
    :param args: The arguments provided to the Pypefitter CLI.
    :param pf_file_path: The path to the file containing a Pypefitter
    definition.
    :return: The content of 'pf_file_path'.
    """
    logger.info(f"Using Pypefitter file [{args.file}]")
    logger.info(f"Reading Pypefitter file [{args.file}]")
    with pf_file_path.open('r') as pf_file:
        pf_content = pf_file.read()
    return pf_content


def set_logging_level(args: argparse.Namespace) -> None:
    """
    Sets the logging level based on the arguments provided.
    :param args: The arguments provided to the Pypefitter CLI.
    """
    # first things first -- set the logging level. we do this by
    # starting at 'error' and working down. we never allow it go
    # below 'debug' though since that would disable all logging
    # and that would be bad.
    log_level = (4 - args.verbosity) * 10 if args.verbosity < 4 else 10
    logger.setLevel(log_level)


def main(argv: List[str] = None) -> int:
    """
    The Pypefitter driver.
    :param argv: Any command-line arguments to be provided.
    """

    # parse the command-line arguments
    args = parse_cli_arguments(argv)
    if args is None:
        return 1

    # set the logging level
    set_logging_level(args)

    # verify that the source file exists -- if not, there's not much
    # point in proceeding.
    pf_file_path = Path(args.file)
    if not pf_file_path.is_file():
        logger.error(f"Pypefitter file [{args.file}] does not exist")
        return 2

    # read and parse the pypefitter definition
    pf_content = read_pypefitter_file(args, pf_file_path)
    parse_pypefitter_definition(args, pf_content)
    return 0
