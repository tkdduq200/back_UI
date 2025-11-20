# belong/ml/train_lonely_death.py

import os
import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

from belong.ml.config import DATA_PATH, MODEL_PATH, FEATURE_PATH, TARGET_COL


def train_model():
    df = pd.read_csv(DATA_PATH)

    if TARGET_COL not in df.columns:
        raise RuntimeError(f"타겟 '{TARGET_COL}'이 CSV에 없습니다!")

    # 1) X, y 분리
    X = df.drop(columns=[TARGET_COL])
    y = df[TARGET_COL]

    # 2) One-hot
    X = pd.get_dummies(X, drop_first=True)

    # 3) 학습 feature 목록 저장
    feature_cols = X.columns.tolist()
    joblib.dump(feature_cols, FEATURE_PATH)

    # 4) Train/Test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # 5) 모델 학습
    model = LinearRegression()
    model.fit(X_train, y_train)

    # 6) 모델 저장
    joblib.dump(feature_cols, FEATURE_PATH)

    print("✔ lonely_death_model.pkl 저장 완료")
    print("✔ lonely_death_features.pkl 저장 완료")
    print("✔ feature 갯수:", len(feature_cols))
    return model


if __name__ == "__main__":
    train_model()
