import spacy
from spacy.lang.en.stop_words import STOP_WORDS
import string
from textblob import TextBlob

class Analyzer:

    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm") #default

    def set_language(self, module_name):
        self.nlp = spacy.load(module_name)

    def remove_stop_words(self, corpus): #this removes too many important words that give a lot of weight to various sentiments in a corpus
        stop_words = list(STOP_WORDS)
        doc = self.nlp(corpus)
        tokens = [token.text for token in doc if token.text not in stop_words and token.text not in string.punctuation]

        return " ".join(tokens)

    def process_sentiment_advanced(self, corpus):
        blob = TextBlob(corpus)
        polarity = blob.polarity
        subjectivity = blob.subjectivity
        #Sintensity = blob.inte
        return polarity, subjectivity        
