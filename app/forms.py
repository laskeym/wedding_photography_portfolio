from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.fields.html5 import EmailField, DateField
from wtforms.validators import DataRequired, Email, Length


class ContactForm(FlaskForm):
  first_name = StringField('First Name', validators=[DataRequired()])
  last_name = StringField('Last Name', validators=[DataRequired()])
  email = EmailField('Email Address', validators=[DataRequired(), Email()])
  subject = StringField('Subject', validators=[DataRequired(), Length(max=35)])
  message = TextAreaField('Message', validators=[DataRequired(), Length(max=200)])
  submit = SubmitField('Submit')