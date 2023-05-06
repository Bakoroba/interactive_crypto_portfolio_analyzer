import pandas as pd
from pathlib import Path

from.data_prep import prep_data

def daily_returns (coin):
    # Get the coin closing data form all the exchanges
    df = prep_data(coin)
    
    df_daily_returns = df.pct_change().dropna()
     
    df1 = df_daily_returns
    return df1
    