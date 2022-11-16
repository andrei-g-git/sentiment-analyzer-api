from textblob import TextBlob

class Sentiment_analyzer_textblob:
    def __init__(self):
        pass

    def analyze_sentiment(self, corpus):
        blob = TextBlob(corpus)
        polarity = blob.polarity
        subjectivity = blob.subjectivity
        return polarity, subjectivity   