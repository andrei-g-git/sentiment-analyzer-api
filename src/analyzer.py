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
from sklearn.model_selection import train_test_split
from utils import Utils #there;s no need for this kind of coupling ...
class Analyzer():

    def __init__(self):
        self.frames = []
        self.df = None
        self.nlp = spacy.load("en_core_web_sm") #default
        self.utils = None
        self.pipe = None
        #self.predictors = None

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

    # def set_predictors(self, predictors):
    #     self.predictors = predictors

    def df_to_csv(self, relative_path): #this doesn't need to be here...
        #ut = Utils()
        self.df.to_csv(self.utils.get_valid_path(relative_path))

    def set_language(self, module_name):
        self.nlp = spacy.load(module_name)

    def tokenize_without_stopwords(self, corpus):
        stop_words = list(STOP_WORDS)
        doc = self.nlp(corpus)
        tokens = [token.lemma_.lower().strip() if token.lemma_ != "-PRON-" else token.lower_ for token in doc] #it think this return strings, not tokens (the first expression might stringify)
        tokens = [token for token in tokens if token not in stop_words and token not in string.punctuation]

        return tokens    

    def create_scikit_pipelines(self, predictors):
        vectorizer = CountVectorizer(tokenizer = self.tokenize_without_stopwords, ngram_range=(1,1)) 
        classifier = LinearSVC()
        self.pipe = Pipeline([               
            ("cleaner", predictors),
            ('vectorizer', vectorizer),
            ('classifier', classifier)   
        ])

    def train_test_split_mine(self, test_ratio=0.2, random_state=30):
        X = self.df['Message']
        ylabels = self.df['Target']
        X_train, X_test, y_train, y_test = train_test_split(X, ylabels, test_size=test_ratio, random_state=random_state)      

        self.pipe.fit(X_train, y_train) 

        return X_train, X_test, y_train, y_test
        