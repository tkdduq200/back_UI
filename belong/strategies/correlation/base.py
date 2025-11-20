from abc import ABC, abstractmethod
from typing import Dict, Any

class BaseCorrelationStrategy(ABC):

    @abstractmethod
    def calculate(self, filters: Dict[str, Any]):
        pass
