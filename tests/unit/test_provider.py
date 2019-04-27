from pathlib import Path
from pypefitter import PypefitterError
from pypefitter.api.emitter import Emitter
from pypefitter.api.provider import ProviderHelper
from pypefitter.api.manager import EmitterManager, ProviderManager, PypefitterProviderNotFoundError, PypefitterEmitterNotFoundError
import pytest


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
