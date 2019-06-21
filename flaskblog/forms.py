from flask_wtf import Form
from wtforms import StringField, TextAreaField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo, InputRequired


class RegistrationForm(Form):
    username = StringField('Name',validators=[DataRequired(message="Enter Your Name Please"),Length(min=2, max=50)])
    email = StringField('Email',validators=[DataRequired(message="Enter Your Name Please"),Email()])
    password = PasswordField('Password',validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',validators=[DataRequired(),EqualTo('password')])
    submit = SubmitField('Sign Up')


class LoginForm(Form):
    email = StringField('Email',validators=[DataRequired(),Email()])
    password = PasswordField('Password',validators=[DataRequired(),Length(min=2,max=10)])
    submit = SubmitField('Sign In')
