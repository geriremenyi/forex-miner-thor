from marshmallow import Schema, fields, post_load

from forex_miner_thor.api.trade.trade_signal import TradeSignal


class TradeSignalSchema(Schema):
    instrument = fields.Str()
    direction = fields.Str()
    stop_loss = fields.Float()
    take_the_profit = fields.Float()

    @post_load
    def make_trade_signal(self, data, **kwargs):
        return TradeSignal(**data)

