from forex_miner_thor.api.trade import TradeDirection


class TradeSignal:
    def __init__(self, instrument: str, direction: TradeDirection, stop_loss: float, take_the_profit: float):
        self.instrument = instrument
        self.direction = direction
        self.stop_loss = stop_loss
        self.take_the_profit = take_the_profit

