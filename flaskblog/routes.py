from flaskblog.models import User,Post
from flask import render_template, url_for, redirect, flash
from flaskblog.forms import RegistrationForm,LoginForm
from flaskblog import app, db, bcrypt
from flaskblog.data import Articles

posts = Articles()
@app.route('/')
def home():
    return render_template('home.html',posts=posts)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/articles')
def articles():
    return render_template('articles.html',posts=posts)


@app.route('/register',methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_pwd = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_pwd)
        db.session.add(user)
        db.session.commit()
        flash('Account created successfully. Please login','success')
        return redirect(url_for('login'))
    return render_template('register.html',form=form)


@app.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data=='mohsin@gmail.com' and form.password.data =='123':
            flash('Login Successful','success')
            return redirect(url_for('home'))
        else:
            flash('Please check your email and password','danger')
    return render_template('login.html',form=form)
