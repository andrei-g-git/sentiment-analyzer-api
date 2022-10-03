from turtle import shape
import pandas as pd
import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from utils import Utils

class Analyzer:

    def __init__(self):
        self.frames = []
        #self.keys = []
        self.df = None
        self.nlp = spacy.load("en_core_web_sm") #default

    def set_frames(self, *args):
        self.frames = [arg for arg in args]
        for columnPairs in self.frames:
            columnPairs.columns = ["Message", "Target"]
            #print(columnPairs.columns)

    def set_df_with_keys(self, *args):
        self.df = pd.concat(
            self.frames,
            keys=[arg for arg in args]
        )   
        #print(self.df.shape)
        #print(self.df.head())  

    def df_to_csv(self, relative_path):
        ut = Utils()
        self.df.to_csv(ut.get_valid_path(relative_path))

    def set_language(self, module_name):
        self.nlp = spacy.load(module_name)

    def remove_stopwords(self, corpus):
        stop_words = list(STOP_WORDS)
        #print(stop_words)  
        doc = self.nlp(corpus) 
            
