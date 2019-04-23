import os
from pathlib import Path
import pypefitter
import conftest
from pypefitter.api.provider import Emitter, EmitterManager, ProviderHelper, ProviderManager, \
    PypefitterProviderNotFoundError, PypefitterEmitterNotFoundError, PypefitterError
import pytest


# default_pf_text = 'pypefitter { }'


# @pytest.fixture
# def pf_real_file():
#     with open(f"{pypefitter.pf_default_file}", 'w') as pf_file:
#         pf_file.write(default_pf_text)
#         pf_file.close()
#     yield Path(pf_file.name)
#     os.remove(f"{pypefitter.pf_default_file}")


# @pytest.fixture
# def pf_fake_file():
#     return Path(pypefitter.pf_default_file)


#
# PROVIDER HELPER
#

def test_provider_helper_reads_real_file(pf_real_file: Path, pf_definition: str):
    assert ProviderHelper.read_pypefitter_file(pf_real_file) == pf_definition


def test_provider_helper_does_not_read_missing_file(pf_fake_file):
    with pytest.raises(PypefitterError):
        ProviderHelper.read_pypefitter_file(pf_fake_file)


#
# PROVIDER MANAGER
#

def test_manager_knows_discovered_providers(pf_provider: str):
    assert ProviderManager.get_provider(pf_provider) is not None


def test_manager_fails_on_unknown_provider():
    with pytest.raises(PypefitterProviderNotFoundError):
        assert ProviderManager.get_provider('does-not-exist')


#
# EMITTER MANAGER
#
def test_default_emitters_are_loaded(pf_emitter: str):
    assert EmitterManager.get_loaded_emitter_names() == ['cloudformation', 'jenkinsfile', 'terraform']


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
