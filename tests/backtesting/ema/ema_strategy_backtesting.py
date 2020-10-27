import pandas as pd
from backtesting.lib import SignalStrategy, TrailingStrategy

from forex_miner_thor.strategies.ema.ema import ema


class EmaStrategyBackTesting(SignalStrategy, TrailingStrategy):
    n1 = 10
    n2 = 20
    percentile = 75
    position_size_percentage = 10
    stop_loss = 2

    def init(self):
        # Init composed strategies
        super().init()

        # Precompute the two moving averages
        self.ema1 = self.I(ema, self.data.Close, self.n1)
        self.ema2 = self.I(ema, self.data.Close, self.n2)

        # Precompute volume percentile
        volume_percentile = pd.Series(self.data.Volume).quantile((self.percentile * 0.01))

        # Cross signal
        cross = (pd.Series(self.ema1) > self.ema2).astype(int).diff().fillna(0)

        # Volume signal
        volume = pd.Series((pd.Series(self.data.Volume) > volume_percentile)).astype(int).fillna(0)

        # Use 10% of the liquid balance for each trade
        entry_size = cross * volume * (self.position_size_percentage * 0.01)

        # Use the strategies implemented
        self.set_signal(entry_size)
        self.set_trailing_sl(self.stop_loss)

