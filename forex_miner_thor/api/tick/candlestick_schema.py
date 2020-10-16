from marshmallow import Schema, fields, post_load

from forex_miner_thor.api.tick.candlestick import Candlestick


class CandlestickSchema(Schema):
    open = fields.Float()
    close = fields.Float()
    high = fields.Float()
    low = fields.Float()

    @post_load
    def make_candlestick(self, data, **kwargs):
        return Candlestick(**data)
