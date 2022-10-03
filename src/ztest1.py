import pandas as pd
import os
from analyzer import Analyzer 
from utils import Utils 
from predictor import Predictors

an = Analyzer()
ut = Utils()
an.set_frames(
    pd.read_table(ut.get_valid_path("assets/data/yelp_labelled.txt")),
    pd.read_table(ut.get_valid_path("assets/data/imdb_labelled.txt")),
    pd.read_table(ut.get_valid_path("assets/data/amazon_cells_labelled.txt"))
)

an.set_df_with_keys('Yelp','IMDB','Amazon')
an.set_utils(ut) #still not great but better than hard coding...

#an.df_to_csv("assets/data/sentimentdataset.csv")

# tokens = an.tokenize_without_stopwords("This is how John Walker was walking. He was also running beside the lawn.")
# print(tokens)

predictors = Predictors()
predictors.set_utils(ut)

an.create_scikit_pipelines(predictors)

X_train, X_test, y_train, y_test = an.train_test_split(random_state=42)
for (sample,pred) in zip(X_test, an.pipe.predict(X_test)):
    print(sample,"Prediction=>",pred)


# print("X_train len:  ", len(X_train))
# print("X_test len:  ", len(X_test))
