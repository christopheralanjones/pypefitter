import pypefitter
import pytest
from typing import List


@pytest.mark.parametrize(
    'cli_params, expected', [
        ([],                        200),
        (['-v'],                    200),
        (['-f'],                    400),
        (['--file'],                400),
        (['-f', 'test'],            200),
        (['--file', 'test'],        200),
    ]
)
def test_parse_cli_arguments(pf_provider: str, pf_command: str, cli_params: List[str], expected: bool):
    all_cli_params: List[str] = cli_params.copy()
    all_cli_params.append(pf_provider)
    all_cli_params.append(pf_command)
    response = pypefitter.parse_cli_arguments(all_cli_params)
    assert response.return_code == expected

