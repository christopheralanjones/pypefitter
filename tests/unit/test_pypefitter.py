import os
import pypefitter
import pytest
from typing import List



@pytest.fixture
def pf_file():
    with open(f"{pypefitter.pf_default_file}", 'w') as pf_file:
        pf_file.write('pypefitter { }')
        pf_file.close()
    yield pf_file
    os.remove(f"{pypefitter.pf_default_file}")


@pytest.mark.parametrize(
    'cli_params, expected', [
        ([],                        True),
        (['-v'],                    True),
        (['-f'],                    False),
        (['--file'],                False),
        (['-f', 'test'],            True),
        (['--file', 'test'],        True),
    ]
)
def test_parse_cli_arguments(cli_params: List[str], expected: bool):
    parsed_args = pypefitter.parse_cli_arguments(cli_params)
    if expected:
        assert parsed_args is not None
    else:
        assert parsed_args is None


@pytest.mark.parametrize(
    'cli_params, expected', [
        ([],                        0),
        (['-v'],                    0),
        (['-f'],                    1),
        (['--file'],                1),
        (['-f', 'test'],            2),
        (['--file', 'test'],        2),
    ]
)
def test_main(cli_params: List[str], expected: bool, pf_file):
    return_code = pypefitter.main(cli_params)
    assert return_code == expected
