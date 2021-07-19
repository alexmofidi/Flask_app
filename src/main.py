from flask import Flask
from flask import render_template
from logging.config import dictConfig
from flask import request
from flask import jsonify
from google.cloud import language_v1

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

        client = language_v1.LanguageServiceClient()
        document = language_v1.Document(content=request.get_json()['payload'], type_=language_v1.Document.Type.PLAIN_TEXT)
        sentiment = client.analyze_sentiment(request={'document': document}).document_sentiment
        # print("Text: {}".format(text))
        print("Sentiment: {}, {}".format(sentiment.score, sentiment.magnitude))
        resp = "Sentiment: " + str(sentiment.score) + ", " + str(sentiment.magnitude)
        response = {"message":resp}
        return jsonify(response)