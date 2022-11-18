from flask import Flask, make_response, request
from flask_cors import CORS
import json
from analysis.analyzer import Analyzer as RealAnalyzer
from analysis.sentiment_analyzer_textblob import Sentiment_analyzer_textblob as Sentiment_analyzer
from analysis.emotion_detector import Emotion_detector

an = RealAnalyzer()
#an.set_sentiment_analyzer(Sentiment_analyzer())
#an.set_emotion_detector(Emotion_detector())

app = Flask(__name__)
CORS(app)

app.debug = True

@app.route("/analyze", methods=["POST"])
def post_sentiment_and_emotions():

    data = json.loads(
        request
            .data
            .decode("utf-8"),
        strict=False
    )  

    #data_object = json.loads(data, strict=False)
    print("DATA:   " + data["text"])


    response = make_response("here's the general sentiment and emotions object")

    #response.headers.add('Access-Control-Allow-Origin', '*')
    #response.headers.add("Content-Type", "application/json; charset=utf-8")

    return response

if __name__ == '__main__':
    app.run(host="localhost", port=5000)    