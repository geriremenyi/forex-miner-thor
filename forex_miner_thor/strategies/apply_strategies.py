from typing import Optional
import pandas as pd

from forex_miner_thor.model.trade import TradeSignal
from forex_miner_thor.strategies.get_strategies import get_strategies


def apply_strategies(instrument: str, data: pd.DataFrame):
    strategies = get_strategies(instrument, data)
    final_trade_signal: Optional[TradeSignal] = None

    for strategy in strategies:
        trade_signal = strategy.apply()
        if (
            (trade_signal is not None)
            and (final_trade_signal is None or final_trade_signal.confidence < trade_signal.confidence)
        ):
            final_trade_signal = trade_signal

    return final_trade_signal

