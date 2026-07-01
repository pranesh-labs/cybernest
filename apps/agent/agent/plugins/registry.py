from typing import Dict, Optional, Type
from agent.plugins.base import BasePlugin

class PluginRegistry:
    """
    Registry for cataloging scanner plugins.
    """
    def __init__(self) -> None:
        self._plugins: Dict[str, Type[BasePlugin]] = {}

    def register(self, plugin_cls: Type[BasePlugin]) -> Type[BasePlugin]:
        """
        Register a plugin class.
        """
        # Read the name property
        name = plugin_cls.__name__
        self._plugins[name.lower()] = plugin_cls
        return plugin_cls

    def get(self, name: str) -> Optional[Type[BasePlugin]]:
        return self._plugins.get(name.lower())

    def get_all(self) -> Dict[str, Type[BasePlugin]]:
        return self._plugins

plugin_registry = PluginRegistry()
