from abc import ABC, abstractmethod
from typing import Any, Dict

class BasePlugin(ABC):
    """
    Abstract Base Class for all Agent integration plugins (Zeek, Scapy, Shodan, etc.).
    """
    @property
    @abstractmethod
    def name(self) -> str:
        """
        Unique name of the plugin.
        """
        pass

    @property
    @abstractmethod
    def version(self) -> str:
        """
        Plugin version.
        """
        pass

    @abstractmethod
    async def initialize(self) -> None:
        """
        Initialize plugin (validate dependencies, open connections, etc.).
        """
        pass

    @abstractmethod
    async def scan(self, target_subnet: str) -> Dict[str, Any]:
        """
        Execute scan operation on the target subnet/host.
        """
        pass
