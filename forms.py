from flask_wtf import Form
from wtforms import StringField, TextAreaField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class RegistrationForm(Form):
    name = StringField('Name',validators=[DataRequired,Length(min=2, max=50)])
    username = StringField('User Name',validators=[DataRequired,Length(min=2, max=50)])
    email = StringField('Email',validators=[DataRequired,Email])
    password = PasswordField('Password',validators=[DataRequired,Length(min=2,max=10)])
    confirm_password = PasswordField('Confirm Password',validators=[DataRequired,EqualTo('password')])
    submit = SubmitField()


class LoginForm(Form):
    email = StringField('Email',validators=[DataRequired,Email])
    password = PasswordField('Password',validators=[DataRequired,Length(min=2,max=10)])
    submit = SubmitField()
