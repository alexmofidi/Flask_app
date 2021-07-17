from flask import Flask
from flask import render_template
from logging.config import dictConfig
from flask import request
from flask import jsonify

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, alireza!</p>"

@app.route('/index')
def hello():
    return render_template('index.html')

@app.route('/sentiment',methods=['POST'])
def sentiment():
    if request.method == 'POST':
        response = {"message":request.get_json()['payload']}
        return jsonify(response)