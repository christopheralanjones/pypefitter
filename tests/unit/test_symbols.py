from pypefitter.dsl.symbols import SymbolType, SymbolTable, DuplicateSymbolError
import pytest


@pytest.mark.parametrize(
    'name, symbol_type, table, expected', [
        ('legal', SymbolType.PYPELINE, SymbolTable(), True),
        (None,    SymbolType.PYPELINE, SymbolTable(), False),
        ('legal', None,                SymbolTable(), False),
        ('legal', SymbolType.PYPELINE, None,          False),
        (None,    None,                SymbolTable(), False),
        ('legal', None,                None,          False),
        (None,    SymbolType.PYPELINE, None,          False),
        (None,    None,                None,          False),
    ]
)
def test_duplicate_symbol_error(name: str, symbol_type: SymbolType, table: SymbolTable, expected: bool):
    if expected:
        assert DuplicateSymbolError(name, symbol_type, table)
    else:
        with pytest.raises(ValueError):
            assert DuplicateSymbolError(name, symbol_type, table)


@pytest.mark.parametrize(
    'name, symbol_type, expected', [
        ('legal', SymbolType.PYPELINE, True),
        (None,    SymbolType.PYPELINE, False),
        ('legal', None,                False),
        (None,    None,                False),
    ]
)
def test_symbol_builders(name: str, symbol_type: SymbolType, expected: bool):
    if expected:
        symbol = SymbolTable.Symbol(name, symbol_type)
        assert symbol is not None
        assert symbol.name == name
        assert symbol.symbol_type == symbol_type
        assert symbol.symbol_table is None
    else:
        with pytest.raises(ValueError):
            assert SymbolTable.Symbol(name, symbol_type)


@pytest.mark.parametrize(
    'name, symbol_type, found', [
        ('dupe',   SymbolType.PYPELINE, True),
        ('nodupe', SymbolType.PYPELINE, False),
    ]
)
def test_symbol_table_finder(name: str, symbol_type: SymbolType, found: bool):
    # add an entry to a table
    table: SymbolTable = SymbolTable()
    table.add_symbol('dupe', SymbolType.PYPELINE)

    # now look for the row
    if found:
        assert table.find_symbol(name, symbol_type) is not None
        with pytest.raises(DuplicateSymbolError):
            table.add_symbol(name, symbol_type)
    else:
        assert table.find_symbol(name, symbol_type) is None
        try:
            table.add_symbol(name, symbol_type)
        except DuplicateSymbolError:
            pytest.fail('Unique name-type pairs can be added to a symbol table')
