from agent.plugins.base import BasePlugin
from agent.plugins.registry import plugin_registry
from agent.plugins.manager import PluginManager

# Import concrete plugins so they register themselves upon package load
from agent.plugins.zeek import ZeekPlugin
from agent.plugins.scapy import ScapyPlugin
from agent.plugins.fingerbank import FingerbankPlugin
from agent.plugins.nvd import NvdPlugin
from agent.plugins.shodan import ShodanPlugin

__all__ = [
    "BasePlugin",
    "plugin_registry",
    "PluginManager",
    "ZeekPlugin",
    "ScapyPlugin",
    "FingerbankPlugin",
    "NvdPlugin",
    "ShodanPlugin",
]
