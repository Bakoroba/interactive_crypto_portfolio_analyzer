# Return the std dataframe and max min values

import pandas as pd
from pathlib import Path
import numpy as np

from.data_prep import prep_data

def standard_deviation (cryptocoin, window_size,value4):

    # Get the coin closing data from all the exchanges
    df = prep_data(cryptocoin)
    # Calulate the rolling standard deviation
    df_standard_deviation  = df.rolling(window=int(window_size)).std()
    
    # Return the rolling std for plotting
    return df_standard_deviation,df_standard_deviation.max(),df_standard_deviation.min()
