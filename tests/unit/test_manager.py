from pypefitter.api.manager import EntryPointManager, PypefitterPluginNotFoundError
import pytest


#
# GENERAL MANAGER
#
def test_no_plugin_for_non_loaded_entry_points():
    with pytest.raises(PypefitterPluginNotFoundError):
        assert EntryPointManager.get_plugin('does.not.exist', 'does-not-exist') is None


def test_no_plugin_names_for_non_loaded_entry_points():
    assert EntryPointManager.get_plugin_names('does.not.exist') is None


def test_no_plugins_for_non_loaded_entry_points():
    assert EntryPointManager.get_plugins('does.not.exist') is None
