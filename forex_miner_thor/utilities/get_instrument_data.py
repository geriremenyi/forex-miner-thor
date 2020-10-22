import pandas as pd

from forex_miner_thor.utilities import get_or_create_instrument_file


def get_instrument_data(instrument: str, granularity: str) -> pd.DataFrame:
    return pd.read_csv(get_or_create_instrument_file(instrument, granularity), parse_dates=['Time'], index_col='Time')

