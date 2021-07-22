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
        #print("Sentiment: {}, {}".format(sentiment.score, sentiment.magnitude))
        Sent="Undecided"
        if sentiment.score > (.1) :
            Sent="Possitive"
        elif sentiment.score < (-.1) :
            Sent="Negative"
        else:
            Sent= "Neutral"
        resp = "Sentiment: {} The score is: ".format(Sent) + str(round(sentiment.score,2)) + ", " + str(round(sentiment.magnitude,2))
        response = {"message":resp}
        return jsonify(response)

@app.route('/entity',methods=['POST'])
def entity():
    if request.method == 'POST':

        client = language_v1.LanguageServiceClient()
        type_ = language_v1.Document.Type.PLAIN_TEXT
        language = "en"
        document = language_v1.Document(content=request.get_json()['payload'], type_=language_v1.Document.Type.PLAIN_TEXT, language= language)
        encoding_type = language_v1.EncodingType.UTF8
        response = client.analyze_entities(request = {'document': document, 'encoding_type': encoding_type})
        resp=''
        for entity in response.entities:
            resp += "Entity: {}".format(entity.name) +"--> " + "Entity type: {}".format(language_v1.Entity.Type(entity.type_).name) + "\n"
        print("Entity:  {}".format(resp))
        response = {"message":resp}
        return jsonify(response)

@app.route('/class',methods=['POST'])
def classify():
    if request.method == 'POST':

        client = language_v1.LanguageServiceClient()
        type_ = language_v1.Document.Type.PLAIN_TEXT

        language = "en"
        document = language_v1.Document(content=request.get_json()['payload'], type_=language_v1.Document.Type.PLAIN_TEXT, language= language)
        response = client.classify_text(request = {'document': document })
        resp=''
        for category in response.categories:
            resp+= u"Category name: {}".format(category.name)  + "--> " + "Confidence: {}".format(round(category.confidence,2))  +  "\n"

        print("Class:  {}".format(resp))
        response = {"message":resp}
        return jsonify(response)

@app.route('/summerize',methods=['POST'])
def summerize():
    if request.method == 'POST':

        client = language_v1.LanguageServiceClient()
        type_ = language_v1.Document.Type.PLAIN_TEXT

        language = "en"
        document = language_v1.Document(content=request.get_json()['payload'], type_=language_v1.Document.Type.PLAIN_TEXT, language= language)
        encoding_type = language_v1.EncodingType.UTF8
        response = client.classify_text(request = {'document': document})
        resp=''
        for category in response.categories:
            resp+= u"Category name: {}".format(category.name)  + "    " + "Confidence: {}".format(category.confidence)  + "                       "

        print("Class:  {}".format(resp))
        response = {"message":resp}
        return jsonify(response)
