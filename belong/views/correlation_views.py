from flask import Blueprint, render_template
from belong.forms.correlation_forms import CorrelationOverviewForm
from belong.services.correlation_service import CorrelationService

bp = Blueprint("correlation", __name__, url_prefix="/correlation")
service = CorrelationService()

GU_CHOICES = [
    ("강남구","강남구"), ("강동구","강동구"), ("강북구","강북구"), ("강서구","강서구"),
    ("관악구","관악구"), ("광진구","광진구"), ("구로구","구로구"), ("금천구","금천구"),
    ("노원구","노원구"), ("도봉구","도봉구"), ("동대문구","동대문구"), ("동작구","동작구"),
    ("마포구","마포구"), ("서대문구","서대문구"), ("서초구","서초구"), ("성동구","성동구"),
    ("성북구","성북구"), ("송파구","송파구"), ("양천구","양천구"), ("영등포구","영등포구"),
    ("용산구","용산구"), ("은평구","은평구"), ("종로구","종로구"), ("중구","중구"),
    ("중랑구","중랑구")
]

@bp.route("/overview", methods=["GET","POST"])
def overview():
    form = CorrelationOverviewForm()
    form.gu.choices = GU_CHOICES

    results = None

    if form.validate_on_submit():
        filters = {"gu": form.gu.data}
        results = service.get_overview_results(filters)

    return render_template("correlation/overview.html",
                           form=form,
                           results=results)
