from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.fields.html5 import EmailField, DateField
from wtforms.validators import DataRequired, Email


class ContactForm(FlaskForm):
  first_name = StringField('First Name', validators=[DataRequired()])
  last_name = StringField('Last Name', validators=[DataRequired()])
  email = EmailField('Email Address', validators=[DataRequired(), Email()])
  date = DateField('Date of Desired Appointment', validators=[DataRequired()])
  submit = SubmitField('Submit')