"""
Contains the visitor classes for the pypefitter language recognizer.
"""
from antlr4.error.ErrorListener import ErrorListener
from antlr4.error.Errors import ParseCancellationException
import pypefitter
from pypefitter.api import PypefitterError
from pypefitter.dsl.symbols import SymbolType, SymbolTable
from pypefitter.dsl.parser.PypefitterParser import PypefitterParser
from pypefitter.dsl.parser.PypefitterVisitor import PypefitterVisitor
from typing import List


class PypefitterErrorListener(ErrorListener):
    """
    A custom error listener so that we can terminate the parse on bad
    input.
    """
    def __init__(self):
        super(PypefitterErrorListener, self).__init__()

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        message: str = f"{str(line)}:{str(column)}: syntax ERROR, {str(msg)}"
        raise PypefitterError(message) from ParseCancellationException(message)

    def reportAmbiguity(self, recognizer, dfa, startIndex, stopIndex, exact, ambigAlts, configs):
        message: str = f"Ambiguity ERROR, {str(configs)}"
        raise PypefitterError(message) from ParseCancellationException(message)

    def reportAttemptingFullContext(self, recognizer, dfa, startIndex, stopIndex, conflictingAlts, configs):
        message: str = f"Attempting full context ERROR, {str(configs)}"
        raise PypefitterError(message) from ParseCancellationException(message)

    def reportContextSensitivity(self, recognizer, dfa, startIndex, stopIndex, prediction, configs):
        message: str = f"Context ERROR, {str(configs)}"
        raise PypefitterError(message) from ParseCancellationException(message)


class AbstractPypefitterVisitor(PypefitterVisitor):
    """
    This is a base class for all PypefitterVisitors so that we can incorporate
    some standard extensions like a symbol table. These really don't belong in
    the visitor per se, but since these are extensions to the parser it will do
    for now.
    """

    global_symbol_table: SymbolTable = SymbolTable()
    """
    Holds the global symbol to which all of the elements should have access.
    """

    symbol_table_stack: List[SymbolTable] = []
    """
    Holds the stack of symbol tables that is used during parsing.
    """


class PypefitterVisitor(AbstractPypefitterVisitor):
    """
    Controls the visit on the root-level pypefitter grammar.
    """
    def visitPypefitter(self, ctx: PypefitterParser.PypefitterContext) -> None:
        pypefitter.logger.debug(f"Initializing symbol table")
        AbstractPypefitterVisitor.global_symbol_table = SymbolTable()
        pypefitter.logger.debug(f"Pypefitter visitor started")
        pypeline_name = ctx.stage_body().name.text

        # add the symbol to the global symbol table and then add the pypeline
        # symbol table to the stack so that the next set of elements can be
        # processed.
        pypeline_symbol: SymbolTable.Symbol = \
            AbstractPypefitterVisitor.global_symbol_table.add_symbol(pypeline_name, SymbolType.PYPELINE)
        AbstractPypefitterVisitor.symbol_table_stack.append(pypeline_symbol.symbol_table)

        # parse the children and pop the stack
        for stage in ctx.stage_body().stage():
            self.visitStage(stage.stage_body())
        AbstractPypefitterVisitor.symbol_table_stack.pop()
        pypefitter.logger.debug(f"Pypefitter visitor ended")

    def visitStage_body(self, ctx: PypefitterParser.Stage_bodyContext):
        pypefitter.logger.debug(f"Pypefitter visitor started")
        stage_name = ctx.name.text
        stage_symbol: SymbolTable.Symbol = \
            AbstractPypefitterVisitor.symbol_table_stack[-1].add_symbol(stage_name, SymbolType.STAGE)
        print(stage_symbol)
        AbstractPypefitterVisitor.symbol_table_stack.append(stage_symbol.symbol_table)
        AbstractPypefitterVisitor.symbol_table_stack.pop()
