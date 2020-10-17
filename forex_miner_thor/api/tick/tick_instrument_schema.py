from marshmallow import Schema, fields, post_load

from forex_miner_thor.api.tick.tick_instrument import TickInstrument
from forex_miner_thor.api.tick.candlestick_schema import CandlestickSchema


class TickInstrumentSchema(Schema):
    instrument = fields.Str()
    time = fields.DateTime()
    volume = fields.Int()
    bid = fields.Nested(CandlestickSchema)
    mid = fields.Nested(CandlestickSchema)
    ask = fields.Nested(CandlestickSchema)

    @post_load
    def make_tick_instrument(self, data,  **kwargs):
        return TickInstrument(**data)

