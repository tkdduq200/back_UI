# belong/strategies/correlation/senior_housing.py

from typing import Dict, Any
from belong.strategies.correlation.base import BaseCorrelationStrategy
from belong.repositories.correlation_repository import CorrelationRepository

repo = CorrelationRepository()

class SeniorHousingCorrelationStrategy(BaseCorrelationStrategy):

    def calculate(self, filters: Dict[str, Any]):
        df = repo.load()

        gu = filters["gu"]

        # 해당 구만 전체 연도 통합
        df_filtered = df[df["구"] == gu]

        housing_sum = float(df_filtered["단독주택_계"].sum())
        senior_sum = float(df_filtered["65세 이상"].sum())

        # 템플릿에서 쓰기 쉽게 dict 형태로 반환
        result = {
            "title": "단독주택 1인가구 수 vs 65세 이상 인구 (전체연도 통합)",
            "x_label": "항목",
            "y_label": "값",
            # labels는 그래프에서 직접 문자열로 박을 거라 여기선 안 씀
            "y_values": {
                "housing": housing_sum,
                "senior": senior_sum,
            },
            "correlation_value": 0,  # 두 점이라 상관계수 의미 없으니 0 고정
            "meta": filters,
        }

        return result
