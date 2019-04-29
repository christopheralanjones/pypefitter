from pathlib import Path
from pypefitter import PypefitterError
from pypefitter.api.plugin import PypefitterPluginNotFoundError, PluginManager
from pypefitter.api.parser import PypefitterParserHelper
from pypefitter.api.provider import Provider
import pytest


#
# PROVIDER HELPER
#

def test_provider_helper_reads_real_file(pf_real_file: Path, pf_definition: str):
    assert PypefitterParserHelper.read_pypefitter_file(pf_real_file) == pf_definition


def test_provider_helper_does_not_read_missing_file(pf_fake_file):
    with pytest.raises(PypefitterError):
        PypefitterParserHelper.read_pypefitter_file(pf_fake_file)


#
# PROVIDER
#
def test_manager_knows_discovered_providers(pf_provider: str):
    assert PluginManager.get_plugin(Provider.get_entry_point(), pf_provider) is not None


def test_manager_fails_on_unknown_provider():
    with pytest.raises(PypefitterPluginNotFoundError):
        assert PluginManager.get_plugin(Provider.get_entry_point(), 'does-not-exist')
