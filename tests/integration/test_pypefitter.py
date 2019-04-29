from pathlib import Path
import pypefitter
import pytest
from typing import List
from .conftest import pf_fixtures_dir


def test_pypefitter(pf_provider: str, pf_command: str, pf_test_dir: str) -> None:
    """
    Exercises the actual parsing of the pypefitter file provided by the
    fixture.
    :param pf_provider: The name of the provider to be used during the test.
    :param pf_command: The pypefitter command to be used during the test.
    :param pf_test_dir: The fixture that we're binding to.
    """
    # whether the test should succeed or not is built into the test name. if
    # we have an 'S' then the test should succeed. otherwise it should fail.
    success_or_failure_code = pf_test_dir[5:6]

    # we have the test directory, but we need to derive the file name
    pf_file: str = pf_fixtures_dir / pf_test_dir / 'pypefitter.pf'

    # invoke pypefitter and check the result.
    return_code = pypefitter.main(['-vvvv', '--file', f"{pf_file}", pf_provider, pf_command])
    if success_or_failure_code == 'S':
        assert return_code == 0
    else:
        assert return_code != 0


@pytest.mark.parametrize(
    'cli_params, expected', [
        ([],                        0),
        (['-v'],                    0),
        (['-f'],                    400),
        (['--file'],                400),
        (['-f', 'test'],            400),
        (['--file', 'test'],        400),
    ]
)
def test_pypefitter_with_bad_arguments(pf_real_file: Path, cli_params: List[str], expected: bool) -> None:
    actual = pypefitter.main(cli_params)
    assert expected == actual
