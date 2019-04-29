"""
This module contains the symbol table constructs and logic that underpin
the Pypefitter parser and code generator.
"""
from enum import Enum, unique
import pypefitter
from pypefitter.api import PypefitterError
from typing import List


@unique
class SymbolType(Enum):
    PYPELINE = 1,
    STAGE = 2
    EVENT = 3


class DuplicateSymbolError(PypefitterError):
    """
    Reflects a problem where two Symbols with the same attributes have been
    added to the same SymbolTable.
    """
    def __init__(self, name: str, symbol_type: SymbolType, symbol_table):
        """
        Initializes the DuplicateSymbolError.

        Parameters
        ----------
        name : str
            The name of the new Symbol. This value is required.
        symbol_type : SymbolType
            The type of the symbol.
        symbol_table : SymbolTable
            The SymbolTable where the conflict arose.

        Raises
        ------
        ValueError
            If either the symbol or the symbol_table is not provided.
        """
        if name is None:
            raise ValueError('Parameter ''name'' is required')
        if symbol_type is None:
            raise ValueError('Parameter ''symbol_type'' is required')
        if symbol_table is None:
            raise ValueError('Parameter ''symbol_table'' is required')
        self.name = name
        self.symbol_type = symbol_type
        self.symbol_table = symbol_table
        self.message = f"Symbol [{name}] of type [{symbol_type}] already exists in the symbol table"


class SymbolTable(object):
    """
    A SymbolTable holds a collection of symbols. There is one root SymbolTable
    that contains references to Symbols.

    Each SymbolTable can refer to other symbol tables, typically its parent.
    This allows us to track the scope of symbols and determine the overriding
    of symbols based on those scopes.
    """
    class Symbol(object):
        """
        A symbol is an entry in the symbol table. Each symbol has its own
        SymbolTable, which is used to manage the symbols within its scope.
        """
        def __init__(self, name: str, symbol_type: SymbolType, **kwargs):
            """
            Initializes the Symbol.

            Parameters
            ----------
            name : str
                The name of the new Symbol. This value is required.
            symbol_type : SymbolType
                The type of the Symbol. This value is required.

            Raises
            ------
            ValueError
                If either the 'name' or 'symbol_type' parameters are not provided.
            """
            if name is None:
                raise ValueError('Parameter ''name'' is required')
            if symbol_type is None:
                raise ValueError('Parameter ''symbol_type'' is required')
            self.name = name
            self.symbol_type = symbol_type
            self.symbol_table = SymbolTable()
            self.attributes = kwargs

    def __init__(self, parent=None):
        self.parent = parent
        self.symbols: List[SymbolTable.Symbol] = []

    def add_symbol(self, name: str, symbol_type: SymbolType, **kwargs) -> Symbol:
        """
        Adds the specified Symbol to the SymbolTable.

        Parameters
        ----------
        name : str
            The name of the new Symbol. This value is required.
        symbol_type : SymbolType
            The type of the Symbol. This value is required.

        Returns
        -------
        Symbol
            The symbol that was added to the symbol table.

        Raises
        ------
        DuplicateSymbolError
            If an attempt is made to add the same symbol to the SymbolTable.
        ValueError
            If the name or entry parameters are not provided.
        """
        if self.find_symbol(name, symbol_type):
            raise DuplicateSymbolError(name, symbol_type, self)
        new_symbol: SymbolTable.Symbol = SymbolTable.Symbol(name, symbol_type, **kwargs)
        self.symbols.append(new_symbol)
        return new_symbol

    def find_symbol(self, name: str, symbol_type: SymbolType) -> Symbol:
        """
        Attempts to locate a Symbol in the SymbolTable.

        Parameters
        name : str
            The name of the Symbol we're looking for.
        symbol_type : SymbolType
            The type of Symbol we're looking for. This matters because we
            could have different types in the table with the same name.
            That's technically legal.

        Returns
        -------
        Symbol
            The Symbol in the table with the specific `name` and `type` or
            `None` if no such Symbol exists.
        """
        matching_symbols: List[SymbolTable.Symbol] = \
            list(filter(lambda symbol: symbol.name == name and symbol.symbol_type == symbol_type, self.symbols))
        return matching_symbols[0] if len(matching_symbols) != 0 else None

    def print(self, indent: int = 0) -> None: # pragma: no cover
        """
        Prints the symbol table in human-readable format.
        """
        for symbol in self.symbols:
            leading_spaces: str = '' if indent == 0 else ' ' * 2 * indent
            pypefitter.logger.debug(f"{leading_spaces}{symbol.name} [{symbol.symbol_type}] {symbol.attributes}")
            symbol.symbol_table.print(indent+1)
