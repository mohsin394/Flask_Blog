from flask import Flask, render_template, url_for
from data import Articles

Articles = Articles()
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/articles')
def article():
    return render_template('articles.html',articles=Articles)




if __name__ == '__main__':
    app.run(debug=True)
