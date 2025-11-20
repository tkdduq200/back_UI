from typing import Dict
import numpy as np

from belong.strategies.correlation.base import BaseCorrelationStrategy
from belong.services.correlation_service import CorrelationResult
from belong.repositories.correlation_repository import CorrelationRepository

repo = CorrelationRepository()


class SeniorSingleRatioCorrelationStrategy(BaseCorrelationStrategy):

    def calculate(self, filters: Dict):
        df = repo.load()

        gu = filters["gu"]

        df_filtered = df[df["구"] == gu]

        # 1인가구 비율 평균
        ratio_avg = df_filtered["1인가구_비율"].mean()

        # 65세 이상 인구 합계
        senior_sum = df_filtered["65세 이상"].sum()

        # 상관계수: 두 점만 있음 → 계산 불가 → 0 처리
        corr = 0

        y_dict = {
            "ratio": ratio_avg,
            "senior": senior_sum
        }

        return CorrelationResult(
            title="전체 1인가구 비율 vs 65세 이상 인구 (전체연도 통합)",
            x_label="항목",
            y_label="값",
            x_values=["1인가구_비율(평균)", "65세_이상_인구(합)"],
            y_values=y_dict,
            correlation_value=corr,
            meta=filters
        )
