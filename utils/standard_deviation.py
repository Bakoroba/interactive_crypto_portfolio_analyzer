import pandas as pd
from pathlib import Path
import numpy as np

from.data_prep import prep_data

def rolling_sharpe(y):
    return np.sqrt(126) * (y.mean() / y.std()) # 21 days per month X 6 months = 126

def standard_deviation (window_size):
    # Read the aapl data, set the `date` as the index
    aapl_csv_path = Path("data/aapl.csv")

    aapl_df = pd.read_csv(
        aapl_csv_path, index_col="date", infer_datetime_format=True, parse_dates=True
    )
    # Use the `drop` function to drop the extra columns
    aapl_df.drop(columns=["volume"], inplace=True)
    daily_returns_aapl = aapl_df.pct_change().dropna()
    #window_size =7
    #df1 = aapl_df.rolling(window=window_size).mean() 
    df1 = daily_returns_aapl.rolling(window=window_size).apply(rolling_sharpe)
    return df1