import pandas as pd
from pathlib import Path

from.data_prep import prep_data

def daily_returns(window_size):
    # Read the aapl data, set the `date` as the index
    aapl_csv_path = Path("data/aapl.csv")

    aapl_df = pd.read_csv(
        aapl_csv_path, index_col="date", infer_datetime_format=True, parse_dates=True
    )
    # Use the `drop` function to drop the extra columns
    aapl_df.drop(columns=["volume"], inplace=True)

    #window_size =7
    df1 = aapl_df.rolling(window=window_size).mean() 
    return df1
    