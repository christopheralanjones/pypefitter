import os
from pathlib import Path
import pypefitter
import pytest


# Pre-calcluate the directory that contains all of our sample files so that
# we don't need to do it so often later.
#fixtures_directory = Path(f"{os.path.dirname(os.path.realpath(__file__))}/fixtures").resolve().absolute()
fixtures_directory = Path(__file__).parent / "fixtures"


@pytest.fixture(
    params=['jenkins', 'aws']
)
def pf_provider(request) -> str:
    return request.param


@pytest.fixture(
    params=['validate', 'generate']
)
def pf_command(request) -> str:
    return request.param


@pytest.fixture(
    params=os.listdir(f"{fixtures_directory}")
)
def pf_test_dir(request) -> str:
    """
    This fixture iterates over the various sample pipefitter files and
    processes each one.
    :param request: Contains the current directory name being processed by
    the fixture.
    :return: The name of the test directory containing the pypefitter
    definition.
    """
    return request.param


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
    pf_file: str = fixtures_directory / pf_test_dir / 'pypefitter.pf'

    # invoke pypefitter and check the result.
    return_code = pypefitter.main(['-vvv', '--file', f"{pf_file}", pf_provider, pf_command])
    if success_or_failure_code == 'S':
        assert return_code == 0
    else:
        assert return_code != 0
