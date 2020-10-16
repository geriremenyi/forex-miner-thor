import datetime

from forex_miner_thor.api.tick.candlestick import Candlestick


class TickInstrument(object):
    def __init__(
            self,
            instrument: str,
            time: datetime,
            volume: int,
            bid: Candlestick,
            mid: Candlestick,
            ask: Candlestick
    ):
        self.instrument = instrument
        self.time = time
        self.volume = volume
        self.bid = bid
        self.mid = mid
        self.ask = ask

