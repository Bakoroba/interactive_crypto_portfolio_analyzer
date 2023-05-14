# Compare the closing prices of a crypto currency on all exchanges
# Return the dataframe and max min values
import pandas as pd
from pathlib import Path

from.data_prep import prep_data

def arbitrage(cryptocoin, window_size,value4):
    df = prep_data(cryptocoin)
    
    return df, df.max(), df.min()
