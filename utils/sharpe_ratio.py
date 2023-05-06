import pandas as pd
from pathlib import Path
import numpy as np

from.data_prep import prep_data

def rolling_sharpe(y):
    return np.sqrt(126) * (y.mean() / y.std()) # 21 days per month X 6 months = 126

def sharpe_ratio (cryptocoin):
    # Get the coin closing data form all the exchanges
    df = prep_data(cryptocoin)
    
    #df_daily_returns = df.pct_change().dropna()
    df_daily_returns = df.pct_change()
     
    df1 = df_daily_returns.rolling(window=180).apply(rolling_sharpe)
    return df1