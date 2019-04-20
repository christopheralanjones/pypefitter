import os
from pathlib import Path
import pypefitter
from pypefitter.api.provider import Emitter, EmitterManager, ProviderHelper, ProviderManager, \
    PypefitterProviderNotFoundError, PypefitterEmitterNotFoundError
import pytest


default_pf_text = 'pypefitter { }'


@pytest.fixture
def pf_real_file():
    with open(f"{pypefitter.pf_default_file}", 'w') as pf_file:
        pf_file.write(default_pf_text)
        pf_file.close()
    yield Path(pf_file.name)
    os.remove(f"{pypefitter.pf_default_file}")


@pytest.fixture
def pf_fake_file():
    return Path(pypefitter.pf_default_file)


#
# PROVIDER HELPER
#

def test_provider_helper_reads_real_file(pf_real_file):
    assert ProviderHelper.read_pypefitter_file(pf_real_file) == default_pf_text


def test_provider_helper_does_not_read_missing_file(pf_fake_file):
    with pytest.raises(FileNotFoundError):
        ProviderHelper.read_pypefitter_file(pf_fake_file)


#
# PROVIDER MANAGER
#

# This isn't really right, but we need to force a load of a bunch of
# providers. This should really be mocked -- in more ways than one.
ProviderManager.load_providers()


@pytest.fixture(
    params=ProviderManager.get_loaded_provider_names()
)
def pf_provider(request):
    return request.param


def test_manager_knows_discovered_providers(pf_provider: str):
    assert ProviderManager.get_provider(pf_provider) is not None


def test_manager_fails_on_unknown_provider():
    with pytest.raises(PypefitterProviderNotFoundError):
        assert ProviderManager.get_provider('does-not-exist')


#
# EMITTER MANAGER
#

# The emitters were loaded as part of the provider load.


@pytest.fixture(
    params=EmitterManager.get_loaded_emitter_names()
)
def pf_emitter(request):
    return request.param


def test_manager_knows_discovered_emitters(pf_emitter: str):
    emitter: Emitter = EmitterManager.get_emitter(pf_emitter)
    assert emitter is not None
    assert emitter.get_emitter_id() == pf_emitter
    assert EmitterManager.get_emitter(emitter.get_emitter_id()) is emitter


def test_manager_fails_on_unknown_emitter():
    with pytest.raises(PypefitterEmitterNotFoundError):
        assert EmitterManager.get_emitter('does-not-exist')


def test_emitter_provider_always_loaded(pf_emitter: str):
    provider_id: str = EmitterManager.get_emitter(pf_emitter).get_provider_id()
    assert ProviderManager.get_provider(provider_id)
