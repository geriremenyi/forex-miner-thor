import datetime

from forex_miner_thor.model.candle import Candlestick


class Candle(object):
    def __init__(self, time: datetime, volume: int, bid: Candlestick, mid: Candlestick, ask: Candlestick):
        self.time = time
        self.volume = volume
        self.bid = bid
        self.mid = mid
        self.ask = ask

    def to_dict(self):
        # Currently only support mid for csv serialization
        return {
            'Time': self.time,
            'Open': self.mid.open,
            'High': self.mid.high,
            'Low': self.mid.low,
            'Close': self.mid.close,
            'Volume': self.volume,
        }

