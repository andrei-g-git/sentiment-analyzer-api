from flask import Flask, make_response, request, jsonify
from flask_cors import CORS
import git, json, time
from analysis.analyzer import Analyzer as RealAnalyzer
from analysis.sentiment_analyzer_textblob import Sentiment_analyzer_textblob as Sentiment_analyzer
from analysis.emotion_detector import Emotion_detector
from utils import Utils

an = RealAnalyzer()
an.set_sentiment_analyzer(Sentiment_analyzer())
an.set_emotion_detector(Emotion_detector())

app = Flask(__name__)
CORS(app)

app.debug = True

# @app.route("/git_push", methods=["POST"])
# def webhook():
#     repo = git.Repo(".", search_parent_directories=True)
#     origin = repo.remotes.origin
#     origin.pull()
#     return 'Updated PythonAnywhere successfully', 200

@app.route("/")
def welcome():
    return "Welcomeeeeeee!"
# if __name__ == "__main__":
#     app.run() #don't know if I need this route...

@app.route("/analyze", methods=["POST"])
def post_sentiment_and_emotions():

    data = json.loads(
        request
            .data
            .decode("utf-8"),
        strict=False
    )  
    print("DATA:   " + data["text"])

    corpus = data["text"]

    polarity, subjectivity = an.analyze_sentiment(corpus)
    sentiment = "neutral"
    if polarity > 0.2: 
        sentiment = "positive"
    elif polarity < -0.2:
        sentiment = "negative"

    ut = Utils()
    score = ut.scale_number(polarity, -1, 1, 1, 5)

    emotions = an.assess_emotions(corpus)

    response_data = {
        "score": score,
        "sentiment": sentiment,
        "subjectivity": subjectivity,
        "emotions": emotions
    }

    response = make_response(jsonify(response_data))

    time.sleep(2) # I have a fancy loading screen on my client and this thing processes the request too fast to see it

    return response

if __name__ == '__main__':
    #app.run(host="localhost", port=5000)   
    #app.run(host="192.168.42.206", port=5000)  
    app.run(host="192.168.42.206", port=80)