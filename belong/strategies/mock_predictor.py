from .predictor_strategy import PredictorStrategy


class MockPredictor(PredictorStrategy):
    """
    진짜 ML 모델 대신 사용하는 Mock Predictor.
    고정된 값을 반환해서 서비스 로직이 정상 동작하는지 테스트할 때 사용함.
    """

    def predict(self, gu: str, year: int):
        # 그냥 예시로 가짜 예측값 1234를 반환
        return 1234

    def predict_with_detail(self, gu: str, year: int):
        # 예시용 디테일 버전 (진짜 모델이 생기면 교체)
        return {
            "y_pred": 1234,
            "y_true": None,
        }
