from flask import Flask, render_template, url_for, redirect, flash, session, logging, request
from data import Articles
import pymysql
from passlib.hash import sha256_crypt
from flask_wtf import Form
from forms import RegistrationForm,LoginForm
from wtforms import TextField, BooleanField, PasswordField, TextAreaField, validators


Articles = Articles()
app = Flask(__name__)
app.config['SECRET_KEY'] = 'efffe48c4cb7cb7e21d9764018a401b2'

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/articles')
def article():
    return render_template('articles.html',articles=Articles)


@app.route('/register',methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash("Your Account is created Successfully")
        return redirect(url_for('login'))
    return render_template('register.html',form=form)

if __name__ == '__main__':
    app.run(debug=True)
