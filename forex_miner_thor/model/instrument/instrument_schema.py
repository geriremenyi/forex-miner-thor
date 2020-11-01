from marshmallow import Schema, fields, post_load

from forex_miner_thor.model.instrument import Instrument
from forex_miner_thor.model.candle import CandleSchema


class InstrumentSchema(Schema):
    instrument = fields.Str()
    granularity = fields.Str()
    candles = fields.List(fields.Nested(CandleSchema))

    @post_load
    def make_instrument(self, data,  **kwargs):
        return Instrument(**data)

