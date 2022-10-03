from turtle import shape
import pandas as pd
import spacy
from spacy.lang.en.stop_words import STOP_WORDS
import string
from sklearn.feature_extraction.text import CountVectorizer,TfidfVectorizer
from sklearn.metrics import accuracy_score 
from sklearn.base import TransformerMixin 
from sklearn.pipeline import Pipeline
from sklearn.svm import LinearSVC
from utils import Utils #there;s no need for this kind of coupling ...

class Analyzer(TransformerMixin):

    def __init__(self):
        self.frames = []
        self.df = None
        self.nlp = spacy.load("en_core_web_sm") #default
        self.utils = None

    def set_frames(self, *args):
        self.frames = [arg for arg in args]
        for columnPairs in self.frames:
            columnPairs.columns = ["Message", "Target"]

    def set_df_with_keys(self, *args):
        self.df = pd.concat(
            self.frames,
            keys=[arg for arg in args]
        )   

    def set_utils(self, utils_object):
        self.utils = utils_object

    def df_to_csv(self, relative_path): #this doesn't need to be here...
        #ut = Utils()
        self.df.to_csv(self.utils.get_valid_path(relative_path))

    def set_language(self, module_name):
        self.nlp = spacy.load(module_name)

    def tokenize_without_stopwords(self, corpus):
        stop_words = list(STOP_WORDS)
        doc = self.nlp(corpus)
        tokens = [token.lemma_.lower().strip() if token.lemma_ != "-PRON-" else token.lower_ for token in doc] 
        tokens = [token for token in tokens if token not in stop_words and token not in string.punctuation]

        return tokens    

    #couple of overrides I think...
    def transform(self, X, **transform_params):
        return [self.utils.strip_and_lower(text) for text in X]

    def fit(self, X, y=None, **fit_params):
        return self

    def get_params(self, deep=True):
        return {}

