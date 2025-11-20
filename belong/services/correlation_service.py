# belong/services/correlation_service.py

from typing import Dict, Any

from belong.strategies.correlation.senior_housing import SeniorHousingCorrelationStrategy
from belong.strategies.correlation.senior_single_ratio import SeniorSingleRatioCorrelationStrategy


class CorrelationService:
    def __init__(self):
        self._strategies = {
            "housing": SeniorHousingCorrelationStrategy(),
            "ratio": SeniorSingleRatioCorrelationStrategy(),
        }

    def get_overview_results(self, filters: Dict[str, Any]):
        housing_result = self._strategies["housing"].calculate(filters)
        ratio_result = self._strategies["ratio"].calculate(filters)

        return {
            "housing": housing_result,
            "ratio": ratio_result,
        }
