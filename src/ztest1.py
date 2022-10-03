import pandas as pd
import os
from analyzer import Analyzer 
from utils import Utils 

an = Analyzer()
ut = Utils()
an.set_frames(
    pd.read_table(ut.get_valid_path("assets/data/yelp_labelled.txt")),
    pd.read_table(ut.get_valid_path("assets/data/imdb_labelled.txt")),
    pd.read_table(ut.get_valid_path("assets/data/amazon_cells_labelled.txt"))
)

an.set_df_with_keys('Yelp','IMDB','Amazon')

#an.df_to_csv("assets/data/sentimentdataset.csv")

an.remove_stopwords()