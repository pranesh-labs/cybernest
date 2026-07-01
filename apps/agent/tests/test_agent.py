from agent.fingerprinting.config.settings import agent_settings
from agent.plugins import plugin_registry

def test_config_loading() -> None:
    """
    Ensures that default configuration loads successfully.
    """
    assert agent_settings.AGENT_ID is not None
    assert agent_settings.API_URL is not None

def test_plugin_registration() -> None:
    """
    Verifies that scanner plugins register themselves into the global registry.
    """
    all_plugins = plugin_registry.get_all()
    assert "zeek" in all_plugins
    assert "scapy" in all_plugins
    assert "fingerbank" in all_plugins
    assert "nvd" in all_plugins
    assert "shodan" in all_plugins
