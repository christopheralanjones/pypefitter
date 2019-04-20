import os
from pathlib import Path
import pytest


pf_fixtures_dir: Path = Path(__file__).parent / "fixtures"


@pytest.fixture(
    params=os.listdir(f"{pf_fixtures_dir}")
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
