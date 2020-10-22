from typing import List

import pandas as pd

from forex_miner_thor.model.candle import Candle
from forex_miner_thor.utilities import get_or_create_instrument_file
from forex_miner_thor.utilities import get_instrument_data


def add_instrument_data(instrument: str, granularity: str, incoming_candles: List[Candle]) -> pd.DataFrame:
    # Get current candles
    candles = get_instrument_data(instrument, granularity)

    # Add new candles
    new_candles = pd.DataFrame.from_records([c.to_dict() for c in incoming_candles], index='Time')
    candles_to_save = candles.append(new_candles)
    candles_to_save = candles_to_save[~candles_to_save.index.duplicated(keep='last')]

    # Make sure it is ordered by time
    candles_to_save.sort_index()

    # Save back to file
    candles_to_save.to_csv(get_or_create_instrument_file(instrument, granularity))

    # Return data frame
    return candles_to_save

