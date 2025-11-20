from typing import Dict
import numpy as np

from belong.strategies.correlation.base import BaseCorrelationStrategy
from belong.services.correlation_service import CorrelationResult
from belong.repositories.correlation_repository import CorrelationRepository

repo = CorrelationRepository()


class SeniorHousingCorrelationStrategy(BaseCorrelationStrategy):

    def calculate(self, filters: Dict):
        df = repo.load()

        gu = filters["gu"]

        # 해당 '구'만 전체 연도 통합
        df_filtered = df[df["구"] == gu]

        # 단독주택 1인가구 수 (전체 연도 합)
        housing_sum = df_filtered["단독주택_계"].sum()

        # 65세 이상 인구 전체 합
        senior_sum = df_filtered["65세 이상"].sum()

        # 상관분석용 배열
        x_values = [housing_sum]
        y_values = [senior_sum]

        # 상관계수는 두 점만 있으면 불가 → 예외처리
        corr = 0

        y_dict = {
            "housing": housing_sum,
            "senior": senior_sum
        }

        return CorrelationResult(
            title="단독주택 1인가구 수 vs 65세 이상 인구 (전체연도 통합)",
            x_label="항목",
            y_label="값",
            x_values=["단독주택_1인가구수", "65세_이상_인구"],
            y_values=y_dict,
            correlation_value=corr,
            meta=filters
        )
