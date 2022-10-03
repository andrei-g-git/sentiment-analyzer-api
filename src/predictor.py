from sklearn.feature_extraction.text import CountVectorizer,TfidfVectorizer
from sklearn.metrics import accuracy_score 
from sklearn.base import TransformerMixin 
from sklearn.pipeline import Pipeline
from sklearn.svm import LinearSVC

class Predictors(TransformerMixin):   
    def __init__(self):
        super().__init__()
        self.utils = None

    def set_utils(self, utils_object):
        self.utils = utils_object

    def transform(self, X, **transform_params):
        return [self.utils.strip_and_lower(text) for text in X]

    def fit(self, X, y=None, **fit_params):
        return self

    def get_params(self, deep=True):
        return {}