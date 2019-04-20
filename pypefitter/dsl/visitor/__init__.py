"""
Contains the visitor classes for the pypefitter language recognizer.
"""
from antlr4.error.ErrorListener import ErrorListener
from antlr4.error.Errors import ParseCancellationException
from pypefitter.api import PypefitterError
from pypefitter.dsl.parser.PypefitterParser import PypefitterParser
from pypefitter.dsl.parser.PypefitterVisitor import PypefitterVisitor


class PypefitterErrorListener(ErrorListener):
    """
    A custom error listener so that we can terminate the parse on bad
    input.
    """
    def __init__(self):
        super(PypefitterErrorListener, self).__init__()

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        message: str = f"{str(line)}:{str(column)}: syntax ERROR, {str(msg)}"
        raise PypefitterError() from ParseCancellationException(message)

    def reportAmbiguity(self, recognizer, dfa, startIndex, stopIndex, exact, ambigAlts, configs):
        message: str = f"Ambiguity ERROR, {str(configs)}"
        raise PypefitterError() from ParseCancellationException(message)

    def reportAttemptingFullContext(self, recognizer, dfa, startIndex, stopIndex, conflictingAlts, configs):
        message: str = f"Attempting full context ERROR, {str(configs)}"
        raise PypefitterError() from ParseCancellationException(message)

    def reportContextSensitivity(self, recognizer, dfa, startIndex, stopIndex, prediction, configs):
        message: str = f"Context ERROR, {str(configs)}"
        raise PypefitterError() from ParseCancellationException(message)


class PypefitterVisitor(PypefitterVisitor):
    """
    Controls the visit on the root-level pypefitter grammar.
    """
    def visitPypefitter(self, ctx: PypefitterParser.PypefitterContext) -> None:
        return super().visitPypefitter(ctx)

