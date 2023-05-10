import pandas as pd
from pathlib import Path

from.data_prep import prep_data

def arbitrage(cryptocoin, window_size):
    # Create a dataframe containing the crypto data
   
    df = prep_data(cryptocoin)
    
    return df