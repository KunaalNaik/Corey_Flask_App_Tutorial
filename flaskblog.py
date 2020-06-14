from flask import Flask, render_template, url_for
app = Flask(__name__)


posts = [
    {
        'author': 'Kunaal',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Kunaal',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts = posts)


@app.route('/about')
def about():
    return render_template('about.html', title = 'About')


if __name__ == '__main__':  # When we run flaskblog1.py directly, it executes the following commands
    app.run(debug=True)

# https://flask.palletsprojects.com/en/1.1.x/quickstart/
# to Run on Terminal -> set FLASK_APP=flaskblog1.py
# then -> flask run

# Run in debug mode
# set FLASK_DEBUG = 1
