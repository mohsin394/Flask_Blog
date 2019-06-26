from flask_wtf import Form
from wtforms import StringField, TextAreaField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo, InputRequired, ValidationError
from flaskblog.models import User


class RegistrationForm(Form):
    username = StringField('Name',validators=[DataRequired(message="Enter Your Name Please"),Length(min=2, max=50)])
    email = StringField('Email',validators=[DataRequired(message="Enter Your Name Please"),Email()])
    password = PasswordField('Password',validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',validators=[DataRequired(),EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self,username):
        user = User.query.filter_by(username = username.data).first()
        if user:
            raise ValidationError('This username is already taken. Please choose another one')

    def validate_email(self,email):
        user = User.query.filter_by(email = email.data).first()
        if user:
            raise ValidationError('This email is already taken. Please choose another one')


class LoginForm(Form):
    email = StringField('Email',validators=[DataRequired(),Email()])
    password = PasswordField('Password',validators=[DataRequired(),Length(min=2,max=10)])
    submit = SubmitField('Sign In')
