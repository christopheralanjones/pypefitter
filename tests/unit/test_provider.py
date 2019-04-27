from pathlib import Path
from pypefitter import PypefitterError
from pypefitter.api import PypefitterPlugin
from pypefitter.api.manager import PypefitterPluginNotFoundError, EntryPointManager
from pypefitter.api.emitter import Emitter
from pypefitter.api.provider import ProviderHelper, Provider
import pytest


class FakePluginType(PypefitterPlugin):
    """
    We need a fake plugin type that's only used for some testing.
    """
    @classmethod
    def get_entry_point(cls) -> str:
        """
        Each class of plugin corresponds to an entry point. the plugin class
        can define its own entry_point, but it has to have one.

        Returns
        -------
        str
            The name of the entry point associated with the plugin.
        """
        return 'pypefitter.does-not-exist'

    @classmethod
    def get_plugin_id(cls) -> str:
        """
        Each class of plugin needs to have its own to help uniquely identify it
        within its entry point.

        Returns
        -------
        str
            The ID of the plugin that uniquely identifies it within its entry
            point.
        """
        return 'does-not-exist'


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
def test_manager_no_plugins_for_non_pluggable_types():
    with pytest.raises(ValueError):
        assert EntryPointManager.get_plugin(str, 'does-not-exist')


def test_manager_no_plugins_for_non_loaded_type():
    assert EntryPointManager.get_plugin(FakePluginType, 'does-not-exist') is None


#
# PROVIDER MANAGER
#

def test_manager_knows_discovered_providers(pf_provider: str):
    assert EntryPointManager.get_plugin(Provider, pf_provider) is not None


def test_manager_fails_on_unknown_provider():
    with pytest.raises(PypefitterPluginNotFoundError):
        assert EntryPointManager.get_plugin(Provider, 'does-not-exist')


#
# EMITTER MANAGER
#
def test_default_emitters_are_loaded(pf_emitter: str):
    assert EntryPointManager.get_plugin_names(Emitter) == ['cloudformation', 'jenkinsfile', 'terraform']


def test_manager_knows_discovered_emitters(pf_emitter: str):
    emitter: Emitter = EntryPointManager.get_plugin(Emitter, pf_emitter)
    assert emitter is not None
    assert emitter.get_plugin_id() == pf_emitter
    assert EntryPointManager.get_plugin(Emitter, emitter.get_plugin_id()) is emitter


def test_manager_fails_on_unknown_emitter():
    with pytest.raises(PypefitterPluginNotFoundError):
        assert EntryPointManager.get_plugin(Emitter, 'does-not-exist')
