# belong/strategies/ml_predictor.py

from typing import Dict, Any
import numpy as np
import pandas as pd
import joblib

from belong.ml.config import MODEL_PATH, FEATURE_PATH, TARGET_COL
from belong.ml.future_builder import build_feature_dataframe
from belong.ml.model_loader import load_model
from .predictor_strategy import PredictorStrategy


class MLPredictor(PredictorStrategy):
    """
    ML 모델 기반 예측 전략.
    """

    def __init__(self):
        self._df_features = build_feature_dataframe()

        # 모델 로드
        self._model = load_model()

        # feature_cols 로드 (학습 당시 스키마)
        self._feature_cols = joblib.load(FEATURE_PATH)

    def _prepare_row(self, gu: str, year: int) -> pd.DataFrame:
        row = self._df_features[
            (self._df_features["구"] == gu)
            & (self._df_features["연도"] == year)
        ]

        if row.empty:
            raise ValueError(f"존재하지 않는 (구,연도): {gu}, {year}")

        # 1) One-hot
        row = pd.get_dummies(row, drop_first=True)

        # 2) 학습 feature 순서로 강제 정렬
        row = row.reindex(columns=self._feature_cols, fill_value=0)

        return row

    def predict(self, gu: str, year: int) -> float:
        X = self._prepare_row(gu, year)
        pred = float(self._model.predict(X)[0])
        return pred

    def predict_with_detail(self, gu: str, year: int) -> Dict[str, Any]:
        X = self._prepare_row(gu, year)
        pred = float(self._model.predict(X)[0])

        # 실제값(y_true)이 있으면 추가
        row = self._df_features[
            (self._df_features["구"] == gu)
            & (self._df_features["연도"] == year)
        ]
        y_true = float(row[TARGET_COL].iloc[0]) if TARGET_COL in row.columns else None

        return {
            "구": gu,
            "연도": year,
            "y_pred": pred,
            "y_true": y_true,
        }
