from flask_wtf import FlaskForm
from wtforms import StringField, SelectMultipleField, IntegerField, \
    SelectField, BooleanField, SubmitField
from wtforms.validators import DataRequired, NumberRange


class JobForm(FlaskForm):
    job = StringField('Job title', validators=[DataRequired()])
    team_leader_id = SelectField('Team Leader id', validators=[DataRequired()])
    work_size = IntegerField('Work size', validators=[DataRequired(), NumberRange(1)])
    collaborators = SelectMultipleField('Collaborators')
    is_finished = BooleanField('Is job finished?')
    submit = SubmitField('Save')
