from pathlib import Path
from pypefitter import PypefitterError
from pypefitter.api.manager import PypefitterPluginNotFoundError, EntryPointManager
from pypefitter.api.emitter import Emitter
from pypefitter.api.provider import ProviderHelper, Provider
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
# GENERAL MANAGER
#
def test_manager_no_plugins_for_missing_entry_points():
    assert EntryPointManager.get_plugin('does-not-exist', 'does-not-exist') is None


#
# PROVIDER MANAGER
#

def test_manager_knows_discovered_providers(pf_provider: str):
    assert EntryPointManager.get_plugin(Provider.get_entry_point(), pf_provider) is not None


def test_manager_fails_on_unknown_provider():
    with pytest.raises(PypefitterPluginNotFoundError):
        assert EntryPointManager.get_plugin(Provider.get_entry_point(), 'does-not-exist')


#
# EMITTER MANAGER
#
def test_default_emitters_are_loaded(pf_emitter: str):
    assert EntryPointManager.get_plugin_names(Emitter.get_entry_point()) == ['cloudformation', 'jenkinsfile', 'terraform']


def test_manager_knows_discovered_emitters(pf_emitter: str):
    emitter: Emitter = EntryPointManager.get_plugin(Emitter.get_entry_point(), pf_emitter)
    assert emitter is not None
    assert emitter.get_plugin_id() == pf_emitter
    assert EntryPointManager.get_plugin(Emitter.get_entry_point(), emitter.get_plugin_id()) is emitter


def test_manager_fails_on_unknown_emitter():
    with pytest.raises(PypefitterPluginNotFoundError):
        assert EntryPointManager.get_plugin(Emitter.get_entry_point(), 'does-not-exist')
