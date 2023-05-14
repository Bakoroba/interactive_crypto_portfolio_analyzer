import pandas as pd
from pathlib import Path
import numpy as np

from.data_prep import prep_data

<<<<<<< HEAD
def standard_deviation (cryptocoin, window_size,value4):
    # Get the coin closing data form all the exchanges
=======
def standard_deviation (cryptocoin, window_size):
    # Get the coin closing data from all the exchanges
>>>>>>> ef023ae487edf1336b375b087f78ef918debc2a9
    df = prep_data(cryptocoin)
    # Calulate the rolling standard devition
    df_standard_deviation  = df.rolling(window=int(window_size)).std()
    
    # Return the rolling std for plotting
<<<<<<< HEAD
    return df_standard_deviation,df_standard_deviation.max(),df_standard_deviation.min()
=======
    return df_standard_deviation
>>>>>>> ef023ae487edf1336b375b087f78ef918debc2a9
