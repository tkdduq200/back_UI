# belong/strategies/correlation/senior_single_ratio.py

from typing import Dict, Any
from belong.strategies.correlation.base import BaseCorrelationStrategy
from belong.repositories.correlation_repository import CorrelationRepository

repo = CorrelationRepository()

class SeniorSingleRatioCorrelationStrategy(BaseCorrelationStrategy):

    def calculate(self, filters: Dict[str, Any]):
        df = repo.load()

        gu = filters["gu"]

        df_filtered = df[df["구"] == gu]

        ratio_avg = float(df_filtered["1인가구_비율"].mean())
        senior_sum = float(df_filtered["65세 이상"].sum())

        result = {
            "title": "전체 1인가구 비율 vs 65세 이상 인구 (전체연도 통합)",
            "x_label": "항목",
            "y_label": "값",
            "y_values": {
                "ratio": ratio_avg,
                "senior": senior_sum,
            },
            "correlation_value": 0,  # 마찬가지로 두 점이라 0
            "meta": filters,
        }

        return result
