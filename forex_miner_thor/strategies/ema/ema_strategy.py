from typing import Optional

import pandas as pd

from forex_miner_thor.strategies.ema.ema import ema
from forex_miner_thor.strategies.strategy import Strategy
from forex_miner_thor.model.trade import TradeSignal, TradeDirection


class EmaStrategy(Strategy):
    n10: int = 10
    n20: int = 20

    def __init__(self, instrument: str, data: pd.DataFrame):
        self.instrument = instrument
        # Precalculate Close price ema for strategy
        self.data = data
        self.data['10EMA'] = ema(data['Close'], self.n10)  # Close price is used!
        self.data['20EMA'] = ema(data['Close'], self.n20)  # Close price is used!

    def apply(self) -> Optional[TradeSignal]:
        if (
            self.data.iloc[-2]['10EMA'] < self.data.iloc[-2]['20EMA'] and
            self.data.iloc[-1]['10EMA'] > self.data.iloc[-1]['20EMA'] and
            self.data['Volume'].quantile(0.75) <= self.data.iloc[-1]['Volume']
        ):
            return TradeSignal(self.instrument, TradeDirection.LONG, 1)

        elif (
                self.data.iloc[-2]['10EMA'] > self.data.iloc[-2]['20EMA'] and
                self.data.iloc[-1]['10EMA'] < self.data.iloc[-1]['20EMA'] and
                self.data['Volume'].quantile(0.75) <= self.data.iloc[-1]['Volume']
        ):
            return TradeSignal(self.instrument, TradeDirection.SHORT, 1)

        return None

