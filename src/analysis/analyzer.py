class Analyzer:
    def __init__(self):
        self.sentiment_analyzer = None
        self.emotion_detector = None

    def set_sentiment_analyzer(self, analyzer):
        self.sentiment_analyzer = analyzer

    def set_emotion_detector(self, detector):
        self.emotion_detector = detector

    def analyze_sentiment(self, corpus):
        return self.sentiment_analyzer.analyze_sentiment(corpus)

    def assess_emotions(self, corpus):
        return self.emotion_detector.assess_emotions(corpus)       