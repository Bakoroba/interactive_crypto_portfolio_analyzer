import pandas as pd
from pathlib import Path

from.data_prep import prep_data
def arbitrage(cryptocoin, window_size):
    df = prep_data(cryptocoin)
    #df = df.dropna()
    df_daily_returns = df.pct_change(periods=int(window_size))
    #df_daily_returns = df.rolling(windows=int(window_size)).mean()
     
     
    df1 = df_daily_returns
    return df