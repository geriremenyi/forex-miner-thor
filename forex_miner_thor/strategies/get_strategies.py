from typing import List

import pandas as pd

from forex_miner_thor.strategies import Strategy
from forex_miner_thor.strategies.ema import EmaStrategy


def get_strategies(instrument: str, data: pd.DataFrame) -> List[Strategy]:
    return [EmaStrategy(instrument, data)]

