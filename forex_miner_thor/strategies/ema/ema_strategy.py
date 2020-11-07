from typing import Optional

import pandas as pd

from forex_miner_thor.strategies.ema.ema import ema
from forex_miner_thor.strategies.strategy import Strategy
from forex_miner_thor.model.trade import TradeSignal, TradeDirection


class EmaStrategy(Strategy):
    n1: int = 70
    n2: int = 180
    percentile: float = 0.85

    def __init__(self, instrument: str, data: pd.DataFrame):
        self.instrument = instrument
        # Precalculate Close price ema for strategy
        self.data = data
        self.data['N1EMA'] = ema(data['Close'], self.n1)  # Close price is used!
        self.data['N2EMA'] = ema(data['Close'], self.n2)  # Close price is used!

    def apply(self) -> Optional[TradeSignal]:
        if (
            self.data.iloc[-2]['N1EMA'] < self.data.iloc[-2]['N2EMA'] and
            self.data.iloc[-1]['N1EMA'] > self.data.iloc[-1]['N2EMA'] and
            self.data['Volume'].quantile(self.percentile) <= self.data.iloc[-1]['Volume']
        ):
            return TradeSignal(self.instrument, TradeDirection.LONG, 1)

        elif (
                self.data.iloc[-2]['N1EMA'] > self.data.iloc[-2]['N2EMA'] and
                self.data.iloc[-1]['N1EMA'] < self.data.iloc[-1]['N2EMA'] and
                self.data['Volume'].quantile(self.percentile) <= self.data.iloc[-1]['Volume']
        ):
            return TradeSignal(self.instrument, TradeDirection.SHORT, 1)

        return None

