import pandas as pd
from pathlib import Path
import numpy as np

from.data_prep import prep_data

def rolling_sharpe(y):
    year_trading_days = 252
    #return np.sqrt(126) * (y.mean() / y.std()) # 21 days per month X 6 months = 126
    return (y.mean() * year_trading_days) / (y.std() * np.sqrt(year_trading_days))

def sharpe_ratio (cryptocoin, window_size):
    # Get the coin closing data form all the exchanges
    df = prep_data(cryptocoin)
    year_trading_days = 252

    #df_daily_returns = df.pct_change().dropna()
    df_daily_returns = df.pct_change()
     
    df1 = df_daily_returns.rolling(window=int(window_size)).apply(rolling_sharpe)
    return df1
