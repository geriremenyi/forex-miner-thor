from marshmallow import Schema, fields, post_load

from forex_miner_thor.model.trade.trade_signal import TradeSignal


class TradeSignalSchema(Schema):
    instrument = fields.Str()
    direction = fields.Str()
    confidence = fields.Float()

    @post_load
    def make_trade_signal(self, data, **kwargs):
        return TradeSignal(**data)

