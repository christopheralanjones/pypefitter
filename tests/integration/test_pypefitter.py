import os
import pypefitter
import pytest


# Pre-calcluate the directory that contains all of our sample files so that
# we don't need to do it so often later.
fixtures_directory = f"{os.path.dirname(os.path.realpath(__file__))}/fixtures"


@pytest.fixture(
    params=os.listdir(f"{fixtures_directory}")
)
def pf_file(request) -> str:
    """
    This fixture iterates over the various sample pipefitter files and
    processes each one.
    :param request: Contains the current directory name being processed by
    the fixture.
    :return: The complete path to the pypefitter script so that we can pass
    it in on the command-line arguments.
    """
    return f"{fixtures_directory}/{request.param}/pypefitter.py"


def test_pypefitter(pf_file: str) -> None:
    """
    Exercises the actual parsing of the pypefitter file provided by the
    fixture.
    :param pf_file: The fixture that we're binding to.
    """
    # whether the test should succeed or not is built into the test name. if
    # we have an 'S' then the test should succeed. otherwise it should fail.
    success_or_failure_code = pf_file[5:6]

    # invoke pypefitter and check the result.
    return_code = pypefitter.main(['--file', pf_file])
    if success_or_failure_code == 'S':
        assert return_code == 0
    else:
        assert return_code != 0