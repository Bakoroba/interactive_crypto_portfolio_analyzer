import pandas as pd
from pathlib import Path

from.data_prep import prep_data

def daily_returns (coin, window_size, value4):
    # Get the coin closing data form all the exchanges
    df = prep_data(coin)
    
    df_daily_returns = df.pct_change(periods=int(window_size))
     
    df1 = df_daily_returns
    return df1, df1.max(),df1.min()
    