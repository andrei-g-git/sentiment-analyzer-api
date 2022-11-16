from http.server import HTTPServer, BaseHTTPRequestHandler
import socketserver
import pandas as pd
from analyzer_new import Analyzer 
from utils import Utils 
from predictor import Predictors
import json
from api_handlers import ApiHandler as API
#from analysis.emotion_detector_test import Emotion_detector_test
from analysis.analyzer import Analyzer as RealAnalyzer
from analysis.emotion_detector import Emotion_detector


def init_analyzer():
    print("initializing analyzer")
    an = Analyzer()
    ut = Utils()
    an.set_frames(
        pd.read_table(ut.get_valid_path("assets/data/yelp_labelled.txt")),
        pd.read_table(ut.get_valid_path("assets/data/imdb_labelled.txt")),
        pd.read_table(ut.get_valid_path("assets/data/amazon_cells_labelled.txt"))
    )

    an.set_df_with_keys('Yelp','IMDB','Amazon')
    an.set_utils(ut)

    predictors = Predictors()
    predictors.set_utils(ut)

    an.create_scikit_pipelines(predictors)

    X_train, X_test, y_train, y_test = an.train_test_split(random_state=42)

    print("analyzer initialized")

    return an

#analyzer = init_analyzer() #can't see another way to achieve this...
analyzer = Analyzer()
class AnalyzerServer(BaseHTTPRequestHandler):
    
    def do_GET(self):
        self.handle_post_headers("/test")
        print("prepare to send response")
        self.wfile.write(bytes("request received", encoding="utf8"))

    def do_POST(self):
        self.handle_post_headers("/analyze")

        api = API()
        body = api.load_request_body(self) 
        text = body["text"]

        #predictionArray = analyzer.pipe.predict([text])
        polarity, subjectivity = analyzer.process_sentiment_advanced(text)

        sentiment = "neutral"
        #range change from -1,1 to 1,3
        #convert range as analog to 1, 5
        
        new_polarity = polarity + 2
        old_range_span = 2
        new_range_span = 5 - 1
        #multiplier = new_range_span / old_range_span
        #score = new_polarity * multiplier
        ut = Utils()
        score = ut.scale_number(polarity, -1, 1, 1, 5)

        if polarity > 0.2: 
            sentiment = "positive"
        elif polarity < -0.2:
            sentiment = "negative"

        #########################
        analyzer.generate_emotions_object(text)
        affection_dictionary = analyzer.get_affection_dictionary()
        top_emotions = analyzer.get_top_emotions()
        emotion_scores = analyzer.get_emotion_scores()
        affection_frequencies = analyzer.get_affection_frequencies()
        
        print("SCORES::::  ", emotion_scores)
        print("DICT----- ", affection_dictionary)
        print("FREQUENCIES:    :      :    ", affection_frequencies)

        #############################################
        #analyzer.add_negex_pipe()   --- makes no sense to keep adding pipelines here on every post request
        print("---Spacy Emotions with negex:\n     ", analyzer.get_goemotions(text))#[ emotion_with_negation["emotion"] for emotion_with_negation in analyzer.get_goemotions(text)])


        ########
        # BERT
        anal = RealAnalyzer()
        anal.set_emotion_detector(Emotion_detector())
        emotions = anal.assess_emotions(text)
        print("######### EMOTIONS WITH ROBERTA ######### \n ", emotions, " \n ########################################")

        data = {
            "score": score,
            "sentiment": sentiment,
            "subjectivity": subjectivity,
            "emotions": affection_frequencies
        }
        response = json.dumps(data)
        self.wfile.write(bytes(response, "utf8"))

    def set_pipe(self, pipe):
        self.pipe = pipe

    def handle_post_headers(self, path):
        self.send_response(200)
        self.path = path
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header("Content-type", "application/json")
        self.end_headers()

    @staticmethod
    def init_server(HOST, PORT):
        server = HTTPServer((HOST, PORT), AnalyzerServer) #so this passes it's class before it can fully instantiate? ...
        print("server running at ", HOST, " ", PORT)
        server.serve_forever()
        server.server_close()
        print("server stopped...")
        
        return "Server running at ", HOST, "  on port ", PORT      

