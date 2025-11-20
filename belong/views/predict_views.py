# belong/views/predict_views.py

from datetime import datetime
from flask import Blueprint, render_template, request, flash
from werkzeug.utils import redirect
from typing import List

from belong.services.prediction_service import PredictionService
from belong.repositories.lonely_prediction_repository import LonelyPredictionRepository
from belong.strategies.ml_predictor import MLPredictor

bp = Blueprint("predict", __name__, url_prefix="/predict")

# ✅ 예측 서비스 인스턴스 (전략 + 리포지토리 주입)
_prediction_service = PredictionService(
    predictor=MLPredictor(),
    prediction_repository=LonelyPredictionRepository(),
)


@bp.route("/", methods=("GET", "POST"))
def index():
    """
    /predict/ - ML 기반 고독사 예측 + 시각화 렌더링
    """
    regions: List[str] = _prediction_service.get_regions()
    years: List[int] = _prediction_service.get_years()

    prediction = None           # LonelyPrediction 또는 None
    from_cache = False          # DB 캐시 여부

    # ✅ 차트용 데이터 (템플릿으로 넘겨서 시각화에 사용)
    chart_labels = []           # ['예측값', '실제값'] 이런 식
    chart_values = []           # [12.34, 10.0] 이런 식

    if request.method == "POST":
        gu = request.form.get("gu")
        year_raw = request.form.get("year")

        if not gu or not year_raw:
            flash("구와 연도를 모두 선택해 주세요.")
        else:
            try:
                year = int(year_raw)
            except ValueError:
                flash("연도 값이 올바르지 않습니다.")
            else:
                # ✅ PredictionService에게 예측 or 캐시 조회 요청
                prediction, from_cache = _prediction_service.get_or_predict(gu, year)

                if prediction is not None:
                    # 여기서부터는 "시각화용 데이터"를 준비하는 단계
                    # 기본은 예측값만 시각화
                    chart_labels = ["예측값"]
                    chart_values = [round(prediction.predicted_value, 2)]

                    # 실제값이 있는 과거 연도라면 실제값도 같이 시각화
                    if prediction.actual_value is not None:
                        chart_labels.append("실제값")
                        chart_values.append(round(prediction.actual_value, 2))

    # ✅ 템플릿으로 예측 결과 + 시각화 데이터 모두 전달
    return render_template(
        "predict/form.html",
        regions=regions,
        years=years,
        prediction=prediction,
        from_cache=from_cache,
        chart_labels=chart_labels,
        chart_values=chart_values,
    )


@bp.route("/future", methods=["GET", "POST"])
def future():
    """
    2026~2075년 장기 예측 (CSV 기반) 5년 단위 Bar Chart
    """
    gu_list: List[str] = _prediction_service.get_regions()
    selected_gu = gu_list[0] if gu_list else None

    if request.method == "POST":
        selected_gu = request.form.get("gu") or selected_gu

    records = []
    chart_years = []
    chart_values = []

    if selected_gu:
        # 50년 데이터 조회
        records = _prediction_service.get_future_curve(selected_gu)

        # ❶ 연도, 값 꺼내기
        years = [int(r["연도"]) for r in records]
        preds = [float(r["예측값_명"]) for r in records]

        # ❷ 5년 단위 구간 설정
        bins = [
            (2026, 2030),
            (2031, 2035),
            (2036, 2040),
            (2041, 2045),
            (2046, 2050),
            (2051, 2055),
            (2056, 2060),
            (2061, 2065),
            (2066, 2070),
            (2071, 2075),
        ]

        year_ranges = []
        binned_values = []

        # ❸ 각 구간 평균값 계산
        for start, end in bins:
            year_ranges.append(f"{start}~{end}")
            vals = [
                preds[i]
                for i in range(len(years))
                if start <= years[i] <= end
            ]
            avg_val = sum(vals) / len(vals) if vals else 0
            binned_values.append(round(avg_val, 2))

    return render_template(
        "predict/future_predict.html",
        gu_list=gu_list,
        selected_gu=selected_gu,
        records=records,
        year_ranges=year_ranges,
        binned_values=binned_values
    )



