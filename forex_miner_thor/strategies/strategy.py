from typing import Optional

from abc import ABC, abstractmethod

from forex_miner_thor.model.trade import TradeSignal


class Strategy(ABC):
    @abstractmethod
    def apply(self) -> Optional[TradeSignal]:
        pass

