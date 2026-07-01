from typing import Any, Dict, List
import structlog
from agent.plugins.base import BasePlugin
from agent.plugins.registry import plugin_registry

logger = structlog.get_logger()

class PluginManager:
    """
    Manager to load, initialize, and execute plugins.
    """
    def __init__(self) -> None:
        self._active_plugins: Dict[str, BasePlugin] = {}

    async def load_plugins(self) -> None:
        """
        Instantiates registered plugins and initializes them.
        """
        for name, plugin_cls in plugin_registry.get_all().items():
            try:
                instance = plugin_cls()
                await instance.initialize()
                self._active_plugins[name] = instance
                logger.info("Plugin loaded and initialized", plugin_name=name)
            except Exception as e:
                logger.error("Failed to load plugin", plugin_name=name, error=str(e))

    def get_active_plugins(self) -> List[BasePlugin]:
        return list(self._active_plugins.values())

    async def execute_all(self, target_subnet: str) -> Dict[str, Any]:
        """
        Runs all active plugins against the target and aggregates outcomes.
        """
        scan_results: Dict[str, Any] = {}
        for name, plugin in self._active_plugins.items():
            try:
                logger.info("Executing plugin scan", plugin_name=name, target=target_subnet)
                res = await plugin.scan(target_subnet)
                scan_results[name] = res
            except Exception as e:
                logger.error("Plugin scan execution failed", plugin_name=name, error=str(e))
                scan_results[name] = {"error": str(e)}
        return scan_results
