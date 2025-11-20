"""
belong.ml.config

ML 관련 공통 설정:
- DATA_PATH: 학습용 CSV
- MODEL_PATH: 학습된 모델
- FEATURE_PATH: 학습 당시 feature 리스트
"""

# belong/ml/config.py

from pathlib import Path

ML_ROOT = Path(__file__).resolve().parent

# 학습용 CSV
DATA_PATH = ML_ROOT / "merged_sum.csv"

# 모델 저장 경로
MODEL_PATH = ML_ROOT / "lonely_death_model.pkl"

# 학습 시 생성되는 feature 목록
FEATURE_PATH = ML_ROOT / "lonely_death_features.pkl"

# 타깃 컬럼명
TARGET_COL = "값"

# (옵션) 미래 예측용 CSV
FUTURE_PRED_PATH = ML_ROOT / "future_pred_2026_2075_v1_1_linear.csv"
