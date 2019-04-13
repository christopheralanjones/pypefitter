import pytest
import sys
from pypefitter import pypefitter
from typing import List


@pytest.mark.parametrize(
    'cli_params, expected', [
        (['-v'],                    True),
        (['-c'],                    False),
        (['-c', 'test'],            True),
        (['--config'],              False),
        (['--config', 'test'],      True),
        (['-s'],                    False),
        (['--src'],                 False),
        (['-s', 'test'],            True),
        (['--src', 'test'],         True),
        (['-p'],                    False),
        (['--provider'],            False),
        (['-p', 'jenkins'],         True),
        (['--provider', 'jenkins'], True),
        (['--provider', 'jenkins'], True),
        (['-p', 'aws'],             True),
        (['--provider', 'aws'],     True),
    ]
)
def test_parse_cli_arguments(cli_params: List[str], expected: bool):
    parsed_args = pypefitter.parse_cli_arguments(cli_params)
    if expected:
        assert parsed_args is not None
    else:
        assert parsed_args is None
