import spacy
from spacy.lang.en.stop_words import STOP_WORDS
import string
from textblob import TextBlob

#test
from nrclex import NRCLex
import numpy as np
import pandas as pd
from negspacy.negation import Negex

class Analyzer:

    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm") #default
        self.emotions_object = None
        self.emotions_spacy_model = spacy.load("en_textcat_goemotions") #default
        self.emotions_spacy_model.add_pipe("sentencizer")
        self.add_negex_pipe()

    def set_language(self, module_name):
        self.nlp = spacy.load(module_name)

    def generate_emotions_object(self, corpus):
        self.emotions_object = NRCLex(corpus)

    def remove_stop_words(self, corpus): #this removes too many important words that give a lot of weight to various sentiments in a corpus
        stop_words = list(STOP_WORDS)
        doc = self.nlp(corpus)
        tokens = [token.text for token in doc if token.text not in stop_words and token.text not in string.punctuation]

        return " ".join(tokens)

    def process_sentiment_advanced(self, corpus):
        blob = TextBlob(corpus)
        polarity = blob.polarity
        subjectivity = blob.subjectivity

        #test
        # emotion = NRCLex(corpus)
        # print("EMOTIONS:   ", emotion.affect_dict)

        return polarity, subjectivity        

    # def analyze_emotions(self, corpus):
    #     emotion_object = NRCLex(corpus)
    #     affections_dictionary = emotion_object.affect_dict
    #     top_emotion = emotion_object.top_emotions
    #     emotion_scores = emotion_object.raw_emotion_scores
    #     affection_frequencies = emotion_object.affect_frequencies

    def get_affection_dictionary(self):
        return self.emotions_object.affect_dict

    def get_top_emotions(self):
        return self.emotions_object.top_emotions

    def get_emotion_scores(self):
            return self.emotions_object.raw_emotion_scores

    def get_affection_frequencies(self):
            return self.emotions_object.affect_frequencies          

    def add_negex_pipe(self):
        nlp = self.emotions_spacy_model
        nlp.add_pipe("negex", config={
            "ent_types":[
                "admiration",
                "amusement",
                "anger",
                "annoyance",
                "approval",
                "caring",
                "confusion",
                "curiosity",
                "desire",
                "disappointment",
                "disapproval",
                "disgust",
                "embarrassment",
                "excitement",
                "fear",
                "gratitude",
                "grief",
                "joy",
                "love",
                "nervousness",
                "optimism",
                "pride",
                "realization",
                "relief",
                "remorse",
                "sadness",
                "surprise",
                "neutral"                
            ]
        })
        print("PIPELINES^^^^^^^^^^^^   \n", nlp.pipe_names)

    # def getEmotionWithNegation(entity):
    #     return {
    #         emotion: entity.text,
    #         negation: entity._.negex
    #     }

    def get_goemotions(self, corpus):
        nlp = self.emotions_spacy_model
        doc = nlp(corpus)
        print("tesssttttttt==================================  ", [sent for sent in doc.sents])
        return [ 
            {
                "emotion": ent.text,
                "negation": ent._.negex
            }
            for ent in doc.ents
        ]





