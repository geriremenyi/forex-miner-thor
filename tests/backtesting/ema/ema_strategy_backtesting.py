from backtesting import Strategy
from backtesting.lib import crossover

from forex_miner_thor.strategies.ema.ema import ema


class EmaStrategyBackTesting(Strategy):
    n1 = 10
    n2 = 20

    def init(self):
        # Precompute the two moving averages
        self.ema1 = self.I(ema, self.data.Close, self.n1)
        self.ema2 = self.I(ema, self.data.Close, self.n2)

    def next(self):
        # If sma1 crosses above sma2, close any existing
        # short trades, and buy the asset
        if crossover(self.ema1, self.ema2):
            self.position.close()
            self.buy()

        # Else, if sma1 crosses below sma2, close any existing
        # long trades, and sell the asset
        elif crossover(self.ema1, self.ema2):
            self.position.close()
            self.sell()

