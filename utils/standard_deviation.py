import pandas as pd
from pathlib import Path
import numpy as np

from.data_prep import prep_data

def rolling_sharpe(y):
    return np.sqrt(126) * (y.mean() / y.std()) # 21 days per month X 6 months = 126

def standard_deviation (cryptocoin, window_size):
# Get the coin closing data form all the exchanges
    df = prep_data(cryptocoin)
    
#df_daily_returns = df.pct_change().dropna()
    df_daily_returns = df.pct_change()
     
    df1 = df_daily_returns.rolling(window=window_size).std()
    return df1