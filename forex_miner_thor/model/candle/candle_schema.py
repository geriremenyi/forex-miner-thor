from marshmallow import Schema, fields, post_load

from forex_miner_thor.model.candle import Candle, CandlestickSchema


class CandleSchema(Schema):
    time = fields.DateTime()
    volume = fields.Int()
    bid = fields.Nested(CandlestickSchema)
    mid = fields.Nested(CandlestickSchema)
    ask = fields.Nested(CandlestickSchema)

    @post_load
    def make_candle(self, data, **kwargs):
        return Candle(**data)

