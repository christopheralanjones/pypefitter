"""
This module contains some misfit classes that assist with general actions
like reading and parsing pypefitter definitions.
"""
from antlr4 import CommonTokenStream, InputStream
import errno
import os
from pathlib import Path
import pypefitter
from pypefitter import PypefitterError
from pypefitter.dsl.parser.PypefitterLexer import PypefitterLexer
from pypefitter.dsl.parser.PypefitterParser import PypefitterParser
from pypefitter.dsl.visitor import PypefitterErrorListener, PypefitterVisitor


class PypefitterParserHelper:
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
