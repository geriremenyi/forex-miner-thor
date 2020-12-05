from forex_miner_thor.model.trade import TradeDirection


class TradeSignal:
    def __init__(self, instrument: str, direction: TradeDirection, confidence: float):
        self.instrument = instrument
        self.direction = direction
        self.confidence = confidence
