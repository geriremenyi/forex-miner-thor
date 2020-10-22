from typing import List

from forex_miner_thor.model.candle import Candle


class Instrument(object):
    def __init__(
            self,
            instrument: str,
            granularity: str,
            candles: List[Candle]
    ):
        self.instrument = instrument
        self.granularity = granularity
        self.candles = candles

