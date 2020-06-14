from flask import Flask
app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    return '<h1>Home Page</h1>'


@app.route('/about')
def about():
    return '<h1>About Page</h1>'


if __name__ == '__main__':  # When we run flaskblog1.py directly, it executes the following commands
    app.run(debug=True)

# https://flask.palletsprojects.com/en/1.1.x/quickstart/
# to Run on Terminal -> set FLASK_APP=flaskblog1.py
# then -> flask run

# Run in debug mode
# set FLASK_DEBUG = 1
