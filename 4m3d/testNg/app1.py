from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "hello world"

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('test.html', name=name)