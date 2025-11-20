from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField
from wtforms.validators import DataRequired

class CorrelationOverviewForm(FlaskForm):
    gu = SelectField("자치구", validators=[DataRequired()])
    submit = SubmitField("조회")
