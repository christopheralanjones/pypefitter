"""
Contains the visitor classes for the pypefitter language recognizer.
"""

from pypefitter.dsl.parser.PypefitterParser import PypefitterParser
from pypefitter.dsl.parser.PypefitterVisitor import PypefitterVisitor


class PypefitterVisitor(PypefitterVisitor):
    """
    Controls the visit on the root-level pypefitter grammar.
    """

    def visitPypefitter(self, ctx: PypefitterParser.PypefitterContext) -> None:
        return super().visitPypefitter(ctx)

