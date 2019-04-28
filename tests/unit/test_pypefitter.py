from pypefitter import PypefitterCLIRequestBuilder
import pytest
from typing import List


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
def test_parse_cli_arguments(pf_provider: str, pf_command: str, cli_params: List[str], expected: bool):
    all_cli_params: List[str] = cli_params.copy()
    all_cli_params.append(pf_provider)
    all_cli_params.append(pf_command)
    request = PypefitterCLIRequestBuilder().build(**{'args': all_cli_params})
    if expected:
        assert request is not None
    else:
        assert request is None

