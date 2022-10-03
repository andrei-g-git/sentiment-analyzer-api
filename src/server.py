from http.server import HTTPServer, BaseHTTPRequestHandler
import socketserver
import pandas as pd
from analyzer import Analyzer 
from utils import Utils 
from predictor import Predictors
import json
from api_handlers import ApiHandler as API

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

analyzer = init_analyzer()
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

        #predictionArray = self.pipe.predict([text])
        predictionArray = analyzer.pipe.predict([text])
        #print("ARRAY ++++++ ", predictionArray[0])
        response = "good"
        if predictionArray[0] == 0: 
            response = "bad"

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

    # def init_analyzer(self):
    #     print("initializing analyzer")
    #     an = Analyzer()
    #     ut = Utils()
    #     an.set_frames(
    #         pd.read_table(ut.get_valid_path("assets/data/yelp_labelled.txt")),
    #         pd.read_table(ut.get_valid_path("assets/data/imdb_labelled.txt")),
    #         pd.read_table(ut.get_valid_path("assets/data/amazon_cells_labelled.txt"))
    #     )

    #     an.set_df_with_keys('Yelp','IMDB','Amazon')
    #     an.set_utils(ut)

    #     predictors = Predictors()
    #     predictors.set_utils(ut)

    #     an.create_scikit_pipelines(predictors)

    #     X_train, X_test, y_train, y_test = an.train_test_split(random_state=42)

    #     #self.set_pipe(an.pipe)

    #     print("analyzer initialized")

    #     return an