from typing import Optional

from forex_miner_thor.strategies import Strategy
from forex_miner_thor.model.trade import TradeSignal


class MockStrategy(Strategy):
    def __init__(self, trade_signal: TradeSignal):
        self.trade_signal = trade_signal

    def apply(self) -> Optional[TradeSignal]:
        return self.trade_signal

