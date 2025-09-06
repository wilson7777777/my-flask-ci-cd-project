from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello again, CI/CD!'

@app.route('/about')
def about():
    return 'This is a simple Flask application deployed with a CI/CD pipeline.'
