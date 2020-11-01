import unittest

from marshmallow import fields

from forex_miner_thor.model.instrument import InstrumentSchema


class TestInstrumentSchema(unittest.TestCase):
    def test_init(self):
        # Arrange
        # Act
        instrument_schema = InstrumentSchema()

        # Assert
        self.assertEqual(type(instrument_schema.fields["instrument"]), fields.String)
        self.assertEqual(type(instrument_schema.fields["granularity"]), fields.String)
        self.assertEqual(type(instrument_schema.fields["candles"]), fields.List)

    def test_make(self):
        # Arrange
        instrument = 'EUR_USD'
        granularity = 'H1'
        candles = []

        # Act
        instrument_schema = InstrumentSchema()
        instrument_make = instrument_schema.make_instrument(
            {
                'instrument': instrument,
                'granularity': granularity,
                'candles': candles
            }
        )

        # Assert
        self.assertEqual(instrument_make.instrument, instrument)
        self.assertEqual(instrument_make.granularity, granularity)
        self.assertEqual(instrument_make.candles, candles)


if __name__ == '__main__':
    unittest.main()