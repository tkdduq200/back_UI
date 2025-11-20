from dataclasses import dataclass
from typing import List, Dict, Any

from belong.strategies.correlation.senior_housing import SeniorHousingCorrelationStrategy
from belong.strategies.correlation.senior_single_ratio import SeniorSingleRatioCorrelationStrategy


@dataclass
class CorrelationResult:
    title: str
    x_label: str
    y_label: str
    x_values: List[Any]
    y_values: Dict[str, Any]
    correlation_value: float
    meta: Dict


class CorrelationService:
    def __init__(self):
        self._strategies = {
            "housing": SeniorHousingCorrelationStrategy(),
            "ratio": SeniorSingleRatioCorrelationStrategy()
        }

    def get_overview_results(self, filters: Dict):
        return {
            "housing": self._strategies["housing"].calculate(filters),
            "ratio": self._strategies["ratio"].calculate(filters)
        }
