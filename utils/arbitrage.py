import pandas as pd
from pathlib import Path

from.data_prep import prep_data
<<<<<<< HEAD
def arbitrage(cryptocoin, window_size,value4):
    df = prep_data(cryptocoin)
    
    return df, df.max(), df.min()
=======

def arbitrage(cryptocoin, window_size):
    # Create a dataframe containing the crypto data
   
    df = prep_data(cryptocoin)
    
    return df
>>>>>>> ef023ae487edf1336b375b087f78ef918debc2a9
