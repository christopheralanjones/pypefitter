import os
from pathlib import Path
import pypefitter
from pypefitter.api.provider import ProviderManager
import pytest


@pytest.fixture
def pf_definition():
    return 'pypefitter {}'


@pytest.fixture
def pf_real_file(pf_definition):
    with open(f"{pypefitter.pf_default_file}", 'w') as pf_file:
        pf_file.write(pf_definition)
        pf_file.close()
    yield Path(pf_file.name)
    os.remove(f"{pypefitter.pf_default_file}")


@pytest.fixture
def pf_fake_file():
    return Path(pypefitter.pf_default_file)


@pytest.fixture(scope="module", autouse=True)
def providers_fixture():
    ProviderManager.load_providers()


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
    params=['jenkinsfile', 'cloudformation', 'terraform']
)
def pf_emitter(request):
    return request.param
