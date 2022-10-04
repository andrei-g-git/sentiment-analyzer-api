# import pandas as pd
# from analyzer import Analyzer 
# from utils import Utils 
# from predictor import Predictors

# an = Analyzer()
# ut = Utils()
# an.set_frames(
#     pd.read_table(ut.get_valid_path("assets/data/yelp_labelled.txt")),
#     pd.read_table(ut.get_valid_path("assets/data/imdb_labelled.txt")),
#     pd.read_table(ut.get_valid_path("assets/data/amazon_cells_labelled.txt"))
# )

# an.set_df_with_keys('Yelp','IMDB','Amazon')
# an.set_utils(ut) #still not great but better than hard coding...

# an.df_to_csv("assets/data/sentimentdataset.csv")

# predictors = Predictors()
# predictors.set_utils(ut)

# an.create_scikit_pipelines(predictors)

# X_train, X_test, y_train, y_test = an.train_test_split(random_state=42)
# for (sample,pred) in zip(X_test, an.pipe.predict(X_test)):
#     print(sample,"Prediction=>",pred)

from analyzer_textblob import Analyzer

an = Analyzer()
polarity, subjectivity = an.process_sentiment_advanced("the waitress gave me an empty cup")
print ("polarity:  ", polarity, "   subjectivity:  ", subjectivity)